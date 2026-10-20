---
source: report/progress/m-progress-19-07-2026.md
date: 19-07-2026
kind: progress
comments: true
generated: 2026-10-20T15:44:29
---

# MNL model development

<p class="doc-meta"><span class="chip chip-progress">Progress</span> <span class="chip chip-project">Master</span> <span class="chip chip-date">19-07-2026</span></p>

The first time the model was fitted to the cleaned ground truth (907 stays with known answers). MNL is the type of model used here: it turns scores into probabilities (see [Glossary](../notes/glossary.md)).

- **Search distance.** A search distance (`R_buffer`) of **10 m** works better than 15 m for every model tried: [R_buffer: 10 m vs 15 m](../analysis/m-r-buffer-10m-vs-15m.md).
- **Six models compared**, each adding something to the one before: [Model 1: base](../analysis/m-model-1-base.md) → [Model 2: share-type and sigma](../analysis/m-model-2-share-type-sigma.md) → [Directional scope ablation (3a vs 3b)](../analysis/m-directional-scope-ablation.md) → [Model 4a: alternative-specific parameters](../analysis/m-model-4a-alternative-specific.md) → [Model 5: alternative-specific constants (rejected)](../analysis/m-model-5-asc-rejected.md) → [Interaction term screen (α = 1)](../analysis/m-interaction-term-screen.md). Accuracy (the share of stays with the correct type) rose from 0.540 to 0.733.
- **α.** The setting α controls how fast the distance score drops with distance. It was tuned to 2.76 on Model 4a ([Alpha calibration](../analysis/m-alpha-calibration.md)). With α at 2.76, the extra term f_distance² was no longer useful and was removed ([The f_distance² artifact](../analysis/m-f-distance-squared-artifact.md)).
- **Best model at that time.** Separate weights for each place type (Model 4a at the tuned α). 13 parameters, accuracy 0.733. The combined term f_distribution × share_type is significant on its own, but it overlaps too much with the other terms to keep ([Stepwise VIF elimination](../analysis/m-stepwise-vif-elimination.md)).
- **High VIF values.** Some important terms have high VIF values (a warning sign that terms overlap). Here that comes from how the model is built, and it is not a mistake: [Multicollinearity is structural](../notes/m-multicollinearity-is-structural.md).

Later corrected by [RQ1 rebuilt with grouped CV](m-progress-21-07-2026.md).


<div class="backlinks" markdown>

**Linked from** [Assignment framework](../threads/m-assignment-framework.md) · [Calibration](../threads/m-calibration.md) · [Thesis summary](../threads/m-thesis-summary.md)

</div>
