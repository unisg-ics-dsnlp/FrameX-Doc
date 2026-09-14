# Facts

`object[attribute -> value].` states a fact. Values can be objects, strings,
numbers, or booleans. Only direct facts are stated — everything else is
derived by rules.

```prolog
// Attribute, reference, installation, revision, and boolean facts.
rob[hasName -> "Rob"].
rob[hasParent -> henryk].
reserve[installedOn -> odyssey].
reserve[configurationRevision -> 4].
rob[hasJob -> false].
```
