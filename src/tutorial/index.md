# Tutorial

This tutorial introduces FrameX from the beginning. You will model objects
and their relationships, write rules, ask questions and explain the results.
A small family knowledge graph provides the first examples; later lessons
introduce incomplete evidence and controlled agents. No prior knowledge of a
logic programming system is required.

FrameX is an object-oriented rule engine for hybrid and neurosymbolic AI
teaching. Its offline core derives consequences from supplied knowledge. An
external host connects it to language models and tools. Neither a model
answer nor a logical proof establishes that an input claim is true in the
real world.

FrameX uses one property arrow, explicit variable markers and explicit world
assumptions. Learn these through the examples before turning to the
[quick reference](./reference.md). Each new concept builds on the preceding
lessons.

## How to study

Read a program, predict its answer, run it, and change one fact. Explain why
the answer changed. The early examples deliberately ask questions before
introducing expectations. Later examples add executable checks. Every printed
program is a complete file; do not concatenate files that declare different
worlds.

## Relationship to the handbooks

The family and small paper examples here are public worked exercises, not
solutions to assessed tasks.

## Lessons

- [1. Your first object, rule and question](./lesson-01-first.md)
- [2. A small family knowledge graph](./lesson-02-family.md)
- [3. Properties, identity and multiple values](./lesson-03-values.md)
- [4. Classes and inheritance](./lesson-04-inheritance.md)
- [5. Parameterized methods are relations](./lesson-05-methods.md)
- [6. Schemas and consistency checks](./lesson-06-schema.md)
- [7. Navigate with visible joins](./lesson-07-paths.md)
- [8. Recursion and the fixed point](./lesson-08-recursion.md)
- [9. Missing evidence: open and closed worlds](./lesson-09-open.md)
- [10. Close only what is complete](./lesson-10-closed.md)
- [11. Ordered data and numeric conditions](./lesson-11-sequence.md)
- [12. Namespaces and modules are different](./lesson-12-namespaces.md)
- [13. Inspect the object model](./lesson-13-meta.md)
- [14. Provenance: a reason is not a probability](./lesson-14-evidence.md)
- [15. From knowledge to controlled agents](./lesson-15-state.md)
- [Quick reference: choosing the right construct](./reference.md)
- [Practice and verification](./practice.md)

> Source: *FrameX: A Practical F-Logic Tutorial* (September 2026,
> FrameX 0.4.2). Listings are complete standalone programs from
> `examples/flogic-tutorial/`; run them with `framex run <file>.fx`.
