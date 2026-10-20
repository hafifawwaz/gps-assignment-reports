---
source: report/analysis/m-stepwise-vif-elimination.md
date: 21-07-2026
kind: analysis
comments: true
generated: 2026-10-20T15:44:29
---

# Stepwise VIF elimination

<p class="doc-meta"><span class="chip chip-analysis">Analysis</span> <span class="chip chip-project">Master</span> <span class="chip chip-date">21-07-2026</span></p>

Removing weak terms one at a time from [Model 6, re-derived at calibrated alpha](m-model-6-rederived.md). At each step, find the extra term (not one of the core terms) with the highest VIF, remove it, and fit the model again. Stop when every extra term has a VIF of 10 or less. The 13 core terms from Model 4a are never removed ([Multicollinearity is structural](../notes/m-multicollinearity-is-structural.md)).

| Step | Worst droppable | VIF | Action |
|---:|---|---:|---|
| 0 | σ² | 19.51 | drop |
| 1 | f_distribution × share_type | 10.44 | drop |
| 2 | none left | | stop |

Both extra terms go. f_distribution × share_type is only just above the line of 10, although it is significant on its own (t = 4.61 before the first step). Removing both costs some fit (LR = 20.42, df = 2, **p < 0.0001**), but accuracy on unseen data goes up (0.703 → 0.712), and the condition number drops about 5 times (9,031 → 1,878), so the model becomes much more stable.

**Result, the 13-parameter model:** the 13 core terms of Model 4a, at α = 2.764.


$$V_t = w_{1,t} f_\text{distribution} + w_{2,t} f_\text{distance} + w_{3,t} f_\text{directional} + w_{4,t}\,share_t + w_5\,\sigma$$


Accuracy 0.733, accuracy on unseen data **0.712 ± 0.038**, condition number 1,878.

Later it was made smaller, to 11 parameters: [f_directional: shared vs split](m-f-directional-shared-vs-split.md). Part of [Calibration](../threads/m-calibration.md).


<div class="backlinks" markdown>

**Linked from** [Calibration](../threads/m-calibration.md) · [MNL model development](../progress/m-progress-19-07-2026.md) · [Model 6, re-derived at calibrated alpha](m-model-6-rederived.md) · [Model progression](m-model-progression-table.md) · [Multicollinearity is structural](../notes/m-multicollinearity-is-structural.md) · [Overfitting signature](../notes/m-overfitting-signature.md) · [RQ1 rebuilt with grouped CV](../progress/m-progress-21-07-2026.md) · [Sigma in tree importance](m-sigma-tree-importance.md) · [Thesis bug fixes and adopted rerun](../inbox/thesis-bug-fix.md) · [f_distribution](../notes/m-f-distribution.md)

</div>
