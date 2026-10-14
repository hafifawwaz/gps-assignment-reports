---
source: report/analysis/m-candidate-search-area.md
date: 29-07-2026
kind: analysis
comments: true
generated: 2026-10-14T14:44:07
---

# Downsampling shrinks the candidate search area

<p class="doc-meta"><span class="chip chip-analysis">Analysis</span> <span class="chip chip-project">Master</span> <span class="chip chip-date">29-07-2026</span></p>

With the same search distance (`R_buffer` = 10 m), the full survey data produced **36,110** candidate rows, and the thinned data **22,484**. That is 1.6 times more candidates for the same 907 stays.

This is expected. [Candidate selection](../notes/m-candidate-selection.md) draws a circle around every GPS point of a stay. The full data has about 9.9 times more points, and more circles cover more ground, even with the same radius. So thinning the data also makes the search area smaller, not only the number of points. Keep this in mind if the search distance is tested again ([R_buffer: 10 m vs 15 m](m-r-buffer-10m-vs-15m.md)).

Part of [Raw-density refit](m-raw-density-refit.md).


<div class="backlinks" markdown>

**Linked from** [Candidate selection](../notes/m-candidate-selection.md) · [Complexity and transfer](../threads/m-complexity-and-transfer.md) · [Does downsampling matter?](../progress/m-progress-29-07-2026.md) · [Downsampling to MILES density](../notes/m-downsampling-to-miles-density.md) · [Raw-density refit](m-raw-density-refit.md)

</div>
