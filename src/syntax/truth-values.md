# Truth Values

Every statement evaluates to `true`, `false`, or `unknown` (see
[World Assumption](./world-assumption.md)). How conditions combine:

| Combination | True | False | Unknown |
| --- | --- | --- | --- |
| Required conditions with AND | Every condition is true | At least one condition is false | No false condition, at least one unknown |
| Alternatives with OR | At least one alternative is true | Every alternative is false in a complete candidate set | No true alternative, at least one unknown |

Two consequences: `unknown` evidence is preserved unless a `false` condition
already decides the result, and deleting a negative fact produces `unknown`,
never `true`.
