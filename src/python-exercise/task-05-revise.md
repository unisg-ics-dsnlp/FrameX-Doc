# Task 5: Revising Safely

## Solution to Task 4

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
```

</details>

## Theory: Look Before You Retract

Removing a stated fact also removes everything derived from it. `dependents`
shows that reach before you commit to it:

```python
client.dependents("dario[hasParent -> bruno]")
```

It returns a plain list of fact strings — the facts that would lose their
support:

```text
['dario[hasGrandparent -> elena]']
```

`retract(fact=...)` then withdraws the stated fact and answers with the same
`added` / `removed` shape that `add` used. The derived facts appear in
`removed`; you withdrew one fact and the engine dropped its consequences.

`diff()` repeats the most recent change. It takes no arguments and is useful
when the call that caused the change is far from the code inspecting it.

After a retraction the question that used to answer `true` answers `unknown`,
not `false`. Withdrawing evidence removes a reason to believe something. It
does not create a reason to disbelieve it.

## Task

Take Dario's parent away and watch the consequences.

1. Print the dependents of `dario[hasParent -> bruno]` before touching it.
2. Retract the fact, and print the `removed` list from the result.
3. Print the `removed` list from `diff()` as well, and compare the two.
4. Ask `?- dario[hasGrandparent -> elena].` again and print the answer.

Predict the final status before you run it. It was `true` in Task 1.

## Optional Extra Task

`retract_source(source)` removes everything that came from one source at once,
rather than one fact at a time. `compare(facts=..., before=..., after=...)`
checks a set of facts across two revisions.

Use `dependents` on `bruno[hasParent -> elena]` instead, and predict how many
facts that retraction would remove before you try it. It sits one step higher in
the chain than the fact you just withdrew.
