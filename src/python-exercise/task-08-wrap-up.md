# Task 8: Solution and What Comes Next

## Solution to Task 7

<details class="solution" open>
<summary>Show the full program and what it prints</summary>

```python
"""Drive a small family knowledge base from Python."""

from framex import Client, FrameXError

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


def ask(client, query):
    try:
        return describe(client.query(query))
    except FrameXError as error:
        return f"rejected ({error.error['kind']}): {error.error['message']}"


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

        print()
        switch = client.world("closed")
        print("closing removed:", switch["removed"])
        print("closed         :", describe(client.query("?- dario[hasGrandparent -> elena].")))

        report = client.validate()
        print("violations     :", report["violations"])

        print()
        print("bad query:", ask(client, "?- this is not FrameX"))

        print("commands :", [entry["command"] for entry in client.transcript])
        try:
            client.save_replay("session.jsonl")
            print("replay   : written to session.jsonl")
        except FileExistsError:
            print("replay   : session.jsonl already exists; delete it first")


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

closing removed: []
closed         : false
violations     : []

bad query: rejected (SyntaxError): expected comparison operator
commands : ['load', 'query', 'query', 'query', 'query', 'query', 'add', 'query', 'explain', 'why_not', 'dependents', 'retract', 'diff', 'query', 'world', 'query', 'validate', 'query']
replay   : written to session.jsonl
```

</details>

## More to Come

That is the core of the Python API: start a session, load a program, ask
questions, grow and revise what the engine knows, make it explain itself,
switch the world assumption, and keep a record of everything you sent. The
[Client](../python/client.md) page lists the methods in one table, including
the ones this exercise did not use — `compare`, `retract_source`, `rdf_import`
and `rdf_export`.

Beyond the core client the framework goes further: an external-tool host where
FrameX rules decide what to fetch or call and Python executes it, helpers that
turn a natural-language question into a query, and a coding harness for
automated code modification under a policy the engine enforces.

Those are not documented here yet. More tasks will follow.
