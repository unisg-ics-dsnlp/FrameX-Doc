# Python API

The public FrameX-Core Python package contains the client for the reasoning
engine, an external-tool host, model-provider integration, dialogue flows
and a coverage interviewer. It requires Python 3.10 or newer and has no
third-party runtime dependencies. The Rust engine is installed separately.

Where the [FrameX Syntax](../syntax/index.md) describes *what* you write, the
Python API describes *how* a program drives the engine: loading programs,
asking queries and revising state.

```python
from framex import Client

with Client() as client:
    client.load("world open.\n socrates:Human.\n ?X:Mortal <- ?X:Human.")
    result = client.query("?- socrates:Mortal.")
    print(result)  # {'status': 'true'}
```

In the following chapters, the Python API will be explained:

- [Installation and Quick Start](./installation.md)
- [Add FrameX to a uv Project](./uv-project.md)
- [Client](./client.md)
- [Tool Calling](./tool-calling.md)
- [Tool Reference](./tools.md)
- [Model Settings and Replay](./model-settings.md)
- [Dialogue and Interviews](./dialogue.md)

The [Python API Exercise](../python-exercise/index.md) teaches the persistent
client. The [hybrid section](../hybrid/index.md) explains how to choose a
coupling and keep acceptance decisions in rules.
