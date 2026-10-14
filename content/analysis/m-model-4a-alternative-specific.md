---
source: report/analysis/m-model-4a-alternative-specific.md
date: 21-07-2026
kind: analysis
comments: true
generated: 2026-10-14T14:44:07
---

# Model 4a: alternative-specific parameters

<p class="doc-meta"><span class="chip chip-analysis">Analysis</span> <span class="chip chip-project">Master</span> <span class="chip chip-date">21-07-2026</span></p>

In this model, every score gets **its own weight for each place type** (building, street, open space). This is called "alternative-specific". [sigma](../notes/m-sigma.md) keeps one shared weight. In total, 13 parameters:


$$V_t = w_{1,t} f_\text{distribution} + w_{2,t} f_\text{distance} + w_{3,t} f_\text{directional} + w_{4,t}\,share_t + w_5\,\sigma$$


| | Model 4a (R=10 m, α=1) |
|---|---:|
| ρ² vs LL(C) | 0.265 |
| LR vs 3a (df=6) | 114.15, p < 1e-16 |
| Accuracy | 0.717 |
| Building / street / open space | 0.902 / 0.443 / 0.466 |
| CV accuracy (grouped) | 0.707 ± 0.069 |
| Condition number | 775 |

The LR test compares this model with model 3a, which has shared weights. The result is very clear (p < 1e-16): separate weights per type fit much better.

For the first time, **all three types improve together** (building +3 percentage points, street +8.1, open space +6.8). The highest VIF is 10.69, for `f_directional_street`. The strong overlap between inputs of the same type is explained in [Multicollinearity is structural](../notes/m-multicollinearity-is-structural.md).

`f_distance_bldg` and `f_distance_street` are not significant on their own (t = 0.29 and 0.34). Once weights are split by type, part of the distance information is picked up by share and sigma.

All later models build on this one. Next: [Model 5: alternative-specific constants (rejected)](m-model-5-asc-rejected.md), [Interaction term screen (α = 1)](m-interaction-term-screen.md). α was tuned on this model: [Alpha calibration](m-alpha-calibration.md). Part of [Calibration](../threads/m-calibration.md).


<div class="backlinks" markdown>

**Linked from** [Calibration](../threads/m-calibration.md) · [Directional scope ablation (3a vs 3b)](m-directional-scope-ablation.md) · [Interaction term screen (α = 1)](m-interaction-term-screen.md) · [MNL model development](../progress/m-progress-19-07-2026.md) · [Model 5: alternative-specific constants (rejected)](m-model-5-asc-rejected.md) · [Model 6, re-derived at calibrated alpha](m-model-6-rederived.md) · [Model progression](m-model-progression-table.md) · [Multicollinearity is structural](../notes/m-multicollinearity-is-structural.md)

</div>
