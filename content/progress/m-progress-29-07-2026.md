---
source: report/progress/m-progress-29-07-2026.md
date: 29-07-2026
kind: progress
comments: true
generated: 2026-10-14T14:44:07
---

# Does downsampling matter?

<p class="doc-meta"><span class="chip chip-progress">Progress</span> <span class="chip chip-project">Master</span> <span class="chip chip-date">29-07-2026</span></p>

Sensei's question. Before fitting, the survey data is thinned out to look like MILES (downsampling). Does this step change the result? To check, the [Final model](../analysis/m-final-model.md) was fitted again on the full survey data, without thinning.

- **Downsampling does no harm.** On unseen data, the thinned data gives 0.716 ± 0.076 and the full data gives 0.697 ± 0.062. The model is also more stable with thinned data (condition number 1,373 vs 2,865) ([Raw-density refit](../analysis/m-raw-density-refit.md)).
- **α changes.** With the full data, the best α is 4.6159 instead of 2.4297. But the fit changes very little over a wide range of α, so this value is less certain ([Raw-density alpha profile](../analysis/m-raw-density-alpha-profile.md)).
- **Side finding.** Downsampling also makes the search area around each stay smaller, so each stay gets fewer candidates ([Downsampling shrinks the candidate search area](../analysis/m-candidate-search-area.md)).


<div class="backlinks" markdown>

**Linked from** [Complexity and transfer](../threads/m-complexity-and-transfer.md) · [Ground truth data](../threads/m-ground-truth-data.md) · [Thesis summary](../threads/m-thesis-summary.md)

</div>
