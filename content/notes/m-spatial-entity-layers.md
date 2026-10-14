---
source: report/notes/m-spatial-entity-layers.md
date: 25-07-2026
kind: note
comments: true
generated: 2026-10-14T14:44:07
---

# Spatial entity layers

<p class="doc-meta"><span class="chip chip-note">Note</span> <span class="chip chip-project">Master</span> <span class="chip chip-date">25-07-2026</span></p>

The map is split into three types of place (entities). They never overlap, so every spot on the map belongs to exactly one type.

| Type | Source |
|---|---|
| Building | ZTOWN building outlines, used as they are |
| Street | MAPPLE street center lines, widened to the width of each street |
| Open space | Everything that is left after streets and buildings are removed from the street network area |

Two details matter later:

- Streets are stored as many short pieces next to each other. Because of this, a stay on a street has many street candidates around it, and this hurts the model: [Candidate density bias toward building](../analysis/m-candidate-density-bias.md).
- Underground shopping arcades are not in ZTOWN. Stays recorded there had no matching building, so they were removed: [Ground truth drop list](../analysis/m-drop-list.md).

Part of [Ground truth data](../threads/m-ground-truth-data.md).


<div class="backlinks" markdown>

**Linked from** [Candidate density bias toward building](../analysis/m-candidate-density-bias.md) · [Ground truth data](../threads/m-ground-truth-data.md) · [Ground truth drop list](../analysis/m-drop-list.md) · [Study area](m-study-area.md)

</div>
