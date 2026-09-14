# Attribute Signatures

`Class { attribute: Type }.` declares which attributes a class provides and
their value type. Every member of the class (and its subclasses) shares the
declared capability — but never another individual's values.

```prolog
// Every Person can carry a hasName string;
// every Company member the same empty shape.
Person { hasName: String }.
Company {}.
```
