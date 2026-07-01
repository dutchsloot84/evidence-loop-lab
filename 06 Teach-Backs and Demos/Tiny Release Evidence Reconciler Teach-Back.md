# Tiny Release Evidence Reconciler Teach-Back

## Purpose

Five-minute teach-back for explaining the first completed Evidence Loop Lab artifact.

Audience: someone who understands release work, AI-assisted workflows, or engineering process, but has not followed this lab.

Supporting artifacts:

- `01 Release Intelligence Lab/Tiny Release Evidence Reconciler/Outputs/Full 20 Example Eval Aggregate.md`
- `01 Release Intelligence Lab/Tiny Release Evidence Reconciler/Release Evidence Playbook.md`

## Opening

The point of this lab was simple: turn a readiness claim into an evidence-backed report.

The claim might sound like:

> "This release is ready."

The loop asks a narrower question:

> "What observable evidence supports that claim, what evidence is missing, and what should a human review next?"

This is not an autonomous ship decision. It is a structured evidence check.

## The Loop

The Tiny Release Evidence Reconciler uses four pieces:

1. A synthetic release packet.
2. A model-visible report template.
3. A scorer-only answer key.
4. A manual scoring rubric.

The important boundary is that the report generator sees only the packet and template. It does not see the answer key. Scoring happens afterward.

The loop turns:

```text
claim -> evidence -> unsupported claims -> gaps -> risk label -> next evidence
```

into a markdown readiness report.

## The Labels

The reports use four labels:

- Green: evidence supports readiness.
- Yellow: partial readiness; human review needed.
- Red: readiness claim is materially unsupported.
- Blocked: evidence directly contradicts readiness or a required gate is missing.

The hardest distinction is Red vs Blocked.

Red means the packet does not prove readiness.

Blocked means the packet shows a direct contradiction, failed core validation, failed rollback, missing required approval, or unresolved critical issue.

## What We Built

First, we created synthetic release packets and a scorer-only answer key.

Then we added a tiny prepare helper:

```sh
python3 scripts/release_eval_prepare.py REL-G-004 --write-files
```

That helper does not score. It only selects one packet, creates a model-visible prompt, and creates a predictable report shell.

Scoring stayed manual.

That was deliberate. The learning target was evidence judgment, not speed.

## Eval Result

The full eval used 20 synthetic examples:

- 5 Green
- 5 Yellow
- 5 Red
- 5 Blocked

Result:

| Metric | Result |
| --- | ---: |
| Reports generated | 20 |
| Exact label matches | 20 |
| Average score | 99.3 |
| Red or Blocked scored Green | 0 |
| Blocked examples labeled Blocked | 5 |
| Automatic-fail count | 0 |

The eval passed the rubric thresholds.

## What The Eval Proved

The loop handled the key traps:

- It did not confuse merged work with release readiness.
- It did not treat approval as validation.
- It did not treat a backup as a complete rollback plan.
- It did not ignore failed rollback evidence.
- It did not soften critical Blocked cases into ordinary Red or Yellow risk.
- It preserved the human approval boundary.

## What It Did Not Prove

This is still a learning lab result.

The data is synthetic and intentionally structured. Scoring was manual and may be generous. The helper reduces prompt and file-path mistakes, but it does not prove automated scoring is safe.

So the next proof should not be "automate everything."

The next proof should be either:

- a noisier eval set, or
- a parallel-generation experiment with strict answer-key separation, or
- a transfer map into field-operations pilot proof.

## Closing

The reusable lesson is:

Do not ask AI to decide whether a claim is true.

Ask it to produce a traceable evidence report, preserve the human decision boundary, and then score the result against expected behavior.

That is the Evidence Loop Lab pattern:

```text
claim -> checked evidence -> scored output -> failure modes -> next loop
```
