# 3. Properties, identity and multiple values

```framex
world open.
jacob:Person[child -> {joseph, benjamin}; label -> "Jacob"].
?- jacob[child -> ?Child].
?- jacob[child -> {joseph, benjamin}].
expect unknown: jacob[child -> anotherChild].
```

The variable query returns Benjamin and Joseph as separate bindings. The
ground question about both values returns true. Neither question claims that
no other child exists.

`->` means that a property has a value. It does not promise a single value
and it is not assignment. Adding another child preserves earlier children.
Repeating the same fact does not create another logical copy.

The braces abbreviate multiple facts; they do not store a list or a
set-valued object. They carry no ordering information. Bundles in conditions
require all their members. Express alternatives with explicitly grouped OR.

The identifier `jacob` is different from the label string `"Jacob"`. Labels
are human-facing data. Two objects with the same label do not automatically
become the same object. Stable identity matters when merging sources and
knowledge graphs.

## Naming convention

Use descriptive lower-camel-case object and property names, capitalized class
names, quoted strings, and `?Name` variables. Do not rely on capitalization
alone to mark a variable. For an uppercase entity in a value position, use a
backtick-delimited identifier. Integers, finite decimal numbers, booleans and
strings remain different kinds of values; avoid assuming text-to-number
conversion.

## Try it

Add another child and rerun the ground question. Why does the answer remain
true? What extra assumption would you need to claim the list was complete?
