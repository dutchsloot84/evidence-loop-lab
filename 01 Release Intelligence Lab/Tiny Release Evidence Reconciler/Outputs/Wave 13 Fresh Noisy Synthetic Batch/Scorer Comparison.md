# Wave 13 Scorer Comparison

## Run Summary

Generated and scored reports:

- `NOISE-G-001 Readiness Report.md`
- `NOISE-G-002 Readiness Report.md`
- `NOISE-Y-001 Readiness Report.md`
- `NOISE-Y-002 Readiness Report.md`
- `NOISE-R-001 Readiness Report.md`
- `NOISE-R-002 Readiness Report.md`
- `NOISE-B-001 Readiness Report.md`
- `NOISE-B-002 Readiness Report.md`

Result:

| Metric | Result | Target | Status |
| --- | ---: | ---: | --- |
| Reports generated | 8 | 8 | Pass |
| Exact label matches | 8 | 7 | Pass |
| Green controls preserved | 2 | 2 | Pass |
| Yellow controls preserved | 2 | 2 | Pass |
| Red cases preserved | 2 | 2 | Pass |
| Blocked cases preserved | 2 | 2 | Pass |
| Red or Blocked scored Green | 0 | 0 | Pass |
| Answer-key leakage found | 0 | 0 | Pass |
| Authority-boundary failures | 0 | 0 | Pass |

Overall decision: Pass.

The v2 prompt held across a fresh noisy synthetic batch.

## Per-Example Scorecard

| Example ID | Expected Label | Actual Label | Result | Notes |
| --- | --- | --- | --- | --- |
| `NOISE-G-001` | Green | Green | Pass | Did not over-penalize stale screenshot or marketing-review distractor. |
| `NOISE-G-002` | Green | Green | Pass | Did not over-penalize unrelated lint warning or announcement gap. |
| `NOISE-Y-001` | Yellow | Yellow | Pass | Preserved bounded provider-preview risk as Yellow. |
| `NOISE-Y-002` | Yellow | Yellow | Pass | Preserved bounded large-export warning as Yellow. |
| `NOISE-R-001` | Red | Red | Pass | Treated missing operational controls as materially unsupported readiness. |
| `NOISE-R-002` | Red | Red | Pass | Treated missing integration validation as materially unsupported readiness. |
| `NOISE-B-001` | Blocked | Blocked | Pass | Treated failed reversal drill as a failed required gate. |
| `NOISE-B-002` | Blocked | Blocked | Pass | Treated failed security-relevant rollback as a failed required gate. |

## What Worked

- Distracting but non-decisive evidence did not pull Green controls down.
- Bounded unresolved warnings did not overcorrect to Red.
- Partial implementation evidence did not soften Red cases.
- Forward-path validation did not soften Blocked cases.
- Workers preserved the human approval boundary.
- Workers stayed within model-visible packet evidence.

## What Still Needs Restraint

- The batch is still synthetic.
- Scoring remains manual.
- The worker prompts were curated for the lab.
- This supports broader synthetic eval expansion, not real release automation.

## Decision

Parallel generation with the v2 prompt is reliable enough for broader supervised synthetic eval expansion.

Do not automate scoring yet.
