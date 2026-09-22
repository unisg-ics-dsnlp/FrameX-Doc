# Task 1: Connect and Ask

## Theory: The Client

`Client` starts the `framex` engine as a separate process and talks to it over
its standard input and output. One `Client` is one session. What you load stays
loaded until you replace it, so the calls you make build on each other.

Use it as a context manager. The `with` block shuts the engine down when it
ends, including when your program raises:

```python
from framex import Client

with Client() as client:
    ...
```

`load` sends a complete program and replaces whatever the session held before.
It answers with the number of facts the engine now holds, counting the facts it
derived for itself:

```text
{'facts': 26}
```

`query` sends one question and returns a dictionary. A question about a fact
with no variables answers `{'status': 'true'}`.

## Task

Create `main.py` in your Workbench workspace and press *Run program*.

1. Import `Client` from `framex`.
2. Put the family program below in a module-level string called `PROGRAM`. It is
   the model from [Family Tree](../examples/family-tree.md), cut down to two
   rules.
3. Open a `Client` in a `with` block and `load` the program. Print what `load`
   returned.
4. Ask whether Elena is Dario's grandparent, and print the answer.

```framex
world open.

Person { hasName: String }.
Man extends Person.
Woman extends Person.

elena : Woman.
anna : Woman.
bruno : Man.
dario : Man.
felix : Man.

anna[hasParent -> elena].
bruno[hasParent -> elena].
dario[hasParent -> bruno].
felix[hasParent -> anna].

?X[hasSibling -> ?Y] <- ?X[hasParent -> ?P] AND ?Y[hasParent -> ?P] AND ?X != ?Y.
?C[hasGrandparent -> ?G] <- ?C[hasParent -> ?P] AND ?P[hasParent -> ?G].
```

Only the four `hasParent` facts are stated. Every sibling and grandparent
answer in this exercise is derived from them.

Keep this file. Every later task grows it.

## Optional Extra Task

Ask a second question, this time one the program cannot support: whether Felix
is Dario's grandparent. Predict the answer before you run it.

If the engine is not on your `PATH`, `Client()` cannot start it. Point at it
explicitly instead, as [Installation and Quick Start](../python/installation.md)
shows:

```python
client = Client(binary="/usr/local/bin/framex")
```
