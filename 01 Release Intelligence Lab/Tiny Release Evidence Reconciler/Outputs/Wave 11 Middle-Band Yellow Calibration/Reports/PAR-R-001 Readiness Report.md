## Eval Example

PAR-R-001

## Input Claim

"The deployment is ready and operational coverage is complete."

## Summary

The packet supports partial deployment readiness: the release candidate passed build verification, code review is complete, and a release window is identified. However, the operational coverage portion of the claim is materially unsupported because rollback, monitoring, post-deploy validation, and owner/on-call coverage are missing.

## Evidence Summary

- Deployment note lists the deploy command and planned release window.
- Build verification passed on the release candidate.
- Code review approval is complete.
- Release window note identifies when deployment should occur.
- No known issues are documented.

## Readiness Label

Red

## Rationale

The evidence supports that the candidate has passed build verification and review, but it does not support the broader claim that operational coverage is complete. A deploy command and release window do not demonstrate rollback readiness, monitoring coverage, post-deploy validation, or accountable ownership.

## Supported Claims

- Release candidate build verification passed.
- Code review approval is complete.
- A deployment window has been identified.
- A deploy command is documented.

## Unsupported or Weak Claims

- Operational coverage is complete.
- Deployment is fully ready from an operations standpoint.
- Post-deployment health can be verified.
- Incident response ownership is established.

## Evidence Gaps

- Rollback plan is missing.
- Monitoring plan is missing.
- No post-deploy smoke test is defined.
- No release owner or on-call note is present.

## Risks

- Deployment failure may not have a documented recovery path.
- Post-deploy regressions may go undetected.
- Response ownership may be unclear during or after the release.
- Human reviewers may lack enough operational evidence to treat the claim as ready.

## Next Evidence

- Document rollback steps and rollback decision criteria.
- Provide monitoring checks or dashboards for the release.
- Define post-deploy smoke tests.
- Identify release owner and on-call coverage.

## Human Review Note

Human review is needed before treating the readiness claim as supported. This report recommends a Red label based only on the provided packet evidence.
