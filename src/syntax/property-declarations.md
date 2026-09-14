# Property Declarations

`declare` states how a property behaves, so the engine derives consequences
with no extra rules: hierarchy (`subproperty`), reversal (`inverse`), chaining
(`transitive`), and mirroring (`symmetric`).

```prolog
// A son is a child.
declare subproperty hasSon hasChild.

// bob[hasParent -> rob] follows from rob[hasSon -> bob].
declare inverse hasChild hasParent.

// Chains collapse and mirror automatically.
declare transitive relatedTo.
declare symmetric relatedTo.
```
