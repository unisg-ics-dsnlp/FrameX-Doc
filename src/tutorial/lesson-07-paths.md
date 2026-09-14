# Navigate with visible joins

```framex
world open.
jacob[father -> isaac].
isaac[father -> abraham].
?Child[grandfather -> ?Grandfather] <-
    ?Child[father -> ?Father]
    AND ?Father[father -> ?Grandfather].
?- jacob[grandfather -> ?Grandfather].
expect true: jacob[grandfather -> abraham].
```

The intermediate variable makes the path explicit: start at a child, follow
father, then follow father again. The answer is `Grandfather = abraham`.

Bracket joins make each relationship along a path visible. The intermediate
object can be named, queried and inspected. This is especially useful when
more than one value is present or evidence is incomplete.

A join is equality of the reused binding, not a textual similarity match. If
the first fact pointed to another identifier with label "Isaac", the second
fact would not join solely because of that label.

## Check each edge

When a path query is unexpectedly empty, query each edge individually. Check
identifiers, property names and module context before changing the rule.
Under an open world, a missing edge is not evidence that the real-world
relationship does not exist.

## Try it

Add a second father edge in a copy and inspect the new grandfather results.
Then discuss whether a functional constraint should flag that input.
