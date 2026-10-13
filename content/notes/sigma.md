---
source: report/notes/sigma.md
date: 19-07-2026
kind: note
comments: true
generated: 2026-10-13T20:41:00
---

# sigma

<p class="doc-meta"><span class="chip chip-note">Note</span> <span class="chip chip-date">19-07-2026</span></p>

Stay-level positional dispersion,


$$\sigma_i = \sqrt{\mathrm{var}(x) + \mathrm{var}(y)}$$


Inside [f_distance](f-distance.md) it sets the decay width (5 m floor). As a model feature it is capped at the 99th percentile (179.14 m) and standardized once by `sigma_scale` = 36.708, then reused unchanged in every model:


$$\sigma_k = \begin{cases} \min(\sigma_i,\ 179.14) \,/\, 36.708 & \text{street or open-space candidate} \\ 0 & \text{building candidate} \end{cases}$$


It enters with **one shared coefficient** and building as the reference (0 for building rows). Splitting it by type is an identification problem, not a modelling option.

Clean positive effect in every model ([Model 2: share-type and sigma](../analysis/model-2-share-type-sigma.md), [Final model](../analysis/final-model.md)), yet tree models rank it far higher than its modest coefficient suggests: [Sigma in tree importance](../analysis/sigma-tree-importance.md).

Part of [Assignment framework](../threads/assignment-framework.md).


<div class="backlinks" markdown>

**Linked from** [Assignment framework](../threads/assignment-framework.md) · [Framework overview](framework-overview.md) · [Model 2: share-type and sigma](../analysis/model-2-share-type-sigma.md) · [Model 4a: alternative-specific parameters](../analysis/model-4a-alternative-specific.md) · [Sigma in tree importance](../analysis/sigma-tree-importance.md) · [f_distance](f-distance.md)

</div>
