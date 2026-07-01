## Eval Example

NEW-G-001

## Input Claim

"The feature flag cleanup is ready because validation, rollback, and monitoring are covered."

## Summary

The evidence supports a readiness recommendation of **Green**. Validation, rollback planning, monitoring coverage, and owner scope acceptance are all represented. Remaining gaps appear minor and documentation-oriented.

## Evidence Summary

- Flag diff shows two retired flags removed and one dormant-path default value changed.
- Automated validation passed for enabled, disabled, and default-path behavior.
- Manual smoke testing covered sign-in, workspace load, and the settings panel.
- Rollback note describes restoring the previous flag snapshot and rerunning validation.
- Monitoring note identifies flag-evaluation errors and settings-panel error rate for the first two hours.
- Owner note confirms cleanup scope is acceptable.

## Readiness Label

Green

## Rationale

The central readiness claim is supported by direct evidence across validation, rollback, monitoring, and ownership. The known issue is limited to an internal runbook screenshot showing the old flag name, which does not directly undermine rollout readiness. The missing product narrative is a documentation gap, not a contradiction of the technical readiness evidence.

## Supported Claims

- Validation coverage exists for enabled, disabled, and default behavior.
- Manual smoke coverage includes relevant user flows.
- Rollback approach is described.
- Monitoring signals are identified for the immediate post-rollout window.
- Cleanup scope has owner acceptance.

## Unsupported or Weak Claims

- The evidence does not show that the internal runbook has been updated.
- The product-facing narrative is not separately documented.

## Evidence Gaps

- No separate product narrative is attached.
- Runbook screenshot still references the old flag name.

## Risks

- Operators may be briefly confused by stale runbook imagery.
- Product or support stakeholders may lack a concise narrative if questions arise.

## Next Evidence

- Update the internal runbook screenshot.
- Attach or summarize the product narrative if stakeholder communication is expected.

## Human Review Note

A human reviewer should confirm the documentation gap is acceptable before treating the rollout as ready.
