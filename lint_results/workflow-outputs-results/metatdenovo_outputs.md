# Workflow outputs migration: metatdenovo

- Generated: 2026-08-26T00:12:06.186338+00:00
- Status: :x: **error** — no `output {}` block found; still relies on the legacy `publishDir` directive

This report tracks migration from the legacy `publishDir` directive to the new [workflow outputs](https://docs.seqera.io/nextflow/tutorials/workflow-outputs) syntax.

## Workflow `output {}` blocks

No top-level `output {}` block found. See the docs for how to add one:
https://docs.seqera.io/nextflow/tutorials/workflow-outputs

## Legacy `publishDir` references

Found 16 `publishDir` references across 2 files that should be migrated to the workflow `output {}` block:

- [`conf/modules.config`](https://github.com/nf-core/metatdenovo/blob/0c421761f5d5f8d33b99f69509fb340c80a37cf0/conf/modules.config#L13) — 15 references
- [`modules/nf-core/subread/featurecounts/tests/nextflow.config`](https://github.com/nf-core/metatdenovo/blob/0c421761f5d5f8d33b99f69509fb340c80a37cf0/modules/nf-core/subread/featurecounts/tests/nextflow.config#L3) — 1 reference
