# Workflow outputs migration: viralmetagenome

- Generated: 2026-09-05T00:22:14.993204+00:00
- Status: :x: **error** — no `output {}` block found; still relies on the legacy `publishDir` directive

This report tracks migration from the legacy `publishDir` directive to the new [workflow outputs](https://docs.seqera.io/nextflow/tutorials/workflow-outputs) syntax.

## Workflow `output {}` blocks

No top-level `output {}` block found. See the docs for how to add one:
https://docs.seqera.io/nextflow/tutorials/workflow-outputs

## Legacy `publishDir` references

Found 118 `publishDir` references across 4 files that should be migrated to the workflow `output {}` block:

- [`conf/modules.config`](https://github.com/nf-core/viralmetagenome/blob/d46ec0b30e460abfdefbc78d732e354ca7bd2e02/conf/modules.config#L15) — 115 references
- [`modules/nf-core/mmseqs/cluster/tests/nextflow.config`](https://github.com/nf-core/viralmetagenome/blob/d46ec0b30e460abfdefbc78d732e354ca7bd2e02/modules/nf-core/mmseqs/cluster/tests/nextflow.config#L3) — 1 reference
- [`modules/nf-core/mmseqs/linclust/tests/nextflow.config`](https://github.com/nf-core/viralmetagenome/blob/d46ec0b30e460abfdefbc78d732e354ca7bd2e02/modules/nf-core/mmseqs/linclust/tests/nextflow.config#L3) — 1 reference
- [`subworkflows/local/map_reads/tests/nextflow.config`](https://github.com/nf-core/viralmetagenome/blob/d46ec0b30e460abfdefbc78d732e354ca7bd2e02/subworkflows/local/map_reads/tests/nextflow.config#L21) — 1 reference
