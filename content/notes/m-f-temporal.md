---
source: report/notes/m-f-temporal.md
date: 25-07-2026
kind: note
comments: true
generated: 2026-10-20T15:22:17
---

# f_temporal

<p class="doc-meta"><span class="chip chip-note">Note</span> <span class="chip chip-project">Master</span> <span class="chip chip-date">25-07-2026</span></p>

The longest unbroken stretch of time the stay spent at the candidate, as a share of the whole stay:


$$f_\text{temporal}(E_k, C_i) = \frac{\max_{S \in S(E_k, C_i)} \sum_{p \in S} W_p}{\sum_{p \in C_i} W_p}$$


$S$ is a run of points in time order that belong to candidate $E_k$. A point belongs to $E_k$ when it lies within `R_buffer` (10 m) of it, as in [f_distribution](m-f-distribution.md). $W_p$ is the time weight from [f_distribution](m-f-distribution.md). The score takes the longest run.

A short jump outside does not end a run. A point more than 10 m away still counts toward the run when it comes at most $\Delta t_\text{gap} = 300$ seconds after the last point within 10 m. The run ends only at a point outside that comes more than five minutes after the last point within 10 m. A stretch with no GPS points at all never ends a run, because missing points give no sign that the person left.

Example: a 60-minute stay is within 10 m from minute 0 to 20, outside for 3 minutes, back from 23 to 40, outside for 10 minutes, and back from 50 to 60. The first run covers minutes 0 to 40, so $f_\text{temporal}$ = 40/60 ≈ 0.67.

**In the models:** this score was removed after the first model. It was never significant, and it moved almost the same way as [f_distribution](m-f-distribution.md) (correlation r ≈ 0.96, VIF about 22), so it added little new information. See [Model 1: base](../analysis/m-model-1-base.md).

Part of [Framework overview](m-framework-overview.md).


<div class="backlinks" markdown>

**Linked from** [Assignment framework](../threads/m-assignment-framework.md) · [Framework overview](m-framework-overview.md) · [Model 1: base](../analysis/m-model-1-base.md) · [Model 2: share-type and sigma](../analysis/m-model-2-share-type-sigma.md) · [Thesis bug fixes and adopted rerun](../inbox/thesis-bug-fix.md)

</div>
