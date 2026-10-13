---
source: report/notes/framework-overview.md
date: 25-07-2026
kind: note
comments: true
generated: 2026-10-13T20:41:00
---

# Framework overview

<p class="doc-meta"><span class="chip chip-note">Note</span> <span class="chip chip-date">25-07-2026</span></p>

1. **Candidates:** every entity within `R_buffer` of the stay cluster ([Candidate selection](candidate-selection.md)).
2. **Scores:** four components per candidate: [f_distribution](f-distribution.md), [f_distance](f-distance.md), [f_temporal](f-temporal.md), [f_directional](f-directional.md).
3. **Utility:** a weighted sum of the scores (plus [share_type](share-type.md) and [sigma](sigma.md) once calibration added them),


$$V_k = w_1 f_\text{distribution} + w_2 f_\text{distance} + w_3 f_\text{temporal} + w_4 f_\text{directional}$$


   additive rather than multiplicative, so a single zero score cannot eliminate a candidate.
4. **Probability:** a type-level conditional logit,


$$P(t \mid C_i) = \frac{\sum_{k \in t} \exp(V_k)}{\sum_{j \in \text{Candidates}(C_i)} \exp(V_j)}$$


The weights are estimated by maximum likelihood on the [Ground truth dataset](ground-truth-dataset.md) rather than fixed in advance.

Part of [Assignment framework](../threads/assignment-framework.md). Answers the "how" of [Research questions](research-questions.md) RQ1.


<div class="backlinks" markdown>

**Linked from** [Assignment framework](../threads/assignment-framework.md) · [Candidate selection](candidate-selection.md) · [Contributions](contributions.md) · [Extending map matching to stationary stays](map-matching-extension.md) · [Research questions](research-questions.md) · [f_directional](f-directional.md) · [f_distance](f-distance.md) · [f_distribution](f-distribution.md) · [f_temporal](f-temporal.md)

</div>
