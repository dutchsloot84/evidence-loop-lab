# NOISE-R-002 Worker Prompt

You are a generation-only worker in a parallel evidence-loop test.

Use only this prompt. Do not inspect repo files. Do not read answer keys, expected labels, scoring rubrics, eval ledgers, prior reports, or other project files.

Return one markdown readiness report.

Rules and severity calibration are the same as Wave 13: use only the packet, do not invent evidence, assign exactly one label, preserve the human approval boundary, and do not mention scoring or answer keys. Red means the central readiness claim is materially unsupported even if partial implementation evidence exists.

Packet:

```md
## NOISE-R-002

- Example ID: NOISE-R-002
- Release type: Integration readiness update
- Readiness claim: "The partner integration release is ready for production."
- Evidence details:
  - Code review approval is complete.
  - Unit tests passed for request payload mapping.
  - Sandbox setup note confirms credentials were created but does not show an end-to-end call.
  - Stakeholder comment says the release is important for timing.
  - A manual checklist exists but all integration validation rows are still blank.
- Known issues:
  - None documented.
- Evidence gaps:
  - No integration smoke test.
  - No production-like payload test.
  - No monitoring note.
  - No rollback or disablement plan.
  - No owner sign-off for unresolved integration validation.
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
