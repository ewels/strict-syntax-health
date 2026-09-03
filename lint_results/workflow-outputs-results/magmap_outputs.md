# Workflow outputs migration: magmap

- Generated: 2026-09-03T00:23:48.696306+00:00
- Status: :x: **error** — no `output {}` block found; still relies on the legacy `publishDir` directive

This report tracks migration from the legacy `publishDir` directive to the new [workflow outputs](https://docs.seqera.io/nextflow/tutorials/workflow-outputs) syntax.

## Workflow `output {}` blocks

No top-level `output {}` block found. See the docs for how to add one:
https://docs.seqera.io/nextflow/tutorials/workflow-outputs

## Legacy `publishDir` references

Found 26 `publishDir` references across 2 files that should be migrated to the workflow `output {}` block:

- [`conf/modules.config`](https://github.com/nf-core/magmap/blob/01ce1bbb006e6336839d6396d7590bc248dad467/conf/modules.config#L15) — 25 references
- [`modules/nf-core/subread/featurecounts/tests/nextflow.config`](https://github.com/nf-core/magmap/blob/01ce1bbb006e6336839d6396d7590bc248dad467/modules/nf-core/subread/featurecounts/tests/nextflow.config#L3) — 1 reference
