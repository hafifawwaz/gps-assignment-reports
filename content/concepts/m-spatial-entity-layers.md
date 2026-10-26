---
source: report/concepts/m-spatial-entity-layers.md
date: 25-07-2026
kind: concept
comments: true
generated: 2026-10-26T20:41:14
---

# Spatial entity layers

<p class="doc-meta"><span class="chip chip-concept">Concept</span> <span class="chip chip-project">Master</span> <span class="chip chip-date">25-07-2026</span></p>

The map is split into three types of place (entities).

| Type | Source |
|---|---|
| Building | Zmap TOWN building outlines, used as they are |
| Street | MAPPLE street center lines, widened to the width of each street |
| Open space | All land that is left after streets and buildings are removed from the street network area. Rivers and other water are not part of it. |

Open space never overlaps the other two types. Buildings and streets do overlap in places, where a widened street reaches into a building outline, so a GPS point can lie inside both. Both map sources start in the old Tokyo Datum and are converted to JGD2000 with the official TKY2JGD grid, then to one projected system (WGS 84 / UTM zone 53N, EPSG:32653).

Two details matter later:

- Streets are stored as many short pieces next to each other. Because of this, a stay on a street has many street candidates around it, and this hurts the model: [Candidate density bias toward building](../analysis/m-candidate-density-bias.md).
- Underground shopping arcades are not in Zmap TOWN. Stays recorded there had no matching building, so they were removed: [Ground truth drop list](../analysis/m-drop-list.md).

Part of [Ground truth data](../threads/m-ground-truth-data.md).


<div class="backlinks" markdown>

**Linked from** [Candidate density bias toward building](../analysis/m-candidate-density-bias.md) · [Ground truth data](../threads/m-ground-truth-data.md) · [Ground truth drop list](../analysis/m-drop-list.md) · [Study area](m-study-area.md)

</div>
