# Hybrid AI with FrameX

FrameX gives language models and rules separate jobs. Models read ambiguous
text, phrase questions and propose candidates. Rules determine what evidence
counts, which action is allowed and when a workflow ends. The Python host
connects them through requests and receipts.

There are two kinds of logic to model:

| Layer | Questions it answers | Example |
| --- | --- | --- |
| Domain logic | What follows from the accepted facts? | Which connections satisfy the passenger's constraints? |
| Control logic | What may happen next, and with which evidence? | Is the query admissible, must a person clarify, or may an answer be shown? |

A model's proposed fact is an observation to assess. A proof shows what
follows from accepted premises; it does not verify the premises in the world.

## Read this section

- [Foundations](./foundations.md): five invariants, four moves and distinct failures.
- [Thirteen Coupling Patterns](./patterns.md): choose a named design and its acceptance boundary.
- [Choosing and Combining Patterns](./choosing.md): start from a requirement and test a composition.
- [Sources and Version Scope](./sources.md): course material and public implementation boundaries.

For implementation, start with [Tool Calling](../python/tool-calling.md),
consult the [Tool Reference](../python/tools.md), and run
[Grounded Extraction](../examples/grounded-extraction.md). The existing
[syntax tutorial](../tutorial/index.md) supplies the language prerequisites.
