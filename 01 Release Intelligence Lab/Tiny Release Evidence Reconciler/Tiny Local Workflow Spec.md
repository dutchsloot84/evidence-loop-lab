# Tiny Local Workflow Spec

## Purpose

Define the smallest local workflow that could support the Tiny Release Evidence Reconciler after the manual eval loop has been run and scored.

This is not an implementation plan for a product. It is a restraint document: keep the workflow small enough that it improves consistency without hiding the evidence judgment the lab is trying to learn.

## Current State

Wave 2 starts manual-first:

- select one synthetic release packet
- generate one readiness report from model-visible evidence
- score the report against the scorer-only answer key
- record misses in the eval ledger
- decide whether a tiny helper script is justified

The workflow should remain markdown-native until manual scoring shows repeated mechanical errors.

## Inputs

Model-visible inputs:

- `Mock Data/Release Packets.md`
- `Report Template.md`
- `Loop Spec.md`
- selected eval example ID

Scorer-only inputs:

- `Mock Data/Answer Key.md`
- `Scoring Rubric.md`
- `Eval Run Ledger.md`

The generated readiness report must not read or receive `Mock Data/Answer Key.md`. The answer key is only for scoring after generation.

## Outputs

Primary output:

- one markdown readiness report per eval example

Scorer output:

- one ledger row per scored report
- short miss notes
- failure-mode tag
- next fix

Optional summary output:

- aggregate score notes after a batch is complete
- tiny script decision note

## Future Command Shape

Only add a command after the manual run proves it would reduce errors. If justified, the command should be shaped around file selection and repeatable output paths, not automatic judgment.

Possible future command:

```sh
release-eval prepare REL-G-001
```

Expected behavior:

- find the selected packet in `Mock Data/Release Packets.md`
- create or identify the report output path
- print a generation prompt that includes only model-visible context
- prefill a blank ledger row for later scoring

Possible later command:

```sh
release-eval score REL-G-001
```

Expected behavior:

- open the generated report
- open scorer-only materials
- present scoring headings in a consistent order
- require a human scorer to enter scores and miss notes

The scorer command may use `Mock Data/Answer Key.md`. The prepare command may not.

## Files Read And Written

Prepare step may read:

- `Mock Data/Release Packets.md`
- `Report Template.md`
- `Loop Spec.md`

Prepare step may write:

- `Outputs/Wave 2 Manual Eval/<example-id> Readiness Report.md`, if creating a blank report shell
- temporary prompt text, if needed

Prepare step must not read:

- `Mock Data/Answer Key.md`
- `Eval Run Ledger.md`, except to confirm the example is not already running

Score step may read:

- generated readiness report
- `Mock Data/Answer Key.md`
- `Scoring Rubric.md`
- `Eval Run Ledger.md`

Score step may write:

- `Eval Run Ledger.md`
- optional scoring review note

## What Remains Manual

Keep these human-controlled:

- readiness label judgment
- evidence sufficiency judgment
- whether a gap matters enough to change the risk label
- whether a known issue is acceptable
- final score assignment
- decision to expand the eval set
- decision to move from manual run to script-assisted run

The workflow may reduce copy/paste mistakes. It should not remove the need to reason about evidence.

## Stop Conditions

Stop the workflow if:

- the selected example ID is not found
- the packet appears to contain real or sensitive details
- the generated report cites evidence not present in the packet
- the generated report claims authority to ship or approve
- the report output path already exists and would be overwritten
- scorer-only material appears in a model-visible prompt

## Script Justification Rule

Write a tiny local script only if at least two of these are true after the first 3-report run:

- packet selection caused copy/paste mistakes
- report filenames or headings were inconsistent
- ledger rows were incomplete or hard to compare
- scoring notes repeatedly needed the same structure
- the next batch will expand beyond 3 examples

Do not write a script if the main uncertainty is still conceptual: label rules, scoring criteria, missing-evidence judgment, or human approval boundaries.

## First Useful Version

The first useful version should do only three things:

1. select a packet by example ID
2. print a clean generation prompt with model-visible context only
3. create a predictable output path or blank report shell

Anything beyond that waits until manual scoring proves where the workflow is losing consistency.
