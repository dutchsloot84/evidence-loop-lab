## Eval Example

NOISE-Y-002

## Input Claim

"The export formatting update is ready; only cosmetic table alignment remains."

## Summary

The update appears partially ready: core export behavior has supporting evidence, but unresolved risk remains around large-export behavior and possible optional-note truncation.

## Readiness Label

Yellow

## Rationale

The warning is bounded because the file completed and row counts matched, but optional-note loss has not been ruled out. This is partial readiness, not a failed gate.

## Key Evidence

- Golden-file tests passed standard and empty export cases.
- Manual export smoke passed the primary report type.
- Code review found simplified column ordering.
- UI alignment issue appears cosmetic.
- Large export completed with matching row counts but emitted a truncation warning.

## Human Review Note

Human approval should remain required before treating this as fully ready, especially to decide whether optional-note warning risk is acceptable.
