# Eval Run Ledger

Scorer-side ledger for Tiny Release Evidence Reconciler eval runs.

Keep this ledger synthetic and sanitized. Do not paste real release details, company names, customer names, employee names, repo names, ticket IDs, links, exact titles, or sensitive context.

## Wave 2 Manual Eval Run

Run shape:

- Local-first manual eval
- No eval runner required
- Model-visible input: `Mock Data/Release Packets.md`
- Scorer-only reference: `Mock Data/Answer Key.md`
- Rubric: `Scoring Rubric.md`
- First run size: exactly 3 packets

## Results Ledger

| Example ID | Expected Label | Actual Label | Score | Key Misses | Failure Mode | Next Fix |
| --- | --- | --- | ---: | --- | --- | --- |
| REL-G-001 | Green | Green | 92 | Slightly over-asked for owner-rotation and visual-deferral evidence in a green case. | Minor over-penalization of cosmetic or operational follow-up despite strong readiness evidence. | Distinguish nice-to-have closure evidence from material release-readiness evidence. |
| REL-Y-001 | Yellow | Yellow | 100 | None material. | Avoided marking green just because some tests passed and review approval existed. | Keep using missing QA, rollback, and monitoring as yellow calibration anchors. |
| REL-R-002 | Red | Red | 98 | Could state more directly why this is red rather than blocked. | Avoided downplaying a known workflow issue, but should name the optional/non-critical-path distinction. | Add a red-vs-blocked sentence when a known issue remains unresolved. |

## Aggregate Notes

| Metric | Result | Notes |
| --- | --- | --- |
| Reports generated | 3 | First manual run used `REL-G-001`, `REL-Y-001`, and `REL-R-002`. |
| Exact label matches | 3 | All selected labels matched the scorer-only answer key. |
| Average score | 96.7 | Strong enough to expand the eval run, but still useful for calibration. |
| Automatic-fail count | 0 | No report claimed shipping authority, invented evidence, exposed sensitive details, or assigned Green unsafely. |
| Recurring miss pattern | Calibration nuance | Green reports should not over-weight minor follow-ups; red reports should explain why the issue is not blocked when applicable. |
| Tiny script justified? | Yes, prepare-only | A tiny prepare helper is justified before expanding beyond 3 examples. Scoring should remain manual. |

## Script Decision Notes

Use this section after scoring the 3-packet run.

- Evidence that a script would reduce errors:
  - The next run should expand beyond 3 examples, so consistent packet selection and output paths matter.
  - A prepare-only helper would reduce copy/paste and file-naming mistakes without automating judgment.
- Evidence that manual process should stay manual for now:
  - Label scoring and failure-mode interpretation still benefit from human calibration.
  - The main learning signal is the scorer's reasoning about gaps, not tool speed.
- Proposed smallest useful script behavior:
  - Select one packet by example ID.
  - Print a generation prompt using only model-visible materials.
  - Create or point to a predictable report output path.
