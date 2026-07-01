# Eval Example

PAR-B-001

# Input Claim

"The migration is ready after successful staging validation."

# Summary

The packet shows meaningful staging validation and review evidence, but the failed rollback drill is a direct readiness blocker for a migration release. The readiness claim is not sufficiently supported until rollback recovery is fixed and retested.

# Evidence Summary

- Staging validation passed for read and write operations after migration.
- Automated regression passed before the rollback drill.
- Code review approval is complete.
- Rollback drill failed because the restored environment did not pass health checks.

# Readiness Label

Blocked

# Rationale

The migration has positive functional evidence, but rollback is a required safety control for this release type. Because the rollback drill failed in staging and there is no verified fix or successful retest, the packet directly contradicts treating the migration as ready.

# Supported Claims

- Staging read and write validation passed.
- Automated regression completed successfully before rollback testing.
- Code review approval is complete.

# Unsupported or Weak Claims

- The migration is ready overall.
- Rollback capability is available if needed.
- Operational readiness is established.

# Evidence Gaps

- No successful rollback retest.
- No operational mitigation if rollback is needed.
- No human acceptance of rollback risk.
- Monitoring thresholds are not defined.

# Risks

- A failed migration may not be recoverable through the documented rollback path.
- Restored environments may remain unhealthy after rollback.
- Operators may lack defined thresholds for detecting post-migration issues.
- Residual rollback risk has not been formally reviewed by humans.

# Next Evidence

- Verified rollback fix.
- Successful rollback retest with passing health checks.
- Defined monitoring thresholds.
- Documented mitigation plan if rollback is needed.
- Human review of residual rollback risk.

# Human Review Note

A human reviewer should evaluate the rollback failure, mitigation plan, and residual operational risk before treating this migration as ready.
