---
source: report/analysis/m-sigma-tree-importance.md
date: 23-07-2026
kind: analysis
comments: true
generated: 2026-10-20T15:22:17
---

# Sigma in tree importance

<p class="doc-meta"><span class="chip chip-analysis">Analysis</span> <span class="chip chip-project">Master</span> <span class="chip chip-date">23-07-2026</span></p>

[sigma](../notes/m-sigma.md) (how spread out a stay's GPS points are) has a moderate weight in the simple model (+1.02 in the [Final model](m-final-model.md)). But the tree models rank it as one of their most important inputs:

| Run | σ rank |
|---|---|
| Stay-level, RF impurity / XGBoost gain | 1st / 1st |
| Stay-level, out-of-fold permutation | RF 1st, XGBoost 2nd |
| Row-level, RF impurity | 1st (0.34) |
| Row-level, XGBoost gain | 3rd, after the building and street indicators |

(Impurity, gain and permutation are three common ways to measure how much a tree model uses an input.)

There are two possible explanations:

- σ may work like a threshold: below some spread one answer is likely, above it another. One straight-line weight cannot show that.
- The trees may use σ as a stand-in for something related to it, such as how long the stay lasted or the surroundings.

σ² did not survive in the simple model ([Stepwise VIF elimination](m-stepwise-vif-elimination.md)). Other forms, such as log(σ) or a threshold, have not been tried yet.

In the row-level test, the trees learn the differences between types directly from the place-type input. f_distance ranks last in both tree models.

Sources: [ML baseline, stay level (superseded)](m-ml-baseline-stay-level.md), [ML ceiling check, row level](m-ml-ceiling-row-level.md). Part of [Complexity and transfer](../threads/m-complexity-and-transfer.md).


<div class="backlinks" markdown>

**Linked from** [Complexity and transfer](../threads/m-complexity-and-transfer.md) · [ML baseline](../progress/m-progress-20-07-2026.md) · [ML baseline, stay level (superseded)](m-ml-baseline-stay-level.md) · [ML ceiling check, row level](m-ml-ceiling-row-level.md) · [sigma](../notes/m-sigma.md)

</div>
