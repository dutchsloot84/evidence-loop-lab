# Sample Readiness Report

This sample is fully synthetic and generic. It does not refer to real companies, customers, employees, repositories, tickets, links, exact titles, or sensitive context.

## Release Readiness Report

### Eval Example

- Example ID: synthetic-yellow-001
- Release type: Feature release
- Claimed or desired decision: Ready to release after final approval
- Expected readiness label: Yellow

### Input Claim

> The feature update is ready to release because the main implementation is complete, automated checks passed, and a product stakeholder reviewed the workflow. Only final approval is needed.

### Evidence Summary

- Strong evidence:
  - Main implementation work is marked complete in the synthetic release packet.
  - Automated unit and integration checks passed for the primary workflow.
  - A product stakeholder completed a review of the happy-path experience.
- Weak or partial evidence:
  - Manual QA covered only the primary workflow and one common alternate path.
  - Regression coverage for adjacent workflows is listed as planned but not complete.
  - The rollback plan is described only as "revert if needed" with no owner, timing expectation, or validation steps.
- Known issues:
  - A minor display issue remains open and is believed to be cosmetic, but no impact note confirms whether it affects accessibility or user comprehension.

### Readiness Label

Yellow

### Rationale

The claim is partially supported because core implementation evidence and automated checks exist, and the happy-path review gives useful confidence. However, the evidence does not fully support "ready to release" because QA is incomplete, rollback ownership is ambiguous, and the known issue has not been tied to a clear impact assessment. This looks potentially releasable after human review, but the report should not treat the available evidence as enough for an autonomous ship recommendation.

### Supported Claims

- The main implementation appears complete based on the synthetic packet.
- The primary workflow has passing automated test evidence.
- A stakeholder reviewed the happy-path experience.

### Unsupported or Weak Claims

- "Ready to release" is stronger than the current QA and rollback evidence supports.
- The stakeholder review does not prove full release readiness because it covered only the happy path.
- The known issue is described as cosmetic, but that claim is weak without an impact note.
- Final approval is not the only remaining need because validation and ownership gaps remain.

### Evidence Gaps

- Complete manual QA results for regression and adjacent workflows.
- Explicit rollback plan with owner, trigger conditions, steps, and validation checks.
- Impact assessment for the open display issue.
- Named owner for release-day monitoring and issue triage.
- Confirmation that acceptance criteria map to completed test coverage.

### Risks

- Adjacent workflow regression may be missed if QA remains incomplete.
- Rollback may be delayed or improvised because ownership and steps are unclear.
- The open display issue may have user-impact or accessibility implications that are not yet understood.
- Human approvers may over-trust passing automated checks without seeing the validation gaps.

### Next Evidence

- Completed QA checklist covering primary, alternate, and adjacent workflows.
- Rollback note with assigned owner, decision triggers, execution steps, and post-rollback validation.
- Short impact note for the open display issue, including whether it affects accessibility or comprehension.
- Monitoring and triage owner for the first release window.
- Evidence map showing which acceptance criteria are covered by automated or manual validation.

### Human Review Note

Human review is required before release. The reviewer should decide whether the incomplete QA scope, unclear rollback ownership, and unresolved impact note are acceptable for this release window or require more evidence before approval.

### Eval Notes

- Expected label: Yellow
- Actual label: Yellow
- Match: Yes
- Important evidence cited: Passing automated checks, happy-path stakeholder review, incomplete QA, weak rollback plan, unresolved display issue impact.
- Failure mode to watch for: Overstating readiness because some evidence is strong while ignoring rollback and ownership gaps.
- Review note: This is a needs-human-review case, not a red case, because useful evidence exists and no critical contradiction is present.
