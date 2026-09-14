# Membership

`object:Class` states that an object is a member of a class. Membership is
inherited through the taxonomy: from `rob : Man` and `Man extends Person`,
`rob : Person` follows with no extra rule.

```prolog
rob : Man.
reserve:DirectAntenna.

// Follows by inheritance — no rule needed.
?- rob : Person.
?- reserve:CommunicationDevice.
```
