# Wave 10 Model Visible Packets

Synthetic packets for the severity-calibrated parallel rerun.

These packets are model-visible. They do not include expected labels or scorer-only rationale.

## PAR-R-001

- Example ID: PAR-R-001
- Release type: Deployment readiness update
- Readiness claim: "The deployment is ready and operational coverage is complete."
- Claimed or desired decision: Evaluate whether the stated readiness claim is supported by the evidence.
- Evidence sources present:
  - Deployment note
  - Build verification
  - Code review approval
  - Release window note
- Evidence details:
  - Deployment note lists the deploy command and planned release window.
  - Build verification passed on the release candidate.
  - Code review approval is complete.
  - Release window note identifies when the deployment should occur.
- Known issues:
  - None documented.
- Evidence gaps:
  - Rollback plan is missing.
  - Monitoring plan is missing.
  - No post-deploy smoke test is defined.
  - No release owner or on-call note is present.

## PAR-B-001

- Example ID: PAR-B-001
- Release type: Migration release
- Readiness claim: "The migration is ready after successful staging validation."
- Claimed or desired decision: Evaluate whether the stated readiness claim is supported by the evidence.
- Evidence sources present:
  - Staging validation note
  - Automated regression result
  - Rollback drill result
  - Code review approval
- Evidence details:
  - Staging validation passed for read and write operations after migration.
  - Automated regression passed before the rollback drill.
  - Rollback drill failed because the restored environment did not pass health checks.
  - Code review approval is complete.
- Known issues:
  - Rollback failed in staging and has no verified fix.
- Evidence gaps:
  - No successful rollback retest.
  - No operational mitigation if rollback is needed.
  - No human acceptance of rollback risk.
  - Monitoring thresholds are not defined.

## PAR-Y-001

- Example ID: PAR-Y-001
- Release type: Third-party sync update
- Readiness claim: "The sync update is ready; remaining issues are only cosmetic."
- Claimed or desired decision: Evaluate whether the stated readiness claim is supported by the evidence.
- Evidence sources present:
  - Integration smoke test
  - Sandbox credential note
  - Code review approval
  - Manual UI review
- Evidence details:
  - Integration smoke test passed for account connection and first sync in sandbox.
  - Sandbox credential note confirms test credentials worked during validation.
  - Code review approval says retry behavior was reviewed.
  - Manual UI review found alignment and label spacing issues in the sync settings panel.
  - A low-frequency delayed-sync warning appeared twice in sandbox but was not reproduced under a larger batch.
- Known issues:
  - Delayed-sync warning may be functional or may be sandbox-only; impact is not proven.
- Evidence gaps:
  - No production-like batch sync test.
  - No monitoring note for delayed syncs.
  - No user-impact note for the delayed-sync warning.
