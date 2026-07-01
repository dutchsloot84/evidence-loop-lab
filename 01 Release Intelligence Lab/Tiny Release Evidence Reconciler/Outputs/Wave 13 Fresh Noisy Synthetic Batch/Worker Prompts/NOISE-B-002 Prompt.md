# NOISE-B-002 Worker Prompt

You are a generation-only worker in a parallel evidence-loop test.

Use only this prompt. Do not inspect repo files. Do not read answer keys, expected labels, scoring rubrics, eval ledgers, prior reports, or other project files.

Return one markdown readiness report.

Rules and severity calibration are the same as Wave 13: use only the packet, do not invent evidence, assign exactly one label, preserve the human approval boundary, and do not mention scoring or answer keys. Blocked means evidence directly contradicts readiness or a required gate failed; failed rollback can make a release Blocked.

Packet:

```md
## NOISE-B-002

- Example ID: NOISE-B-002
- Release type: Permission migration release
- Readiness claim: "The permission migration is ready because access checks passed in staging."
- Evidence details:
  - Staging access checks passed for two standard roles.
  - Automated regression passed before rollback testing.
  - Security review note says the intended permission model is acceptable.
  - Rollback drill failed because one restricted role retained elevated access after restore.
  - A comment says the role is rarely used, but no risk acceptance is attached.
- Known issues:
  - Rollback left a restricted role with elevated access in staging.
- Evidence gaps:
  - No successful rollback retest.
  - No mitigation for elevated-access rollback failure.
  - No human acceptance of security rollback risk.
  - No monitoring or audit query for elevated access after migration.
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
