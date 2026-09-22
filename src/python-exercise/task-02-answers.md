# Task 2: Reading the Answer

## Solution to Task 1

<details class="solution">
<summary>Show the full program and what it prints</summary>

```python
"""Drive a small family knowledge base from Python."""

from framex import Client

PROGRAM = """world open.

Person { hasName: String }.
Man extends Person.
Woman extends Person.

elena : Woman.
anna : Woman.
bruno : Man.
dario : Man.
felix : Man.

anna[hasParent -> elena].
bruno[hasParent -> elena].
dario[hasParent -> bruno].
felix[hasParent -> anna].

?X[hasSibling -> ?Y] <- ?X[hasParent -> ?P] AND ?Y[hasParent -> ?P] AND ?X != ?Y.
?C[hasGrandparent -> ?G] <- ?C[hasParent -> ?P] AND ?P[hasParent -> ?G].
"""


def main():
    with Client() as client:
        loaded = client.load(PROGRAM)
        print("loaded:", loaded)

        result = client.query("?- dario[hasGrandparent -> elena].")
        print("grandparent:", result)


if __name__ == "__main__":
    main()
```

Running it prints:

```text
loaded: {'facts': 26}
grandparent: {'status': 'true'}
```

</details>

## Theory: Four Shapes of Answer

Every `query` returns a dictionary with a `status`. There are four values:

| `status` | Meaning |
| --- | --- |
| `true` | The engine derived the fact |
| `false` | The engine refuted it |
| `unknown` | The engine can neither support nor refute it |
| `bindings` | The question had variables; the matches are in `bindings` |

The `bindings` key is present **only** when `status` is `bindings`:

```text
{'status': 'true'}
{'status': 'bindings', 'bindings': [{'G': 'elena'}]}
```

So `result["bindings"]` raises `KeyError` on a question without variables. Read
`status` first, then reach for `bindings`.

`bindings` is a list of dictionaries, one per match. The keys are the variable
names without the `?` marker: `?G` in the query comes back as `G`. An empty
list means the question had variables but nothing matched.

`unknown` is not `false`. Under `world open.` a question the program can
neither support nor refute stays open, and the engine says so rather than
guessing. See [World Assumption](../syntax/world-assumption.md).

## Task

Add a function `describe(result)` above `main` that turns a result dictionary
into a short readable string:

- when `status` is `bindings`, report how many matches there were and show them
- otherwise, report the status itself

Then use it to ask four questions and print each answer:

1. `?- dario[hasGrandparent -> elena].` — a fact the rules derive
2. `?- dario[hasGrandparent -> ?G].` — the same question with a variable
3. `?- dario[hasParent -> anna].` — something the program never states
4. `?- ?X[hasSibling -> ?Y].` — two variables at once

Before running, predict which of the four comes back `unknown`, and how many
matches the last one finds.

## Optional Extra Task

The sibling question returns Anna and Bruno twice, once in each direction.
Print the matches as one line each instead of one long list, and explain in a
comment why both directions appear.
