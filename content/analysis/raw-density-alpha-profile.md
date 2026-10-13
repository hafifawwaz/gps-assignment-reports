---
source: report/analysis/raw-density-alpha-profile.md
date: 29-07-2026
kind: analysis
comments: true
generated: 2026-10-13T20:05:33
---

# Raw-density alpha profile

<p class="doc-meta"><span class="chip chip-analysis">Analysis</span> <span class="chip chip-date">29-07-2026</span></p>

Profile likelihood on Model 4a, both datasets ([Alpha calibration](alpha-calibration.md)):

| α | Downsampled LL(b) | Raw-density LL(b) |
|---:|---:|---:|
| 1.0 | -0.6881 | -0.7127 |
| 2.4297 | **-0.6701** | -0.6928 |
| 3.0 | -0.6707 | -0.6924 |
| 4.0 | -0.6725 | -0.6920 |
| 4.6159 | | **-0.6919** |
| 6.0 | | -0.6920 |

Downsampled data has a **sharp** peak at 2.4-2.6. Raw density peaks at 4.6159, but LL(b) stays within 0.0009 of its maximum across α = 3-6: a real optimum, much less precisely identified.

Part of [Raw-density refit](raw-density-refit.md).


<div class="backlinks" markdown>

**Linked from** [Alpha calibration](alpha-calibration.md) · [Complexity and transfer](../threads/complexity-and-transfer.md) · [Does downsampling matter?](../progress/progress-29-07-2026.md) · [Raw-density refit](raw-density-refit.md)

</div>
