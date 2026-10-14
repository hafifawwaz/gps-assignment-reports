---
source: report/notes/m-f-temporal.md
date: 25-07-2026
kind: note
comments: true
generated: 2026-10-14T14:44:07
---

# f_temporal

<p class="doc-meta"><span class="chip chip-note">Note</span> <span class="chip chip-project">Master</span> <span class="chip chip-date">25-07-2026</span></p>

The longest unbroken stretch of time the stay spent at the candidate, as a share of the whole stay:


$$f_\text{temporal}(E_k, C_i) = \frac{\max_{S \in S(E_k, C_i)} \sum_{p \in S} W_p}{\sum_{p \in C_i} W_p}$$


$S$ is a run of points in time order that belong to candidate $E_k$. $W_p$ is the time weight from [f_distribution](m-f-distribution.md). The score takes the longest run. A short jump outside the place does not end a run, as long as the total time outside stays within $\Delta t_\text{gap} = 300$ seconds. Gaps longer than five minutes count as a new activity.

**In the models:** this score was removed after the first model. It was never significant, and it moved almost the same way as [f_distribution](m-f-distribution.md) (correlation r ≈ 0.88, VIF 7-8), so it added little new information. See [Model 1: base](../analysis/m-model-1-base.md).

Part of [Framework overview](m-framework-overview.md).


<div class="backlinks" markdown>

**Linked from** [Assignment framework](../threads/m-assignment-framework.md) · [Framework overview](m-framework-overview.md) · [Model 1: base](../analysis/m-model-1-base.md) · [Model 2: share-type and sigma](../analysis/m-model-2-share-type-sigma.md)

</div>
