## Eval Example

NOISE-R-002

## Input Claim

"The partner integration release is ready for production."

## Summary

The claim is not sufficiently supported. Current evidence shows some implementation readiness, but core production-readiness evidence for an external integration is missing.

## Readiness Label

Red

## Rationale

Production readiness is materially unsupported because there is no end-to-end integration call, no integration smoke test, no production-like payload validation, no monitoring, no rollback or disablement plan, and no owner sign-off for unresolved validation.

## Key Evidence

- Code review is complete.
- Unit tests passed for request payload mapping.
- Sandbox credentials were created.
- Manual integration validation checklist rows are blank.
- Timing pressure is documented but is not readiness evidence.

## Human Review Note

This report does not approve the release. A human owner should review unresolved integration validation gaps before any production decision.
