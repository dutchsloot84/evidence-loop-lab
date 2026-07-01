# Automation Trust Ladder

## Purpose

This note defines how Evidence Loop Lab earns trust for heartbeat-driven and agent-assisted work.

The goal is not to automate everything. The goal is to increase autonomy only after the loop produces evidence that it can act safely.

## Trust Rule

Automation may gain scope only when the previous level works repeatedly without creating cleanup debt, public-repo risk, or unclear human approval boundaries.

## Level 1: Reminder

Automation may:

- wake the thread on a schedule
- remind me what wave is active
- summarize the next planned review

Automation may not:

- edit files
- create branches
- launch sub-agents
- push changes

Use when:

- testing heartbeat reliability
- keeping a project visible without adding execution risk

## Level 2: Auditor

Automation may:

- check `git status`
- confirm whether `main` is synced with `origin/main`
- inspect known artifact paths
- report missing or stale artifacts
- recommend the next wave

Automation may not:

- edit files
- launch new work
- merge branches
- push changes

Use when:

- a wave has completed
- the next decision should be evidence-backed
- I want a status check before launching more work

## Level 3: Wave Planner

Automation may:

- propose 2-4 parallel slices
- define branch names
- define owned files
- draft worker prompts
- identify reviewer roles

Automation may not:

- launch threads without approval
- edit files
- push changes

Use when:

- the next wave is known, but needs decomposition
- parallel work needs clean ownership boundaries

## Level 4: Gated Launcher

Automation may:

- launch pre-approved slice types
- use separate worktree threads
- assign disjoint file ownership
- request read-only reviewer sub-agents after integration

Automation may not:

- use sensitive data
- change scope
- push public changes without approval
- launch product or infrastructure work without a specific plan

Use when:

- prior wave audits have been clean
- slice types are routine
- file ownership is unambiguous

## Level 5: Lab Operator

Automation may:

- launch a wave
- monitor worker completion
- integrate branches
- run reviewers
- prepare commits
- prepare a push or PR summary

Automation still requires human approval for:

- public push
- sensitive data
- new scope
- destructive actions
- real product, customer, or operational decisions

Use when:

- lower levels have worked repeatedly
- the work is low-risk and markdown/eval focused
- the user wants supervised autonomy

## Current Trust Level

Current level: Level 2, Auditor.

Reason:

Wave 1 proved that parallel worktree slices and reviewer sub-agents can produce useful artifacts, but the system still needs human approval before launching or pushing new work.

## Wave 9 Parallel Generation Note

Wave 9 tested four generation-only workers in parallel with strict answer-key separation.

Result:

- answer-key leakage: 0
- authority-boundary failures: 0
- exact label matches: 2 of 4
- Red or Blocked softened to Green: 0
- decision: review, not promotion

The coordination boundary worked, but severity calibration did not. Parallel generation is not yet approved for broader unattended eval expansion.

Allowed next use:

- synthetic or sanitized examples only
- generation-only workers only
- main-thread scoring required
- leakage audit required
- stronger severity-calibrated worker prompt required

Trust level remains Level 2, Auditor.

## Wave 10 Severity-Calibrated Rerun Note

Wave 10 reran two Wave 9 severity misses and one Yellow control with a stronger worker prompt.

Result:

- answer-key leakage: 0
- authority-boundary failures: 0
- exact label matches: 2 of 3
- Wave 9 severity misses corrected: 2 of 2
- Yellow control preserved: 0 of 1
- decision: improved, but not promotion-quality

The severity calibration fixed under-severity for Red and Blocked examples, but overcorrected the Yellow control to Red. Parallel generation remains useful only for small supervised synthetic batches with main-thread scoring.

Allowed next use:

- synthetic or sanitized examples only
- generation-only workers only
- main-thread scoring required
- leakage audit required
- middle-band Yellow calibration required

Trust level remains Level 2, Auditor.

## Wave 11 Middle-Band Yellow Calibration Note

Wave 11 reran the same three-example shape with a v2 worker prompt that clarified the Yellow middle band.

Result:

- answer-key leakage: 0
- authority-boundary failures: 0
- exact label matches: 3 of 3
- Yellow control preserved: 1 of 1
- Red operational-control case preserved: 1 of 1
- Blocked failed-gate case preserved: 1 of 1
- decision: pass for this small calibration slice

The v2 prompt preserved Yellow without softening Red or Blocked on the known calibration examples. This supports continued small supervised synthetic batches, but does not yet prove generalization to unseen examples.

Allowed next use:

- fresh synthetic or sanitized examples only
- generation-only workers only
- main-thread scoring required
- leakage audit required
- answer-key separation required

Trust level remains Level 2, Auditor.

## Wave 12 Fresh Unseen Parallel Batch Note

Wave 12 tested the v2 worker prompt on four fresh unseen synthetic examples: one Green, one Yellow, one Red, and one Blocked.

Result:

- answer-key leakage: 0
- authority-boundary failures: 0
- exact label matches: 4 of 4
- Green control preserved: 1 of 1
- Yellow control preserved: 1 of 1
- Red operational-control case preserved: 1 of 1
- Blocked failed-gate case preserved: 1 of 1
- decision: pass

The v2 prompt generalized to a fresh synthetic batch. This supports small supervised synthetic eval expansion with generation-only workers, answer-key separation, and main-thread scoring.

Allowed next use:

- fresh synthetic or sanitized examples only
- small supervised batches only
- generation-only workers only
- main-thread scoring required
- leakage audit required
- answer-key separation required

Trust level remains Level 2, Auditor. Consider a separate trust-ladder promotion review only after deciding whether heartbeat automation, not just user-approved parallel generation, has earned more autonomy.

## Promotion Rule

Promote one level only after two clean runs at the current level.

A clean run means:

- no unexpected file edits
- no sensitive data exposure
- no unclear branch ownership
- no unreviewed public push
- clear next recommendation
- useful evidence recorded

## Demotion Rule

Move down one level if automation:

- launches work too early
- creates ambiguous state
- misses a sanitation issue
- makes a recommendation without evidence
- requires more cleanup than it saves
