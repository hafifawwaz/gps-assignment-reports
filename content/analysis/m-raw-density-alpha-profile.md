---
source: report/analysis/m-raw-density-alpha-profile.md
date: 29-07-2026
kind: analysis
comments: true
generated: 2026-11-06T11:37:20
---

# Raw-density alpha profile

<p class="doc-meta"><span class="chip chip-analysis">Analysis</span> <span class="chip chip-project">Master</span> <span class="chip chip-date">29-07-2026</span></p>

How the fit changes with α, for the downsampled data and for the full data. Same method as in [Alpha calibration](m-alpha-calibration.md), using Model 4a. LL(b) closer to 0 means a better fit.

| α | Downsampled LL(b) | Raw-density LL(b) |
|---:|---:|---:|
| 1.0 | -0.6731 | -0.7154 |
| 2.0 | -0.6494 | -0.6913 |
| 2.979 | **-0.6453** | |
| 3.0 | -0.6453 | -0.6855 |
| 4.0 | -0.6461 | -0.6828 |
| 5.0 | -0.6447 | -0.6812 |
| 6.0 | -0.6437 | **-0.6804** |

With downsampled data, the fit has an inside best point at α = 2.979. It is almost flat above α ≈ 2.4, and it rises slowly again above α ≈ 4 (at α = 6 it is higher by 1.4 total log-likelihood units, which is not significant). With the full data, there is no inside best point: the fit keeps rising up to the search limit (α = 6). Between α = 3 and α = 6 it changes by 0.0051 per stay (4.6 in total), against 54 in total between α = 0.2 and 3. So neither version pins α down well, and the full data even less.

Part of [Raw-density refit](m-raw-density-refit.md).


<div class="backlinks" markdown>

**Linked from** [Alpha calibration](m-alpha-calibration.md) · [Complexity and transfer](../threads/m-complexity-and-transfer.md) · [Does downsampling matter?](../progress/m-progress-29-07-2026.md) · [Raw-density refit](m-raw-density-refit.md)

</div>
