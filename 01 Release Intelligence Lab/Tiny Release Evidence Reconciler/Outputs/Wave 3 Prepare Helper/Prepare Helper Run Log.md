# Wave 3 Prepare Helper Run Log

## Run Date

2026-07-01

## Command Shape

```sh
python3 scripts/release_eval_prepare.py <example-id> --write-files
```

## Prepared Examples

| Example ID | Prompt | Blank Report Shell | Result |
| --- | --- | --- | --- |
| REL-G-002 | `REL-G-002 Prompt.md` | `REL-G-002 Readiness Report.md` | Prepared |
| REL-Y-002 | `REL-Y-002 Prompt.md` | `REL-Y-002 Readiness Report.md` | Prepared |
| REL-R-003 | `REL-R-003 Prompt.md` | `REL-R-003 Readiness Report.md` | Prepared |

## Guardrail Checks

| Check | Result | Evidence |
| --- | --- | --- |
| Missing example ID fails clearly | Pass | `REL-DOES-NOT-EXIST` returned an example-not-found error. |
| Existing output is not overwritten | Pass | Re-running `REL-G-002 --write-files` refused to overwrite the prompt and report shell. |
| Prompt excludes scorer-only expected outcomes | Pass | Search found no answer-key, expected-rationale, scoring-rubric, or eval-ledger language in the prepared prompt. |

## Decision

The prepare-only helper is useful enough to keep for the next eval batch.

Do not automate scoring yet. The next step is to generate reports from the three prepared prompts, then score them manually with the scorer-only answer key and rubric.
