# Wave 12 ROI Review

## Question

Did the v2 prompt generalize well enough on fresh unseen synthetic examples to justify more small-batch parallel generation?

## Result

Decision: Yes, for small supervised synthetic eval expansion.

Wave 12 produced a clean four-label result on fresh synthetic examples. This is stronger evidence than Wave 11 because the examples were not reused from calibration.

## ROI Summary

| Dimension | Result |
| --- | --- |
| Speed | Positive. Four workers completed quickly. |
| Quality | Strong. Four exact labels. |
| Safety | Strong. No leakage or authority-boundary issue found. |
| Learning value | High. The v2 calibration generalized beyond known cases. |
| Reuse value | High. The prompt can support the next synthetic eval expansion. |

## What This Proves

- The v2 prompt can handle a fresh Green, Yellow, Red, and Blocked batch.
- Parallel generation can preserve answer-key separation under strict setup.
- Controls for Green and Yellow are valuable because they catch over-penalization.

## What This Does Not Prove

- The loop is ready for real or sensitive release data.
- Scoring can be automated.
- The prompt will remain stable on noisy or adversarial examples.

## Next Fix

The next best proof is a fresh noisy synthetic batch:

- use 6-8 examples
- include incomplete, ambiguous, or distracting evidence
- preserve one Green control and one Yellow control
- keep answer-key separation and manual scoring
- record failure modes separately
