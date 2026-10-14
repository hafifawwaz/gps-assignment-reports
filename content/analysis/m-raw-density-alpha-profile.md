---
source: report/analysis/m-raw-density-alpha-profile.md
date: 29-07-2026
kind: analysis
comments: true
generated: 2026-10-14T14:44:07
---

# Raw-density alpha profile

<p class="doc-meta"><span class="chip chip-analysis">Analysis</span> <span class="chip chip-project">Master</span> <span class="chip chip-date">29-07-2026</span></p>

How the fit changes with α, for the thinned data and for the full data. Same method as in [Alpha calibration](m-alpha-calibration.md), using Model 4a. LL(b) closer to 0 means a better fit.

| α | Downsampled LL(b) | Raw-density LL(b) |
|---:|---:|---:|
| 1.0 | -0.6881 | -0.7127 |
| 2.4297 | **-0.6701** | -0.6928 |
| 3.0 | -0.6707 | -0.6924 |
| 4.0 | -0.6725 | -0.6920 |
| 4.6159 | | **-0.6919** |
| 6.0 | | -0.6920 |

With thinned data, the best α is **clearly** between 2.4 and 2.6. With the full data, the best α is 4.6159. But between α = 3 and α = 6, the fit changes by less than 0.0009. So the full data does have a best value, but it is much less certain.

Part of [Raw-density refit](m-raw-density-refit.md).


<div class="backlinks" markdown>

**Linked from** [Alpha calibration](m-alpha-calibration.md) · [Complexity and transfer](../threads/m-complexity-and-transfer.md) · [Does downsampling matter?](../progress/m-progress-29-07-2026.md) · [Raw-density refit](m-raw-density-refit.md)

</div>
