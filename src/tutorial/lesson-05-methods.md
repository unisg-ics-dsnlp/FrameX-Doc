# 5. Parameterized methods are relations

```framex
world open.
birth1:Birth[father -> jacob; mother -> rachel;
             child -> joseph; order -> 11].
birth2:Birth[father -> jacob; mother -> rachel;
             child -> benjamin; order -> 12].
?Father[childWith(?Mother) -> ?Child] <-
    ?Birth:Birth[father -> ?Father; mother -> ?Mother;
                 child -> ?Child].
?- jacob[childWith(rachel) -> ?Child].
expect true: jacob[childWith(rachel) -> joseph].
```

A birth is represented as an identified object with named roles. The rule
projects these roles into a parameterized method: Jacob's child with Rachel
is Joseph or Benjamin. The query returns both children.

The parentheses belong to the method's parameters. They do not invoke Python
or execute an object method. A method result is stored or derived logical
knowledge. The same method can relate an object and argument to several
results.

Birth objects are useful when a relationship itself needs a date, order,
source or uncertainty annotation. Give each observation a stable ID. FrameX
does not create new IDs using object-generating function terms.

## Choosing a representation

Use a simple slot for a simple binary relationship. Use a method when an
argument naturally selects a relation. Use a named relationship object when
you need to attach evidence or several roles. Favor the representation
students can explain without memorizing positional arguments.

## Try it

Add a birth with a different mother. Query that method argument and predict
why the existing query is unchanged.
