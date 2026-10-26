---
source: report/threads/m-ground-truth-data.md
date: 05-08-2026
kind: thread
comments: true
generated: 2026-10-26T20:41:14
---

# Ground truth data

<p class="doc-meta"><span class="chip chip-thread">Thread</span> <span class="chip chip-project">Master</span> <span class="chip chip-date">05-08-2026</span></p>

Part of [Thesis summary](m-thesis-summary.md). The study area, the map layers, and how a field survey produced 907 stays with known correct answers.

- [Study area](../concepts/m-study-area.md): Hiroshima City, and the MILES GPS dataset the method is built for
- [Spatial entity layers](../concepts/m-spatial-entity-layers.md): how the map was split into buildings, streets and open space
- [Experiment design](../concepts/m-experiment-design.md): the field survey that produced the correct answers
  - the five groups of stops: [Group A: vertical position](../concepts/m-experiment-group-a.md), [Group B: sky view obstruction](../concepts/m-experiment-group-b.md), [Group C: indoor position](../concepts/m-experiment-group-c.md), [Group D: movement type](../concepts/m-experiment-group-d.md), [Group E: ambiguous edge cases](../concepts/m-experiment-group-e.md)
  - [Self-report form](../concepts/m-self-report-form.md): the form participants filled in at each stop
- [Downsampling to MILES density](../concepts/m-downsampling-to-miles-density.md): removing survey points so the data looks like MILES
- [Ground truth cleaning](../concepts/m-ground-truth-cleaning.md): from 1,017 records to 975, then to 907
- [Ground truth drop list](../analysis/m-drop-list.md): what was removed in the last cleaning step
- [Ground truth dataset](../concepts/m-ground-truth-dataset.md): the final 907 stays

Meetings: [RQ2 diagnostics and RQ3 ceiling check](../progress/m-progress-23-07-2026.md) (975 vs 956 count), [Does downsampling matter?](../progress/m-progress-29-07-2026.md) (does downsampling matter?).


<div class="backlinks" markdown>

**Linked from** [Downsampling to MILES density](../concepts/m-downsampling-to-miles-density.md) · [Experiment design](../concepts/m-experiment-design.md) · [Ground truth cleaning](../concepts/m-ground-truth-cleaning.md) · [Ground truth dataset](../concepts/m-ground-truth-dataset.md) · [Ground truth drop list](../analysis/m-drop-list.md) · [Spatial entity layers](../concepts/m-spatial-entity-layers.md) · [Study area](../concepts/m-study-area.md) · [Thesis summary](m-thesis-summary.md)

</div>
