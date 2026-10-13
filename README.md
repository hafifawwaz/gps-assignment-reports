# GPS Staypoint Assignment: research reports

**Read the reports here: <https://hafifawwaz.github.io/gps-assignment-reports/>**

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

Dates are written
`DD-MM-YYYY`. A light/dark switch is in the header.

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
