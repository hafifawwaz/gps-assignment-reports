---
source: report/analysis/m-directional-scope-ablation.md
date: 21-07-2026
kind: analysis
comments: true
generated: 2026-10-14T14:44:07
---

# Directional scope ablation (3a vs 3b)

<p class="doc-meta"><span class="chip chip-analysis">Analysis</span> <span class="chip chip-project">Master</span> <span class="chip chip-date">21-07-2026</span></p>

Is [f_directional](../notes/m-f-directional.md) useful only for streets? Two versions were compared. 3a is [Model 2: share-type and sigma](m-model-2-share-type-sigma.md) unchanged, with the direction score for every candidate. 3b sets the direction score to 0 for buildings and open spaces, so only streets keep it:


$$V_k = w_1 f_\text{distribution} + w_2 f_\text{distance} + w_3 f_\text{dir,street} + w_4\,share_\text{bldg} + w_5\,share_\text{street} + w_6\,share_\text{os} + w_7\,\sigma$$


Both versions have 7 parameters, so they can be compared directly.

| R=10 m | 3a: shared | 3b: street only |
|---|---:|---:|
| LL(b) | **-0.7510** | -0.7520 |
| Accuracy | **0.668** | 0.666 |
| Building / street / open space | 0.872 / **0.362** / 0.398 | 0.872 / 0.335 / **0.414** |
| CV accuracy (grouped) | **0.664 ± 0.046** | 0.658 ± 0.040 |
| Condition number | **117** | 135 |

- Keeping the score only for streets does not help. The fit is a little worse and the model is less stable (the direction score's VIF is 9.26 instead of 7.11).
- It only **moves** accuracy from street to open space.
- In 3b, `share_bldg` becomes significant (t goes from 0.76 to 2.54). So whether `share_bldg` matters depends on how the direction score is set up.

3a was kept. The same result came back later with the tuned α, in [f_directional: shared vs split](m-f-directional-shared-vs-split.md). Next: [Model 4a: alternative-specific parameters](m-model-4a-alternative-specific.md). Part of [Calibration](../threads/m-calibration.md).


<div class="backlinks" markdown>

**Linked from** [Calibration](../threads/m-calibration.md) · [MNL model development](../progress/m-progress-19-07-2026.md) · [Model 2: share-type and sigma](m-model-2-share-type-sigma.md) · [Model progression](m-model-progression-table.md) · [f_directional](../notes/m-f-directional.md) · [f_directional: shared vs split](m-f-directional-shared-vs-split.md)

</div>
