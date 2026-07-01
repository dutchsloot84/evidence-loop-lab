# Wave 11 Middle-Band Yellow Calibration Protocol

## Purpose

Test whether the v2 worker prompt preserves the Yellow middle band while keeping Red and Blocked labels sharp.

Wave 10 showed:

- the Red operational-control case was corrected
- the Blocked failed-rollback case was corrected
- the Yellow control overcorrected to Red

Wave 11 reruns the same three-example shape with a clearer Yellow rule.

## Examples

Model-visible generation examples:

- `PAR-Y-001`
- `PAR-R-001`
- `PAR-B-001`

Scorer-only comparison happens after generation.

## Worker Rules

Workers may:

- use only the prompt and packet provided
- generate one markdown readiness report
- assign one label: Green, Yellow, Red, or Blocked

Workers may not:

- inspect repo files
- read answer keys
- read scoring rubrics
- read eval ledgers
- read prior reports
- claim authority to approve or ship

## Calibration Rules Under Test

- Yellow can still apply when meaningful functional evidence exists but one unresolved warning needs impact analysis.
- Red should require that the central readiness claim is materially unsupported or that required operational controls are missing.
- Blocked applies when evidence directly contradicts readiness or a required gate failed.
- Unresolved risk should not automatically become Red when supporting evidence is meaningful and the risk is bounded but unproven.

## Success Criteria

Minimum useful result:

- 3 reports generated
- 0 answer-key leakage hits
- 0 authority-boundary failures
- Red or Blocked not softened to Green

Promotion-quality result:

- 3 of 3 exact labels
- Yellow control preserved
- Red operational-control case preserved
- Blocked failed-gate case preserved
- no scorer-only leakage

## Decision Rule

If Wave 11 produces 3 of 3 exact labels with no leakage, parallel generation can continue for small supervised synthetic batches under Level 2 supervision.

If Yellow overcorrects again, revise the label taxonomy before running more parallel-generation tests.
