---
source: report/concepts/m-experiment-design.md
date: 25-07-2026
kind: concept
comments: true
generated: 2026-10-26T20:41:14
---

# Experiment design

<p class="doc-meta"><span class="chip chip-concept">Concept</span> <span class="chip chip-project">Master</span> <span class="chip chip-date">25-07-2026</span></p>

The correct answers (ground truth) come from a planned field survey. Participants visited places with set instructions and wrote down where they were.

- **11 participants**, each doing 2 sessions, between 5 and 14 June 2026.
- **5 groups of stops** (A to E), each testing one theme. Each session has 12 planned stops and 4 free stops chosen by the participant: [Group A: vertical position](m-experiment-group-a.md) (floor level), [Group B: sky view obstruction](m-experiment-group-b.md) (how much sky is visible), [Group C: indoor position](m-experiment-group-c.md) (position inside a building), [Group D: movement type](m-experiment-group-d.md) (how the person moves), [Group E: ambiguous edge cases](m-experiment-group-e.md) (places that are hard to classify).
- **3 phones per session** (4 or 5 in six sessions), to collect more GPS data. The recordings of one stop are not independent of each other. This is why testing uses [Grouped cross-validation](m-grouped-cross-validation.md).
- The start and end of each stay come from the [Self-report form](m-self-report-form.md), not from an algorithm.

Result: [Ground truth dataset](m-ground-truth-dataset.md). Part of [Ground truth data](../threads/m-ground-truth-data.md).


<div class="backlinks" markdown>

**Linked from** [Ground truth data](../threads/m-ground-truth-data.md) · [Ground truth dataset](m-ground-truth-dataset.md) · [Group A: vertical position](m-experiment-group-a.md) · [Group B: sky view obstruction](m-experiment-group-b.md) · [Group C: indoor position](m-experiment-group-c.md) · [Group D: movement type](m-experiment-group-d.md) · [Group E: ambiguous edge cases](m-experiment-group-e.md) · [Grouped cross-validation](m-grouped-cross-validation.md) · [Self-report form](m-self-report-form.md)

</div>
