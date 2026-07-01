# Release Eval Prepare Prompt

Example ID: REL-G-004

Use the selected synthetic release packet and the report template below to generate one markdown readiness report.

Rules:

- Use only the packet evidence provided here.
- Do not invent evidence.
- Assign exactly one readiness label: Green, Yellow, Red, or Blocked.
- Separate supported claims from unsupported or weak claims.
- Name concrete evidence gaps and next evidence needed.
- Preserve the human approval boundary. You may recommend a label, but you may not claim authority to ship or approve.
- Keep all details synthetic and sanitized.

## Selected Packet

### Example REL-G-004

- Example ID: REL-G-004
- Release type: Minor feature
- Readiness claim: "The minor feature is ready for general availability."
- Claimed or desired decision: Evaluate whether the stated readiness claim is supported by the evidence.
- Evidence sources present:
  - Acceptance criteria checklist
  - Automated test mapping
  - Manual smoke test
  - Code review approval
  - Release note draft
  - Monitoring note
- Evidence details:
  - Each acceptance criterion maps to at least one automated test or documented manual check.
  - Automated tests passed for the new feature path, permission handling, and disabled state.
  - Manual smoke test covered the primary desktop and mobile flows.
  - Code review approval included confirmation that edge-case handling was reviewed.
  - Release note draft accurately describes the user-visible change.
  - Monitoring note names event counters for feature usage and error rate.
- Known issues:
  - One help-text improvement is scheduled for a later documentation update.
- Evidence gaps:
  - Accessibility review is summarized but not attached as a separate artifact.

## Report Template

# Release Readiness Report Template

Use this template once per eval example. Keep entries synthetic or sanitized. Do not include real company names, customer names, employee names, repo names, ticket IDs, links, exact titles, or sensitive context.

## Release Readiness Report

### Eval Example

- Example ID:
- Release type:
- Claimed or desired decision:

### Input Claim

> Paste the readiness claim exactly as provided in the synthetic input packet.

### Summary

Write a concise readiness summary in one to three sentences.

### Evidence Summary

Summarize the observable evidence used for the decision. Separate strong evidence from weak, missing, or ambiguous evidence.

- Strong evidence:
  -
- Weak or partial evidence:
  -
- Known issues:
  -

### Readiness Label

Selected label:

Allowed labels: Green / Yellow / Red / Blocked

### Rationale

Explain why this label fits the evidence. State what the evidence supports, what it does not support, and why the decision still needs or does not need human review.

### Supported Claims

-

### Unsupported or Weak Claims

-

### Evidence Gaps

-

### Risks

-

### Next Evidence

List the concrete evidence needed to improve confidence or move the release decision forward.

-

### Human Review Note

State whether human review is required and why. The report may recommend a readiness label, but it should not claim authority to ship.

### Eval Notes

Use this section only after generation, during scoring.

- Actual label:
- Important evidence cited:
- Score:
- Review note:
