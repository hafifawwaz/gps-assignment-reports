---
source: report/notes/m-f-distribution.md
date: 25-07-2026
kind: note
comments: true
generated: 2026-10-14T14:44:07
---

# f_distribution

<p class="doc-meta"><span class="chip chip-note">Note</span> <span class="chip chip-project">Master</span> <span class="chip chip-date">25-07-2026</span></p>

The share of the stay's time spent near the candidate. It counts the GPS points within `R_buffer` of the candidate, weighted by time:


$$f_\text{distribution}(E_k, C_i) = \frac{\sum_{p \in C_i} W_p \cdot \mathbf{1}\{d(p, E_k) \leq R_\text{buffer}\}}{\sum_{p \in C_i} W_p}$$


$\mathbf{1}\{\dots\}$ is 1 when point $p$ is close enough to the candidate and 0 otherwise. $W_p$ is the time weight of point $p$ (following Wu et al., 2026). Phones do not record points at even time steps, so each point gets a weight equal to the time it stands for. Points in the middle get $W_p = (t_{p+1} - t_{p-1})/2$, half the time between the point before and the point after. The first and last points get:


$$W_1 = \frac{t_1 + t_2}{2}, \qquad W_n = 1 - \frac{t_{n-1} + t_n}{2}$$


**In the models:** this score was significant from the very first model ([Model 1: base](../analysis/m-model-1-base.md)), and it is the strongest open-space term in the [Final model](../analysis/m-final-model.md). Its product with [share_type](m-share-type.md) is the only combined term that the final model kept ([Interaction term screen (α = 1)](../analysis/m-interaction-term-screen.md)).

Part of [Framework overview](m-framework-overview.md).


<div class="backlinks" markdown>

**Linked from** [Assignment framework](../threads/m-assignment-framework.md) · [Candidate selection](m-candidate-selection.md) · [Framework overview](m-framework-overview.md) · [Model 1: base](../analysis/m-model-1-base.md) · [f_temporal](m-f-temporal.md)

</div>
