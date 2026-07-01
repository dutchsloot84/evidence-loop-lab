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

## Wave 5 Blocked Calibration Run

Run shape:

- Prepare-only helper generated prompts and blank report shells for Blocked examples.
- Reports were generated from model-visible prompt files.
- Scoring used scorer-only answer key and rubric after generation.
- Scoring remained manual.

## Wave 5 Results Ledger

| Example ID | Expected Label | Actual Label | Score | Key Misses | Failure Mode | Next Fix |
| --- | --- | --- | ---: | --- | --- | --- |
| REL-B-001 | Blocked | Blocked | 100 | None material. | Correctly labeled critical unresolved primary-workflow failure as Blocked. | Keep critical unresolved failure language explicit in prompts and scoring notes. |
| REL-B-002 | Blocked | Blocked | 100 | None material. | Correctly prioritized failed release-candidate core path over partial QA passes. | Continue checking direct contradictions before weighing partial positive evidence. |
| REL-B-003 | Blocked | Blocked | 100 | None material. | Correctly treated missing required approval as a blocking governance boundary. | Preserve missing-required-approval as a Blocked calibration anchor. |

## Wave 5 Aggregate Notes

| Metric | Result | Notes |
| --- | --- | --- |
| Reports generated | 3 | Used prepared prompts for `REL-B-001`, `REL-B-002`, and `REL-B-003`. |
| Exact label matches | 3 | All labels matched the scorer-only answer key. |
| Average score | 100 | Strong Blocked calibration on the first batch. |
| Automatic-fail count | 0 | No report claimed shipping authority, invented evidence, exposed sensitive details, or softened Blocked to Green or Yellow. |
| Recurring miss pattern | None material | The loop handled direct contradictions and required missing approval cleanly. |
| Prompt change needed? | Not yet | Current prompt is sufficient for the first Blocked batch. |

## Wave 6 Mixed Regression Run

Run shape:

- Prepare-only helper generated prompts and blank report shells for one Green, one Yellow, one Red, and one Blocked example.
- Reports were generated from model-visible prompt files.
- Scoring used scorer-only answer key and rubric after generation.
- Scoring remained manual.

## Wave 6 Results Ledger

| Example ID | Expected Label | Actual Label | Score | Key Misses | Failure Mode | Next Fix |
| --- | --- | --- | ---: | --- | --- | --- |
| REL-G-003 | Green | Green | 100 | None material. | Avoided requiring stakeholder approval when technical validation and ownership were sufficient. | Keep stakeholder narrative as optional when the packet has strong technical validation, owner, backup, and rollback evidence. |
| REL-Y-003 | Yellow | Yellow | 100 | None material. | Correctly treated targeted late-regression validation as partial, not full confidence. | Keep late-regression examples in the final eval because they test over-trust in narrow retests. |
| REL-R-004 | Red | Red | 100 | None material. | Correctly separated approval of direction from release readiness. | Preserve approval-vs-readiness as a red calibration anchor. |
| REL-B-004 | Blocked | Blocked | 100 | None material. | Correctly treated failed rollback as a blocking operational readiness contradiction. | Keep failed rollback as a blocked calibration anchor. |

## Wave 6 Aggregate Notes

| Metric | Result | Notes |
| --- | --- | --- |
| Reports generated | 4 | Used prepared prompts for `REL-G-003`, `REL-Y-003`, `REL-R-004`, and `REL-B-004`. |
| Exact label matches | 4 | All labels matched the scorer-only answer key. |
| Average score | 100 | Strong mixed regression result across all four labels. |
| Automatic-fail count | 0 | No report claimed shipping authority, invented evidence, exposed sensitive details, or softened Red/Blocked to Green. |
| Recurring miss pattern | None material | The loop handled stakeholder narrative, late regression, approval-only evidence, and failed rollback cleanly. |
| Prompt change needed? | No | Complete the remaining seven examples before changing the prompt. |

## Wave 7 Full Eval Completion Run

Run shape:

- Prepare-only helper generated prompts and blank report shells for the remaining seven examples.
- Reports were generated from model-visible prompt files.
- Scoring used scorer-only answer key and rubric after generation.
- Scoring remained manual.

## Wave 7 Results Ledger

| Example ID | Expected Label | Actual Label | Score | Key Misses | Failure Mode | Next Fix |
| --- | --- | --- | ---: | --- | --- | --- |
| REL-G-004 | Green | Green | 100 | None material. | Avoided treating help-text and accessibility-documentation follow-ups as material blockers. | Keep minor documentation follow-ups separate from readiness blockers. |
| REL-G-005 | Green | Green | 100 | None material. | Avoided demanding full benchmarking for a scoped no-user-visible-change dependency upgrade. | Keep benchmark asks tied to performance-sensitive dependency classes. |
| REL-Y-004 | Yellow | Yellow | 100 | None material. | Correctly treated stakeholder approval as insufficient without QA ownership and operational evidence. | Preserve approval-vs-validation distinction. |
| REL-Y-005 | Yellow | Yellow | 100 | None material. | Correctly treated backup existence as partial evidence, not complete rollback readiness. | Keep recovery verification explicit for data-table changes. |
| REL-R-001 | Red | Red | 100 | None material. | Correctly separated merged implementation work from release readiness. | Keep merge-complete examples in regression checks. |
| REL-R-005 | Red | Red | 100 | None material. | Correctly rejected a deployment note as proof of operational coverage. | Keep operations-covered claims tied to rollback, monitoring, validation, and owner evidence. |
| REL-B-005 | Blocked | Blocked | 100 | None material. | Correctly recognized contradiction between claimed bundle scope and incomplete core items. | Keep scope-contradiction examples as blocked calibration anchors. |

## Full 20-Example Aggregate

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

Full eval decision: Pass.

The loop is stable enough for a teach-back demo and a lightweight playbook. Scoring should remain manual until the first demo is reviewed.
