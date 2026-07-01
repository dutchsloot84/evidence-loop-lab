## Eval Example

NOISE-B-002

## Input Claim

"The permission migration is ready because access checks passed in staging."

## Summary

The release is not ready for human approval. Staging checks passed for two standard roles, but rollback testing exposed elevated access for a restricted role after restore, with no retest, mitigation, monitoring, or accepted risk.

## Readiness Label

Blocked

## Rationale

A permission migration cannot rely only on forward-path staging checks when rollback leaves elevated access in place. The known issue directly affects access control and lacks documented risk acceptance.

## Key Evidence

- Staging access checks passed for two standard roles.
- Automated regression passed before rollback testing.
- Security review found the intended permission model acceptable.
- Rollback drill failed because one restricted role retained elevated access after restore.
- No mitigation, retest, audit query, or risk acceptance exists.

## Human Review Note

Human approval is required before release because the unresolved rollback failure creates a security-relevant access-control risk.
