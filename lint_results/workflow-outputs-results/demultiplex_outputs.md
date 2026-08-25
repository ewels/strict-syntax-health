# Workflow outputs migration: demultiplex

- Generated: 2026-08-25T00:09:39.807385+00:00
- Status: :warning: **warn** — uses the new `output {}` syntax but still has legacy `publishDir` references to migrate

This report tracks migration from the legacy `publishDir` directive to the new [workflow outputs](https://docs.seqera.io/nextflow/tutorials/workflow-outputs) syntax.

## Workflow `output {}` block

Found 1 top-level `output {}` block:

- [`main.nf:129`](https://github.com/nf-core/demultiplex/blob/80c6c2b01a9dd7bb0f1f3fcd7f90ee52fa324703/main.nf#L129)

## Legacy `publishDir` references

Found 5 `publishDir` references across 3 files that should be migrated to the workflow `output {}` block:

- [`conf/test.config`](https://github.com/nf-core/demultiplex/blob/80c6c2b01a9dd7bb0f1f3fcd7f90ee52fa324703/conf/test.config#L38) — 2 references
- [`conf/test_uncompressed.config`](https://github.com/nf-core/demultiplex/blob/80c6c2b01a9dd7bb0f1f3fcd7f90ee52fa324703/conf/test_uncompressed.config#L39) — 2 references
- [`conf/test_flowcell.config`](https://github.com/nf-core/demultiplex/blob/80c6c2b01a9dd7bb0f1f3fcd7f90ee52fa324703/conf/test_flowcell.config#L39) — 1 reference
