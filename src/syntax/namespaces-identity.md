# Namespaces and Identity

`prefix name = "iri".` binds a namespace; `name::object` addresses an object
inside it. Two objects may share a display name yet stay distinct — an alias
match never establishes which object is meant.

```prolog
prefix cars = "https://example.org/cars#".
prefix animals = "https://example.org/animals#".

cars::Car {}.
animals::Animal {}.
cars::jaguar : cars::Car.
animals::jaguar : animals::Animal.

// Same display name, distinct objects: unknown, not false.
expect unknown: cars::jaguar : animals::Animal.
```
