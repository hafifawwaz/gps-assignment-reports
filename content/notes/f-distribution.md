---
source: report/notes/f-distribution.md
date: 25-07-2026
kind: note
comments: true
generated: 2026-10-13T20:41:00
---

# f_distribution

<p class="doc-meta"><span class="chip chip-note">Note</span> <span class="chip chip-date">25-07-2026</span></p>

Time-weighted share of the cluster's points that fall within the buffer of the candidate:


$$f_\text{distribution}(E_k, C_i) = \frac{\sum_{p \in C_i} W_p \cdot \mathbf{1}\{d(p, E_k) \leq R_\text{buffer}\}}{\sum_{p \in C_i} W_p}$$


$W_p$ is the time weight of point $p$ (following Wu et al., 2026), so irregular sampling does not bias the share. Interior points get $W_p = (t_{p+1} - t_{p-1})/2$; the first and last points


$$W_1 = \frac{t_1 + t_2}{2}, \qquad W_n = 1 - \frac{t_{n-1} + t_n}{2}$$


The most consistently significant score from the very first model ([Model 1: base](../analysis/model-1-base.md)) and the strongest open-space term in the [Final model](../analysis/final-model.md). Its product with [share_type](share-type.md) is the one interaction that survived ([Interaction term screen (α = 1)](../analysis/interaction-term-screen.md)).

Part of [Framework overview](framework-overview.md).


<div class="backlinks" markdown>

**Linked from** [Assignment framework](../threads/assignment-framework.md) · [Candidate selection](candidate-selection.md) · [Framework overview](framework-overview.md) · [Model 1: base](../analysis/model-1-base.md) · [f_temporal](f-temporal.md)

</div>
