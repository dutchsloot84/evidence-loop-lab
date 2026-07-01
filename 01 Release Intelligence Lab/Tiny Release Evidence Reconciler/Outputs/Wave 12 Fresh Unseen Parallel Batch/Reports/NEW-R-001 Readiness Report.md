## Eval Example

NEW-R-001

## Input Claim

"The service deployment is ready and operational readiness is complete."

## Summary

The evidence supports partial release preparation, including build verification, deployment scheduling, and code review approval. However, the operational readiness claim is materially unsupported because key operational controls are missing.

## Evidence Summary

- Build verification passed on the release candidate.
- Deployment command note lists the intended release-window command.
- Code review approval is complete.
- Release calendar entry reserves a deployment window.
- No known issues are documented.

## Readiness Label

Red

## Rationale

The packet shows the release candidate has passed build verification and has received code review approval, but operational readiness requires more than a deploy command and scheduled window. Missing rollback, monitoring, post-deploy validation, ownership, on-call, and incident response criteria leave the central readiness claim unsupported.

## Supported Claims

- The release candidate passed build verification.
- Code review approval is complete.
- A deployment window has been reserved.
- A deployment command has been identified for the release window.

## Unsupported or Weak Claims

- Operational readiness is complete.
- The deployment is ready to proceed without further review.
- Rollback, monitoring, validation, ownership, and incident response coverage are in place.

## Evidence Gaps

- Rollback plan is missing.
- Monitoring plan is missing.
- No post-deploy smoke test is defined.
- No release owner, support owner, or on-call note is present.
- No incident response criteria are documented.

## Risks

- Failed deployment may not have a defined recovery path.
- Production issues may go undetected without monitoring coverage.
- Post-deploy behavior may not be validated.
- Ownership gaps may delay response during the release window.
- Incident handling may be inconsistent without documented criteria.

## Next Evidence

- Document rollback plan and validation steps.
- Define monitoring checks for the release.
- Add post-deploy smoke test criteria.
- Identify release owner, support owner, and on-call coverage.
- Document incident response triggers and escalation criteria.

## Human Review Note

A human reviewer should assess the missing operational controls before treating the deployment readiness claim as ready.
