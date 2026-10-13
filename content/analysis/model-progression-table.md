---
source: report/analysis/model-progression-table.md
date: 21-07-2026
kind: analysis
comments: true
generated: 2026-10-13T16:57:34
---

# Model progression

<p class="doc-meta"><span class="chip chip-analysis">Analysis</span> <span class="chip chip-date">21-07-2026</span></p>

Every model refit under [Grouped cross-validation](../notes/grouped-cross-validation.md), `R_buffer` = 10 m unless noted.

| Model | α | Params | Accuracy | CV accuracy (grouped) | Condition no. |
|---|---:|---:|---:|---:|---:|
| [Model 1: base](model-1-base.md) | 1 | 4 | 0.518 | 0.514 ± 0.089 | 36 |
| [Model 1: base](model-1-base.md), 15 m | 1 | 4 | 0.509 | 0.512 ± 0.098 | 26 |
| [Model 2: share-type and sigma](model-2-share-type-sigma.md) | 1 | 7 | 0.668 | 0.664 ± 0.046 | 117 |
| [Model 2: share-type and sigma](model-2-share-type-sigma.md), 15 m | 1 | 7 | 0.654 | 0.647 ± 0.042 | 98 |
| 3b, [Directional scope ablation (3a vs 3b)](directional-scope-ablation.md) | 1 | 7 | 0.666 | 0.658 ± 0.040 | 135 |
| [Model 4a: alternative-specific parameters](model-4a-alternative-specific.md) | 1 | 13 | 0.717 | 0.707 ± 0.069 | 775 |
| [Model 5: alternative-specific constants (rejected)](model-5-asc-rejected.md) | 1 | 15 | 0.728 | 0.717 ± 0.068 | 37,583 |
| Model 6, [Interaction term screen (α = 1)](interaction-term-screen.md) | 1 | 16 | 0.724 | 0.711 ± 0.077 | 20,695 |
| Model 4a at α\* | 2.43 | 13 | 0.723 | 0.717 ± 0.065 | 2,338 |
| [Model 6, re-derived at calibrated alpha](model-6-rederived.md) | 2.43 | 15 | 0.723 | 0.710 ± 0.075 | 14,851 |
| [Stepwise VIF elimination](stepwise-vif-elimination.md) | 2.43 | 14 | 0.724 | 0.709 ± 0.075 | 2,430 |
| **[Final model](final-model.md)** | 2.43 | **12** | 0.721 | **0.716 ± 0.076** | **1,373** |

Accuracy climbs about 20 points, mostly from two steps: adding share-type and σ (+15) and going alternative-specific (+5). After that, complexity mostly moves conditioning, not accuracy.

Part of [Chapter 5: Results](../progress/ch5-results.md).


<div class="backlinks" markdown>

**Linked from** [Chapter 5: Results](../progress/ch5-results.md) · [Final model](final-model.md) · [Grouped cross-validation](../notes/grouped-cross-validation.md) · [RQ1 rebuilt with grouped CV](../progress/progress-21-07-2026.md)

</div>
