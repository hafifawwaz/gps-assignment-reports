---
source: report/notes/m-ground-truth-dataset.md
date: 25-07-2026
kind: note
comments: true
generated: 2026-10-14T14:44:07
---

# Ground truth dataset

<p class="doc-meta"><span class="chip chip-note">Note</span> <span class="chip chip-project">Master</span> <span class="chip chip-date">25-07-2026</span></p>

The final set of stays with known correct answers: **907 stays** (one record per phone) from **280 real stops**. After thinning ([Downsampling to MILES density](m-downsampling-to-miles-density.md)), they contain 17,010 GPS points.

| Type | Stays | Share |
|---|---:|---:|
| Building | 531 | 58.5% |
| Street | 185 | 20.4% |
| Open space | 191 | 21.1% |

The mix of 59% building, 20% street and 21% open space comes from how the [Experiment design](m-experiment-design.md) planned the stops. Real people may visit these types in a different mix. This is a risk when the model is used on MILES ([Overfitting signature](m-overfitting-signature.md)).

How 1,029 stop records became 907: [Ground truth cleaning](m-ground-truth-cleaning.md).

Part of [Ground truth data](../threads/m-ground-truth-data.md).


<div class="backlinks" markdown>

**Linked from** [Contributions](m-contributions.md) · [Experiment design](m-experiment-design.md) · [Framework overview](m-framework-overview.md) · [Ground truth cleaning](m-ground-truth-cleaning.md) · [Ground truth data](../threads/m-ground-truth-data.md) · [Overfitting signature](m-overfitting-signature.md) · [Study area](m-study-area.md)

</div>
