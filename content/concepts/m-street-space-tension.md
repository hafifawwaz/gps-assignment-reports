---
source: report/concepts/m-street-space-tension.md
date: 23-07-2026
kind: concept
comments: true
generated: 2026-10-26T20:41:14
---

# Tension with the street-space argument

<p class="doc-meta"><span class="chip chip-concept">Concept</span> <span class="chip chip-project">Master</span> <span class="chip chip-date">23-07-2026</span></p>

The method treats streets and open spaces as places just as important as buildings, because Jacobs, Gehl and Whyte describe them as real sites of daily life. The results of research question 2 make this harder. The model finds 90.0% of building stays, but only 48.6% of street stays and 44.0% of open-space stays, and it mistakes both mostly for buildings ([Confusion matrix](../analysis/m-confusion-matrix.md)).

For streets, the cause lies in how the model was fitted, not in weak GPS data. The `share_type` term gives a lower value to a candidate with many neighbours of the same type. Street stays have about 1.9 times as many same-type candidates as building stays (13.13 against 7.00 on average), because the map stores streets as many short pieces ([Candidate density bias toward building](../analysis/m-candidate-density-bias.md)). For open space this explanation does not work: open-space stays have the fewest same-type candidates, and the cause of their errors is still open.

For streets, two explanations are still possible:

- The problem belongs to this street map. A map with fewer, longer street pieces would make the gap smaller.
- Long, repeated place types like streets are at a disadvantage in any method that counts nearby candidates.

None of the papers checked can decide between the two. Testing other ways of cutting the street map could ([Future work](m-future-work.md)).

A subsection of the Discussion in the thesis. Part of [Error analysis](../threads/m-error-analysis.md).


<div class="backlinks" markdown>

**Linked from** [Candidate density bias toward building](../analysis/m-candidate-density-bias.md) · [Error analysis](../threads/m-error-analysis.md) · [Future work](m-future-work.md) · [Motivation](m-motivation.md) · [Thesis summary](../threads/m-thesis-summary.md)

</div>
