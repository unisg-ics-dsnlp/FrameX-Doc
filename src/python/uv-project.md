# Add FrameX to a uv Project

This tutorial adds FrameX from its Git repository to an existing
**uv-managed Python codebase**. It follows the setup used by the
[H2 template](https://github.com/unisg-ics-dsnlp/hybridai-h2-template): uv
installs the Python package, and an installer builds the matching Rust
engine into the project's virtual environment.

The engine and client are two separate installations:

| Part | Installed by | Location |
| --- | --- | --- |
| Python package, including `Client` and tool hosts | `uv add` / `uv sync` | Project `.venv` |
| `framex` engine binary | `scripts/install-engine.sh` | `.venv/bin/framex` |

Commands below use a macOS/Linux shell. You need uv, Git, curl, a Rust
toolchain with Cargo, and a project supporting Python 3.10 or newer. No model
server or API key is needed for this tutorial.

## 1. Start in your project root

Use the directory containing your existing `pyproject.toml`. If you want to
try this in a new project first:

```bash
uv init my-framex-app --python 3.12
cd my-framex-app
```

Keep your application's existing name, dependencies and build configuration.
If its supported Python range includes versions below 3.10, update that
range to match FrameX's requirements before adding the dependency.

## 2. Add the Python package from Git

Run this in your project root:

```bash
uv add "framex @ git+https://gitlab.com/ds-unisg/framex-core@48b5f077f542e0c44a18874871b82a899161128a#subdirectory=python"
```

The commit is the public 0.4.4 revision used by these docs and the template.
`subdirectory=python` is required because the repository root is a Rust
project; the Python package lives under `python/`.

uv adds `framex` to your dependencies, records the Git source in
`pyproject.toml`, updates `uv.lock`, and installs the package into `.venv`.
The relevant configuration looks like this; merge these entries into your
existing tables rather than replacing the whole file:

```toml
[project]
requires-python = ">=3.10"
dependencies = [
    "framex",
    # Keep your other dependencies here.
]

[tool.uv.sources]
framex = { git = "https://gitlab.com/ds-unisg/framex-core", subdirectory = "python", rev = "48b5f077f542e0c44a18874871b82a899161128a" }
```

If you edit the TOML manually instead of using `uv add`, run `uv sync` to
resolve, lock and install it. For uv's dependency and source behavior, see
the [official dependency guide](https://docs.astral.sh/uv/concepts/projects/dependencies/).

## 3. Install the engine using the template's script

Reuse the H2 template's
[install-engine.sh](https://github.com/unisg-ics-dsnlp/hybridai-h2-template/blob/56b16cf1ae7f6673e8ec9322d1a79c24a14a31f3/scripts/install-engine.sh).
Save it as `scripts/install-engine.sh` in your own project. To download that
reviewed revision directly:

```bash
mkdir -p scripts
curl -fsSL \
  "https://raw.githubusercontent.com/unisg-ics-dsnlp/hybridai-h2-template/56b16cf1ae7f6673e8ec9322d1a79c24a14a31f3/scripts/install-engine.sh" \
  -o scripts/install-engine.sh
sh scripts/install-engine.sh
```

The script reads `rev` from the inline `framex` source entry shown above and
runs Cargo against that revision of `framex-core`. It installs the engine
into `.venv/bin/framex` and prints its version. This keeps the client and
engine on the same commit without a global engine installation.

Run `uv sync` first if `.venv` does not exist. The script expects the default
project-local `.venv` and the one-line source entry with a hexadecimal commit
ID; a custom environment location or differently formatted TOML needs an
adapted installer. The first build requires network access and a working
Rust toolchain.

Confirm both installations:

```bash
uv run python -c "from importlib.metadata import version; print(version('framex'))"
uv run framex --version
```

The package and binary should both report `0.4.4`. The explicit Git pin,
rather than the version number alone, records the source revision.

## 4. Ask a question from your application

Create `framex_demo.py` next to `pyproject.toml`:

```python
from framex import Client

PROGRAM = """world open.
socrates:Human.
?Person:Mortal <- ?Person:Human.
"""

with Client() as client:
    client.load(PROGRAM)
    print(client.query("?- socrates:Mortal."))
```

Run it through uv:

```bash
uv run python framex_demo.py
```

Expected output:

```text
{'status': 'true'}
```

`uv run` puts the project's `.venv/bin` on `PATH`, so `Client()` finds the
engine installed in step 3. No environment activation is needed. The
context manager starts `framex serve` and closes it after the query.

If an IDE or another process runs outside `uv run`, select the project's
Python interpreter and ensure the engine is discoverable, or pass its path
explicitly with `Client(binary="/absolute/path/to/project/.venv/bin/framex")`.
The base `Client` uses `PATH` or `binary=`, not `FRAMEX_BINARY` automatically.

## 5. Make setup repeatable for your team

Commit `pyproject.toml`, `uv.lock`, your installer and application code.
Keep `.venv/` in `.gitignore`; each machine builds its own engine.

After cloning your project, a teammate runs:

```bash
uv sync --locked
sh scripts/install-engine.sh
uv run --locked python framex_demo.py
```

`--locked` refuses an out-of-date lockfile rather than silently changing it.
See uv's [locking and syncing guide](https://docs.astral.sh/uv/concepts/projects/sync/).
Python environment synchronization does not build the engine. If `.venv`
is deleted or recreated, run the installer again after syncing.

To upgrade FrameX, change the `rev` in `[tool.uv.sources]`, run `uv sync`,
then rerun `sh scripts/install-engine.sh`. Review and commit the configuration
and lockfile changes together. Because the installer reads the pin, you do
not need to update a second revision inside the script.

## Explore the H2 example

The [H2 template](https://github.com/unisg-ics-dsnlp/hybridai-h2-template) is a
complete application of this setup:

| File | What to reuse or study |
| --- | --- |
| [pyproject.toml](https://github.com/unisg-ics-dsnlp/hybridai-h2-template/blob/56b16cf1ae7f6673e8ec9322d1a79c24a14a31f3/pyproject.toml) | Git source, package subdirectory and shared revision pin |
| [scripts/install-engine.sh](https://github.com/unisg-ics-dsnlp/hybridai-h2-template/blob/56b16cf1ae7f6673e8ec9322d1a79c24a14a31f3/scripts/install-engine.sh) | Build the engine into the uv environment |
| [src/runtime/client.py](https://github.com/unisg-ics-dsnlp/hybridai-h2-template/blob/56b16cf1ae7f6673e8ec9322d1a79c24a14a31f3/src/runtime/client.py) | Application-specific client extensions for staged bulk loading |
| [src/runtime/session.py](https://github.com/unisg-ics-dsnlp/hybridai-h2-template/blob/56b16cf1ae7f6673e8ec9322d1a79c24a14a31f3/src/runtime/session.py) | A persistent session for a larger knowledge base |

To run the template itself, clone it and perform its two setup steps:

```bash
git clone https://github.com/unisg-ics-dsnlp/hybridai-h2-template.git
cd hybridai-h2-template
uv sync
sh scripts/install-engine.sh
```

The tiny `framex_demo.py` above verifies the integration without downloading
rail data. The template's [usage guide](https://github.com/unisg-ics-dsnlp/hybridai-h2-template/blob/56b16cf1ae7f6673e8ec9322d1a79c24a14a31f3/docs/usage.md)
then explains `--init`, queries and the REPL. Its rail-specific `Session` and
client extensions belong to the application; a small integration can use
`framex.Client` directly.

## Common setup problems

| Symptom | Check |
| --- | --- |
| Git source has no Python project | Include `#subdirectory=python` in the dependency URL |
| `ModuleNotFoundError: framex` | Run `uv sync` and launch with `uv run` |
| `FileNotFoundError` for `framex` | Install the engine after syncing, then check `uv run framex --version` |
| Installer cannot find a revision | Keep the inline `[tool.uv.sources]` entry shown above, including `rev` |
| Installer cannot find Cargo | Install the Rust toolchain and make Cargo available in your shell |
| Lockfile is out of date | Run `uv sync` after an intentional dependency change and commit `uv.lock` |

Continue with [Client](./client.md) for persistent sessions or
[Tool Calling](./tool-calling.md) to connect rules to tools and models.
