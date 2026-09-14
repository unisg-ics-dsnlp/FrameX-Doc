# World Assumption

Every complete FrameX program starts with a world declaration:

```prolog
// Step 1: declare the world assumption —
// open means "not stated" is unknown, not false.
world open.
```

This single line fixes how the engine treats **missing information**: as
`unknown` (open world) rather than `false` (closed world). The rest of this
page explains the two assumptions in general and what `world open.` means
concretely in FrameX.

## The general concept

The distinction comes from knowledge representation and also appears in
databases and logic programming:

- **Open-world assumption (OWA):** a statement that is not entailed by the
  knowledge base is `unknown` — it may still be true. Absence of a fact is
  not a negative fact. See the
  [Open-world assumption](https://en.wikipedia.org/wiki/Open-world_assumption)
  on Wikipedia.
- **Closed-world assumption (CWA):** a statement that is not entailed is
  taken to be `false`. What is not known to be true is assumed false — the
  classic example is a database query such as "list all flights from Zurich
  to Vienna", where missing rows mean "no such flight". See the
  [Closed-world assumption](https://en.wikipedia.org/wiki/Closed-world_assumption)
  on Wikipedia, originally formalised by
  [Raymond Reiter](https://en.wikipedia.org/wiki/Closed-world_assumption).

Neither is "correct" in the abstract — it is a modelling choice about what
silence means.

## What `world open.` means in FrameX

FrameX programs declare `world open.`, i.e. the open-world assumption holds
by default:

- A fact that is stated (or derived) is `true`.
- An explicitly refuted statement is `false` (e.g. `primary` is explicitly
  unhealthy).
- Everything else is `unknown` — for example, the health of `reserve`, about
  which no statement exists.

Consequences that follow directly:

1. **Deleting a negative fact yields `unknown`, not `true`.** Removing
   `reserve[health -> false]` does not make the reserve healthy; it makes its
   health unknown.
2. **An alias match establishes nothing.** Two objects may share a display
   name (the `cars::jaguar` / `animals::jaguar` case), and asking about one in
   place of the other answers `unknown` rather than guessing.
3. **A missing output of your implementation is a defect**, not an encoding
   of `unknown`. Distinguish "the engine answered `unknown`" from "my program
   produced no answer".

## Completeness per inventory

Open world does not mean "anything goes". Each FrameX case additionally
declares **which inventories are complete**. Typically complete are: the
component inventory, the type hierarchy, requirement groups and their
membership, action types, and the resource inventory. A scenario therefore
cannot hide another usable antenna.

Still potentially `unknown` are: capability, qualification, and inspection
evidence. That split is what makes the starting snapshot interesting — the
device list is fixed and fully known, while the condition of `reserve` is
genuinely open:

```prolog
// A complete inventory: these three devices are all there are.
primary : DirectAntenna.
reserve : DirectAntenna.
relay : RelayTerminal.

// Capability evidence: stated, hence true.
relay[health -> true].

// Inspection evidence: explicitly negative, hence false.
primary[health -> false].

// No health statement about reserve exists —
// under world open. this is unknown, not false.
?- reserve[health -> true].
```

## The three answers in one file

The orientation example shows `true`, a concrete value, and `unknown` side
by side:

```prolog
// Taxonomy and installation — stated facts.
CommunicationDevice extends Component.
DirectAntenna extends CommunicationDevice.
reserve:DirectAntenna.
odyssey:Spacecraft.
reserve[installedOn -> odyssey].
reserve[configurationRevision -> 4].

// An older inspection, kept as history (revision 3, device is at 4).
earlierInspection:Inspection.
earlierInspection[component -> reserve].
earlierInspection[configurationRevision -> 3].
earlierInspection[outcome -> "pass"].

// Inherited membership: true.
?- reserve:CommunicationDevice.
// Stated attribute: answers 4.
?- reserve[configurationRevision -> ?Revision].
// Unasserted observation: unknown under world open.
?- reserve[health -> true].
```

## Rule of thumb

> If you did not state it and cannot derive it, FrameX answers `unknown`.
> If you need `false`, state the negative fact or close the specific
> inventory it belongs to, never rely on silence!
