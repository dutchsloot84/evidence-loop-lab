# Wave 9 ROI Review

## Question

Did parallel generation improve throughput enough to justify the added coordination risk?

## Result

Decision: Useful, but not yet promotable.

Parallel generation produced four reports quickly and preserved answer-key separation, but two severity labels were softened. The value came from surfacing the coordination risk, not from saving enough time to justify expanding immediately.

## ROI Summary

| Dimension | Result |
| --- | --- |
| Speed | Positive. Four reports returned quickly once workers were launched. |
| Quality | Mixed. Two exact matches, two severity misses. |
| Safety | Good. No answer-key leakage or authority-boundary failure found. |
| Coordination overhead | Moderate. Worker prompts, collection, scoring, and audit added real work. |
| Reuse value | High. This creates the first real parallel-agent governance artifact. |

## Best Use Going Forward

Use parallel generation when:

- examples are synthetic or sanitized
- answer-key separation is enforceable
- main-thread scoring is required
- the goal is throughput or agent-governance testing

Avoid parallel generation when:

- labels are safety-sensitive and prompt calibration is untested
- outputs will influence real release or product decisions
- scoring would be skipped
- workers could access sensitive or scorer-only context

## Next Fix

Create a stronger generation-only worker prompt that includes severity calibration rules:

- Missing operational controls can make a claim Red.
- Failed rollback can make a claim Blocked.
- Positive implementation evidence does not erase operational contradictions.
- Deployment commands do not prove operational coverage.

Then rerun a four-example parallel trust test.
