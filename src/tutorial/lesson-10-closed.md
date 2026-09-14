# Close only what is complete

```framex
world open.
closed slot reviewed.
p1:Paper.
p2:Paper.
p1[reviewed -> true].
?Paper:NeedsReview <-
    ?Paper:Paper AND NOT ?Paper[reviewed -> true].
?- p2:NeedsReview.
expect false: p2[reviewed -> true].
expect true: p2:NeedsReview.
expect unknown: p2:Cited.
```

The review slot is declared complete within this program's module. Missing
review evidence for p2 is now false, so the rule derives NeedsReview. Cited
remains unknown: the whole world was not closed.

Completeness is a modeling contract. A closed review slot is appropriate only
if the supplied review information is complete for the intended scope. It
does not claim that all literature everywhere has been searched.

Negation variables must be bound by positive conditions. Avoid negative
cycles: a conclusion must not depend negatively on itself. FrameX rejects
unsafe or unstratified programs rather than treating rule order as a repair.

## Universal questions via counterexamples

To express "all required items are present", identify the required items and
derive a counterexample when a required item is absent in a complete evidence
scope. Then test the counterexample projection under an explicit completeness
contract.

Do not mistake absence of a counterexample in an open source for proof of
completeness. Likewise, absence of an ancestor path does not justify "these
people are unrelated" without an adequate closed model.

## Try it

Explain why closing reviewed does not make `p2:Cited` false. Then describe a
situation where closing reviewed would be an invalid assumption.
