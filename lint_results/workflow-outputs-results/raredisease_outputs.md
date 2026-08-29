# Workflow outputs migration: raredisease

- Generated: 2026-08-29T00:19:54.964134+00:00
- Status: :warning: **warn** — uses the new `output {}` syntax but still has legacy `publishDir` references to migrate

This report tracks migration from the legacy `publishDir` directive to the new [workflow outputs](https://docs.seqera.io/nextflow/tutorials/workflow-outputs) syntax.

## Workflow `output {}` block

Found 1 top-level `output {}` block:

- [`main.nf:1011`](https://github.com/nf-core/raredisease/blob/7c0672095b8fac4077c78595f60992284238602e/main.nf#L1011)

## Legacy `publishDir` references

Found 2 `publishDir` references across 2 files that should be migrated to the workflow `output {}` block:

- [`conf/base.config`](https://github.com/nf-core/raredisease/blob/7c0672095b8fac4077c78595f60992284238602e/conf/base.config#L65) — 1 reference
- [`modules/nf-core/spring/decompress/tests/nextflow.config`](https://github.com/nf-core/raredisease/blob/7c0672095b8fac4077c78595f60992284238602e/modules/nf-core/spring/decompress/tests/nextflow.config#L3) — 1 reference
