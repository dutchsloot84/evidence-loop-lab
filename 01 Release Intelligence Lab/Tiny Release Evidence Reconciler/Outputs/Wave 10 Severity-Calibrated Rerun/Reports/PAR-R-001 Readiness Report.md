## Eval Example

PAR-R-001

## Input Claim

"The deployment is ready and operational coverage is complete."

## Summary

The evidence supports partial implementation readiness, but it does not support the claim that operational coverage is complete. Core operational controls are missing.

## Evidence Summary

The packet includes a deployment note with the deploy command and planned release window. Build verification passed on the release candidate, code review approval is complete, and the release window is identified.

## Readiness Label

Red

## Rationale

The deployment has positive build and review evidence, but the operational-readiness claim is materially unsupported. There is no rollback plan, monitoring plan, post-deploy smoke test, release owner, or on-call coverage note.

## Supported Claims

- Release candidate build verification passed.
- Code review approval is complete.
- A deployment command and release window are documented.

## Unsupported or Weak Claims

- Operational coverage is complete.
- The deployment is ready from an operations standpoint.
- Post-deploy validation is prepared.
- Ownership and response coverage are established.

## Evidence Gaps

- Rollback plan is missing.
- Monitoring plan is missing.
- No post-deploy smoke test is defined.
- No release owner or on-call note is present.

## Risks

- Failed deployment may not have a documented recovery path.
- Issues after deployment may go undetected.
- Post-deploy behavior may not be validated.
- Incident ownership may be unclear during or after the release window.

## Next Evidence

- Documented rollback plan.
- Monitoring and alerting plan.
- Defined post-deploy smoke test.
- Named release owner and on-call coverage note.

## Human Review Note

A human reviewer should assess the missing operational controls before treating the readiness claim as ready.
