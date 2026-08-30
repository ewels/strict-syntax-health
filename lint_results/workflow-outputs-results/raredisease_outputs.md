# Workflow outputs migration: raredisease

- Generated: 2026-08-30T00:23:27.583868+00:00
- Status: :warning: **warn** — uses the new `output {}` syntax but still has legacy `publishDir` references to migrate

This report tracks migration from the legacy `publishDir` directive to the new [workflow outputs](https://docs.seqera.io/nextflow/tutorials/workflow-outputs) syntax.

## Workflow `output {}` block

Found 1 top-level `output {}` block:

- [`main.nf:1011`](https://github.com/nf-core/raredisease/blob/c19373fad659d5160f2fa6209464cd431de2da6a/main.nf#L1011)

## Legacy `publishDir` references

Found 2 `publishDir` references across 2 files that should be migrated to the workflow `output {}` block:

- [`conf/base.config`](https://github.com/nf-core/raredisease/blob/c19373fad659d5160f2fa6209464cd431de2da6a/conf/base.config#L65) — 1 reference
- [`modules/nf-core/spring/decompress/tests/nextflow.config`](https://github.com/nf-core/raredisease/blob/c19373fad659d5160f2fa6209464cd431de2da6a/modules/nf-core/spring/decompress/tests/nextflow.config#L3) — 1 reference
