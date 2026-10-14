---
source: report/analysis/m-model-6-rederived.md
date: 21-07-2026
kind: analysis
comments: true
generated: 2026-10-14T14:44:07
---

# Model 6, re-derived at calibrated alpha

<p class="doc-meta"><span class="chip chip-analysis">Analysis</span> <span class="chip chip-project">Master</span> <span class="chip chip-date">21-07-2026</span></p>

Model 6 built again with the tuned α (2.4297). It starts from [Model 4a: alternative-specific parameters](m-model-4a-alternative-specific.md) and adds the two terms that still passed the test with the new α: σ² and f_distribution × share_type. In total, 15 parameters:


$$V_t = w_{1,t} f_\text{distribution} + w_{2,t} f_\text{distance} + w_{3,t} f_\text{directional} + w_{4,t}\,share_t + w_5\,\sigma + w_6\,\sigma^2 + w_7\,(f_\text{distribution}\times share_\text{type})$$


| | 4a at α\* | Model 6 re-derived |
|---|---:|---:|
| LL(b) | -0.6701 | -0.6520 |
| LR vs 4a at α\* (df=2) | | 32.72, p < 1e-7 |
| Accuracy | 0.723 | 0.723 |
| CV accuracy (grouped) | 0.717 ± 0.065 | 0.710 ± 0.075 |
| Condition number | 2,338 | 14,851 |
| Max VIF | | 18.38 (σ²) |

The fit is significantly better, but the model becomes much less stable (condition number from 2,338 to 14,851). σ² again adds little. Next: [Stepwise VIF elimination](m-stepwise-vif-elimination.md). Part of [Calibration](../threads/m-calibration.md).


<div class="backlinks" markdown>

**Linked from** [Calibration](../threads/m-calibration.md) · [Interaction term screen (α = 1)](m-interaction-term-screen.md) · [Model progression](m-model-progression-table.md) · [Stepwise VIF elimination](m-stepwise-vif-elimination.md) · [The f_distance² artifact](m-f-distance-squared-artifact.md)

</div>
