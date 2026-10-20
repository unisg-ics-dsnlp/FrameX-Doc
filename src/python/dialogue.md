# Dialogue and Interviews

`framex.dialogue` loads the bundled `policies/flow.fx`. Rules decide which
step is active, whether to ask again, which branch to take and when to stop.
Models phrase questions and interpret answers. The [tool reference](./tools.md)
distinguishes these dialogue tools from the generic host.

## A scripted flow without a model

Save this as `certificate.flow`:

```text
world open.
flow certificate starts collect.
ask collect "Which English certificate do you have?"
    answered "Does the answer name an English certificate?"
    attempts 2 then done.
say done "Thank you. The answer has been recorded." then end.
```

The compact `.flow` notation translates into ordinary F-Logic. To inspect
that translation:

```bash
python -m framex.flow_notation certificate.flow
```

Save the following as `certificate-answers.json`:

```json
{"answers": ["I have a C1 English certificate."], "verdicts": ["yes"]}
```

Run from a shell with the installed Python package and `framex` on `PATH`:

```bash
python -m framex.dialogue certificate.flow \
  --script certificate-answers.json --output certificate-run
```

`--script` supplies both answers and judgments, so this is a test of control
flow rather than a model evaluation. Choose a new output directory for each
run. The driver saves the transcript, receipts and outcome information.

For a live dialogue, configure [model settings](./model-settings.md) and
omit `--script`. `--answers` supplies scripted human answers while the models
remain live. The flow decides what follows from each receipt.

## A verdict is not an admission decision

A Collect step checks whether an answer has been supplied. A substantive
eligibility decision needs a separate criterion and rules. Merely naming
an English certificate does not establish a C1 qualification.

The policy represents judge verdicts as slot states `"true"`, `"false"` or
`"unknown"`. These are stored strings describing an interpretation; they
are distinct from the engine's logical answer about whether a fact holds.
Failed calls and invalid formats follow separate policy paths. See
[Foundations](../hybrid/foundations.md).

## Coverage interviewer

The public core also ships `framex.interview`, `policies/coverage.fx`, and
the compact `.guide` notation. A guide declares blocks, objectives and
budgets. An Observer assesses objective coverage, while a Speaker phrases
the question chosen by rules. Full coverage needs a quote from the
participant's answer.

From the public `framex-core` checkout, after installation:

```bash
python -m framex.interview examples/interview/keynote.guide \
  --script examples/interview/terse.json --output keynote-run
python -m framex.interview export keynote-run --output keynote-bundle
```

The scripted mode needs no model. `--stdin` reads participant answers from
the terminal; `--live` enables the Observer and Speaker model calls. The
interviewer defaults its binary to `target/release/framex` relative to the
working directory; use `--binary` or `FRAMEX_BINARY` when running elsewhere.
