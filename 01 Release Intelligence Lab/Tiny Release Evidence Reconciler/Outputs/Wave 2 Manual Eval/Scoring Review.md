# Wave 2 Manual Eval Scoring Review

## Run Summary

Scored reports:

- `REL-G-001 Readiness Report.md`
- `REL-Y-001 Readiness Report.md`
- `REL-R-002 Readiness Report.md`

Result:

| Metric | Result |
| --- | ---: |
| Reports generated | 3 |
| Exact label matches | 3 |
| Average score | 96.7 |
| Automatic-fail count | 0 |

## Per-Example Scorecard

| Example ID | Expected Label | Actual Label | Label Pts /25 | Evidence Pts /20 | Unsupported Pts /15 | Gaps Pts /12 | Next Evidence Pts /10 | Risk Pts /10 | Boundary Pts /8 | Total /100 | Pass? | Miss Reason |
| --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| REL-G-001 | Green | Green | 25 | 20 | 13 | 10 | 8 | 8 | 8 | 92 | Pass | Slightly over-asked for cleanup evidence despite strong green readiness evidence. |
| REL-Y-001 | Yellow | Yellow | 25 | 20 | 15 | 12 | 10 | 10 | 8 | 100 | Pass | None material. |
| REL-R-002 | Red | Red | 25 | 20 | 15 | 12 | 10 | 8 | 8 | 98 | Pass | Could state the red-vs-blocked distinction more explicitly. |

## Calibration Notes

The loop successfully checked readiness claims against evidence without using scorer-only material during report generation.

The green case shows the first calibration issue: a report can recommend Green while still sounding slightly too cautious. Minor visual issues or owner-rotation follow-ups should be named as follow-ups, not treated like material release blockers when regression, smoke, review, rollback, deployment, and monitoring evidence are present.

The red case shows the second calibration issue: when a known issue remains unresolved, the report should explain whether the issue contradicts a critical path or merely makes the broad rollout claim unsupported. That distinction is what separates Red from Blocked.

## Decision

Move to a prepare-only helper before expanding the run beyond 3 examples.

Keep scoring manual for now. The next useful automation should reduce selection, prompt, and output-path errors, but should not assign labels or scores automatically.
