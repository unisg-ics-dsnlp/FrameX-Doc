# FrameX-Doc

FrameX is an offline, domain-neutral frame-logic engine with a Python host
for tools and language models, developed by the Chair of Data Science and
Natural Language Processing at the University of St. Gallen. It derives
conclusions from facts and rules, answers queries and explains its reasoning.

In a hybrid system, models read, phrase and propose; rules decide which
evidence counts and what may happen next. This documentation covers the
public [FrameX-Core](https://gitlab.com/ds-unisg/framex-core) **0.4.4** export
and the coupling patterns introduced in Hybrid AI Studio EX06.

> [!TIP]
> Start with [Quick Start](./quick-start.md), then the
> [language tutorial](./tutorial/index.md). For language-model integration,
> read [Hybrid AI with FrameX](./hybrid/index.md) and
> [Tool Calling](./python/tool-calling.md).

![HSG NLP Logo](./images/HSG_NLP_Logo%20Classic.png)

---

## FrameX Syntax

- [World Assumption](./syntax/world-assumption.md)
- [Variables](./syntax/variables.md)
- [Comments](./syntax/comments.md)
- [Classes and Subclasses](./syntax/classes-subclasses.md)
- [Membership](./syntax/membership.md)
- [Attribute Signatures](./syntax/attribute-signatures.md)
- [Facts](./syntax/facts.md)
- [Rules](./syntax/rules.md)
- [External Requests](./syntax/external-requests.md)
- [Property Declarations](./syntax/property-declarations.md)
- [Namespaces and Identity](./syntax/namespaces-identity.md)
- [Paths](./syntax/paths.md)
- [Constraints](./syntax/constraints.md)
- [Queries](./syntax/queries.md)
- [Expectations](./syntax/expectations.md)
- [Truth Values](./syntax/truth-values.md)

## Python API

- [Python API overview](./python/index.md)
- [Installation and Quick Start](./python/installation.md)
- [Add FrameX to a uv Project](./python/uv-project.md)
- [Client](./python/client.md)
- [Tool Calling](./python/tool-calling.md)
- [Tool Reference](./python/tools.md)
- [Model Settings and Replay](./python/model-settings.md)
- [Dialogue and Interviews](./python/dialogue.md)

## Hybrid AI with FrameX

- [Overview](./hybrid/index.md)
- [Foundations: Invariants and Moves](./hybrid/foundations.md)
- [Thirteen Coupling Patterns](./hybrid/patterns.md)
- [Choosing and Combining Patterns](./hybrid/choosing.md)
- [Sources and Version Scope](./hybrid/sources.md)

## Examples

- [Family Tree](./examples/family-tree.md)
- [Grounded Extraction](./examples/grounded-extraction.md)

## Tutorial

- [Tutorial overview](./tutorial/index.md)
- [1. Your first object, rule and question](./tutorial/lesson-01-first.md)
- [2. A small family knowledge graph](./tutorial/lesson-02-family.md)
- [3. Properties, identity and multiple values](./tutorial/lesson-03-values.md)
- [4. Classes and inheritance](./tutorial/lesson-04-inheritance.md)
- [5. Parameterized methods are relations](./tutorial/lesson-05-methods.md)
- [6. Schemas and consistency checks](./tutorial/lesson-06-schema.md)
- [7. Navigate with visible joins](./tutorial/lesson-07-paths.md)
- [8. Recursion and the fixed point](./tutorial/lesson-08-recursion.md)
- [9. Missing evidence: open and closed worlds](./tutorial/lesson-09-open.md)
- [10. Close only what is complete](./tutorial/lesson-10-closed.md)
- [11. Ordered data and numeric conditions](./tutorial/lesson-11-sequence.md)
- [12. Namespaces and modules are different](./tutorial/lesson-12-namespaces.md)
- [13. Inspect the object model](./tutorial/lesson-13-meta.md)
- [14. Provenance: a reason is not a probability](./tutorial/lesson-14-evidence.md)
- [15. From knowledge to controlled agents](./tutorial/lesson-15-state.md)
- [Quick reference](./tutorial/reference.md)
- [Practice and verification](./tutorial/practice.md)

## Python API Exercise

- [Exercise overview](./python-exercise/index.md)
- [Task 1: Connect and Ask](./python-exercise/task-01-connect.md)
- [Task 2: Reading the Answer](./python-exercise/task-02-answers.md)
- [Task 3: Growing the Knowledge Base](./python-exercise/task-03-grow.md)
- [Task 4: Making the Engine Explain Itself](./python-exercise/task-04-explain.md)
- [Task 5: Revising Safely](./python-exercise/task-05-revise.md)
- [Task 6: Worlds and Validation](./python-exercise/task-06-worlds.md)
- [Task 7: When Things Go Wrong](./python-exercise/task-07-failure.md)
- [Task 8: Solution and What Comes Next](./python-exercise/task-08-wrap-up.md)

---
