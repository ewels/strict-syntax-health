# Workflow outputs migration: metatdenovo

- Generated: 2026-08-27T01:24:38.554594+00:00
- Status: :x: **error** — no `output {}` block found; still relies on the legacy `publishDir` directive

This report tracks migration from the legacy `publishDir` directive to the new [workflow outputs](https://docs.seqera.io/nextflow/tutorials/workflow-outputs) syntax.

## Workflow `output {}` blocks

No top-level `output {}` block found. See the docs for how to add one:
https://docs.seqera.io/nextflow/tutorials/workflow-outputs

## Legacy `publishDir` references

Found 16 `publishDir` references across 2 files that should be migrated to the workflow `output {}` block:

- [`conf/modules.config`](https://github.com/nf-core/metatdenovo/blob/983ae70c11d4250ee7f4200e03b87d7d3a47a8c1/conf/modules.config#L13) — 15 references
- [`modules/nf-core/subread/featurecounts/tests/nextflow.config`](https://github.com/nf-core/metatdenovo/blob/983ae70c11d4250ee7f4200e03b87d7d3a47a8c1/modules/nf-core/subread/featurecounts/tests/nextflow.config#L3) — 1 reference
