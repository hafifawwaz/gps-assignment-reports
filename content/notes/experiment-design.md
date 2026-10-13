---
source: report/notes/experiment-design.md
date: 25-07-2026
kind: note
comments: true
generated: 2026-10-13T20:30:42
---

# Experiment design

<p class="doc-meta"><span class="chip chip-note">Note</span> <span class="chip chip-date">25-07-2026</span></p>

The ground truth comes from a controlled field survey:

- **11 participants**, 2 sessions each
- **5 thematic stop groups** (A-E), each with 12 controlled stops plus 4 free-roam stops: [Group A: vertical position](experiment-group-a.md) (vertical position), [Group B: sky view obstruction](experiment-group-b.md) (sky obstruction), [Group C: indoor position](experiment-group-c.md) (indoor position), [Group D: movement type](experiment-group-d.md) (movement type), [Group E: ambiguous edge cases](experiment-group-e.md) (ambiguous edges)
- **3 devices per session**, for sample density. Sibling recordings of one stop are not independent, which is why validation uses [Grouped cross-validation](grouped-cross-validation.md).
- Stay windows come from the [Self-report form](self-report-form.md), not from algorithmic stay detection.

Result: [Ground truth dataset](ground-truth-dataset.md). Part of [Ground truth data](../threads/ground-truth-data.md).


<div class="backlinks" markdown>

**Linked from** [Ground truth data](../threads/ground-truth-data.md) · [Ground truth dataset](ground-truth-dataset.md) · [Group A: vertical position](experiment-group-a.md) · [Group B: sky view obstruction](experiment-group-b.md) · [Group C: indoor position](experiment-group-c.md) · [Group D: movement type](experiment-group-d.md) · [Group E: ambiguous edge cases](experiment-group-e.md) · [Grouped cross-validation](grouped-cross-validation.md) · [Self-report form](self-report-form.md)

</div>
