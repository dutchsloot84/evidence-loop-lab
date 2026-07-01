# Wave 10 Worker Run Log

## Launch

Branch: `codex/severity-calibrated-rerun-wave`

Workers launched as generation-only agents with `fork_context: false`.

| Example | Worker Nickname | Agent ID | Scope |
| --- | --- | --- | --- |
| `PAR-R-001` | Anscombe | `019f1f18-b467-7671-9f52-0386ac85da15` | Generate one readiness report from model-visible packet. |
| `PAR-B-001` | Einstein | `019f1f18-b4d1-75d0-966b-f2c09c333338` | Generate one readiness report from model-visible packet. |
| `PAR-Y-001` | Cicero | `019f1f18-b54a-75d3-8d8c-8412276bfb49` | Generate one readiness report from model-visible packet. |

## Boundary

Workers were instructed not to inspect repo files and not to read:

- answer keys
- scoring rubrics
- eval ledgers
- prior reports
- other project files

## Results

| Example | Worker Result | Notes |
| --- | --- | --- |
| `PAR-R-001` | Red | Corrected the Wave 9 softening from Yellow to Red. |
| `PAR-B-001` | Blocked | Corrected the Wave 9 softening from Red to Blocked. |
| `PAR-Y-001` | Red | Overcorrected the Yellow control to Red. |

## Initial Read

The severity-calibrated prompt fixed the two known operational-readiness misses, but it introduced an overcorrection risk for ambiguous functional warnings.
