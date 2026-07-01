# Wave 13 Model Visible Packets

Synthetic packets for the fresh noisy batch.

These packets are model-visible. They do not include expected labels or scorer-only rationale.

## NOISE-G-001

- Example ID: NOISE-G-001
- Release type: Static copy cleanup
- Readiness claim: "The copy cleanup is ready because the changed strings are validated and rollback is covered."
- Claimed or desired decision: Evaluate whether the stated readiness claim is supported by the evidence.
- Evidence sources present:
  - Copy diff summary
  - Automated snapshot result
  - Manual smoke test
  - Rollback note
  - Monitoring note
  - Content owner approval
- Evidence details:
  - Copy diff summary shows wording changes to help text only; no business logic, routing, or permission strings changed.
  - Automated snapshots passed for desktop and mobile views.
  - Manual smoke test covered sign-in, help drawer open, and account settings load.
  - Rollback note describes restoring the previous string bundle.
  - Monitoring note names client-render errors and help drawer error rate for the first day.
  - Content owner approval confirms wording scope.
  - A stale screenshot in a training draft still shows old wording.
- Known issues:
  - Training draft screenshot is stale.
- Evidence gaps:
  - No separate marketing review is attached.

## NOISE-G-002

- Example ID: NOISE-G-002
- Release type: Dependency patch release
- Readiness claim: "The dependency patch is ready because regression, rollback, and monitoring checks are complete."
- Claimed or desired decision: Evaluate whether the stated readiness claim is supported by the evidence.
- Evidence sources present:
  - Dependency diff summary
  - Automated regression result
  - Manual smoke test
  - Rollback note
  - Monitoring note
  - Technical owner approval
- Evidence details:
  - Dependency diff summary shows one patch-level update for a utility package with no public API change.
  - Automated regression passed for affected parsing and formatting paths.
  - Manual smoke test covered import, export, and settings save.
  - Rollback note says the package lockfile can be restored and regression rerun.
  - Monitoring note names import error rate and export failure rate.
  - Technical owner approval is recorded.
  - A non-blocking lint warning exists in an unrelated sample file.
- Known issues:
  - Unrelated sample lint warning remains.
- Evidence gaps:
  - No product-facing announcement is attached.

## NOISE-Y-001

- Example ID: NOISE-Y-001
- Release type: Notification template update
- Readiness claim: "The notification template update is ready; remaining concerns are only copy polish."
- Claimed or desired decision: Evaluate whether the stated readiness claim is supported by the evidence.
- Evidence sources present:
  - Template render test
  - Manual inbox smoke test
  - Code review approval
  - Copy review note
  - Delivery observation note
- Evidence details:
  - Template render test passed for default and compact layouts.
  - Manual inbox smoke test passed for one mailbox provider.
  - Code review approval is complete.
  - Copy review found two punctuation changes to make.
  - Delivery observation note says a secondary mailbox provider showed delayed preview text twice, but the messages were delivered.
  - A designer comment asks whether the subject line should be shorter, but no owner marked it blocking.
- Known issues:
  - Delayed preview text may be provider-specific or may indicate template compatibility risk; impact is not proven.
- Evidence gaps:
  - No multi-provider inbox sweep.
  - No monitoring note for delayed preview text.
  - No user-impact note for preview delay.

## NOISE-Y-002

- Example ID: NOISE-Y-002
- Release type: Export formatting update
- Readiness claim: "The export formatting update is ready; only cosmetic table alignment remains."
- Claimed or desired decision: Evaluate whether the stated readiness claim is supported by the evidence.
- Evidence sources present:
  - Golden-file test
  - Manual export smoke test
  - Code review approval
  - UI review note
- Evidence details:
  - Golden-file tests passed for standard and empty export cases.
  - Manual export smoke test passed for the primary report type.
  - Code review approval says column ordering was simplified.
  - UI review found cosmetic table alignment differences in a preview screen.
  - One large export produced a warning about truncated optional notes, but the file completed and row counts matched.
- Known issues:
  - Large-export warning may be harmless or may indicate optional-note loss; impact is not proven.
- Evidence gaps:
  - No large-export content comparison.
  - No monitoring note for truncation warnings.
  - No user-impact note for optional notes.

## NOISE-R-001

- Example ID: NOISE-R-001
- Release type: Operational readiness update
- Readiness claim: "The operational readiness package is complete for deployment."
- Claimed or desired decision: Evaluate whether the stated readiness claim is supported by the evidence.
- Evidence sources present:
  - Build verification
  - Deployment command note
  - Code review approval
  - Calendar hold
  - Team chat summary
- Evidence details:
  - Build verification passed on the release candidate.
  - Deployment command note lists the command to run.
  - Code review approval is complete.
  - Calendar hold reserves a release window.
  - Team chat summary says "ops looks fine" but does not list checks.
  - A draft rollback heading exists in a planning note, but no steps are filled in.
- Known issues:
  - None documented.
- Evidence gaps:
  - Rollback steps are missing.
  - Monitoring plan is missing.
  - No post-deploy smoke test is defined.
  - No release owner or on-call note is present.
  - No incident response criteria are documented.

## NOISE-R-002

- Example ID: NOISE-R-002
- Release type: Integration readiness update
- Readiness claim: "The partner integration release is ready for production."
- Claimed or desired decision: Evaluate whether the stated readiness claim is supported by the evidence.
- Evidence sources present:
  - Code review approval
  - Unit test result
  - Sandbox setup note
  - Stakeholder comment
- Evidence details:
  - Code review approval is complete.
  - Unit tests passed for request payload mapping.
  - Sandbox setup note confirms credentials were created but does not show an end-to-end call.
  - Stakeholder comment says the release is important for timing.
  - A manual checklist exists but all integration validation rows are still blank.
- Known issues:
  - None documented.
- Evidence gaps:
  - No integration smoke test.
  - No production-like payload test.
  - No monitoring note.
  - No rollback or disablement plan.
  - No owner sign-off for unresolved integration validation.

## NOISE-B-001

- Example ID: NOISE-B-001
- Release type: Data backfill release
- Readiness claim: "The data backfill is ready after staging validation."
- Claimed or desired decision: Evaluate whether the stated readiness claim is supported by the evidence.
- Evidence sources present:
  - Staging backfill result
  - Row-count check
  - Reversal drill result
  - Code review approval
- Evidence details:
  - Staging backfill completed and row-count checks matched expected totals.
  - Code review approval is complete.
  - Reversal drill failed because restored records duplicated a subset of rows.
  - A note says duplicate rows were "probably test fixture related" but no retest is attached.
  - A dashboard screenshot shows normal staging load after the failed reversal.
- Known issues:
  - Reversal drill failed and has no verified fix.
- Evidence gaps:
  - No successful reversal retest.
  - No mitigation if reversal is needed.
  - No human acceptance of reversal risk.
  - No monitoring thresholds for duplicate records.

## NOISE-B-002

- Example ID: NOISE-B-002
- Release type: Permission migration release
- Readiness claim: "The permission migration is ready because access checks passed in staging."
- Claimed or desired decision: Evaluate whether the stated readiness claim is supported by the evidence.
- Evidence sources present:
  - Staging access check
  - Automated regression result
  - Rollback drill result
  - Security review note
- Evidence details:
  - Staging access checks passed for two standard roles.
  - Automated regression passed before rollback testing.
  - Security review note says the intended permission model is acceptable.
  - Rollback drill failed because one restricted role retained elevated access after restore.
  - A comment says the role is rarely used, but no risk acceptance is attached.
- Known issues:
  - Rollback left a restricted role with elevated access in staging.
- Evidence gaps:
  - No successful rollback retest.
  - No mitigation for elevated-access rollback failure.
  - No human acceptance of security rollback risk.
  - No monitoring or audit query for elevated access after migration.
