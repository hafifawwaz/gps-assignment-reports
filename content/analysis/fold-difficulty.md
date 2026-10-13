---
source: report/analysis/fold-difficulty.md
date: 23-07-2026
kind: analysis
comments: true
generated: 2026-10-13T20:05:33
---

# Fold difficulty

<p class="doc-meta"><span class="chip chip-analysis">Analysis</span> <span class="chip chip-date">23-07-2026</span></p>

Per-fold accuracy of the [Final model](final-model.md) (grouped CV):

| Fold | Total | Building | Street | Open space |
|---:|---:|---:|---:|---:|
| 0 | 0.635 | 0.896 | 0.162 | 0.368 |
| 1 | 0.665 | 0.906 | 0.324 | 0.333 |
| 2 | 0.801 | 0.897 | 0.667 | 0.658 |
| 3 | 0.791 | 0.877 | 0.622 | 0.718 |
| 4 | 0.685 | 0.906 | 0.368 | 0.378 |

Building is stable (0.877-0.906). Street swings more than 4× (0.162-0.667) with nearly equal support per fold (36-38 stays), so the swings are not a sample-size effect. Folds 0 and 1 are hardest for **every** type and for Random Forest and XGBoost too ([ML ceiling check, row level](ml-ceiling-row-level.md)): difficulty belongs to which stays land in a fold, not to one type.

Part of [Error analysis](../threads/error-analysis.md).


<div class="backlinks" markdown>

**Linked from** [Confusion matrix](confusion-matrix.md) · [Error analysis](../threads/error-analysis.md) · [ML ceiling check, row level](ml-ceiling-row-level.md) · [RQ2 diagnostics and RQ3 ceiling check](../progress/progress-23-07-2026.md)

</div>
