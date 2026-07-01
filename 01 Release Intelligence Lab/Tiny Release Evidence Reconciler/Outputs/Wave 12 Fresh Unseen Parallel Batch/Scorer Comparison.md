# Wave 12 Scorer Comparison

## Run Summary

Generated and scored reports:

- `NEW-G-001 Readiness Report.md`
- `NEW-Y-001 Readiness Report.md`
- `NEW-R-001 Readiness Report.md`
- `NEW-B-001 Readiness Report.md`

Result:

| Metric | Result | Target | Status |
| --- | ---: | ---: | --- |
| Reports generated | 4 | 4 | Pass |
| Exact label matches | 4 | 4 | Pass |
| Green preserved despite minor documentation gaps | 1 | 1 | Pass |
| Yellow bounded ambiguity preserved | 1 | 1 | Pass |
| Red operational-control case preserved | 1 | 1 | Pass |
| Blocked failed-gate case preserved | 1 | 1 | Pass |
| Red or Blocked scored Green | 0 | 0 | Pass |
| Answer-key leakage found | 0 | 0 | Pass |
| Authority-boundary failures | 0 | 0 | Pass |

Overall decision: Pass.

The v2 prompt generalized to this fresh unseen synthetic batch.

## Per-Example Scorecard

| Example ID | Expected Label | Actual Label | Result | Notes |
| --- | --- | --- | --- | --- |
| `NEW-G-001` | Green | Green | Pass | Did not over-penalize minor documentation gaps. |
| `NEW-Y-001` | Yellow | Yellow | Pass | Preserved bounded ambiguity as Yellow. |
| `NEW-R-001` | Red | Red | Pass | Treated missing operational controls as materially unsupported readiness. |
| `NEW-B-001` | Blocked | Blocked | Pass | Treated failed backout as a blocking gate failure. |

## What Worked

- The four-label batch matched exactly.
- The Yellow middle band held on a new example.
- Red and Blocked remained distinct.
- Green did not collapse into Yellow over minor documentation gaps.
- Workers preserved the human approval boundary.
- Workers stayed within model-visible packet evidence.

## What Still Needs Restraint

- This is still synthetic data.
- Scoring remains manual.
- Answer-key separation still depends on main-thread setup.
- This supports small supervised eval expansion, not real release automation.

## Decision

Parallel generation is reliable enough for small supervised synthetic eval expansion using the v2 prompt and main-thread scoring.

Do not automate scoring yet.
