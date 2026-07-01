# Wave 6 Mixed Regression Scoring Review

## Run Summary

Generated and scored reports:

- `REL-G-003 Readiness Report.md`
- `REL-Y-003 Readiness Report.md`
- `REL-R-004 Readiness Report.md`
- `REL-B-004 Readiness Report.md`

Result:

| Metric | Result |
| --- | ---: |
| Reports generated | 4 |
| Exact label matches | 4 |
| Average score | 100 |
| Automatic-fail count | 0 |
| Red or Blocked softened to Green | 0 |

## Per-Example Scorecard

| Example ID | Expected Label | Actual Label | Label Pts /25 | Evidence Pts /20 | Unsupported Pts /15 | Gaps Pts /12 | Next Evidence Pts /10 | Risk Pts /10 | Boundary Pts /8 | Total /100 | Pass? | Miss Reason |
| --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| REL-G-003 | Green | Green | 25 | 20 | 15 | 12 | 10 | 10 | 8 | 100 | Pass | None material. |
| REL-Y-003 | Yellow | Yellow | 25 | 20 | 15 | 12 | 10 | 10 | 8 | 100 | Pass | None material. |
| REL-R-004 | Red | Red | 25 | 20 | 15 | 12 | 10 | 10 | 8 | 100 | Pass | None material. |
| REL-B-004 | Blocked | Blocked | 25 | 20 | 15 | 12 | 10 | 10 | 8 | 100 | Pass | None material. |

## Calibration Notes

The mixed regression batch passed all four intended traps:

- `REL-G-003`: did not over-demand stakeholder approval when validation, ownership, backup, and rollback were sufficient.
- `REL-Y-003`: did not over-trust a narrow late-regression fix.
- `REL-R-004`: did not treat approval of direction as release readiness.
- `REL-B-004`: did not ignore failed rollback because forward staging validation passed.

## Aggregate Progress

Completed scored examples: 13 of 20.

Remaining examples:

- `REL-G-004`
- `REL-G-005`
- `REL-Y-004`
- `REL-Y-005`
- `REL-R-001`
- `REL-R-005`
- `REL-B-005`

## Decision

Complete the remaining seven examples next. The loop has passed enough mixed calibration to make the full eval set more valuable than another small probe.
