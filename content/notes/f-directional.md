---
source: report/notes/f-directional.md
date: 25-07-2026
kind: note
comments: true
generated: 2026-10-13T16:57:34
---

# f_directional

<p class="doc-meta"><span class="chip chip-note">Note</span> <span class="chip chip-date">25-07-2026</span></p>

Bearing alignment with the street's orientation. For buildings and open spaces it is computed as **1 − max alignment with any adjacent street**, so it carries a value for every candidate.

How to specify it took three tests: [Directional scope ablation (3a vs 3b)](../analysis/directional-scope-ablation.md), its collinearity with an ASC in [Model 5: alternative-specific constants (rejected)](../analysis/model-5-asc-rejected.md), and finally [f_directional: shared vs split](../analysis/f-directional-shared-vs-split.md), which settled on one coefficient shared across types.

Part of [Framework overview](framework-overview.md).


<div class="backlinks" markdown>

**Linked from** [Chapter 4: Framework](../progress/ch4-framework.md) · [Directional scope ablation (3a vs 3b)](../analysis/directional-scope-ablation.md) · [Framework overview](framework-overview.md) · [Model 2: share-type and sigma](../analysis/model-2-share-type-sigma.md) · [Model 5: alternative-specific constants (rejected)](../analysis/model-5-asc-rejected.md) · [f_directional: shared vs split](../analysis/f-directional-shared-vs-split.md)

</div>
