# Eval Set Plan

## Purpose

Create a 20-example synthetic eval set for release readiness reconciliation.

The eval set should test whether the loop can:

- distinguish claims from evidence
- avoid overtrusting status claims
- identify missing evidence
- assign a defensible readiness label
- request concrete next evidence
- preserve human approval boundaries

## Dataset Shape

Total examples: 20

- 5 green
- 5 yellow
- 5 red
- 5 blocked or misleading

## Example Fields

Each model-visible example should include:

- example ID
- release type
- readiness claim
- claimed or desired decision
- evidence sources present
- evidence details
- known issues
- evidence gaps

The scorer-only answer key should include:

- example ID
- expected readiness label
- expected rationale
- important evidence to cite
- failure mode to watch for

Keep the answer key separate from the model-visible packet file.

## Green Patterns

Use green when strong evidence supports the claim and gaps are minor.

Candidate patterns:

- platform patch with regression tests, smoke tests, review approval, and staging validation
- security fix with vulnerability remediation verified and rollback documented
- configuration update with backup, validation report, and clear owner
- minor feature with acceptance criteria mapped to tests
- dependency upgrade with automated test suite and monitoring note

## Yellow Patterns

Use yellow when the release may be viable but needs human review.

Candidate patterns:

- feature release with incomplete QA checklist
- integration release with cosmetic vs functional ambiguity
- business-logic release with late regression fixed but not broadly retested
- release with stakeholder approval but unclear QA owner
- data-table update with backup evidence but incomplete rollback detail

## Red Patterns

Use red when the claim is stronger than the evidence.

Candidate patterns:

- ready claim with only PR summaries and no test evidence
- rollout claim with unresolved known issue affecting core path
- release notes claim broad compatibility but one key platform is untested
- approval exists but acceptance criteria are not mapped to validation
- deployment note exists but rollback and monitoring are missing

## Blocked or Misleading Patterns

Use blocked when evidence contradicts the claim or a critical decision cannot be made.

Candidate patterns:

- critical regression remains open
- test results failed on the core workflow
- owner is missing for required signoff
- rollback failed in staging
- release is claimed ready but evidence says several core items remain in backlog

## Sanitation Rule

The eval set must be synthetic.

Do not include:

- customer names
- employee names
- internal project names
- repo names
- ticket IDs
- PR links
- exact ticket or PR titles
- proprietary strategy
- sensitive business context
