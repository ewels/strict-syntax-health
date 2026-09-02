# Workflow outputs migration: genomicrelatedness

- Generated: 2026-09-02T00:20:44.266873+00:00
- Status: :x: **error** — no `output {}` block found; still relies on the legacy `publishDir` directive

This report tracks migration from the legacy `publishDir` directive to the new [workflow outputs](https://docs.seqera.io/nextflow/tutorials/workflow-outputs) syntax.

## Workflow `output {}` blocks

No top-level `output {}` block found. See the docs for how to add one:
https://docs.seqera.io/nextflow/tutorials/workflow-outputs

## Legacy `publishDir` references

Found 61 `publishDir` references across 40 files that should be migrated to the workflow `output {}` block:

- [`conf/modules/samtools_index.config`](https://github.com/nf-core/genomicrelatedness/blob/2484e643de827050d2b6a10b150223cf9ec5c9e6/conf/modules/samtools_index.config#L16) — 3 references
- [`conf/modules/samtools_merge.config`](https://github.com/nf-core/genomicrelatedness/blob/2484e643de827050d2b6a10b150223cf9ec5c9e6/conf/modules/samtools_merge.config#L16) — 3 references
- [`conf/subworkflows/prepare_genome.config`](https://github.com/nf-core/genomicrelatedness/blob/2484e643de827050d2b6a10b150223cf9ec5c9e6/conf/subworkflows/prepare_genome.config#L17) — 3 references
- [`conf/modules.config`](https://github.com/nf-core/genomicrelatedness/blob/2484e643de827050d2b6a10b150223cf9ec5c9e6/conf/modules.config#L15) — 2 references
- [`conf/modules/bcftools_sort.config`](https://github.com/nf-core/genomicrelatedness/blob/2484e643de827050d2b6a10b150223cf9ec5c9e6/conf/modules/bcftools_sort.config#L16) — 2 references
- [`conf/modules/bcftools_stats.config`](https://github.com/nf-core/genomicrelatedness/blob/2484e643de827050d2b6a10b150223cf9ec5c9e6/conf/modules/bcftools_stats.config#L16) — 2 references
- [`conf/modules/gatk4_analyzecovariates.config`](https://github.com/nf-core/genomicrelatedness/blob/2484e643de827050d2b6a10b150223cf9ec5c9e6/conf/modules/gatk4_analyzecovariates.config#L16) — 2 references
- [`conf/modules/gatk4_applybqsr.config`](https://github.com/nf-core/genomicrelatedness/blob/2484e643de827050d2b6a10b150223cf9ec5c9e6/conf/modules/gatk4_applybqsr.config#L16) — 2 references
- [`conf/modules/gatk4_baserecalibrator.config`](https://github.com/nf-core/genomicrelatedness/blob/2484e643de827050d2b6a10b150223cf9ec5c9e6/conf/modules/gatk4_baserecalibrator.config#L16) — 2 references
- [`conf/modules/gatk4_gatherbqsrreports.config`](https://github.com/nf-core/genomicrelatedness/blob/2484e643de827050d2b6a10b150223cf9ec5c9e6/conf/modules/gatk4_gatherbqsrreports.config#L16) — 2 references
- [`conf/modules/gatk4_genomicsdbimport.config`](https://github.com/nf-core/genomicrelatedness/blob/2484e643de827050d2b6a10b150223cf9ec5c9e6/conf/modules/gatk4_genomicsdbimport.config#L16) — 2 references
- [`conf/modules/gatk4_genotypegvcfs.config`](https://github.com/nf-core/genomicrelatedness/blob/2484e643de827050d2b6a10b150223cf9ec5c9e6/conf/modules/gatk4_genotypegvcfs.config#L16) — 2 references
- [`conf/modules/gatk4_haplotypecaller.config`](https://github.com/nf-core/genomicrelatedness/blob/2484e643de827050d2b6a10b150223cf9ec5c9e6/conf/modules/gatk4_haplotypecaller.config#L19) — 2 references
- [`conf/modules/gatk4_mergevcfs.config`](https://github.com/nf-core/genomicrelatedness/blob/2484e643de827050d2b6a10b150223cf9ec5c9e6/conf/modules/gatk4_mergevcfs.config#L16) — 2 references
- [`conf/modules/make_scaffold_bed.config`](https://github.com/nf-core/genomicrelatedness/blob/2484e643de827050d2b6a10b150223cf9ec5c9e6/conf/modules/make_scaffold_bed.config#L16) — 2 references
- [`conf/modules/vcftools.config`](https://github.com/nf-core/genomicrelatedness/blob/2484e643de827050d2b6a10b150223cf9ec5c9e6/conf/modules/vcftools.config#L18) — 2 references
- [`conf/subworkflows/cram_baserecalibrator.config`](https://github.com/nf-core/genomicrelatedness/blob/2484e643de827050d2b6a10b150223cf9ec5c9e6/conf/subworkflows/cram_baserecalibrator.config#L16) — 2 references
- [`conf/subworkflows/filter_variants.config`](https://github.com/nf-core/genomicrelatedness/blob/2484e643de827050d2b6a10b150223cf9ec5c9e6/conf/subworkflows/filter_variants.config#L16) — 2 references
- [`conf/modules/angsd_ngsrelate.config`](https://github.com/nf-core/genomicrelatedness/blob/2484e643de827050d2b6a10b150223cf9ec5c9e6/conf/modules/angsd_ngsrelate.config#L18) — 1 reference
- [`conf/modules/bcftools_call.config`](https://github.com/nf-core/genomicrelatedness/blob/2484e643de827050d2b6a10b150223cf9ec5c9e6/conf/modules/bcftools_call.config#L17) — 1 reference
- [`conf/modules/bcftools_concat.config`](https://github.com/nf-core/genomicrelatedness/blob/2484e643de827050d2b6a10b150223cf9ec5c9e6/conf/modules/bcftools_concat.config#L17) — 1 reference
- [`conf/modules/bcftools_index.config`](https://github.com/nf-core/genomicrelatedness/blob/2484e643de827050d2b6a10b150223cf9ec5c9e6/conf/modules/bcftools_index.config#L17) — 1 reference
- [`conf/modules/bcftools_isec.config`](https://github.com/nf-core/genomicrelatedness/blob/2484e643de827050d2b6a10b150223cf9ec5c9e6/conf/modules/bcftools_isec.config#L17) — 1 reference
- [`conf/modules/bcftools_mpileup.config`](https://github.com/nf-core/genomicrelatedness/blob/2484e643de827050d2b6a10b150223cf9ec5c9e6/conf/modules/bcftools_mpileup.config#L17) — 1 reference
- [`conf/modules/bcftools_query.config`](https://github.com/nf-core/genomicrelatedness/blob/2484e643de827050d2b6a10b150223cf9ec5c9e6/conf/modules/bcftools_query.config#L18) — 1 reference
- [`conf/modules/bwamem2_mem.config`](https://github.com/nf-core/genomicrelatedness/blob/2484e643de827050d2b6a10b150223cf9ec5c9e6/conf/modules/bwamem2_mem.config#L16) — 1 reference
- [`conf/modules/fastp.config`](https://github.com/nf-core/genomicrelatedness/blob/2484e643de827050d2b6a10b150223cf9ec5c9e6/conf/modules/fastp.config#L16) — 1 reference
- [`conf/modules/gatk4_addorreplacereadgroups.config`](https://github.com/nf-core/genomicrelatedness/blob/2484e643de827050d2b6a10b150223cf9ec5c9e6/conf/modules/gatk4_addorreplacereadgroups.config#L21) — 1 reference
- [`conf/modules/gatk4_markduplicates.config`](https://github.com/nf-core/genomicrelatedness/blob/2484e643de827050d2b6a10b150223cf9ec5c9e6/conf/modules/gatk4_markduplicates.config#L17) — 1 reference
- [`conf/modules/gunzip.config`](https://github.com/nf-core/genomicrelatedness/blob/2484e643de827050d2b6a10b150223cf9ec5c9e6/conf/modules/gunzip.config#L16) — 1 reference
- [`conf/modules/mosdepth.config`](https://github.com/nf-core/genomicrelatedness/blob/2484e643de827050d2b6a10b150223cf9ec5c9e6/conf/modules/mosdepth.config#L16) — 1 reference
- [`conf/modules/normalize_bam_names.config`](https://github.com/nf-core/genomicrelatedness/blob/2484e643de827050d2b6a10b150223cf9ec5c9e6/conf/modules/normalize_bam_names.config#L16) — 1 reference
- [`conf/modules/preseq_ccurve.config`](https://github.com/nf-core/genomicrelatedness/blob/2484e643de827050d2b6a10b150223cf9ec5c9e6/conf/modules/preseq_ccurve.config#L16) — 1 reference
- [`conf/modules/preseq_lcextrap.config`](https://github.com/nf-core/genomicrelatedness/blob/2484e643de827050d2b6a10b150223cf9ec5c9e6/conf/modules/preseq_lcextrap.config#L18) — 1 reference
- [`conf/modules/samtools_convert.config`](https://github.com/nf-core/genomicrelatedness/blob/2484e643de827050d2b6a10b150223cf9ec5c9e6/conf/modules/samtools_convert.config#L16) — 1 reference
- [`conf/modules/samtools_stats.config`](https://github.com/nf-core/genomicrelatedness/blob/2484e643de827050d2b6a10b150223cf9ec5c9e6/conf/modules/samtools_stats.config#L16) — 1 reference
- [`conf/modules/splitintervals.config`](https://github.com/nf-core/genomicrelatedness/blob/2484e643de827050d2b6a10b150223cf9ec5c9e6/conf/modules/splitintervals.config#L17) — 1 reference
- [`conf/modules/spring.config`](https://github.com/nf-core/genomicrelatedness/blob/2484e643de827050d2b6a10b150223cf9ec5c9e6/conf/modules/spring.config#L16) — 1 reference
- [`conf/subworkflows/prepare_intervals.config`](https://github.com/nf-core/genomicrelatedness/blob/2484e643de827050d2b6a10b150223cf9ec5c9e6/conf/subworkflows/prepare_intervals.config#L16) — 1 reference
- [`modules/nf-core/spring/decompress/tests/nextflow.config`](https://github.com/nf-core/genomicrelatedness/blob/2484e643de827050d2b6a10b150223cf9ec5c9e6/modules/nf-core/spring/decompress/tests/nextflow.config#L3) — 1 reference
