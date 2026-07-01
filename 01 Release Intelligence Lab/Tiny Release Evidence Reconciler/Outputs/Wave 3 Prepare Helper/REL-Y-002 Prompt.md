# Release Eval Prepare Prompt

Example ID: REL-Y-002

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

### Example REL-Y-002

- Example ID: REL-Y-002
- Release type: Third-party integration
- Readiness claim: "The integration is ready; only cosmetic issues remain."
- Claimed or desired decision: Evaluate whether the stated readiness claim is supported by the evidence.
- Evidence sources present:
  - Integration smoke test
  - Manual visual review
  - Partner sandbox note
  - Code review approval
- Evidence details:
  - Integration smoke test passed for account connection and initial sync in sandbox.
  - Manual visual review found spacing and label inconsistencies in the connection modal.
  - Partner sandbox note confirms test credentials worked during validation.
  - Code review approval notes retry behavior was reviewed but not load tested.
- Known issues:
  - One intermittent sync delay occurs in sandbox, described as likely non-user-facing but not fully explained.
- Evidence gaps:
  - No production-like sync volume test.
  - No monitoring note for delayed syncs.
  - Cosmetic-vs-functional impact of the intermittent delay is unclear.

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
