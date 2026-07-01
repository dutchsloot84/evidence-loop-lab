# PAR-Y-001 Worker Prompt

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
## PAR-Y-001

- Example ID: PAR-Y-001
- Release type: Third-party sync update
- Readiness claim: "The sync update is ready; remaining issues are only cosmetic."
- Claimed or desired decision: Evaluate whether the stated readiness claim is supported by the evidence.
- Evidence sources present:
  - Integration smoke test
  - Sandbox credential note
  - Code review approval
  - Manual UI review
- Evidence details:
  - Integration smoke test passed for account connection and first sync in sandbox.
  - Sandbox credential note confirms test credentials worked during validation.
  - Code review approval says retry behavior was reviewed.
  - Manual UI review found alignment and label spacing issues in the sync settings panel.
  - A low-frequency delayed-sync warning appeared twice in sandbox but was not reproduced under a larger batch.
- Known issues:
  - Delayed-sync warning may be functional or may be sandbox-only; impact is not proven.
- Evidence gaps:
  - No production-like batch sync test.
  - No monitoring note for delayed syncs.
  - No user-impact note for the delayed-sync warning.
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
