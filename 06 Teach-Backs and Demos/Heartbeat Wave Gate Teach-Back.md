# Heartbeat Wave Gate Teach-Back

## One-Sentence Explanation

Evidence Loop Lab uses heartbeat checks as gates between waves: finish a wave, inspect the evidence, recommend the next wave, and wait for human approval before launching more work.

## Five-Minute Teach-Back

### 1. The Problem

Parallel AI work can create speed, but it can also create mess:

- unclear branches
- half-finished artifacts
- missed review issues
- public-repo sanitation risk
- next steps chosen by momentum instead of evidence

The lab needs a way to pause between waves and ask: did the last wave actually produce trusted evidence?

### 2. The Pattern

The wave gate is:

```text
wave completes -> integrate -> review -> heartbeat audits -> recommend next wave -> human approves
```

The heartbeat is not an autopilot at first. It is a scheduled auditor.

### 3. What The Heartbeat Checks

The first heartbeat test checks:

- whether Git is clean and synced
- whether expected artifacts exist
- whether the last wave had reviewer findings
- whether any risks remain
- which next wave is highest leverage

It reports evidence instead of just saying "looks good."

### 4. Why This Matters

This turns project management into an evidence loop.

Instead of asking, "What should we do next?" from memory, we ask:

- What exists?
- What was reviewed?
- What risks remain?
- What is the next smallest useful wave?
- What still needs human approval?

### 5. Trust Ladder

Automation earns trust in levels:

1. Reminder
2. Auditor
3. Wave planner
4. Gated launcher
5. Lab operator

Evidence Loop Lab is currently at Level 2: Auditor.

That means the heartbeat can check and recommend, but it cannot launch work or push changes without approval.

### 6. First Test

The first test is intentionally boring:

- finite schedule
- read-only audit
- no auto-launch
- concise report
- recommend one next wave

If it works twice, we can consider letting it draft wave plans next.

## Reusable Teaching Line

The heartbeat is not there to make the project autonomous. It is there to make the pause between waves evidence-backed.

