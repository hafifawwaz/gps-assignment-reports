---
source: report/notes/m-downsampling-to-miles-density.md
date: 25-07-2026
kind: note
comments: true
generated: 2026-10-14T14:44:07
---

# Downsampling to MILES density

<p class="doc-meta"><span class="chip chip-note">Note</span> <span class="chip chip-project">Master</span> <span class="chip chip-date">25-07-2026</span></p>

The survey phones recorded a GPS point about every metre. MILES records far fewer points. If the model learned from the dense survey data, it would not fit MILES well. So before scoring, the survey data is thinned out (downsampled) to the typical MILES density of **0.967 points per minute**.

For a stay that lasts $d$ minutes, the number of points to keep is


$$n = \max\big(1,\ \mathrm{round}(d \times 0.967)\big)$$


but never more than the stay originally had. The first and the last point are always kept. The other $n - 2$ points are picked at random from the points in between, and no point is picked twice.

For the 907 stays, this leaves **17,010** points out of the original **167,615**, about 9.9 times fewer.

Does thinning change the result? A test with the full data says no: [Raw-density refit](../analysis/m-raw-density-refit.md). Thinning also makes the search area around each stay smaller: [Downsampling shrinks the candidate search area](../analysis/m-candidate-search-area.md).

Part of [Ground truth data](../threads/m-ground-truth-data.md).


<div class="backlinks" markdown>

**Linked from** [Ground truth data](../threads/m-ground-truth-data.md) · [Ground truth dataset](m-ground-truth-dataset.md) · [Raw-density refit](../analysis/m-raw-density-refit.md)

</div>
