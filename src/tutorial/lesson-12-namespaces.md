# 12. Namespaces and modules are different

```framex
world open.
prefix family = "urn:family:".
prefix alias = "urn:family:".
prefix archive = "urn:archive:".
family::isaac[label -> "Isaac"].
archive::isaac[label -> "Isaac"].
?- alias::isaac[label -> "Isaac"].
expect true: family::isaac != archive::isaac.
```

The alias resolves to the same expanded identity as family, so its query is
true. The archive identity remains distinct despite having the same label.
Prefixes organize identifiers; they do not retrieve data from the Internet.

A namespace answers "which entity does this name denote?" A module answers
"in which knowledge context is this assertion evaluated?" Naming an entity
does not make its facts available in every module. Positive imports do not
import a source module's completeness assumptions.

FrameX uses prefix declarations and qualified identifiers to keep names
unambiguous. Use explicit prefixes when integrating graphs. Exact external
identifiers may be represented with backticks. Do not assume arbitrary URI
spelling differences identify the same resource.

Module-local completeness is useful for snapshots, institutions or evidence
sources. Keep the context visible in a query rather than treating namespace
qualification as a substitute for context.

## Try it

Give `archive::isaac` a different label. Why is the family query unaffected?
What would an identity-resolution decision need beyond matching labels?
