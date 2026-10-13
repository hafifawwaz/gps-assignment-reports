---
source: report/notes/downsampling-to-miles-density.md
date: 25-07-2026
kind: note
comments: true
generated: 2026-10-13T20:41:00
---

# Downsampling to MILES density

<p class="doc-meta"><span class="chip chip-note">Note</span> <span class="chip chip-date">25-07-2026</span></p>

The survey devices record a point roughly every metre. MILES is far sparser, so ground-truth points are downsampled to MILES's median density of **0.967 points/minute** before scoring. For a cluster spanning $d$ minutes the target point count is


$$n = \max\big(1,\ \mathrm{round}(d \times 0.967)\big)$$


capped at the cluster's original count. The first and last points are kept; the other $n - 2$ are drawn at random, without replacement, from the interior points.

For the 907 stays this means **17,010** points instead of the raw **167,615** (about 9.9× fewer).

Does it matter? Refitting on raw density says no: [Raw-density refit](../analysis/raw-density-refit.md). It also shrinks the candidate search area as a side effect: [Downsampling shrinks the candidate search area](../analysis/candidate-search-area.md).

Part of [Ground truth data](../threads/ground-truth-data.md).


<div class="backlinks" markdown>

**Linked from** [Ground truth data](../threads/ground-truth-data.md) · [Ground truth dataset](ground-truth-dataset.md) · [Raw-density refit](../analysis/raw-density-refit.md)

</div>
