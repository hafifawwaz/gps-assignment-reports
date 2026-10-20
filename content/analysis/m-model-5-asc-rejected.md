---
source: report/analysis/m-model-5-asc-rejected.md
date: 21-07-2026
kind: analysis
comments: true
generated: 2026-10-20T15:44:29
---

# Model 5: alternative-specific constants (rejected)

<p class="doc-meta"><span class="chip chip-analysis">Analysis</span> <span class="chip chip-project">Master</span> <span class="chip chip-date">21-07-2026</span></p>

[Model 4a: alternative-specific parameters](m-model-4a-alternative-specific.md) plus two constants, `asc_street` and `asc_os`. A constant (ASC) is a fixed extra value for each type, which shows whether a type is preferred in general. Building is the reference ($ASC_\text{bldg} = 0$). In total, 15 parameters:


$$V_t = w_{1,t} f_\text{distribution} + w_{2,t} f_\text{distance} + w_{3,t} f_\text{directional} + w_{4,t}\,share_t + w_5\,\sigma + ASC_t$$


| | 4a | 5 (+ ASC) |
|---|---:|---:|
| Accuracy | 0.722 | 0.728 |
| CV accuracy (grouped) | 0.700 ± 0.036 | 0.719 ± 0.033 |
| LR vs 4a (df=2) | | 35.6, p < 0.0001 |
| Max VIF | 8.83 | **30.57** |
| Condition number | 737 | **2,027** |

On paper, the constants are significant, and accuracy on unseen data also goes up (by less than the normal spread between test sets). But **`asc_street` and `f_directional_street` move almost together (r = 0.94)**. The reason: [f_directional](../notes/m-f-directional.md) hardly changes between street candidates, so it acts almost like a constant for streets. The model is asked to measure the same "street-ness" twice. As a result, the weight of the street direction score **changes sign**, from +3.46 in Model 4a to -5.30, so the two weights can no longer be read on their own.

With the tuned α it gets worse: each constant also moves almost together with its own f_distance score (`asc_t` and `f_distance_t`, r = 0.99), and the highest VIF rises to 95. With a 15 m search distance the model behaves about the same as at 10 m (accuracy on unseen data 0.714 ± 0.019, condition number 1,827).

**Rejected, because its weights cannot be trusted.** It is not a case of overfitting: the gain on unseen data is real, but it comes from a near-copy of another input ([Overfitting signature](../notes/m-overfitting-signature.md)). Part of [Calibration](../threads/m-calibration.md).


<div class="backlinks" markdown>

**Linked from** [Alpha calibration](m-alpha-calibration.md) · [Calibration](../threads/m-calibration.md) · [MNL model development](../progress/m-progress-19-07-2026.md) · [Model 4a: alternative-specific parameters](m-model-4a-alternative-specific.md) · [Model progression](m-model-progression-table.md) · [Multicollinearity is structural](../notes/m-multicollinearity-is-structural.md) · [Overfitting signature](../notes/m-overfitting-signature.md) · [Publications and doctoral plan](../progress/d-progress-20-10-2026.md) · [RQ1 rebuilt with grouped CV](../progress/m-progress-21-07-2026.md) · [Thesis bug fixes and adopted rerun](../inbox/thesis-bug-fix.md) · [f_directional](../notes/m-f-directional.md)

</div>
