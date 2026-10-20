# Sources and Version Scope

These pages combine the public implementation with the October 2026 course
materials. Where a handbook example needs components outside the public
export, the implementation pages state that explicitly.

## Public implementation

[FrameX-Core](https://gitlab.com/ds-unisg/framex-core), version **0.4.4**, is
the source for the installation, client and tool contracts. Examples were
checked against public commit
[`48b5f077f542e0c44a18874871b82a899161128a`](https://gitlab.com/ds-unisg/framex-core/-/tree/48b5f077f542e0c44a18874871b82a899161128a).
Its `EXPORTED_FROM` file identifies the originating development revision.

| Included in the public export | Additional development/course components |
| --- | --- |
| Rust engine; Python `Client`, `tools`, `provider`, `dialogue`, `flow_notation`, `interview`, `guide_notation`; flow and coverage policies; an interview example | `framex.candidates` and its candidate-checking adapter, broader rule-learning and casework components, other notations, MCP integration |

Namespace qualification in this version uses `#`, for example
`family#isaac` and `tool#status`. `::` is a subclass relation. The
documentation uses `extends` for subclass declarations and `#` for namespaces.

## Course materials

**Hybrid AI Studio, EX06**, 20 October 2026, Prof. Dr. Siegfried Handschuh,
Götz-Henrik Wiegand and Lorena Raichle. The supplied 30-page deck introduces
control and domain logic, tool calling, invariants, the four moves and the
H2 language/knowledge integration exercise. The tool list explicitly notes
that `_checkCandidate` is unavailable in 0.4.4.

**Siegfried Handschuh, Hybrid AI Patterns: Thirteen Ways to Couple Language
Models with Rules, and How to Choose Among Them**, October 2026. The supplied
85-page reading is the source for the pattern names and conceptual guidance:

| Reading section | Documentation |
| --- | --- |
| 2.1, pp. 3–5: requests, receipts and hosts | [Tool Calling](../python/tool-calling.md), [Tool Reference](../python/tools.md) |
| 2.2–2.3, pp. 5–6: invariants and moves | [Foundations](./foundations.md) |
| 3–6, pp. 7–59: thirteen patterns | [Pattern guide](./patterns.md) |
| 7–8, pp. 60–61: compositions and failure patterns | [Choosing patterns](./choosing.md) |
| 10, pp. 65–68: decision guide and measurements | [Choosing patterns](./choosing.md) |
| Appendix A, pp. 69–73: installation, replay and debugging | [Installation](../python/installation.md), [Model Settings](../python/model-settings.md) |

Use the copies supplied with Studio EX06 or on the course learning platform.
The handbook's companion scripts and recordings are separate course
materials, not files in this documentation repository or the slim public
core export. Its development-repository install instructions do not imply
that all those components ship in `framex-core`.

The documentation's executable examples are deliberately small teaching
examples. They do not reproduce assessed-task solutions or claim the
handbook's measurements as guarantees for other applications.
