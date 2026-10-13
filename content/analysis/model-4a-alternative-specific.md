---
source: report/analysis/model-4a-alternative-specific.md
date: 21-07-2026
kind: analysis
comments: true
generated: 2026-10-13T20:30:42
---

# Model 4a: alternative-specific parameters

<p class="doc-meta"><span class="chip chip-analysis">Analysis</span> <span class="chip chip-date">21-07-2026</span></p>

Every score gets **its own weight per type**; [sigma](../notes/sigma.md) stays shared. 13 parameters:


$$V_t = w_{1,t} f_\text{distribution} + w_{2,t} f_\text{distance} + w_{3,t} f_\text{directional} + w_{4,t}\,share_t + w_5\,\sigma$$


| | Model 4a (R=10 m, α=1) |
|---|---:|
| ρ² vs LL(C) | 0.265 |
| LR vs 3a (df=6) | 114.15, p < 1e-16 |
| Accuracy | 0.717 |
| Building / street / open space | 0.902 / 0.443 / 0.466 |
| CV accuracy (grouped) | 0.707 ± 0.069 |
| Condition number | 775 |

**All three types improve at once** for the first time (building +3 pp, street +8.1 pp, open space +6.8 pp). Max VIF 10.69 on `f_directional_street`; the high within-type correlations are [Multicollinearity is structural](../notes/multicollinearity-is-structural.md).

`f_distance_bldg` and `f_distance_street` are not individually significant (t = 0.29, 0.34): part of the distance signal is absorbed by share and sigma once split by type.

Becomes the base for everything after. Next: [Model 5: alternative-specific constants (rejected)](model-5-asc-rejected.md), [Interaction term screen (α = 1)](interaction-term-screen.md). Alpha is calibrated on this model: [Alpha calibration](alpha-calibration.md). Part of [Calibration](../threads/calibration.md).


<div class="backlinks" markdown>

**Linked from** [Calibration](../threads/calibration.md) · [Directional scope ablation (3a vs 3b)](directional-scope-ablation.md) · [Interaction term screen (α = 1)](interaction-term-screen.md) · [MNL model development](../progress/progress-19-07-2026.md) · [Model 5: alternative-specific constants (rejected)](model-5-asc-rejected.md) · [Model 6, re-derived at calibrated alpha](model-6-rederived.md) · [Model progression](model-progression-table.md) · [Multicollinearity is structural](../notes/multicollinearity-is-structural.md)

</div>
