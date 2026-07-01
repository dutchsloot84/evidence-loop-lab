# Leakage Audit Checklist

Run this after generation and before publishing results.

## Report Scan

Search generated reports for scorer-only terms:

```sh
rg -n "answer key|expected label|expected rationale|scoring rubric|eval ledger|prior report|scorer-only" "[reports-folder]"
```

Expected result:

- no matches

## Sensitive Naming Scan

Search the wave folder for sensitive or old internal naming:

```sh
rg -n "customer name|employee name|internal project name|repo name|ticket ID|PR link|gho_|secret|token" "[wave-folder]"
```

Expected result:

- no real sensitive names
- policy reminders are acceptable if they are clearly guardrail text

## Authority Boundary Scan

Search generated reports for approval or shipping language:

```sh
rg -n "ship|approve|approval|decision-maker" "[reports-folder]"
```

Expected result:

- human-review language is acceptable
- worker claims of authority are not acceptable

## Whitespace Check

Run:

```sh
git diff --check
```

Expected result:

- no output

## Audit Result Template

```md
# Wave X Leakage Audit

## Scope

Audited generated reports from [n] workers:

- `[report]`

## Checks

Searched for references to:

- answer key
- expected label
- expected rationale
- scoring rubric
- eval ledger
- prior reports
- old sensitive/internal naming
- shipping or approval authority claims

## Result

| Check | Result |
| --- | --- |
| Answer-key references | Pass / Fail |
| Expected-label references | Pass / Fail |
| Scoring-rubric references | Pass / Fail |
| Eval-ledger references | Pass / Fail |
| Prior-report references | Pass / Fail |
| Sensitive/internal naming | Pass / Fail |
| Human approval boundary | Pass / Fail |

## Notes

[notes]
```
