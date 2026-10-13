---
source: report/notes/f-temporal.md
date: 25-07-2026
kind: note
comments: true
generated: 2026-10-13T20:41:00
---

# f_temporal

<p class="doc-meta"><span class="chip chip-note">Note</span> <span class="chip chip-date">25-07-2026</span></p>

The longest uninterrupted (gap-bridged), time-weighted run of the cluster's points inside the candidate:


$$f_\text{temporal}(E_k, C_i) = \frac{\max_{S \in S(E_k, C_i)} \sum_{p \in S} W_p}{\sum_{p \in C_i} W_p}$$


$S$ is a run of chronologically consecutive points associated with $E_k$, and $W_p$ the time weight from [f_distribution](f-distribution.md). A run is not broken while points briefly fall outside the entity, as long as the cumulative time outside stays within $\Delta t_\text{gap} = 300$ s (gaps over five minutes start a new activity episode).

Dropped after the base model: never significant and strongly collinear with [f_distribution](f-distribution.md) (r ≈ 0.88, VIF 7-8). See [Model 1: base](../analysis/model-1-base.md).

Part of [Framework overview](framework-overview.md).


<div class="backlinks" markdown>

**Linked from** [Assignment framework](../threads/assignment-framework.md) · [Framework overview](framework-overview.md) · [Model 1: base](../analysis/model-1-base.md) · [Model 2: share-type and sigma](../analysis/model-2-share-type-sigma.md)

</div>
