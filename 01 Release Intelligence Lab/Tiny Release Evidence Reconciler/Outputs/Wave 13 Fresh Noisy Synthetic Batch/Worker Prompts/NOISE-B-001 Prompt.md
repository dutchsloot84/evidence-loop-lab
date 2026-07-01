# NOISE-B-001 Worker Prompt

You are a generation-only worker in a parallel evidence-loop test.

Use only this prompt. Do not inspect repo files. Do not read answer keys, expected labels, scoring rubrics, eval ledgers, prior reports, or other project files.

Return one markdown readiness report.

Rules and severity calibration are the same as Wave 13: use only the packet, do not invent evidence, assign exactly one label, preserve the human approval boundary, and do not mention scoring or answer keys. Blocked means evidence directly contradicts readiness or a required gate failed; failed reversal can make a release Blocked.

Packet:

```md
## NOISE-B-001

- Example ID: NOISE-B-001
- Release type: Data backfill release
- Readiness claim: "The data backfill is ready after staging validation."
- Evidence details:
  - Staging backfill completed and row-count checks matched expected totals.
  - Code review approval is complete.
  - Reversal drill failed because restored records duplicated a subset of rows.
  - A note says duplicate rows were "probably test fixture related" but no retest is attached.
  - A dashboard screenshot shows normal staging load after the failed reversal.
- Known issues:
  - Reversal drill failed and has no verified fix.
- Evidence gaps:
  - No successful reversal retest.
  - No mitigation if reversal is needed.
  - No human acceptance of reversal risk.
  - No monitoring thresholds for duplicate records.
```

Required report shape:

- Eval Example
- Input Claim
- Summary
- Evidence Summary
- Readiness Label
- Rationale
- Supported Claims
- Unsupported or Weak Claims
- Evidence Gaps
- Risks
- Next Evidence
- Human Review Note
