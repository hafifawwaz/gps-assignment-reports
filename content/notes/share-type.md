---
source: report/notes/share-type.md
date: 19-07-2026
kind: note
comments: true
generated: 2026-10-13T16:57:34
---

# share_type

<p class="doc-meta"><span class="chip chip-note">Note</span> <span class="chip chip-date">19-07-2026</span></p>

How common the candidate's own type is among the stay's candidates, given a separate coefficient per type (`share_bldg`, `share_street`, `share_os`).

Adding it fixed the base model's worst problem ([Model 2: share-type and sigma](../analysis/model-2-share-type-sigma.md)), but its large negative street and open-space weights penalize a candidate for having many same-type neighbours. That is the mechanism behind [Candidate density bias toward building](../analysis/candidate-density-bias.md).

Part of [Chapter 4: Framework](../progress/ch4-framework.md).


<div class="backlinks" markdown>

**Linked from** [Candidate density bias toward building](../analysis/candidate-density-bias.md) · [Chapter 4: Framework](../progress/ch4-framework.md) · [Framework overview](framework-overview.md) · [Model 2: share-type and sigma](../analysis/model-2-share-type-sigma.md) · [f_distribution](f-distribution.md)

</div>
