# Family Tree

This example builds a small family model step by step. Each step adds one
piece of FrameX logic: taxonomy, facts, derivation rules, property
declarations, and finally checks with `expect` and queries with `?-`.

Five people are enough to show everything: `elena` is the parent of the
siblings `anna` and `bruno`; `bruno` is the parent of `dario` and `anna` is
the parent of `felix`. That makes `dario` and `felix` cousins.

The family in one picture — solid arrows are the stated `hasParent` facts,
everything else on this page is derived from them:

```mermaid
flowchart TD
    elena["Elena"] --> anna["Anna"]
    elena --> bruno["Bruno"]
    bruno --> dario["Dario"]
    anna --> felix["Felix"]
```

## Step 1 — Declare the world and the taxonomy

Every complete program declares its [world](../syntax/world-assumption.md). Then define the classes:

```prolog
world open.

Person { hasName: String }.
Man extends Person.
Woman extends Person.
```

`Man` and `Woman` inherit from `Person`, so every `Man` or `Woman` is also a
`Person`. Membership shares the declared capability (`hasName`); it does not
share any individual's condition.

## Step 2 — Add the people

Objects use stable IDs. Display names are plain attributes and may collide;
IDs may not:

```prolog
elena : Woman.
anna : Woman.
bruno : Man.
dario : Man.
felix : Man.

elena[hasName -> "Elena"].
anna[hasName -> "Anna"].
bruno[hasName -> "Bruno"].
dario[hasName -> "Dario"].
felix[hasName -> "Felix"].
```

## Step 3 — State the parent facts

Only direct parents are stated. Everything else is derived:

- `elena` is the parent of `anna` and `bruno`
- `bruno` is the parent of `dario`
- `anna` is the parent of `felix`

```prolog
anna[hasParent -> elena].
bruno[hasParent -> elena].
dario[hasParent -> bruno].
felix[hasParent -> anna].
```

## Step 4 — Derive siblings, brothers, and sisters

A sibling shares a parent. Brothers and sisters add a class check:

```prolog
?X[hasSibling -> ?Y] <- ?X[hasParent -> ?P] AND ?Y[hasParent -> ?P].
?X[hasBrother -> ?Y] <- ?X[hasParent -> ?P] AND ?Y[hasParent -> ?P] AND ?Y : Man.
?X[hasSister -> ?Y] <- ?X[hasParent -> ?P] AND ?Y[hasParent -> ?P] AND ?Y : Woman.

declare symmetric hasSibling.
```

Note: as stated, the sibling rule also matches a person with themselves
(`anna` shares a parent with `anna`). The queries and checks below always use
distinct persons, so this does not affect any result here.

## Step 5 — Derive grandparents, uncles, and aunts

One step up through an intermediate object:

```prolog
?C[hasGrandparent -> ?G] <- ?C[hasParent -> ?P] AND ?P[hasParent -> ?G].
?C[hasUncle -> ?U] <- ?C[hasParent -> ?P] AND ?P[hasBrother -> ?U].
?C[hasAunt -> ?A] <- ?C[hasParent -> ?P] AND ?P[hasSister -> ?A].
```

This gives, for example: `dario`'s parent `bruno` has sister `anna`, so
`dario[hasAunt -> anna]`. `felix`'s parent `anna` has brother `bruno`, so
`felix[hasUncle -> bruno]`.

## Step 6 — Declare inverse and transitive relations

Children follow from parents automatically, and ancestry chains recurse:

```prolog
declare inverse hasParent hasChild.
declare transitive ancestor.

?A[ancestor -> ?D] <- ?D[hasParent -> ?A].
?A[ancestor -> ?D] <- ?D[hasParent -> ?P] AND ?A[ancestor -> ?P].
```

`declare inverse` means `bruno[hasChild -> dario]` follows from
`dario[hasParent -> bruno]` with no extra rule. The two `ancestor` rules cover
the direct case and the recursive case: `felix`'s ancestor `elena` is reached
via `anna`.

## Step 7 — Derive cousins

Cousins are the children of siblings:

```prolog
?X[hasCousin -> ?Y] <- ?X[hasParent -> ?PX] AND ?Y[hasParent -> ?PY] AND ?PX[hasSibling -> ?PY].

declare symmetric hasCousin.
```

`dario`'s parent `bruno` is the sibling of `felix`'s parent `anna`, so
`dario[hasCousin -> felix]` — and by symmetry the reverse holds too.

## Step 8 — Check expectations and ask queries

`expect` states what the engine must derive. `?-` asks an open query:

```prolog
expect true: anna : Person.
expect true: dario[hasGrandparent -> elena].
expect true: anna[hasSibling -> bruno].
expect true: felix[hasUncle -> bruno].
expect true: dario[hasAunt -> anna].
expect true: dario[hasCousin -> felix].
expect true: felix[hasCousin -> dario].
expect true: felix[ancestor -> elena].
expect true: bruno[hasChild -> dario].
expect unknown: dario[hasParent -> anna].

?- dario[hasGrandparent -> ?G].
?- felix[hasUncle -> ?U].
?- dario[hasCousin -> ?C].
```

`dario[hasParent -> anna]` is `unknown`, not `false`: the world is open and no
fact confirms or denies it. A missing statement is never treated as a negative
fact.

## Complete file

```prolog
// Step 1: world and taxonomy — every program declares its world,
// then defines the classes it reasons about.
world open.

Person { hasName: String }.
Man extends Person.
Woman extends Person.

// Step 2a: the people — stable IDs, one object per person.
elena : Woman.
anna : Woman.
bruno : Man.
dario : Man.
felix : Man.

// Step 2b: display names — plain attributes, may collide across objects.
elena[hasName -> "Elena"].
anna[hasName -> "Anna"].
bruno[hasName -> "Bruno"].
dario[hasName -> "Dario"].
felix[hasName -> "Felix"].

// Step 3: parent facts — only direct parents are stated,
// everything else is derived.
anna[hasParent -> elena].
bruno[hasParent -> elena].
dario[hasParent -> bruno].
felix[hasParent -> anna].

// Step 4: siblings — two people sharing a parent;
// brothers and sisters add a class check.
?X[hasSibling -> ?Y] <- ?X[hasParent -> ?P] AND ?Y[hasParent -> ?P].
?X[hasBrother -> ?Y] <- ?X[hasParent -> ?P] AND ?Y[hasParent -> ?P] AND ?Y : Man.
?X[hasSister -> ?Y] <- ?X[hasParent -> ?P] AND ?Y[hasParent -> ?P] AND ?Y : Woman.

// Step 5: grandparents, uncles, aunts — one step up
// through an intermediate object.
?C[hasGrandparent -> ?G] <- ?C[hasParent -> ?P] AND ?P[hasParent -> ?G].
?C[hasUncle -> ?U] <- ?C[hasParent -> ?P] AND ?P[hasBrother -> ?U].
?C[hasAunt -> ?A] <- ?C[hasParent -> ?P] AND ?P[hasSister -> ?A].

// Step 6: ancestry — direct case plus recursion through an intermediate parent.
?A[ancestor -> ?D] <- ?D[hasParent -> ?A].
?A[ancestor -> ?D] <- ?D[hasParent -> ?P] AND ?A[ancestor -> ?P].

// Step 7: cousins — children of siblings.
?X[hasCousin -> ?Y] <- ?X[hasParent -> ?PX] AND ?Y[hasParent -> ?PY] AND ?PX[hasSibling -> ?PY].

// Property declarations — symmetry, inverse, and transitivity
// the engine applies on top of the rules above.
declare symmetric hasSibling.
declare symmetric hasCousin.
declare inverse hasParent hasChild.
declare transitive ancestor.

// Step 8a: checks — what the engine must derive.
expect true: anna : Person.
expect true: dario[hasGrandparent -> elena].
expect true: anna[hasSibling -> bruno].
expect true: felix[hasUncle -> bruno].
expect true: dario[hasAunt -> anna].
expect true: dario[hasCousin -> felix].
expect true: felix[hasCousin -> dario].
expect true: felix[ancestor -> elena].
expect true: bruno[hasChild -> dario].
expect unknown: dario[hasParent -> anna].

// Step 8b: open queries — ask the engine to fill in ?G, ?U, ?C.
?- dario[hasGrandparent -> ?G].
?- felix[hasUncle -> ?U].
?- dario[hasCousin -> ?C].
```

Run it with:

```bash
framex test family-tree.fx
```

All ten expectations should pass.

## What to try next

- Remove `felix[hasParent -> anna].` and explain why `felix[hasUncle -> bruno]`
  becomes `unknown` rather than `false`.
- Add `expect true: elena[hasChild -> anna].` and explain which declaration
  makes it follow with no extra rule.
- Add a second child for `anna` and check who becomes cousins with `dario`.
