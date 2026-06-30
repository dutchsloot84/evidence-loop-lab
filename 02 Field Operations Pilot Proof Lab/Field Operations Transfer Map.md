# Field Operations Transfer Map

## Purpose

This map explains how the Release Evidence Reconciler pattern transfers into a field-operations pilot-proof loop while keeping the two labs separate.

The shared pattern is:

claim -> evidence -> risk -> next evidence -> report

The field-operations product loop is:

login -> visit capture -> generated summary -> review -> repeat

This file uses only mock, sanitized examples. It should not contain real customer data, internal names, issue IDs, repo names, links, exact field notes, proprietary strategy, or sensitive business context.

## What Transfers

The Release Evidence Reconciler teaches a generic evidence habit:

1. Identify the claim being made.
2. Check the claim against observable evidence.
3. Name what is supported, weak, missing, or contradicted.
4. Assign a readiness or risk label.
5. Request the next evidence needed.
6. Produce a short report that preserves human approval boundaries.

For field-operations pilot proof, the same habit becomes a product-proof loop:

1. A pilot user can log in.
2. The user can capture a mock field visit.
3. The system can generate a useful summary.
4. A human can review the summary against the captured visit.
5. The loop can repeat across multiple sanitized visit shapes.

The transfer is not from release management into a field-operations feature list. The transfer is from evidence discipline into pilot-proof judgment.

## Keep The Labs Separate

### Release Intelligence Lab Learning Goals

The Release Intelligence Lab exists to learn the generic pattern:

- separate readiness claims from evidence
- identify unsupported or overbroad claims
- assign green, yellow, red, or blocked labels
- request concrete next evidence
- evaluate outputs against expected judgments
- turn the loop into a reusable playbook

Its artifacts should stay release-shaped: mock readiness packets, readiness reports, eval examples, scorecards, and failure modes.

### Field Operations Pilot Proof Lab Product-Proof Goals

The Field Operations Pilot Proof Lab exists to prove whether the sacred product loop works in a mock or sanitized setting:

- a user can log in
- a user can capture a visit
- the captured visit is structured enough to summarize
- the generated summary is useful, accurate, and reviewable
- a human can approve, correct, or reject the summary
- the loop can repeat across representative visit shapes

Its artifacts should stay field-operations-shaped: mock visit captures, generated summaries, review rubrics, pilot-proof reports, and repeat-loop scorecards.

## Loop Mapping

| Generic evidence loop | Field-operations pilot loop | Product-proof question |
| --- | --- | --- |
| claim | login | Can the intended pilot user reach the workflow without help? |
| evidence | visit capture | Is there observable, reviewable input from a mock visit? |
| risk | generated summary | Does the summary expose accuracy, completeness, or usefulness risks? |
| next evidence | review | What human correction, approval, or additional capture is needed? |
| report | repeat | Can the loop run again and produce comparable evidence across examples? |

The generic loop produces a readiness report. The field operations loop produces a pilot-proof report: a concise record of what worked, what failed, what needs human review, and what mock example should be tried next.

## Pilot-Proof Claim Types

Use these claim types when writing field-operations-shaped examples:

- Access claim: "A pilot user can log in and reach the visit workflow."
- Capture claim: "A pilot user can record the important details of a field visit."
- Structure claim: "The captured visit contains enough structured information to generate a useful summary."
- Summary claim: "The generated summary accurately reflects the captured visit."
- Review claim: "A human reviewer can quickly approve, correct, or reject the summary."
- Repeat claim: "The workflow remains understandable and useful across multiple visit shapes."
- Boundary claim: "The workflow does not expose or depend on sensitive real-world data."

Each claim should be checked against observable mock evidence, not assumed because the flow sounds plausible.

## Evidence Sources

Use mock or sanitized evidence sources only:

- synthetic login result, such as "mock pilot user reached visit capture screen"
- mock visit form fields, such as location type, visit purpose, observed issue, action taken, follow-up needed
- sanitized free-text visit note with no customer names, employee names, addresses, asset IDs, or exact operational details
- generated summary text from the mock visit
- human review notes that mark accurate, missing, unclear, or invented details
- summary quality rubric score
- repeat-run comparison across several synthetic visits
- failure-mode note when the loop produces weak or risky output

Do not use screenshots, logs, exports, customer records, or real work artifacts unless a sanitation check has explicitly approved them for lab use.

## Readiness And Risk Labels

Reuse the release lab labels, but define them in pilot-proof terms:

| Label | field-operations pilot-proof meaning |
| --- | --- |
| Green | The mock loop supports the claim. The login, capture, summary, and review evidence are coherent, and gaps are minor. |
| Yellow | The loop mostly works, but human review is needed because a summary is incomplete, a capture field is ambiguous, or repeatability is not proven yet. |
| Red | The claim is stronger than the evidence. The mock visit is not captured well enough, the summary misses important details, or review cannot make a confident decision. |
| Blocked | The loop cannot be evaluated safely or meaningfully because required mock evidence is missing, contradictory, unsanitized, or outside the current boundary. |

Risk notes should be plain and specific:

- Accuracy risk: the summary invents, drops, or distorts visit details.
- Completeness risk: the capture misses information needed for review.
- Usability risk: the user can technically complete the flow, but only with confusion or workarounds.
- Repeatability risk: one example works, but the loop has not been tested across varied visit shapes.
- Boundary risk: an example depends on real field-operations data or sensitive context and must be replaced with sanitized mock data.

## First Mock Examples To Create Later

Create these as future artifacts, not in this transfer map:

| Mock example | Claim tested | Expected label | Purpose |
| --- | --- | --- | --- |
| Basic routine visit | A simple visit can be captured and summarized accurately. | Green | Establish the happy path with a short, low-ambiguity visit. |
| Visit with missing follow-up | The generated summary can identify needed next action. | Yellow | Test whether the loop surfaces incomplete capture rather than hiding it. |
| Visit with conflicting note details | Human review can catch a risky or overconfident summary. | Red | Test contradiction handling and reviewer judgment. |
| Unsanitized source attempt | The lab rejects examples that include sensitive details. | Blocked | Protect the boundary before any product-proof work proceeds. |
| Repeat set of three visits | The loop remains useful across varied visit shapes. | Yellow | Test repeatability before claiming pilot readiness. |

All examples should be synthetic. Use generic names like "Mock Site A" or "Pilot User 1" only when a name is needed.

## Human Approval Boundaries

The field-operations pilot-proof loop may recommend a readiness label, but it must not claim authority to approve real pilot readiness.

Human approval is required when:

- any example might contain real customer, employee, asset, location, ticket, repo, link, or business-sensitive context
- a generated summary changes the meaning of the captured visit
- the summary omits a follow-up, risk, or unresolved condition
- the review result would influence real product, customer, pilot, or operational decisions
- the workflow needs access to real systems or real user data
- a claim sounds stronger than the mock evidence supports

The output should say "needs human review" whenever evidence is incomplete, ambiguous, contradictory, or close to the sanitation boundary.

## What Not To Build Yet

Do not build these until the markdown loop produces useful artifacts:

- production dashboard
- database-backed pilot evidence store
- live-data connector
- automated ingestion from external systems
- agent framework for autonomous pilot decisions
- external-facing reports
- production authentication integration
- real workflow instrumentation
- broad architecture for future features
- polished UI before mock examples and rubrics exist

The first useful version can be manual: one mock visit packet, one generated summary, one review note, one readiness label, one next-evidence request, and one pilot-proof report.

## Transfer Output Shape

A field-operations pilot-proof report should include:

- pilot-proof claim
- mock visit evidence used
- generated summary under review
- supported parts of the claim
- unsupported, weak, or invented parts
- readiness or risk label
- next evidence needed
- human review note
- repeat-loop recommendation

## Integration Notes

This map should sit between the Release Evidence Reconciler and a future Field Operations Pilot Proof Lab loop spec.

It should not replace the Release Intelligence Lab artifacts. It should help translate their evidence discipline into field-operations-shaped mock product proof when the project moves from the first release-intelligence sprint into later pilot-proof work.
