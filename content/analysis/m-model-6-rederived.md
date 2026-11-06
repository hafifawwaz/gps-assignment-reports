---
source: report/analysis/m-model-6-rederived.md
date: 21-07-2026
kind: analysis
comments: true
generated: 2026-11-06T11:37:20
---

# Model 6, re-derived at calibrated alpha

<p class="doc-meta"><span class="chip chip-analysis">Analysis</span> <span class="chip chip-project">Master</span> <span class="chip chip-date">21-07-2026</span></p>

Model 6 built again with the tuned α (2.979). It starts from [Model 4a: alternative-specific parameters](m-model-4a-alternative-specific.md) and adds the two terms that still passed the test with the new α: σ² and f_distribution × share_type. In total, 15 parameters:


$$V_t = w_{1,t} f_\text{distribution} + w_{2,t} f_\text{distance} + w_{3,t} f_\text{directional} + w_{4,t}\,share_t + w_5\,\sigma + w_6\,\sigma^2 + w_7\,(f_\text{distribution}\times share_\text{type})$$


| | 4a at α\* | Model 6 re-derived |
|---|---:|---:|
| LL(b) | -0.6453 | -0.6355 |
| LR vs 4a at α\* (df=2) | | 17.73, p < 0.001 |
| Accuracy | 0.727 | 0.722 |
| CV accuracy (grouped) | 0.710 ± 0.030 | 0.698 ± 0.043 |
| Condition number | 2,036 | 11,696 |
| Max VIF | 25.85 (f_distance, street) | 36.70 (σ) |

The fit is significantly better, but accuracy drops a little, also on unseen data, and the model becomes much less stable (condition number from 2,036 to 11,696). σ² again adds little (t = 0.15). Next: [Stepwise VIF elimination](m-stepwise-vif-elimination.md). Part of [Calibration](../threads/m-calibration.md).


<div class="backlinks" markdown>

**Linked from** [Calibration](../threads/m-calibration.md) · [Interaction term screen (α = 1)](m-interaction-term-screen.md) · [Model progression](m-model-progression-table.md) · [Stepwise VIF elimination](m-stepwise-vif-elimination.md) · [The f_distance² artifact](m-f-distance-squared-artifact.md)

</div>
