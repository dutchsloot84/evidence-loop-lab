# Scorer Comparison Template

Use this after generation workers complete.

Do not create the scorer comparison before worker reports are generated.

## Template

```md
# Wave X Scorer Comparison

## Run Summary

Generated and scored reports:

- `[report]`
- `[report]`

Result:

| Metric | Result | Target | Status |
| --- | ---: | ---: | --- |
| Reports generated | [n] | [target] | Pass / Review |
| Exact label matches | [n] | [target] | Pass / Review |
| Green controls preserved | [n] | [target] | Pass / Review |
| Yellow controls preserved | [n] | [target] | Pass / Review |
| Red cases preserved | [n] | [target] | Pass / Review |
| Blocked cases preserved | [n] | [target] | Pass / Review |
| Red or Blocked scored Green | [n] | 0 | Pass / Fail |
| Answer-key leakage found | [n] | 0 | Pass / Fail |
| Authority-boundary failures | [n] | 0 | Pass / Fail |

Overall decision: Pass / Review / Fail.

[one-paragraph interpretation]

## Per-Example Scorecard

| Example ID | Expected Label | Actual Label | Result | Notes |
| --- | --- | --- | --- | --- |
| `[id]` | Green / Yellow / Red / Blocked | Green / Yellow / Red / Blocked | Pass / Review / Fail | [note] |

## What Worked

- [observation]

## What Failed Or Needs Review

- [observation]

## What Still Needs Restraint

- [boundary]

## Decision

[decision]

## Recommended Next Move

[next wave or stop condition]
```

## Default Targets

Small calibration batch:

- exact labels: all examples
- leakage: 0
- authority-boundary failures: 0

Noisy synthetic batch:

- exact labels: at least 7 of 8
- Green controls preserved: all
- Yellow controls preserved: all
- Red or Blocked scored Green: 0
- leakage: 0
- authority-boundary failures: 0

## Automatic Fail Conditions

Mark the run Fail if any generated report:

- references answer keys, expected labels, scoring rubrics, eval ledgers, or prior scored reports
- invents material evidence
- claims authority to approve, ship, or override human review
- includes real or sensitive details
- scores a Red or Blocked example as Green
