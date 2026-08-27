# Workflow outputs migration: raredisease

- Generated: 2026-08-27T01:27:17.144432+00:00
- Status: :warning: **warn** — uses the new `output {}` syntax but still has legacy `publishDir` references to migrate

This report tracks migration from the legacy `publishDir` directive to the new [workflow outputs](https://docs.seqera.io/nextflow/tutorials/workflow-outputs) syntax.

## Workflow `output {}` block

Found 1 top-level `output {}` block:

- [`main.nf:1006`](https://github.com/nf-core/raredisease/blob/08158a8d67cd5233f07767bd422a14da58dd0718/main.nf#L1006)

## Legacy `publishDir` references

Found 2 `publishDir` references across 2 files that should be migrated to the workflow `output {}` block:

- [`conf/base.config`](https://github.com/nf-core/raredisease/blob/08158a8d67cd5233f07767bd422a14da58dd0718/conf/base.config#L65) — 1 reference
- [`modules/nf-core/spring/decompress/tests/nextflow.config`](https://github.com/nf-core/raredisease/blob/08158a8d67cd5233f07767bd422a14da58dd0718/modules/nf-core/spring/decompress/tests/nextflow.config#L3) — 1 reference
