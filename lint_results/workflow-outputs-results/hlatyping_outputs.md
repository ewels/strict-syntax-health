# Workflow outputs migration: hlatyping

- Generated: 2026-09-05T00:19:07.523801+00:00
- Status: :x: **error** — no `output {}` block found; still relies on the legacy `publishDir` directive

This report tracks migration from the legacy `publishDir` directive to the new [workflow outputs](https://docs.seqera.io/nextflow/tutorials/workflow-outputs) syntax.

## Workflow `output {}` blocks

No top-level `output {}` block found. See the docs for how to add one:
https://docs.seqera.io/nextflow/tutorials/workflow-outputs

## Legacy `publishDir` references

Found 20 `publishDir` references across 2 files that should be migrated to the workflow `output {}` block:

- [`conf/modules.config`](https://github.com/nf-core/hlatyping/blob/fff6d750aae2557d6bb647cf0ad3265c7e78db39/conf/modules.config#L15) — 19 references
- [`modules/nf-core/hlala/preparegraph/tests/nextflow.config`](https://github.com/nf-core/hlatyping/blob/fff6d750aae2557d6bb647cf0ad3265c7e78db39/modules/nf-core/hlala/preparegraph/tests/nextflow.config#L7) — 1 reference
