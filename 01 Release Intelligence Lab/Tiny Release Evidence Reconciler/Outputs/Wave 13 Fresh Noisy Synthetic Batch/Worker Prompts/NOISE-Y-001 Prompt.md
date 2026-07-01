# NOISE-Y-001 Worker Prompt

You are a generation-only worker in a parallel evidence-loop test.

Use only this prompt. Do not inspect repo files. Do not read answer keys, expected labels, scoring rubrics, eval ledgers, prior reports, or other project files.

Return one markdown readiness report.

Rules and severity calibration are the same as Wave 13: use only the packet, do not invent evidence, assign exactly one label, preserve the human approval boundary, and do not mention scoring or answer keys. Green means supported with minor gaps; Yellow means partial readiness with bounded unresolved risk; Red means materially unsupported; Blocked means evidence directly contradicts readiness or a required gate failed.

Packet:

```md
## NOISE-Y-001

- Example ID: NOISE-Y-001
- Release type: Notification template update
- Readiness claim: "The notification template update is ready; remaining concerns are only copy polish."
- Evidence details:
  - Template render test passed for default and compact layouts.
  - Manual inbox smoke test passed for one mailbox provider.
  - Code review approval is complete.
  - Copy review found two punctuation changes to make.
  - Delivery observation note says a secondary mailbox provider showed delayed preview text twice, but the messages were delivered.
  - A designer comment asks whether the subject line should be shorter, but no owner marked it blocking.
- Known issues:
  - Delayed preview text may be provider-specific or may indicate template compatibility risk; impact is not proven.
- Evidence gaps:
  - No multi-provider inbox sweep.
  - No monitoring note for delayed preview text.
  - No user-impact note for preview delay.
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
