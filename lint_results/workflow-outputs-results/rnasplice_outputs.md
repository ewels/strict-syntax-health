# Workflow outputs migration: rnasplice

- Generated: 2026-09-09T00:22:14.695579+00:00
- Status: :x: **error** — no `output {}` block found; still relies on the legacy `publishDir` directive

This report tracks migration from the legacy `publishDir` directive to the new [workflow outputs](https://docs.seqera.io/nextflow/tutorials/workflow-outputs) syntax.

## Workflow `output {}` blocks

No top-level `output {}` block found. See the docs for how to add one:
https://docs.seqera.io/nextflow/tutorials/workflow-outputs

## Legacy `publishDir` references

Found 70 `publishDir` references across 4 files that should be migrated to the workflow `output {}` block:

- [`conf/modules.config`](https://github.com/nf-core/rnasplice/blob/dabaadc68178943e06d180ac894734738cd07492/conf/modules.config#L16) — 67 references
- [`modules/nf-core/subread/featurecounts/tests/nextflow.config`](https://github.com/nf-core/rnasplice/blob/dabaadc68178943e06d180ac894734738cd07492/modules/nf-core/subread/featurecounts/tests/nextflow.config#L3) — 1 reference
- [`modules/nf-core/umitools/extract/tests/nextflow.config`](https://github.com/nf-core/rnasplice/blob/dabaadc68178943e06d180ac894734738cd07492/modules/nf-core/umitools/extract/tests/nextflow.config#L3) — 1 reference
- [`subworkflows/nf-core/bedgraph_bedclip_bedgraphtobigwig/tests/nextflow.config`](https://github.com/nf-core/rnasplice/blob/dabaadc68178943e06d180ac894734738cd07492/subworkflows/nf-core/bedgraph_bedclip_bedgraphtobigwig/tests/nextflow.config#L3) — 1 reference
