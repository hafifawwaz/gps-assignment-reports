---
source: report/analysis/m-model-progression-table.md
date: 21-07-2026
kind: analysis
comments: true
generated: 2026-10-26T20:41:14
---

# Model progression

<p class="doc-meta"><span class="chip chip-analysis">Analysis</span> <span class="chip chip-project">Master</span> <span class="chip chip-date">21-07-2026</span></p>

All models in one table, in the order they were built. Every model was tested with [Grouped cross-validation](../concepts/m-grouped-cross-validation.md), with a 10 m search distance unless the row says 15 m.

How to read it: **Accuracy** is measured on the training data. **CV accuracy** is measured on unseen data and is the fairer number. **Condition number** shows how stable the model is: higher means less stable.

| Model | α | Params | Accuracy | CV accuracy (grouped) | Condition no. |
|---|---:|---:|---:|---:|---:|
| [Model 1: base](m-model-1-base.md) | 1 | 4 | 0.540 | 0.539 ± 0.051 | 84 |
| [Model 1: base](m-model-1-base.md), 15 m | 1 | 4 | 0.538 | 0.533 ± 0.033 | 76 |
| [Model 2: share-type and sigma](m-model-2-share-type-sigma.md) | 1 | 7 | 0.673 | 0.666 ± 0.035 | 115 |
| [Model 2: share-type and sigma](m-model-2-share-type-sigma.md), 15 m | 1 | 7 | 0.649 | 0.645 ± 0.046 | 103 |
| 3b, [Directional scope ablation (3a vs 3b)](m-directional-scope-ablation.md) | 1 | 7 | 0.671 | 0.655 ± 0.027 | 216 |
| [Model 4a: alternative-specific parameters](m-model-4a-alternative-specific.md) | 1 | 13 | 0.722 | 0.700 ± 0.036 | 737 |
| [Model 5: alternative-specific constants (rejected)](m-model-5-asc-rejected.md) | 1 | 15 | 0.728 | 0.719 ± 0.033 | 2,027 |
| Model 6, [Interaction term screen (α = 1)](m-interaction-term-screen.md) | 1 | 16 | 0.728 | 0.710 ± 0.031 | 13,198 |
| Model 4a at α\* | 2.76 | 13 | 0.733 | 0.712 ± 0.038 | 1,878 |
| [Model 6, re-derived at calibrated alpha](m-model-6-rederived.md) | 2.76 | 15 | 0.733 | 0.703 ± 0.049 | 9,031 |
| [Stepwise VIF elimination](m-stepwise-vif-elimination.md) | 2.76 | 13 | 0.733 | 0.712 ± 0.038 | 1,878 |
| **[Final model](m-final-model.md)** | 2.76 | **11** | 0.731 | **0.719 ± 0.032** | **1,681** |

Accuracy rises by about 19 percentage points in total. Most of it comes from two steps: adding share_type and σ (+13) and giving each type its own weights (+5). After that, extra complexity mostly changes how stable the model is, not how accurate it is. The stepwise step ends exactly at Model 4a at α\*, because it removes both extra terms.

Part of [Calibration](../threads/m-calibration.md).


<div class="backlinks" markdown>

**Linked from** [Calibration](../threads/m-calibration.md) · [Final model](m-final-model.md) · [Grouped cross-validation](../concepts/m-grouped-cross-validation.md) · [RQ1 rebuilt with grouped CV](../progress/m-progress-21-07-2026.md)

</div>
