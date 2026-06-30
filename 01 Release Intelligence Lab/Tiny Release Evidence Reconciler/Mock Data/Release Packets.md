# Release Packets

Synthetic eval dataset for the [[Tiny Release Evidence Reconciler]].

Use these examples to test whether the loop can separate readiness claims from evidence, identify unsupported confidence, assign a defensible readiness label, and request concrete next evidence. All names, identifiers, owners, systems, and release details are generic and synthetic.

## Label Balance

- Green: 5 examples
- Yellow: 5 examples
- Red: 5 examples
- Blocked: 5 examples

## Green Examples

### Example REL-G-001

- Example ID: REL-G-001
- Release type: Platform patch
- Readiness claim: "The platform patch is ready for release after staging validation."
- Claimed or desired decision: Evaluate whether the stated readiness claim is supported by the evidence.
- Evidence sources present:
  - Automated regression suite
  - Manual smoke test checklist
  - Code review approval
  - Staging deployment note
  - Rollback note
  - Monitoring note
- Evidence details:
  - Automated regression suite passed on the release candidate.
  - Smoke testing covered sign-in, primary navigation, create/update flows, and notification delivery.
  - Two reviewers approved the final change set after requested fixes were applied.
  - Staging deployment completed without new errors in the release window.
  - Rollback is documented as a previous package redeploy with validation steps.
  - Monitoring note names the core health dashboard and alert threshold to watch for the first hour.
- Known issues:
  - One low-priority visual alignment issue remains in a secondary settings view.
- Evidence gaps:
  - Post-release owner rotation is noted but not scheduled in detail.

### Example REL-G-002

- Example ID: REL-G-002
- Release type: Security fix
- Readiness claim: "The security fix is ready to ship with verified remediation and rollback coverage."
- Claimed or desired decision: Evaluate whether the stated readiness claim is supported by the evidence.
- Evidence sources present:
  - Targeted remediation test
  - Automated regression suite
  - Security verification note
  - Code review approval
  - Rollback note
  - Deployment checklist
- Evidence details:
  - The targeted remediation test reproduced the issue before the fix and passed after the fix.
  - Automated regression suite passed across the affected service boundary.
  - Security verification note confirms the vulnerable path is no longer reachable under the tested conditions.
  - Two reviewers approved the fix and documented why the change is limited in scope.
  - Rollback plan names the previous package version and the verification steps after rollback.
  - Deployment checklist includes staged rollout, alert review, and owner contact.
- Known issues:
  - None documented.
- Evidence gaps:
  - Long-term hardening follow-up is not included in the release packet.

### Example REL-G-003

- Example ID: REL-G-003
- Release type: Configuration update
- Readiness claim: "The configuration update is ready because validation passed and recovery is documented."
- Claimed or desired decision: Evaluate whether the stated readiness claim is supported by the evidence.
- Evidence sources present:
  - Configuration diff summary
  - Data integrity report
  - Backup confirmation
  - Manual validation checklist
  - Named release owner
  - Rollback note
- Evidence details:
  - Configuration diff summary shows only the intended flags and thresholds changed.
  - Data integrity report confirms all required rows are present and no duplicate entries were introduced.
  - Backup confirmation was captured before the update.
  - Manual validation covered the default path, opt-in path, and disabled-path behavior.
  - Release owner is named by role and is available during the release window.
  - Rollback note describes restoring the prior configuration snapshot and re-running validation.
- Known issues:
  - None documented.
- Evidence gaps:
  - No separate stakeholder narrative is attached.

### Example REL-G-004

- Example ID: REL-G-004
- Release type: Minor feature
- Readiness claim: "The minor feature is ready for general availability."
- Claimed or desired decision: Evaluate whether the stated readiness claim is supported by the evidence.
- Evidence sources present:
  - Acceptance criteria checklist
  - Automated test mapping
  - Manual smoke test
  - Code review approval
  - Release note draft
  - Monitoring note
- Evidence details:
  - Each acceptance criterion maps to at least one automated test or documented manual check.
  - Automated tests passed for the new feature path, permission handling, and disabled state.
  - Manual smoke test covered the primary desktop and mobile flows.
  - Code review approval included confirmation that edge-case handling was reviewed.
  - Release note draft accurately describes the user-visible change.
  - Monitoring note names event counters for feature usage and error rate.
- Known issues:
  - One help-text improvement is scheduled for a later documentation update.
- Evidence gaps:
  - Accessibility review is summarized but not attached as a separate artifact.

### Example REL-G-005

- Example ID: REL-G-005
- Release type: Dependency upgrade
- Readiness claim: "The dependency upgrade is ready for release with no expected user-visible change."
- Claimed or desired decision: Evaluate whether the stated readiness claim is supported by the evidence.
- Evidence sources present:
  - Dependency change summary
  - Automated regression suite
  - Build verification
  - Staging smoke test
  - Code review approval
  - Monitoring note
  - Rollback note
- Evidence details:
  - Dependency change summary identifies the upgraded package class and confirms no feature behavior was intentionally changed.
  - Automated regression suite and build verification passed on the release candidate.
  - Staging smoke test covered the app shell, primary workflow, and background job execution.
  - Review approval confirms lockfile and compatibility notes were checked.
  - Monitoring note identifies startup errors, job failures, and response latency as post-release signals.
  - Rollback note documents reverting to the previous dependency lock state and redeploying.
- Known issues:
  - None documented.
- Evidence gaps:
  - Performance comparison is limited to smoke-level observation, not a full benchmark.

## Yellow Examples

### Example REL-Y-001

- Example ID: REL-Y-001
- Release type: Feature release
- Readiness claim: "The feature release is ready after QA."
- Claimed or desired decision: Evaluate whether the stated readiness claim is supported by the evidence.
- Evidence sources present:
  - Partial QA checklist
  - Automated test summary
  - Code review approval
  - Release note draft
- Evidence details:
  - Automated tests passed for the main happy path and permission checks.
  - QA checklist confirms desktop smoke testing but leaves mobile validation and error-state validation unchecked.
  - Code review approval is complete for the implementation changes.
  - Release note draft describes the new workflow and expected user impact.
- Known issues:
  - A low-frequency error message displays generic text when validation fails.
- Evidence gaps:
  - Mobile validation is not complete.
  - Error-state testing is not complete.
  - Rollback and monitoring notes are missing.

### Example REL-Y-002

- Example ID: REL-Y-002
- Release type: Third-party integration
- Readiness claim: "The integration is ready; only cosmetic issues remain."
- Claimed or desired decision: Evaluate whether the stated readiness claim is supported by the evidence.
- Evidence sources present:
  - Integration smoke test
  - Manual visual review
  - Partner sandbox note
  - Code review approval
- Evidence details:
  - Integration smoke test passed for account connection and initial sync in sandbox.
  - Manual visual review found spacing and label inconsistencies in the connection modal.
  - Partner sandbox note confirms test credentials worked during validation.
  - Code review approval notes retry behavior was reviewed but not load tested.
- Known issues:
  - One intermittent sync delay occurs in sandbox, described as likely non-user-facing but not fully explained.
- Evidence gaps:
  - No production-like sync volume test.
  - No monitoring note for delayed syncs.
  - Cosmetic-vs-functional impact of the intermittent delay is unclear.

### Example REL-Y-003

- Example ID: REL-Y-003
- Release type: Business-logic update
- Readiness claim: "The business-logic update is ready after the late regression fix."
- Claimed or desired decision: Evaluate whether the stated readiness claim is supported by the evidence.
- Evidence sources present:
  - Regression fix note
  - Targeted test result
  - Code review approval
  - Partial manual retest
- Evidence details:
  - A late regression was found in a boundary-condition calculation and fixed.
  - Targeted test for the failed boundary condition now passes.
  - Code review approval confirms the fix is narrow.
  - Manual retest covered the originally failing path and one adjacent path.
- Known issues:
  - No known current failure, but broader affected scenarios were not rerun after the late fix.
- Evidence gaps:
  - Full regression suite was not rerun after the late change.
  - Monitoring note is missing.
  - Rollback note is missing.

### Example REL-Y-004

- Example ID: REL-Y-004
- Release type: Workflow enhancement
- Readiness claim: "The release is approved and ready to ship."
- Claimed or desired decision: Evaluate whether the stated readiness claim is supported by the evidence.
- Evidence sources present:
  - Stakeholder approval note
  - Code review approval
  - Automated test summary
  - Draft deployment note
- Evidence details:
  - Stakeholder approval says the workflow matches the requested behavior but does not describe validation scope.
  - Code review approval is complete.
  - Automated tests passed for the main workflow and permission denial.
  - Draft deployment note lists release steps but does not name the QA owner.
- Known issues:
  - None documented.
- Evidence gaps:
  - QA owner is unclear.
  - No manual smoke test evidence.
  - Rollback note is incomplete.
  - Monitoring note is missing.

### Example REL-Y-005

- Example ID: REL-Y-005
- Release type: Data-table update
- Readiness claim: "The data-table update is ready because the backup was taken and validation passed."
- Claimed or desired decision: Evaluate whether the stated readiness claim is supported by the evidence.
- Evidence sources present:
  - Backup confirmation
  - Row-count validation
  - Spot-check notes
  - Change summary
  - Named release owner
- Evidence details:
  - Backup confirmation was captured before the update.
  - Row-count validation matches the expected number of active records.
  - Spot checks passed for five representative rows.
  - Change summary describes added, updated, and removed rows in generic categories.
  - Release owner is named by role for the release window.
- Known issues:
  - One deprecated row category remains for compatibility, marked as intentionally retained.
- Evidence gaps:
  - Rollback detail says "restore backup if needed" but does not describe verification after restore.
  - No downstream smoke test is attached.
  - Monitoring note is missing.

## Red Examples

### Example REL-R-001

- Example ID: REL-R-001
- Release type: Multi-part feature release
- Readiness claim: "The feature is fully ready for release."
- Claimed or desired decision: Evaluate whether the stated readiness claim is supported by the evidence.
- Evidence sources present:
  - Merge summary
  - Pull request description summaries
  - Release note draft
- Evidence details:
  - Merge summary says all planned implementation changes were merged.
  - Pull request description summaries describe intended behavior but do not include validation results.
  - Release note draft describes the feature as available to all users.
- Known issues:
  - None documented in the packet.
- Evidence gaps:
  - No automated test results.
  - No manual QA evidence.
  - No code review approval evidence.
  - No rollback note.
  - No monitoring note.

### Example REL-R-002

- Example ID: REL-R-002
- Release type: Core workflow rollout
- Readiness claim: "The rollout is ready for all users."
- Claimed or desired decision: Evaluate whether the stated readiness claim is supported by the evidence.
- Evidence sources present:
  - Automated test summary
  - Code review approval
  - Deployment note
- Evidence details:
  - Automated tests passed for setup and read-only workflow paths.
  - Code review approval is complete.
  - Deployment note describes the rollout steps.
- Known issues:
  - An edit-and-save path fails for one optional workflow segment and is marked "to fix after release."
- Evidence gaps:
  - No evidence that the known issue is acceptable for broad rollout.
  - No stakeholder impact note.
  - No rollback plan.
  - No monitoring note.

### Example REL-R-003

- Example ID: REL-R-003
- Release type: Compatibility release
- Readiness claim: "The release is broadly compatible across supported platforms."
- Claimed or desired decision: Evaluate whether the stated readiness claim is supported by the evidence.
- Evidence sources present:
  - Automated test summary
  - Desktop smoke test
  - Code review approval
  - Release note draft
- Evidence details:
  - Automated tests passed in the default environment.
  - Desktop smoke testing passed on the primary supported platform.
  - Code review approval is complete.
  - Release note draft claims support across desktop, tablet, and mobile web.
- Known issues:
  - None documented.
- Evidence gaps:
  - Tablet validation is missing.
  - Mobile web validation is missing.
  - No platform-compatibility matrix is attached.
  - Monitoring note is missing.

### Example REL-R-004

- Example ID: REL-R-004
- Release type: Approval-driven process change
- Readiness claim: "The process change is approved and ready."
- Claimed or desired decision: Evaluate whether the stated readiness claim is supported by the evidence.
- Evidence sources present:
  - Stakeholder approval note
  - Acceptance criteria list
  - Code review approval
  - Deployment note
- Evidence details:
  - Stakeholder approval says the process direction is acceptable.
  - Acceptance criteria list has five criteria but none are mapped to tests or manual checks.
  - Code review approval is complete.
  - Deployment note lists timing but not validation steps.
- Known issues:
  - None documented.
- Evidence gaps:
  - No automated test mapping.
  - No manual validation evidence.
  - No acceptance-criteria verification.
  - No rollback note.
  - No monitoring note.

### Example REL-R-005

- Example ID: REL-R-005
- Release type: Deployment-only release
- Readiness claim: "The deployment is ready; operations are covered."
- Claimed or desired decision: Evaluate whether the stated readiness claim is supported by the evidence.
- Evidence sources present:
  - Deployment note
  - Build verification
  - Code review approval
- Evidence details:
  - Deployment note lists the planned release window and deploy command.
  - Build verification passed.
  - Code review approval is complete.
- Known issues:
  - None documented.
- Evidence gaps:
  - Rollback plan is missing.
  - Monitoring plan is missing.
  - No post-deploy smoke test is defined.
  - No on-call or owner note is present.

## Blocked Examples

### Example REL-B-001

- Example ID: REL-B-001
- Release type: Core workflow release
- Readiness claim: "The release is ready despite one remaining issue."
- Claimed or desired decision: Evaluate whether the stated readiness claim is supported by the evidence.
- Evidence sources present:
  - Automated test summary
  - Known issue log
  - Code review approval
  - Release note draft
- Evidence details:
  - Automated tests passed for sign-in and navigation.
  - Known issue log says the primary submit action intermittently fails in staging.
  - Code review approval predates the latest failure report.
  - Release note draft announces the workflow as ready for normal use.
- Known issues:
  - Critical staging regression remains open for the primary submit action.
- Evidence gaps:
  - No fix verification for the critical regression.
  - No mitigation plan.
  - No rollback plan.
  - No human acceptance of the staging failure.

### Example REL-B-002

- Example ID: REL-B-002
- Release type: Checkout-like workflow update
- Readiness claim: "The workflow update passed testing and is ready."
- Claimed or desired decision: Evaluate whether the stated readiness claim is supported by the evidence.
- Evidence sources present:
  - Test run summary
  - Manual QA note
  - Code review approval
  - Deployment note
- Evidence details:
  - Test run summary shows the core completion-path test failed on the release candidate.
  - Manual QA note says setup and navigation passed, but completion could not be verified because of the failing test.
  - Code review approval is complete but does not address the failed release-candidate test.
  - Deployment note is drafted but not executed.
- Known issues:
  - Core completion path fails in the release-candidate test run.
- Evidence gaps:
  - No passing retest.
  - No workaround.
  - No rollback plan.
  - No decision owner accepted the failure.

### Example REL-B-003

- Example ID: REL-B-003
- Release type: Approval-gated release
- Readiness claim: "The release is ready pending no further action."
- Claimed or desired decision: Evaluate whether the stated readiness claim is supported by the evidence.
- Evidence sources present:
  - Automated test summary
  - Manual smoke test
  - Draft approval checklist
  - Deployment note
- Evidence details:
  - Automated tests passed for the main path.
  - Manual smoke test passed in staging.
  - Draft approval checklist requires release-owner signoff, but the owner field is blank.
  - Deployment note says release cannot proceed without that signoff.
- Known issues:
  - Required release-owner signoff is missing.
- Evidence gaps:
  - No named approval owner.
  - No final approval.
  - No escalation path for missing signoff.

### Example REL-B-004

- Example ID: REL-B-004
- Release type: Infrastructure migration
- Readiness claim: "The migration is ready because staging validation passed."
- Claimed or desired decision: Evaluate whether the stated readiness claim is supported by the evidence.
- Evidence sources present:
  - Staging validation note
  - Rollback drill result
  - Automated regression suite
  - Code review approval
- Evidence details:
  - Staging validation passed for read and write operations after migration.
  - Automated regression suite passed before the rollback drill.
  - Rollback drill failed because the restored environment did not pass health checks.
  - Code review approval is complete.
- Known issues:
  - Rollback failed in staging and has no verified fix.
- Evidence gaps:
  - No successful rollback retest.
  - No operational mitigation if rollback is needed.
  - No human acceptance of rollback risk.
  - Monitoring thresholds are not defined.

### Example REL-B-005

- Example ID: REL-B-005
- Release type: Bundled feature release
- Readiness claim: "All core items are complete and the bundle is ready."
- Claimed or desired decision: Evaluate whether the stated readiness claim is supported by the evidence.
- Evidence sources present:
  - Release checklist
  - Backlog status summary
  - Automated test summary
  - Release note draft
- Evidence details:
  - Release checklist marks the bundle as ready.
  - Backlog status summary shows three core items still in "not started" or "in progress" status.
  - Automated tests passed only for the completed subset.
  - Release note draft describes all core items as included.
- Known issues:
  - Several core items claimed in scope are not complete.
- Evidence gaps:
  - No scope-change approval.
  - No updated release note matching the completed subset.
  - No validation for incomplete core items.
  - No decision owner accepting a reduced scope.
