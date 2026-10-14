---
source: report/notes/m-framework-overview.md
date: 25-07-2026
kind: note
comments: true
generated: 2026-10-14T14:44:07
---

# Framework overview

<p class="doc-meta"><span class="chip chip-note">Note</span> <span class="chip chip-project">Master</span> <span class="chip chip-date">25-07-2026</span></p>

The method in four steps, from one stay to a probability for each type of place.

1. **Candidates.** Find every place (building, street piece or open space) within `R_buffer` of the stay's GPS points ([Candidate selection](m-candidate-selection.md)).
2. **Scores.** Give each candidate four scores, each looking at the GPS points in a different way: [f_distribution](m-f-distribution.md), [f_distance](m-f-distance.md), [f_temporal](m-f-temporal.md), [f_directional](m-f-directional.md).
3. **Utility.** Add the scores together, each multiplied by a weight. The result $V_k$ (the "utility") says how likely candidate $k$ is. Calibration later added two more inputs, [share_type](m-share-type.md) and [sigma](m-sigma.md).


$$V_k = w_1 f_\text{distribution} + w_2 f_\text{distance} + w_3 f_\text{temporal} + w_4 f_\text{directional}$$


   The scores are added, not multiplied. With multiplication, one score of zero would remove a candidate, even if its other scores were high.
4. **Probability.** Turn the utilities into probabilities for each type $t$ (building, street, open space). The model adds up $\exp(V_k)$ for all candidates of that type and divides by the total for all candidates. This is a conditional logit model.


$$P(t \mid C_i) = \frac{\sum_{k \in t} \exp(V_k)}{\sum_{j \in \text{Candidates}(C_i)} \exp(V_j)}$$


The weights $w$ are not chosen by hand. The model learns them from the [Ground truth dataset](m-ground-truth-dataset.md), by finding the weights that best predict the correct answers (maximum likelihood).

Part of [Assignment framework](../threads/m-assignment-framework.md). Answers the "how" part of [Research questions](m-research-questions.md) RQ1.


<div class="backlinks" markdown>

**Linked from** [Assignment framework](../threads/m-assignment-framework.md) · [Candidate selection](m-candidate-selection.md) · [Contributions](m-contributions.md) · [Extending map matching to stationary stays](m-map-matching-extension.md) · [Research questions](m-research-questions.md) · [f_directional](m-f-directional.md) · [f_distance](m-f-distance.md) · [f_distribution](m-f-distribution.md) · [f_temporal](m-f-temporal.md)

</div>
