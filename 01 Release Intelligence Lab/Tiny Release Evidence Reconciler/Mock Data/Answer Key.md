# Release Packet Answer Key

Scorer-only answer key for `Release Packets.md`.

Do not include this file in model-visible prompt context when evaluating generated readiness reports.

## Answer Key

### REL-G-001

- Expected readiness label: Green
- Expected rationale: Core readiness is supported by regression tests, smoke validation, review approval, staging deployment evidence, rollback documentation, and monitoring. The remaining visual issue is minor and does not materially change the release decision.
- Important evidence to cite:
  - Automated regression suite passed on the release candidate.
  - Smoke testing covered sign-in, primary navigation, create/update flows, and notification delivery.
  - Two reviewers approved the final change set after requested fixes were applied.
  - Staging deployment completed without new errors in the release window.
  - Rollback is documented as a previous package redeploy with validation steps.
  - Monitoring note names the core health dashboard and alert threshold to watch for the first hour.
- Failure mode to watch for: Over-penalizing a minor cosmetic issue despite strong release evidence.

### REL-G-002

- Expected readiness label: Green
- Expected rationale: The claim is supported by direct remediation proof, regression evidence, review approval, and rollback coverage. The hardening follow-up is outside the immediate readiness claim.
- Important evidence to cite:
  - The targeted remediation test reproduced the issue before the fix and passed after the fix.
  - Automated regression suite passed across the affected service boundary.
  - Security verification note confirms the vulnerable path is no longer reachable under the tested conditions.
  - Two reviewers approved the fix and documented why the change is limited in scope.
  - Rollback plan names the previous package version and the verification steps after rollback.
  - Deployment checklist includes staged rollout, alert review, and owner contact.
- Failure mode to watch for: Treating a future hardening follow-up as a blocker for a verified immediate fix.

### REL-G-003

- Expected readiness label: Green
- Expected rationale: Validation, integrity checks, backup evidence, clear ownership, and rollback documentation support the readiness claim. Missing stakeholder narrative is a minor documentation gap for this low-risk configuration update.
- Important evidence to cite:
  - Configuration diff summary shows only the intended flags and thresholds changed.
  - Data integrity report confirms all required rows are present and no duplicate entries were introduced.
  - Backup confirmation was captured before the update.
  - Manual validation covered the default path, opt-in path, and disabled-path behavior.
  - Release owner is named by role and is available during the release window.
  - Rollback note describes restoring the prior configuration snapshot and re-running validation.
- Failure mode to watch for: Requiring stakeholder approval when technical validation and ownership are already sufficient for the claim.

### REL-G-004

- Expected readiness label: Green
- Expected rationale: The readiness claim is well supported because acceptance criteria are mapped to validation, tests passed, smoke testing covered key paths, review is complete, and monitoring is defined. The help-text and attachment gaps are minor.
- Important evidence to cite:
  - Each acceptance criterion maps to at least one automated test or documented manual check.
  - Automated tests passed for the new feature path, permission handling, and disabled state.
  - Manual smoke test covered the primary desktop and mobile flows.
  - Code review approval included confirmation that edge-case handling was reviewed.
  - Release note draft accurately describes the user-visible change.
  - Monitoring note names event counters for feature usage and error rate.
- Failure mode to watch for: Ignoring acceptance-criteria mapping and treating all documentation follow-ups as material gaps.

### REL-G-005

- Expected readiness label: Green
- Expected rationale: The claim is appropriately limited to a no-user-visible-change dependency upgrade and is supported by regression, build, staging, review, monitoring, and rollback evidence. Full benchmarking is not required by the stated claim.
- Important evidence to cite:
  - Dependency change summary identifies the upgraded package class and confirms no feature behavior was intentionally changed.
  - Automated regression suite and build verification passed on the release candidate.
  - Staging smoke test covered the app shell, primary workflow, and background job execution.
  - Review approval confirms lockfile and compatibility notes were checked.
  - Monitoring note identifies startup errors, job failures, and response latency as post-release signals.
  - Rollback note documents reverting to the previous dependency lock state and redeploying.
- Failure mode to watch for: Demanding broad performance proof when the packet includes sufficient scoped validation.

### REL-Y-001

- Expected readiness label: Yellow
- Expected rationale: The release may be viable, but the readiness claim is only partially supported. Core implementation evidence exists, yet QA is incomplete and rollback/monitoring are missing, so human review is needed before release.
- Important evidence to cite:
  - Automated tests passed for the main happy path and permission checks.
  - QA checklist confirms desktop smoke testing but leaves mobile validation and error-state validation unchecked.
  - Code review approval is complete for the implementation changes.
  - Release note draft describes the new workflow and expected user impact.
- Failure mode to watch for: Marking green because some tests passed and review approval exists while ignoring incomplete QA.

### REL-Y-002

- Expected readiness label: Yellow
- Expected rationale: Evidence supports partial readiness, but the claim that only cosmetic issues remain is not fully proven because the intermittent sync delay may be functional. Human review should decide whether more integration validation is required.
- Important evidence to cite:
  - Integration smoke test passed for account connection and initial sync in sandbox.
  - Manual visual review found spacing and label inconsistencies in the connection modal.
  - Partner sandbox note confirms test credentials worked during validation.
  - Code review approval notes retry behavior was reviewed but not load tested.
- Failure mode to watch for: Accepting the packet's "cosmetic only" framing without checking the sync-delay evidence.

### REL-Y-003

- Expected readiness label: Yellow
- Expected rationale: The late regression appears fixed, but validation after the fix is too narrow to support a confident release. Human review is needed because broader regression, monitoring, and rollback evidence are missing.
- Important evidence to cite:
  - A late regression was found in a boundary-condition calculation and fixed.
  - Targeted test for the failed boundary condition now passes.
  - Code review approval confirms the fix is narrow.
  - Manual retest covered the originally failing path and one adjacent path.
- Failure mode to watch for: Treating a targeted pass as equivalent to broad retesting after a late regression.

### REL-Y-004

- Expected readiness label: Yellow
- Expected rationale: Approval and automated tests support some readiness, but ownership and operational evidence are incomplete. The claim should be downgraded to human-review-needed rather than accepted as fully ready.
- Important evidence to cite:
  - Stakeholder approval says the workflow matches the requested behavior but does not describe validation scope.
  - Code review approval is complete.
  - Automated tests passed for the main workflow and permission denial.
  - Draft deployment note lists release steps but does not name the QA owner.
- Failure mode to watch for: Overweighting stakeholder approval as a substitute for QA ownership and release controls.

### REL-Y-005

- Expected readiness label: Yellow
- Expected rationale: Backup and validation evidence are useful, but rollback is underspecified and downstream impact is not proven. The update may be releasable after human review and concrete recovery validation.
- Important evidence to cite:
  - Backup confirmation was captured before the update.
  - Row-count validation matches the expected number of active records.
  - Spot checks passed for five representative rows.
  - Change summary describes added, updated, and removed rows in generic categories.
  - Release owner is named by role for the release window.
- Failure mode to watch for: Treating backup existence as a complete rollback plan.

### REL-R-001

- Expected readiness label: Red
- Expected rationale: The claim is much stronger than the evidence. Merge descriptions and release notes are not enough to establish readiness without test, review, rollback, or monitoring evidence.
- Important evidence to cite:
  - Merge summary says all planned implementation changes were merged.
  - Pull request description summaries describe intended behavior but do not include validation results.
  - Release note draft describes the feature as available to all users.
- Failure mode to watch for: Confusing merged implementation work with release readiness.

### REL-R-002

- Expected readiness label: Red
- Expected rationale: Although some engineering evidence exists, an unresolved issue affects an optional workflow segment and the packet does not justify releasing to all users. This is red because the broad rollout claim is unsupported, but the packet does not show a direct critical-path contradiction that would make it blocked.
- Important evidence to cite:
  - Automated tests passed for setup and read-only workflow paths.
  - Code review approval is complete.
  - Deployment note describes the rollout steps.
- Failure mode to watch for: Downplaying a known workflow issue because unrelated tests passed, or over-escalating to blocked without a direct critical-path contradiction.

### REL-R-003

- Expected readiness label: Red
- Expected rationale: The broad compatibility claim is not supported because key platforms are untested. Evidence supports only limited platform readiness, not the stated release scope.
- Important evidence to cite:
  - Automated tests passed in the default environment.
  - Desktop smoke testing passed on the primary supported platform.
  - Code review approval is complete.
  - Release note draft claims support across desktop, tablet, and mobile web.
- Failure mode to watch for: Letting a broad release note claim stand when platform evidence is narrow.

### REL-R-004

- Expected readiness label: Red
- Expected rationale: Approval exists, but acceptance criteria are not validated. The packet does not support a release-ready claim because validation, rollback, and monitoring evidence are missing.
- Important evidence to cite:
  - Stakeholder approval says the process direction is acceptable.
  - Acceptance criteria list has five criteria but none are mapped to tests or manual checks.
  - Code review approval is complete.
  - Deployment note lists timing but not validation steps.
- Failure mode to watch for: Treating approval of direction as approval of readiness.

### REL-R-005

- Expected readiness label: Red
- Expected rationale: The operations-covered claim is unsupported because the packet lacks rollback, monitoring, post-deploy validation, and owner evidence. Build and review evidence alone do not prove operational readiness.
- Important evidence to cite:
  - Deployment note lists the planned release window and deploy command.
  - Build verification passed.
  - Code review approval is complete.
- Failure mode to watch for: Accepting a deployment note as proof that operational controls exist.

### REL-B-001

- Expected readiness label: Blocked
- Expected rationale: A critical issue in the primary workflow contradicts the readiness claim. The release cannot be safely judged ready until the regression is fixed or an explicit mitigation decision is documented.
- Important evidence to cite:
  - Automated tests passed for sign-in and navigation.
  - Known issue log says the primary submit action intermittently fails in staging.
  - Code review approval predates the latest failure report.
  - Release note draft announces the workflow as ready for normal use.
- Failure mode to watch for: Labeling red instead of blocked when evidence directly shows a critical unresolved failure.

### REL-B-002

- Expected readiness label: Blocked
- Expected rationale: The packet claims testing passed, but the evidence says the core path failed. This direct contradiction blocks a safe release decision.
- Important evidence to cite:
  - Test run summary shows the core completion-path test failed on the release candidate.
  - Manual QA note says setup and navigation passed, but completion could not be verified because of the failing test.
  - Code review approval is complete but does not address the failed release-candidate test.
  - Deployment note is drafted but not executed.
- Failure mode to watch for: Summarizing partial QA passes while missing the failed core test.

### REL-B-003

- Expected readiness label: Blocked
- Expected rationale: Technical evidence is positive, but the packet itself identifies a required approval gate with no owner or final signoff. The decision cannot be made safely until the approval boundary is resolved.
- Important evidence to cite:
  - Automated tests passed for the main path.
  - Manual smoke test passed in staging.
  - Draft approval checklist requires release-owner signoff, but the owner field is blank.
  - Deployment note says release cannot proceed without that signoff.
- Failure mode to watch for: Marking yellow because tests passed while ignoring a required missing approval.

### REL-B-004

- Expected readiness label: Blocked
- Expected rationale: Staging validation is not enough because rollback failed in staging. A failed recovery path contradicts operational readiness and blocks a safe release decision.
- Important evidence to cite:
  - Staging validation passed for read and write operations after migration.
  - Automated regression suite passed before the rollback drill.
  - Rollback drill failed because the restored environment did not pass health checks.
  - Code review approval is complete.
- Failure mode to watch for: Overweighting happy-path staging validation and ignoring failed rollback evidence.

### REL-B-005

- Expected readiness label: Blocked
- Expected rationale: The readiness claim is misleading because evidence shows core items remain incomplete while release notes claim they are included. The packet needs a scope decision before readiness can be evaluated.
- Important evidence to cite:
  - Release checklist marks the bundle as ready.
  - Backlog status summary shows three core items still in "not started" or "in progress" status.
  - Automated tests passed only for the completed subset.
  - Release note draft describes all core items as included.
- Failure mode to watch for: Marking red for weak evidence without recognizing the explicit contradiction between claimed scope and backlog evidence.
