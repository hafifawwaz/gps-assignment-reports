---
source: report/threads/m-assignment-framework.md
date: 05-08-2026
kind: thread
comments: true
generated: 2026-10-27T18:04:09
---

# Assignment framework

<p class="doc-meta"><span class="chip chip-thread">Thread</span> <span class="chip chip-project">Master</span> <span class="chip chip-date">05-08-2026</span></p>

Part of [Thesis summary](m-thesis-summary.md). How the method turns one stay into a probability for building, street and open space.

- [Framework overview](../concepts/m-framework-overview.md): the four steps, from a stay to probabilities
- [Candidate selection](../concepts/m-candidate-selection.md): which nearby places are considered
- The four scores for each candidate: [f_distribution](../concepts/m-f-distribution.md), [f_distance](../concepts/m-f-distance.md), [f_temporal](../concepts/m-f-temporal.md), [f_directional](../concepts/m-f-directional.md)
- Two extra inputs added during calibration: [share_type](../concepts/m-share-type.md), [sigma](../concepts/m-sigma.md)

How the model learned its weights: [Calibration](m-calibration.md).

Meetings: [MNL model development](../progress/m-progress-19-07-2026.md) (first learned weights), [RQ1 rebuilt with grouped CV](../progress/m-progress-21-07-2026.md) (one shared weight for f_directional).


<div class="backlinks" markdown>

**Linked from** [CSIS DAYS 2026 slides](../analysis/m-csis-slide.md) · [Framework overview](../concepts/m-framework-overview.md) · [Nested probabilities](../plans/d-nested-probabilities.md) · [Sequence-aware assignment](../plans/d-sequence-aware.md) · [Thesis summary](m-thesis-summary.md) · [share_type](../concepts/m-share-type.md) · [sigma](../concepts/m-sigma.md)

</div>
