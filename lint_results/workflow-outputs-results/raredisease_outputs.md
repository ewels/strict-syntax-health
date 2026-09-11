# Workflow outputs migration: raredisease

- Generated: 2026-09-11T00:21:46.047816+00:00
- Status: :warning: **warn** — uses the new `output {}` syntax but still has legacy `publishDir` references to migrate

This report tracks migration from the legacy `publishDir` directive to the new [workflow outputs](https://docs.seqera.io/nextflow/tutorials/workflow-outputs) syntax.

## Workflow `output {}` block

Found 1 top-level `output {}` block:

- [`main.nf:1004`](https://github.com/nf-core/raredisease/blob/469e32cd79e8280a0853455c9bcd89afccd56946/main.nf#L1004)

## Legacy `publishDir` references

Found 2 `publishDir` references across 2 files that should be migrated to the workflow `output {}` block:

- [`conf/base.config`](https://github.com/nf-core/raredisease/blob/469e32cd79e8280a0853455c9bcd89afccd56946/conf/base.config#L68) — 1 reference
- [`modules/nf-core/spring/decompress/tests/nextflow.config`](https://github.com/nf-core/raredisease/blob/469e32cd79e8280a0853455c9bcd89afccd56946/modules/nf-core/spring/decompress/tests/nextflow.config#L3) — 1 reference
