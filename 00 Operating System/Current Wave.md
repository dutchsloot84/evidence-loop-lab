# Current Wave

## Status

Status: Wave 7 full 20-example eval complete. Teach-back demo recommended next.

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

## Wave 6 Summary

Wave 6 ran a mixed regression batch:

- `REL-G-003`
- `REL-Y-003`
- `REL-R-004`
- `REL-B-004`

Result:

- 4 reports generated
- 4 exact label matches
- average score: 100
- automatic-fail count: 0
- Red or Blocked softened to Green: 0
- prompt change needed: no

## Wave 6 Evidence

Artifacts:

- `01 Release Intelligence Lab/Tiny Release Evidence Reconciler/Outputs/Wave 6 Mixed Regression/REL-G-003 Prompt.md`
- `01 Release Intelligence Lab/Tiny Release Evidence Reconciler/Outputs/Wave 6 Mixed Regression/REL-Y-003 Prompt.md`
- `01 Release Intelligence Lab/Tiny Release Evidence Reconciler/Outputs/Wave 6 Mixed Regression/REL-R-004 Prompt.md`
- `01 Release Intelligence Lab/Tiny Release Evidence Reconciler/Outputs/Wave 6 Mixed Regression/REL-B-004 Prompt.md`
- `01 Release Intelligence Lab/Tiny Release Evidence Reconciler/Outputs/Wave 6 Mixed Regression/REL-G-003 Readiness Report.md`
- `01 Release Intelligence Lab/Tiny Release Evidence Reconciler/Outputs/Wave 6 Mixed Regression/REL-Y-003 Readiness Report.md`
- `01 Release Intelligence Lab/Tiny Release Evidence Reconciler/Outputs/Wave 6 Mixed Regression/REL-R-004 Readiness Report.md`
- `01 Release Intelligence Lab/Tiny Release Evidence Reconciler/Outputs/Wave 6 Mixed Regression/REL-B-004 Readiness Report.md`
- `01 Release Intelligence Lab/Tiny Release Evidence Reconciler/Outputs/Wave 6 Mixed Regression/Scoring Review.md`
- `01 Release Intelligence Lab/Tiny Release Evidence Reconciler/Eval Run Ledger.md`

## Wave 7 Summary

Wave 7 completed the remaining eval examples:

- `REL-G-004`
- `REL-G-005`
- `REL-Y-004`
- `REL-Y-005`
- `REL-R-001`
- `REL-R-005`
- `REL-B-005`

Result:

- 7 reports generated
- 7 exact label matches
- final batch average score: 100
- full eval average score: 99.3
- full eval exact label matches: 20 of 20
- automatic-fail count: 0
- full eval decision: Pass

## Wave 7 Evidence

Artifacts:

- `01 Release Intelligence Lab/Tiny Release Evidence Reconciler/Outputs/Wave 7 Full Eval Completion/REL-G-004 Prompt.md`
- `01 Release Intelligence Lab/Tiny Release Evidence Reconciler/Outputs/Wave 7 Full Eval Completion/REL-G-005 Prompt.md`
- `01 Release Intelligence Lab/Tiny Release Evidence Reconciler/Outputs/Wave 7 Full Eval Completion/REL-Y-004 Prompt.md`
- `01 Release Intelligence Lab/Tiny Release Evidence Reconciler/Outputs/Wave 7 Full Eval Completion/REL-Y-005 Prompt.md`
- `01 Release Intelligence Lab/Tiny Release Evidence Reconciler/Outputs/Wave 7 Full Eval Completion/REL-R-001 Prompt.md`
- `01 Release Intelligence Lab/Tiny Release Evidence Reconciler/Outputs/Wave 7 Full Eval Completion/REL-R-005 Prompt.md`
- `01 Release Intelligence Lab/Tiny Release Evidence Reconciler/Outputs/Wave 7 Full Eval Completion/REL-B-005 Prompt.md`
- `01 Release Intelligence Lab/Tiny Release Evidence Reconciler/Outputs/Wave 7 Full Eval Completion/Scoring Review.md`
- `01 Release Intelligence Lab/Tiny Release Evidence Reconciler/Outputs/Full 20 Example Eval Aggregate.md`
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

## Recommended Wave 8

Recommended next wave:

Teach-Back Demo And Playbook

Reason:

The full 20-example eval now passes. The highest-leverage next step is to turn the work into a reusable explanation and playbook before adding more automation.

Potential slices:

- write a 5-minute teach-back script
- create a one-page playbook for turning readiness claims into evidence-backed reports
- document when to use the prepare helper and when to keep scoring manual
- name the next proof: noisier eval set, parallel generation experiment, or field-operations transfer
- keep scoring automation deferred until after the teach-back review

## Stop Condition

Do not automate scoring yet. Stop if the teach-back blurs the human approval boundary, implies real work validation, or omits the synthetic-data limitation.
