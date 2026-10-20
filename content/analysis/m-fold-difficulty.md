---
source: report/analysis/m-fold-difficulty.md
date: 23-07-2026
kind: analysis
comments: true
generated: 2026-10-20T15:22:17
---

# Fold difficulty

<p class="doc-meta"><span class="chip chip-analysis">Analysis</span> <span class="chip chip-project">Master</span> <span class="chip chip-date">23-07-2026</span></p>

Cross-validation splits the data into 5 test sets (folds). This table shows the [Final model](m-final-model.md)'s accuracy in each one:

| Fold | Total | Building | Street | Open space |
|---:|---:|---:|---:|---:|
| 0 | 0.758 | 0.916 | 0.649 | 0.421 |
| 1 | 0.683 | 0.877 | 0.432 | 0.378 |
| 2 | 0.747 | 0.934 | 0.500 | 0.474 |
| 3 | 0.703 | 0.877 | 0.486 | 0.436 |
| 4 | 0.702 | 0.896 | 0.361 | 0.487 |

Building accuracy hardly changes (0.877-0.934). Street accuracy changes almost 2 times (0.361-0.649). Each fold has about the same number of street stays (36-38), so the changes do not come from small numbers. For street, the two hardest folds (4 and 1) are also the two hardest overall, and the two best (0 and 2) are the two best overall. So for street, the difficulty comes from which stays end up in a fold.

Open space does not follow this pattern. It is low in every fold (0.378-0.487), and its best fold (4) is one of the hardest overall. So its weakness is not a fold effect.

Random Forest and XGBoost agree only in part ([ML ceiling check, row level](m-ml-ceiling-row-level.md)): fold 1 is the hardest for all three models, and fold 2 is among the two best for all three. The other folds change places between models.

Part of [Error analysis](../threads/m-error-analysis.md).


<div class="backlinks" markdown>

**Linked from** [Confusion matrix](m-confusion-matrix.md) · [Error analysis](../threads/m-error-analysis.md) · [ML ceiling check, row level](m-ml-ceiling-row-level.md) · [RQ2 diagnostics and RQ3 ceiling check](../progress/m-progress-23-07-2026.md) · [Thesis bug fixes and adopted rerun](../inbox/thesis-bug-fix.md)

</div>
