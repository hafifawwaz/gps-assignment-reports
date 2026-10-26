"""Rebuild dashboard/content/ from report/.

Reads report/ (never writes to it), restructures it into the site layout, rewrites links and
copies the figures the published pages reference. Only writes under dashboard/.

    python tools/sync.py --mode stage   # everything not explicitly skipped (for the dry run)
    python tools/sync.py --mode final   # only files approved with an unchanged hash
"""

from __future__ import annotations

import argparse
import hashlib
import html
import json
import posixpath
import re
import sys
from dataclasses import dataclass
from datetime import datetime
from pathlib import Path, PurePosixPath
from urllib.parse import unquote

import yaml
from markdown.extensions.toc import slugify as toc_slugify

from paths import (
    APPROVALS,
    CONTENT,
    FIGURES,
    MANUSCRIPT,
    ONLINE,
    REPO,
    REPORT,
    RULES,
    SITE,
    SYNC_MANIFEST,
)

# report subfolder -> (site folder, page status, nav label, one-line description)
# Only these folders are read. report/group/, zemi/, archives/, _processed/ and the
# _archive-v*.zip files (old structures) are not listed, so they are never published.
SECTIONS = {  # also the tab order (Home and Map are in the header, not tabs)
    "threads": ("threads", "thread", "Threads",
                "Hubs by theme: the thesis summary and the doctoral plan, then one list of notes per theme."),
    "progress": ("progress", "progress", "Progress",
                 "Dated updates for sensei, and slide exports."),
    "plans": ("plans", "plan", "Plans", "Work items by status: on-going, planned, on hold, done."),
    "concepts": ("concepts", "concept", "Concepts",
                 "Settled pieces of the work: method, data, interpretation, discussion."),
    "analysis": ("analysis", "analysis", "Analysis", "Raw analysis output: tables, numbers and diagnostics."),
    "notes": ("notes", "note", "Notes", "Loose notes and sketches, not part of the main line yet."),
    "inbox": ("inbox", "inbox", "Inbox", "Open items not yet settled with sensei."),
}
CATCHUP = "catchup.md"  # report/catchup.md: the hand-written hero text on the home page
BOARD = "plans/board.md"  # an Obsidian Kanban board: its lanes (## headings) are the plans' statuses
HOME_CARDS = 5  # newest items shown per section on the home page
HOME_COLUMNS = ("threads", "progress", "concepts", "analysis")  # the four home columns
HOME_BELOW = ("plans", "inbox")  # full-width rows under the home columns
GENERIC_PDF_NAMES = {"slides-export", "slides", "main", "export"}
IMAGE_EXT = {".png", ".jpg", ".jpeg", ".svg", ".gif", ".webp"}
# Never offered for publishing, whatever the user picks.
PDF_NEVER = ("literature", "template")

DATE_RE = re.compile(r"\d{2}-\d{2}-\d{4}")
FENCE_RE = re.compile(r"^\s*(```|~~~)")
CODE_SPAN_RE = re.compile(r"(`+[^`\n]+?`+)")
IMG_RE = re.compile(r"!\[([^\]]*)\]\(\s*<?([^)>]+?)>?(?:\s+\"[^\"]*\")?\s*\)")
WIKI_IMG_RE = re.compile(r"!\[\[([^\]|]+)(?:\|[^\]]*)?\]\]")
LINK_RE = re.compile(r"(?<!!)\[([^\]]+)\]\(\s*<?([^)>]+?)>?(?:\s+\"[^\"]*\")?\s*\)")
WIKI_RE = re.compile(r"(?<!!)\[\[([^\]|#]+)(#[^\]|]*)?(?:\|([^\]]*))?\]\]")
EXTERNAL_RE = re.compile(r"^(https?:|mailto:|#)", re.I)
CODE_REPORT_RE = re.compile(r"^report/[\w./ -]+\.md$")
CODE_FIGURE_RE = re.compile(r"^(?:analysis/figures/)?([\w.-]+\.(?:png|jpe?g|svg|gif|webp))$", re.I)


class SyncError(Exception):
    pass


@dataclass
class Source:
    path: Path  # absolute source file
    key: str  # repo-relative posix path, e.g. report/analysis/final-model.md
    dest: str  # content-relative posix path, e.g. timeline/19-07-2026.md
    section: str  # notes / progress / inbox / analysis / hero
    status: str  # summary / detail / inbox / note
    date: str | None  # DD-MM-YYYY if one appears in the path
    sha256: str = ""
    state: str = "ask"  # include / skip / ask
    title: str = ""


def sha256_file(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def slug(part: str) -> str:
    stem, dot, ext = part.rpartition(".")
    if not dot:
        stem, ext = part, ""
    stem = re.sub(r"[^a-z0-9_-]+", "-", stem.lower()).strip("-") or "page"
    return f"{stem}.{ext.lower()}" if ext else stem


def date_key(date: str | None) -> tuple:
    """Sort key for DD-MM-YYYY (undated last when sorting newest-first)."""
    if not date:
        return (0, 0, 0)
    d, m, y = date.split("-")
    return (int(y), int(m), int(d))


def load_approvals() -> dict:
    if APPROVALS.exists():
        return json.loads(APPROVALS.read_text(encoding="utf-8"))
    return {}


def discover() -> list[Source]:
    approvals = load_approvals()
    out: list[Source] = []
    seen: dict[str, str] = {}
    for section, (folder, status, _, _blurb) in SECTIONS.items():
        base = REPORT / section
        if not base.is_dir():
            continue
        for p in sorted(base.rglob("*.md")):
            if p.name.lower() == "readme.md":
                continue  # navigation notes, never published
            if p == REPORT / BOARD:
                continue  # the plans board becomes the Plans index page (below)
            rel = p.relative_to(base)
            dest = PurePosixPath(folder, *[slug(part) for part in rel.parts]).as_posix()
            key = p.relative_to(REPO).as_posix()
            if dest in seen:
                raise SyncError(f"{key} and {seen[dest]} both map to {dest}")
            seen[dest] = key
            m = DATE_RE.search(rel.as_posix())
            src = Source(p, key, dest, section, status, m.group(0) if m else front_matter_date(p))
            src.sha256 = sha256_file(p)
            entry = approvals.get(key)
            if entry and entry.get("sha256") == src.sha256:
                src.state = entry["decision"]
            src.title = read_title(p)
            out.append(src)
    for path, dest, section in ((REPORT / CATCHUP, "index.md", "hero"), (REPORT / BOARD, "plans/index.md", "board")):
        if path.is_file():
            src = Source(path, path.relative_to(REPO).as_posix(), dest, section, section, None)
            src.sha256 = sha256_file(path)
            entry = approvals.get(src.key)
            if entry and entry.get("sha256") == src.sha256:
                src.state = entry["decision"]
            src.title = "Plans" if section == "board" else read_title(path)
            out.append(src)
    return out


BOARD_LANE_RE = re.compile(r"^##\s+(.+?)\s*$")
BOARD_CARD_RE = re.compile(r"^\s*- \[[ xX]\]\s+(.+?)\s*$")


def board_lanes(path: Path) -> list[tuple[str, list[str]]]:
    """[(lane, [card text])] from an Obsidian Kanban board; the %% settings %% block is dropped."""
    lanes: list[tuple[str, list[str]]] = []
    text = OBS_COMMENT_RE.sub("", strip_front_matter(source_text(path)))
    for line in text.split("\n"):
        m = BOARD_LANE_RE.match(line)
        if m:
            lanes.append((m.group(1), []))
            continue
        m = BOARD_CARD_RE.match(line)
        if m and lanes:
            lanes[-1][1].append(m.group(1))
    return lanes


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8-sig").replace("\r\n", "\n")


REDACTED: dict[str, int] = {}  # source key -> replacements made in the published copy


def load_redactions() -> list[tuple[re.Pattern, str]]:
    """rules/redactions.txt: 'regex<TAB>replacement' per line. Local only (gitignored)."""
    path = RULES / "redactions.txt"
    out = []
    if path.exists():
        for line in path.read_text(encoding="utf-8").splitlines():
            line = line.strip()
            if not line or line.startswith("#"):
                continue
            pattern, tab, replacement = line.partition("\t")
            if not tab:
                raise SyncError(f"redactions.txt: expected 'regex<TAB>replacement', got: {line}")
            out.append((re.compile(pattern.strip()), replacement.strip()))
    return out


def source_text(path: Path) -> str:
    """A report source as it will be published: censored in memory, the file itself is never touched."""
    text = read_text(path)
    total = 0
    for pattern, replacement in load_redactions():
        text, n = pattern.subn(lambda m, r=replacement: r, text)
        total += n
    REDACTED[path.relative_to(REPO).as_posix()] = total
    return text


FRONT_DATE_RE = re.compile(r"^date:\s*['\"]?(\d{2}-\d{2}-\d{4})", re.M)


def front_matter_date(path: Path) -> str | None:
    """`date: DD-MM-YYYY` from a note's front matter (Obsidian property), if present."""
    text = read_text(path)
    if text.startswith("---\n"):
        end = text.find("\n---", 4)
        m = FRONT_DATE_RE.search(text[4:end if end != -1 else 0])
        if m:
            return m.group(1)
    return None


def strip_front_matter(text: str) -> str:
    if text.startswith("---\n"):
        end = text.find("\n---\n", 4)
        if end != -1:
            return text[end + 5 :]
    return text


TITLE_DATE_RE = re.compile(r"\s*[(\[]?\b\d{2}-\d{2}-\d{4}\b[)\]]?")


def clean_title(title: str) -> str:
    """Drop the date from a title; it is already shown as a chip beside it."""
    out = TITLE_DATE_RE.sub("", title).strip(" -\u2013\u2014:,")
    return out or title


def short_titles() -> dict[str, str]:
    """site/titles.txt: short display titles for the published copy (sources keep theirs)."""
    out = {}
    path = SITE / "titles.txt"
    if path.exists():
        for line in path.read_text(encoding="utf-8").splitlines():
            key, tab, title = line.partition("\t")
            if tab and not key.startswith("#"):
                out[key.strip()] = title.strip()
    return out


def source_dates() -> dict[str, str]:
    """site/dates.txt: a DD-MM-YYYY date for sources whose path has none (e.g. a PDF export)."""
    out = {}
    path = SITE / "dates.txt"
    if path.exists():
        for line in path.read_text(encoding="utf-8").splitlines():
            key, tab, date = line.partition("	")
            if tab and not key.startswith("#") and DATE_RE.fullmatch(date.strip()):
                out[key.strip()] = date.strip()
    return out


def redirects() -> dict[str, str]:
    """site/redirects.txt: 'old<TAB>new' content paths of pages that moved."""
    out = {}
    path = SITE / "redirects.txt"
    if path.exists():
        for line in path.read_text(encoding="utf-8").splitlines():
            old, tab, new = line.partition("\t")
            if tab and not old.startswith("#"):
                out[old.strip()] = new.strip()
    return out


def read_title(path: Path) -> str:
    override = short_titles().get(path.relative_to(REPO).as_posix())
    if override:
        return override
    for line in strip_front_matter(source_text(path)).splitlines():
        if line.startswith("# "):
            return clean_title(line[2:].strip())
    return pretty(path.stem)


def pdf_candidates() -> list[str]:
    """The user's own PDF exports under manuscript/. Paths only; files are never opened."""
    if not MANUSCRIPT.is_dir():
        return []
    out = []
    for p in sorted(MANUSCRIPT.rglob("*.pdf")):
        rel = p.relative_to(MANUSCRIPT)
        if rel.parts[0] in PDF_NEVER:
            continue
        out.append(p.relative_to(REPO).as_posix())
    return out


class Renderer:
    def __init__(self, all_sources: list[Source], selected: list[Source]):
        self.by_path = {s.path.resolve(): s for s in selected}
        self.stems: dict[str, list[Source]] = {}
        for s in all_sources:
            self.stems.setdefault(s.path.stem.lower(), []).append(s)
        self.selected_keys = {s.key for s in selected}
        self.figures: dict[str, Path] = {}  # published name -> source file
        self.figure_users: dict[str, set[str]] = {}  # published name -> dest pages
        self.page_dests = {s.dest for s in selected}
        self.edges: set[tuple[str, str]] = set()  # (from dest, to dest)
        self.errors: list[str] = []
        # PDFs picked in this run: resolved path -> {"name", "cover", "title", "dest"}. A note that
        # embeds one (![[...pdf]]) becomes its page; otherwise it gets a page of its own.
        self.pdfs: dict[Path, dict] = {}
        self.pdf_embedders: dict[Path, str] = {}  # PDF -> dest of the first page embedding it
        # every note under report/ by file name, so a link to an unpublished one still shows its title
        self.unpublished = {p.stem.lower(): p for p in sorted(REPORT.rglob("*.md")) if p.name.lower() != "readme.md"}

    # -- target resolution ------------------------------------------------
    def _find(self, src: Source, target: str) -> Path | None:
        target = unquote(target.split("#", 1)[0].split("?", 1)[0]).strip()
        if not target:
            return None
        for base in (src.path.parent, REPO, REPORT, FIGURES):
            cand = base / target
            try:
                if cand.is_file():
                    return cand.resolve()
            except OSError:
                pass
        return None

    def _find_wiki(self, src: Source, name: str) -> Path | None:
        name = name.strip()
        for cand in (name, name + ".md"):
            hit = self._find(src, cand)
            if hit:
                return hit
        matches = self.stems.get(Path(name).stem.lower(), [])
        if len(matches) == 1:
            return matches[0].path.resolve()
        return self._pdf(src, name)

    def _pdf(self, src: Source, target: str) -> Path | None:
        """A picked PDF named by path or (if unique among the picked ones) by file name."""
        hit = self._find(src, target)
        if hit in self.pdfs:
            return hit
        named = [q for q in self.pdfs if q.name.lower() == Path(target.strip()).name.lower()]
        return named[0] if len(named) == 1 else None

    def _rel(self, dest: str, target_dest: str) -> str:
        return posixpath.relpath(target_dest, posixpath.dirname(dest) or ".")

    def _figure(self, path: Path, dest: str) -> str | None:
        if path.suffix.lower() not in IMAGE_EXT:
            return None
        if FIGURES.resolve() not in path.parents and REPORT.resolve() not in path.parents:
            return None
        name = slug(path.name)
        known = self.figures.get(name)
        if known and known != path:
            self.errors.append(f"two different figures are both named {name}: {known} / {path}")
        self.figures[name] = path
        self.figure_users.setdefault(name, set()).add(dest)
        return self._rel(dest, f"figures/{name}")

    def _link(self, path: Path | None, dest: str) -> str | None:
        if path is None:
            return None
        hit = self.by_path.get(path)
        if hit:
            if dest in self.page_dests and dest != hit.dest:
                self.edges.add((dest, hit.dest))
            return self._rel(dest, hit.dest)
        pdf = self.pdfs.get(path)
        if pdf and pdf["dest"]:
            if dest in self.page_dests and dest != pdf["dest"]:
                self.edges.add((dest, pdf["dest"]))
            return self._rel(dest, pdf["dest"])
        return self._figure(path, dest)

    # -- rewriting --------------------------------------------------------
    def _text(self, text: str, src: Source, dest: str) -> str:
        def embed(alt: str, target: str) -> str:
            if target.lower().endswith(".pdf"):
                pdf_path = self._pdf(src, target)
                if pdf_path is None:  # not picked in this run: no file to show
                    return alt or Path(target).stem
                self.pdf_embedders.setdefault(pdf_path, dest)
                pdf = self.pdfs[pdf_path]
                # raw HTML is not rewritten by MkDocs, and a page x.md is served as x/ (directory URLs)
                up = "" if dest.endswith("index.md") else "../"
                href = up + self._rel(dest, f"progress/files/{pdf['name']}")
                img = up + self._rel(dest, f"progress/files/{pdf['cover']}")
                # HTML, so the link rewriting that runs after embeds leaves these paths alone
                return (f'<a class="md-button md-button--primary" href="{href}" target="_blank">Open the PDF in a new tab</a>\n\n'
                        f'<a href="{href}" target="_blank"><img class="pdf-cover" src="{img}" '
                        f'alt="First page of {html.escape(pdf["title"])}"></a>')
            path = self._find(src, target) or self._find(src, Path(target).name)
            link = self._figure(path, dest) if path else None
            if not link:
                self.errors.append(f"{src.key}: figure not found: {target}")
                return alt
            return f"![{alt}]({link})"

        def img(m):
            target = m.group(2).strip()
            return m.group(0) if EXTERNAL_RE.match(target) else embed(m.group(1), target)

        def wiki_img(m):
            target = m.group(1).strip()
            note = self._find_wiki(src, target)
            if note and note.suffix.lower() == ".md":  # ![[note]] embeds a note: link to it instead
                new = self._link(note, dest)
                return f"[{target}]({new})" if new else target
            return embed("", target)

        def link(m):
            label, target = m.group(1), m.group(2).strip()
            if EXTERNAL_RE.match(target):
                return m.group(0)
            anchor = "#" + target.split("#", 1)[1] if "#" in target else ""
            new = self._link(self._find(src, target), dest)
            return f"[{label}]({new}{anchor})" if new else label

        def wiki(m):
            name, anchor, alias = m.group(1), m.group(2) or "", m.group(3)
            if anchor:  # [[note#Heading]] -> the id MkDocs gives that heading
                anchor = "#" + toc_slugify(anchor[1:].strip(), "-")
            path = self._find_wiki(src, name)
            hit = self.by_path.get(path) if path else None
            label = alias or (hit.title if hit else name.strip())  # [[file-name]] shows the note's title
            if not alias and path in self.pdfs:
                label = self.pdfs[path]["title"]
            new = self._link(path, dest)
            if not new and not alias:  # a note that is not published (e.g. in archives/): its title, as text
                other = self.unpublished.get(Path(name.strip()).stem.lower())
                label = read_title(other) if other else Path(name.strip()).stem
            return f"[{label}]({new}{anchor})" if new else label

        text = IMG_RE.sub(img, text)
        text = WIKI_IMG_RE.sub(wiki_img, text)
        text = LINK_RE.sub(link, text)
        return WIKI_RE.sub(wiki, text)

    def _code(self, span: str, src: Source, dest: str, in_link: bool) -> str:
        inner = span.strip("`").strip()
        if in_link:
            return span
        if CODE_REPORT_RE.match(inner):
            new = self._link(self._find(src, inner), dest)
            return f"[{span}]({new})" if new else span
        m = CODE_FIGURE_RE.match(inner)
        if m and (FIGURES / m.group(1)).is_file():
            new = self._figure((FIGURES / m.group(1)).resolve(), dest)
            return f"[{span}]({new})" if new else span
        return span

    def body(self, src: Source, dest: str) -> str:
        """Source markdown with links rewritten for a page living at `dest`."""
        out, fenced = [], False
        for line in obsidian_to_site(strip_front_matter(source_text(src.path))).split("\n"):
            if FENCE_RE.match(line):
                fenced = not fenced
                out.append(line)
                continue
            if fenced:
                out.append(line)
                continue
            stripped = line.strip()
            if len(stripped) > 4 and stripped.startswith("$$") and stripped.endswith("$$"):
                out += ["", stripped, ""]
                continue
            parts = CODE_SPAN_RE.split(line)
            for i, part in enumerate(parts):
                if i % 2:
                    parts[i] = self._code(part, src, dest, parts[i - 1].endswith("["))
                else:
                    parts[i] = self._text(part, src, dest)
            out.append("".join(parts))
        return "\n".join(out).strip() + "\n"


OBS_COMMENT_RE = re.compile(r"%%.*?%%", re.S)
OBS_BLOCK_ID_RE = re.compile(r"\s\^[A-Za-z0-9-]+$")
OBS_HIGHLIGHT_RE = re.compile(r"(?<![=\w])==(?=\S)(.+?)(?<=\S)==(?!=)")
CALLOUT_RE = re.compile(r"^>\s*\[!(\w+)\]([+-]?)\s*(.*)$")
CALLOUT_TYPES = {
    "note": "note", "info": "info", "todo": "info", "tip": "tip", "hint": "tip", "important": "tip",
    "success": "success", "check": "success", "done": "success", "question": "question", "help": "question",
    "faq": "question", "warning": "warning", "caution": "warning", "attention": "warning",
    "failure": "failure", "fail": "failure", "missing": "failure", "danger": "danger", "error": "danger",
    "bug": "bug", "example": "example", "quote": "quote", "cite": "quote", "abstract": "abstract",
    "summary": "abstract", "tldr": "abstract",
}


def obsidian_to_site(text: str) -> str:
    """Make Obsidian-flavoured markdown render the same on the site.

    %%comments%% are dropped (never published), callouts become admonitions, ==highlights==
    become <mark>, and trailing block ids (^abc) are removed. Code blocks are left alone.
    """
    text = OBS_COMMENT_RE.sub("", text)
    out, fenced, callout = [], False, False
    for line in text.split("\n"):
        if FENCE_RE.match(line) and not callout:
            fenced = not fenced
        if fenced:
            out.append(line)
            continue
        m = CALLOUT_RE.match(line)
        if m:
            kind = CALLOUT_TYPES.get(m.group(1).lower(), "note")
            marker = {"-": "???", "+": "???+"}.get(m.group(2), "!!!")
            title = m.group(3).strip().replace('"', "'")
            out += ["", f'{marker} {kind} "{title}"' if title else f"{marker} {kind}"]
            callout = True
            continue
        if callout:
            if line.startswith(">"):
                out.append("    " + line[1:].removeprefix(" "))
                continue
            callout = False
            out.append("")
        line = OBS_BLOCK_ID_RE.sub("", line)
        out.append(OBS_HIGHLIGHT_RE.sub(r"<mark>\1</mark>", line))
    return "\n".join(out)


STATUS_LABEL = {"thread": "Thread", "concept": "Concept", "note": "Note", "plan": "Plan", "progress": "Progress",
                "inbox": "Inbox", "analysis": "Analysis", "hero": "Catch-up", "board": "Plans"}


# `project:` in a note's front matter -> a chip, so thesis and dissertation notes stay apart on the site
PROJECT_LABEL = {"m": "Master", "d": "Doctoral"}
FRONT_PROJECT_RE = re.compile(r"^project:\s*['\"]?([\w-]+)", re.M)


def front_matter_project(path: Path) -> str | None:
    """`project: <name>` from a note's front matter (Obsidian property), if present."""
    text = read_text(path)
    if text.startswith("---\n"):
        end = text.find("\n---", 4)
        m = FRONT_PROJECT_RE.search(text[4:end if end != -1 else 0])
        if m:
            return m.group(1)
    return None


def chips(status: str, date: str | None, pdf: bool = False, project: str | None = None,
          lane: str | None = None) -> str:
    out = [f'<span class="chip chip-{status}">{STATUS_LABEL[status]}</span>']
    if lane:  # a plan's status: the board lane it sits in
        out.append(f'<span class="chip chip-lane">{html.escape(lane)}</span>')
    if project:
        out.append(f'<span class="chip chip-project">{html.escape(PROJECT_LABEL.get(project, project))}</span>')
    if pdf:
        out.append('<span class="chip chip-pdf">PDF</span>')
    if date:
        out.append(f'<span class="chip chip-date">{date}</span>')
    return " ".join(out)


def page(src: Source, renderer: Renderer, titles: dict[str, str] | None = None, pdf: bool = False,
         lane: str | None = None) -> str:
    lines = renderer.body(src, src.dest).split("\n")
    h1 = next((i for i, line in enumerate(lines) if line.startswith("# ")), None)
    if h1 is None:
        lines.insert(0, f"# {pretty(src.path.stem)}")
        h1 = 0
    lines[h1] = "# " + (short_titles().get(src.key) or clean_title(lines[h1][2:].strip()))
    extra = ["", f'<p class="doc-meta">{chips(src.status, src.date, pdf=pdf, project=front_matter_project(src.path), lane=lane)}</p>']
    if src.status == "inbox":
        extra += ["", '!!! question "For discussion"', "    Rough draft and open questions. Not yet reviewed."]
    lines[h1 + 1 : h1 + 1] = extra
    incoming = sorted({a for a, b in renderer.edges if b == src.dest}, key=lambda d: (titles or {}).get(d, d))
    if incoming:
        links = " · ".join(f"[{(titles or {}).get(d, d)}]({renderer._rel(src.dest, d)})" for d in incoming)
        lines += ["", '<div class="backlinks" markdown>', "", f"**Linked from** {links}", "", "</div>"]
    front = {"source": src.key, "date": src.date or "", "kind": src.status, "comments": True}
    head = "---\n" + yaml.safe_dump(front, sort_keys=False, allow_unicode=True) + "generated: {generated}\n---\n\n"
    return head + "\n".join(lines).strip() + "\n"


def first_paragraph(body: str) -> str:
    para: list[str] = []
    for line in body.split("\n"):
        if line.startswith(("#", "|", "!!!", "<", ">", "```", "---")):
            if para:
                break
            continue
        if not line.strip():
            if para:
                break
            continue
        para.append(line)
    return " ".join(para)


@dataclass
class Item:
    """One entry in a section listing: a report page or a PDF page."""

    title: str
    dest: str
    status: str
    date: str | None
    pdf: bool = False


def first_page_png(pdf: Path) -> bytes:
    """Page 1 of a picked PDF as a PNG (only the cover is shown on the site)."""
    import pymupdf as fitz

    with fitz.open(pdf) as doc:
        page = doc[0]
        zoom = 1600 / page.rect.width
        return page.get_pixmap(matrix=fitz.Matrix(zoom, zoom), alpha=False).tobytes("png")


def cards(items: list[Item], base: str, rel) -> list[str]:
    """Material 'grid cards' block. Links are markdown, so mkdocs --strict validates them."""
    out = ['<div class="grid cards" markdown>', ""]
    for it in items:
        out += [f"-   <p class=\"doc-meta\">{chips(it.status, None, it.pdf)}</p>", "",
                f"    **[{it.title}]({rel(base, it.dest)})**", ""]
    return out + ["</div>", ""]


def pretty(stem: str) -> str:
    return re.sub(r"[_-]+", " ", DATE_RE.sub("", stem)).strip().lower() or stem


def build(mode: str, pdfs: list[str]) -> dict:
    sources = discover()
    if mode == "final":
        selected = [s for s in sources if s.state == "include"]
    else:
        selected = [s for s in sources if s.state != "skip"]
    r = Renderer(sources, selected)
    rel = r._rel
    files: dict[str, bytes | str] = {}  # content-relative path -> text (with {generated}) or bytes

    hero = next((s for s in selected if s.section == "hero"), None)
    board = next((s for s in selected if s.section == "board"), None)
    listing: dict[str, list[Item]] = {name: [] for name in SECTIONS}
    pages = [s for s in selected if s.section not in ("hero", "board")]

    # PDFs picked in this run. Each is shown under Progress: on the page of the note that embeds it
    # (![[...pdf]]), or else on a page of its own.
    allowed = set(pdf_candidates())
    picked: list[tuple[Path, str, str | None]] = []
    for item in pdfs:
        item = item.replace("\\", "/")
        if item not in allowed:
            raise SyncError(f"not an offerable PDF (must be one of the user's own exports under manuscript/): {item}")
        source = Path(item)
        generic = source.stem.lower() in GENERIC_PDF_NAMES
        name = slug(f"{source.parent.name}-{source.name}" if generic else source.name)
        m = DATE_RE.search(item)
        date = m.group(0) if m else source_dates().get(item)
        title = short_titles().get(item) or pretty(source.parent.name if generic else source.stem)
        r.pdfs[(REPO / item).resolve()] = {"name": name, "cover": f"{name[:-4]}-page1.png", "title": title, "dest": None}
        picked.append(((REPO / item).resolve(), item, date))
    for s in pages:  # pass 0: find which note embeds which PDF
        r.body(s, s.dest)
    for path, info in r.pdfs.items():
        info["dest"] = r.pdf_embedders.get(path) or f"progress/{info['name'][:-4]}.md"
    pdf_pages = set(r.pdf_embedders.values())
    r.edges.clear()

    # The plans board: each lane is a status, each card links to a plan
    lanes = board_lanes(board.path) if board else []
    lane_of: dict[str, str] = {}  # plan dest -> lane
    for lane, lane_cards in lanes:
        for card in lane_cards:
            for m in WIKI_RE.finditer(card):
                hit = r.by_path.get(r._find_wiki(board, m.group(1)))
                if hit:
                    lane_of.setdefault(hit.dest, lane)

    for s in pages:  # first pass: collect the link graph so every page can list what links to it
        r.body(s, s.dest)
    titles = {s.dest: s.title for s in pages}
    for s in pages:
        files[s.dest] = page(s, r, titles, pdf=s.dest in pdf_pages, lane=lane_of.get(s.dest))
        listing[s.section].append(Item(s.title, s.dest, s.status, s.date, pdf=s.dest in pdf_pages))

    for path, item, date in picked:
        info = r.pdfs[path]
        files[f"progress/files/{info['name']}"] = path.read_bytes()
        files[f"progress/files/{info['cover']}"] = first_page_png(path)
        if path in r.pdf_embedders:
            continue  # shown on the embedding note's page
        dest, title, name, cover = info["dest"], info["title"], info["name"], info["cover"]
        if dest in files:
            raise SyncError(f"a picked PDF and another page both map to {dest}")
        files[dest] = "\n".join([
            "---", "kind: progress", "comments: true", "generated: {generated}", "---", "",
            f"# {title}", "", f'<p class="doc-meta">{chips("progress", date, pdf=True)}</p>', "",
            f"[Open the PDF in a new tab](files/{name}){{ .md-button .md-button--primary target=_blank }}", "",
            f"[![First page of {title}](files/{cover}){{ .pdf-cover }}](files/{name}){{ target=_blank }}", "",
        ])
        listing["progress"].append(Item(title, dest, "progress", date, pdf=True))

    for items in listing.values():
        items.sort(key=lambda it: (date_key(it.date), it.dest), reverse=True)

    # Section index pages
    for section, (folder, _, heading, blurb) in SECTIONS.items():
        base = f"{folder}/index.md"
        lines = [f"# {heading}", "", blurb, ""]
        items = listing[section]
        if section == "plans" and lanes:  # the board, one column per lane
            lines += ['<div class="plan-board" markdown>', ""]
            for lane, lane_cards in lanes:
                lines += ['<div class="plan-lane" markdown>', "", f"### {lane}", ""]
                lines += [f"- {r._text(card, board, base)}" for card in lane_cards] or ['<p class="empty">Nothing here.</p>']
                lines += ["", "</div>", ""]
            lines += ["</div>", ""]
            loose = [it for it in items if it.dest not in lane_of]
            if loose:
                lines += ["## Not on the board", ""] + cards(loose, base, rel)
        elif not items:
            lines.append("*Nothing published here yet.*")
        else:  # grouped by year, then month (each card keeps its own date chip)
            for year, months in by_year_month(items):
                lines += [f"## {year}", ""]
                for month, group in months:
                    if month:
                        lines += [f"### {month}", ""]
                    lines += cards(group, base, rel)
        files[base] = "\n".join(lines).rstrip() + "\n"

    # Home: hero + newest items of each section
    home = ["---", "hide:", "  - navigation", "  - toc", "---", "", '<div class="hero" markdown>', "",
            "# Catch-up summary", ""]
    if hero:
        # the file's own top heading, if any, becomes a bold lead line under the fixed hero title
        home += [f"**{clean_title(line[2:].strip())}**" if line.startswith("# ") else line
                 for line in r.body(hero, "index.md").split("\n")]
    else:
        home += ['<p class="empty">No summary written yet. Add one in <code>report/catchup.md</code>.</p>']
    home += ["", "</div>", ""]
    def home_col(section: str, cls: str) -> list[str]:
        folder, _, heading, blurb = SECTIONS[section]
        items = listing[section]
        out = [f'<div class="{cls}" markdown>', "", f"## [{heading}]({folder}/index.md) {{ .home-section }}", "",
               f'<p class="section-blurb">{blurb}</p>', ""]
        if section == "plans" and lanes:  # one line per lane of the board
            for lane, lane_cards in lanes:
                if lane_cards:
                    out += [f"- **{lane}**: " + " · ".join(r._text(c, board, "index.md") for c in lane_cards)]
            out += ["", f"[The board]({folder}/index.md){{ .more }}", ""]
        elif items:
            for it in items[:HOME_CARDS]:
                pdf = ' <span class="chip chip-pdf">PDF</span>' if it.pdf else ""
                out += [f"- [{it.title}]({rel('index.md', it.dest)}){pdf}"]
            out += ["", f"[All {len(items)}]({folder}/index.md){{ .more }}", ""]
        else:
            out += ['<p class="empty">Nothing yet.</p>', ""]
        return out + ["</div>", ""]

    home += ['<div class="home-columns" markdown>', ""]
    for section in HOME_COLUMNS:
        home += home_col(section, "home-col")
    home += ["</div>", ""]
    for section in HOME_BELOW:
        home += home_col(section, "home-col home-below")
    home += [read_text(SITE / "about.md").strip(), ""]
    files["index.md"] = "\n".join(home)

    # Knowledge map: nodes = published pages, links = resolved links between them
    nodes = [{"id": s.dest, "title": s.title, "kind": s.status, "date": s.date or "",
              "url": "../" + s.dest[:-3] + "/"} for s in pages]
    for it in listing["progress"]:
        if it.pdf and it.dest not in {s.dest for s in pages}:
            nodes.append({"id": it.dest, "title": it.title, "kind": "progress", "date": it.date or "",
                          "url": "../" + it.dest[:-3] + "/", "pdf": True})
    graph = {"nodes": nodes, "links": [{"source": a, "target": b} for a, b in sorted(r.edges)]}
    files["map/graph.json"] = json.dumps(graph, ensure_ascii=False, indent=1).encode("utf-8")
    files["map/index.md"] = "\n".join([
        "---", "hide:", "  - navigation", "  - toc", "---", "",
        "# Knowledge map", "",
        '<p class="section-blurb">Every published note and the links between them. Drag to move, scroll to zoom, '
        'hover to see a note\'s neighbours, click to open it. Larger dots have more links.</p>', "",
        '<div class="kmap-legend">'
        '<span class="kmap-key hub">Thread</span>'
        '<span class="kmap-key" style="--dot: var(--c-chip-progress)">Progress</span>'
        '<span class="kmap-key" style="--dot: var(--c-node-plan)">Plan</span>'
        '<span class="kmap-key" style="--dot: var(--c-node-note)">Concept</span>'
        '<span class="kmap-key" style="--dot: var(--c-chip-analysis)">Analysis</span>'
        '<span class="kmap-key" style="--dot: var(--c-node-scratch)">Note</span>'
        '<span class="kmap-key" style="--dot: var(--c-red)">Inbox</span></div>', "",
        '<div id="kmap" class="kmap"></div>', "",
        '<script src="https://cdn.jsdelivr.net/npm/d3@7/dist/d3.min.js"></script>',
        '<script src="../javascripts/kmap.js"></script>', "",
    ])

    # Figures referenced by a published page (copied; there is no gallery page)
    for name in sorted(r.figures):
        files[f"figures/{name}"] = r.figures[name].read_bytes()

    # Redirect pages at addresses that moved (site/redirects.txt), so links shared earlier keep working
    for old, new in redirects().items():
        if old in files or new not in files:
            continue  # the old page still exists, or the target is not published in this run
        old_dir, new_dir = old[:-3], new[:-3]
        href = posixpath.relpath(new_dir, old_dir) + "/"
        title = html.escape(titles.get(new, new))
        files[f"{old_dir}/index.html"] = "\n".join([
            "<!doctype html>", '<html lang="en">', "<head>", '<meta charset="utf-8">',
            '<meta name="viewport" content="width=device-width, initial-scale=1">',
            f"<title>{title} (moved)</title>", '<meta name="robots" content="noindex">',
            f'<link rel="canonical" href="{href}">', f'<meta http-equiv="refresh" content="0; url={href}">',
            "</head>", "<body>", f'<p>This page moved to <a href="{href}">{title}</a>.</p>', "</body>", "</html>", "",
        ]).encode("utf-8")

    # Hand-written static assets (css/js) that mkdocs expects inside docs_dir
    static = SITE / "static"
    for p in sorted(static.rglob("*")):
        if p.is_file():
            files[p.relative_to(static).as_posix()] = p.read_bytes()

    if r.errors:
        raise SyncError("\n".join(r.errors))

    write_content(files)
    write_nav(listing)

    manifest = {
        "mode": mode,
        "sources": [
            {"key": s.key, "dest": s.dest, "state": s.state, "sha256": s.sha256, "published": s in selected,
             "redactions": REDACTED.get(s.key, 0)}
            for s in sources
        ],
        "figures": sorted(r.figures),
        "pdfs": pdfs,
        "pdf_candidates": sorted(allowed),
    }
    SYNC_MANIFEST.write_text(json.dumps(manifest, indent=2), encoding="utf-8")
    return manifest


GENERATED_RE = re.compile(r"^generated: .*$", re.M)


def write_content(files: dict[str, bytes | str]) -> None:
    """Make content/ exactly equal to `files`. `generated` only moves when a page really changed."""
    now = datetime.now().strftime("%Y-%m-%dT%H:%M:%S")
    for rel, data in files.items():
        target = CONTENT / rel
        target.parent.mkdir(parents=True, exist_ok=True)
        if isinstance(data, str):
            if target.exists():
                old = target.read_text(encoding="utf-8")
                if GENERATED_RE.sub("generated: {generated}", old, count=1) == data:
                    continue
            data = data.replace("{generated}", now, 1).encode("utf-8")
        if not target.exists() or target.read_bytes() != data:
            target.write_bytes(data)
    wanted = {(CONTENT / rel).resolve() for rel in files}
    for p in sorted(CONTENT.rglob("*"), reverse=True):
        if p.is_file() and p.resolve() not in wanted:
            p.unlink()
        elif p.is_dir() and not any(p.iterdir()):
            try:
                p.rmdir()
            except OSError:
                pass  # OneDrive sometimes holds an empty folder; it is harmless and git ignores it


MONTHS = ["January", "February", "March", "April", "May", "June", "July", "August", "September",
          "October", "November", "December"]


def by_year_month(items: list) -> list:
    """[(year, [(month name, items)])], newest first; undated items go last under 'Undated'."""
    years: dict = {}
    for it in items:
        if it.date:
            _, m, y = it.date.split("-")
            years.setdefault(y, {}).setdefault(int(m), []).append(it)
        else:
            years.setdefault("Undated", {}).setdefault(0, []).append(it)
    order = sorted((y for y in years if y != "Undated"), reverse=True) + (["Undated"] if "Undated" in years else [])
    return [(y, [(MONTHS[m - 1] if m else "", years[y][m]) for m in sorted(years[y], reverse=True)]) for y in order]


def nav_label(it) -> str:
    """Sidebar label: the page title in lowercase (the date is shown on the page itself)."""
    label = it.title if len(it.title) <= 60 else it.title[:57].rsplit(" ", 1)[0] + "…"
    return label.lower() + (" (pdf)" if it.pdf else "")


def write_nav(listing: dict) -> None:
    """site/mkdocs.yml = the hand-edited mkdocs.base.yml + a nav generated from what is published."""
    # Home stays first so the theme knows the home page, but its tab is hidden (the header title and
    # logo link home); the map has a header button (site/overrides/partials/header.html), not a tab.
    nav: list = [{"Home": "index.md"}]
    for section, (folder, _, heading, _blurb) in SECTIONS.items():
        entries: list = [f"{folder}/index.md"]
        items = listing[section]
        for year, months in by_year_month(items):
            year_entries: list = []
            for month, group in months:
                links = [{nav_label(it): it.dest} for it in group]
                year_entries += [{month: links}] if month else links
            entries.append({year: year_entries})
        nav.append({heading: entries})
    text = "# GENERATED by tools/sync.py. Edit mkdocs.base.yml instead.\nINHERIT: mkdocs.base.yml\n"
    text += yaml.safe_dump({"nav": nav}, sort_keys=False, allow_unicode=True)
    target = SITE / "mkdocs.yml"
    if not target.exists() or target.read_text(encoding="utf-8") != text:
        target.write_text(text, encoding="utf-8", newline="\n")


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--mode", choices=["stage", "final"], required=True)
    ap.add_argument("--pdf", action="append", default=[], help="repo-relative PDF to publish (repeatable)")
    args = ap.parse_args()
    assert ONLINE in CONTENT.parents
    try:
        manifest = build(args.mode, args.pdf)
    except SyncError as e:
        print(f"SYNC FAILED\n{e}", file=sys.stderr)
        return 1
    n = sum(1 for s in manifest["sources"] if s["published"])
    print(f"sync ({args.mode}): {n} of {len(manifest['sources'])} report files, "
          f"{len(manifest['figures'])} figures, {len(manifest['pdfs'])} PDFs")
    return 0


if __name__ == "__main__":
    sys.exit(main())
