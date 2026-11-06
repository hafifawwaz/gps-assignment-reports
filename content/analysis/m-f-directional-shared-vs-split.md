---
source: report/analysis/m-f-directional-shared-vs-split.md
date: 21-07-2026
kind: analysis
comments: true
generated: 2026-11-06T11:37:20
---

# f_directional: shared vs split

<p class="doc-meta"><span class="chip chip-analysis">Analysis</span> <span class="chip chip-project">Master</span> <span class="chip chip-date">21-07-2026</span></p>

Does [f_directional](../concepts/m-f-directional.md) need a separate weight for each place type ("split", the 13-parameter model, $w_{3,t} f_\text{directional}$)? Or is one weight for all types enough ("shared", 11 parameters, $w_3 f_\text{directional}$)? Everything else stayed the same.

| | Shared (11) | Split (13) | Street only (11) |
|---|---:|---:|---:|
| Accuracy | **0.729** | 0.727 | 0.724 |
| CV accuracy (grouped) | **0.718 ± 0.028** | 0.710 ± 0.030 | 0.714 ± 0.024 |
| Condition number | **1,869** | 2,036 | 1,882 |

**Split vs shared: LR = 4.32, df = 2, p = 0.115.** This is not significant: the two extra weights do not improve the fit enough. They improve the fit on the training data a little, but *lower* accuracy on unseen data and raise the condition number. That is overfitting ([Overfitting signature](../concepts/m-overfitting-signature.md)).

The shared weight is clearly significant (t = +6.82). In the split version, the building and street weights pass 1.96, and the street weight turns negative (-5.14). "Street only" is a little worse than shared at this size: lower accuracy on unseen data (0.714 against 0.718), the same fit, slightly lower stability, and lower training accuracy. In the 7-parameter models, shared wins on every measure (CV 0.655 against 0.646), the same result as in [Directional scope ablation (3a vs 3b)](m-directional-scope-ablation.md).

**Decision: shared, 11 parameters** → [Final model](m-final-model.md), the final model of the thesis (Section 5.1.8). Part of [Calibration](../threads/m-calibration.md).


<div class="backlinks" markdown>

**Linked from** [Calibration](../threads/m-calibration.md) · [Directional scope ablation (3a vs 3b)](m-directional-scope-ablation.md) · [Overfitting signature](../concepts/m-overfitting-signature.md) · [RQ1 rebuilt with grouped CV](../progress/m-progress-21-07-2026.md) · [Stepwise VIF elimination](m-stepwise-vif-elimination.md) · [f_directional](../concepts/m-f-directional.md)

</div>
