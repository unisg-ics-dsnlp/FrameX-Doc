# 9. Missing evidence: open and closed worlds

```framex
world open.
p1:Paper.
p2:Paper.
p1[reviewed -> true].
?Paper:NeedsReview <-
    ?Paper:Paper AND NOT ?Paper[reviewed -> true].
?- p2:NeedsReview.
?- ?Paper:Paper AND unknown { ?Paper[reviewed -> true] }.
expect unknown: p2:NeedsReview.
```

Paper p2 has no review evidence. The first answer is unknown. The second
query returns p2 as a positively identified Paper whose review statement is
unknown. Its candidate domain is explicit; the engine is not enumerating
every imaginable object.

`NOT` does not turn unknown into true. The rule therefore does not derive
NeedsReview for p2 in this open-world program. A scope warning points out
that absence cannot be established. This is intentional evidence about the
modeling assumption, not a reason to suppress the warning.

## Three outcomes

True means supported under the program. False means refuted under its
closed-scope semantics. Unknown means the program cannot settle the
statement under its current assumptions. `expect unknown` checks that last
outcome; it does not assert a negative fact.

A stored boolean false is also distinct: a property with value false is an
ordinary assertion about that value, not automatically the negation of the
same property with value true.

See also [World Assumption](../syntax/world-assumption.md).

## Try it

Replace the world declaration with `world closed.` in a copy. Predict both
queries before running. The NeedsReview answer becomes true; the
unknown-filter query has no p2 binding.
