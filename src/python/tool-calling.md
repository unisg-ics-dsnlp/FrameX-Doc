# Tool Calling

An `external` rule derives a request object. A Python host runs the named
tool and records a receipt. Rules read that receipt and decide what follows.
The reasoning engine itself stays offline.

| Stage | Standard model tool calling | FrameX tool calling |
| --- | --- | --- |
| Choose | The model selects a tool | Rules derive a request |
| Execute | The host runs the tool | The host runs the tool |
| Return | The result goes to the model | The result becomes a receipt |
| Continue | The model interprets the result | Rules check evidence and decide |

A model can also call read operations on the engine. That is the opposite
direction from rules requesting `_llm`; keep their callers and checks explicit.

## A complete example without a model

Save this as `tool-query.fx`:

```framex
{{#include ../examples/programs/tool-query.fx}}
```

Run it through the Python host:

```bash
python -m framex.tools tool-query.fx --receipts-out tool-query.receipts.fx
```

The host queries the current knowledge base and adds a receipt. The final
query returns `true`: the slot `answer` contains the string `"true"`.
The event's `status: "succeeded"` describes tool execution;
`result("status") -> "true"` describes the logical answer.

Recompute from the receipt without executing tools:

```bash
framex run tool-query.fx tool-query.receipts.fx
```

Running only `framex run tool-query.fx` derives the request but does not
execute it. Its `answer` question is then `unknown`.

## Request identity and receipts

The example creates `` `checkHuman(socrates)` `` with
`tool#name -> "_query"`, `tool#requested -> true`, and
`tool#arg1 -> socrates`. Rules join the receipt to its subject through the
argument link.

Each completed call has `tool#completed -> true` and a `tool#status` of
`"succeeded"` or `"failed"`. Successful scalar fields become
`result("key")`; the reserved `rows` array becomes `row(N, "key")`, starting
at 1. Failure records `error` instead of result rows. Events retain inputs,
timing and available tool evidence.

Use flat JSON. The host allows at most 64 top-level fields and 64 rows of at
most 64 fields each. Nested row values fail the call. A top-level object or
list outside `rows` is ignored and marked `tool#ignored("key") -> true`.
JSON `null` adds no fact.

Within an episode, each request identity is performed at most once. Put an
attempt number or revision in its arguments when rules permit another
attempt. A fresh invocation starts a new episode; model-answer caching is
separate. Different request names enabled together need distinct numeric
`tool#order` values; the lowest runs first. A run ends at one derived
`workflow[status -> ...]` or at quiescence when no request remains. The
generic Python host also has a technical default limit of 32 actions.

## Direct Python calls

`execute` returns `(output, evidence)`:

```python
from framex import Client
from framex.tools import execute

with Client() as client:
    client.load("world open. socrates:Human.")
    output, evidence = execute(
        "_query", {"query": "?- socrates:Human."}, client=client
    )
    print(output["status"])  # true
```

For the studio's model example, configure a running Ollama server and its
downloaded model, then call `_llm`:

```python
import os
from framex.tools import execute

os.environ["FRAMEX_MODEL_PROVIDER"] = "ollama"
os.environ["FRAMEX_MODEL"] = "gpt-oss:20b"

output, evidence = execute(
    "_llm",
    {"prompt": 'Say hello. Return JSON: {"message": "..."}.'},
    client=None,
)
print(output["message"])
print(evidence["model"])
```

This makes a live call or replays a stored answer. Direct `execute` calls do
not insert receipts or apply acceptance rules, and failures raise exceptions.
Use the episode host when rules should govern the workflow; it turns tool
exceptions into failure receipts.

## Application tools

An adapter exposes `TOOLS = {name: function}`. Each function takes request
fields and returns `(output, evidence)`. The operator registers it at startup:

```bash
python -m framex.tools application.fx --adapter application_tools.py
```

A `.fx` program can request a registered tool; it cannot load Python code.
See the [Tool Reference](./tools.md) for host-specific registrations and
[Grounded Extraction](../examples/grounded-extraction.md) for an acceptance
rule that checks receipt evidence.
