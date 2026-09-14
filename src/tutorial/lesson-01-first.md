# Your first object, rule and question

```framex
world open.
socrates:Human.
?Person:Mortal <- ?Person:Human.
?- socrates:Mortal.
```

Read the three meaningful statements aloud: Socrates is a human. A person is
mortal if that person is human. Is Socrates mortal?

`socrates` is an object identifier. `Human` and `Mortal` are class names.
`?Person` is a variable; its question-mark marker makes the distinction
visible. A class name after a colon is literal, even though it starts with a
capital letter.

The answer is `true`. The rule does not say that every mortal is human. An
implication is directional. Nor does asking the question add a fact.

## Run it

With FrameX on your path, from the repository root:

```bash
framex run examples/flogic-tutorial/01-first.fx
```

In Studio, open the file and choose *Run program*. The query is inside the
file. The result contains the logical answer; execution status is a separate
success/failure indicator.

The CLI may also report fact and rule counts. These describe the evaluated
representation, including derived facts and internal rules for object
semantics. They are not a count of the sentences you typed. This example has
one authored implication. A successful process exit alone does not mean every
possible query is true.

Every statement ends with a period. Newlines do not end statements.
`world open.` makes incomplete knowledge explicit; its consequences return in
[Lesson 9](./lesson-09-open.md).

## Try it

Remove the human fact, retaining the rule and question. Predict the answer
under an open world. Then restore the fact.
