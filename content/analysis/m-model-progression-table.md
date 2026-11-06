---
source: report/analysis/m-model-progression-table.md
date: 21-07-2026
kind: analysis
comments: true
generated: 2026-11-06T11:37:20
---

# Model progression

<p class="doc-meta"><span class="chip chip-analysis">Analysis</span> <span class="chip chip-project">Master</span> <span class="chip chip-date">21-07-2026</span></p>

All models in one table, in the order they were built. Every model was tested with [Grouped cross-validation](../concepts/m-grouped-cross-validation.md), with a 10 m search distance unless the row says 15 m.

How to read it: **Accuracy** is measured on the training data. **CV accuracy** is measured on unseen data and is the fairer number. **Condition number** shows how stable the model is: higher means less stable.

| Model | α | Params | Accuracy | CV accuracy (grouped) | Condition no. |
|---|---:|---:|---:|---:|---:|
| [Model 1: base](m-model-1-base.md) | 1 | 4 | 0.519 | 0.522 ± 0.055 | 86 |
| [Model 1: base](m-model-1-base.md), 15 m | 1 | 4 | 0.512 | 0.505 ± 0.065 | 78 |
| [Model 2: share-type and sigma](m-model-2-share-type-sigma.md) | 1 | 7 | 0.663 | 0.655 ± 0.029 | 114 |
| [Model 2: share-type and sigma](m-model-2-share-type-sigma.md), 15 m | 1 | 7 | 0.639 | 0.642 ± 0.031 | 106 |
| 3b, [Directional scope ablation (3a vs 3b)](m-directional-scope-ablation.md) | 1 | 7 | 0.653 | 0.644 ± 0.023 | 231 |
| [Model 4a: alternative-specific parameters](m-model-4a-alternative-specific.md) | 1 | 13 | 0.714 | 0.697 ± 0.026 | 739 |
| [Model 5: alternative-specific constants (rejected)](m-model-5-asc-rejected.md) | 1 | 15 | 0.728 | 0.719 ± 0.016 | 2,055 |
| Model 6, [Interaction term screen (α = 1)](m-interaction-term-screen.md) | 1 | 16 | 0.716 | 0.709 ± 0.037 | 13,815 |
| Model 4a at α\* | 2.98 | 13 | 0.727 | 0.710 ± 0.030 | 2,036 |
| [Model 6, re-derived at calibrated alpha](m-model-6-rederived.md) | 2.98 | 15 | 0.722 | 0.698 ± 0.043 | 11,696 |
| [Stepwise VIF elimination](m-stepwise-vif-elimination.md) | 2.98 | 13 | 0.727 | 0.710 ± 0.030 | 2,036 |
| **[Final model](m-final-model.md)** | 2.98 | **11** | 0.729 | **0.718 ± 0.028** | **1,869** |

Accuracy rises by about 21 percentage points in total. Most of it comes from two steps: adding share_type and σ (+14) and giving each type its own weights (+5). After that, extra complexity mostly changes how stable the model is, not how accurate it is. The stepwise step ends exactly at Model 4a at α\*, because it removes both extra terms.

Part of [Calibration](../threads/m-calibration.md).


<div class="backlinks" markdown>

**Linked from** [Calibration](../threads/m-calibration.md) · [Final model](m-final-model.md) · [Grouped cross-validation](../concepts/m-grouped-cross-validation.md) · [RQ1 rebuilt with grouped CV](../progress/m-progress-21-07-2026.md)

</div>
