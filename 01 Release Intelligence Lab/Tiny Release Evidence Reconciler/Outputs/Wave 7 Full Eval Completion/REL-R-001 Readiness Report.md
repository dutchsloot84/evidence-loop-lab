# Release Readiness Report

### Eval Example

- Example ID: REL-R-001
- Release type: Multi-part feature release
- Claimed or desired decision: Evaluate whether the stated readiness claim is supported by the evidence.

### Input Claim

> "The feature is fully ready for release."

### Summary

The packet does not support the claim that the feature is fully ready for release. It shows merged implementation work and a release note draft, but no validation, review approval, rollback, or monitoring evidence.

### Evidence Summary

- Strong evidence:
  - Merge summary says all planned implementation changes were merged.
  - Pull request description summaries describe intended behavior.
  - Release note draft describes the feature as available to all users.
- Weak or partial evidence:
  - Pull request descriptions do not include validation results.
  - Release note draft communicates availability but does not prove readiness.
  - Merge summary proves implementation completion, not release validation.
- Known issues:
  - None documented in the packet.

### Readiness Label

Selected label: Red

Allowed labels: Green / Yellow / Red / Blocked

### Rationale

The readiness claim is much stronger than the evidence. Merge summaries and intended-behavior descriptions are not enough to establish release readiness, especially for a multi-part feature. The packet lacks automated test results, manual QA evidence, code review approval evidence, rollback, and monitoring. This is Red because readiness is unsupported, but the packet does not show a direct failed critical path that would make it Blocked.

### Supported Claims

- Planned implementation changes were merged.
- Pull request descriptions describe intended behavior.
- A release note draft exists and describes the feature as available to all users.

### Unsupported or Weak Claims

- The claim that the feature is fully ready is unsupported.
- Validation readiness is unsupported because no test or QA results are present.
- Review readiness is unsupported because no code review approval evidence is present.
- Operational readiness is unsupported because rollback and monitoring notes are missing.

### Evidence Gaps

- No automated test results.
- No manual QA evidence.
- No code review approval evidence.
- No rollback note.
- No monitoring note.

### Risks

- Implementation may be complete while release readiness remains unproven.
- Users may see a release note for a feature whose behavior has not been validated in the packet.
- Missing rollback and monitoring make recovery and detection unclear.

### Next Evidence

- Add automated test results for the feature scope.
- Add manual QA evidence for the main user paths.
- Add code review approval evidence.
- Add rollback and monitoring notes.

### Human Review Note

Human review is required because the packet lacks material validation and operational evidence. This report recommends a readiness label from the packet evidence but does not authorize shipment.

### Eval Notes

Use this section only after generation, during scoring.

- Actual label:
- Important evidence cited:
- Score:
- Review note:
