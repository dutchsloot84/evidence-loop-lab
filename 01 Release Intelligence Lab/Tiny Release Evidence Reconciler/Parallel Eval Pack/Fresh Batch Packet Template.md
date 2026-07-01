# Fresh Batch Packet Template

Use this template to create model-visible release packets.

Do not include expected labels or scorer-only rationale in this file.

## Batch Header

```md
# Wave X Model Visible Packets

Synthetic packets for [batch purpose].

These packets are model-visible. They do not include expected labels or scorer-only rationale.
```

## Example Packet

```md
## EXAMPLE-ID

- Example ID: EXAMPLE-ID
- Release type: [release type]
- Readiness claim: "[claim to evaluate]"
- Claimed or desired decision: Evaluate whether the stated readiness claim is supported by the evidence.
- Evidence sources present:
  - [source]
  - [source]
  - [source]
- Evidence details:
  - [direct supporting evidence]
  - [direct supporting evidence]
  - [distractor or ambiguous evidence if this is a noisy batch]
- Known issues:
  - [known issue, or None documented]
- Evidence gaps:
  - [gap]
  - [gap]
```

## Batch Composition Guidance

For a four-example batch:

- one Green control
- one Yellow bounded-risk example
- one Red materially unsupported example
- one Blocked failed-gate example

For a noisy six-to-eight-example batch:

- at least one Green control
- at least one Yellow control
- at least one Red case
- at least one Blocked case
- at least two examples with distracting but non-decisive evidence

## Label Design Notes

Green examples should include:

- strong direct evidence
- rollback or recovery path when relevant
- monitoring or validation signals when relevant
- only minor documentation or communication gaps

Yellow examples should include:

- meaningful supporting evidence
- one bounded unresolved warning or compatibility risk
- missing impact analysis, monitoring, or broader validation
- no failed required gate

Red examples should include:

- partial implementation evidence
- a readiness claim that is broader than the evidence supports
- missing operational controls, validation, owner sign-off, or monitoring
- no direct failed required gate

Blocked examples should include:

- a failed rollback, backout, reversal, migration recovery, security recovery, or required approval gate
- no verified fix, retest, mitigation, or explicit human risk acceptance
- positive forward-path evidence that must not erase the failed gate

## Sanitation Rules

Use only synthetic or sanitized content.

Do not include:

- customer names
- employee names
- internal project names
- repository names
- ticket IDs
- PR links
- exact ticket or PR titles
- proprietary strategy
- sensitive business context
