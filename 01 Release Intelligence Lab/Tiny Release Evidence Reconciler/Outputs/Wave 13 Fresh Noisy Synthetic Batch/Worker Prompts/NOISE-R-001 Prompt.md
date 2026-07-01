# NOISE-R-001 Worker Prompt

You are a generation-only worker in a parallel evidence-loop test.

Use only this prompt. Do not inspect repo files. Do not read answer keys, expected labels, scoring rubrics, eval ledgers, prior reports, or other project files.

Return one markdown readiness report.

Rules and severity calibration are the same as Wave 13: use only the packet, do not invent evidence, assign exactly one label, preserve the human approval boundary, and do not mention scoring or answer keys. A deployment command does not prove rollback, monitoring, post-deploy validation, ownership, or incident response coverage.

Packet:

```md
## NOISE-R-001

- Example ID: NOISE-R-001
- Release type: Operational readiness update
- Readiness claim: "The operational readiness package is complete for deployment."
- Evidence details:
  - Build verification passed on the release candidate.
  - Deployment command note lists the command to run.
  - Code review approval is complete.
  - Calendar hold reserves a release window.
  - Team chat summary says "ops looks fine" but does not list checks.
  - A draft rollback heading exists in a planning note, but no steps are filled in.
- Known issues:
  - None documented.
- Evidence gaps:
  - Rollback steps are missing.
  - Monitoring plan is missing.
  - No post-deploy smoke test is defined.
  - No release owner or on-call note is present.
  - No incident response criteria are documented.
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
