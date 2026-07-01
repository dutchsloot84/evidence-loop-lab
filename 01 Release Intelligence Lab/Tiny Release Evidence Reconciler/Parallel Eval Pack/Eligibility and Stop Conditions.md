# Eligibility and Stop Conditions

## Eligible For Parallel Generation

A batch is eligible only when all are true:

- examples are synthetic or sanitized
- worker prompts can be model-visible without answer keys
- expected labels are stored separately from worker prompts
- each worker receives one packet only
- main thread will score manually after generation
- leakage audit will run before publishing results
- outputs are for learning, evals, or playbooks only

## Not Eligible

Do not run parallel generation when:

- real customer, employee, repository, ticket, or release details are present
- the output will influence a real release decision
- scoring would be skipped
- workers could inspect scorer-only files
- examples require domain context that cannot be safely sanitized
- the batch scope is vague

## Required Human Boundaries

Workers may:

- recommend a readiness label
- identify supported and unsupported claims
- list evidence gaps and next evidence

Workers may not:

- approve release
- claim shipping authority
- override human review
- accept risk on behalf of an owner
- infer sensitive or missing context

## Stop Immediately If

- answer-key content appears in generation context
- a worker references expected labels or scoring rubrics
- a report invents material evidence
- a report includes sensitive details
- a report claims authority to approve or ship
- Red or Blocked evidence is softened to Green
- the batch needs real data to be meaningful

## Trust Rule

Passing a synthetic batch increases confidence in the workflow, not authority.

Do not promote automation trust level from batch results alone. Promotion requires a separate automation trust review.
