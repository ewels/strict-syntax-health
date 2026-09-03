# Workflow outputs migration: mag

- Generated: 2026-09-03T00:23:25.092485+00:00
- Status: :x: **error** — no `output {}` block found; still relies on the legacy `publishDir` directive

This report tracks migration from the legacy `publishDir` directive to the new [workflow outputs](https://docs.seqera.io/nextflow/tutorials/workflow-outputs) syntax.

## Workflow `output {}` blocks

No top-level `output {}` block found. See the docs for how to add one:
https://docs.seqera.io/nextflow/tutorials/workflow-outputs

## Legacy `publishDir` references

Found 74 `publishDir` references across 2 files that should be migrated to the workflow `output {}` block:

- [`conf/modules.config`](https://github.com/nf-core/mag/blob/07a8b41b8d2b3d62e5346d0547a27934365ad7f6/conf/modules.config#L16) — 73 references
- [`modules/nf-core/dastool/dastool/tests/nextflow.config`](https://github.com/nf-core/mag/blob/07a8b41b8d2b3d62e5346d0547a27934365ad7f6/modules/nf-core/dastool/dastool/tests/nextflow.config#L3) — 1 reference
