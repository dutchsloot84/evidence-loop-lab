# Manual Eval Run Guide

## Purpose

Run the Tiny Release Evidence Reconciler manually before any coding exists.

This guide is for Wave 2: a local-first, markdown-native eval run that proves the loop can generate readiness reports from synthetic release packets, score them against a scorer-only answer key, record misses, and decide whether a tiny local script is justified.

## Source Boundaries

Use only synthetic or sanitized materials.

Model-visible input:

- `Mock Data/Release Packets.md`
- `Report Template.md`
- `Loop Spec.md`, if extra task framing is needed

Scorer-only material:

- `Mock Data/Answer Key.md`
- `Scoring Rubric.md`
- `Eval Run Ledger.md`

Do not include `Mock Data/Answer Key.md` in the prompt or context used to generate reports. The answer key exists only for scoring after a report has been produced.

## First Run Scope

Run exactly 3 packets:

| Run Order | Example ID | Packet Source |
| ---: | --- | --- |
| 1 | REL-G-001 | `Mock Data/Release Packets.md` |
| 2 | REL-Y-001 | `Mock Data/Release Packets.md` |
| 3 | REL-R-002 | `Mock Data/Release Packets.md` |

This first run is intentionally small. It should test one expected green case, one expected yellow case, and one expected red case without introducing automation complexity too early.

## Report Generation Steps

Repeat these steps once per packet.

1. Open `Mock Data/Release Packets.md`.
2. Copy only the selected packet into the generation context.
3. Open `Report Template.md`.
4. Ask the model to produce a markdown readiness report using the template.
5. Make clear that the model must assign one label: Green, Yellow, Red, or Blocked.
6. Make clear that the model may recommend a readiness label, but must not claim authority to ship or approve the release.
7. Save or paste the generated report in local eval notes or an output file using the example ID in the heading.

Suggested generation prompt:

```md
Using the release packet below and the Release Readiness Report Template, generate one synthetic markdown readiness report.

Rules:
- Use only the packet evidence provided here.
- Do not invent evidence.
- Assign exactly one readiness label: Green, Yellow, Red, or Blocked.
- Separate supported claims from unsupported or weak claims.
- Name concrete evidence gaps and next evidence needed.
- Preserve the human approval boundary. You may recommend a label, but you may not claim authority to ship or approve.
- Keep all details synthetic and sanitized.

Packet:

[paste one selected packet from Release Packets.md]
```

## Scoring Steps

Score each generated report only after generation is complete.

1. Open `Scoring Rubric.md`.
2. Open `Mock Data/Answer Key.md`.
3. Find the answer-key entry for the same example ID.
4. Compare the generated report against:
   - expected readiness label
   - expected rationale
   - important evidence to cite
   - failure mode to watch for
5. Assign category points using the rubric.
6. Record the actual label, total score, key misses, failure mode, and next fix in `Eval Run Ledger.md`.
7. Mark automatic-fail conditions if the report:
   - assigns Green to a red or blocked case
   - claims final authority to ship or approve
   - invents evidence not present in the packet
   - includes sensitive or real work details

For Wave 2, the main evidence is not just the score. The useful output is the shape of the misses: whether the loop over-trusts weak evidence, ignores known issues, misses rollback or monitoring gaps, or blurs the human approval boundary.

## Miss Recording

Use short, concrete miss notes. A miss should name what the report did wrong and what evidence it should have used.

Good miss notes:

- `Over-penalized minor visual issue despite regression, smoke, rollback, and monitoring evidence.`
- `Marked Green while ignoring incomplete mobile and error-state QA plus missing rollback and monitoring.`
- `Downplayed unresolved edit-and-save issue and did not challenge broad all-users rollout claim.`

Avoid vague miss notes:

- `Bad rationale.`
- `Needs more detail.`
- `Wrong label.`

## Tiny Script Decision

After the 3-packet run, decide whether a tiny local script is justified.

A script is justified if at least two of these are true:

- Copying packet text into prompts is error-prone.
- Reports are hard to associate with example IDs.
- Ledger rows are inconsistent or missing required fields.
- Scoring notes repeatedly need the same headings or table format.
- The next run will expand beyond 3 packets.

A script is not justified yet if:

- The manual process is still unclear.
- The prompt or template is changing after every example.
- The scorer is still discovering what misses matter.
- The only benefit would be speed, not consistency or error reduction.

If justified, the first script should stay tiny and local. It should help select packet text, create report filenames or headings, and prefill ledger rows. It should not score reports automatically until the manual scoring process is stable.

## Completion Checklist

- [ ] Generated reports for exactly `REL-G-001`, `REL-Y-001`, and `REL-R-002`.
- [ ] Used `Release Packets.md` as model-visible input.
- [ ] Kept `Answer Key.md` scorer-only.
- [ ] Scored each report with `Scoring Rubric.md`.
- [ ] Recorded each result in `Eval Run Ledger.md`.
- [ ] Recorded key misses and failure modes.
- [ ] Decided whether a tiny local script is justified.
- [ ] Kept all artifacts synthetic, sanitized, and markdown-native.
