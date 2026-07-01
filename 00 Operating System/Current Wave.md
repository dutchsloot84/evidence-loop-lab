# Current Wave

## Status

Status: Wave 5 blocked calibration complete. Full eval completion recommended next.

## Current Date

2026-07-01

## Active Lab

Tiny Release Evidence Reconciler

## Wave 1 Summary

Wave 1 created the first working evidence base for the lab:

- synthetic release packets
- scorer-only answer key
- scoring rubric
- report template
- sample readiness report
- field-operations transfer map
- reviewer cleanup for public-repo safety and eval coherence

## Wave 1 Evidence

Artifacts:

- `01 Release Intelligence Lab/Tiny Release Evidence Reconciler/Mock Data/Release Packets.md`
- `01 Release Intelligence Lab/Tiny Release Evidence Reconciler/Mock Data/Answer Key.md`
- `01 Release Intelligence Lab/Tiny Release Evidence Reconciler/Scoring Rubric.md`
- `01 Release Intelligence Lab/Tiny Release Evidence Reconciler/Report Template.md`
- `01 Release Intelligence Lab/Tiny Release Evidence Reconciler/Outputs/Sample Readiness Report.md`
- `02 Field Operations Pilot Proof Lab/Field Operations Transfer Map.md`

Repository:

- `main` pushed to public GitHub repo
- last known Wave 1 cleanup commit: `f76b03a`

## Wave 2 Summary

Wave 2 tested the first manual eval loop:

- manual eval run guide
- eval run ledger
- three generated readiness reports
- tiny local workflow spec
- scorer-side review of the first three reports

Result:

- 3 reports generated
- 3 exact label matches
- average score: 96.7
- automatic-fail count: 0
- next recommendation: build a prepare-only helper before expanding past 3 examples

## Wave 2 Evidence

Artifacts:

- `01 Release Intelligence Lab/Tiny Release Evidence Reconciler/Manual Eval Run Guide.md`
- `01 Release Intelligence Lab/Tiny Release Evidence Reconciler/Eval Run Ledger.md`
- `01 Release Intelligence Lab/Tiny Release Evidence Reconciler/Tiny Local Workflow Spec.md`
- `01 Release Intelligence Lab/Tiny Release Evidence Reconciler/Outputs/Wave 2 Manual Eval/REL-G-001 Readiness Report.md`
- `01 Release Intelligence Lab/Tiny Release Evidence Reconciler/Outputs/Wave 2 Manual Eval/REL-Y-001 Readiness Report.md`
- `01 Release Intelligence Lab/Tiny Release Evidence Reconciler/Outputs/Wave 2 Manual Eval/REL-R-002 Readiness Report.md`
- `01 Release Intelligence Lab/Tiny Release Evidence Reconciler/Outputs/Wave 2 Manual Eval/Scoring Review.md`

## Wave 3 Summary

Wave 3 added the first tiny local helper:

- dependency-free local prepare script
- prepare-helper usage guide
- prepared prompt and blank report shell for the next three examples
- guardrail run log

Result:

- command shape: `python3 scripts/release_eval_prepare.py <example-id> --write-files`
- prepared examples: `REL-G-002`, `REL-Y-002`, `REL-R-003`
- overwrite guard: passed
- missing-example guard: passed
- scorer-only leakage scan: passed
- scoring automation: not added

## Wave 3 Evidence

Artifacts:

- `scripts/release_eval_prepare.py`
- `01 Release Intelligence Lab/Tiny Release Evidence Reconciler/Prepare Helper Guide.md`
- `01 Release Intelligence Lab/Tiny Release Evidence Reconciler/Outputs/Wave 3 Prepare Helper/README.md`
- `01 Release Intelligence Lab/Tiny Release Evidence Reconciler/Outputs/Wave 3 Prepare Helper/Prepare Helper Run Log.md`
- `01 Release Intelligence Lab/Tiny Release Evidence Reconciler/Outputs/Wave 3 Prepare Helper/REL-G-002 Prompt.md`
- `01 Release Intelligence Lab/Tiny Release Evidence Reconciler/Outputs/Wave 3 Prepare Helper/REL-Y-002 Prompt.md`
- `01 Release Intelligence Lab/Tiny Release Evidence Reconciler/Outputs/Wave 3 Prepare Helper/REL-R-003 Prompt.md`

## Wave 4 Summary

Wave 4 used the prepared prompts from Wave 3 to generate and manually score the next batch:

- `REL-G-002`
- `REL-Y-002`
- `REL-R-003`

Result:

- 3 reports generated
- 3 exact label matches
- average score: 98.7
- automatic-fail count: 0
- prepare-only helper: still useful
- scoring automation: still deferred

## Wave 4 Evidence

Artifacts:

- `01 Release Intelligence Lab/Tiny Release Evidence Reconciler/Outputs/Wave 3 Prepare Helper/REL-G-002 Readiness Report.md`
- `01 Release Intelligence Lab/Tiny Release Evidence Reconciler/Outputs/Wave 3 Prepare Helper/REL-Y-002 Readiness Report.md`
- `01 Release Intelligence Lab/Tiny Release Evidence Reconciler/Outputs/Wave 3 Prepare Helper/REL-R-003 Readiness Report.md`
- `01 Release Intelligence Lab/Tiny Release Evidence Reconciler/Outputs/Wave 4 Generated Batch/Scoring Review.md`
- `01 Release Intelligence Lab/Tiny Release Evidence Reconciler/Eval Run Ledger.md`

## Wave 5 Summary

Wave 5 tested Blocked calibration:

- `REL-B-001`
- `REL-B-002`
- `REL-B-003`

Result:

- 3 reports generated
- 3 exact label matches
- average score: 100
- automatic-fail count: 0
- Blocked softened to Red, Yellow, or Green: 0
- prompt change needed: not yet

## Wave 5 Evidence

Artifacts:

- `01 Release Intelligence Lab/Tiny Release Evidence Reconciler/Outputs/Wave 5 Blocked Calibration/REL-B-001 Prompt.md`
- `01 Release Intelligence Lab/Tiny Release Evidence Reconciler/Outputs/Wave 5 Blocked Calibration/REL-B-002 Prompt.md`
- `01 Release Intelligence Lab/Tiny Release Evidence Reconciler/Outputs/Wave 5 Blocked Calibration/REL-B-003 Prompt.md`
- `01 Release Intelligence Lab/Tiny Release Evidence Reconciler/Outputs/Wave 5 Blocked Calibration/REL-B-001 Readiness Report.md`
- `01 Release Intelligence Lab/Tiny Release Evidence Reconciler/Outputs/Wave 5 Blocked Calibration/REL-B-002 Readiness Report.md`
- `01 Release Intelligence Lab/Tiny Release Evidence Reconciler/Outputs/Wave 5 Blocked Calibration/REL-B-003 Readiness Report.md`
- `01 Release Intelligence Lab/Tiny Release Evidence Reconciler/Outputs/Wave 5 Blocked Calibration/Scoring Review.md`
- `01 Release Intelligence Lab/Tiny Release Evidence Reconciler/Eval Run Ledger.md`

## Current Trust Level

Automation trust level: Level 2, Auditor.

The heartbeat test completed and was deleted after it became stale. Future heartbeats may check state and recommend the next wave. They should not launch work without approval.

## Heartbeat Test

Result:

The heartbeat successfully woke the thread, inspected the repo, reported Wave 1 artifact status, and recommended a next wave. It also exposed a useful operating rule: heartbeat instructions should be retired or updated once the wave advances, otherwise the monitor can recommend stale work.

Original goal:

Prove that a heartbeat can wake this thread, inspect project state, summarize evidence, and recommend the next wave without taking action.

Heartbeat should check:

- git status
- sync state with `origin/main`
- wave-one artifact presence
- public-repo sanitation risk
- eval-readiness risk
- whether worktree/thread cleanup is needed

Heartbeat should output:

```md
## Wave Monitor Check

Status: Green / Yellow / Red

Evidence:
- Git:
- Artifacts:
- Reviews:
- Open risks:

Recommended next wave:
- Name:
- Why:
- Suggested slices:
- Requires approval: yes
```

## Recommended Wave 6

Recommended next wave:

Complete Eval Set Or Mixed Regression Batch

Reason:

The loop has now performed well on Green, Yellow, Red, and Blocked examples. The remaining question is whether this quality holds across the full 20-example eval set without overfitting to the first nine examples.

Potential slices:

- Option A: prepare, generate, and score the remaining 11 examples to complete the 20-example eval.
- Option B: run a 4-example mixed regression batch if time is tight: `REL-G-003`, `REL-Y-003`, `REL-R-004`, `REL-B-004`.
- Update the aggregate eval results across all completed examples.
- Decide whether the loop is stable enough for a teach-back demo.
- Keep scoring manual until the full eval pattern is understood.

## Stop Condition

Do not automate scoring yet. Stop if any report uses scorer-only material, invents evidence, claims shipping authority, exposes real or sensitive details, or if a Red/Blocked case is softened to Green.
