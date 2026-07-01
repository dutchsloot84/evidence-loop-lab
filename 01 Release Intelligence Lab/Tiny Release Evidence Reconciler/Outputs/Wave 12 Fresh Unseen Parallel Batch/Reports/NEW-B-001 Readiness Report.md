## Eval Example

NEW-B-001

## Input Claim

"The schema migration is ready after staging validation and review."

## Summary

The evidence shows meaningful staging and review progress, including successful migration execution, basic read/write validation, regression success, data integrity checks, and completed code review. However, the failed backout drill is a direct readiness blocker for this schema migration release because there is no verified fix, no successful retest, and no accepted mitigation.

## Evidence Summary

- Staging migration completed successfully.
- Basic read/write checks passed.
- Automated regression passed before the backout drill.
- Data integrity check found no mismatched row counts after migration.
- Code review approval is complete.
- Backout drill failed due to incomplete restored indexes and failed query health checks.

## Readiness Label

Blocked

## Rationale

The central readiness claim is contradicted by the failed staging backout drill. For a schema migration release, rollback or backout readiness is a required operational control. The packet states the backout failure has no verified fix, no successful retest, and no operational mitigation if backout is needed. Positive migration, regression, integrity, and review evidence does not overcome that unresolved operational failure.

## Supported Claims

- The migration ran successfully in staging.
- Basic staging read/write behavior was validated.
- Automated regression passed before the backout drill.
- Data integrity checks found no mismatched row counts.
- Code review approval is complete.

## Unsupported or Weak Claims

- The migration is ready overall.
- Backout readiness is established.
- Query health after rollback is acceptable.
- Operational readiness is sufficient if backout becomes necessary.

## Evidence Gaps

- No successful backout retest.
- No verified fix for incomplete restored indexes.
- No operational mitigation for a needed backout.
- No human acceptance of the failed-backout risk.
- No monitoring thresholds for post-migration query health.

## Risks

- A production backout could leave indexes incomplete.
- Query health could degrade after rollback.
- Operators may lack a verified recovery path if migration issues appear.
- Post-migration query health problems may not be detected quickly without defined thresholds.

## Next Evidence

- Fix the backout issue and rerun the backout drill successfully.
- Verify restored indexes and query health checks after backout.
- Define post-migration query health monitoring thresholds.
- Document operational mitigation steps if backout is needed.
- Obtain human review of any residual backout risk.

## Human Review Note

A human reviewer should evaluate the corrected backout evidence and any proposed operational mitigation before treating the migration as ready.
