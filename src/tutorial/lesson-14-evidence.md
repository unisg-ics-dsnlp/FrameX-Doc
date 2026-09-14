# Provenance: a reason is not a probability

```framex
world open.
report7:Report[text -> "The antenna passed inspection."].
antenna[healthy -> true].
annotate antenna[healthy -> true] source "inspection-7"
    time "2026-09-14" weight 0.9.
antenna:Ready <- antenna[healthy -> true].
?- antenna:Ready.
expect true: antenna:Ready.
```

The annotation attaches a source name, timestamp and weight to an assertion.
The readiness rule derives a conclusion from the health fact. Ask
`framex explain` about `'antenna:Ready'` to inspect its support.

The source name is an identifier, not a verification service. It should
connect to a retained report or observation in the surrounding application.
The explicit report object carries source text; an application should keep
that text and its assertion records aligned.

A weight of 0.9 does not change logical true into "ninety percent true".
Raw model confidence, provenance algebra values and calibrated probabilities
are different concepts. A proof records how supplied premises support a
conclusion. It does not validate the observation itself.

For language-model extraction, retain the source, relevant quote, proposed
interpretation, model and request identity, acceptance decision and resulting
fact. Validate the returned structure and apply explicit acceptance rules
before relying on a proposed fact.

## Try it

Describe what must be checked before accepting an LLM's claim that an
antenna is healthy. Which checks are structural, which are logical, and
which require evidence beyond the model?
