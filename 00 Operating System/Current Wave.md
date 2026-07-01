# Current Wave

## Status

Status: Wave 3 prepare-only helper complete. Next report-generation batch prepared.

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

## Recommended Wave 4

Recommended next wave:

Generate And Score Prepared Batch

Reason:

Wave 3 prepared the next three examples with predictable prompts and blank report shells. The next proof should generate the reports, score them manually, and decide whether the helper remains sufficient before expanding toward the full 20-example eval set.

Potential slices:

- generate reports from the three prepared prompts
- score the reports against the scorer-only answer key and rubric
- update the eval ledger with scores and misses
- compare Wave 2 and Wave 4 miss patterns
- decide whether to prepare the remaining 14 examples or improve the prompt first

## Stop Condition

Do not automate scoring yet. Stop if generated reports use scorer-only material, overwrite prepared shells without review, invent evidence, claim shipping authority, or expose real or sensitive details.
