# Thirteen Coupling Patterns

The catalogue in Handschuh's *Hybrid AI Patterns* groups patterns by what
crosses the model/rules boundary, who controls the process, how reasoning is
shared, and how knowledge changes over time. Numbers retain the handbook's
identities, including patterns 12 and 13 in their conceptual groups.

This is an implementation-oriented guide. The complete catalogue and its
measurements remain in the [course reading](./sources.md).

## At the boundary

| Pattern | Use it when | What the rules must decide |
| --- | --- | --- |
| **1. Model as Sensor** | Facts are expressed in documents, speech or other unstructured input | Which extracted values have sufficient evidence and may become facts |
| **2. Model as Author** | A policy text needs a proposed formalization | Whether a draft passes syntax, vocabulary and regression checks before a person adopts it |
| **3. Model as Translator** | A person asks a question or needs an explanation in ordinary language | Whether a proposed query may run and whether the answer stays tied to the symbolic result |
| **12. Model Selects, Rules Write** | Displayed passages and values must be exact | Whether selected IDs identify permitted source passages; deterministic code copies their content |

For **Sensor**, retain the source and quote and make the checks part of
acceptance. The [extraction example](../examples/grounded-extraction.md) uses
`groundIn`, `quoteFound` and `valueQuoted`. A model's confidence cannot replace
that evidence, and an exact quote still needs an appropriate interpretation.

For **Author**, use hidden cases and allowed rule heads to test a candidate
in isolation. A passing check offers a draft for adoption; it is not an
automatic policy change. The public export omits the handbook's
[`_checkCandidate` implementation](../python/tools.md#_checkcandidate-needs-additional-code).

For **Translator**, constrain the formal vocabulary and operations before
execution. Check the proposed query and ground the wording of the response
in the actual result and explanation. A plausible natural-language answer is
not evidence that the underlying query was correct.

For **Selects, Rules Write**, ask the model for IDs rather than rewritten
source text. Check them and assemble the answer from retained passages or
facts. Exact copying prevents textual drift but does not prevent selection
of an irrelevant passage.

## Control

| Pattern | Use it when | What the rules must decide |
| --- | --- | --- |
| **4. Model Proposes, Rules Dispose** | A model proposes actions with external effects | Admit, refuse or narrow the proposal based on current permissions and evidence |
| **5. Rules Steer the Model** | A protocol has explicit steps and stopping conditions | Which step is active, what context it sees, and what may happen next |
| **6. Critique and Repair** | A checkable reply fails a condition | What feedback to return, how many attempts are allowed, and when repair has stalled |
| **7. Division by Competence** | Some cases can be decided formally while others remain ambiguous | Which cases the rules settle and which require another reader or a person |
| **13. Fail-Safe Union** | Several checks assess one case and an overly permissive result is costly | Combine verdicts under an explicit order; stricter evidence can only tighten the result |

For **Proposes, Rules Dispose**, permit effects only after checking the
current state. Completion requires recorded evidence, not a model declaring
itself finished. Include action scope and revision in the decision.

For **Steer**, keep transitions and context selection in the policy. Models
can phrase a question or judge an answer without choosing the next step.
The public [dialogue driver](../python/dialogue.md) supplies this structure.

For **Repair**, return the actual failed check. Use a new attempt identity
and a fixed bound. Repeating the same unresolved failure must eventually
stop or hand over; repair must not silently rewrite a verdict in Python.

For **Division by Competence**, route on explicit result and evidence states.
A model's claim of high confidence is not an authority to bypass the rules.
An ambiguous case may need a specific missing fact rather than another
unconstrained model response.

For **Fail-Safe Union**, declare the verdict ordering, for example
`release < hold < block`, and the required sources. Define what happens when
a source fails or has not returned; missing evidence must not imply release.
Expect more false alarms as stricter sources are added.

## In the reasoning

| Pattern | Use it when | What the rules must decide |
| --- | --- | --- |
| **8. Model as Hypothesis Generator** | An observation needs candidate explanations | Which hypotheses survive explicit tests and what evidence would discriminate them |
| **9. Model as Critic of the Rules** | A rule change needs review beyond available automated checks | Which grounded remarks become findings and whether unresolved findings block approval |
| **10. Rules Teach the Model** | A model needs examples, labels or feedback from a formal domain | Labels, examples and grades derived with proofs |

For **Hypothesis Generator**, keep candidate generation distinct from
testing. No surviving candidate after a bounded search does not prove that
no explanation exists. Ask for evidence that separates remaining candidates.

For **Critic**, run deterministic checks first and give the model a fixed
change to review. A critic supplements those checks; it cannot certify that
all semantic faults have been found.

For **Teach**, keep evaluation cases independent of training examples and
feedback. A learned response does not inherit the guarantee of the engine
that supplied its label.

## Over time

| Pattern | Use it when | What the rules must decide |
| --- | --- | --- |
| **11. Rule-Governed Memory** | Conversation-derived knowledge persists and changes across sessions | Which source may establish each fact; admission, supersession, withdrawal and context selection |

Memory storage uses **Sensor**; recall uses **Steer**. Retain the utterance,
source, quote and time. Derive which statements are current and which are
selected for a request; validate cited IDs against that selection. Forgetting
a cache record alone does not withdraw an accepted claim.

Use [Choosing and Combining Patterns](./choosing.md) to compose these designs.
Every composition still needs all five [invariants](./foundations.md).
