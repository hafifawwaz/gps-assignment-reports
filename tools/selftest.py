"""Scanner self-test: plant one case per rule in a temp folder and check each is caught.

    python tools/selftest.py

All planted values are fabricated. This file is exempt from the text rules (see
rules/text_scan_exempt.txt) because it necessarily contains strings that trip them.
"""

from __future__ import annotations

import sys
import tempfile
from pathlib import Path

import scan as scanner

# rule expected -> (file name, content)
BLOCK_CASES = {
    "data-file-type": ("points.csv", "a,b\n1,2\n"),
    "file-too-large": ("big.png", "x" * (scanner.MAX_BYTES + 1)),
    "latlon-pair": ("a.md", "The stop was at 34.39750, 132.47530 that day.\n"),
    "lonlat-pair": ("b.md", "x=132.71352 y=34.40128\n"),
    "utm-pair": ("c.md", "centroid (293411.2, 3809877.5) in the projected CRS\n"),
    "wkt-geometry": ("d.md", "geometry: POINT (1.5 2.5)\n"),
    "geojson-coordinates": ("e.json", '{"type": "Point", "coordinates": [1, 2]}\n'),
    "gt-stay-id": ("f.md", "Worst case was stay 99Z_s10_12Pro3 in the survey.\n"),
    "id-value": ("g.md", "filtered to participant_id == 99Z only\n"),
    "windows-path": ("h.md", r"saved to C:\Users\someone\data\out" + "\n"),
    "unix-home-path": ("i.md", "saved to /home/someone/data/out\n"),
    "email-address": ("j.md", "contact someone@example.org for access\n"),
    "github-token": ("k.md", "token ghp_" + "a1B2" * 9 + "\n"),
    "aws-key": ("l.md", "AKIA" + "ABCDEFGHIJKLMNOP" + "\n"),
    "private-key": ("m.md", "-----BEGIN RSA PRIVATE KEY-----\n"),
    "env-file": ("n.md", "values are read from the .env file\n"),
    "local-settings": ("o.md", "see settings.local.json\n"),
    "participant-code": ("t.md", "| 07C | 13 | Some cafe | manual verification |\n"),
}
WARN_CASES = {
    "licensed-data-file": ("p.md", "loaded from ZENRIN_buildings_2020.shp\n"),
    "titled-person": ("q.md", "as suggested by Prof. Example\n"),
    "honorific-person": ("r.md", "Example-sensei asked about this\n"),
    "entity-id": ("s.md", "assigned to B_1234567 instead\n"),
}
# Ordinary report prose that must NOT trip any blocking rule.
CLEAN = (
    "CV accuracy 0.7155 ± 0.0758 vs 0.6968 ± 0.0623; alpha 2.4297 vs 4.6159.\n"
    "167,615 points downsampled to 17,010; 36,110 vs. 22,484 candidate rows at R_buffer=10m.\n"
    "Grouped by (participant_id, stop_sequence), 907 stays, condition number 1,373.4.\n"
    "See `report/memory/29-07-2026/raw_density_final_model_refit.md` and Section 3.3.3.\n"
    "open_space stayed the stuck weak point    (0.40–0.47 range across every variant), at this point (3 of 5 folds).\n"
)


def main() -> int:
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    failures = []
    with tempfile.TemporaryDirectory() as tmp:
        root = Path(tmp)
        for name, content in list(BLOCK_CASES.values()) + list(WARN_CASES.values()):
            (root / name).write_text(content, encoding="utf-8")
        (root / "clean.md").write_text(CLEAN, encoding="utf-8")
        findings = scanner.scan(root)

    for level, cases in (("BLOCK", BLOCK_CASES), ("WARN", WARN_CASES)):
        for rule, (name, _) in cases.items():
            hit = any(f.level == level and f.rule == rule and f.path == name for f in findings)
            print(f"  {'ok  ' if hit else 'MISS'} {level:5} {rule:22} {name}")
            if not hit:
                failures.append(rule)
    false_pos = [f for f in findings if f.path == "clean.md" and f.level == "BLOCK"]
    print(f"  {'ok  ' if not false_pos else 'FAIL'} clean prose raises no blocking finding")
    for f in false_pos:
        print(f"       {f.rule}: {f.excerpt}")
    if failures or false_pos:
        print(f"selftest: FAIL ({len(failures)} missed, {len(false_pos)} false positives)")
        return 1
    print(f"selftest: PASS ({len(BLOCK_CASES)} blocking + {len(WARN_CASES)} warning cases caught)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
