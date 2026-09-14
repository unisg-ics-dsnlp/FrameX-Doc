# Variables

Variables always start with `?`: `?Device`, `?X`, `?Revision`. Without the
prefix, a name is a class (after `:`) or an object (`reserve`). Quantification
is implicit — there are no explicit `for all` / `exists` keywords.

```prolog
// ?X is a variable; Mortal and Human are classes.
?X:Mortal <- ?X:Human.

// ?Revision is a variable the query fills in.
?- reserve[configurationRevision -> ?Revision].
```
