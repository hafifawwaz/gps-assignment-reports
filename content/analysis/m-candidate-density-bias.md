---
source: report/analysis/m-candidate-density-bias.md
date: 23-07-2026
kind: analysis
comments: true
generated: 2026-10-14T14:44:07
---

# Candidate density bias toward building

<p class="doc-meta"><span class="chip chip-analysis">Analysis</span> <span class="chip chip-project">Master</span> <span class="chip chip-date">23-07-2026</span></p>

Why the model often says "building" when the correct answer is street or open space.

A first guess would be that street stays have too few street candidates. The data shows the opposite. Stays that really were on a street have the **most** candidates of their own type:

| True type | Same-type candidates, mean | median | Total candidates, mean |
|---|---:|---:|---:|
| Building | 7.09 | 5 | 22.99 |
| Street | **13.17** | **11** | 36.61 |
| Open space | 5.42 | 3 | 18.34 |

The [share_type](../notes/m-share-type.md) term gives a lower value to a candidate with many neighbours of the same type (the weight `share_street` is -8.09 in the [Final model](m-final-model.md)). The map stores streets as **many short pieces next to each other** ([Spatial entity layers](../notes/m-spatial-entity-layers.md)). So a stay on a street is punished for a crowd of street pieces that the map itself created. The probability then moves to the nearest building ([Confusion matrix](m-confusion-matrix.md)).

This comes from the street map, so it can be fixed. The GPS data itself does not set the limit ([Contributions](../notes/m-contributions.md)). But it weakens the argument that streets are real places of activity: [Tension with the street-space argument](../notes/m-street-space-tension.md), [Candidate density as boundary-matching difficulty](../notes/m-boundary-matching-analogy.md).

Part of [Error analysis](../threads/m-error-analysis.md).


<div class="backlinks" markdown>

**Linked from** [Candidate density as boundary-matching difficulty](../notes/m-boundary-matching-analogy.md) · [Confusion matrix](m-confusion-matrix.md) · [Contributions](../notes/m-contributions.md) · [Error analysis](../threads/m-error-analysis.md) · [Limitations](../notes/m-limitations.md) · [Model 2: share-type and sigma](m-model-2-share-type-sigma.md) · [RQ2 diagnostics and RQ3 ceiling check](../progress/m-progress-23-07-2026.md) · [Spatial entity layers](../notes/m-spatial-entity-layers.md) · [Tension with the street-space argument](../notes/m-street-space-tension.md) · [Thesis summary](../threads/m-thesis-summary.md) · [share_type](../notes/m-share-type.md)

</div>
