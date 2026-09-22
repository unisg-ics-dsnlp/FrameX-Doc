# Task 6: Worlds and Validation

## Solution to Task 5

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

        print()
        print(client.explain("dario[hasGrandparent -> elena]"))

        blocked = client.why_not("dario[hasParent -> anna]")
        print("why_not status:", blocked["nodes"][0]["status"])
        print("why_not scope :", blocked["scope"])

        print()
        print("dependents:", client.dependents("dario[hasParent -> bruno]"))

        removal = client.retract(fact="dario[hasParent -> bruno]")
        print("retracted :", removal["removed"])
        print("diff      :", client.diff()["removed"])
        print("after     :", describe(client.query("?- dario[hasGrandparent -> elena].")))


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

World assumption: open
dario[hasGrandparent -> elena]
  Derived by rule #1: ?C[hasGrandparent -> ?G] <- ?C[hasParent -> ?P] AND ?P[hasParent -> ?G].
  Bindings: C = dario, G = elena, P = bruno
  Because:
    dario[hasParent -> bruno]
      Asserted fact
        Source: <json-source> | time: unspecified | weight: None | <json-source>:15:1
    bruno[hasParent -> elena]
      Asserted fact
        Source: <json-source> | time: unspecified | weight: None | <json-source>:14:1

why_not status: unknown
why_not scope : bounded first-blocker inspection; not exhaustive minimal repairs

dependents: ['dario[hasGrandparent -> elena]']
retracted : ['dario[hasGrandparent -> elena]']
diff      : ['dario[hasGrandparent -> elena]']
after     : unknown
```

</details>

## Theory: Closing the World

`world(mode)` switches the session's assumption between `"open"` and
`"closed"`, and answers with the same `added` / `removed` diff as any other
change.

The switch changes what missing evidence means. Under `world open.` a fact the
program cannot support is `unknown`. Under `world closed.` the program is taken
to be complete, so the same fact is `false`:

```text
open   : unknown
closed : false
```

Close a world only when the data really is complete. Closing an incomplete
program turns every gap in it into a confident `false`.

`validate()` runs the declared checks and returns four keys:

```text
{'violations': [...], 'schema_checks': [...], 'constraint_checks': [...], 'coverage': '...'}
```

An empty `violations` list means nothing the engine checked was violated. Read
`coverage` before concluding more than that — it states what validation did and
did not cover, and it is explicit that there is no global consistency or
completeness claim.

## Task

Your program currently ends with a question that answers `unknown`. Close the
world under it.

1. Call `world("closed")` and print the `removed` list it returns.
2. Ask `?- dario[hasGrandparent -> elena].` again and print the answer.
3. Call `validate()` and print the `violations` list.

The same question has now given three different answers across the exercise:
`true` in Task 1, `unknown` in Task 5, `false` here. Be able to say why each
one changed.

## Optional Extra Task

Print the `coverage` string in full and read it. Then give the program
something to find: state a fact that conflicts with the `hasName: String`
signature on `Person`, re-run `validate()`, and see whether it appears in
`violations` or in `schema_checks`.
