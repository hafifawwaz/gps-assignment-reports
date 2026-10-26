---
source: report/concepts/m-self-report-form.md
date: 23-07-2026
kind: concept
comments: true
generated: 2026-10-26T20:41:14
---

# Self-report form

<p class="doc-meta"><span class="chip chip-concept">Concept</span> <span class="chip chip-project">Master</span> <span class="chip chip-date">23-07-2026</span></p>

At every stop, planned or free, participants filled in this form on the spot. In total there are 325 raw answers. The start time and end time on the form mark where a stay begins and ends in the GPS data.

| Field | Response |
|---|---|
| Timestamp | Auto-recorded |
| Participant ID | Participant code |
| Phase | Controlled / Free roam |
| Stop sequence | Stop order within the session |
| Start Time, End Time | Time of day; together they define the stay window |
| Location Name (Please include building name) | Free text |
| Activity Description (What were you doing?) | Free text |
| Location Type | Inside Building / Street (Place for walking) / Open Space / Building-attached Outdoor (terrace or balcony) |
| Floor Number | Free text, inconsistent format (`1F`, `1f`, `1F & 2F`, `Upper 8F`, ...) |
| Sky view condition | Clear sky / Partially clear sky / Urban canyon / Enclosed |
| Indoor position | Center / Edge / Corner, or free text when moving |
| GPS Signal (Please refer to Reem san's App) | Normal / Weak / Lost, often blank |
| Geotagged Photo Upload | Image file |
| Notes (Optional) | Free text |

"Building-attached Outdoor" (for example a terrace or balcony) is counted as open space in the model. This is a simplification, listed in [Limitations](m-limitations.md).

Part of [Experiment design](m-experiment-design.md).


<div class="backlinks" markdown>

**Linked from** [Experiment design](m-experiment-design.md) · [Ground truth data](../threads/m-ground-truth-data.md) · [Limitations](m-limitations.md) · [RQ2 diagnostics and RQ3 ceiling check](../progress/m-progress-23-07-2026.md)

</div>
