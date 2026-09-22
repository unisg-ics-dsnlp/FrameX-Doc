# Python API

The FrameX Python Framework is a pure Python client for the FrameX reasoning
engine, with zero third-party dependencies.

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
- [Client](./client.md)
