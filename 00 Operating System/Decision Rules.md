# Decision Rules

## Weekly Lab Decision

At the end of each week, every active lab receives one decision:

- keep
- pause
- merge
- simplify

Only one lab should be active unless there is a clear reason to run a small support slice in parallel.

## Keep

Keep a lab when it is producing at least one of:

- reusable evidence
- a clearer playbook
- stronger judgment
- a useful eval set
- a teach-back artifact
- transferable workflow knowledge

## Pause

Pause a lab when it needs:

- data that cannot be safely used
- context that is not available yet
- infrastructure that would exceed the current learning goal
- stakeholder feedback before the next step is meaningful

Pausing is not failure. It prevents a lab from becoming vague work.

## Merge

Merge a lab when another lab uses the same loop pattern.

Examples:

- release readiness and field-operations pilot proof both use claim -> evidence -> risk -> next evidence
- agent governance and weekly review both use approval boundaries and stop conditions
- Obsidian knowledge loops and teach-back artifacts both use raw source -> synthesis -> update neighbors

## Simplify

Simplify a lab when:

- the artifact is unclear
- the eval is missing
- the build is expanding faster than the learning
- the workflow cannot be explained in five minutes
- the loop has too many inputs, steps, or outcomes

The simplification move is usually:

1. Reduce the input set.
2. Reduce the output format.
3. Remove automation.
4. Write the manual loop.
5. Add evals back only after the loop is clear.

## Stop Conditions

Stop a sprint slice when:

- the artifact exists
- the lesson is documented
- the next evidence is named
- the current scope is about to expand without a decision

## Approval Boundary

Any workflow that touches real work-like data must pass a sanitation check before it becomes part of the lab.

For now, the lab defaults to:

- synthetic data
- sanitized structure only
- no customer names
- no employee names
- no internal project names
- no repo names
- no ticket IDs
- no PR links
- no exact ticket or PR titles
- no proprietary strategy
- no sensitive business context

