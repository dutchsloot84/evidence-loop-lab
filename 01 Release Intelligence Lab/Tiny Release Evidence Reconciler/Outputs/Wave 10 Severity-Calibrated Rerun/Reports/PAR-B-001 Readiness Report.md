## Eval Example

PAR-B-001

## Input Claim

"The migration is ready after successful staging validation."

## Summary

The migration has positive staging validation and review evidence, but readiness is contradicted by a failed rollback drill with no verified fix or mitigation. The claim should not be treated as ready without additional human review and successful rollback evidence.

## Evidence Summary

- Staging validation passed for read and write operations after migration.
- Automated regression passed before the rollback drill.
- Code review approval is complete.
- Rollback drill failed because the restored environment did not pass health checks.

## Readiness Label

Blocked

## Rationale

A migration readiness claim depends on the ability to recover safely if the migration causes issues. The failed rollback drill directly undermines operational readiness, and there is no successful rollback retest, mitigation plan, or human acceptance of rollback risk.

## Supported Claims

- Staging read and write validation passed.
- Automated regression passed before rollback testing.
- Code review approval is complete.

## Unsupported or Weak Claims

- The migration is ready for release.
- Rollback capability is reliable.
- Operational readiness is sufficient if recovery is needed.

## Evidence Gaps

- No successful rollback retest.
- No verified fix for the failed rollback.
- No operational mitigation if rollback is required.
- No human acceptance of rollback risk.
- Monitoring thresholds are not defined.

## Risks

- Recovery may fail if the migration must be rolled back.
- Health checks may remain unreliable after restore.
- Teams may lack clear monitoring signals during or after deployment.
- Release confidence may be overstated by staging validation alone.

## Next Evidence

- Successful rollback retest with passing health checks.
- Documented mitigation plan for rollback failure scenarios.
- Defined monitoring thresholds for migration and restore health.
- Human review and acceptance of any remaining rollback risk.

## Human Review Note

A human decision-maker should review the failed rollback evidence and decide whether the release can proceed only after recovery readiness is demonstrated or explicitly accepted.
