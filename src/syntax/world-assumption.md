# World Assumption

Every complete FrameX program must explicitly declare `world open.` or
`world closed.`. There is no implicit default.

```framex
// The declaration is mandatory — silence about the world is not allowed.
world open.
```

To use it correctly, keep three things strictly apart: the **world
assumption**, a **stored Boolean value**, and the **truth value of a query**.
Confusing any two of them is the most common modeling mistake.

## Three different things

**1. The world assumption** says what silence means — how the engine treats
a statement it can neither support nor refute:

- Under `world open.`, an unsupported statement normally remains `unknown`.
  A named closure declaration can make a specific class, slot or method
  complete (for example, `closed slot reviewed.`).
- Under `world closed.`, statements that cannot be established are treated
  as `false`.

**2. A stored Boolean value is ordinary data.** Writing
`rob[hasJob -> false].` asserts that the `hasJob` property has the value
`false`, the same way `reserve[configurationRevision -> 4].` asserts a
number. It is not logical negation: it does not by itself make anything
`false` at the query level.

**3. The truth value of a query** (`true`, `false` or `unknown`) is the
engine's answer about one asked statement under the program's assumptions.
`true` means supported under the program. `false` means refuted under its
closed-scope semantics. `unknown` means the program cannot settle the
statement. `expect unknown` checks that last outcome; it does not assert a
negative fact.

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
silence means. FrameX forces you to state the choice up front.

## Open world with selective closure

Open world does not mean "anything goes". Each FrameX case additionally
declares **which inventories are complete**, and a named closure declaration
can complete one class, slot or method without closing the whole world.
Typically complete are: the component inventory, the type hierarchy,
requirement groups and their membership, action types, and the resource
inventory. A scenario therefore cannot hide another usable antenna.

Still potentially `unknown` are: capability, qualification, and inspection
evidence. That split is what makes the starting snapshot interesting — the
device list is fixed and fully known, while the condition of `reserve` is
genuinely open:

```framex
// Open world with selective closure (see the last block).
world open.

// The device inventory is contractually complete:
// these three devices are all there are.
primary : DirectAntenna.
reserve : DirectAntenna.
relay : RelayTerminal.

// Supported evidence: the query is true.
relay[health -> true].
?- relay[health -> true].

// The recorded health value is false.
// This does not itself negate health -> true.
primary[health -> false].

// No health statement about reserve exists —
// under world open. this is unknown, not false.
?- reserve[health -> true].

// Named closure: the inspected slot is declared complete,
// so a missing value here is false instead of unknown.
closed slot inspected.
primary[inspected -> true].
?- reserve[inspected -> true].
```

The last query answers `false`: with the slot closed, absence counts as
refutation — the one case where silence legitimately means `false`.

## The three answers in one file

The orientation example shows `true`, a concrete value, and `unknown` side
by side:

```framex
// Open world: unasserted observations stay unknown.
world open.

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

Two further consequences:

1. **An alias match establishes nothing.** Two objects may share a display
   name (the `cars::jaguar` / `animals::jaguar` case), and asking about one in
   place of the other answers `unknown` rather than guessing.
2. **A missing output of your implementation is a defect**, not an encoding
   of `unknown`. Distinguish "the engine answered `unknown`" from "my program
   produced no answer".

## Rule of thumb

> Silence means `unknown` under `world open.` and `false` under
> `world closed.`. A stored `false` is data, not negation. If you need a
> logical `false` under an open world, close the specific class, slot or
> method it belongs to — never rely on a stored value to do the negating.
