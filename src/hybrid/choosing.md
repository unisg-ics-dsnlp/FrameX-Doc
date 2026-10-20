# Choosing and Combining Patterns

Start by asking whether a hybrid is needed. A small, stable set of rules may
be sufficient by itself. A language task without a formal decision boundary
may need only a model. Combine them when you need both language handling and
an explicit proof, action policy, auditable process, exact aggregation or
testable rule changes.

The handbook reports gains and costs for particular tasks and models, not
universal break-even thresholds. Test your own baseline for accuracy, unsafe
outcomes, latency and cost.

## From a requirement to patterns

These questions are independent; several answers can apply to one system.

| Requirement | Starting patterns |
| --- | --- |
| Read facts from documents or speech | 1 Sensor, with 6 Repair |
| Turn an explicit policy text into candidate rules | 2 Author, with checks and 6 Repair |
| Ask questions in everyday language or explain a proof | 3 Translator |
| Propose external actions | 4 Proposes/Dispose, often with 5 Steer |
| Follow a multistep protocol or conversation | 5 Steer, 1 Sensor, 6 Repair, 7 Division |
| Escalate ambiguous cases | 7 Division |
| Explain an observation with candidate causes | 8 Hypothesis Generator, often with 5 Steer |
| Review a policy change beyond automated checks | 9 Critic, supplementing 2 Author |
| Supply a model with formal labels and feedback | 10 Teach |
| Remember claims across sessions and revise them | 11 Memory, composed with 1 and 5 |
| Display exact passages or values | 12 Selects/Write |
| Combine several judgments under a conservative ordering | 13 Fail-Safe Union, with 7 for unresolved cases |

## Example: a passenger-rail assistant

Studio EX06 uses a symbolic Swiss passenger-rail system as the setting for
connecting language and knowledge. A possible composition is:

1. **Translator (3)** maps a passenger's question into a candidate query.
2. A check limits its vocabulary and operations; the engine evaluates the
   admitted query against accepted timetable facts.
3. **Steer (5)** selects the next step: answer, obtain a missing constraint,
   or explain why a requested connection is unsupported.
4. **Division (7)** routes ambiguity to a person. **Repair (6)** handles
   invalid output within a fixed attempt limit.
5. **Selects/Write (12)** can assemble the final times and station names from
   exact result fields instead of asking a model to reproduce them.

If disruption information comes from text, add **Sensor (1)** with source
checks. Keep base timetable knowledge, proposed observations and accepted
updates distinguishable. An answer must retain the data revision that
supported it. See the [H2 starter project](https://github.com/unisg-ics-dsnlp/hybridai-h2-template)
for the course's application setting; its setup and data belong to that
project rather than FrameX-Core.

## Failure patterns to avoid

Section 8 of the handbook names five recurring mistakes:

| Failure pattern | What goes wrong | Concrete correction |
| --- | --- | --- |
| Silent Rule Override | Host code changes a verdict outside the proof | Record the observation and derive the correction explicitly |
| Circular Evaluation | The evaluated model or developer also supplies its own gold labels | Fix independent cases and criteria before measuring |
| Self-Judge | An answer and its assessment share the same blind spots | Use checkable external evidence and independent assessment |
| Prose Policy | Decisions exist only as instructions in a prompt | Put the decisive conditions and transitions into testable rules |
| Decorative Check | Evidence is logged but does not affect acceptance | Require the check in the rule that admits the claim or action |

## Test the boundary

Before making live calls, provide receipts for a valid answer, invalid
evidence, malformed output, failed execution, ambiguous judgment and an
exhausted repair budget. Check both the intended conclusion and the absence
of permission when evidence is insufficient.

Preserve programs, input revisions, requests, receipts and acceptance
decisions. Measure the composition against a rules-only or model-only
baseline where appropriate. Passing a symbolic test verifies behavior under
those premises; it does not establish a real-world source claim.
