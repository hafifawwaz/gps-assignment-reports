---
source: report/notes/framework-overview.md
date: 25-07-2026
kind: note
comments: true
generated: 2026-10-13T16:57:34
---

# Framework overview

<p class="doc-meta"><span class="chip chip-note">Note</span> <span class="chip chip-date">25-07-2026</span></p>

1. **Candidates:** every entity within `R_buffer` of the stay cluster ([Candidate selection](candidate-selection.md)).
2. **Scores:** four components per candidate: [f_distribution](f-distribution.md), [f_distance](f-distance.md), [f_temporal](f-temporal.md), [f_directional](f-directional.md).
3. **Utility:** a weighted sum $V_k$ of the scores (plus [share_type](share-type.md) and [sigma](sigma.md) once calibration added them).
4. **Probability:** a type-level conditional logit,


$$P(t \mid C_i) = \frac{\sum_{k \in t} \exp(V_k)}{\sum_j \exp(V_j)}$$


The weights are estimated by maximum likelihood on the [Ground truth dataset](ground-truth-dataset.md) rather than fixed in advance.

Part of [Chapter 4: Framework](../progress/ch4-framework.md). Answers the "how" of [Research questions](research-questions.md) RQ1.


<div class="backlinks" markdown>

**Linked from** [Candidate selection](candidate-selection.md) · [Chapter 4: Framework](../progress/ch4-framework.md) · [Contributions](contributions.md) · [Extending map matching to stationary stays](map-matching-extension.md) · [Research questions](research-questions.md) · [f_directional](f-directional.md) · [f_distance](f-distance.md) · [f_distribution](f-distribution.md) · [f_temporal](f-temporal.md)

</div>
