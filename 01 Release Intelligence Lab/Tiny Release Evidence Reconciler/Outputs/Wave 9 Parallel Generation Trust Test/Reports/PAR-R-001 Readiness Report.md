## Eval Example

PAR-R-001

## Input Claim

"The deployment is ready and operational coverage is complete."

## Summary

The evidence partially supports deployment readiness, but it does not support the claim that operational coverage is complete.

## Evidence Summary

The packet includes a deployment note with the deploy command and planned release window, a passing build verification for the release candidate, completed code review approval, and a release window note.

## Readiness Label

Yellow

## Rationale

The release candidate has basic readiness evidence: build verification passed, code review approval is complete, and a release window is identified. However, several operational readiness elements are missing, including rollback, monitoring, post-deploy smoke testing, and ownership/on-call coverage.

## Supported Claims

- The release candidate passed build verification.
- Code review approval is complete.
- A planned release window exists.
- A deploy command is documented.

## Unsupported or Weak Claims

- Operational coverage is complete.
- Deployment is fully ready without additional release controls.
- Post-deployment validation is accounted for.

## Evidence Gaps

- Rollback plan is missing.
- Monitoring plan is missing.
- No post-deploy smoke test is defined.
- No release owner or on-call note is present.

## Risks

- Failed deployment may be harder to recover without a rollback plan.
- Issues may go undetected without monitoring coverage.
- Post-deploy regressions may not be caught promptly.
- Response ownership may be unclear during or after release.

## Next Evidence

- Add a rollback plan.
- Add monitoring expectations and alert coverage.
- Define post-deploy smoke tests.
- Identify release owner and on-call contact.

## Human Review Note

This report recommends a readiness label only. A human reviewer should decide whether the deployment may proceed.
