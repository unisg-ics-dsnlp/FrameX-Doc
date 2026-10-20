# Foundations: Invariants and Moves

These principles summarize sections 2.2 and 2.3 of Siegfried Handschuh's
*Hybrid AI Patterns* (October 2026), also introduced in Studio EX06.
They apply to every pattern and composition in this section.

## Five invariants

| Invariant | Implementation consequence |
| --- | --- |
| Model text is data | Store proposed rules, queries and actions as candidates. Check and admit them before execution. |
| Model answers are dated observations | Retain prompt, inputs, model, timestamp and result so observations can be audited and replayed. |
| Rules decide | Encode acceptance, transitions and completion in executable rules. |
| Evidence decides acceptance | Require checkable evidence, such as a permitted property and a supporting source quote. Confidence is ordinary data. |
| Failures stay distinct | Preserve failed execution, malformed replies, unclear interpretations and logical unknowns. |

The host performs calls and measurements. It should not silently replace a
model verdict with its own domain decision before the rules see the receipt.
If a correction matters to the outcome, represent it explicitly so the proof
can show it.

## Four moves

| Move | What crosses the boundary |
| --- | --- |
| Request | A rule derives a request with the exact inputs the tool may see. |
| Receipt | The host records the outcome as facts linked to that request and its subject. |
| Accept | A rule admits a proposed claim, records a reason to refuse it, or leaves it unresolved. |
| Ask | A rule identifies a question for a person or the evidence that would settle an open goal; the answer becomes a receipt. |

A received field and an accepted domain fact are different stages. Merely
recording `quoteFound` provides no protection unless a rule requires it.
See [Grounded Extraction](../examples/grounded-extraction.md) for this boundary
in executable form.

## Distinguish the outcomes

| Situation | Representation | Meaning |
| --- | --- | --- |
| Provider or tool failure | `tool#status -> "failed"` with `error` | Execution did not produce usable output |
| Invalid response format | Generic host failure, or dialogue `formatError` and `received` fields | A reply arrived but broke the expected contract |
| Ambiguous interpretation | Judge `result("verdict") -> "unclear"` | The model could not settle the criterion |
| Logical unknown | Query status `unknown` | Current facts and completeness assumptions do not settle the goal |
| Evidence refused | An application rejection rule and its reason | A received proposal failed an acceptance condition |

These cases can call for different next steps: bounded format repair,
additional evidence, human clarification, or termination. None should be
converted into an affirmative answer merely to continue the workflow.

Stored values such as `false` or `"unknown"` remain data. See
[World Assumption](../syntax/world-assumption.md) for query truth, and
[Dialogue and Interviews](../python/dialogue.md) for a flow that stores a
judge's three-way interpretation as slot state.

## Keep authority and evidence separate

A quote existing in a document is a lexical measurement. It does not show
that the document is authoritative for that claim. A conversational source
may establish a language preference while being insufficient evidence of a
degree or qualification. Give sources explicit permissions and keep those
permissions visible in the acceptance rules.

Likewise, an old approval does not authorize a new state. Include relevant
revisions in evidence joins and request identities, as introduced in
[Lesson 15](../tutorial/lesson-15-state.md).
