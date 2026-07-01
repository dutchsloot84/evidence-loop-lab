# Release Evidence Playbook

## Purpose

Use this playbook to turn a release-readiness claim into an evidence-backed readiness report.

This playbook is for synthetic, sanitized, or training examples. It does not authorize real releases.

## When To Use

Use this loop when someone claims:

- a release is ready
- only minor issues remain
- QA is complete
- approval means readiness
- operations are covered
- rollback is documented

The loop is most useful when the claim sounds plausible but the evidence may be incomplete.

## Inputs

Model-visible:

- one release packet
- report template
- optional loop framing

Scorer-only:

- answer key
- scoring rubric
- eval ledger

Do not include scorer-only material when generating a report.

## Output

One markdown readiness report with:

- input claim
- evidence summary
- readiness label
- rationale
- supported claims
- unsupported or weak claims
- evidence gaps
- risks
- next evidence
- human review note

## Readiness Labels

| Label | Use When |
| --- | --- |
| Green | Evidence supports the readiness claim and gaps are minor. |
| Yellow | Evidence supports partial readiness, but human review is needed. |
| Red | The readiness claim is materially unsupported. |
| Blocked | Evidence directly contradicts readiness, or a required gate is missing. |

## Evidence Checks

Ask:

1. What does the claim say?
2. What evidence directly supports it?
3. What evidence is missing?
4. Does any evidence contradict the claim?
5. Are approvals being treated as validation?
6. Are deployment notes being treated as rollback or monitoring proof?
7. Is a known issue minor, material, or blocking?
8. What concrete evidence would move the decision forward?

## Common Failure Modes

| Failure Mode | Safer Check |
| --- | --- |
| Merged work treated as release readiness | Ask for validation, review, rollback, and monitoring evidence. |
| Approval treated as validation | Ask what was validated and by whom. |
| Backup treated as rollback | Ask for restore verification. |
| Deployment note treated as operational coverage | Ask for rollback, monitoring, post-deploy smoke, and owner evidence. |
| Minor follow-up treated as blocker | Check whether core readiness evidence is already strong. |
| Critical failure softened to Red | Use Blocked when core validation, rollback, required approval, or scope evidence directly contradicts readiness. |

## Prepare Helper

Use the helper when preparing repeated examples:

```sh
python3 scripts/release_eval_prepare.py REL-G-004 --write-files
```

The helper should:

- select the packet by example ID
- create a model-visible prompt
- create a predictable blank report shell
- refuse to overwrite existing files

The helper should not:

- read the answer key
- score the report
- assign the final human decision

## Manual Scoring

Score after report generation.

Use:

- `Mock Data/Answer Key.md`
- `Scoring Rubric.md`
- `Eval Run Ledger.md`

Record:

- expected label
- actual label
- score
- key misses
- failure mode
- next fix

## Stop Conditions

Stop if:

- scorer-only material appears in generation context
- report invents evidence
- report claims authority to ship or approve
- sensitive or real work details appear
- Red or Blocked evidence is softened to Green

## Current Evidence

The first 20-example synthetic eval passed:

| Metric | Result |
| --- | ---: |
| Reports generated | 20 |
| Exact label matches | 20 |
| Average score | 99.3 |
| Automatic-fail count | 0 |

This proves the loop is usable for synthetic training examples. It does not yet prove real-world release readiness.

## Next Use

Before adding scoring automation, use this playbook to:

- teach the loop to another person
- run a noisier synthetic eval set
- test parallel report generation without answer-key leakage
- transfer the pattern to field-operations pilot proof

## Parallel Eval Pack

Use `Parallel Eval Pack/` when running supervised parallel synthetic batches.

The pack includes:

- stable generation-only worker prompt
- fresh-batch packet template
- scorer comparison template
- leakage audit checklist
- eligibility and stop conditions
- worker run log template

Use the pack only for synthetic or sanitized examples. Keep scorer-only labels separate from worker prompts, score manually after generation, and run leakage checks before publishing results.
