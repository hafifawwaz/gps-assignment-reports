# GPS Staypoint Assignment: research reports

**Read the reports here: <https://hafihafiyyan.github.io/gps-assignment-reports/>**

MSc research by **Hafiyyan Hilmy Fawwaz**, Urban Transportation and Planning Lab, Hiroshima University.

A GPS staypoint rarely tells you which place a person actually visited: positional error is often
larger than the gap between a building, the street in front of it and the open space beside it.
This research builds a probabilistic framework that assigns each staypoint to an urban spatial
entity (building, street or open space) under explicit positional uncertainty, instead of snapping
it to the nearest one. The framework is calibrated on a controlled field-survey ground truth and
then applied to a large GPS trajectory dataset.

## How to read the site

| Section | What is there |
|---|---|
| **Home** | A short catch-up summary of current work, and the newest items from every section. |
| **Notes** | Small pieces of progress: method, data, interpretation, discussion. |
| **Progress** | Hubs ready to present: the thesis summary, one hub per chapter, dated updates for seminar (zemi) and supervision, and slide exports. |
| **Inbox** | Open items not yet settled in supervision. |
| **Analysis** | Raw analysis output: model tables, numbers and diagnostics, one finding per note. |
| **Map** | A knowledge graph of every note and the links between them. Start from *Thesis summary*. |

Every page has its own link, so a single report can be shared directly. Dates are written
`DD-MM-YYYY`. A light/dark switch is in the header.

**For my supervisor:** the newest Progress entry is the update to read before a meeting; Inbox
lists what I would like to ask. Comments and questions are welcome, by email or in person.

**For lab members:** Progress is the best entry point. Analysis holds the full numbers behind
each summary if you want to check a result or reuse an approach.

**For everyone else:** this is ongoing MSc work. Results can change between updates and have not
been peer reviewed, so please ask before citing or reusing them.

## What is and is not in this repository

This repository contains **only the published reports and the tooling that builds the site**.
The analysis code and all data (GPS trajectories, the field-survey ground truth, and licensed map
layers) are kept private and are never published here.

| Folder | Contents |
|---|---|
| `content/` | The report pages and figures, generated from my private notes. Not edited by hand. |
| `site/` | Site configuration and design (MkDocs Material, colours and fonts from my slide deck). |
| `docs/` | The built website that GitHub Pages serves. |
| `tools/` | The publishing tools: `sync.py` builds `content/`, `scan.py` checks it, `publish.py` runs the steps. |

### How a report gets published

1. Reports are written once, in Obsidian, in my private research folder.
2. `tools/sync.py` copies them into `content/`, rewrites links, and censors identifiers in the copy
   only (the originals are untouched).
3. `tools/scan.py` blocks the publish if it finds data files, coordinates, participant or device
   identifiers, local paths, addresses or keys. `python tools/selftest.py` checks that every rule
   still catches a planted example.
4. Each new or changed report is approved individually before anything is pushed.
