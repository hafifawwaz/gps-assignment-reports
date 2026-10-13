---
source: report/analysis/sigma-tree-importance.md
date: 23-07-2026
kind: analysis
comments: true
generated: 2026-10-13T16:57:34
---

# Sigma in tree importance

<p class="doc-meta"><span class="chip chip-analysis">Analysis</span> <span class="chip chip-date">23-07-2026</span></p>

[sigma](../notes/sigma.md) has a modest logit coefficient (+0.78 in the [Final model](final-model.md)) yet tree models rank it at or near the top:

| Run | σ rank |
|---|---|
| Stay-level, RF impurity / XGBoost gain | 2nd / 2nd |
| Stay-level, out-of-fold permutation | RF 1st, XGBoost 2nd |
| Row-level, RF impurity | 1st (0.31) |
| Row-level, XGBoost gain | 2nd, after the building indicator |

Either positional dispersion carries nonlinear, threshold-like signal a single linear term cannot express, or the trees use it as a proxy for something correlated (stay duration, environment). σ² did not survive in the logit ([Stepwise VIF elimination](stepwise-vif-elimination.md)), but other forms (log, threshold) were not tried.

In the row-level run the trees learn type-specific boundaries straight from the one-hot type indicator; `f_distance` ranks last in both.

Sources: [ML baseline, stay level (superseded)](ml-baseline-stay-level.md), [ML ceiling check, row level](ml-ceiling-row-level.md). Part of [Chapter 5: Results](../progress/ch5-results.md).


<div class="backlinks" markdown>

**Linked from** [Chapter 5: Results](../progress/ch5-results.md) · [ML baseline](../progress/progress-20-07-2026.md) · [ML baseline, stay level (superseded)](ml-baseline-stay-level.md) · [ML ceiling check, row level](ml-ceiling-row-level.md) · [sigma](../notes/sigma.md)

</div>
