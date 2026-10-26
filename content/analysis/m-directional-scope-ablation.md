---
source: report/analysis/m-directional-scope-ablation.md
date: 21-07-2026
kind: analysis
comments: true
generated: 2026-10-26T20:41:14
---

# Directional scope ablation (3a vs 3b)

<p class="doc-meta"><span class="chip chip-analysis">Analysis</span> <span class="chip chip-project">Master</span> <span class="chip chip-date">21-07-2026</span></p>

Is [f_directional](../concepts/m-f-directional.md) useful only for streets? Two versions were compared. 3a is [Model 2: share-type and sigma](m-model-2-share-type-sigma.md) unchanged, with the direction score for every candidate. 3b sets the direction score to 0 for buildings and open spaces, so only streets keep it:


$$V_k = w_1 f_\text{distribution} + w_2 f_\text{distance} + w_3 f_\text{dir,street} + w_4\,share_\text{bldg} + w_5\,share_\text{street} + w_6\,share_\text{os} + w_7\,\sigma$$


Both versions have 7 parameters, so they can be compared directly.

| R=10 m | 3a: shared | 3b: street only |
|---|---:|---:|
| LL(b) | **-0.7359** | -0.7503 |
| Accuracy | **0.673** | 0.671 |
| Building / street / open space | 0.851 / **0.459** / 0.382 | **0.861** / 0.422 / **0.387** |
| CV accuracy (grouped) | **0.666 ± 0.035** | 0.655 ± 0.027 |
| Condition number | **115** | 216 |

- Keeping the score only for streets does not help. The fit is worse and the model is less stable (the direction score's VIF is 7.87 instead of 7.12, and the condition number almost doubles).
- It mainly **moves** accuracy from street to building.
- In 3b, `share_bldg` gets stronger (t goes from 2.82 to 3.59). So how the direction score is set up changes what `share_bldg` picks up.

3a was kept. The same result came back later with the tuned α, in [f_directional: shared vs split](m-f-directional-shared-vs-split.md). Next: [Model 4a: alternative-specific parameters](m-model-4a-alternative-specific.md). Part of [Calibration](../threads/m-calibration.md).


<div class="backlinks" markdown>

**Linked from** [Calibration](../threads/m-calibration.md) · [MNL model development](../progress/m-progress-19-07-2026.md) · [Model 2: share-type and sigma](m-model-2-share-type-sigma.md) · [Model progression](m-model-progression-table.md) · [f_directional](../concepts/m-f-directional.md) · [f_directional: shared vs split](m-f-directional-shared-vs-split.md)

</div>
