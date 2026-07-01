# Wave 11 Worker Run Log

## Launch

Branch: `codex/middle-band-yellow-calibration-wave`

Workers launched as generation-only agents with `fork_context: false`.

| Example | Worker Nickname | Agent ID | Scope |
| --- | --- | --- | --- |
| `PAR-Y-001` | Mill | `019f1f39-5128-76c0-af01-dde271bbaaba` | Generate one readiness report from model-visible packet. |
| `PAR-R-001` | Darwin | `019f1f39-5199-7433-817c-400adb1443cf` | Generate one readiness report from model-visible packet. |
| `PAR-B-001` | Huygens | `019f1f39-5213-7e63-aa02-6c965045a5bd` | Generate one readiness report from model-visible packet. |

## Boundary

Workers are instructed not to inspect repo files and not to read:

- answer keys
- scoring rubrics
- eval ledgers
- prior reports
- other project files

## Results

| Example | Worker Result | Notes |
| --- | --- | --- |
| `PAR-Y-001` | Yellow | Corrected the Wave 10 overcorrection from Red to Yellow. |
| `PAR-R-001` | Red | Preserved the Wave 10 correction from Yellow to Red. |
| `PAR-B-001` | Blocked | Preserved the Wave 10 correction from Red to Blocked. |

## Initial Read

The v2 prompt preserved the Yellow middle band while keeping Red and Blocked sharp on the targeted calibration examples.
