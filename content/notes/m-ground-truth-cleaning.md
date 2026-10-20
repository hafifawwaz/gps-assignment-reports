---
source: report/notes/m-ground-truth-cleaning.md
date: 23-07-2026
kind: note
comments: true
generated: 2026-10-20T15:22:17
---

# Ground truth cleaning

<p class="doc-meta"><span class="chip chip-note">Note</span> <span class="chip chip-project">Master</span> <span class="chip chip-date">23-07-2026</span></p>

How the survey records were cleaned before use, as written in the final thesis (Section 3.3.4).

First, the self-report forms were checked against the GPS tracks:

- Rows for different floors of the same visit, with the same start and end time, become one stop.
- Four entries had a typo in one time field (one hour or twelve hours off). Each was corrected using the stops before and after, the time the form was sent, and the GPS track.
- One session ran over two days. Each of its stops gets the day on which the session's GPS covers the reported time.
- Four form windows were filled in after the session and covered several stops of different place types under one time block. No single answer fits such a window, so these stops were left out.

| Step | Count |
|---|---:|
| Stops after these checks | 301 |
| Stay records, one per phone | 1,017 |
| Records with at least one GPS point in the reported time window | 975 |
| After removing stays with no matching entity polygon (chiefly the Shareo and Kamiyacho underground arcades) and a few dropped after manual verification | **907** (280 stops) |

No filter on point count or length is applied, so a few very short stays remain (after downsampling, 20 stays have one point and 13 have two). Some phones ran out of battery during several sessions. That explains most of the 42 records without GPS points, and it affected some participants and sessions more than others. The last cleaning step is listed stop by stop in [Ground truth drop list](../analysis/m-drop-list.md).

An earlier draft of the thesis gave 956 as the count before the second step. The saved data showed 975, and the final thesis uses 975.

Result: [Ground truth dataset](m-ground-truth-dataset.md). Part of [Ground truth data](../threads/m-ground-truth-data.md).


<div class="backlinks" markdown>

**Linked from** [Ground truth data](../threads/m-ground-truth-data.md) · [Ground truth dataset](m-ground-truth-dataset.md) · [Ground truth drop list](../analysis/m-drop-list.md) · [RQ2 diagnostics and RQ3 ceiling check](../progress/m-progress-23-07-2026.md) · [Thesis bug fixes and adopted rerun](../inbox/thesis-bug-fix.md) · [Thesis summary](../threads/m-thesis-summary.md)

</div>
