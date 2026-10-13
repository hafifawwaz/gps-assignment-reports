"""Publish flow for the online dashboard: sync -> scan -> build -> dry run -> approve -> commit -> push.

    python tools/publish.py stage [--pdf X.pdf ...]    # dry run with everything not yet skipped
    python tools/publish.py decide include A.md B.md   # record per-file answers (repo-relative paths)
    python tools/publish.py decide skip C.md
    python tools/publish.py final [--pdf X.pdf ...]    # rebuild from approved files only
    python tools/publish.py commit -m "..." [--ack-warnings]
    python tools/publish.py push

`commit` refuses unless the exact tree on disk passed the scanner after a `final` run.
Nothing here ever pushes with --force, touches the research repo's files, or skips the scan.
"""

from __future__ import annotations

import argparse
import json
import subprocess
import sys

import scan as scanner
import sync
from paths import APPROVALS, BUILD, ONLINE, RULES, SCAN_STAMP, SITE

# Kept beside the rules (text-scan exempt) because the trailer contains an address.
ATTRIBUTION = (RULES / "commit_trailer.txt").read_text(encoding="utf-8").strip()


def git(*args: str, check: bool = True) -> str:
    res = subprocess.run(["git", "-C", str(ONLINE), *args], capture_output=True, text=True, encoding="utf-8")
    if check and res.returncode != 0:
        raise SystemExit(f"git {' '.join(args)} failed:\n{res.stderr or res.stdout}")
    return res.stdout


def build_site() -> None:
    res = subprocess.run(
        [sys.executable, "-m", "mkdocs", "build", "--strict", "--clean", "-f", str(SITE / "mkdocs.yml")],
        capture_output=True, text=True, encoding="utf-8", errors="replace",
    )
    if res.returncode != 0:
        raise SystemExit(f"BUILD FAILED (mkdocs build --strict)\n{res.stdout}\n{res.stderr}")
    (BUILD / ".nojekyll").write_text("", encoding="utf-8")
    print("build: ok (mkdocs build --strict)")


def run(mode: str, pdfs: list[str]) -> int:
    SCAN_STAMP.unlink(missing_ok=True)
    try:
        manifest = sync.build(mode, pdfs)
    except sync.SyncError as e:
        print(f"SYNC FAILED\n{e}")
        return 1
    n = sum(1 for s in manifest["sources"] if s["published"])
    print(f"sync ({mode}): {n} of {len(manifest['sources'])} report files, "
          f"{len(manifest['figures'])} figures, {len(manifest['pdfs'])} PDFs")

    # Scan the sources of the site before building, so blocked content never reaches the build.
    pre = scanner.scan(ONLINE, exclude=("docs/",))
    if any(f.level == "BLOCK" for f in pre):
        print(scanner.report(pre))
        print("Stopped before build. Fix the source or review the rule, then run again.")
        return 1
    build_site()
    findings = scanner.scan(ONLINE)
    print(scanner.report(findings))
    blocked = any(f.level == "BLOCK" for f in findings)
    if not blocked:
        warns = sum(1 for f in findings if f.level == "WARN")
        SCAN_STAMP.write_text(
            json.dumps({"tree": scanner.tree_hash(ONLINE), "warnings": warns, "mode": mode}), encoding="utf-8"
        )
    dry_run(manifest)
    return 1 if blocked else 0


def dry_run(manifest: dict) -> None:
    print("\n=== DRY RUN (nothing committed) ===")
    has_head = subprocess.run(["git", "-C", str(ONLINE), "rev-parse", "HEAD"], capture_output=True).returncode == 0
    status = git("status", "--porcelain", "--untracked-files=all", "--", "content").splitlines()
    added = [ln[3:] for ln in status if ln[:2] in ("??", "A ", "AM")]
    removed = [ln[3:] for ln in status if "D" in ln[:2]]
    changed = [ln[3:] for ln in status if ln[3:] not in added and ln[3:] not in removed]
    for title, group in (("New pages/files", added), ("Changed", changed), ("Removed", removed)):
        print(f"\n{title}: {len(group)}")
        for f in group:
            print(f"  {f}")
    if has_head:
        stat = git("diff", "--stat", "HEAD", "--", "content").strip()
        if stat:
            print("\nDiff summary (content/):\n" + stat)
    files = scanner.list_files(ONLINE)
    total = sum((ONLINE / f).stat().st_size for f in files)
    print(f"\nPublish tree: {len(files)} files, {total / 1e6:.2f} MB")

    ask = [s for s in manifest["sources"] if s["state"] == "ask"]
    inc = [s for s in manifest["sources"] if s["state"] == "include"]
    skip = [s for s in manifest["sources"] if s["state"] == "skip"]
    print(f"\nReport files: {len(inc)} approved (unchanged), {len(skip)} skipped (unchanged), {len(ask)} need an answer")
    for s in ask:
        print(f"  ASK   {s['key']}")
    for s in skip:
        print(f"  skip  {s['key']}")
    censored = [s for s in manifest["sources"] if s["published"] and s.get("redactions")]
    print(f"\nCensored in the published copy only (originals untouched): {len(censored)} file(s)")
    for s in censored:
        print(f"  {s['redactions']} replacement(s)  {s['key']}  ->  content/{s['dest']}")
    print(f"\nPDFs in this run: {len(manifest['pdfs'])} (none are published unless picked now)")
    for p in manifest["pdfs"]:
        print(f"  PICKED {p}")
    print("PDFs that may be offered:")
    for p in manifest["pdf_candidates"]:
        print(f"  {p}")


def decide(decision: str, keys: list[str]) -> int:
    sources = {s.key: s for s in sync.discover()}
    approvals = sync.load_approvals()
    for key in keys:
        key = key.replace("\\", "/")
        if key not in sources:
            print(f"not a publishable report file: {key}")
            return 1
        approvals[key] = {"decision": decision, "sha256": sources[key].sha256}
        print(f"{decision:8} {key}")
    APPROVALS.write_text(json.dumps(approvals, indent=2, sort_keys=True), encoding="utf-8")
    SCAN_STAMP.unlink(missing_ok=True)
    return 0


def final(pdfs: list[str]) -> int:
    pending = [s.key for s in sync.discover() if s.state == "ask"]
    if pending:
        print("These report files still need an include/skip answer:")
        for key in pending:
            print(f"  {key}")
        return 1
    return run("final", pdfs)


def commit(message: str, ack_warnings: bool) -> int:
    if not SCAN_STAMP.exists():
        print("No passing scan on record. Run `publish.py final` first.")
        return 1
    stamp = json.loads(SCAN_STAMP.read_text(encoding="utf-8"))
    if stamp.get("mode") != "final":
        print("The last passing scan was a staging run. Run `publish.py final` first.")
        return 1
    if stamp["tree"] != scanner.tree_hash(ONLINE):
        print("Files changed since the last scan. Run `publish.py final` again.")
        return 1
    if stamp["warnings"] and not ack_warnings:
        print(f"{stamp['warnings']} scanner warnings need the user's explicit OK (--ack-warnings).")
        return 1
    git("add", "-A")
    if not git("status", "--porcelain").strip():
        print("Nothing to commit.")
        return 0
    git("commit", "-m", message, "-m", ATTRIBUTION)
    print(git("log", "-1", "--stat", "--format=%h %s").strip())
    return 0


def push() -> int:
    if git("status", "--porcelain").strip():
        print("Working tree is not clean. Commit through `publish.py commit` first.")
        return 1
    res = subprocess.run(["git", "-C", str(ONLINE), "push", "origin", "main"], capture_output=True, text=True)
    print((res.stdout + res.stderr).strip())
    return res.returncode


def main() -> int:
    for stream in (sys.stdout, sys.stderr):
        stream.reconfigure(encoding="utf-8", errors="replace")
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = ap.add_subparsers(dest="cmd", required=True)
    p = sub.add_parser("stage")
    p.add_argument("--pdf", action="append", default=[])
    p = sub.add_parser("decide")
    p.add_argument("decision", choices=["include", "skip"])
    p.add_argument("keys", nargs="+")
    p = sub.add_parser("final")
    p.add_argument("--pdf", action="append", default=[])
    p = sub.add_parser("commit")
    p.add_argument("-m", "--message", required=True)
    p.add_argument("--ack-warnings", action="store_true")
    sub.add_parser("push")
    args = ap.parse_args()
    if args.cmd == "stage":
        return run("stage", args.pdf)
    if args.cmd == "decide":
        return decide(args.decision, args.keys)
    if args.cmd == "final":
        return final(args.pdf)
    if args.cmd == "commit":
        return commit(args.message, args.ack_warnings)
    return push()


if __name__ == "__main__":
    sys.exit(main())
