# NEW-G-001 Worker Prompt

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
## NEW-G-001

- Example ID: NEW-G-001
- Release type: Feature flag configuration rollout
- Readiness claim: "The feature flag cleanup is ready because validation, rollback, and monitoring are covered."
- Claimed or desired decision: Evaluate whether the stated readiness claim is supported by the evidence.
- Evidence sources present:
  - Flag diff summary
  - Automated validation result
  - Manual smoke test
  - Rollback note
  - Monitoring note
  - Owner approval note
- Evidence details:
  - Flag diff summary shows two retired flags removed and one default value changed only for a dormant path.
  - Automated validation passed for enabled, disabled, and default-path behavior.
  - Manual smoke test covered sign-in, workspace load, and the settings panel that reads the flag.
  - Rollback note describes restoring the previous flag snapshot and rerunning validation.
  - Monitoring note names flag-evaluation errors and settings-panel error rate for the first two hours.
  - Owner approval note confirms the cleanup scope is acceptable.
- Known issues:
  - One internal runbook screenshot still shows the old flag name.
- Evidence gaps:
  - No separate product narrative is attached.
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
