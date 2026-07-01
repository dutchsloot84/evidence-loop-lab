# Wave 12 Scorer Answer Key

Scorer-only answer key created after generation workers completed.

Do not include this file in model-visible generation prompts.

## NEW-G-001

- Expected readiness label: Green
- Expected rationale: The feature flag cleanup has direct evidence for scoped changes, validation, manual smoke coverage, rollback, monitoring, and owner approval. The stale screenshot and missing product narrative are minor documentation gaps.
- Failure mode to watch for: Over-penalizing minor documentation gaps despite complete readiness evidence.

## NEW-Y-001

- Expected readiness label: Yellow
- Expected rationale: The API behavior update has meaningful test and review evidence, but the claim that only documentation polish remains is not fully supported because a secondary-client fallback warning has unresolved impact.
- Failure mode to watch for: Escalating bounded unresolved ambiguity to Red despite meaningful supporting validation, or accepting the documentation-only framing as Green.

## NEW-R-001

- Expected readiness label: Red
- Expected rationale: Build, review, deploy command, and calendar evidence exist, but operational readiness is materially unsupported because rollback, monitoring, post-deploy validation, ownership, and incident response criteria are missing.
- Failure mode to watch for: Marking Yellow because partial release-preparation evidence exists while underweighting missing operational controls.

## NEW-B-001

- Expected readiness label: Blocked
- Expected rationale: The schema migration has staging, regression, integrity, and review evidence, but the failed backout drill directly contradicts readiness for a migration release until fixed, retested, mitigated, or explicitly accepted.
- Failure mode to watch for: Marking Red instead of Blocked when a required recovery gate failed.
