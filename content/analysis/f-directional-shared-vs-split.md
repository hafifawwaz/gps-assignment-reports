---
source: report/analysis/f-directional-shared-vs-split.md
date: 21-07-2026
kind: analysis
comments: true
generated: 2026-10-13T16:57:34
---

# f_directional: shared vs split

<p class="doc-meta"><span class="chip chip-analysis">Analysis</span> <span class="chip chip-date">21-07-2026</span></p>

Does [f_directional](../notes/f-directional.md) need one coefficient per type ("split", the 14-parameter model) or one for all types ("shared", 12 parameters)? Everything else held fixed.

| | Shared (12) | Split (14) | Street only (12) |
|---|---:|---:|---:|
| Accuracy | 0.721 | 0.724 | 0.723 |
| CV accuracy (grouped) | **0.716 ± 0.076** | 0.709 ± 0.075 | **0.716 ± 0.069** |
| Condition number | **1,373** | 2,430 | 1,431 |

**Split vs shared: LR = 5.41, df = 2, p = 0.067**, not significant. The split's two extra parameters buy +0.3 pp in-sample but *lower* CV and double the condition number: it overfits ([Overfitting signature](../notes/overfitting-signature.md)).

The shared coefficient is cleanly significant (t = +3.12); in the split version only the building term clears 1.96. Street-only is statistically equivalent to shared at this size, never better; at the 7-parameter size shared wins on every metric (CV 0.666 vs 0.656), echoing [Directional scope ablation (3a vs 3b)](directional-scope-ablation.md).

**Decision: shared, 12 parameters** → [Final model](final-model.md), adopted as the thesis's final model (Section 5.1.8). Part of [Chapter 5: Results](../progress/ch5-results.md).


<div class="backlinks" markdown>

**Linked from** [Chapter 5: Results](../progress/ch5-results.md) · [Directional scope ablation (3a vs 3b)](directional-scope-ablation.md) · [Overfitting signature](../notes/overfitting-signature.md) · [RQ1 rebuilt with grouped CV](../progress/progress-21-07-2026.md) · [Stepwise VIF elimination](stepwise-vif-elimination.md) · [f_directional](../notes/f-directional.md)

</div>
