# Task 3: Growing the Knowledge Base

## Solution to Task 2

<details class="solution">
<summary>Show the full program and what it prints</summary>

```python
"""Drive a small family knowledge base from Python."""

from framex import Client

PROGRAM = """world open.

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
"""


def describe(result):
    status = result["status"]
    if status == "bindings":
        rows = result["bindings"]
        return f"{len(rows)} match(es): {rows}"
    return status


def main():
    with Client() as client:
        loaded = client.load(PROGRAM)
        print("loaded:", loaded)

        result = client.query("?- dario[hasGrandparent -> elena].")
        print("grandparent:", result)

        print("ground :", describe(client.query("?- dario[hasGrandparent -> elena].")))
        print("binding:", describe(client.query("?- dario[hasGrandparent -> ?G].")))
        print("open   :", describe(client.query("?- dario[hasParent -> anna].")))
        print("many   :", describe(client.query("?- ?X[hasSibling -> ?Y].")))


if __name__ == "__main__":
    main()
```

Running it prints:

```text
loaded: {'facts': 26}
grandparent: {'status': 'true'}
ground : true
binding: 1 match(es): [{'G': 'elena'}]
open   : unknown
many   : 2 match(es): [{'X': 'anna', 'Y': 'bruno'}, {'X': 'bruno', 'Y': 'anna'}]
```

</details>

## Theory: Adding Without Reloading

There are two ways to put knowledge into a session, and they are not the same.

`load` **replaces** the session. Everything the engine held is gone, and the
new program takes its place.

`add` **extends** it. The facts and rules you pass join what is already there:

```python
client.add(source="carla : Woman.\n")
```

Note the keyword: `add(source=...)`, not `add(...)`. The same holds for
`retract(fact=...)` later.

`add` answers with the change it caused:

```text
{'added': [...], 'removed': [...]}
```

Both lists include **derived** facts, not just the ones you wrote. Adding one
person who shares a parent makes the sibling rule fire, and the new sibling
facts appear in `added` alongside the class membership the engine inferred. The
engine recomputes consequences as soon as the knowledge changes; you never ask
it to.

## Task

Give Elena a third child.

1. Add a module-level string `NEW_FACTS` stating that `carla` is a `Woman` and
   that Carla's parent is `elena`.
2. Call `add` with it, and print the `added` and `removed` lists separately.
3. Ask who Carla's siblings are, and print the answer with `describe`.

You wrote two facts. Count how many entries come back in `added`, and work out
where each one came from.

## Optional Extra Task

Add a **rule** rather than facts, and watch a larger cascade. Give the program
an aunt rule:

```framex
?C[hasAunt -> ?A] <- ?C[hasParent -> ?P] AND ?P[hasSibling -> ?A] AND ?A : Woman.
```

Predict how many facts it derives before you run it. Remember that Carla is now
a sibling of both Anna and Bruno.
