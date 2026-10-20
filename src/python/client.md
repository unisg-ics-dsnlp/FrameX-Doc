# Client

```python
Client(binary="framex", *, request_timeout=30,
       max_response_bytes=8 * 1024 * 1024,
       max_transcript_bytes=16 * 1024 * 1024)
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
| `explain_graph(fact, max_nodes=2000)` | Structured explanation graph |
| `world(mode)` | Switch `open` / `closed` world |
| `validate()` | Run constraint checks |
| `diff()` | Most recent state change |
| `compare(*, facts, before, after)` | Compare fact sets across revisions |
| `retract_source(source)` | Remove all facts from a source |
| `dependents(fact)` | List facts that depend on this one |
| `why_not(fact)` | Explanation when a fact does not hold |
| `rdf_import(*, source, format, document, module=None)` | Import RDF data |
| `rdf_export(*, format, selection, module=None, predicate="rdf_quad")` | Export as RDF |
| `request(command, **fields)` | Access an engine protocol command without a convenience wrapper |
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

`explain` returns a formatted string; `explain_graph` returns structured data.
`transcript` is a property containing attempted requests, including rejected
ones. `save_replay` refuses to overwrite an existing file. These records are
separate from the [model-answer cache and episode receipts](./model-settings.md#three-different-records).

For a model-facing read interface, the public package provides
`call_tool(client, name, arguments)`. Its allowlist contains `query`,
`explain`, `why_not`, `evidence_needs`, `schema`, `modules` and `validate`.
It does not expose loading, mutation or world switching. A generated query
still needs the application's admission checks; this helper is a dispatch
allowlist rather than a query-policy checker. The broader interface described
in the handbook is not entirely included in the public export.

## Exceptions

- `FrameXError` — the engine returned an error. Carries an `.error` dictionary
  with `kind` and `message`.
- `FrameXTimeout` — the request timed out and the process was killed.

A timed-out sent mutation has an uncertain outcome. Start a fresh session;
do not retry that mutation blindly. Invalid response shape or size also
breaks the client session. Each request is limited to 1 MiB; response and
transcript bounds are configurable in the constructor.

```python
from framex import Client, FrameXError, FrameXTimeout

try:
    client.query("?- broken syntax")
except FrameXError as exc:
    print(exc.error["kind"], exc.error["message"])
except FrameXTimeout:
    print("engine did not answer in time")
```
