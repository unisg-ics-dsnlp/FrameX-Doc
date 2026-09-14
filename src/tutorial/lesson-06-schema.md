# 6. Schemas and consistency checks

```framex
world open.
Person { label: String, father: Person }.
declare required Person label.
declare functional father.
abraham:Person[label -> "Abraham"].
isaac:Person[label -> "Isaac"; father -> abraham].
?- isaac[father -> abraham].
expect true: abraham:Person.
```

The schema describes value types. The required declaration demands a label
for Person objects. The functional declaration limits distinct values for
the father slot. These are three different checks.

Run `framex validate` with this filename. This example has no reported
schema violations. Under the open world, the functional constraint can still
be unresolved; no reported violation is not a global consistency
certificate. For an experiment, work on a copy: remove Isaac's label, use a
string as his father, or add a second father value. Validate after each
change.

Validation reports problems; it does not repair the data, choose a preferred
father, or turn a missing label into a value. A functional declaration
applies to the named property in its module, not merely to the class whose
declaration happens to be nearby.

Typing is also distinct from inference declarations. A range rule can derive
a class membership; a schema type constraint checks one. Neither one
verifies a real-world claim.

A trustworthy knowledge base may preserve conflicting reports as separate
evidence objects before deciding which assertions to accept. Do not silently
overwrite disagreement to make validation pass.

## Try it

Explain the difference between an absent value, a wrong type, two distinct
values and an explicitly closed property. Which declaration addresses each?
