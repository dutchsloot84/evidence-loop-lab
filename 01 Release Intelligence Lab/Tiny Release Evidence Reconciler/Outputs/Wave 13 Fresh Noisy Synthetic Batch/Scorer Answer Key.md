# Wave 13 Scorer Answer Key

Scorer-only answer key created after generation workers completed.

Do not include this file in model-visible generation prompts.

## Expected Labels

| Example | Expected Label | Rationale |
| --- | --- | --- |
| `NOISE-G-001` | Green | Validation, smoke, rollback, monitoring, and content-owner approval are present; stale screenshot and marketing review gap are minor. |
| `NOISE-G-002` | Green | Regression, smoke, rollback, monitoring, and technical approval are present; unrelated lint and announcement gap are minor. |
| `NOISE-Y-001` | Yellow | Core template evidence exists, but delayed preview text is unresolved bounded compatibility risk. |
| `NOISE-Y-002` | Yellow | Normal export evidence exists, but large-export truncation warning needs impact analysis. |
| `NOISE-R-001` | Red | Operational-readiness claim is materially unsupported because controls are missing despite build/review/calendar evidence. |
| `NOISE-R-002` | Red | Production integration readiness is materially unsupported without end-to-end or production-like validation. |
| `NOISE-B-001` | Blocked | Failed reversal drill is an unresolved required-gate failure for data backfill readiness. |
| `NOISE-B-002` | Blocked | Failed security-relevant rollback leaves elevated access and blocks permission migration readiness. |

## Failure Modes To Watch

- Green controls over-penalized because of distracting documentation gaps.
- Yellow controls escalated to Red despite bounded unresolved risk and meaningful support.
- Red cases softened to Yellow because partial implementation evidence exists.
- Blocked cases softened to Red because forward-path validation exists.
