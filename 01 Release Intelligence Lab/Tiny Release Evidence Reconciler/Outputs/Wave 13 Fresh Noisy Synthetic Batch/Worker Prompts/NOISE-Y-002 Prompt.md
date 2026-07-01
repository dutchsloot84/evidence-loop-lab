# NOISE-Y-002 Worker Prompt

You are a generation-only worker in a parallel evidence-loop test.

Use only this prompt. Do not inspect repo files. Do not read answer keys, expected labels, scoring rubrics, eval ledgers, prior reports, or other project files.

Return one markdown readiness report.

Rules and severity calibration are the same as Wave 13: use only the packet, do not invent evidence, assign exactly one label, preserve the human approval boundary, and do not mention scoring or answer keys. Green means supported with minor gaps; Yellow means partial readiness with bounded unresolved risk; Red means materially unsupported; Blocked means evidence directly contradicts readiness or a required gate failed.

Packet:

```md
## NOISE-Y-002

- Example ID: NOISE-Y-002
- Release type: Export formatting update
- Readiness claim: "The export formatting update is ready; only cosmetic table alignment remains."
- Evidence details:
  - Golden-file tests passed for standard and empty export cases.
  - Manual export smoke test passed for the primary report type.
  - Code review approval says column ordering was simplified.
  - UI review found cosmetic table alignment differences in a preview screen.
  - One large export produced a warning about truncated optional notes, but the file completed and row counts matched.
- Known issues:
  - Large-export warning may be harmless or may indicate optional-note loss; impact is not proven.
- Evidence gaps:
  - No large-export content comparison.
  - No monitoring note for truncation warnings.
  - No user-impact note for optional notes.
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
