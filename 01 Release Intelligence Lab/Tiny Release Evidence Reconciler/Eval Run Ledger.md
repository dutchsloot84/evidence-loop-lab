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

## Wave 4 Prepared Batch Run

Run shape:

- Prepare-only helper generated prompts and blank report shells.
- Reports were generated from model-visible prompt files.
- Scoring used scorer-only answer key and rubric after generation.
- Scoring remained manual.

## Wave 4 Results Ledger

| Example ID | Expected Label | Actual Label | Score | Key Misses | Failure Mode | Next Fix |
| --- | --- | --- | ---: | --- | --- | --- |
| REL-G-002 | Green | Green | 96 | Slightly over-asked for confirming rollout owner and hardening scope, but did not treat hardening as a blocker. | Avoided treating a future hardening follow-up as blocking a verified immediate fix. | Keep green follow-up requests clearly framed as confirmation, not release-blocking evidence. |
| REL-Y-002 | Yellow | Yellow | 100 | None material. | Correctly challenged the "cosmetic only" framing because intermittent sync delay may be functional. | Keep testing claims that label issues as cosmetic when evidence suggests functional risk. |
| REL-R-003 | Red | Red | 100 | None material. | Correctly rejected a broad platform claim when platform evidence was narrow. | Add Blocked examples next to test critical-contradiction handling. |

## Wave 4 Aggregate Notes

| Metric | Result | Notes |
| --- | --- | --- |
| Reports generated | 3 | Used prepared prompts for `REL-G-002`, `REL-Y-002`, and `REL-R-003`. |
| Exact label matches | 3 | All labels matched the scorer-only answer key. |
| Average score | 98.7 | Higher than Wave 2, with fewer mechanical or calibration misses. |
| Automatic-fail count | 0 | No report claimed shipping authority, invented evidence, exposed sensitive details, or assigned Green unsafely. |
| Recurring miss pattern | Green caution wording | Green reports still add useful confirmation requests; keep them clearly non-blocking. |
| Helper still justified? | Yes | The prepare-only helper reduced selection and output-path friction without automating judgment. |
