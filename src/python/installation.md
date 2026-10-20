# Installation and Quick Start

FrameX-Core is public at [GitLab](https://gitlab.com/ds-unisg/framex-core).
It contains the Rust engine and Python client and tool hosts. These pages
target **0.4.4**; see the [source notes](../hybrid/sources.md) for the tested
public revision and the scope of the export.

## In FrameX-Workbench

The course Workbench provides the engine and Python package. Create
`main.py` and use `from framex import Client`. For local use, install both
parts below.

## Build the engine locally

You need Git, a Rust toolchain with Cargo, Python 3.10 or newer, and uv.
From a directory where you keep projects:

```bash
git clone https://gitlab.com/ds-unisg/framex-core.git
cd framex-core
git checkout 48b5f077f542e0c44a18874871b82a899161128a
cargo build --release --offline
export PATH="$PWD/target/release:$PATH"
framex --version
```

The engine has no Rust dependencies. Once the toolchain is installed,
`--offline` builds without fetching crates. The binary is
`target/release/framex`; add that directory to `PATH` in each new shell or
configure your shell to retain it. The checkout pins the tested revision.

## Install the Python package

Still inside the checkout:

```bash
uv venv
source .venv/bin/activate
uv pip install ./python
```

For an existing uv project, follow
[Add FrameX to a uv Project](./uv-project.md) for the complete workflow,
including the H2 template's installer that builds the engine into `.venv`.
The Python dependency command is:

```bash
uv add "framex @ git+https://gitlab.com/ds-unisg/framex-core@48b5f077f542e0c44a18874871b82a899161128a#subdirectory=python"
```

Installing the Python package does **not** install the Rust binary. The
package has no runtime dependencies; packaging tools may still be downloaded
during installation.

## Quick start

Save the following as `main.py` and run `python main.py` in the activated
environment. A `Client` starts the engine and closes it when the context ends.

```python
from framex import Client

with Client() as client:
    client.load("world open.\n socrates:Human.\n ?X:Mortal <- ?X:Human.")
    result = client.query("?- socrates:Mortal.")
    print(result)  # {'status': 'true'}
```

This is the [Quick Start](../quick-start.md) program driven from Python: a
world assumption, a fact, a rule, and a question.

## Locating the binary

If `framex` is not on `$PATH`, pass the path explicitly:

```python
client = Client(binary="/absolute/path/to/framex-core/target/release/framex")
```

`Client` uses `PATH` or its `binary` argument. The tool-host commands also
accept `--binary` and read `FRAMEX_BINARY`. Continue with
[Tool Calling](./tool-calling.md) to run an external-tool episode and
[Model Settings](./model-settings.md) to connect a language model.
