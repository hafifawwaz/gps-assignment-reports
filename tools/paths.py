"""Shared locations for the publish tools. Everything is derived from this file's position."""

from pathlib import Path

ONLINE = Path(__file__).resolve().parents[1]  # dashboard/  (the public git repo)
REPO = ONLINE.parent  # research repo root   (never pushed)

REPORT = REPO / "report"
FIGURES = REPO / "analysis" / "figures"
MANUSCRIPT = REPO / "manuscript"

CONTENT = ONLINE / "content"  # generated markdown + figures
SITE = ONLINE / "site"  # mkdocs config, landing template, theme overrides
BUILD = ONLINE / "docs"  # built site, served by GitHub Pages from main:/docs
TOOLS = ONLINE / "tools"
RULES = TOOLS / "rules"

APPROVALS = TOOLS / "approved.json"  # local only (gitignored): per-file include/skip + hash
SCAN_STAMP = TOOLS / ".scan_pass.json"  # local only: proof the current tree passed the scan
SYNC_MANIFEST = TOOLS / ".last_sync.json"  # local only: what the last sync produced
