# External Requests

`external name(arguments) using tool[fields] <- body.` derives a request
whose fields are known from the body. It does not execute the tool inside
the engine.

```framex
world open.
socrates:Human.

external checkHuman(?Person) using _query[query -> "?- socrates:Human."]
    <- ?Person:Human.

?- `checkHuman(socrates)`[tool#requested -> true].
```

The query is `true`: the request exists. The tool has not yet run.
Its object also has `tool#name -> "_query"` and `tool#arg1 -> socrates`.
The `#` is a namespace separator, and backticks identify the request object.

Run a host to perform the request and write a receipt. Rules can then read
`tool#completed`, `tool#status`, `result("key")` and `row(N, "key")`.
An external operation is performed at most once per request identity within
an episode; unlike an ordinary derived conclusion, its occurrence cannot be
undone by withdrawing a premise. New attempts need new identities.

Give rule subjects class conditions so they do not accidentally match the
request objects that also carry input slots. Keep input field names distinct
from derived receipt fields to avoid conflicting request values. See
[Tool Calling](../python/tool-calling.md) for the complete request/receipt
loop, and the [Tool Reference](../python/tools.md) for available hosts.
