# Expectations

`expect <truth>: goal.` states what the engine must derive — the machine-checked
contract of a `.fx` file, run with `framex test <file>.fx`. The worked language
file declares thirteen expectations and all of them must pass.

```prolog
// Ground facts, inheritance, derivation, and paths.
expect true: rob : Person.
expect true: rob[hasUncle -> john].
expect true: rob[hasParent -> ?FxValue1] AND ?FxValue1[hasBrother -> john].

// Same display name, distinct objects: unknown, not false.
expect unknown: cars::jaguar : animals::Animal.
```
