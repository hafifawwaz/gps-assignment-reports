---
source: report/notes/m-f-directional.md
date: 25-07-2026
kind: note
comments: true
generated: 2026-10-14T14:44:07
---

# f_directional

<p class="doc-meta"><span class="chip chip-note">Note</span> <span class="chip chip-project">Master</span> <span class="chip chip-date">25-07-2026</span></p>

Does the person's small movement during the stay follow the direction of a street? Someone standing on a street often moves along it. Someone inside a building moves in more random directions.

For a street candidate, the score is high when the movement follows that street:


$$f_\text{directional}(E_k, C_i) = \frac{1}{n-1} \sum_{j=1}^{n-1} |\cos(\theta_j - \theta_{E_k})|$$


For a building or open-space candidate, movement along a nearby street counts against it. The score is **1 minus the best match with any nearby street**, so every candidate gets a value:


$$f_\text{directional}(E_k, C_i) = 1 - \max_{s \in \text{Adjacent}(E_k)} \left\{ \frac{1}{n-1} \sum_{j=1}^{n-1} |\cos(\theta_j - \theta_s)| \right\}$$


$\theta_j$ is the direction from point $j$ to point $j+1$. It is only computed for steps longer than 0.5 m, to ignore GPS noise. $\theta_{E_k}$ is the direction of the street, taken from its shape on the map. $\text{Adjacent}(E_k)$ means the street pieces within 30 m. If no step is longer than 0.5 m, the score is a neutral 0.5.

**In the models:** finding the right form took three tests: [Directional scope ablation (3a vs 3b)](../analysis/m-directional-scope-ablation.md), its overlap with the ASC terms in [Model 5: alternative-specific constants (rejected)](../analysis/m-model-5-asc-rejected.md), and finally [f_directional: shared vs split](../analysis/m-f-directional-shared-vs-split.md). The final answer is one weight shared by all three place types.

Part of [Framework overview](m-framework-overview.md).


<div class="backlinks" markdown>

**Linked from** [Assignment framework](../threads/m-assignment-framework.md) · [Directional scope ablation (3a vs 3b)](../analysis/m-directional-scope-ablation.md) · [Framework overview](m-framework-overview.md) · [Model 2: share-type and sigma](../analysis/m-model-2-share-type-sigma.md) · [Model 5: alternative-specific constants (rejected)](../analysis/m-model-5-asc-rejected.md) · [f_directional: shared vs split](../analysis/m-f-directional-shared-vs-split.md)

</div>
