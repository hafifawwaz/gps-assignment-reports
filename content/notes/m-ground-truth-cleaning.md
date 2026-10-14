---
source: report/notes/m-ground-truth-cleaning.md
date: 23-07-2026
kind: note
comments: true
generated: 2026-10-14T14:44:07
---

# Ground truth cleaning

<p class="doc-meta"><span class="chip chip-note">Note</span> <span class="chip chip-project">Master</span> <span class="chip chip-date">23-07-2026</span></p>

How the survey records were cleaned before use, as written in the final thesis (Section 3.3.4).

| Step | Stay clusters |
|---|---:|
| Stop records from the experiment | 1,029 |
| After removing incomplete self-reports, failed or too-sparse GPS logs, and stops that could not be verified from the trajectory | 975 |
| After removing stays with no matching entity polygon (chiefly the Shareo and Kamiyacho underground arcades) and a few dropped after manual verification | **907** |

Some phones ran out of battery during several sessions. That is part of the drop from 1,029 to 975, and it affected some participants and sessions more than others. The second cleaning step is listed stop by stop in [Ground truth drop list](../analysis/m-drop-list.md).

An earlier draft of the thesis gave 956 as the count before the second step. The saved data showed 975, and the final thesis uses 975.

Result: [Ground truth dataset](m-ground-truth-dataset.md). Part of [Ground truth data](../threads/m-ground-truth-data.md).


<div class="backlinks" markdown>

**Linked from** [Ground truth data](../threads/m-ground-truth-data.md) · [Ground truth dataset](m-ground-truth-dataset.md) · [Ground truth drop list](../analysis/m-drop-list.md) · [RQ2 diagnostics and RQ3 ceiling check](../progress/m-progress-23-07-2026.md) · [Thesis summary](../threads/m-thesis-summary.md)

</div>
