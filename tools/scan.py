"""Deterministic pre-publish scanner. A BLOCK finding stops the publish; a WARN needs an explicit OK.

Scans exactly the files git would commit in dashboard/ (tracked + untracked, minus ignored).
Rules live in tools/rules/ as plain text so they can be extended without touching this file.

    python tools/scan.py                 # scan the publish tree
    python tools/scan.py --root DIR      # scan any folder (used by selftest.py)
"""

from __future__ import annotations

import argparse
import difflib
import hashlib
import json
import re
import subprocess
import sys
from dataclasses import asdict, dataclass
from pathlib import Path

from paths import ONLINE, RULES, SCAN_STAMP

MAX_BYTES = 5 * 1024 * 1024
IMAGE_EXT = {".png", ".jpg", ".jpeg", ".svg", ".gif", ".webp"}
CHANGE_THRESHOLD = 0.5  # warn when less than this fraction of a page survives since last publish
TEXT_EXT = {
    "", ".md", ".html", ".htm", ".json", ".xml", ".txt", ".yml", ".yaml", ".py", ".css", ".js",
    ".toml", ".tsv", ".svg", ".cfg", ".ini",
}


@dataclass
class Finding:
    level: str  # BLOCK / WARN
    rule: str
    path: str
    line: int
    excerpt: str


def rule_lines(name: str) -> list[str]:
    path = RULES / name
    if not path.exists():
        return []
    lines = [ln.strip() for ln in path.read_text(encoding="utf-8").splitlines()]
    return [ln for ln in lines if ln and not ln.startswith("#")]


def load_patterns(name: str) -> list[tuple[str, re.Pattern]]:
    out = []
    for ln in rule_lines(name):
        rule, _, pattern = ln.partition("\t")
        if not pattern:
            raise SystemExit(f"{name}: expected 'rule-name<TAB>regex', got: {ln}")
        out.append((rule.strip(), re.compile(pattern.strip())))
    return out


def git(root: Path, *args: str) -> subprocess.CompletedProcess:
    return subprocess.run(["git", "-C", str(root), *args], capture_output=True)


def list_files(root: Path, exclude: tuple[str, ...] = ()) -> list[str]:
    """Root-relative posix paths of the publish tree."""
    files: list[str] = []
    if (root / ".git").exists():
        res = git(root, "ls-files", "-z", "--cached", "--others", "--exclude-standard")
        if res.returncode != 0:
            raise SystemExit(res.stderr.decode(errors="replace"))
        files = [f for f in res.stdout.decode("utf-8").split("\0") if f and (root / f).is_file()]
    else:
        files = [p.relative_to(root).as_posix() for p in root.rglob("*") if p.is_file() and ".git" not in p.parts]
    return sorted(f for f in set(files) if not f.startswith(exclude))


def tree_hash(root: Path) -> str:
    h = hashlib.sha256()
    for f in list_files(root):
        h.update(f.encode("utf-8") + b"\0" + hashlib.sha256((root / f).read_bytes()).digest())
    return h.hexdigest()


def excerpt(line: str, start: int, end: int, pad: int = 50) -> str:
    a, b = max(0, start - pad), min(len(line), end + pad)
    return ("…" if a else "") + line[a:b].strip() + ("…" if b < len(line) else "")


def head_text(root: Path, rel: str) -> str | None:
    res = git(root, "show", f"HEAD:{rel}")
    return res.stdout.decode("utf-8", errors="replace") if res.returncode == 0 else None


def scan(root: Path = ONLINE, exclude: tuple[str, ...] = ()) -> list[Finding]:
    blocked_ext = {e.lower() for e in rule_lines("blocked_extensions.txt")}
    block = load_patterns("block_patterns.txt")
    warn = load_patterns("warn_patterns.txt")
    names = [(n, re.compile(rf"(?<!\w){re.escape(n)}(?!\w)", re.I)) for n in rule_lines("names.txt")]
    exempt = tuple(rule_lines("text_scan_exempt.txt"))
    has_git = (root / ".git").exists()
    findings: list[Finding] = []

    for rel in list_files(root, exclude):
        path = root / rel
        ext = path.suffix.lower()
        if ext in blocked_ext:
            findings.append(Finding("BLOCK", "data-file-type", rel, 0, ext))
        size = path.stat().st_size
        if size > MAX_BYTES:
            findings.append(Finding("BLOCK", "file-too-large", rel, 0, f"{size / 1e6:.1f} MB"))
            continue
        if rel.startswith("content/figures/") and ext in IMAGE_EXT and has_git and head_text(root, rel) is None:
            findings.append(Finding("WARN", "new-figure", rel, 0, "not in the last publish"))
        if rel.startswith("content/") and ext == ".pdf":
            findings.append(Finding("WARN", "pdf-not-content-scanned", rel, 0, "PDF contents cannot be scanned"))
        if ext not in TEXT_EXT or rel.startswith(exempt):
            continue
        text = path.read_text(encoding="utf-8", errors="replace")
        for no, line in enumerate(text.splitlines(), 1):
            for level, rules in (("BLOCK", block), ("WARN", warn)):
                for rule, pattern in rules:
                    m = pattern.search(line)
                    if m:
                        findings.append(Finding(level, rule, rel, no, excerpt(line, m.start(), m.end())))
            for name, pattern in names:
                m = pattern.search(line)
                if m:
                    findings.append(Finding("WARN", "person-name", rel, no, excerpt(line, m.start(), m.end())))
        if rel.startswith("content/") and ext == ".md" and has_git:
            old = head_text(root, rel)
            if old is not None:
                ratio = difflib.SequenceMatcher(None, old.splitlines(), text.splitlines()).ratio()
                if ratio < CHANGE_THRESHOLD:
                    findings.append(Finding("WARN", "page-mostly-rewritten", rel, 0, f"{(1 - ratio) * 100:.0f}% changed"))
    return findings


def report(findings: list[Finding]) -> str:
    blocks = [f for f in findings if f.level == "BLOCK"]
    warns = [f for f in findings if f.level == "WARN"]
    lines = []
    for title, group in (("BLOCK", blocks), ("WARN", warns)):
        for f in group:
            where = f"{f.path}:{f.line}" if f.line else f.path
            lines.append(f"  {title:5} {f.rule:24} {where}\n        {f.excerpt}")
    verdict = "FAIL" if blocks else "PASS"
    lines.append(f"scan: {verdict}  ({len(blocks)} blocking, {len(warns)} warnings)")
    return "\n".join(lines)


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--root", type=Path, default=ONLINE)
    ap.add_argument("--exclude", action="append", default=[], help="path prefix to skip (repeatable)")
    ap.add_argument("--json", action="store_true")
    args = ap.parse_args()
    findings = scan(args.root.resolve(), tuple(args.exclude))
    if args.json:
        print(json.dumps([asdict(f) for f in findings], indent=2, ensure_ascii=False))
    else:
        print(report(findings))
    blocked = any(f.level == "BLOCK" for f in findings)
    if args.root.resolve() == ONLINE and not args.exclude:
        SCAN_STAMP.unlink(missing_ok=True)
        if not blocked:
            warns = sum(1 for f in findings if f.level == "WARN")
            SCAN_STAMP.write_text(json.dumps({"tree": tree_hash(ONLINE), "warnings": warns}), encoding="utf-8")
    return 1 if blocked else 0


if __name__ == "__main__":
    sys.exit(main())
