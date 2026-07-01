# Wave 13 ROI Review

## Question

Did the v2 prompt hold under noisy synthetic evidence well enough to justify broader supervised synthetic eval expansion?

## Result

Decision: Yes.

Wave 13 passed with eight exact labels across fresh noisy synthetic examples. This is the strongest parallel-generation proof so far because it tested distractors, incomplete evidence, bounded ambiguity, missing controls, and failed gates in the same batch.

## ROI Summary

| Dimension | Result |
| --- | --- |
| Speed | Positive. Eight examples completed in two mini-batches due to thread limits. |
| Quality | Strong. Eight exact labels. |
| Safety | Strong. No leakage or authority-boundary issue found. |
| Learning value | High. The v2 prompt held under noisy evidence. |
| Reuse value | High. This supports broader synthetic eval expansion and future playbook reuse. |

## What This Proves

- The v2 prompt handles noisy synthetic evidence across all four labels.
- Parallel generation remains useful with strict answer-key separation.
- Noisy controls are important for detecting over-penalization and under-penalization.

## What This Does Not Prove

- The loop is safe for real or sensitive release data.
- Scoring can be automated.
- The system can run without main-thread setup and review.

## Next Fix

Move from isolated generated reports to a reusable eval pack:

- consolidate the stable v2 prompt
- define a fresh-batch template
- define a scorer comparison template
- define a leakage audit checklist
- define when a batch is eligible for parallel generation
