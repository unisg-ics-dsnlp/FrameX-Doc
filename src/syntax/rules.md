# Rules

`head <- body.` derives new knowledge: whenever the body holds, the head
holds. Body conditions are joined with `AND`; `OR` alternatives must be
explicitly grouped. Rules are written recursively rather than as listed
closures.

```prolog
// From a taxonomy fact to a derived membership.
?X:Mortal <- ?X:Human.

// A derivation over two references.
?X[hasUncle -> ?U] <- ?X[hasParent -> ?P] AND ?P[hasBrother -> ?U].

// Recursive closure: one step plus the transitive step.
?D[requires -> ?R] <- ?D[needs -> ?M] AND ?M[requires -> ?R].
```
