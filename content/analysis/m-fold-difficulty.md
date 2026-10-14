---
source: report/analysis/m-fold-difficulty.md
date: 23-07-2026
kind: analysis
comments: true
generated: 2026-10-14T14:44:07
---

# Fold difficulty

<p class="doc-meta"><span class="chip chip-analysis">Analysis</span> <span class="chip chip-project">Master</span> <span class="chip chip-date">23-07-2026</span></p>

Cross-validation splits the data into 5 test sets (folds). This table shows the [Final model](m-final-model.md)'s accuracy in each one:

| Fold | Total | Building | Street | Open space |
|---:|---:|---:|---:|---:|
| 0 | 0.635 | 0.896 | 0.162 | 0.368 |
| 1 | 0.665 | 0.906 | 0.324 | 0.333 |
| 2 | 0.801 | 0.897 | 0.667 | 0.658 |
| 3 | 0.791 | 0.877 | 0.622 | 0.718 |
| 4 | 0.685 | 0.906 | 0.368 | 0.378 |

Building accuracy hardly changes (0.877-0.906). Street accuracy changes by more than 4 times (0.162-0.667). Each fold has about the same number of street stays (36-38), so the changes do not come from small numbers. Folds 0 and 1 are the hardest for **every** type, and also for Random Forest and XGBoost ([ML ceiling check, row level](m-ml-ceiling-row-level.md)). So the difficulty comes from which stays end up in a fold, not from one place type.

Part of [Error analysis](../threads/m-error-analysis.md).


<div class="backlinks" markdown>

**Linked from** [Confusion matrix](m-confusion-matrix.md) · [Error analysis](../threads/m-error-analysis.md) · [ML ceiling check, row level](m-ml-ceiling-row-level.md) · [RQ2 diagnostics and RQ3 ceiling check](../progress/m-progress-23-07-2026.md)

</div>
