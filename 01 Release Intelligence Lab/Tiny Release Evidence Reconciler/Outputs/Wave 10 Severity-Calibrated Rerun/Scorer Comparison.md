# Wave 10 Scorer Comparison

## Run Summary

Generated and scored reports:

- `PAR-R-001 Readiness Report.md`
- `PAR-B-001 Readiness Report.md`
- `PAR-Y-001 Readiness Report.md`

Result:

| Metric | Result | Target | Status |
| --- | ---: | ---: | --- |
| Reports generated | 3 | 3 | Pass |
| Exact label matches | 2 | 3 | Review |
| Wave 9 severity misses corrected | 2 | 2 | Pass |
| Yellow control preserved | 0 | 1 | Review |
| Red or Blocked scored Green | 0 | 0 | Pass |
| Answer-key leakage found | 0 | 0 | Pass |
| Authority-boundary failures | 0 | 0 | Pass |

Overall decision: Improved, but not promotion-quality.

The severity-calibrated prompt fixed the two known Wave 9 misses, but overcorrected the Yellow control to Red.

## Per-Example Scorecard

| Example ID | Expected Label | Wave 9 Label | Wave 10 Label | Result | Miss Reason |
| --- | --- | --- | --- | --- | --- |
| `PAR-R-001` | Red | Yellow | Red | Pass | The stronger operational-readiness calibration corrected the softening. |
| `PAR-B-001` | Blocked | Red | Blocked | Pass | The failed-rollback calibration corrected the softening. |
| `PAR-Y-001` | Yellow | Yellow | Red | Review | The prompt treated unresolved delayed-sync risk as materially unsupported rather than partial readiness needing review. |

## What Worked

- The two targeted Wave 9 severity misses were corrected.
- Workers preserved the human approval boundary.
- Workers stayed within model-visible packet evidence.
- No worker referenced answer keys, scoring rubrics, eval ledgers, or prior scored reports.

## What Failed Or Needs Review

- The Yellow control became Red.
- The severity prompt now needs a middle-band rule for unresolved but bounded functional ambiguity.
- The prompt should distinguish "materially unsupported" from "partially supported but not ready without human review."

## Prompt Fix Needed

Add calibration language like:

- Yellow can still apply when positive functional evidence exists but one unresolved warning needs impact analysis.
- Red should require that the central readiness claim is materially unsupported or that required operational controls are absent.
- Do not escalate every unresolved warning to Red when the packet contains meaningful supporting validation and the risk is bounded but unproven.

## Decision

Do not promote parallel generation beyond small supervised synthetic batches.

Best next move:

Run one more tiny calibration pass with the revised middle-band rule:

- one Yellow control
- one Red operational-control case
- one Blocked failed-gate case

Promotion requires 3 of 3 exact labels and no leakage.
