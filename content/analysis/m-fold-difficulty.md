---
source: report/analysis/m-fold-difficulty.md
date: 23-07-2026
kind: analysis
comments: true
generated: 2026-11-06T11:37:20
---

# Fold difficulty

<p class="doc-meta"><span class="chip chip-analysis">Analysis</span> <span class="chip chip-project">Master</span> <span class="chip chip-date">23-07-2026</span></p>

Cross-validation splits the data into 5 test sets (folds). This table shows the [Final model](m-final-model.md)'s accuracy in each one:

| Fold | Total | Building | Street | Open space |
|---:|---:|---:|---:|---:|
| 0 | 0.753 | 0.916 | 0.649 | 0.395 |
| 1 | 0.706 | 0.887 | 0.459 | 0.432 |
| 2 | 0.736 | 0.915 | 0.500 | 0.474 |
| 3 | 0.714 | 0.868 | 0.486 | 0.513 |
| 4 | 0.680 | 0.877 | 0.361 | 0.436 |

Building accuracy hardly changes (0.868-0.916). Street accuracy changes almost 2 times (0.361-0.649). Each fold has about the same number of street stays (36-38), so the changes do not come from small numbers. For street, the two hardest folds (4 and 1) are also the two hardest overall, and the two best (0 and 2) are the two best overall. So for street, the difficulty comes from which stays end up in a fold.

Open space does not follow this pattern. It is low in every fold (0.395-0.513), and its weakest fold (0) is the best fold overall. So its weakness is not a fold effect.

Random Forest and XGBoost agree only in part ([ML ceiling check, row level](m-ml-ceiling-row-level.md)): fold 1 is among the two hardest for all three models, and fold 2 is among the two best for all three. The other folds change places between models.

Part of [Error analysis](../threads/m-error-analysis.md).


<div class="backlinks" markdown>

**Linked from** [Confusion matrix](m-confusion-matrix.md) · [Error analysis](../threads/m-error-analysis.md) · [ML ceiling check, row level](m-ml-ceiling-row-level.md) · [RQ2 diagnostics and RQ3 ceiling check](../progress/m-progress-23-07-2026.md)

</div>
