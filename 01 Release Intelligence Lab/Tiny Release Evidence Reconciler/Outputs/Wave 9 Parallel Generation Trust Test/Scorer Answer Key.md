# Wave 9 Scorer Answer Key

Scorer-only answer key created after generation workers completed.

Do not include this file in model-visible generation prompts.

## PAR-G-001

- Expected readiness label: Green
- Expected rationale: The configuration cleanup is supported by scoped diff evidence, validation, smoke testing, backup, rollback, and monitoring. The stale internal comment and missing stakeholder narrative are minor follow-ups.
- Important evidence to cite:
  - Configuration diff shows only deprecated flags removed and one renamed threshold without behavior change.
  - Automated validation passed default, opt-in, and disabled-path behavior.
  - Manual smoke test covered sign-in, dashboard load, and affected settings view.
  - Backup confirmation was captured before cleanup.
  - Rollback restores previous configuration snapshot and reruns validation.
  - Monitoring covers configuration-load errors and settings-view error rate.
- Failure mode to watch for: Over-penalizing minor documentation follow-ups despite strong technical readiness evidence.

## PAR-Y-001

- Expected readiness label: Yellow
- Expected rationale: Basic sandbox sync evidence exists, but the claim that only cosmetic issues remain is not proven because the delayed-sync warning may be functional and lacks batch validation, monitoring, and impact analysis.
- Important evidence to cite:
  - Integration smoke test passed account connection and first sync in sandbox.
  - Sandbox credentials worked during validation.
  - Code review says retry behavior was reviewed.
  - Manual UI review found spacing and label issues.
  - Delayed-sync warning appeared twice and impact is not proven.
- Failure mode to watch for: Accepting the "cosmetic only" framing without challenging delayed-sync evidence.

## PAR-R-001

- Expected readiness label: Red
- Expected rationale: Build, review, deployment command, and release-window evidence are useful, but the claim that operational coverage is complete is materially unsupported because rollback, monitoring, post-deploy validation, and ownership are missing.
- Important evidence to cite:
  - Deployment note lists deploy command and release window.
  - Build verification passed.
  - Code review approval is complete.
  - Rollback plan is missing.
  - Monitoring plan is missing.
  - Post-deploy smoke test and owner/on-call note are missing.
- Failure mode to watch for: Marking Yellow because implementation/deploy basics exist while underweighting missing operational coverage.

## PAR-B-001

- Expected readiness label: Blocked
- Expected rationale: Staging validation is not enough because rollback failed in staging. A failed recovery path directly contradicts migration readiness until rollback is fixed, retested, mitigated, or explicitly accepted by an authorized human owner.
- Important evidence to cite:
  - Staging validation passed for read and write operations after migration.
  - Automated regression passed before rollback drill.
  - Rollback drill failed because restored environment did not pass health checks.
  - Code review approval is complete.
  - No successful rollback retest, mitigation, risk acceptance, or monitoring thresholds exist.
- Failure mode to watch for: Marking Red instead of Blocked when failed rollback directly contradicts operational readiness.
