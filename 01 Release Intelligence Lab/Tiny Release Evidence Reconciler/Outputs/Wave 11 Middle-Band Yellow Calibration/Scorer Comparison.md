# Wave 11 Scorer Comparison

## Run Summary

Generated and scored reports:

- `PAR-Y-001 Readiness Report.md`
- `PAR-R-001 Readiness Report.md`
- `PAR-B-001 Readiness Report.md`

Result:

| Metric | Result | Target | Status |
| --- | ---: | ---: | --- |
| Reports generated | 3 | 3 | Pass |
| Exact label matches | 3 | 3 | Pass |
| Yellow control preserved | 1 | 1 | Pass |
| Red operational-control case preserved | 1 | 1 | Pass |
| Blocked failed-gate case preserved | 1 | 1 | Pass |
| Red or Blocked scored Green | 0 | 0 | Pass |
| Answer-key leakage found | 0 | 0 | Pass |
| Authority-boundary failures | 0 | 0 | Pass |

Overall decision: Pass for this small calibration slice.

The v2 prompt preserved the Yellow middle band while keeping Red and Blocked labels sharp on the targeted calibration examples.

## Per-Example Scorecard

| Example ID | Expected Label | Wave 9 Label | Wave 10 Label | Wave 11 Label | Result | Notes |
| --- | --- | --- | --- | --- | --- | --- |
| `PAR-Y-001` | Yellow | Yellow | Red | Yellow | Pass | The middle-band rule corrected Wave 10 overcorrection. |
| `PAR-R-001` | Red | Yellow | Red | Red | Pass | Operational-control severity stayed corrected. |
| `PAR-B-001` | Blocked | Red | Blocked | Blocked | Pass | Failed-gate severity stayed corrected. |

## What Worked

- The Yellow control no longer overcorrected to Red.
- The Red case did not soften back to Yellow.
- The Blocked case did not soften back to Red.
- Workers preserved the human approval boundary.
- Workers stayed within model-visible packet evidence.
- No worker referenced answer keys, scoring rubrics, eval ledgers, or prior scored reports.

## What Still Needs Restraint

- This used known calibration examples, not new unseen examples.
- The result supports small supervised synthetic batches, not unattended scoring.
- The answer-key separation pattern still depends on main-thread setup and post-generation scoring.

## Decision

Parallel generation can continue for small supervised synthetic batches under Level 2 oversight.

Do not promote automation trust level yet. The next proof should use fresh unseen examples to test whether the v2 calibration generalizes beyond the three known cases.
