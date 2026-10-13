---
source: report/notes/model-evaluation-metrics.md
date: 19-07-2026
kind: note
comments: true
generated: 2026-10-13T16:57:34
---

# Model evaluation metrics

<p class="doc-meta"><span class="chip chip-note">Note</span> <span class="chip chip-date">19-07-2026</span></p>

| Metric | Meaning |
|---|---|
| LL(0) | Log-likelihood with equal probability for every candidate |
| LL(C) | Constant-only: one intercept per type (the type-share baseline) |
| LL(b) | The fitted model |
| ρ² vs LL(C) | Fit gained over the type-share baseline; negative means worse than it |
| Accuracy | Share of stays whose highest-probability type is correct |
| Condition number | Numerical conditioning of the fit; large values mean unreliable individual coefficients |
| VIF | Variance inflation per feature; above 10 is the usual caution line |

ρ² vs LL(C) cannot compare different `R_buffer` values, because LL(C) itself changes with the candidate pool ([R_buffer: 10 m vs 15 m](../analysis/r-buffer-10m-vs-15m.md)). All CV numbers use [Grouped cross-validation](grouped-cross-validation.md).

Part of [Chapter 4: Framework](../progress/ch4-framework.md).


<div class="backlinks" markdown>

**Linked from** [Chapter 4: Framework](../progress/ch4-framework.md) · [R_buffer: 10 m vs 15 m](../analysis/r-buffer-10m-vs-15m.md)

</div>
