---
source: report/concepts/m-candidate-selection.md
date: 25-07-2026
kind: concept
comments: true
generated: 2026-10-26T20:41:14
---

# Candidate selection

<p class="doc-meta"><span class="chip chip-concept">Concept</span> <span class="chip chip-project">Master</span> <span class="chip chip-date">25-07-2026</span></p>

How the method decides which places to consider for one stay. Draw a circle with radius `R_buffer` around every GPS point of the stay. Every place that touches at least one circle becomes a candidate:


$$\text{Candidates}(C_i) = \{E_k \mid \min_{p \in C_i} d(p, E_k) \leq R_\text{buffer}\}$$


In words: place $E_k$ is a candidate if its distance $d$ to at least one point $p$ of stay $C_i$ is at most $R_\text{buffer}$.

A circle is used instead of "the point is inside the place", because GPS error can put a recorded point outside the place where the person really was. [f_distribution](m-f-distribution.md) uses the same radius on purpose.

`R_buffer = 10 m` was chosen over 15 m: [R_buffer: 10 m vs 15 m](../analysis/m-r-buffer-10m-vs-15m.md). Because each point has its own circle, a stay with more points covers a larger area: [Downsampling shrinks the candidate search area](../analysis/m-candidate-search-area.md).

Part of [Framework overview](m-framework-overview.md).


<div class="backlinks" markdown>

**Linked from** [Assignment framework](../threads/m-assignment-framework.md) · [Downsampling shrinks the candidate search area](../analysis/m-candidate-search-area.md) · [Framework overview](m-framework-overview.md) · [R_buffer: 10 m vs 15 m](../analysis/m-r-buffer-10m-vs-15m.md)

</div>
