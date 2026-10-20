---
source: report/notes/m-f-distance.md
date: 25-07-2026
kind: note
comments: true
generated: 2026-10-20T15:22:17
---

# f_distance

<p class="doc-meta"><span class="chip chip-note">Note</span> <span class="chip chip-project">Master</span> <span class="chip chip-date">25-07-2026</span></p>

How close the candidate is to the center of the stay. The score is 1 when the candidate is at the center and falls toward 0 as it gets farther away. How fast it falls depends on how spread out the stay's points are ($\sigma_i$) and on a setting $\alpha$:


$$f_{\text{distance}}(E_k, C_i) = \exp\left(-\frac{d_{ki}^2}{2(\alpha \cdot \sigma_i)^2}\right)$$


$d_{ki}$ is the distance from the stay's medoid to candidate $E_k$, and 0 when the medoid lies inside it. The medoid is the GPS point closest to the average position of the stay. $\sigma_i$ is the spread of the stay's points ([sigma](m-sigma.md)), with a minimum of 5 m. When the points are widely spread, the GPS position is less certain, so the score falls more slowly and farther places still get some credit.

**In the models:** $\alpha$ was 1.0 (not tuned) until [Alpha calibration](../analysis/m-alpha-calibration.md) set it to **2.764**. Before that, its weight changed sign between the 10 m and 15 m search distances ([Model 1: base](../analysis/m-model-1-base.md), [Model 2: share-type and sigma](../analysis/m-model-2-share-type-sigma.md)). A squared version of this score also looked useful, but only because α was wrong ([The f_distance² artifact](../analysis/m-f-distance-squared-artifact.md)).

Part of [Framework overview](m-framework-overview.md).


<div class="backlinks" markdown>

**Linked from** [Alpha calibration](../analysis/m-alpha-calibration.md) · [Assignment framework](../threads/m-assignment-framework.md) · [Framework overview](m-framework-overview.md) · [Model 1: base](../analysis/m-model-1-base.md) · [Model 2: share-type and sigma](../analysis/m-model-2-share-type-sigma.md) · [sigma](m-sigma.md)

</div>
