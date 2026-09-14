# Queries

`?- goal.` asks the engine a question. It can check a ground statement
(`true` / `false` / `unknown`) or fill in variables. The orientation example
shows all three answer shapes in one file.

```prolog
// Inherited membership: true.
?- reserve:CommunicationDevice.

// Stated attribute: answers 4.
?- reserve[configurationRevision -> ?Revision].

// Unasserted observation under world open: unknown.
?- reserve[health -> true].
```
