---
source: report/notes/m-contributions.md
date: 25-07-2026
kind: note
comments: true
generated: 2026-10-14T14:44:07
---

# Contributions

<p class="doc-meta"><span class="chip chip-note">Note</span> <span class="chip chip-project">Master</span> <span class="chip chip-date">25-07-2026</span></p>

What is new in this thesis.

1. **A new method.** It is the first method that gives a stay a probability for three types of place (building, street, open space) instead of one fixed answer. It works for people standing still, and it learns its weights from data instead of using fixed values ([Framework overview](m-framework-overview.md), [Final model](../analysis/m-final-model.md)).
2. **New data and a new finding.** A cleaned set of 907 stays in Hiroshima with known correct answers ([Ground truth dataset](m-ground-truth-dataset.md)). And the finding that streets and open spaces score lower because of how the street map is cut into pieces, which can be fixed. The GPS data itself is not the limit ([Candidate density bias toward building](../analysis/m-candidate-density-bias.md)).

Part of [Outlook](../threads/m-outlook.md).


<div class="backlinks" markdown>

**Linked from** [Candidate density bias toward building](../analysis/m-candidate-density-bias.md) · [Outlook](../threads/m-outlook.md)

</div>
