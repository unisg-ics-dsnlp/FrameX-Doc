# Paths

A path is a conjunction through an intermediate object: hop from one object
to the next by sharing a variable such as `?FxValue1`. Paths express
multi-step traversals a single slot cannot.

```prolog
// From rob to john via whoever sits in between.
rob[hasParent -> ?FxValue1] AND ?FxValue1[hasBrother -> john].
```
