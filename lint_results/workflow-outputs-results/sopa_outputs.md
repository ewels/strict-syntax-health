# Workflow outputs migration: sopa

- Generated: 2026-08-26T00:13:17.145279+00:00
- Status: :x: **error** — no `output {}` block found; still relies on the legacy `publishDir` directive

This report tracks migration from the legacy `publishDir` directive to the new [workflow outputs](https://docs.seqera.io/nextflow/tutorials/workflow-outputs) syntax.

## Workflow `output {}` blocks

No top-level `output {}` block found. See the docs for how to add one:
https://docs.seqera.io/nextflow/tutorials/workflow-outputs

## Legacy `publishDir` references

Found 4 `publishDir` references across 4 files that should be migrated to the workflow `output {}` block:

- [`conf/modules.config`](https://github.com/nf-core/sopa/blob/0b959963a3984ff78725209113d9ecdb78cef0b6/conf/modules.config#L16) — 1 reference
- [`modules/local/explorer/main.nf`](https://github.com/nf-core/sopa/blob/0b959963a3984ff78725209113d9ecdb78cef0b6/modules/local/explorer/main.nf#L10) — 1 reference
- [`modules/local/explorer_raw/main.nf`](https://github.com/nf-core/sopa/blob/0b959963a3984ff78725209113d9ecdb78cef0b6/modules/local/explorer_raw/main.nf#L12) — 1 reference
- [`modules/local/report/main.nf`](https://github.com/nf-core/sopa/blob/0b959963a3984ff78725209113d9ecdb78cef0b6/modules/local/report/main.nf#L10) — 1 reference
