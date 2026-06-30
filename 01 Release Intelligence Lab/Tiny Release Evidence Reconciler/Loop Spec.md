# Loop Spec

## Loop Name

Tiny Release Evidence Reconciler

## Loop Goal

Turn a release-readiness claim into an evidence-backed readiness report.

## Inputs

- release type
- readiness claim
- evidence sources present
- evidence details
- known issues
- evidence gaps
- claimed or desired decision

## Steps

1. Parse the readiness claim.
2. List the evidence sources.
3. Separate strong evidence from weak evidence.
4. Identify unsupported or overbroad claims.
5. Identify known issues and missing evidence.
6. Assign readiness label: green, yellow, red, or blocked.
7. Write a short rationale.
8. Request the next evidence needed.
9. Produce a markdown report.
10. Compare the result to the expected label and rationale.

## Evidence Strength

Strong evidence:

- automated tests passed
- manual smoke test passed
- regression test passed
- code review approval
- documented rollback plan
- deployment note
- monitoring or alerting note
- data integrity report
- explicit signoff with rationale

Weak or partial evidence:

- stakeholder approval without rationale
- manual shoulder check without scope
- vague QA pass
- incomplete checklist
- known issue marked out of scope without impact explanation
- deployment note without rollback
- tests passed but coverage unclear

Missing or risky evidence:

- unresolved regression
- unclear owner
- no rollback plan
- no monitoring plan
- no customer-impact note when impact is plausible
- test coverage incomplete
- acceptance criteria not mapped to tests
- status claim says ready but evidence says needs review

## Readiness Decision Rules

Green:

Use green only when the core claim is supported by strong evidence and no critical gaps remain.

Yellow:

Use yellow when the release may be viable, but human review is needed because evidence is incomplete, ambiguous, or contains non-blocking known issues.

Red:

Use red when the readiness claim is not supported by the available evidence.

Blocked:

Use blocked when a critical issue, contradiction, or missing approval prevents a safe decision.

## Output Report Sections

The report should include:

- readiness label
- summary
- supported claims
- unsupported or weak claims
- evidence gaps
- risks
- next evidence needed
- human review note

## Evaluation

Each example should have:

- expected readiness label
- expected rationale
- important evidence that should be cited
- failure mode to watch for

The output is successful when:

- the label matches or is defensibly close to expected
- unsupported claims are identified
- the report does not overstate confidence
- next evidence is concrete
- human review boundaries are preserved

