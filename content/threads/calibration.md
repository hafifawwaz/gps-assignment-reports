---
source: report/threads/calibration.md
date: 05-08-2026
kind: thread
comments: true
generated: 2026-10-13T21:08:51
---

# Calibration

<p class="doc-meta"><span class="chip chip-thread">Thread</span> <span class="chip chip-date">05-08-2026</span></p>

Part of [Thesis summary](thesis-summary.md). RQ1: from the base model to the final 12-parameter model.

How models are compared: [Model evaluation metrics](../notes/model-evaluation-metrics.md), [Grouped cross-validation](../notes/grouped-cross-validation.md).

The model progression, in order (overview: [Model progression](../analysis/model-progression-table.md)):

1. [Model 1: base](../analysis/model-1-base.md) and [R_buffer: 10 m vs 15 m](../analysis/r-buffer-10m-vs-15m.md)
2. [Model 2: share-type and sigma](../analysis/model-2-share-type-sigma.md)
3. [Directional scope ablation (3a vs 3b)](../analysis/directional-scope-ablation.md)
4. [Model 4a: alternative-specific parameters](../analysis/model-4a-alternative-specific.md)
5. [Model 5: alternative-specific constants (rejected)](../analysis/model-5-asc-rejected.md)
6. [Interaction term screen (α = 1)](../analysis/interaction-term-screen.md)
7. [Alpha calibration](../analysis/alpha-calibration.md), which exposed [The f_distance² artifact](../analysis/f-distance-squared-artifact.md)
8. [Model 6, re-derived at calibrated alpha](../analysis/model-6-rederived.md) and [Stepwise VIF elimination](../analysis/stepwise-vif-elimination.md)
9. [f_directional: shared vs split](../analysis/f-directional-shared-vs-split.md)
10. Result: [Final model](../analysis/final-model.md) ([Final model correlation matrix](../analysis/final-model-correlation-matrix.md), [Multicollinearity is structural](../notes/multicollinearity-is-structural.md))

Meetings: [MNL model development](../progress/progress-19-07-2026.md), [RQ1 rebuilt with grouped CV](../progress/progress-21-07-2026.md).


<div class="backlinks" markdown>

**Linked from** [Alpha calibration](../analysis/alpha-calibration.md) · [Assignment framework](assignment-framework.md) · [Directional scope ablation (3a vs 3b)](../analysis/directional-scope-ablation.md) · [Final model](../analysis/final-model.md) · [Final model correlation matrix](../analysis/final-model-correlation-matrix.md) · [Grouped cross-validation](../notes/grouped-cross-validation.md) · [Interaction term screen (α = 1)](../analysis/interaction-term-screen.md) · [Model 1: base](../analysis/model-1-base.md) · [Model 2: share-type and sigma](../analysis/model-2-share-type-sigma.md) · [Model 4a: alternative-specific parameters](../analysis/model-4a-alternative-specific.md) · [Model 5: alternative-specific constants (rejected)](../analysis/model-5-asc-rejected.md) · [Model 6, re-derived at calibrated alpha](../analysis/model-6-rederived.md) · [Model evaluation metrics](../notes/model-evaluation-metrics.md) · [Model progression](../analysis/model-progression-table.md) · [Multicollinearity is structural](../notes/multicollinearity-is-structural.md) · [R_buffer: 10 m vs 15 m](../analysis/r-buffer-10m-vs-15m.md) · [Research questions](../notes/research-questions.md) · [Stepwise VIF elimination](../analysis/stepwise-vif-elimination.md) · [The f_distance² artifact](../analysis/f-distance-squared-artifact.md) · [Thesis summary](thesis-summary.md) · [f_directional: shared vs split](../analysis/f-directional-shared-vs-split.md)

</div>
