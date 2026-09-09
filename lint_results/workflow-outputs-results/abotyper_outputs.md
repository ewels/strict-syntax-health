# Workflow outputs migration: abotyper

- Generated: 2026-09-09T00:19:30.648988+00:00
- Status: :x: **error** — no `output {}` block found; still relies on the legacy `publishDir` directive

This report tracks migration from the legacy `publishDir` directive to the new [workflow outputs](https://docs.seqera.io/nextflow/tutorials/workflow-outputs) syntax.

## Workflow `output {}` blocks

No top-level `output {}` block found. See the docs for how to add one:
https://docs.seqera.io/nextflow/tutorials/workflow-outputs

## Legacy `publishDir` references

Found 12 `publishDir` references across 2 files that should be migrated to the workflow `output {}` block:

- [`conf/modules.config`](https://github.com/nf-core/abotyper/blob/e0aa5055e91567330ab0d74dd3f4350408826e5e/conf/modules.config#L14) — 11 references
- [`modules/local/abo/snps2pheno/main.nf`](https://github.com/nf-core/abotyper/blob/e0aa5055e91567330ab0d74dd3f4350408826e5e/modules/local/abo/snps2pheno/main.nf#L10) — 1 reference
