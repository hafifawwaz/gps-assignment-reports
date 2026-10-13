---
source: report/analysis/directional-scope-ablation.md
date: 21-07-2026
kind: analysis
comments: true
generated: 2026-10-13T20:30:42
---

# Directional scope ablation (3a vs 3b)

<p class="doc-meta"><span class="chip chip-analysis">Analysis</span> <span class="chip chip-date">21-07-2026</span></p>

Does [f_directional](../notes/f-directional.md) only mean something for streets? Both variants have 7 parameters, so they compare directly (not nested).

| R=10 m | 3a: shared | 3b: street only |
|---|---:|---:|
| LL(b) | **-0.7510** | -0.7520 |
| Accuracy | **0.668** | 0.666 |
| Building / street / open space | 0.872 / **0.362** / 0.398 | 0.872 / 0.335 / **0.414** |
| CV accuracy (grouped) | **0.664 ± 0.046** | 0.658 ± 0.040 |
| Condition number | **117** | 135 |

- Restricting to streets does not help: marginally worse fit, worse conditioning (directional VIF 9.26 vs 7.11).
- It only **trades** street accuracy for open-space accuracy.
- `share_bldg` turns significant in 3b (t 0.76 → 2.54) as a side effect, so its significance depends on how the directional term is scoped.

3a carried forward. Reconfirmed at calibrated alpha in [f_directional: shared vs split](f-directional-shared-vs-split.md). Next: [Model 4a: alternative-specific parameters](model-4a-alternative-specific.md). Part of [Calibration](../threads/calibration.md).


<div class="backlinks" markdown>

**Linked from** [Calibration](../threads/calibration.md) · [MNL model development](../progress/progress-19-07-2026.md) · [Model 2: share-type and sigma](model-2-share-type-sigma.md) · [Model progression](model-progression-table.md) · [f_directional](../notes/f-directional.md) · [f_directional: shared vs split](f-directional-shared-vs-split.md)

</div>
