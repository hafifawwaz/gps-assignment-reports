---
source: report/notes/sigma.md
date: 19-07-2026
kind: note
comments: true
generated: 2026-10-13T16:57:34
---

# sigma

<p class="doc-meta"><span class="chip chip-note">Note</span> <span class="chip chip-date">19-07-2026</span></p>

Stay-level positional dispersion, $\sigma = \sqrt{\mathrm{var}(x) + \mathrm{var}(y)}$, standardized once by `sigma_scale` = 36.708 (99th-percentile cap 179.14 m) and reused unchanged in every model.

It enters with **one shared coefficient** and building as the reference (0 for building rows). Splitting it by type is an identification problem, not a modelling option.

Clean positive effect in every model ([Model 2: share-type and sigma](../analysis/model-2-share-type-sigma.md), [Final model](../analysis/final-model.md)), yet tree models rank it far higher than its modest coefficient suggests: [Sigma in tree importance](../analysis/sigma-tree-importance.md).

Part of [Chapter 4: Framework](../progress/ch4-framework.md).


<div class="backlinks" markdown>

**Linked from** [Chapter 4: Framework](../progress/ch4-framework.md) · [Framework overview](framework-overview.md) · [Model 2: share-type and sigma](../analysis/model-2-share-type-sigma.md) · [Model 4a: alternative-specific parameters](../analysis/model-4a-alternative-specific.md) · [Sigma in tree importance](../analysis/sigma-tree-importance.md)

</div>
