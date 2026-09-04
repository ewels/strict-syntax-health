# Workflow outputs migration: raredisease

- Generated: 2026-09-04T00:22:03.667406+00:00
- Status: :warning: **warn** — uses the new `output {}` syntax but still has legacy `publishDir` references to migrate

This report tracks migration from the legacy `publishDir` directive to the new [workflow outputs](https://docs.seqera.io/nextflow/tutorials/workflow-outputs) syntax.

## Workflow `output {}` block

Found 1 top-level `output {}` block:

- [`main.nf:1011`](https://github.com/nf-core/raredisease/blob/ecab8e6280b63d59617f319fb2e419bbabde58b7/main.nf#L1011)

## Legacy `publishDir` references

Found 2 `publishDir` references across 2 files that should be migrated to the workflow `output {}` block:

- [`conf/base.config`](https://github.com/nf-core/raredisease/blob/ecab8e6280b63d59617f319fb2e419bbabde58b7/conf/base.config#L68) — 1 reference
- [`modules/nf-core/spring/decompress/tests/nextflow.config`](https://github.com/nf-core/raredisease/blob/ecab8e6280b63d59617f319fb2e419bbabde58b7/modules/nf-core/spring/decompress/tests/nextflow.config#L3) — 1 reference
