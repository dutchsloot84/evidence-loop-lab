# PAR-B-001 Worker Prompt

You are a generation-only worker in a parallel evidence-loop test.

Use only this prompt. Do not inspect repo files. Do not read answer keys, scoring rubrics, eval ledgers, prior reports, or other project files.

Return one markdown readiness report.

Rules:

- Use only the packet evidence provided here.
- Do not invent evidence.
- Assign exactly one readiness label: Green, Yellow, Red, or Blocked.
- Preserve the human approval boundary. You may recommend a label, but you may not claim authority to ship or approve.
- Keep all details synthetic and sanitized.

Severity calibration:

- Green means the evidence supports the readiness claim and remaining gaps are minor.
- Yellow means evidence supports partial readiness, but human review is needed before treating the claim as ready.
- Yellow can still apply when meaningful functional evidence exists but one unresolved warning needs impact analysis.
- Red means the central readiness claim is materially unsupported.
- Red can apply when required operational controls are missing for an operational-readiness claim.
- Blocked means evidence directly contradicts readiness or a required gate failed.
- Failed rollback can make a release Blocked.
- Positive implementation evidence does not erase operational contradictions.
- A deployment command does not prove rollback, monitoring, post-deploy validation, or owner coverage.
- Do not escalate every unresolved warning to Red when the packet contains meaningful supporting validation and the risk is bounded but unproven.

Packet:

```md
## PAR-B-001

- Example ID: PAR-B-001
- Release type: Migration release
- Readiness claim: "The migration is ready after successful staging validation."
- Claimed or desired decision: Evaluate whether the stated readiness claim is supported by the evidence.
- Evidence sources present:
  - Staging validation note
  - Automated regression result
  - Rollback drill result
  - Code review approval
- Evidence details:
  - Staging validation passed for read and write operations after migration.
  - Automated regression passed before the rollback drill.
  - Rollback drill failed because the restored environment did not pass health checks.
  - Code review approval is complete.
- Known issues:
  - Rollback failed in staging and has no verified fix.
- Evidence gaps:
  - No successful rollback retest.
  - No operational mitigation if rollback is needed.
  - No human acceptance of rollback risk.
  - Monitoring thresholds are not defined.
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

Final reminder:

Do not mention scoring, answer keys, expected labels, rubrics, or prior reports.
