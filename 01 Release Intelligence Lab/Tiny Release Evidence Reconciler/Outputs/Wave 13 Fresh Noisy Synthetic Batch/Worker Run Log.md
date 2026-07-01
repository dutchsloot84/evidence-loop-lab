# Wave 13 Worker Run Log

## Launch

Branch: `codex/fresh-noisy-synthetic-batch-wave`

Workers launched as generation-only agents with `fork_context: false`.

| Example | Worker Nickname | Agent ID | Scope |
| --- | --- | --- | --- |
| `NOISE-G-001` | Noether | `019f1f5c-b87b-73f3-9f16-a8e36514cc1d` | Generate one readiness report from model-visible packet. |
| `NOISE-G-002` | Avicenna | `019f1f5c-b8fa-7632-b8f8-08554e232f2c` | Generate one readiness report from model-visible packet. |
| `NOISE-Y-001` | McClintock | `019f1f5c-b968-7c43-a289-bbca2e3e8356` | Generate one readiness report from model-visible packet. |
| `NOISE-Y-002` | Epicurus | `019f1f5c-b9e1-7ba3-b540-8cea0dc3656c` | Generate one readiness report from model-visible packet. |
| `NOISE-R-001` | Harvey | `019f1f5c-ba63-7891-be7f-4ed5f80192b9` | Generate one readiness report from model-visible packet. |
| `NOISE-R-002` | Galileo | `019f1f5c-bad9-7622-9565-56d929ba8fb3` | Generate one readiness report from model-visible packet. |
| `NOISE-B-001` | Archimedes | `019f1f5d-758a-75c0-9833-caed9436f919` | Generate one readiness report from model-visible packet. |
| `NOISE-B-002` | Pascal | `019f1f5d-7614-7862-b68d-cd6e0e381737` | Generate one readiness report from model-visible packet. |

Note: the first launch hit the available thread limit after six workers, so the two Blocked workers are queued for a second mini-batch after completed agents are closed.

## Boundary

Workers are instructed not to inspect repo files and not to read:

- answer keys
- expected labels
- scoring rubrics
- eval ledgers
- prior reports
- other project files

## Results

| Example | Worker Result | Notes |
| --- | --- | --- |
| `NOISE-G-001` | Green | Preserved Green despite stale screenshot and missing marketing review. |
| `NOISE-G-002` | Green | Preserved Green despite unrelated lint warning and missing announcement. |
| `NOISE-Y-001` | Yellow | Preserved bounded provider-preview ambiguity as Yellow. |
| `NOISE-Y-002` | Yellow | Preserved bounded large-export warning as Yellow. |
| `NOISE-R-001` | Red | Identified missing operational controls despite informal "ops looks fine" note. |
| `NOISE-R-002` | Red | Identified missing integration validation despite unit and credential evidence. |
| `NOISE-B-001` | Blocked | Treated failed reversal drill as failed required gate. |
| `NOISE-B-002` | Blocked | Treated failed security-relevant rollback as failed required gate. |

## Initial Read

The v2 prompt held across the noisy synthetic batch. The examples returned the intended label distribution without scorer-visible leakage.
