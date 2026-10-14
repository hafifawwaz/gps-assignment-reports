---
source: report/notes/m-share-type.md
date: 19-07-2026
kind: note
comments: true
generated: 2026-10-14T14:44:07
---

# share_type

<p class="doc-meta"><span class="chip chip-note">Note</span> <span class="chip chip-project">Master</span> <span class="chip chip-date">19-07-2026</span></p>

How common the candidate's own type is among all candidates of the stay. If a stay has 20 candidates and 12 of them are street pieces, the street share is 12/20 = 0.6. With $n_{t,i}$ candidates of type $t$ out of $N_i$ candidates for stay $i$:


$$\text{share}_t(C_i) = \frac{n_{t,i}}{N_i}$$


Each type gets its own weight (`share_bldg`, `share_street`, `share_os`). Each column holds the share for rows of that type and 0 for the other rows.

**In the models:** adding this term fixed the biggest problem of the first model ([Model 2: share-type and sigma](../analysis/m-model-2-share-type-sigma.md)). But its weights for street and open space are large and negative. So a candidate with many neighbours of the same type gets a lower value. That is the cause of [Candidate density bias toward building](../analysis/m-candidate-density-bias.md).

Part of [Assignment framework](../threads/m-assignment-framework.md).


<div class="backlinks" markdown>

**Linked from** [Assignment framework](../threads/m-assignment-framework.md) · [Candidate density bias toward building](../analysis/m-candidate-density-bias.md) · [Framework overview](m-framework-overview.md) · [Model 2: share-type and sigma](../analysis/m-model-2-share-type-sigma.md) · [f_distribution](m-f-distribution.md)

</div>
