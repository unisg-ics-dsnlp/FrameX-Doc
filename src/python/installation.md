# Installation and Quick Start

## Prerequisites

- FrameX-Workbench provides everything you need to get started. 

### For local use
- The `framex` binary on `$PATH` 
- Python 3.10 or newer

## Quick start

A `Client` starts the engine, accepts a program and answers queries. Used as a
context manager it shuts the engine down again when the block ends.

```python
from framex import Client

with Client() as client:
    client.load("world open.\n socrates:Human.\n ?X:Mortal <- ?X:Human.")
    result = client.query("?- socrates:Mortal.")
    print(result)  # {'status': 'true', 'bindings': []}
```

This is the [Quick Start](../quick-start.md) program driven from Python: a
world assumption, a fact, a rule, and a question.

## Locating the binary

If `framex` is not on `$PATH`, pass the path explicitly:

```python
client = Client(binary="/usr/local/bin/framex")
```
