# Wave 5 Blocked Calibration Scoring Review

## Run Summary

Generated and scored reports:

- `REL-B-001 Readiness Report.md`
- `REL-B-002 Readiness Report.md`
- `REL-B-003 Readiness Report.md`

Result:

| Metric | Result |
| --- | ---: |
| Reports generated | 3 |
| Exact label matches | 3 |
| Average score | 100 |
| Automatic-fail count | 0 |
| Blocked softened to Red/Yellow/Green | 0 |

## Per-Example Scorecard

| Example ID | Expected Label | Actual Label | Label Pts /25 | Evidence Pts /20 | Unsupported Pts /15 | Gaps Pts /12 | Next Evidence Pts /10 | Risk Pts /10 | Boundary Pts /8 | Total /100 | Pass? | Miss Reason |
| --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| REL-B-001 | Blocked | Blocked | 25 | 20 | 15 | 12 | 10 | 10 | 8 | 100 | Pass | None material. |
| REL-B-002 | Blocked | Blocked | 25 | 20 | 15 | 12 | 10 | 10 | 8 | 100 | Pass | None material. |
| REL-B-003 | Blocked | Blocked | 25 | 20 | 15 | 12 | 10 | 10 | 8 | 100 | Pass | None material. |

## Calibration Notes

The loop correctly identified three different Blocked patterns:

- critical unresolved primary-workflow failure
- failed release-candidate core-path test
- required missing approval gate

This matters more than the score alone. These are the cases where an evidence loop must avoid optimistic smoothing. In this batch, partial positive evidence did not override direct contradiction or required missing approval.

## Comparison To Earlier Waves

| Metric | Wave 2 | Wave 4 | Wave 5 |
| --- | ---: | ---: | ---: |
| Reports generated | 3 | 3 | 3 |
| Exact label matches | 3 | 3 | 3 |
| Average score | 96.7 | 98.7 | 100 |
| Automatic-fail count | 0 | 0 | 0 |

## Decision

Keep the prompt unchanged for now.

Next, prepare and run the remaining 11 examples to complete the 20-example eval set, or run a smaller mixed regression batch if time is tight.
