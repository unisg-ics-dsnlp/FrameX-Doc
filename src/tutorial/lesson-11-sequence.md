# Ordered data and numeric conditions

```framex
world open.
step1:Step[position -> 1; next -> step2].
step2:Step[position -> 2; next -> step3].
step3:Step[position -> 3].
?Step:EarlyStep <- ?Step:Step[position -> ?Position]
                  AND ?Position < 3.
?- ?Step:EarlyStep.
?- step1[next -> ?Next].
expect true: step2:EarlyStep.
```

The first query returns step1 and step2; the second returns step2. The
numeric variable is bound by a frame before it is compared.

A sequence can be modeled with named nodes, position values and next edges.
This finite graph is inspectable and can carry provenance. It does not
implement Prolog list terms, head/tail unification or arbitrary term
construction.

The next edge describes an order. Merely asserting it does not execute a
step, consume a token or prevent two steps from running. An external
executor must respect the permissions and transitions derived by the rules.

Use rules to compare values that are already available. Put parsing, numeric
computation and external access into explicit external adapters with
recorded inputs and outputs. Aggregates are outside this core teaching
profile.

## Try it

Add a fourth step. Which facts describe ordering, and which rule classifies
early steps? Does either perform an action?
