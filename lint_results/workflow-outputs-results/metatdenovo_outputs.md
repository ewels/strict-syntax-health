# Workflow outputs migration: metatdenovo

- Generated: 2026-09-09T00:20:54.798480+00:00
- Status: :x: **error** — no `output {}` block found; still relies on the legacy `publishDir` directive

This report tracks migration from the legacy `publishDir` directive to the new [workflow outputs](https://docs.seqera.io/nextflow/tutorials/workflow-outputs) syntax.

## Workflow `output {}` blocks

No top-level `output {}` block found. See the docs for how to add one:
https://docs.seqera.io/nextflow/tutorials/workflow-outputs

## Legacy `publishDir` references

Found 17 `publishDir` references across 4 files that should be migrated to the workflow `output {}` block:

- [`conf/modules.config`](https://github.com/nf-core/metatdenovo/blob/1cf20844ef618a21d1266774514a64d8568beba7/conf/modules.config#L13) — 14 references
- [`modules/nf-core/mmseqs/cluster/tests/nextflow.config`](https://github.com/nf-core/metatdenovo/blob/1cf20844ef618a21d1266774514a64d8568beba7/modules/nf-core/mmseqs/cluster/tests/nextflow.config#L3) — 1 reference
- [`modules/nf-core/mmseqs/linclust/tests/nextflow.config`](https://github.com/nf-core/metatdenovo/blob/1cf20844ef618a21d1266774514a64d8568beba7/modules/nf-core/mmseqs/linclust/tests/nextflow.config#L3) — 1 reference
- [`modules/nf-core/subread/featurecounts/tests/nextflow.config`](https://github.com/nf-core/metatdenovo/blob/1cf20844ef618a21d1266774514a64d8568beba7/modules/nf-core/subread/featurecounts/tests/nextflow.config#L3) — 1 reference
