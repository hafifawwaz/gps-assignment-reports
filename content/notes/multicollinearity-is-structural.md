---
source: report/notes/multicollinearity-is-structural.md
date: 19-07-2026
kind: note
comments: true
generated: 2026-10-13T20:05:33
---

# Multicollinearity is structural

<p class="doc-meta"><span class="chip chip-note">Note</span> <span class="chip chip-date">19-07-2026</span></p>

In alternative-specific models, each type's own features (`f_distance_t`, `f_directional_t`, `share_t`) come from the same per-stay candidate pool, so they correlate strongly within a type (often r = 0.86-0.94), and VIFs above 10 appear on core terms.

This is a property of the design, not redundant feature choice. Getting every VIF under 10 would mean removing components from the alternative-specific structure, which would undo why it beats the generic models ([Model 4a: alternative-specific parameters](../analysis/model-4a-alternative-specific.md)). The elimination procedure therefore protects the core terms ([Stepwise VIF elimination](../analysis/stepwise-vif-elimination.md)).

What is *not* structural: an ASC that duplicates a near-constant feature ([Model 5: alternative-specific constants (rejected)](../analysis/model-5-asc-rejected.md)).

Seen in [Final model correlation matrix](../analysis/final-model-correlation-matrix.md). Part of [Calibration](../threads/calibration.md).


<div class="backlinks" markdown>

**Linked from** [Calibration](../threads/calibration.md) · [Final model correlation matrix](../analysis/final-model-correlation-matrix.md) · [MNL model development](../progress/progress-19-07-2026.md) · [Model 4a: alternative-specific parameters](../analysis/model-4a-alternative-specific.md) · [Stepwise VIF elimination](../analysis/stepwise-vif-elimination.md)

</div>
