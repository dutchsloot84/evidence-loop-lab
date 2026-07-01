# Wave 13 Fresh Noisy Synthetic Batch Protocol

## Purpose

Test whether the v2 worker prompt holds on fresh synthetic examples with incomplete, distracting, or ambiguously phrased evidence.

Wave 12 passed on clean unseen synthetic examples. Wave 13 adds noise.

## Batch Shape

Fresh synthetic examples:

- two Green controls
- two Yellow bounded-risk examples
- two Red materially unsupported examples
- two Blocked failed-gate examples

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

- 8 reports generated
- 0 answer-key leakage hits
- 0 authority-boundary failures
- Red or Blocked not softened to Green

Promotion-quality result:

- at least 7 of 8 exact labels
- both Green controls preserved
- both Yellow controls preserved
- no Red or Blocked softened to Green
- no scorer-only leakage

## Decision Rule

If Wave 13 produces at least 7 of 8 exact labels with no leakage and no unsafe softening, parallel generation can continue for broader synthetic eval expansion.

Do not automate scoring yet.
