# Release Readiness Report

### Eval Example

- Example ID: REL-B-002
- Release type: Checkout-like workflow update
- Claimed or desired decision: Evaluate whether the stated readiness claim is supported by the evidence.

### Input Claim

> "The workflow update passed testing and is ready."

### Summary

The readiness claim is contradicted by the test evidence. The core completion-path test failed on the release candidate, manual QA could not verify completion, and there is no passing retest, workaround, rollback plan, or owner acceptance of the failure.

### Evidence Summary

- Strong evidence:
  - Manual QA confirms setup and navigation passed.
  - Code review approval is complete.
- Weak or partial evidence:
  - Deployment note is drafted but not executed.
  - Code review approval does not address the failed release-candidate test.
- Known issues:
  - Core completion path fails in the release-candidate test run.

### Readiness Label

Selected label: Blocked

Allowed labels: Green / Yellow / Red / Blocked

### Rationale

The packet directly contradicts the claim that testing passed and the workflow is ready. The core completion path failed on the release candidate, and manual QA could not verify completion because of that failing test. This is Blocked because the failed core path prevents a safe readiness recommendation until there is a passing retest, accepted workaround, or explicit human decision that addresses the failure.

### Supported Claims

- Setup and navigation passed manual QA.
- Code review approval is complete.
- Deployment note has been drafted.

### Unsupported or Weak Claims

- The claim that the workflow update passed testing is contradicted by the failed core completion-path test.
- The claim that the workflow is ready is unsupported because completion could not be verified.
- Code review approval is weak readiness evidence because it does not address the failed release-candidate test.
- The drafted deployment note does not prove deployment readiness.

### Evidence Gaps

- No passing retest.
- No workaround.
- No rollback plan.
- No decision owner accepted the failure.

### Risks

- Users may be unable to complete the core workflow.
- Shipping with a failed release-candidate core-path test could convert a known test failure into a user-facing failure.
- Without rollback or workaround evidence, recovery is undefined.

### Next Evidence

- Provide a passing retest for the core completion path on the release candidate.
- Add a documented workaround or mitigation if the failure cannot be fixed immediately.
- Add a rollback plan with verification steps.
- Add explicit decision-owner acceptance if any risk is deferred.

### Human Review Note

Human review is required, but the current packet supports a Blocked recommendation because a release-candidate core path failed. This report does not authorize shipment.

### Eval Notes

Use this section only after generation, during scoring.

- Actual label:
- Important evidence cited:
- Score:
- Review note:
