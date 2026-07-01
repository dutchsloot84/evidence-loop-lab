# Release Readiness Report

### Eval Example

- Example ID: REL-B-004
- Release type: Infrastructure migration
- Claimed or desired decision: Evaluate whether the stated readiness claim is supported by the evidence.

### Input Claim

> "The migration is ready because staging validation passed."

### Summary

The migration is blocked despite passing staging validation. The rollback drill failed in staging, the restored environment did not pass health checks, and there is no verified fix, successful rollback retest, operational mitigation, or human acceptance of rollback risk.

### Evidence Summary

- Strong evidence:
  - Staging validation passed for read and write operations after migration.
  - Automated regression suite passed before the rollback drill.
  - Code review approval is complete.
- Weak or partial evidence:
  - Positive validation evidence only covers forward migration behavior, not recovery.
  - Monitoring thresholds are not defined.
- Known issues:
  - Rollback failed in staging and has no verified fix.

### Readiness Label

Selected label: Blocked

Allowed labels: Green / Yellow / Red / Blocked

### Rationale

The packet directly contradicts operational readiness because rollback failed in staging. Passing forward-path staging validation is not enough for an infrastructure migration when the recovery path is known to fail. This is Blocked because the failed rollback drill creates a direct release-safety contradiction until rollback is fixed, retested, mitigated, or explicitly accepted by an authorized human owner.

### Supported Claims

- Forward staging validation passed for read and write operations.
- Automated regression suite passed before the rollback drill.
- Code review approval is complete.

### Unsupported or Weak Claims

- The claim that the migration is ready is contradicted by the failed rollback drill.
- Operational readiness is unsupported because rollback failed and has no verified fix.
- Monitoring readiness is unsupported because thresholds are not defined.

### Evidence Gaps

- No successful rollback retest.
- No operational mitigation if rollback is needed.
- No human acceptance of rollback risk.
- Monitoring thresholds are not defined.

### Risks

- If the migration causes production issues, the recovery path may fail.
- The restored environment may remain unhealthy after rollback.
- Without monitoring thresholds, the team may not detect migration or rollback issues quickly.

### Next Evidence

- Fix the rollback issue and provide a successful rollback retest.
- Add operational mitigation if rollback remains risky.
- Define monitoring thresholds for migration and rollback health.
- Add explicit human acceptance if any rollback risk is deferred.

### Human Review Note

Human review is required, and the current evidence supports a Blocked recommendation until rollback is fixed, retested, mitigated, or explicitly accepted. This report does not authorize shipment.

### Eval Notes

Use this section only after generation, during scoring.

- Actual label:
- Important evidence cited:
- Score:
- Review note:
