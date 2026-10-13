---
source: report/analysis/drop-list.md
date: 23-07-2026
kind: analysis
comments: true
generated: 2026-10-13T16:57:34
---

# Ground truth drop list

<p class="doc-meta"><span class="chip chip-analysis">Analysis</span> <span class="chip chip-date">23-07-2026</span></p>

The last cleaning round dropped stops with no matching entity polygon: **21 physical stops** (68 stay records, 975 → 907).

| Category | Stops | Rule |
|---|---:|---|
| Underground | 10 | Location in the Shareo or Kamiyacho underground arcades, which ZTOWN does not capture ([Spatial entity layers](../notes/spatial-entity-layers.md)) |
| Manual verification | 11 | Checked one by one against the self-report record |

Manual-verification stops (location names as reported; participant codes left out on purpose):

- City Bakery, Minamoa
- RIDERS Motomachi, Hiroshima Gate Park
- Starbucks Hiroshima City Central Park
- Hirogin HD (Hiroshima Bank head office branch)
- Omnibus Roasters Motomachi
- Fukuya to Taito Station underground passage (named "underground" but not in Shareo/Kamiyacho, so classed here)
- Bus stop, Hiroshima Station
- Hiroshima National Peace Memorial Hall for the Atomic Bomb Victims
- Pride of Hiroshima, Hiroshima Gate Park
- Lawson Shimint
- Coco's Restaurant Danbara

All 21 names were cross-checked against the raw self-report data and matched.

Where this round sits in the whole cleaning chain: [Ground truth cleaning](../notes/ground-truth-cleaning.md).

Part of [Chapter 3: Data and ground truth](../progress/ch3-data.md).


<div class="backlinks" markdown>

**Linked from** [Chapter 3: Data and ground truth](../progress/ch3-data.md) · [Ground truth cleaning](../notes/ground-truth-cleaning.md) · [RQ2 diagnostics and RQ3 ceiling check](../progress/progress-23-07-2026.md) · [Spatial entity layers](../notes/spatial-entity-layers.md)

</div>
