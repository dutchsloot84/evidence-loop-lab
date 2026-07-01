# Wave 12 Model Visible Packets

Synthetic packets for the fresh unseen parallel batch.

These packets are model-visible. They do not include expected labels or scorer-only rationale.

## NEW-G-001

- Example ID: NEW-G-001
- Release type: Feature flag configuration rollout
- Readiness claim: "The feature flag cleanup is ready because validation, rollback, and monitoring are covered."
- Claimed or desired decision: Evaluate whether the stated readiness claim is supported by the evidence.
- Evidence sources present:
  - Flag diff summary
  - Automated validation result
  - Manual smoke test
  - Rollback note
  - Monitoring note
  - Owner approval note
- Evidence details:
  - Flag diff summary shows two retired flags removed and one default value changed only for a dormant path.
  - Automated validation passed for enabled, disabled, and default-path behavior.
  - Manual smoke test covered sign-in, workspace load, and the settings panel that reads the flag.
  - Rollback note describes restoring the previous flag snapshot and rerunning validation.
  - Monitoring note names flag-evaluation errors and settings-panel error rate for the first two hours.
  - Owner approval note confirms the cleanup scope is acceptable.
- Known issues:
  - One internal runbook screenshot still shows the old flag name.
- Evidence gaps:
  - No separate product narrative is attached.

## NEW-Y-001

- Example ID: NEW-Y-001
- Release type: API response behavior update
- Readiness claim: "The API behavior update is ready; remaining concerns are limited to documentation polish."
- Claimed or desired decision: Evaluate whether the stated readiness claim is supported by the evidence.
- Evidence sources present:
  - Contract test result
  - Integration smoke test
  - Code review approval
  - Documentation draft
  - Client compatibility note
- Evidence details:
  - Contract tests passed for the documented success and validation-error responses.
  - Integration smoke test passed for the primary client flow in sandbox.
  - Code review approval notes that response parsing was simplified.
  - Documentation draft still needs examples for one optional field.
  - Client compatibility note says one secondary client logged a rare fallback warning during sandbox testing, but no failed requests were observed.
- Known issues:
  - The fallback warning may be harmless or may indicate a compatibility edge case; impact is not proven.
- Evidence gaps:
  - No production-like compatibility sweep across all client variants.
  - No monitoring note for fallback warning frequency.
  - No user-impact note for the secondary client warning.

## NEW-R-001

- Example ID: NEW-R-001
- Release type: Operational deployment readiness
- Readiness claim: "The service deployment is ready and operational readiness is complete."
- Claimed or desired decision: Evaluate whether the stated readiness claim is supported by the evidence.
- Evidence sources present:
  - Build verification
  - Deployment command note
  - Code review approval
  - Release calendar entry
- Evidence details:
  - Build verification passed on the release candidate.
  - Deployment command note lists the command intended for the release window.
  - Code review approval is complete.
  - Release calendar entry reserves a deployment window.
- Known issues:
  - None documented.
- Evidence gaps:
  - Rollback plan is missing.
  - Monitoring plan is missing.
  - No post-deploy smoke test is defined.
  - No release owner, support owner, or on-call note is present.
  - No incident response criteria are documented.

## NEW-B-001

- Example ID: NEW-B-001
- Release type: Schema migration release
- Readiness claim: "The schema migration is ready after staging validation and review."
- Claimed or desired decision: Evaluate whether the stated readiness claim is supported by the evidence.
- Evidence sources present:
  - Staging migration result
  - Automated regression result
  - Backout drill result
  - Code review approval
  - Data integrity check
- Evidence details:
  - Staging migration completed and basic read/write checks passed.
  - Automated regression passed before the backout drill.
  - Data integrity check found no mismatched row counts after migration.
  - Backout drill failed because restored indexes were incomplete and query health checks did not pass.
  - Code review approval is complete.
- Known issues:
  - Backout failed in staging and has no verified fix.
- Evidence gaps:
  - No successful backout retest.
  - No operational mitigation if backout is needed.
  - No human acceptance of failed-backout risk.
  - No monitoring thresholds for post-migration query health.
