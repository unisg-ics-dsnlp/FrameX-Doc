# Grounded Extraction

This example implements **Model as Sensor (1)**. A model proposes a customer
name and quote; the host measures their occurrence in the source; rules
decide whether to accept the claim. It makes the
[request, receipt and accept moves](../hybrid/foundations.md) visible.

## The program

Download [grounded-extraction.fx](./programs/grounded-extraction.fx), or copy
this complete file:

```framex
{{#include programs/grounded-extraction.fx}}
```

The `Document` class condition restricts the subject. The receipt joins back
to it through `tool#arg1`. Acceptance requires a successful completed call,
the allowed slot `customer`, and both `quoteFound` and `valueQuoted`.

This is a small lexical grounding example. It does not prove that a source
is authoritative or that a copied value is semantically the customer. A real
application needs source permissions and suitable domain checks. Model
confidence is not an acceptance condition.

## Test without a model

The following authored receipts simulate the host's output. They test rule
behavior; they do not measure a model or independently test quote matching.
Save the program and fixtures together, then run each case separately:

| Fixture | What it tests |
| --- | --- |
| [grounded-extraction.accepted.test.fx](./programs/grounded-extraction.accepted.test.fx) | Valid evidence produces the customer fact |
| [grounded-extraction.rejected.test.fx](./programs/grounded-extraction.rejected.test.fx) | A missing source quote, an unquoted value or a different slot prevents acceptance |
| [grounded-extraction.failed.test.fx](./programs/grounded-extraction.failed.test.fx) | Failure remains an error and does not establish the customer |

```bash
framex test grounded-extraction.fx grounded-extraction.accepted.test.fx
framex test grounded-extraction.fx grounded-extraction.rejected.test.fx
framex test grounded-extraction.fx grounded-extraction.failed.test.fx
```

Do not concatenate conflicting scenario receipts. Under this open-world
program, a refused customer claim stays `unknown`; refusal does not establish
the opposite claim.

## Run against a model

After [installation](../python/installation.md) and
[model configuration](../python/model-settings.md):

```bash
python -m framex.tools grounded-extraction.fx --receipts-out extraction.receipts.fx
framex run grounded-extraction.fx extraction.receipts.fx
framex explain grounded-extraction.fx extraction.receipts.fx 'doc1[customer -> "Acme AG"]'
```

The first command runs the host. The second replays receipt facts offline;
the third inspects the conclusion if the model supplied accepted evidence.
Live output depends on the model and is not guaranteed to match the authored
success case.

The host's `groundIn` checks compute the two Boolean fields; a model cannot
authorize its own claim by writing `quoteFound: true`. A success event still
does not bypass the acceptance rule. If no acceptable value is returned,
the application should derive a bounded repair or a question for a person.
