# Paths

A path is a conjunction through an intermediate object: hop from one object
to the next by sharing a variable such as `?FxValue1`. Paths express
multi-step traversals a single slot cannot. A bare conjunction is not a
standalone program — it belongs inside a query or a rule body.

```framex
world open.
rob[hasParent -> henryk].
henryk[hasBrother -> john].

// As a query: who sits between rob and john?
?- rob[hasParent -> ?FxValue1] AND ?FxValue1[hasBrother -> john].

// As a rule: name the two-step traversal.
?X[hasUncle -> ?U] <- ?X[hasParent -> ?FxValue1] AND ?FxValue1[hasBrother -> ?U].
```
