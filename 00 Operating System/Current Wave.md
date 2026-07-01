# Current Wave

## Status

Status: Wave 2 manual eval run complete. Prepare-only helper recommended.

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

## Recommended Wave 3

Recommended next wave:

Prepare-Only Local Helper

Reason:

Wave 2 proved that the manual loop can generate and score the first three reports. The next bottleneck is repeatability, not judgment. A tiny helper should reduce packet-selection, prompt-shaping, and output-path mistakes before expanding to the 20-example eval set.

Potential slices:

- define the helper command contract
- create a tiny local prepare helper
- add a dry-run example for one packet
- verify the helper never reads `Mock Data/Answer Key.md`
- expand the manual eval run to the next 3-5 packets

## Stop Condition

Do not automate scoring yet. Stop if scorer-only material appears in model-visible prompts, if the helper overwrites a report, or if any packet contains real or sensitive details.
