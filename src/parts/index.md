# Parts of FrameX

FrameX separates an offline reasoning engine, hosts that perform external
operations, and interfaces for people. The public
[FrameX-Core repository](https://gitlab.com/ds-unisg/framex-core) contains
the engine and the Python components described below.

## FrameX-Workbench

The course [FrameX-Workbench](https://framex.nlp-lab.ai/) provides a browser
workspace for `.fx` and Python programs. It is the quickest route for course
participants who do not want a local installation. Follow [Quick Start](../quick-start.md).

## FrameX-CLI

The `framex` binary supports file-based execution, queries, validation,
expectation tests, explanations and an interactive `framex repl`. Use
`framex --help` for the command list. It also provides `framex serve` for
the Python client and `framex agent` for external-tool episodes.

Build it from the public source using the
[installation instructions](../python/installation.md). Ordinary reasoning,
validation and receipt replay need no network or language model.

## FrameX-Engine

The Rust engine evaluates facts and rules, manages explicit world and closure
assumptions, answers queries and retains provenance. It has no Rust
dependencies. An `external` declaration produces a request; the engine does
not itself make a model API call.

## Python package and hosts

| Component | Responsibility |
| --- | --- |
| `framex.Client` | Persistent JSON Lines session with `framex serve` |
| `framex.tools` | Perform registered tool requests and record receipts |
| `framex.provider` | Model-provider transport |
| `framex.dialogue` and `flow_notation` | Rule-controlled dialogue and compact `.flow` notation |
| `framex.interview` and `guide_notation` | Coverage-controlled interviews and `.guide` notation |

Rules govern both **domain logic** (what follows from accepted facts) and
**control logic** (which call, question or transition is eligible). The host
performs the requested operation and returns its outcome as data. See
[Hybrid AI with FrameX](../hybrid/index.md).

The public export is smaller than the development framework. Consult
[Sources and Version Scope](../hybrid/sources.md) before using components
from the pattern handbook.

## FrameX-Doc

This site is built with [mdBook](https://github.com/rust-lang/mdBook).
Its source is maintained separately in
[FrameX-Doc](https://github.com/unisg-ics-dsnlp/FrameX-Doc). Engine and host
source belong to FrameX-Core; documentation changes belong to FrameX-Doc.
