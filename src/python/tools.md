# Tool Reference

These contracts describe the public **FrameX-Core 0.4.4** export. The
handbook includes additional development components; appearing in a pattern
does not mean a tool is registered in every host.

## Generic host: `framex.tools`

Run programs with `python -m framex.tools program.fx`. Direct Python calls
use `execute(name, parameters, client, adapters=None)`.

| Tool | Request fields | Successful output |
| --- | --- | --- |
| `_llm` | `prompt` and input fields; optional host fields below | Model scalars as `result("key")`; `rows` as `row(N, "key")` |
| `_query` | `query` | `result("status")`: `true`, `false`, `unknown` or `bindings`; `result("text")`: the full answer as JSON text |
| `_evidence_needs` | `goal`; optional `max_states`, `max_assumptions` | Bounded evidence-question report; preserve its search limits and completeness information |
| `_forgetAnswers` | `text` | `result("removed")`: number of stored model-answer records deleted |
| `_fixture` | `response`: a JSON object encoded as a string | Authored output, with evidence that no model was called |
| `_emit` | `message` | `result("delivered") -> true`; the message in event evidence |

Direct `_query` calls need a `Client`; `framex agent` handles native tools
inside the engine. `_emit` records delivery in this host; it is not a general
messaging-service adapter.

`_forgetAnswers` removes matching model-answer cache records. It does not
retract accepted facts or erase receipts and transcripts. Model withdrawal
separately and revise the session when evidence is removed.

## Fields read by the model host

| Field | Behavior |
| --- | --- |
| `prompt` | Instruction; other named input fields form one JSON message |
| `input` | Explicit user-message text; takes precedence over collecting other named fields |
| `schema` | JSON schema in direct Python calls; constrains provider formatting where supported |
| `groundIn` | Source text; adds `quoteFound` and `valueQuoted` to each returned row |
| `mustSay` | Text for a lexical check; adds `saysDecision` based on the reply's `text` |
| `contextKey` | Step whose `selectedFor` statements rules selected as context |
| `tool#maxContext` | Context bound, default 32 statements; excess fails the call |

The host strips `tool#...` fields and consumes grounding/context controls
before calling the model. A prompt may also be a named object:
`external read(?D) using _llm with readPrompt[document -> ?T] <- ...`,
where `readPrompt:Prompt[text -> "..."]` supplies the instruction.

`quoteFound` checks that a nonempty quote occurs verbatim in `groundIn`.
`valueQuoted` checks that a nonempty value occurs in the quote. These lexical
measurements do not establish that a quote supports the property or that
the source is authoritative. Acceptance rules must read the checks and
restrict which claims a source may establish.

With `contextKey`, the host sends selected statements in identifier order
and records IDs as `tool#sent("id")`. Rules can check that citations refer
to statements sent for that request and still current.

## Dialogue host: `framex.dialogue`

These tools are registered by the dialogue driver. They are not automatically
available in `framex.tools`. See [Dialogue and Interviews](./dialogue.md).

| Tool | Request fields | Successful output |
| --- | --- | --- |
| `_turn` | `question`, `attempt` | `answer`, spoken `utterance`, canonical `question` |
| `_judge` | `criterion`, `question`, `answer` | `verdict`: `yes`, `no` or `unclear`; `reason`; `label` where returned |
| `_ask` | `question` | `question`, `answer`; no model used |
| `_say` | `text` | Displays the text and records delivery |
| `_repairTurn`, `_repairJudge` | Original fields and repair information | Another attempt when the flow policy requests it |

`unclear` is a judge's interpretation, stored as data; engine `unknown` is
a logical answer. Dialogue format problems may return `formatError` and
`received` for rules to inspect. Execution failure remains a failed call.
A successful call alone is not acceptance.

## `_checkCandidate` needs additional code

The handbook's adapter checks candidate rules against a fixed vocabulary,
allowed heads and regression cases. Results include `status`, `feedback`,
`regressions` and `failedAfter`. Checking does not adopt a proposal.

It is **not shipped as a tool in the public 0.4.4 export**. The export also
omits `framex.candidates`, which the handbook's adapter imports. Copying that
adapter alone will fail. Use separately supplied course/development code or
implement and register a checker. Keep generated rules as candidate text
until checks and an explicit adoption decision permit a change.
