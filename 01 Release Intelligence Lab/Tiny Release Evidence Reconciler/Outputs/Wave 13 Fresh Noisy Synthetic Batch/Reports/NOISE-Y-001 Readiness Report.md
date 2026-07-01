## Eval Example

NOISE-Y-001

## Input Claim

"The notification template update is ready; remaining concerns are only copy polish."

## Summary

The update shows partial readiness, but the claim overstates readiness because there is unresolved provider-specific preview-text behavior and missing broader validation.

## Readiness Label

Yellow

## Rationale

The core template appears functional and reviewed, but delayed preview text on a secondary provider creates bounded compatibility risk. The impact is unproven, so the concern is not only copy polish.

## Key Evidence

- Template render testing passed for default and compact layouts.
- Manual inbox smoke passed for one mailbox provider.
- Code review is complete.
- Copy issues appear minor.
- Secondary provider delayed preview text occurred twice, though messages delivered.

## Human Review Note

A human reviewer should decide whether the preview-text risk is acceptable before treating the update as ready.
