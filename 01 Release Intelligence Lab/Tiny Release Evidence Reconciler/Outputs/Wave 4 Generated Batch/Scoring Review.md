# Wave 4 Generated Batch Scoring Review

## Run Summary

Generated and scored reports:

- `REL-G-002 Readiness Report.md`
- `REL-Y-002 Readiness Report.md`
- `REL-R-003 Readiness Report.md`

Result:

| Metric | Result |
| --- | ---: |
| Reports generated | 3 |
| Exact label matches | 3 |
| Average score | 98.7 |
| Automatic-fail count | 0 |

## Per-Example Scorecard

| Example ID | Expected Label | Actual Label | Label Pts /25 | Evidence Pts /20 | Unsupported Pts /15 | Gaps Pts /12 | Next Evidence Pts /10 | Risk Pts /10 | Boundary Pts /8 | Total /100 | Pass? | Miss Reason |
| --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| REL-G-002 | Green | Green | 25 | 20 | 14 | 11 | 9 | 9 | 8 | 96 | Pass | Slightly cautious about hardening scope and rollout ownership, but did not turn them into blockers. |
| REL-Y-002 | Yellow | Yellow | 25 | 20 | 15 | 12 | 10 | 10 | 8 | 100 | Pass | None material. |
| REL-R-003 | Red | Red | 25 | 20 | 15 | 12 | 10 | 10 | 8 | 100 | Pass | None material. |

## Comparison To Wave 2

| Metric | Wave 2 | Wave 4 |
| --- | ---: | ---: |
| Reports generated | 3 | 3 |
| Exact label matches | 3 | 3 |
| Average score | 96.7 | 98.7 |
| Automatic-fail count | 0 | 0 |

Wave 4 reduced mechanical uncertainty because the prepare helper created consistent prompt and report paths. The remaining miss pattern is not tooling; it is calibration language in Green cases. The reports should keep useful follow-up asks, but make clear when those asks are not required to support the current readiness claim.

## Decision

Keep the prepare-only helper. Do not automate scoring yet.

The next batch should add Blocked examples before expanding to the rest of the dataset. The lab has now tested Green, Yellow, and Red behavior twice, but has not yet tested whether the loop catches direct contradictions or critical unresolved failures.
