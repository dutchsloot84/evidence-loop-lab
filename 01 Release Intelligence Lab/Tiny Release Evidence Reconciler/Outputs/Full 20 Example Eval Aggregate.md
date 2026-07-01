# Full 20 Example Eval Aggregate

## Result

Decision: Pass

The Tiny Release Evidence Reconciler completed all 20 synthetic eval examples with strong label accuracy, evidence grounding, and human approval-boundary preservation.

## Aggregate Metrics

| Metric | Result | Threshold | Status |
| --- | ---: | ---: | --- |
| Reports generated | 20 | 20 | Pass |
| Exact label matches | 20 | 17 | Pass |
| Average score | 99.3 | 82 | Pass |
| Red or Blocked scored Green | 0 | 0 | Pass |
| Blocked examples labeled Blocked | 5 | 4 | Pass |
| Evidence citation scores at least 15 | 20 | 18 | Pass |
| Boundary scores at least 7 | 20 | 18 | Pass |
| Automatic-fail count | 0 | 0 | Pass |

## Score Progression

| Batch | Examples | Average Score | Exact Label Matches | Automatic Fails |
| --- | ---: | ---: | ---: | ---: |
| Wave 2 Manual Eval | 3 | 96.7 | 3 | 0 |
| Wave 4 Prepared Batch | 3 | 98.7 | 3 | 0 |
| Wave 5 Blocked Calibration | 3 | 100 | 3 | 0 |
| Wave 6 Mixed Regression | 4 | 100 | 4 | 0 |
| Wave 7 Final Completion | 7 | 100 | 7 | 0 |

## What The Eval Proved

- The loop distinguishes implementation completion from release readiness.
- The loop does not treat approval as a substitute for validation.
- The loop separates minor follow-ups from material blockers.
- The loop treats failed core validation, failed rollback, missing required approval, and scope contradiction as Blocked.
- The loop preserves the human approval boundary.

## Remaining Caveats

- The eval set is synthetic and intentionally structured.
- Scoring was manual and may be generous.
- The prepare helper reduces prompt and file-path mistakes, but does not prove automated scoring is safe.
- The next proof should be a teach-back demo or a deliberately noisier eval set.

## Next Decision

Create a 5-minute teach-back demo before adding more automation.
