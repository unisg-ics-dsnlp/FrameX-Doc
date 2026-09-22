# Task 4: Making the Engine Explain Itself

## Solution to Task 3

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


NEW_FACTS = """carla : Woman.
carla[hasParent -> elena].
"""


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

        change = client.add(source=NEW_FACTS)
        print("added  :", change["added"])
        print("removed:", change["removed"])
        print("carla  :", describe(client.query("?- carla[hasSibling -> ?Y].")))


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
added  : ['carla:Person', 'anna[hasSibling -> carla]', 'bruno[hasSibling -> carla]', 'carla[hasSibling -> anna]', 'carla[hasSibling -> bruno]']
removed: []
carla  : 2 match(es): [{'Y': 'anna'}, {'Y': 'bruno'}]
```

</details>

## Theory: Asking Why

Two calls ask the engine about its own reasoning.

`explain(fact)` returns a **string**, not a dictionary. It is a ready-formatted
proof tree, so print it directly:

```python
print(client.explain("dario[hasGrandparent -> elena]"))
```

It names the rule that fired, the bindings it used, and the asserted facts
underneath, down to the source line each came from. Note the argument: a bare
fact, with no `?-` and no trailing period.

`why_not(fact)` handles the opposite case and returns a dictionary:

```text
{'fact': ..., 'nodes': [...], 'complete': True, 'scope': '...'}
```

Each entry in `nodes` carries a `goal` and its `status`. The `scope` field is a
disclaimer the engine states about its own answer:

```text
bounded first-blocker inspection; not exhaustive minimal repairs
```

It reports the first thing that blocked the derivation. It does not enumerate
every possible repair, and a returned explanation is not evidence that a claim
holds in the real world.

## Task

Make the program account for two of its earlier answers.

1. Print the explanation for `dario[hasGrandparent -> elena]`.
2. Call `why_not` for `dario[hasParent -> anna]` — the question that came back
   `unknown` in Task 2.
3. From the result, print the status of the first entry in `nodes`, and print
   the `scope` field.

Read the proof tree against the program. The rule it names should be the
grandparent rule, and the two facts underneath should be the two `hasParent`
facts that chain through Bruno.

## Optional Extra Task

Combine a query with an explanation. Ask `?- ?X[hasSibling -> carla].`, then
loop over the bindings and print an explanation for each match. Build each fact
string from the binding you got back.
