---
source: report/notes/candidate-selection.md
date: 25-07-2026
kind: note
comments: true
generated: 2026-10-13T20:30:42
---

# Candidate selection

<p class="doc-meta"><span class="chip chip-note">Note</span> <span class="chip chip-date">25-07-2026</span></p>

A stay's candidates are the entities that intersect the **union of its GPS points, each buffered by `R_buffer`**. The same radius is used inside [f_distribution](f-distribution.md), on purpose.

`R_buffer = 10 m` was chosen over 15 m: [R_buffer: 10 m vs 15 m](../analysis/r-buffer-10m-vs-15m.md). Because the search area is a union of buffered points, more points mean a larger area: [Downsampling shrinks the candidate search area](../analysis/candidate-search-area.md).

Part of [Framework overview](framework-overview.md).


<div class="backlinks" markdown>

**Linked from** [Assignment framework](../threads/assignment-framework.md) · [Downsampling shrinks the candidate search area](../analysis/candidate-search-area.md) · [Framework overview](framework-overview.md) · [R_buffer: 10 m vs 15 m](../analysis/r-buffer-10m-vs-15m.md)

</div>
