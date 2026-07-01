# Prepare Helper Guide

## Purpose

Use the prepare helper to reduce copy/paste and file-naming mistakes before expanding the manual eval run.

The helper does not score reports. It does not assign readiness labels. It does not read scorer-only files.

## Command

From the repo root:

```sh
python3 scripts/release_eval_prepare.py REL-G-002 --write-files
```

Without `--write-files`, the helper prints the model-visible prompt to stdout:

```sh
python3 scripts/release_eval_prepare.py REL-G-002
```

## Inputs

The helper reads:

- `Mock Data/Release Packets.md`
- `Report Template.md`

The helper does not read:

- `Mock Data/Answer Key.md`
- `Scoring Rubric.md`
- `Eval Run Ledger.md`

## Outputs

Default output directory:

```text
01 Release Intelligence Lab/Tiny Release Evidence Reconciler/Outputs/Wave 3 Prepare Helper/
```

For each example, the helper prepares:

- `<example-id> Prompt.md`
- `<example-id> Readiness Report.md`

The prompt file is model-visible. The blank report shell is where the generated report can be pasted.

## Stop Conditions

Stop and do not continue the run if:

- the helper cannot find the example ID
- an output file already exists
- the prompt contains scorer-only language or expected outcomes
- the packet appears to contain real or sensitive details
- the generated report claims authority to ship or approve

## Recommended Wave 3 Run

Use the helper for the next 3 examples:

- `REL-G-002`
- `REL-Y-002`
- `REL-R-003`

Generate reports from those prompts manually, then score them with the scorer-only answer key and rubric.

## Success Criteria

Wave 3 succeeds if:

- prompts are created with only model-visible content
- output paths are predictable
- existing report files are not overwritten
- scoring remains manual
- expanding beyond 3 examples feels less error-prone
