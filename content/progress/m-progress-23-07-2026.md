---
source: report/progress/m-progress-23-07-2026.md
date: 23-07-2026
kind: progress
comments: true
generated: 2026-10-20T15:44:29
---

# RQ2 diagnostics and RQ3 ceiling check

<p class="doc-meta"><span class="chip chip-progress">Progress</span> <span class="chip chip-project">Master</span> <span class="chip chip-date">23-07-2026</span></p>

Checks on the [Final model](../analysis/m-final-model.md). The model was not fitted again; these checks only look at its results.

- **RQ2, where the model fails.** The model finds 90.0% of building stays, but only 48.6% of street stays and 44.0% of open-space stays. When it gets a street or open space wrong, it usually says "building" ([Confusion matrix](../analysis/m-confusion-matrix.md)). The reason: street stays have the most street candidates around them, and the `share_type` term punishes that ([Candidate density bias toward building](../analysis/m-candidate-density-bias.md)). The difficult test sets are difficult for all three types ([Fold difficulty](../analysis/m-fold-difficulty.md)).
- **RQ3, could another model do better?** On unseen data, the simple model beats Random Forest and XGBoost (0.719 vs 0.708 and 0.703), even though both fit the training data better ([ML ceiling check, row level](../analysis/m-ml-ceiling-row-level.md)). This reverses the result from [ML baseline](m-progress-20-07-2026.md).
- **Appendices.** The thesis appendices were put together from existing data: [Final model correlation matrix](../analysis/m-final-model-correlation-matrix.md), [Self-report form](../notes/m-self-report-form.md), the five experiment groups, and [Ground truth drop list](../analysis/m-drop-list.md). One count did not match, and the thesis has since been corrected: [Ground truth cleaning](../notes/m-ground-truth-cleaning.md).
- **Discussion draft.** A four-part draft of the discussion, which became the Discussion section of the thesis: [Problem and positioning](../threads/m-problem-and-positioning.md) and [Error analysis](../threads/m-error-analysis.md).


<div class="backlinks" markdown>

**Linked from** [Complexity and transfer](../threads/m-complexity-and-transfer.md) · [Error analysis](../threads/m-error-analysis.md) · [Ground truth data](../threads/m-ground-truth-data.md) · [ML baseline](m-progress-20-07-2026.md) · [Problem and positioning](../threads/m-problem-and-positioning.md) · [Thesis summary](../threads/m-thesis-summary.md)

</div>
