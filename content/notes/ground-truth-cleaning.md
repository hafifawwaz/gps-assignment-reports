---
source: report/notes/ground-truth-cleaning.md
date: 23-07-2026
kind: note
comments: true
generated: 2026-10-13T20:05:33
---

# Ground truth cleaning

<p class="doc-meta"><span class="chip chip-note">Note</span> <span class="chip chip-date">23-07-2026</span></p>

From the final thesis (Section 3.3.4):

| Step | Stay clusters |
|---|---:|
| Stop records from the experiment | 1,029 |
| After removing incomplete self-reports, failed or too-sparse GPS logs, and stops that could not be verified from the trajectory | 975 |
| After removing stays with no matching entity polygon (chiefly the Shareo and Kamiyacho underground arcades) and a few dropped after manual verification | **907** |

Battery failures on several devices are part of the 1,029 → 975 drop; that attrition was uneven across participants and sessions. The second round is listed stop by stop in [Ground truth drop list](../analysis/drop-list.md).

An earlier draft stated 956 before the second round; the saved data showed 975, and the final thesis uses 975.

Result: [Ground truth dataset](ground-truth-dataset.md). Part of [Ground truth data](../threads/ground-truth-data.md).


<div class="backlinks" markdown>

**Linked from** [Ground truth data](../threads/ground-truth-data.md) · [Ground truth dataset](ground-truth-dataset.md) · [Ground truth drop list](../analysis/drop-list.md) · [RQ2 diagnostics and RQ3 ceiling check](../progress/progress-23-07-2026.md) · [Thesis summary](../threads/thesis-summary.md)

</div>
