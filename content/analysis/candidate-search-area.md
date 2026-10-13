---
source: report/analysis/candidate-search-area.md
date: 29-07-2026
kind: analysis
comments: true
generated: 2026-10-13T16:57:34
---

# Downsampling shrinks the candidate search area

<p class="doc-meta"><span class="chip chip-analysis">Analysis</span> <span class="chip chip-date">29-07-2026</span></p>

At the same `R_buffer` = 10 m, raw-density scoring produced **36,110** candidate rows vs **22,484** downsampled: 1.6× more for the same 907 stays.

Not a bug: [Candidate selection](../notes/candidate-selection.md) buffers the union of a stay's points, and about 9.9× more points cover more ground even though the radius is unchanged. Downsampling reduces the effective search area, not just the point count. Worth remembering if `R_buffer` sensitivity is revisited ([R_buffer: 10 m vs 15 m](r-buffer-10m-vs-15m.md)).

Part of [Raw-density refit](raw-density-refit.md).


<div class="backlinks" markdown>

**Linked from** [Candidate selection](../notes/candidate-selection.md) · [Chapter 5: Results](../progress/ch5-results.md) · [Does downsampling matter?](../progress/progress-29-07-2026.md) · [Downsampling to MILES density](../notes/downsampling-to-miles-density.md) · [Raw-density refit](raw-density-refit.md)

</div>
