# NOISE-G-002 Worker Prompt

You are a generation-only worker in a parallel evidence-loop test.

Use only this prompt. Do not inspect repo files. Do not read answer keys, expected labels, scoring rubrics, eval ledgers, prior reports, or other project files.

Return one markdown readiness report.

Rules and severity calibration are the same as Wave 13: use only the packet, do not invent evidence, assign exactly one label, preserve the human approval boundary, and do not mention scoring or answer keys. Green means supported with minor gaps; Yellow means partial readiness with bounded unresolved risk; Red means materially unsupported; Blocked means evidence directly contradicts readiness or a required gate failed.

Packet:

```md
## NOISE-G-002

- Example ID: NOISE-G-002
- Release type: Dependency patch release
- Readiness claim: "The dependency patch is ready because regression, rollback, and monitoring checks are complete."
- Evidence details:
  - Dependency diff summary shows one patch-level update for a utility package with no public API change.
  - Automated regression passed for affected parsing and formatting paths.
  - Manual smoke test covered import, export, and settings save.
  - Rollback note says the package lockfile can be restored and regression rerun.
  - Monitoring note names import error rate and export failure rate.
  - Technical owner approval is recorded.
  - A non-blocking lint warning exists in an unrelated sample file.
- Known issues:
  - Unrelated sample lint warning remains.
- Evidence gaps:
  - No product-facing announcement is attached.
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
