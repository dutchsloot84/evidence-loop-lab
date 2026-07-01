# Wave 11 ROI Review

## Question

Did the middle-band Yellow calibration produce enough value to justify using parallel generation again?

## Result

Decision: Yes, for small supervised synthetic batches.

Wave 11 produced the cleanest parallel-generation result so far. It fixed the Wave 10 overcorrection while preserving the Red and Blocked corrections from Wave 10.

## ROI Summary

| Dimension | Result |
| --- | --- |
| Speed | Positive. Three workers completed quickly. |
| Quality | Strong for this slice. Three exact labels. |
| Safety | Strong. No leakage or authority-boundary issue found. |
| Learning value | High. The label taxonomy now has a usable middle-band rule. |
| Reuse value | High. This creates a transferable prompt-calibration pattern. |

## What This Proves

- The v2 prompt can preserve Yellow without softening Red or Blocked on known calibration cases.
- Parallel workers can preserve answer-key separation under strict model-visible prompts.
- A control example is necessary to catch overcorrection.

## What This Does Not Prove

- The prompt generalizes to new unseen examples.
- Parallel generation is ready for unattended scoring.
- The loop is safe for real or sensitive release data.

## Next Fix

Move from known calibration examples to a fresh unseen synthetic batch:

- one Green example
- one Yellow bounded-risk example
- one Red missing-operational-controls example
- one Blocked failed-gate example

Keep main-thread scoring and leakage audit required.
