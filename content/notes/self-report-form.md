---
source: report/notes/self-report-form.md
date: 23-07-2026
kind: note
comments: true
generated: 2026-10-13T16:57:34
---

# Self-report form

<p class="doc-meta"><span class="chip chip-note">Note</span> <span class="chip chip-date">23-07-2026</span></p>

Every stop, controlled or free roam, was logged with this form at the time of the stop (325 raw rows). Its start and end times define the stay window.

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

"Building-attached Outdoor" is merged into open space in the model, a simplification listed in [Limitations](limitations.md).

Part of [Experiment design](experiment-design.md).


<div class="backlinks" markdown>

**Linked from** [Chapter 3: Data and ground truth](../progress/ch3-data.md) · [Experiment design](experiment-design.md) · [Limitations](limitations.md) · [RQ2 diagnostics and RQ3 ceiling check](../progress/progress-23-07-2026.md)

</div>
