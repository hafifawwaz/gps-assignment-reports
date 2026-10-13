---
source: report/notes/ground-truth-dataset.md
date: 25-07-2026
kind: note
comments: true
generated: 2026-10-13T20:30:42
---

# Ground truth dataset

<p class="doc-meta"><span class="chip chip-note">Note</span> <span class="chip chip-date">25-07-2026</span></p>

**907 stay clusters** (stay-level records, one per device) from **280 physical stops**, 17,010 points after [Downsampling to MILES density](downsampling-to-miles-density.md).

| Type | Stays | Share |
|---|---:|---:|
| Building | 531 | 58.5% |
| Street | 185 | 20.4% |
| Open space | 191 | 21.1% |

The 59/20/21 split comes from the [Experiment design](experiment-design.md), not from real-world movement, which is a risk for transfer to MILES ([Overfitting signature](overfitting-signature.md)).

How 1,029 stop records became 907: [Ground truth cleaning](ground-truth-cleaning.md).

Part of [Ground truth data](../threads/ground-truth-data.md).


<div class="backlinks" markdown>

**Linked from** [Contributions](contributions.md) · [Experiment design](experiment-design.md) · [Framework overview](framework-overview.md) · [Ground truth cleaning](ground-truth-cleaning.md) · [Ground truth data](../threads/ground-truth-data.md) · [Overfitting signature](overfitting-signature.md) · [Study area](study-area.md)

</div>
