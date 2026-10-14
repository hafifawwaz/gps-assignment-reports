---
source: report/analysis/m-model-progression-table.md
date: 21-07-2026
kind: analysis
comments: true
generated: 2026-10-14T14:44:07
---

# Model progression

<p class="doc-meta"><span class="chip chip-analysis">Analysis</span> <span class="chip chip-project">Master</span> <span class="chip chip-date">21-07-2026</span></p>

All models in one table, in the order they were built. Every model was tested with [Grouped cross-validation](../notes/m-grouped-cross-validation.md), with a 10 m search distance unless the row says 15 m.

How to read it: **Accuracy** is measured on the training data. **CV accuracy** is measured on unseen data and is the fairer number. **Condition number** shows how stable the model is: higher means less stable.

| Model | α | Params | Accuracy | CV accuracy (grouped) | Condition no. |
|---|---:|---:|---:|---:|---:|
| [Model 1: base](m-model-1-base.md) | 1 | 4 | 0.518 | 0.514 ± 0.089 | 36 |
| [Model 1: base](m-model-1-base.md), 15 m | 1 | 4 | 0.509 | 0.512 ± 0.098 | 26 |
| [Model 2: share-type and sigma](m-model-2-share-type-sigma.md) | 1 | 7 | 0.668 | 0.664 ± 0.046 | 117 |
| [Model 2: share-type and sigma](m-model-2-share-type-sigma.md), 15 m | 1 | 7 | 0.654 | 0.647 ± 0.042 | 98 |
| 3b, [Directional scope ablation (3a vs 3b)](m-directional-scope-ablation.md) | 1 | 7 | 0.666 | 0.658 ± 0.040 | 135 |
| [Model 4a: alternative-specific parameters](m-model-4a-alternative-specific.md) | 1 | 13 | 0.717 | 0.707 ± 0.069 | 775 |
| [Model 5: alternative-specific constants (rejected)](m-model-5-asc-rejected.md) | 1 | 15 | 0.728 | 0.717 ± 0.068 | 37,583 |
| Model 6, [Interaction term screen (α = 1)](m-interaction-term-screen.md) | 1 | 16 | 0.724 | 0.711 ± 0.077 | 20,695 |
| Model 4a at α\* | 2.43 | 13 | 0.723 | 0.717 ± 0.065 | 2,338 |
| [Model 6, re-derived at calibrated alpha](m-model-6-rederived.md) | 2.43 | 15 | 0.723 | 0.710 ± 0.075 | 14,851 |
| [Stepwise VIF elimination](m-stepwise-vif-elimination.md) | 2.43 | 14 | 0.724 | 0.709 ± 0.075 | 2,430 |
| **[Final model](m-final-model.md)** | 2.43 | **12** | 0.721 | **0.716 ± 0.076** | **1,373** |

Accuracy rises by about 20 percentage points in total. Most of it comes from two steps: adding share_type and σ (+15) and giving each type its own weights (+5). After that, extra complexity mostly changes how stable the model is, not how accurate it is.

Part of [Calibration](../threads/m-calibration.md).


<div class="backlinks" markdown>

**Linked from** [Calibration](../threads/m-calibration.md) · [Final model](m-final-model.md) · [Grouped cross-validation](../notes/m-grouped-cross-validation.md) · [RQ1 rebuilt with grouped CV](../progress/m-progress-21-07-2026.md)

</div>
