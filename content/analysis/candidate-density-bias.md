---
source: report/analysis/candidate-density-bias.md
date: 23-07-2026
kind: analysis
comments: true
generated: 2026-10-13T20:30:42
---

# Candidate density bias toward building

<p class="doc-meta"><span class="chip chip-analysis">Analysis</span> <span class="chip chip-date">23-07-2026</span></p>

It is not candidate sparsity. True street stays have the **densest** same-type pool:

| True type | Same-type candidates, mean | median | Total candidates, mean |
|---|---:|---:|---:|
| Building | 7.09 | 5 | 22.99 |
| Street | **13.17** | **11** | 36.61 |
| Open space | 5.42 | 3 | 18.34 |

[share_type](../notes/share-type.md) penalizes a candidate for many same-type neighbours (`share_street` -8.09 in the [Final model](final-model.md)). Streets are drawn as **many short adjacent GIS segments** ([Spatial entity layers](../notes/spatial-entity-layers.md)), so a true street stay is penalized for density its own geometry creates. Probability then drifts to the nearest building ([Confusion matrix](confusion-matrix.md)).

This is a fixable artifact of the street layer, not a GPS-evidence ceiling ([Contributions](../notes/contributions.md)), but it undercuts the street-space motivation: [Tension with the street-space argument](../notes/street-space-tension.md), [Candidate density as boundary-matching difficulty](../notes/boundary-matching-analogy.md).

Part of [Error analysis](../threads/error-analysis.md).


<div class="backlinks" markdown>

**Linked from** [Candidate density as boundary-matching difficulty](../notes/boundary-matching-analogy.md) · [Confusion matrix](confusion-matrix.md) · [Contributions](../notes/contributions.md) · [Error analysis](../threads/error-analysis.md) · [Limitations](../notes/limitations.md) · [Model 2: share-type and sigma](model-2-share-type-sigma.md) · [RQ2 diagnostics and RQ3 ceiling check](../progress/progress-23-07-2026.md) · [Spatial entity layers](../notes/spatial-entity-layers.md) · [Tension with the street-space argument](../notes/street-space-tension.md) · [Thesis summary](../threads/thesis-summary.md) · [share_type](../notes/share-type.md)

</div>
