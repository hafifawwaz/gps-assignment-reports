---
source: report/analysis/m-drop-list.md
date: 23-07-2026
kind: analysis
comments: true
generated: 2026-10-14T14:44:07
---

# Ground truth drop list

<p class="doc-meta"><span class="chip chip-analysis">Analysis</span> <span class="chip chip-project">Master</span> <span class="chip chip-date">23-07-2026</span></p>

The last cleaning step removed stops that had no matching place on the map: **21 real stops** (68 stay records). This took the dataset from 975 to 907 stays.

| Category | Stops | Rule |
|---|---:|---|
| Underground | 10 | Location in the Shareo or Kamiyacho underground arcades, which ZTOWN does not capture ([Spatial entity layers](../notes/m-spatial-entity-layers.md)) |
| Manual verification | 11 | Checked one by one against the self-report record |

The 11 stops removed after checking by hand (place names as the participants wrote them; participant codes are left out on purpose):

- City Bakery, Minamoa
- RIDERS Motomachi, Hiroshima Gate Park
- Starbucks Hiroshima City Central Park
- Hirogin HD (Hiroshima Bank head office branch)
- Omnibus Roasters Motomachi
- Fukuya to Taito Station underground passage (named "underground", but not in Shareo or Kamiyacho, so it is in this group)
- Bus stop, Hiroshima Station
- Hiroshima National Peace Memorial Hall for the Atomic Bomb Victims
- Pride of Hiroshima, Hiroshima Gate Park
- Lawson Shimint
- Coco's Restaurant Danbara

All 21 names were checked against the raw self-report data, and all of them matched.

Where this step fits in the whole cleaning process: [Ground truth cleaning](../notes/m-ground-truth-cleaning.md).

Part of [Ground truth data](../threads/m-ground-truth-data.md).


<div class="backlinks" markdown>

**Linked from** [Ground truth cleaning](../notes/m-ground-truth-cleaning.md) · [Ground truth data](../threads/m-ground-truth-data.md) · [RQ2 diagnostics and RQ3 ceiling check](../progress/m-progress-23-07-2026.md) · [Spatial entity layers](../notes/m-spatial-entity-layers.md)

</div>
