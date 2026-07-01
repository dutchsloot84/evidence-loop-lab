# Parallel Eval Pack

## Purpose

Use this pack to run small supervised synthetic release-readiness eval batches in parallel without rebuilding the harness each time.

The pack exists because Waves 9-13 showed that parallel generation can work when the boundary is explicit:

- workers see only model-visible packets
- scorer-only labels stay out of generation context
- main thread scores after generation
- leakage and sanitation checks are required
- human approval boundaries stay explicit

## Use Only When

- examples are synthetic or sanitized
- the batch has clear expected labels
- answer-key separation can be maintained
- reports will be manually scored after generation
- generated outputs will not make real release decisions

## Pack Files

- `Stable Worker Prompt v2.md`
- `Fresh Batch Packet Template.md`
- `Scorer Comparison Template.md`
- `Leakage Audit Checklist.md`
- `Eligibility and Stop Conditions.md`
- `Run Log Template.md`

## Minimal Run Shape

1. Create model-visible packets.
2. Create scorer-only answer key separately.
3. Launch generation-only workers with one packet each.
4. Save worker reports verbatim.
5. Score manually after generation.
6. Run leakage and sanitation checks.
7. Record ROI and next recommendation.

## Current Proven Scope

Proven for:

- small synthetic batches
- four-label readiness classification
- noisy but controlled synthetic evidence
- generation-only parallel workers

Not proven for:

- real or sensitive data
- unattended execution
- automated scoring
- release approval
- production governance decisions
