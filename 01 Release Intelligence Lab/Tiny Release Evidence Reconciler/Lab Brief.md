# Tiny Release Evidence Reconciler

## Lab

Release Intelligence Lab

## Sprint

Sprint 1: Tiny Release Evidence Reconciler

## Purpose

Build a tiny, practical loop that checks a release-readiness claim against observable evidence and produces a markdown readiness report.

The goal is not to build a release platform. The goal is to learn how to:

- separate claims from evidence
- identify unsupported claims
- name risk clearly
- request next evidence
- score outputs against expected judgments
- turn the pattern into a reusable playbook

## Why This Lab First

This lab teaches the most transferable pattern in the project:

claim -> evidence -> risk -> next evidence -> report

It connects directly to:

- release intelligence
- Rovo workflows
- FieldIQ pilot proof
- Codex task loops
- eval design
- agent governance
- teach-back artifacts

## Done Statement

Sprint 1 is done when I can take 20 mock release-readiness packets, run or manually apply a documented evidence-check loop, produce a markdown readiness report for each, score the results against expected outcomes, document failure modes, and explain the loop in a 5-minute teach-back.

## Input

A synthetic release-readiness packet containing:

- readiness claim
- release type
- evidence sources present
- sanitized evidence details
- known issues
- evidence gaps
- desired decision or claimed status

## Output

A markdown readiness report containing:

- readiness label
- supported claims
- unsupported or weak claims
- key risks
- missing evidence
- required next evidence
- human review recommendation

## Readiness Labels

Green:

The claim is supported by strong evidence. Gaps are minor and do not materially change the decision.

Yellow:

The claim is partially supported, but there are unresolved gaps, ambiguous ownership, incomplete validation, or known issues that need human review.

Red:

The claim is stronger than the available evidence. Important validation, approval, rollback, or quality evidence is missing.

Blocked:

The evidence contradicts the claim, a critical issue is unresolved, or a required decision cannot be made safely.

## Source Shapes Used

Two sanitized release shapes informed the mock-data categories:

1. A feature-heavy release with merged work and some validation, but incomplete verification, late regression discovery, and unclear QA ownership. This maps to yellow / needs human review.
2. A platform/security release with strong regression evidence, smoke testing, review approval, staging validation, and no blocking issues. This maps to green / shipped, while still allowing minor follow-up gaps.

These source shapes should not be copied into the eval set. They should be used only to generate synthetic examples.

## Mock Data Categories

The 20-example eval set should include:

- 5 green examples where evidence strongly supports the claim
- 5 yellow examples where evidence is partial and needs human review
- 5 red examples where the claim is stronger than the evidence
- 5 blocked or misleading examples where critical evidence contradicts the claim

Derived patterns:

- complex feature release with incomplete QA
- platform/security release with strong regression evidence
- third-party integration release with cosmetic vs functional ambiguity
- business-logic release with late regression
- data-table or configuration release with backup evidence but missing rollback
- release with stakeholder approval but weak test evidence
- release with tests passed but known issue unresolved
- release with strong engineering evidence but missing monitoring
- release with unclear owners
- release with overconfident readiness claim

## Human Approval Boundary

The loop may recommend a readiness label, but it should not claim authority to ship.

The output should make human review explicit when:

- ownership is unclear
- evidence is incomplete
- a known issue remains unresolved
- rollback is missing or weak
- monitoring is undefined
- customer or user impact is ambiguous
- the claim sounds stronger than the evidence supports

