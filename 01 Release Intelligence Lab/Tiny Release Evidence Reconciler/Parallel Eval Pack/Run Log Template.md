# Run Log Template

Use this to track worker launches and preserve coordination evidence.

```md
# Wave X Worker Run Log

## Launch

Branch: `[branch]`

Workers launched as generation-only agents with `fork_context: false`.

| Example | Worker Nickname | Agent ID | Scope |
| --- | --- | --- | --- |
| `[example-id]` | [nickname] | `[agent-id]` | Generate one readiness report from model-visible packet. |

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
| `[example-id]` | Green / Yellow / Red / Blocked | [note] |

## Initial Read

[one-paragraph interpretation before formal scoring]
```
