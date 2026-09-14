# 15. From knowledge to controlled agents

```framex
world open.
mission[currentRevision -> r2].
check1:Check[revision -> r1; approved -> true].
mission:MayProceed <- mission[currentRevision -> ?Revision]
    AND ?Check:Check[revision -> ?Revision; approved -> true].
?- mission:MayProceed.
expect unknown: mission:MayProceed.
```

The check approves an older revision. The current revision is r2, so the
rule cannot derive permission. In this open model the question is unknown.
It is not safe to proceed merely because some approval exists somewhere in
the database.

FrameX models preconditions, evidence requirements, workflow states and
permission rules. An external host invokes tools, records receipts and
updates observations; the engine then recomputes consequences. Revision
matching prevents a stale approval from authorizing a new state.

For H2, a model can propose an interpretation or extracted fact for FrameX
to check. In the other direction, derived answers and provenance can
constrain a prompt that asks the model to explain or request clarification.
For H3, rules determine the next eligible action and the conditions for
adaptation or termination. Python supplies generic adapters rather than
hiding domain policy in a convenience function.

External declarations need the documented tool host; an offline rule run is
not evidence of a real model call.

## Try it

Change the current revision to r1 and predict the permission. Then explain
what an executor must check again immediately before acting.
