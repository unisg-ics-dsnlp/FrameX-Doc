# Task 7: When Things Go Wrong

## Solution to Task 6

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

        print()
        switch = client.world("closed")
        print("closing removed:", switch["removed"])
        print("closed         :", describe(client.query("?- dario[hasGrandparent -> elena].")))

        report = client.validate()
        print("violations     :", report["violations"])


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
```

</details>

## Theory: Failures and the Record

Two exceptions come out of the client, and they mean different things.

`FrameXError` is the engine rejecting a request. The session is fine and you
can keep using it. The detail is on `.error`:

```python
except FrameXError as error:
    print(error.error["kind"], error.error["message"])
```

`FrameXTimeout` is different. The request passed `request_timeout` seconds
(30 by default), so the client **killed the process**. If the timed-out request
was a mutation, its outcome is unknown: it may have been applied. Do not retry
it — start a new session.

```python
client = Client(request_timeout=60)
```

Every attempted request is recorded, failures included. `transcript` is a
property, not a method, and gives back a list of dictionaries:

```python
[entry["command"] for entry in client.transcript]
```

`save_replay(path)` writes that record to a file. It opens the file in mode
`"x"`, so it **refuses to overwrite** — a second run raises `FileExistsError`.
In the Workbench, where you press *Run program* repeatedly, catch it.

## Task

Make the program survive a bad request and then record what it did.

1. Import `FrameXError` alongside `Client`.
2. Add a helper `ask(client, query)` that runs a query through `describe` and,
   on `FrameXError`, returns the error's `kind` and `message` instead of
   raising.
3. Send something that is not valid FrameX and print what comes back.
4. Print the list of commands in the transcript.
5. Call `save_replay("session.jsonl")`, catching `FileExistsError` and printing
   a clear message instead.

Run the program twice. The second run should report that the replay file
already exists, and should not crash.

## Optional Extra Task

Find the rejected query in the transcript. The engine refused it, yet it is
still recorded — the transcript holds what was *attempted*, not what succeeded.
Print the last entry in full and confirm it is the broken query.

Then raise the failure deliberately: build a `Client(request_timeout=...)` with
a very small timeout and see what a `FrameXTimeout` does to the session.
