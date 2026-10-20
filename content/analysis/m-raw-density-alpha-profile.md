---
source: report/analysis/m-raw-density-alpha-profile.md
date: 29-07-2026
kind: analysis
comments: true
generated: 2026-10-20T15:22:17
---

# Raw-density alpha profile

<p class="doc-meta"><span class="chip chip-analysis">Analysis</span> <span class="chip chip-project">Master</span> <span class="chip chip-date">29-07-2026</span></p>

How the fit changes with α, for the downsampled data and for the full data. Same method as in [Alpha calibration](m-alpha-calibration.md), using Model 4a. LL(b) closer to 0 means a better fit.

| α | Downsampled LL(b) | Raw-density LL(b) |
|---:|---:|---:|
| 1.0 | -0.6711 | -0.7139 |
| 2.0 | -0.6505 | -0.6906 |
| 2.764 | **-0.6477** | |
| 3.0 | -0.6478 | -0.6864 |
| 4.0 | -0.6491 | -0.6851 |
| 5.0 | -0.6476 | -0.6844 |
| 6.0 | -0.6466 | **-0.6841** |

With downsampled data, the fit has an inside best point at α = 2.764. It is almost flat above α ≈ 2.2, and it rises slowly again above α ≈ 4 (at α = 6 it is higher by 1.0 total log-likelihood unit, which is not significant). With the full data, there is no inside best point: the fit keeps rising up to the search limit (α = 6). Between α = 3 and α = 6 it changes by only 0.0023 per stay (2.1 in total). So neither version pins α down well, and the full data even less.

Part of [Raw-density refit](m-raw-density-refit.md).


<div class="backlinks" markdown>

**Linked from** [Alpha calibration](m-alpha-calibration.md) · [Complexity and transfer](../threads/m-complexity-and-transfer.md) · [Does downsampling matter?](../progress/m-progress-29-07-2026.md) · [Raw-density refit](m-raw-density-refit.md)

</div>
