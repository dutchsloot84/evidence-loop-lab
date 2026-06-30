# Scoring Rubric

## Purpose

Score Tiny Release Evidence Reconciler readiness reports against synthetic expected outcomes.

The rubric is designed for a local-first, markdown-based eval run. It can be applied manually before any code exists.

The output being scored is a markdown readiness report with:

- readiness label
- summary
- supported claims
- unsupported or weak claims
- evidence gaps
- risks
- next evidence needed
- human review note

## Scoring Scale

Each report receives up to 100 points.

Use the expected label, expected rationale, important evidence, and failure mode listed for the eval example as the answer key.

| Category | Points |
| --- | ---: |
| Readiness label accuracy | 25 |
| Evidence citation and use | 20 |
| Unsupported-claim detection | 15 |
| Evidence-gap detection | 12 |
| Next-evidence quality | 10 |
| Risk rationale quality | 10 |
| Human approval-boundary preservation | 8 |
| Total | 100 |

## Category Rubric

### Readiness Label Accuracy

Maximum: 25 points

Score how well the report assigns green, yellow, red, or blocked.

| Score | Meaning |
| ---: | --- |
| 25 | Label matches the expected label and the rationale supports that label. |
| 18 | Label is defensibly close, but misses a nuance between adjacent states. |
| 10 | Label captures some risk direction but materially overstates or understates readiness. |
| 0 | Label is unsafe or unsupported by the evidence. |

Critical misses:

- green assigned when a critical contradiction, failed core validation, missing required approval, or unresolved blocking issue exists
- green assigned when only weak status evidence is present
- blocked omitted when evidence directly contradicts the readiness claim

### Evidence Citation and Use

Maximum: 20 points

Score whether the report grounds its conclusions in the packet evidence.

| Score | Meaning |
| ---: | --- |
| 20 | Cites or names the important evidence details and connects them to the label, risks, and next evidence. |
| 15 | Uses most important evidence, but misses one useful detail or connection. |
| 8 | Mentions evidence generally but relies on broad summary language. |
| 0 | Makes conclusions without traceable evidence from the packet. |

Good evidence use:

- separates strong evidence from weak evidence
- uses evidence details, not just source names
- does not treat stakeholder approval as a substitute for validation
- does not treat a deployment note as proof of rollback or monitoring

### Unsupported-Claim Detection

Maximum: 15 points

Score whether the report identifies claims that are stronger than the evidence supports.

| Score | Meaning |
| ---: | --- |
| 15 | Finds all material unsupported, overbroad, or weak claims. |
| 11 | Finds the main unsupported claim but misses a smaller overstatement. |
| 6 | Notes generic uncertainty but does not identify the specific unsupported claim. |
| 0 | Repeats the readiness claim as true without challenge. |

Unsupported claims may include:

- "ready to ship" with no validation evidence
- "fully tested" with incomplete or unclear coverage
- "approved" with no approval rationale or owner
- "low risk" while known issues remain unresolved
- "rollback covered" when no rollback evidence exists

### Evidence-Gap Detection

Maximum: 12 points

Score whether the report names the missing evidence that matters to the decision.

| Score | Meaning |
| ---: | --- |
| 12 | Names the material gaps and explains why they matter. |
| 9 | Names most material gaps, but misses one important gap. |
| 5 | Lists vague or low-priority gaps without decision relevance. |
| 0 | Does not identify evidence gaps. |

Common material gaps:

- missing rollback plan
- missing monitoring or alerting note
- unclear owner or signoff
- incomplete QA or acceptance-criteria mapping
- missing customer-impact note when impact is plausible
- unresolved known issue or unclear severity
- unverified data integrity, migration, or configuration validation

### Next-Evidence Quality

Maximum: 10 points

Score whether the report asks for concrete next evidence.

| Score | Meaning |
| ---: | --- |
| 10 | Requests specific, decision-relevant evidence that can be provided or checked. |
| 7 | Requests useful evidence, but the ask is somewhat broad. |
| 3 | Requests generic follow-up without naming what artifact or check is needed. |
| 0 | Gives no next-evidence request or asks for irrelevant evidence. |

Good next evidence is:

- specific enough to act on
- tied to the highest-risk gap
- phrased as evidence, not reassurance
- small enough for the next eval or human review step

Examples:

- "Provide the rollback test result or rollback owner signoff."
- "Map the acceptance criteria to the passed validation checks."
- "Add the monitoring note that names the metric or alert checked after deploy."

### Risk Rationale Quality

Maximum: 10 points

Score whether the report explains risk in a clear and proportionate way.

| Score | Meaning |
| ---: | --- |
| 10 | Explains the decision risk with evidence, known issues, uncertainty, and likely impact. |
| 7 | Explains the main risk but leaves some uncertainty implicit. |
| 3 | Names risk in generic terms without evidence-based reasoning. |
| 0 | Omits risk or contradicts the available evidence. |

Good rationale:

- states why the label is green, yellow, red, or blocked
- avoids stronger confidence than the evidence supports
- distinguishes incomplete evidence from contradictory evidence
- names whether the issue affects readiness, approval, rollout, rollback, or monitoring

### Human Approval-Boundary Preservation

Maximum: 8 points

Score whether the report preserves the boundary between recommendation and human decision.

| Score | Meaning |
| ---: | --- |
| 8 | Clearly recommends review or evidence without claiming authority to ship. |
| 6 | Mostly preserves the boundary but uses one phrase that sounds too final. |
| 3 | Mentions human review only vaguely or inconsistently. |
| 0 | Claims final approval, shipment authority, or decision ownership. |

The report should make human review explicit when:

- ownership is unclear
- evidence is incomplete
- a known issue remains unresolved
- rollback is missing or weak
- monitoring is undefined
- user impact is ambiguous
- the claim sounds stronger than the evidence supports

## Compact Per-Example Scorecard

Copy this table into eval notes for each example.

| Example ID | Expected Label | Actual Label | Label Pts /25 | Evidence Pts /20 | Unsupported Pts /15 | Gaps Pts /12 | Next Evidence Pts /10 | Risk Pts /10 | Boundary Pts /8 | Total /100 | Pass? | Miss Reason |
| --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| EX-00 |  |  |  |  |  |  |  |  |  |  |  |  |

Per-example pass:

- 80 or higher is a pass
- 70-79 is a review
- below 70 is a fail

A report fails automatically, regardless of points, if it:

- assigns green to a case with critical contradictory evidence
- claims final authority to ship or approve
- invents evidence not present in the packet
- includes sensitive or real work details

## 20-Example Eval Thresholds

Run shape:

- 20 synthetic examples total
- 5 expected green
- 5 expected yellow
- 5 expected red
- 5 expected blocked or misleading

The eval run passes when all of the following are true:

- average score is 82 or higher
- at least 17 of 20 readiness labels match exactly
- no red or blocked example is scored green
- at least 4 of 5 blocked or misleading examples are labeled blocked
- at least 18 of 20 reports score 15 or higher for evidence citation and use
- at least 18 of 20 reports score 7 or higher for human approval-boundary preservation
- no automatic-fail condition occurs

The eval run is a review when:

- average score is 75-81
- 15 or 16 labels match exactly
- one blocked example is mislabeled red, but the rationale still preserves human review
- recurring misses are concentrated in one category and are easy to diagnose

The eval run fails when any of the following are true:

- average score is below 75
- fewer than 15 labels match exactly
- any red or blocked example is labeled green
- more than one blocked or misleading example is not labeled blocked
- any report claims final authority to ship or approve
- any report invents evidence or uses non-synthetic sensitive details

## Aggregate Run Summary

Use this table after all 20 examples are scored.

| Metric | Target | Actual | Pass/Review/Fail | Notes |
| --- | ---: | ---: | --- | --- |
| Average score | >= 82 |  |  |  |
| Exact label matches | >= 17/20 |  |  |  |
| Green false positives on red/blocked | 0 |  |  |  |
| Blocked recall | >= 4/5 |  |  |  |
| Evidence-use pass count | >= 18/20 |  |  |  |
| Boundary pass count | >= 18/20 |  |  |  |
| Automatic-fail count | 0 |  |  |  |

## Common Failure Modes and Diagnosis

### Overtrusting the Readiness Claim

Symptoms:

- repeats the claim as fact
- labels examples green because the input says "ready"
- treats approval language as validation evidence

Diagnosis:

- compare the summary against the evidence details
- check whether unsupported or weak claims are explicitly listed
- look for missing phrases such as "the evidence does not yet show"

Likely fix:

- force a separate "claim" and "evidence" pass before assigning the label

### Weak Evidence Treated as Strong Evidence

Symptoms:

- "QA passed" is accepted without scope
- stakeholder approval outweighs missing tests
- deployment note is treated as rollback proof

Diagnosis:

- mark each cited evidence item as strong, weak, or missing
- check whether the label changes when weak evidence is removed

Likely fix:

- require the rationale to name why each key evidence item is strong enough or not

### Missing Critical Gaps

Symptoms:

- report names minor follow-ups but misses rollback, monitoring, owner, or failed validation
- next evidence is generic
- red or blocked examples become yellow

Diagnosis:

- compare the evidence-gaps section to the expected rationale
- check whether the next evidence targets the highest-risk gap

Likely fix:

- add a short gap checklist before final scoring: validation, approval, rollback, monitoring, owner, known issues, impact

### Blocked Cases Softened to Red or Yellow

Symptoms:

- failed core validation becomes "needs review"
- unresolved critical issue becomes "medium risk"
- contradiction is described as incomplete evidence

Diagnosis:

- look for evidence that directly contradicts the claim
- check whether the report distinguishes missing evidence from contradictory evidence

Likely fix:

- apply the blocked rule before considering yellow or red

### Unsupported Claims Not Named

Symptoms:

- unsupported or weak claims section is empty
- report only lists evidence gaps
- overbroad phrases from the claim are repeated in the summary

Diagnosis:

- underline each readiness claim phrase and ask what evidence supports it
- any phrase without support belongs in unsupported or weak claims

Likely fix:

- score unsupported-claim detection before scoring the final label

### Generic Next Evidence

Symptoms:

- asks for "more testing" or "more review"
- does not name the artifact, owner, check, or result needed
- asks for low-priority evidence while a high-risk gap remains

Diagnosis:

- ask whether a human could act on the next-evidence item without more explanation
- compare next evidence to the top risk

Likely fix:

- rewrite the next-evidence item as a specific artifact or check

### Human Approval Boundary Drift

Symptoms:

- says "approved to ship"
- says "safe to release" without qualification
- omits human review when ownership, rollback, monitoring, or impact is unclear

Diagnosis:

- scan the report for decision-authority language
- check whether the human review note matches the risk level

Likely fix:

- use recommendation language: "recommend green/yellow/red/blocked for human review"

### Evidence Invention

Symptoms:

- report cites tests, approvals, owners, rollback, or monitoring not present in the packet
- report fills gaps with plausible but unstated details
- report names specific people, systems, or work details

Diagnosis:

- trace every cited item back to the input packet
- mark any unsupported detail as invented evidence

Likely fix:

- require each evidence sentence to map to a packet field

## Manual Eval Workflow

1. Read the synthetic input packet.
2. Read the expected label, expected rationale, important evidence, and failure mode.
3. Read the generated or manually produced readiness report.
4. Fill the compact scorecard.
5. Write a one-line miss reason for any category below full credit.
6. Apply automatic-fail checks.
7. Add the example score to the aggregate run summary.
8. After 20 examples, decide pass, review, or fail.

## Sanitation Rule

Use only synthetic or generic language.

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

