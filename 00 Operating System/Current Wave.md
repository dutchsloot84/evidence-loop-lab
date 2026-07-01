# Current Wave

## Status

Status: Wave 1 complete. Heartbeat monitor test planned.

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
- last known cleanup commit: `77f992e`

## Current Trust Level

Automation trust level: Level 2, Auditor.

The heartbeat may check state and recommend the next wave. It should not launch work without approval.

## Heartbeat Test

Goal:

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

## Recommended Wave 2

Recommended next wave:

Manual Eval Runner / First Tiny Local Workflow

Reason:

Wave 1 produced model-visible inputs, a scorer-only answer key, a rubric, and a report template. The next proof should test whether the loop can generate and score readiness reports from a few packets.

Potential slices:

- create a manual eval run guide
- generate readiness reports for 3-5 packets
- score reports against `Answer Key.md`
- record failure modes
- decide what the tiny local script should do later

## Stop Condition

Do not launch Wave 2 until the heartbeat confirms Wave 1 is clean and the user approves the next wave.

