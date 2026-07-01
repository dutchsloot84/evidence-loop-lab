# NOISE-G-001 Worker Prompt

You are a generation-only worker in a parallel evidence-loop test.

Use only this prompt. Do not inspect repo files. Do not read answer keys, expected labels, scoring rubrics, eval ledgers, prior reports, or other project files.

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
## NOISE-G-001

- Example ID: NOISE-G-001
- Release type: Static copy cleanup
- Readiness claim: "The copy cleanup is ready because the changed strings are validated and rollback is covered."
- Evidence details:
  - Copy diff summary shows wording changes to help text only; no business logic, routing, or permission strings changed.
  - Automated snapshots passed for desktop and mobile views.
  - Manual smoke test covered sign-in, help drawer open, and account settings load.
  - Rollback note describes restoring the previous string bundle.
  - Monitoring note names client-render errors and help drawer error rate for the first day.
  - Content owner approval confirms wording scope.
  - A stale screenshot in a training draft still shows old wording.
- Known issues:
  - Training draft screenshot is stale.
- Evidence gaps:
  - No separate marketing review is attached.
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
