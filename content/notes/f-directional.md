---
source: report/notes/f-directional.md
date: 25-07-2026
kind: note
comments: true
generated: 2026-10-13T20:41:00
---

# f_directional

<p class="doc-meta"><span class="chip chip-note">Note</span> <span class="chip chip-date">25-07-2026</span></p>

Bearing alignment of the stay's micro-movement with the street's orientation. For a street candidate:


$$f_\text{directional}(E_k, C_i) = \frac{1}{n-1} \sum_{j=1}^{n-1} |\cos(\theta_j - \theta_{E_k})|$$


For buildings and open spaces it is computed as **1 − max alignment with any adjacent street**, so it carries a value for every candidate:


$$f_\text{directional}(E_k, C_i) = 1 - \max_{s \in \text{Adjacent}(E_k)} \left\{ \frac{1}{n-1} \sum_{j=1}^{n-1} |\cos(\theta_j - \theta_s)| \right\}$$


$\theta_j$ is the bearing from point $j$ to $j+1$, computed only for displacements over 0.5 m; $\theta_{E_k}$ is the street's orientation from its polygon; $\text{Adjacent}(E_k)$ is the set of street segments within 30 m. With no displacement over 0.5 m the score is a neutral 0.5.

How to specify it took three tests: [Directional scope ablation (3a vs 3b)](../analysis/directional-scope-ablation.md), its collinearity with an ASC in [Model 5: alternative-specific constants (rejected)](../analysis/model-5-asc-rejected.md), and finally [f_directional: shared vs split](../analysis/f-directional-shared-vs-split.md), which settled on one coefficient shared across types.

Part of [Framework overview](framework-overview.md).


<div class="backlinks" markdown>

**Linked from** [Assignment framework](../threads/assignment-framework.md) · [Directional scope ablation (3a vs 3b)](../analysis/directional-scope-ablation.md) · [Framework overview](framework-overview.md) · [Model 2: share-type and sigma](../analysis/model-2-share-type-sigma.md) · [Model 5: alternative-specific constants (rejected)](../analysis/model-5-asc-rejected.md) · [f_directional: shared vs split](../analysis/f-directional-shared-vs-split.md)

</div>
