# Wave 10 ROI Review

## Question

Did the Wave 10 severity-calibrated rerun produce enough value to justify another parallel-generation pass?

## Result

Decision: Yes, but keep the next pass tiny.

Wave 10 produced a high-value diagnosis: the stronger prompt fixed the known operational-readiness misses, but created overcorrection on the Yellow control. That is useful because the remaining problem is now narrower: calibrating the middle band between Yellow and Red.

## ROI Summary

| Dimension | Result |
| --- | --- |
| Speed | Positive. Three workers completed quickly. |
| Quality | Mixed. Two targeted fixes passed, one control failed. |
| Safety | Good. No leakage or authority-boundary issue found. |
| Learning value | High. The failure mode changed from under-severity to over-severity. |
| Reuse value | High. This produces a concrete prompt-calibration pattern for other projects. |

## What This Proves

- Parallel generation can preserve answer-key separation under strict prompts.
- Targeted prompt calibration can fix known severity misses.
- Controls are necessary because a fix can create a new failure mode.

## What This Does Not Prove

- Parallel generation is ready for unattended scoring.
- The prompt is stable across broader examples.
- The loop is safe for real or sensitive release data.

## Next Fix

Revise the worker prompt with a middle-band Yellow rule:

- Yellow applies when meaningful support exists but one unresolved warning needs impact analysis.
- Red applies when the central claim is materially unsupported or required operational controls are missing.
- Blocked applies when evidence directly contradicts readiness or a required gate failed.

Then rerun the same three-example shape once more.
