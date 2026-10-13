---
source: report/notes/f-distance.md
date: 25-07-2026
kind: note
comments: true
generated: 2026-10-13T20:41:00
---

# f_distance

<p class="doc-meta"><span class="chip chip-note">Note</span> <span class="chip chip-date">25-07-2026</span></p>

Gaussian decay with distance, its width scaled by the cluster's dispersion $\sigma_i$ and a calibrated factor $\alpha$:


$$f_{\text{distance}}(E_k, C_i) = \exp\left(-\frac{d_{ki}^2}{2(\alpha \cdot \sigma_i)^2}\right)$$


$d_{ki}$ is the distance from the cluster medoid (the GPS point closest to the cluster mean) to the nearest edge of $E_k$; $\sigma_i$ is the cluster's spatial standard deviation ([sigma](sigma.md)) with a 5 m floor.

$\alpha$ was 1.0 (uncalibrated) until [Alpha calibration](../analysis/alpha-calibration.md) set it to **2.4297**. Before that, its coefficient flipped sign between radii ([Model 1: base](../analysis/model-1-base.md), [Model 2: share-type and sigma](../analysis/model-2-share-type-sigma.md)) and a squared term appeared significant for the wrong reason ([The f_distance² artifact](../analysis/f-distance-squared-artifact.md)).

Part of [Framework overview](framework-overview.md).


<div class="backlinks" markdown>

**Linked from** [Alpha calibration](../analysis/alpha-calibration.md) · [Assignment framework](../threads/assignment-framework.md) · [Framework overview](framework-overview.md) · [Model 1: base](../analysis/model-1-base.md) · [Model 2: share-type and sigma](../analysis/model-2-share-type-sigma.md) · [sigma](sigma.md)

</div>
