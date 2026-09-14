# 4. Classes and inheritance

```framex
world open.
Person { label: String }.
Man extends Person.
Researcher extends Person.
isaac:Man[label -> "Isaac"].
isaac:Researcher.
?- isaac:Person.
?- isaac:Researcher.
expect true: isaac:Person.
```

Isaac belongs to both Man and Researcher. Both classes extend Person, so
Isaac is a Person. Class membership, inheritance and property assertions are
distinct relationships.

The field declaration describes a type expectation for Person's label. It
does not invent labels for every person. Inheritance supports shared class
structure; it is not an imperative constructor or an instruction to allocate
an object.

An object can have several class memberships. Use `extends` for the
hierarchy. Do not confuse a namespace separator with a subclass declaration.

## Objects without properties

To introduce an entity, give it an appropriate class membership. Empty frames
are outside the teaching profile. Avoid adding meaningless properties merely
to force an object into existence.

## Classes as data

FrameX exposes membership and hierarchy through reserved metadata properties.
[Lesson 13](./lesson-13-meta.md) shows a membership query. This provides a
bounded form of introspection; it is not arbitrary higher-order formula
evaluation.

## Try it

Remove the direct Researcher membership. Does the Person conclusion survive?
Name the remaining reason.
