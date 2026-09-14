# Constraints

A constraint records a violation as data instead of failing silently. The
`frame::record` rule below fires whenever a person works at a company while
`hasJob` is `false`.

```prolog
// Violation recorded as an ordinary derivable fact.
frame::record[frame::tuple(violation::job_conflict, ?X) -> true] <- ?X : Person AND ?X[worksAt -> ?C] AND ?C : Company AND ?X[hasJob -> false].

expect true: frame::record[frame::tuple(violation::job_conflict, rob) -> true].
```
