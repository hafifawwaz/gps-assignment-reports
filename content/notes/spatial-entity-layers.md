---
source: report/notes/spatial-entity-layers.md
date: 25-07-2026
kind: note
comments: true
generated: 2026-10-13T16:57:34
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

Part of [Chapter 3: Data and ground truth](../progress/ch3-data.md).


<div class="backlinks" markdown>

**Linked from** [Candidate density bias toward building](../analysis/candidate-density-bias.md) · [Chapter 3: Data and ground truth](../progress/ch3-data.md) · [Ground truth drop list](../analysis/drop-list.md) · [Study area](study-area.md)

</div>
