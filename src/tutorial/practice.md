# Practice and verification

## A five-step reading exercise

1. Identify every object, class, property and variable in the family example.
2. Predict a new child binding before running the modified file.
3. Explain Sarah's ancestor relationship through the two supporting edges.
4. Contrast p2's review status in the open and selectively closed examples.
5. Explain why an old approval does not authorize the current mission revision.

## Discussion notes

A shared variable joins facts about the same identifier. Multiple values
produce separate bindings, not assignment. Recursion propagates consequences
through a finite graph. Unknown is not false; closure is a completeness
commitment. Permission is about the current state, not the existence of any
earlier approval. These are the conceptual checks to master before
connecting a language model.

## Reproduce the executable checks

```bash
python3 scripts/check-examples.py --binary /path/to/framex
```

Run this from the FrameX-Doc repository after installing the engine and
Python package. The checker verifies tutorial query rows and expectations,
the complete family program, the namespace and external-request examples,
the extraction receipt scenarios, and the Python exercise outputs. It also
runs the tool-query episode and scripted dialogue without a model.

For the schema lesson, experiment with `framex validate` on a saved copy as
described in [Lesson 6](./lesson-06-schema.md). The new
[grounded extraction example](../examples/grounded-extraction.md) includes
downloadable receipts for valid evidence, refused evidence and a failed call.
