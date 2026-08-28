# Workflow outputs migration: fetchngs

- Generated: 2026-08-28T02:46:47.183153+00:00
- Status: :x: **error** — no `output {}` block found; still relies on the legacy `publishDir` directive

This report tracks migration from the legacy `publishDir` directive to the new [workflow outputs](https://docs.seqera.io/nextflow/tutorials/workflow-outputs) syntax.

## Workflow `output {}` blocks

No top-level `output {}` block found. See the docs for how to add one:
https://docs.seqera.io/nextflow/tutorials/workflow-outputs

## Legacy `publishDir` references

Found 9 `publishDir` references across 9 files that should be migrated to the workflow `output {}` block:

- [`conf/base.config`](https://github.com/nf-core/fetchngs/blob/b10bc5ed8e95aa2132d91932b21360c81237c8f5/conf/base.config#L16) — 1 reference
- [`modules/local/aspera_cli/nextflow.config`](https://github.com/nf-core/fetchngs/blob/b10bc5ed8e95aa2132d91932b21360c81237c8f5/modules/local/aspera_cli/nextflow.config#L4) — 1 reference
- [`modules/local/multiqc_mappings_config/nextflow.config`](https://github.com/nf-core/fetchngs/blob/b10bc5ed8e95aa2132d91932b21360c81237c8f5/modules/local/multiqc_mappings_config/nextflow.config#L3) — 1 reference
- [`modules/local/sra_fastq_ftp/nextflow.config`](https://github.com/nf-core/fetchngs/blob/b10bc5ed8e95aa2132d91932b21360c81237c8f5/modules/local/sra_fastq_ftp/nextflow.config#L4) — 1 reference
- [`modules/local/sra_ids_to_runinfo/nextflow.config`](https://github.com/nf-core/fetchngs/blob/b10bc5ed8e95aa2132d91932b21360c81237c8f5/modules/local/sra_ids_to_runinfo/nextflow.config#L3) — 1 reference
- [`modules/local/sra_runinfo_to_ftp/nextflow.config`](https://github.com/nf-core/fetchngs/blob/b10bc5ed8e95aa2132d91932b21360c81237c8f5/modules/local/sra_runinfo_to_ftp/nextflow.config#L3) — 1 reference
- [`modules/nf-core/fastqdl/nextflow.config`](https://github.com/nf-core/fetchngs/blob/b10bc5ed8e95aa2132d91932b21360c81237c8f5/modules/nf-core/fastqdl/nextflow.config#L3) — 1 reference
- [`modules/nf-core/sratools/fasterqdump/nextflow.config`](https://github.com/nf-core/fetchngs/blob/b10bc5ed8e95aa2132d91932b21360c81237c8f5/modules/nf-core/sratools/fasterqdump/nextflow.config#L4) — 1 reference
- [`modules/nf-core/sratools/prefetch/nextflow.config`](https://github.com/nf-core/fetchngs/blob/b10bc5ed8e95aa2132d91932b21360c81237c8f5/modules/nf-core/sratools/prefetch/nextflow.config#L3) — 1 reference
