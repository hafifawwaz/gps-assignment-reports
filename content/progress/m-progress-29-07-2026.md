---
source: report/progress/m-progress-29-07-2026.md
date: 29-07-2026
kind: progress
comments: true
generated: 2026-10-20T15:44:29
---

# Does downsampling matter?

<p class="doc-meta"><span class="chip chip-progress">Progress</span> <span class="chip chip-project">Master</span> <span class="chip chip-date">29-07-2026</span></p>

Sensei's question. Before fitting, the survey data is downsampled: points are removed so that it looks like MILES. Does this step change the result? To check, the [Final model](../analysis/m-final-model.md) was fitted again on the full survey data, without downsampling.

- **Downsampling does no harm.** On unseen data, the downsampled data gives 0.719 ± 0.032 and the full data gives 0.719 ± 0.033. The model is more stable with downsampled data (condition number 1,681 vs 4,849) ([Raw-density refit](../analysis/m-raw-density-refit.md)).
- **α changes.** With the full data, the fit keeps improving up to the search limit, α = 6, instead of stopping at 2.764. But it changes very little over a wide range of α, so neither value is pinned down well ([Raw-density alpha profile](../analysis/m-raw-density-alpha-profile.md)).
- **Side finding.** Downsampling also makes the search area around each stay smaller, so each stay gets fewer candidates ([Downsampling shrinks the candidate search area](../analysis/m-candidate-search-area.md)).


<div class="backlinks" markdown>

**Linked from** [Complexity and transfer](../threads/m-complexity-and-transfer.md) · [Ground truth data](../threads/m-ground-truth-data.md) · [Thesis summary](../threads/m-thesis-summary.md)

</div>
