# Release Readiness Report

### Eval Example

- Example ID: REL-B-005
- Release type: Bundled feature release
- Claimed or desired decision: Evaluate whether the stated readiness claim is supported by the evidence.

### Input Claim

> "All core items are complete and the bundle is ready."

### Summary

The readiness claim is directly contradicted by the packet evidence. The release checklist marks the bundle ready, but the backlog status summary shows core items still not started or in progress, tests only cover the completed subset, and the release note claims all core items are included.

### Evidence Summary

- Strong evidence:
  - Release checklist marks the bundle as ready.
  - Backlog status summary shows three core items still in "not started" or "in progress" status.
  - Automated tests passed only for the completed subset.
  - Release note draft describes all core items as included.
- Weak or partial evidence:
  - Release checklist conflicts with backlog and test-scope evidence.
  - Automated tests do not cover incomplete core items.
- Known issues:
  - Several core items claimed in scope are not complete.

### Readiness Label

Selected label: Blocked

Allowed labels: Green / Yellow / Red / Blocked

### Rationale

The packet needs a scope decision before readiness can be evaluated safely. The claim says all core items are complete, but backlog evidence says several core items are incomplete, tests only cover the completed subset, and the release note still claims all core items are included. This is Blocked because the claimed release scope directly contradicts completion and validation evidence.

### Supported Claims

- Release checklist marks the bundle as ready.
- Backlog status summary identifies incomplete core items.
- Automated tests passed for the completed subset.
- Release note draft claims all core items are included.

### Unsupported or Weak Claims

- The claim that all core items are complete is contradicted by backlog status.
- The claim that the full bundle is ready is unsupported because tests cover only the completed subset.
- The release note overstates scope because it describes all core items as included.

### Evidence Gaps

- No scope-change approval.
- No updated release note matching the completed subset.
- No validation for incomplete core items.
- No decision owner accepting a reduced scope.

### Risks

- Users may expect core items that are not complete.
- A release could ship with mismatched scope, validation, and release notes.
- Tests may give false confidence because they cover only the completed subset.

### Next Evidence

- Decide whether to reduce scope or complete the remaining core items.
- Add scope-change approval if shipping a reduced subset.
- Update the release note to match the completed scope.
- Add validation evidence for any core item kept in scope.
- Add decision-owner acceptance of the final scope.

### Human Review Note

Human review is required, and the current evidence supports a Blocked recommendation until scope, completion, validation, and release-note evidence are reconciled. This report does not authorize shipment.

### Eval Notes

Use this section only after generation, during scoring.

- Actual label:
- Important evidence cited:
- Score:
- Review note:
