# PAR-R-001 Worker Prompt

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
- Red means the readiness claim is materially unsupported.
- Blocked means evidence directly contradicts readiness or a required gate is missing.
- Missing operational controls can make an operational-readiness claim Red.
- Failed rollback can make a release Blocked.
- Positive implementation evidence does not erase operational contradictions.
- A deployment command does not prove rollback, monitoring, post-deploy validation, or owner coverage.

Packet:

```md
## PAR-R-001

- Example ID: PAR-R-001
- Release type: Deployment readiness update
- Readiness claim: "The deployment is ready and operational coverage is complete."
- Claimed or desired decision: Evaluate whether the stated readiness claim is supported by the evidence.
- Evidence sources present:
  - Deployment note
  - Build verification
  - Code review approval
  - Release window note
- Evidence details:
  - Deployment note lists the deploy command and planned release window.
  - Build verification passed on the release candidate.
  - Code review approval is complete.
  - Release window note identifies when the deployment should occur.
- Known issues:
  - None documented.
- Evidence gaps:
  - Rollback plan is missing.
  - Monitoring plan is missing.
  - No post-deploy smoke test is defined.
  - No release owner or on-call note is present.
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
