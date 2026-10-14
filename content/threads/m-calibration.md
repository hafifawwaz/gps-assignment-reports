---
source: report/threads/m-calibration.md
date: 05-08-2026
kind: thread
comments: true
generated: 2026-10-14T14:44:07
---

# Calibration

<p class="doc-meta"><span class="chip chip-thread">Thread</span> <span class="chip chip-project">Master</span> <span class="chip chip-date">05-08-2026</span></p>

Part of [Thesis summary](m-thesis-summary.md). Research question 1: how the model was built step by step, from a simple first model to the final 12-parameter model.

How the models are compared: [Model evaluation metrics](../notes/m-model-evaluation-metrics.md), [Grouped cross-validation](../notes/m-grouped-cross-validation.md).

The models, in the order they were tried (all in one table: [Model progression](../analysis/m-model-progression-table.md)):

1. [Model 1: base](../analysis/m-model-1-base.md) and [R_buffer: 10 m vs 15 m](../analysis/m-r-buffer-10m-vs-15m.md)
2. [Model 2: share-type and sigma](../analysis/m-model-2-share-type-sigma.md)
3. [Directional scope ablation (3a vs 3b)](../analysis/m-directional-scope-ablation.md)
4. [Model 4a: alternative-specific parameters](../analysis/m-model-4a-alternative-specific.md)
5. [Model 5: alternative-specific constants (rejected)](../analysis/m-model-5-asc-rejected.md)
6. [Interaction term screen (α = 1)](../analysis/m-interaction-term-screen.md)
7. [Alpha calibration](../analysis/m-alpha-calibration.md), which revealed the [The f_distance² artifact](../analysis/m-f-distance-squared-artifact.md)
8. [Model 6, re-derived at calibrated alpha](../analysis/m-model-6-rederived.md) and [Stepwise VIF elimination](../analysis/m-stepwise-vif-elimination.md)
9. [f_directional: shared vs split](../analysis/m-f-directional-shared-vs-split.md)
10. Result: [Final model](../analysis/m-final-model.md) ([Final model correlation matrix](../analysis/m-final-model-correlation-matrix.md), [Multicollinearity is structural](../notes/m-multicollinearity-is-structural.md))

Meetings: [MNL model development](../progress/m-progress-19-07-2026.md), [RQ1 rebuilt with grouped CV](../progress/m-progress-21-07-2026.md).


<div class="backlinks" markdown>

**Linked from** [Alpha calibration](../analysis/m-alpha-calibration.md) · [Assignment framework](m-assignment-framework.md) · [Directional scope ablation (3a vs 3b)](../analysis/m-directional-scope-ablation.md) · [Final model](../analysis/m-final-model.md) · [Final model correlation matrix](../analysis/m-final-model-correlation-matrix.md) · [Grouped cross-validation](../notes/m-grouped-cross-validation.md) · [Interaction term screen (α = 1)](../analysis/m-interaction-term-screen.md) · [Model 1: base](../analysis/m-model-1-base.md) · [Model 2: share-type and sigma](../analysis/m-model-2-share-type-sigma.md) · [Model 4a: alternative-specific parameters](../analysis/m-model-4a-alternative-specific.md) · [Model 5: alternative-specific constants (rejected)](../analysis/m-model-5-asc-rejected.md) · [Model 6, re-derived at calibrated alpha](../analysis/m-model-6-rederived.md) · [Model evaluation metrics](../notes/m-model-evaluation-metrics.md) · [Model progression](../analysis/m-model-progression-table.md) · [Multicollinearity is structural](../notes/m-multicollinearity-is-structural.md) · [R_buffer: 10 m vs 15 m](../analysis/m-r-buffer-10m-vs-15m.md) · [Research questions](../notes/m-research-questions.md) · [Stepwise VIF elimination](../analysis/m-stepwise-vif-elimination.md) · [The f_distance² artifact](../analysis/m-f-distance-squared-artifact.md) · [Thesis summary](m-thesis-summary.md) · [f_directional: shared vs split](../analysis/m-f-directional-shared-vs-split.md)

</div>
