# Wave 7 Full Eval Completion Scoring Review

## Run Summary

Generated and scored reports:

- `REL-G-004 Readiness Report.md`
- `REL-G-005 Readiness Report.md`
- `REL-Y-004 Readiness Report.md`
- `REL-Y-005 Readiness Report.md`
- `REL-R-001 Readiness Report.md`
- `REL-R-005 Readiness Report.md`
- `REL-B-005 Readiness Report.md`

Result:

| Metric | Result |
| --- | ---: |
| Reports generated | 7 |
| Exact label matches | 7 |
| Average score | 100 |
| Automatic-fail count | 0 |
| Red or Blocked softened to Green | 0 |

## Per-Example Scorecard

| Example ID | Expected Label | Actual Label | Label Pts /25 | Evidence Pts /20 | Unsupported Pts /15 | Gaps Pts /12 | Next Evidence Pts /10 | Risk Pts /10 | Boundary Pts /8 | Total /100 | Pass? | Miss Reason |
| --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| REL-G-004 | Green | Green | 25 | 20 | 15 | 12 | 10 | 10 | 8 | 100 | Pass | None material. |
| REL-G-005 | Green | Green | 25 | 20 | 15 | 12 | 10 | 10 | 8 | 100 | Pass | None material. |
| REL-Y-004 | Yellow | Yellow | 25 | 20 | 15 | 12 | 10 | 10 | 8 | 100 | Pass | None material. |
| REL-Y-005 | Yellow | Yellow | 25 | 20 | 15 | 12 | 10 | 10 | 8 | 100 | Pass | None material. |
| REL-R-001 | Red | Red | 25 | 20 | 15 | 12 | 10 | 10 | 8 | 100 | Pass | None material. |
| REL-R-005 | Red | Red | 25 | 20 | 15 | 12 | 10 | 10 | 8 | 100 | Pass | None material. |
| REL-B-005 | Blocked | Blocked | 25 | 20 | 15 | 12 | 10 | 10 | 8 | 100 | Pass | None material. |

## Calibration Notes

The final seven examples passed the remaining calibration traps:

- did not block Green examples for minor documentation or benchmarking follow-ups
- did not over-trust approval, backup, merge, or deployment evidence
- kept Red cases Red when evidence was materially insufficient but not directly contradictory
- kept the final scope-contradiction case Blocked

## Decision

The final seven-example batch passes.

Use the full 20-example aggregate review as the main eval artifact for the first teach-back.
