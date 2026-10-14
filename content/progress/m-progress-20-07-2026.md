---
source: report/progress/m-progress-20-07-2026.md
date: 20-07-2026
kind: progress
comments: true
generated: 2026-10-14T14:44:07
---

# ML baseline

<p class="doc-meta"><span class="chip chip-progress">Progress</span> <span class="chip chip-project">Master</span> <span class="chip chip-date">20-07-2026</span></p>

Sensei's question: could machine-learning models such as Random Forest or XGBoost do much better? If yes, that would show how far the simple model is from the best possible result.

- **Result at the time.** Random Forest did a little better (+3.8 percentage points in cross-validation, CV: testing on data the model did not learn from). XGBoost was about the same as the simple model. All tree models scored 100% on their own training data, which means they memorized it: [ML baseline, stay level (superseded)](../analysis/m-ml-baseline-stay-level.md).
- **GPS spread.** σ (how spread out the GPS points are) was one of the most important inputs for both tree models, even though it has only a small weight in the simple model: [Sigma in tree importance](../analysis/m-sigma-tree-importance.md).
- **Decision.** The tree models were not adopted, because they cannot give a clear probability for each place.

This comparison was later replaced by a fairer one in [RQ2 diagnostics and RQ3 ceiling check](m-progress-23-07-2026.md).


<div class="backlinks" markdown>

**Linked from** [Complexity and transfer](../threads/m-complexity-and-transfer.md) · [RQ2 diagnostics and RQ3 ceiling check](m-progress-23-07-2026.md) · [Thesis summary](../threads/m-thesis-summary.md)

</div>
