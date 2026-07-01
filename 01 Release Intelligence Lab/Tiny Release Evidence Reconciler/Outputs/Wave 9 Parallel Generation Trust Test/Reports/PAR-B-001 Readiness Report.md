## Eval Example

PAR-B-001

## Input Claim

"The migration is ready after successful staging validation."

## Summary

The evidence does not support readiness for the migration release. Staging validation and regression results are positive, but rollback failed in staging and there is no verified fix, retest, mitigation, or human acceptance of that rollback risk.

## Evidence Summary

- Staging validation passed for read and write operations after migration.
- Automated regression passed before the rollback drill.
- Rollback drill failed because the restored environment did not pass health checks.
- Code review approval is complete.

## Readiness Label

Red

## Rationale

A migration release needs a credible recovery path if the migration must be reversed. The failed rollback drill directly undermines the readiness claim, especially because there is no successful rollback retest and no documented mitigation.

## Supported Claims

- Staging validation passed for migrated read and write behavior.
- Automated regression completed successfully before the rollback drill.
- Code review approval is complete.

## Unsupported or Weak Claims

- The migration is ready for release.
- Rollback capability is available.
- Operational readiness is sufficient if rollback is needed.

## Evidence Gaps

- No successful rollback retest.
- No verified fix for the failed rollback.
- No operational mitigation if rollback is required.
- No human acceptance of rollback risk.
- Monitoring thresholds are not defined.

## Risks

- Failed rollback could leave the environment unhealthy during recovery.
- Operators may lack clear criteria for detecting migration-related degradation.
- Release decision-makers may underestimate recovery risk if staging success is considered alone.

## Next Evidence

- Verified fix for the rollback failure.
- Successful rollback retest with passing health checks.
- Defined monitoring thresholds for post-migration behavior.
- Documented operational mitigation plan.
- Human review and acceptance of residual rollback risk, if any.

## Human Review Note

A human reviewer should evaluate whether the rollback failure blocks release or whether an explicitly accepted mitigation is sufficient.
