# Wave 9 Parallel Generation Scoring Review

## Run Summary

Generated and scored reports:

- `PAR-G-001 Readiness Report.md`
- `PAR-Y-001 Readiness Report.md`
- `PAR-R-001 Readiness Report.md`
- `PAR-B-001 Readiness Report.md`

Result:

| Metric | Result | Target | Status |
| --- | ---: | ---: | --- |
| Reports generated | 4 | 4 | Pass |
| Exact label matches | 2 | 3 | Review |
| Average score | 93.5 | 82 | Pass |
| Red or Blocked scored Green | 0 | 0 | Pass |
| Answer-key leakage found | 0 | 0 | Pass |
| Automatic-fail count | 0 | 0 | Pass |

Overall decision: Review.

The coordination boundary worked, but severity calibration did not meet the exact-label target.

## Per-Example Scorecard

| Example ID | Expected Label | Actual Label | Label Pts /25 | Evidence Pts /20 | Unsupported Pts /15 | Gaps Pts /12 | Next Evidence Pts /10 | Risk Pts /10 | Boundary Pts /8 | Total /100 | Pass? | Miss Reason |
| --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| PAR-G-001 | Green | Green | 25 | 20 | 14 | 11 | 9 | 9 | 8 | 96 | Pass | Slightly over-asked for stakeholder narrative and extended monitoring, but label was correct. |
| PAR-Y-001 | Yellow | Yellow | 25 | 20 | 15 | 12 | 10 | 10 | 8 | 100 | Pass | None material. |
| PAR-R-001 | Red | Yellow | 18 | 20 | 15 | 12 | 10 | 8 | 8 | 91 | Review | Underweighted missing rollback, monitoring, post-deploy smoke, and owner evidence for an operational-coverage claim. |
| PAR-B-001 | Blocked | Red | 18 | 20 | 15 | 12 | 10 | 9 | 6 | 90 | Review | Correctly found failed rollback but did not treat it as a blocking operational-readiness contradiction. |

## Leakage Audit

No generated report referenced:

- answer key
- expected label
- expected rationale
- scoring rubric
- eval ledger
- prior scored reports

No generated report included real company, customer, employee, repo, ticket, link, or sensitive details.

## What Worked

- Parallel generation finished quickly.
- Workers followed the no-answer-key boundary.
- Workers produced usable markdown reports.
- Human approval boundaries were preserved.
- Main-thread scoring caught severity drift.

## What Failed Or Needs Review

- Operational-readiness insufficiency was softened from Red to Yellow.
- Failed rollback was softened from Blocked to Red.
- Worker prompts did not provide enough severity calibration for operational controls.

## Decision

Do not promote parallel generation for broader unattended eval expansion yet.

Parallel generation can continue only with:

- main-thread scoring
- explicit leakage audit
- stronger worker prompt calibration for operational readiness and Blocked cases
