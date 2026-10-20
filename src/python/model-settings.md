# Model Settings and Replay

The engine needs no model server. A host needs these settings only for live
calls such as `_llm` and dialogue wording and judging. Set them in the
environment of the Python process.

## Local model

With Ollama installed and running:

```bash
ollama pull gpt-oss:20b
export FRAMEX_MODEL_PROVIDER=ollama
export FRAMEX_MODEL=gpt-oss:20b
export FRAMEX_MODEL_ENDPOINT=http://127.0.0.1:11434
python -m framex.tools extraction.fx --receipts-out extraction.receipts.fx
```

Use the [grounded extraction program](../examples/grounded-extraction.md) as
`extraction.fx`. Model choice and memory determine whether a local run is
practical. The example's deterministic tests need no model.

## Hosted or compatible server

Use the model ID and full chat-completions URL supplied by your provider:

```bash
export FRAMEX_MODEL_PROVIDER=openai
export FRAMEX_MODEL=your-model-id
export FRAMEX_MODEL_ENDPOINT=https://your-provider.example/v1/chat/completions
export FRAMEX_MODEL_KEY_ENV=OPENAI_API_KEY
```

Set `OPENAI_API_KEY` using your own secret configuration. The host reads it
from the variable named by `FRAMEX_MODEL_KEY_ENV`; keys do not enter receipts.
Keep them out of `.fx` programs, prompts and source control. If your project
uses `.env`, load it into the process environment yourself; FrameX does not
automatically load `.env` files.

## Settings reference

| Variable | Meaning |
| --- | --- |
| `FRAMEX_MODEL_PROVIDER` | `ollama` (default) or `openai` |
| `FRAMEX_MODEL` | Model identifier; defaults to `local` for Ollama or `gpt-5-mini` for the compatible provider |
| `FRAMEX_MODEL_ENDPOINT` | Ollama base URL or full compatible chat-completions URL |
| `FRAMEX_MODEL_KEY_ENV` | Key variable name, default `OPENAI_API_KEY` |
| `FRAMEX_MODEL_CACHE` | Answer store, default `~/.cache/framex/model` |
| `FRAMEX_MODEL_REFRESH` | `1` asks again instead of replaying |
| `FRAMEX_MODEL_TIMEOUT` | Model-call timeout in seconds, from 1 to 600 |
| `FRAMEX_MODEL_SCHEMA` | `0` disables provider JSON-schema constraints |
| `FRAMEX_MODEL_JSON_EXTRACT` | `1` opts into extracting JSON from surrounding text; evidence marks `json_extracted` |
| `FRAMEX_MODEL_RESPONSE_FORMAT` | `json_object` (default) or `none` |
| `FRAMEX_MODEL_THINK` | `true` or `false` for Ollama and supported local compatible servers |
| `FRAMEX_MODEL_MAX_TOKENS` | Positive output-token limit for the compatible provider |
| `FRAMEX_MODEL_HTTP_HOST` | Permits plain HTTP to one named model host, in addition to loopback |

Keep provider-specific overrides unset unless your endpoint supports them.
Response-format settings do not replace acceptance rules.

## Three different records

| Record | Contents | Use |
| --- | --- | --- |
| Model-answer cache | Provider, model, messages, timestamp, output and provider evidence | Replay an identical request without a live call |
| Episode receipts | Tool-result facts linked to request identities | Recompute conclusions offline with the original program |
| `Client.transcript` | Attempted engine protocol requests, including rejected ones | Export with `save_replay` |

Cache identity includes provider, model and messages; an explicit `THINK`
setting also affects it. A different prompt or model can cause a live call.
Events mark evidence as `mode: "live"` or `"replay"`. Retain source programs
and receipts alongside the cache to reproduce a decision.

Test failure paths with authored receipts. Provider failure, malformed JSON,
an `unclear` judgment and a logical `unknown` must keep distinct meanings;
see [Foundations](../hybrid/foundations.md).
