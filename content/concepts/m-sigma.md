---
source: report/concepts/m-sigma.md
date: 19-07-2026
kind: concept
comments: true
generated: 2026-10-26T20:41:14
---

# sigma

<p class="doc-meta"><span class="chip chip-concept">Concept</span> <span class="chip chip-project">Master</span> <span class="chip chip-date">19-07-2026</span></p>

How spread out the GPS points of one stay are. A large σ means the points are scattered, so the GPS position was uncertain.


$$\sigma_i = \sqrt{\mathrm{var}(x) + \mathrm{var}(y)}$$


$\mathrm{var}(x)$ and $\mathrm{var}(y)$ are the variances of the east-west and north-south positions.

σ is used in two places:

- **Inside [f_distance](m-f-distance.md)** it sets how fast the distance score falls, with a minimum of 5 m.
- **As its own model input.** Very large values are capped at 165.04 m (the 99th percentile). Then the value is divided by `sigma_scale` = 34.862, the standard deviation of the capped values. This scale is computed once and reused unchanged in every model:


$$\sigma_k = \begin{cases} \min(\sigma_i,\ 165.04) \,/\, 34.862 & \text{street or open-space candidate} \\ 0 & \text{building candidate} \end{cases}$$


σ gets **one weight shared by all types**, with building as the reference (0 for building rows). σ has the same value for all candidates of a stay. Giving it a separate weight per type would make the model unable to tell the weights apart, so that option is not available.

**In the models:** σ has a clear positive effect in every model ([Model 2: share-type and sigma](../analysis/m-model-2-share-type-sigma.md), [Final model](../analysis/m-final-model.md)). Tree models rank it much higher than its moderate weight suggests: [Sigma in tree importance](../analysis/m-sigma-tree-importance.md).

Part of [Assignment framework](../threads/m-assignment-framework.md).


<div class="backlinks" markdown>

**Linked from** [Assignment framework](../threads/m-assignment-framework.md) · [Framework overview](m-framework-overview.md) · [Model 2: share-type and sigma](../analysis/m-model-2-share-type-sigma.md) · [Model 4a: alternative-specific parameters](../analysis/m-model-4a-alternative-specific.md) · [Sigma in tree importance](../analysis/m-sigma-tree-importance.md) · [f_distance](m-f-distance.md)

</div>
