# Client

```python
Client(binary="framex", *, request_timeout=30)
```

A `Client` is a persistent subprocess wrapping `framex serve`. It speaks JSON
Lines over stdin and stdout, so the engine state survives across calls: what
you `load` stays loaded until you replace or retract it.

```python
from framex import Client

with Client() as client:
    client.load("world open.\n socrates:Human.\n ?X:Mortal <- ?X:Human.")
    client.add(source="plato:Human.")
    print(client.query("?- ?X:Mortal."))
```

## Methods

| Method | Description |
| --- | --- |
| `load(source)` | Load a full program (replaces current state) |
| `add(*, source)` | Incremental add of facts/rules |
| `retract(*, fact)` | Withdraw a ground fact |
| `query(query)` | F-Logic query, returns a dict with a `status` |
| `explain(fact)` | Provenance chain for a fact |
| `world(mode)` | Switch `open` / `closed` world |
| `validate()` | Run constraint checks |
| `diff()` | Most recent state change |
| `compare(*, facts, before, after)` | Compare fact sets across revisions |
| `retract_source(source)` | Remove all facts from a source |
| `dependents(fact)` | List facts that depend on this one |
| `why_not(fact)` | Explanation when a fact does not hold |
| `rdf_import(*, source, format, document)` | Import RDF data |
| `rdf_export(*, format, selection)` | Export as RDF |
| `save_replay(path)` | Write session transcript to file |

`query` returns a dictionary whose `status` is `true`, `false` or `unknown`
(see [Truth Values](../syntax/truth-values.md)), or `bindings` when the goal
contained variables. The `bindings` key is present only in that last case:

```text
{'status': 'true'}
{'status': 'bindings', 'bindings': [{'G': 'elena'}]}
```

So read `status` before reaching for `bindings`. Each binding is one match, and
its keys are the variable names without the `?` marker.

`world` switches the [World Assumption](../syntax/world-assumption.md) of the
running session, and `validate` runs the declared
[Constraints](../syntax/constraints.md).

## Exceptions

- `FrameXError` — the engine returned an error. Carries an `.error` dictionary
  with `kind` and `message`.
- `FrameXTimeout` — the request timed out and the process was killed.

```python
from framex import Client, FrameXError, FrameXTimeout

try:
    client.query("?- broken syntax")
except FrameXError as exc:
    print(exc.error["kind"], exc.error["message"])
except FrameXTimeout:
    print("engine did not answer in time")
```
