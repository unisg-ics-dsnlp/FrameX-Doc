# A small family knowledge graph

```framex
world open.
abraham:Man.
sarah:Woman.
isaac:Man[father -> abraham; mother -> sarah].
jacob:Man[father -> isaac; mother -> rebekah].
esau:Man[father -> isaac; mother -> rebekah].
rebekah:Woman.
?Parent[son -> ?Child] <- ?Child:Man AND (
    ?Child[father -> ?Parent] OR ?Child[mother -> ?Parent]
).
?- ?Mother:Woman AND ?Mother[son -> ?Son]
   AND ?Son[father -> abraham].
expect true: sarah[son -> isaac].
```

A frame bundles named properties of one object. Isaac's frame records two
relationships, to Abraham and Sarah. A semicolon separates properties; it
does not mean sequence or choice.

The rule reads: a parent's son is a male child whose father *or* mother is
that parent. OR is inclusive. The query joins the mother, son and father by
reusing variables. Its answer is `Mother = sarah, Son = isaac`. Binding
labels in displayed output may omit the question-mark marker used in source.

The final `expect` is an executable assertion about the answer. It is not
evidence that makes that answer true. Use `framex test` with the same
filename to check expectations explicitly; changing `expect true` to another
expected truth value should make a mismatching test fail.

## Try it

Add a second male child with the same parents. Predict how many query rows
appear and explain the shared bindings.
