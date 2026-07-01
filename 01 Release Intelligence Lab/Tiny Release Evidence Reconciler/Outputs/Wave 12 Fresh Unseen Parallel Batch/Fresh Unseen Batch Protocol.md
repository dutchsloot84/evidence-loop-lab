# Wave 12 Fresh Unseen Parallel Batch Protocol

## Purpose

Test whether the v2 worker prompt generalizes beyond the known calibration examples from Waves 9-11.

Wave 11 passed on known calibration cases. Wave 12 uses four fresh synthetic packets:

- one Green
- one Yellow
- one Red
- one Blocked

## Boundary

Generation workers may see only:

- one worker prompt
- one synthetic release packet
- the v2 severity calibration language

Generation workers may not see:

- answer keys
- expected labels
- scoring rubrics
- eval ledgers
- prior reports
- other project files

Scorer-only comparison happens after generation.

## Success Criteria

Minimum useful result:

- 4 reports generated
- 0 answer-key leakage hits
- 0 authority-boundary failures
- Red or Blocked not softened to Green

Promotion-quality result:

- 4 of 4 exact labels
- Green does not over-penalize minor documentation gaps
- Yellow preserves bounded ambiguity
- Red identifies materially unsupported readiness
- Blocked identifies failed required gates
- no scorer-only leakage

## Decision Rule

If Wave 12 produces 4 of 4 exact labels with no leakage, parallel generation can be considered reliable for small supervised synthetic eval expansion.

Do not automate scoring yet.
