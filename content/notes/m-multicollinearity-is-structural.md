---
source: report/notes/m-multicollinearity-is-structural.md
date: 19-07-2026
kind: note
comments: true
generated: 2026-10-14T14:44:07
---

# Multicollinearity is structural

<p class="doc-meta"><span class="chip chip-note">Note</span> <span class="chip chip-project">Master</span> <span class="chip chip-date">19-07-2026</span></p>

Why some warning numbers (VIF above 10) are expected in this model and are not a mistake.

When each type gets its own weights, the inputs for one type (`f_distance_t`, `f_directional_t`, `share_t`) all come from the same list of candidates of that stay. So they move together closely (correlation often r = 0.86-0.94). This overlap is called multicollinearity, and it raises the VIF of important terms above 10.

The overlap comes from how the model is built. It does not mean some inputs are useless copies. To push every VIF below 10, some of these separate weights would have to go, and they are the reason this model works better than the simpler ones ([Model 4a: alternative-specific parameters](../analysis/m-model-4a-alternative-specific.md)). So when weak terms were removed step by step, these important terms were protected ([Stepwise VIF elimination](../analysis/m-stepwise-vif-elimination.md)).

One kind of overlap *is* a real problem: an ASC term (a fixed extra value per type) that copies an input which barely changes within its type ([Model 5: alternative-specific constants (rejected)](../analysis/m-model-5-asc-rejected.md)).

Visible in [Final model correlation matrix](../analysis/m-final-model-correlation-matrix.md). Part of [Calibration](../threads/m-calibration.md).


<div class="backlinks" markdown>

**Linked from** [Calibration](../threads/m-calibration.md) · [Final model](../analysis/m-final-model.md) · [Final model correlation matrix](../analysis/m-final-model-correlation-matrix.md) · [MNL model development](../progress/m-progress-19-07-2026.md) · [Model 4a: alternative-specific parameters](../analysis/m-model-4a-alternative-specific.md) · [Stepwise VIF elimination](../analysis/m-stepwise-vif-elimination.md)

</div>
