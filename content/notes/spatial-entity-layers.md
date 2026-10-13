---
source: report/notes/spatial-entity-layers.md
date: 25-07-2026
kind: note
comments: true
generated: 2026-10-13T20:05:33
---

# Spatial entity layers

<p class="doc-meta"><span class="chip chip-note">Note</span> <span class="chip chip-date">25-07-2026</span></p>

Three entity types, mutually exclusive by construction:

| Type | Source |
|---|---|
| Building | ZTOWN footprints, unmodified |
| Street | MAPPLE centerlines, buffered by street width |
| Open space | The residual area after erasing streets and buildings from the street-network extent |

Streets are drawn as many short adjacent segments, which matters later: [Candidate density bias toward building](../analysis/candidate-density-bias.md). Underground arcades are not in ZTOWN, which is why some stays had to be dropped: [Ground truth drop list](../analysis/drop-list.md).

Part of [Ground truth data](../threads/ground-truth-data.md).


<div class="backlinks" markdown>

**Linked from** [Candidate density bias toward building](../analysis/candidate-density-bias.md) · [Ground truth data](../threads/ground-truth-data.md) · [Ground truth drop list](../analysis/drop-list.md) · [Study area](study-area.md)

</div>
