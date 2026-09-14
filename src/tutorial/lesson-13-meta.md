# 13. Inspect the object model

```framex
world open.
isaac:Person[father -> abraham; label -> "Isaac"].
?- isaac[?Property -> ?Value].
?- isaac[frame::memberOf -> ?Class].
expect true: isaac[father -> abraham].
```

The first query returns the known ordinary property/value pairs: father and
label. The second queries the reserved membership view and returns the
Person class identifier.

The ordinary slot query does not silently return every internal record.
FrameX's reserved metadata properties provide explicit access to supported
structural information. They allow useful meta-queries while retaining a
bounded language.

Do not replace the second query with a variable after the class colon. That
is not the supported class-introspection abbreviation.

Meta-queries help explain what was loaded, inspect schemas, and build
teaching tools. A variable property name makes dependency analysis less
specific, so warnings and stratification may need a more conservative
treatment than with named properties.

## Try it

Add another ordinary property and predict which query changes. Explain why
metadata and domain properties are kept distinguishable.
