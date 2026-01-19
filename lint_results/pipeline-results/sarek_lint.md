# Nextflow lint results

- Generated: 2026-01-19T00:17:14.431378667Z
- Nextflow version: 25.12.0-edge
- Summary: 152 errors, 614 warnings

## :x: Errors

- Error: `conf/modules/aligner.config:19:17`: Unexpected input: ':'

  ```nextflow
          withName: 'BWAMEM1_MEM' {
                  ^
  ```

- Error: `conf/modules/annotate.config:20:17`: Unexpected input: ':'

  ```nextflow
          withName: 'SNPEFF_SNPEFF' {
                  ^
  ```

- Error: `conf/modules/freebayes.config:75:17`: Unexpected input: ':'

  ```nextflow
          withName: '.*:BAM_VARIANT_CALLING_SOMATIC_ALL:BAM_VARIANT_CALLING_FREEBAYES:FREEBAYES' {
                  ^
  ```

- Error: `conf/modules/haplotypecaller.config:60:17`: Unexpected input: ':'

  ```nextflow
          withName: 'NFCORE_SAREK:SAREK:BAM_VARIANT_CALLING_GERMLINE_ALL:BAM_VARIANT_CALLING_HAPLOTYPECALLER:BAM_MERGE_INDEX_SAMTOOLS:(MERGE_BAM|INDEX_MERGE_BAM)' {
                  ^
  ```

- Error: `conf/modules/joint_germline.config:36:17`: Unexpected input: ':'

  ```nextflow
          withName: 'NFCORE_SAREK:SAREK:BAM_VARIANT_CALLING_GERMLINE_ALL:BAM_JOINT_CALLING_GERMLINE_GATK:BCFTOOLS_SORT' {
                  ^
  ```

- Error: `conf/modules/lofreq.config:19:17`: Unexpected input: ':'

  ```nextflow
          withName: "LOFREQ_CALLPARALLEL" {
                  ^
  ```

- Error: `conf/modules/manta.config:18:17`: Unexpected input: ':'

  ```nextflow
          withName: 'MANTA_GERMLINE|MANTA_TUMORONLY|MANTA_SOMATIC' {
                  ^
  ```

- Error: `conf/modules/markduplicates.config:122:9`: If statements cannot be mixed with config statements

  ```nextflow
          if (params.tools && params.tools.split(',').contains('sentieon_dedup')) {
          ^
  ```

- Error: `conf/modules/modules.config:78:17`: Unexpected input: ':'

  ```nextflow
          withName: 'NFCORE_SAREK:SAREK:CRAM_SAMPLEQC:CRAM_QC_RECAL:MOSDEPTH' {
                  ^
  ```

- Error: `conf/modules/mpileup.config:56:17`: Unexpected input: ':'

  ```nextflow
          withName: 'NFCORE_SAREK:SAREK:BAM_VARIANT_CALLING_GERMLINE_ALL:BAM_VARIANT_CALLING_MPILEUP:SAMTOOLS_MPILEUP' {
                  ^
  ```

- Error: `conf/modules/mutect2.config:19:17`: Unexpected input: ':'

  ```nextflow
          withName: 'GATK4_MUTECT2' {
                  ^
  ```

- Error: `conf/modules/prepare_recalibration.config:19:9`: If statements cannot be mixed with config statements

  ```nextflow
          if (params.use_gatk_spark) {
          ^
  ```

- Error: `conf/modules/recalibrate.config:47:17`: Unexpected input: ':'

  ```nextflow
          withName: 'NFCORE_SAREK:SAREK:FASTQ_PREPROCESS_GATK:(BAM_APPLYBQSR|BAM_APPLYBQSR_SPARK):CRAM_MERGE_INDEX_SAMTOOLS:MERGE_CRAM' {
                  ^
  ```

- Error: `conf/modules/sentieon_dedup.config:44:17`: Unexpected input: ':'

  ```nextflow
          withName: 'NFCORE_SAREK:SAREK:FASTQ_PREPROCESS_GATK:BAM_SENTIEON_DEDUP:CRAM_QC_MOSDEPTH_SAMTOOLS:SAMTOOLS_STATS' {
                  ^
  ```

- Error: `conf/modules/sentieon_dnascope_joint_germline.config:28:17`: Unexpected input: ':'

  ```nextflow
          withName: 'NFCORE_SAREK:SAREK:BAM_VARIANT_CALLING_GERMLINE_ALL:BAM_JOINT_CALLING_GERMLINE_SENTIEON:BCFTOOLS_SORT' {
                  ^
  ```

- Error: `conf/modules/sentieon_haplotyper.config:48:17`: Unexpected input: ':'

  ```nextflow
          withName: '.*:SENTIEON_HAPLOTYPER_VCF_VARIANT_FILTERING_GATK:FILTERVARIANTTRANCHES' {
                  ^
  ```

- Error: `conf/modules/sentieon_haplotyper_joint_germline.config:27:17`: Unexpected input: ':'

  ```nextflow
          withName: 'NFCORE_SAREK:SAREK:BAM_VARIANT_CALLING_GERMLINE_ALL:BAM_JOINT_CALLING_GERMLINE_SENTIEON:BCFTOOLS_SORT' {
                  ^
  ```

- Error: `conf/modules/tiddit.config:40:17`: Unexpected input: ':'

  ```nextflow
          withName: 'NFCORE_SAREK:SAREK:BAM_VARIANT_CALLING_SOMATIC_ALL:BAM_VARIANT_CALLING_SOMATIC_TIDDIT:TIDDIT_NORMAL:TABIX_BGZIP_TIDDIT_SV' {
                  ^
  ```

- Error: `conf/modules/umi.config:38:17`: Unexpected input: ':'

  ```nextflow
          withName: 'NFCORE_SAREK:SAREK:FASTQ_PREPROCESS_GATK:FASTQ_CREATE_UMI_CONSENSUS_FGBIO:ALIGN_UMI:BWAMEM.*_MEM' {
                  ^
  ```

- Error: `main.nf:76:1`: Module could not be parsed: '/home/runner/work/strict-syntax-health/strict-syntax-health/pipelines/sarek/subworkflows/local/prepare_intervals/main.nf'

  ```nextflow
  include { PREPARE_INTERVALS               } from './subworkflows/local/prepare_intervals'
  ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  ```

- Error: `main.nf:129:5`: `PREPARE_INTERVALS` is not defined

  ```nextflow
      PREPARE_INTERVALS(PREPARE_GENOME.out.fasta_fai, params.intervals, params.no_intervals, params.nucleotides_per_second, params.outdir, params.step)
      ^^^^^^^^^^^^^^^^^
  ```

- Error: `main.nf:133:72`: `PREPARE_INTERVALS` is not defined

  ```nextflow
      intervals_bed_combined = params.no_intervals ? Channel.value([]) : PREPARE_INTERVALS.out.intervals_bed_combined
                                                                         ^^^^^^^^^^^^^^^^^
  ```

- Error: `main.nf:134:79`: `PREPARE_INTERVALS` is not defined

  ```nextflow
      intervals_bed_gz_tbi_combined = params.no_intervals ? Channel.value([]) : PREPARE_INTERVALS.out.intervals_bed_gz_tbi_combined
                                                                                ^^^^^^^^^^^^^^^^^
  ```

- Error: `main.nf:135:50`: `PREPARE_INTERVALS` is not defined

  ```nextflow
      intervals_bed_combined_for_variant_calling = PREPARE_INTERVALS.out.intervals_bed_combined
                                                   ^^^^^^^^^^^^^^^^^
  ```

- Error: `main.nf:142:17`: `PREPARE_INTERVALS` is not defined

  ```nextflow
      intervals = PREPARE_INTERVALS.out.intervals_bed
                  ^^^^^^^^^^^^^^^^^
  ```

- Error: `main.nf:144:28`: `PREPARE_INTERVALS` is not defined

  ```nextflow
      intervals_bed_gz_tbi = PREPARE_INTERVALS.out.intervals_bed_gz_tbi
                             ^^^^^^^^^^^^^^^^^
  ```

- Error: `main.nf:169:29`: `PREPARE_INTERVALS` is not defined

  ```nextflow
      versions = versions.mix(PREPARE_INTERVALS.out.versions)
                              ^^^^^^^^^^^^^^^^^
  ```

- Error: `modules/nf-core/bbmap/bbsplit/main.nf:41:43`: `index` is already declared

  ```nextflow
      other_ref_names.eachWithIndex { name, index ->
                                            ^^^^^
  ```

- Error: `modules/nf-core/bbmap/bbsplit/main.nf:116:43`: `index` is already declared

  ```nextflow
      other_ref_names.eachWithIndex { name, index ->
                                            ^^^^^
  ```

- Error: `subworkflows/local/bam_baserecalibrator/main.nf:26:21`: `cram` is already declared

  ```nextflow
          .map{ meta, cram, crai, intervals, num_intervals -> [ meta + [ num_intervals:num_intervals ], cram, crai, intervals ] }
                      ^^^^
  ```

- Error: `subworkflows/local/bam_baserecalibrator/main.nf:26:33`: `intervals` is already declared

  ```nextflow
          .map{ meta, cram, crai, intervals, num_intervals -> [ meta + [ num_intervals:num_intervals ], cram, crai, intervals ] }
                                  ^^^^^^^^^
  ```

- Error: `subworkflows/local/bam_baserecalibrator_spark/main.nf:26:21`: `cram` is already declared

  ```nextflow
          .map{ meta, cram, crai, intervals, num_intervals -> [ meta + [ num_intervals:num_intervals ], cram, crai, intervals ] }
                      ^^^^
  ```

- Error: `subworkflows/local/bam_baserecalibrator_spark/main.nf:26:33`: `intervals` is already declared

  ```nextflow
          .map{ meta, cram, crai, intervals, num_intervals -> [ meta + [ num_intervals:num_intervals ], cram, crai, intervals ] }
                                  ^^^^^^^^^
  ```

- Error: `subworkflows/local/bam_joint_calling_germline_gatk/main.nf:74:26`: `fasta` is already declared

  ```nextflow
          fasta.map{ meta, fasta -> [ fasta ] },
                           ^^^^^
  ```

- Error: `subworkflows/local/bam_joint_calling_germline_gatk/main.nf:75:24`: `fai` is already declared

  ```nextflow
          fai.map{ meta, fai -> [ fai ] },
                         ^^^
  ```

- Error: `subworkflows/local/bam_joint_calling_germline_gatk/main.nf:76:25`: `dict` is already declared

  ```nextflow
          dict.map{ meta, dict -> [ dict ] })
                          ^^^^
  ```

- Error: `subworkflows/local/bam_joint_calling_germline_gatk/main.nf:83:26`: `fasta` is already declared

  ```nextflow
          fasta.map{ meta, fasta -> [ fasta ] },
                           ^^^^^
  ```

- Error: `subworkflows/local/bam_joint_calling_germline_gatk/main.nf:84:24`: `fai` is already declared

  ```nextflow
          fai.map{ meta, fai -> [ fai ] },
                         ^^^
  ```

- Error: `subworkflows/local/bam_joint_calling_germline_gatk/main.nf:85:25`: `dict` is already declared

  ```nextflow
          dict.map{ meta, dict -> [ dict ] })
                          ^^^^
  ```

- Error: `subworkflows/local/bam_joint_calling_germline_gatk/main.nf:100:26`: `fasta` is already declared

  ```nextflow
          fasta.map{ meta, fasta -> [ fasta ] },
                           ^^^^^
  ```

- Error: `subworkflows/local/bam_joint_calling_germline_gatk/main.nf:101:24`: `fai` is already declared

  ```nextflow
          fai.map{ meta, fai -> [ fai ] },
                         ^^^
  ```

- Error: `subworkflows/local/bam_joint_calling_germline_gatk/main.nf:102:25`: `dict` is already declared

  ```nextflow
          dict.map{ meta, dict -> [ dict ] })
                          ^^^^
  ```

- Error: `subworkflows/local/bam_joint_calling_germline_gatk/main.nf:114:26`: `fasta` is already declared

  ```nextflow
          fasta.map{ meta, fasta -> [ fasta ] },
                           ^^^^^
  ```

- Error: `subworkflows/local/bam_joint_calling_germline_gatk/main.nf:115:24`: `fai` is already declared

  ```nextflow
          fai.map{ meta, fai -> [ fai ] },
                         ^^^
  ```

- Error: `subworkflows/local/bam_joint_calling_germline_gatk/main.nf:116:25`: `dict` is already declared

  ```nextflow
          dict.map{ meta, dict -> [ dict ] })
                          ^^^^
  ```

- Error: `subworkflows/local/bam_joint_calling_germline_gatk/main.nf:137:9`: Variables in a closure should be declared with `def`

  ```nextflow
          vcf_out = recal_vcf ?: joint_vcf
          ^^^^^^^
  ```

- Error: `subworkflows/local/bam_joint_calling_germline_gatk/main.nf:145:9`: Variables in a closure should be declared with `def`

  ```nextflow
          tbi_out = recal_tbi ?: joint_tbi
          ^^^^^^^
  ```

- Error: `subworkflows/local/bam_joint_calling_germline_sentieon/main.nf:125:13`: Variables in a closure should be declared with `def`

  ```nextflow
              vcf_out = recal_vcf ?: joint_vcf
              ^^^^^^^
  ```

- Error: `subworkflows/local/bam_joint_calling_germline_sentieon/main.nf:133:13`: Variables in a closure should be declared with `def`

  ```nextflow
              tbi_out = recal_tbi ?: joint_tbi
              ^^^^^^^
  ```

- Error: `subworkflows/local/bam_markduplicates/main.nf:22:48`: `fasta` is already declared

  ```nextflow
      GATK4_MARKDUPLICATES(bam, fasta.map{ meta, fasta -> [ fasta ] }, fasta_fai.map{ meta, fasta_fai -> [ fasta_fai ] })
                                                 ^^^^^
  ```

- Error: `subworkflows/local/bam_markduplicates/main.nf:22:91`: `fasta_fai` is already declared

  ```nextflow
      GATK4_MARKDUPLICATES(bam, fasta.map{ meta, fasta -> [ fasta ] }, fasta_fai.map{ meta, fasta_fai -> [ fasta_fai ] })
                                                                                            ^^^^^^^^^
  ```

- Error: `subworkflows/local/bam_markduplicates_spark/main.nf:25:53`: `fasta` is already declared

  ```nextflow
      GATK4SPARK_MARKDUPLICATES(bam, fasta.map{ meta, fasta -> [ fasta ] }, fasta_fai.map{ meta, fasta_fai -> [ fasta_fai ] }, dict.map{ meta, dict -> [ dict ] })
                                                      ^^^^^
  ```

- Error: `subworkflows/local/bam_markduplicates_spark/main.nf:25:96`: `fasta_fai` is already declared

  ```nextflow
      GATK4SPARK_MARKDUPLICATES(bam, fasta.map{ meta, fasta -> [ fasta ] }, fasta_fai.map{ meta, fasta_fai -> [ fasta_fai ] }, dict.map{ meta, dict -> [ dict ] })
                                                                                                 ^^^^^^^^^
  ```

- Error: `subworkflows/local/bam_markduplicates_spark/main.nf:25:142`: `dict` is already declared

  ```nextflow
      GATK4SPARK_MARKDUPLICATES(bam, fasta.map{ meta, fasta -> [ fasta ] }, fasta_fai.map{ meta, fasta_fai -> [ fasta_fai ] }, dict.map{ meta, dict -> [ dict ] })
                                                                                                                                               ^^^^
  ```

- Error: `subworkflows/local/bam_markduplicates_spark/main.nf:37:59`: `fasta` is already declared

  ```nextflow
      GATK4_ESTIMATELIBRARYCOMPLEXITY(bam, fasta.map{ meta, fasta -> [ fasta ] }, fasta_fai.map{ meta, fasta_fai -> [ fasta_fai ] }, dict.map{ meta, dict -> [ dict ] })
                                                            ^^^^^
  ```

- Error: `subworkflows/local/bam_markduplicates_spark/main.nf:37:102`: `fasta_fai` is already declared

  ```nextflow
      GATK4_ESTIMATELIBRARYCOMPLEXITY(bam, fasta.map{ meta, fasta -> [ fasta ] }, fasta_fai.map{ meta, fasta_fai -> [ fasta_fai ] }, dict.map{ meta, dict -> [ dict ] })
                                                                                                       ^^^^^^^^^
  ```

- Error: `subworkflows/local/bam_markduplicates_spark/main.nf:37:148`: `dict` is already declared

  ```nextflow
      GATK4_ESTIMATELIBRARYCOMPLEXITY(bam, fasta.map{ meta, fasta -> [ fasta ] }, fasta_fai.map{ meta, fasta_fai -> [ fasta_fai ] }, dict.map{ meta, dict -> [ dict ] })
                                                                                                                                                     ^^^^
  ```

- Error: `subworkflows/local/bam_sentieon_dedup/main.nf:19:26`: `bam` is already declared

  ```nextflow
      bam = bam.map{ meta, bam -> [ meta - meta.subMap('data_type'), bam ] }
                           ^^^
  ```

- Error: `subworkflows/local/bam_sentieon_dedup/main.nf:20:26`: `bai` is already declared

  ```nextflow
      bai = bai.map{ meta, bai -> [ meta - meta.subMap('data_type'), bai ] }
                           ^^^
  ```

- Error: `subworkflows/local/bam_variant_calling_deepvariant/main.nf:26:21`: `cram` is already declared

  ```nextflow
          .map{ meta, cram, crai, intervals, num_intervals -> [ meta + [ num_intervals:num_intervals ], cram, crai, intervals ]}
                      ^^^^
  ```

- Error: `subworkflows/local/bam_variant_calling_deepvariant/main.nf:26:33`: `intervals` is already declared

  ```nextflow
          .map{ meta, cram, crai, intervals, num_intervals -> [ meta + [ num_intervals:num_intervals ], cram, crai, intervals ]}
                                  ^^^^^^^^^
  ```

- Error: `subworkflows/local/bam_variant_calling_germline_all/main.nf:98:29`: `cram` is already declared

  ```nextflow
              cram.map{ meta, cram, crai -> [ meta, [], cram ] },
                              ^^^^
  ```

- Error: `subworkflows/local/bam_variant_calling_germline_all/main.nf:127:29`: `cram` is already declared

  ```nextflow
              cram.map{ meta, cram, crai -> [ meta, cram, crai, [], [] ] },
                              ^^^^
  ```

- Error: `subworkflows/local/bam_variant_calling_germline_all/main.nf:181:38`: `fasta` is already declared

  ```nextflow
                      fasta.map{ meta, fasta -> [ fasta ] },
                                       ^^^^^
  ```

- Error: `subworkflows/local/bam_variant_calling_germline_all/main.nf:182:42`: `fasta_fai` is already declared

  ```nextflow
                      fasta_fai.map{ meta, fasta_fai -> [ fasta_fai ] },
                                           ^^^^^^^^^
  ```

- Error: `subworkflows/local/bam_variant_calling_germline_all/main.nf:183:37`: `dict` is already declared

  ```nextflow
                      dict.map{ meta, dict -> [ dict ] },
                                      ^^^^
  ```

- Error: `subworkflows/local/bam_variant_calling_germline_all/main.nf:334:37`: `dict` is already declared

  ```nextflow
                      dict.map{ meta, dict -> [ dict ] },
                                      ^^^^
  ```

- Error: `subworkflows/local/bam_variant_calling_germline_all/main.nf:354:30`: `fasta` is already declared

  ```nextflow
              fasta.map{ meta, fasta -> [ fasta ] },
                               ^^^^^
  ```

- Error: `subworkflows/local/bam_variant_calling_germline_all/main.nf:355:34`: `fasta_fai` is already declared

  ```nextflow
              fasta_fai.map{ meta, fasta_fai -> [ fasta_fai ] },
                                   ^^^^^^^^^
  ```

- Error: `subworkflows/local/bam_variant_calling_germline_manta/main.nf:22:9`: Variables in a closure should be declared with `def`

  ```nextflow
          bed_gz = it.size() > 3 ? it[3] : []
          ^^^^^^
  ```

- Error: `subworkflows/local/bam_variant_calling_germline_manta/main.nf:23:9`: Variables in a closure should be declared with `def`

  ```nextflow
          bed_tbi = it.size() > 3 ? it[4] : []
          ^^^^^^^
  ```

- Error: `subworkflows/local/bam_variant_calling_haplotypecaller/main.nf:31:21`: `cram` is already declared

  ```nextflow
          .map{ meta, cram, crai, intervals, num_intervals -> [ meta + [ interval_name:intervals.baseName, num_intervals:num_intervals, variantcaller:'haplotypecaller' ], cram, crai, intervals, [] ] }
                      ^^^^
  ```

- Error: `subworkflows/local/bam_variant_calling_haplotypecaller/main.nf:31:33`: `intervals` is already declared

  ```nextflow
          .map{ meta, cram, crai, intervals, num_intervals -> [ meta + [ interval_name:intervals.baseName, num_intervals:num_intervals, variantcaller:'haplotypecaller' ], cram, crai, intervals, [] ] }
                                  ^^^^^^^^^
  ```

- Error: `subworkflows/local/bam_variant_calling_haplotypecaller/main.nf:45:32`: `cram` is already declared

  ```nextflow
          .map{ meta, gvcf, tbi, cram, crai, intervals, dragstr_model -> [ meta, gvcf, tbi, intervals ] }
                                 ^^^^
  ```

- Error: `subworkflows/local/bam_variant_calling_haplotypecaller/main.nf:45:44`: `intervals` is already declared

  ```nextflow
          .map{ meta, gvcf, tbi, cram, crai, intervals, dragstr_model -> [ meta, gvcf, tbi, intervals ] }
                                             ^^^^^^^^^
  ```

- Error: `subworkflows/local/bam_variant_calling_haplotypecaller/main.nf:49:19`: `vcf` is already declared

  ```nextflow
              meta, vcf -> [ meta - meta.subMap('interval_name'), vcf]
                    ^^^
  ```

- Error: `subworkflows/local/bam_variant_calling_haplotypecaller/main.nf:76:68`: `vcf` is already declared

  ```nextflow
      MERGE_HAPLOTYPECALLER(haplotypecaller_vcf.intervals.map{ meta, vcf -> [ groupKey(meta, meta.num_intervals), vcf ] }.groupTuple(), dict)
                                                                     ^^^
  ```

- Error: `subworkflows/local/bam_variant_calling_haplotypecaller/main.nf:98:42`: `vcf` is already declared

  ```nextflow
      vcf = haplotypecaller_vcf.map{ meta, vcf -> [ meta - meta.subMap('num_intervals'), vcf ] }
                                           ^^^
  ```

- Error: `subworkflows/local/bam_variant_calling_sentieon_dnascope/main.nf:36:21`: `cram` is already declared

  ```nextflow
          .map{ meta, cram, crai, intervals, num_intervals -> [
                      ^^^^
  ```

- Error: `subworkflows/local/bam_variant_calling_sentieon_dnascope/main.nf:36:33`: `intervals` is already declared

  ```nextflow
          .map{ meta, cram, crai, intervals, num_intervals -> [
                                  ^^^^^^^^^
  ```

- Error: `subworkflows/local/bam_variant_calling_sentieon_dnascope/main.nf:66:25`: `gvcf` is already declared

  ```nextflow
              .map{ meta, gvcf, tbi, cram, crai, intervals -> [ meta, gvcf, tbi, intervals ] }
                          ^^^^
  ```

- Error: `subworkflows/local/bam_variant_calling_sentieon_dnascope/main.nf:66:36`: `cram` is already declared

  ```nextflow
              .map{ meta, gvcf, tbi, cram, crai, intervals -> [ meta, gvcf, tbi, intervals ] }
                                     ^^^^
  ```

- Error: `subworkflows/local/bam_variant_calling_sentieon_dnascope/main.nf:66:48`: `intervals` is already declared

  ```nextflow
              .map{ meta, gvcf, tbi, cram, crai, intervals -> [ meta, gvcf, tbi, intervals ] }
                                                 ^^^^^^^^^
  ```

- Error: `subworkflows/local/bam_variant_calling_sentieon_dnascope/main.nf:71:19`: `vcf` is already declared

  ```nextflow
              meta, vcf -> [ meta - meta.subMap('interval_name'), vcf]
                    ^^^
  ```

- Error: `subworkflows/local/bam_variant_calling_sentieon_dnascope/main.nf:87:19`: `gvcf` is already declared

  ```nextflow
              meta, gvcf -> [ meta - meta.subMap('interval_name'), gvcf]
                    ^^^^
  ```

- Error: `subworkflows/local/bam_variant_calling_sentieon_dnascope/main.nf:103:15`: `vcf` is already declared

  ```nextflow
          meta, vcf -> [ groupKey(meta, meta.num_intervals), vcf ]}
                ^^^
  ```

- Error: `subworkflows/local/bam_variant_calling_sentieon_dnascope/main.nf:106:15`: `vcf` is already declared

  ```nextflow
          meta, vcf -> [
                ^^^
  ```

- Error: `subworkflows/local/bam_variant_calling_sentieon_dnascope/main.nf:123:35`: `vcf` is already declared

  ```nextflow
      vcf = dnascope_vcf.map{ meta, vcf -> [ meta - meta.subMap('num_intervals'), vcf ] }
                                    ^^^
  ```

- Error: `subworkflows/local/bam_variant_calling_sentieon_dnascope/main.nf:129:15`: `vcf` is already declared

  ```nextflow
          meta, vcf -> [groupKey(meta, meta.num_intervals), vcf]}
                ^^^
  ```

- Error: `subworkflows/local/bam_variant_calling_sentieon_dnascope/main.nf:132:15`: `vcf` is already declared

  ```nextflow
          meta, vcf -> [ meta - meta.subMap('intervals_name'), vcf ]
                ^^^
  ```

- Error: `subworkflows/local/bam_variant_calling_sentieon_haplotyper/main.nf:34:21`: `cram` is already declared

  ```nextflow
          .map{ meta, cram, crai, intervals, num_intervals -> [
                      ^^^^
  ```

- Error: `subworkflows/local/bam_variant_calling_sentieon_haplotyper/main.nf:34:33`: `intervals` is already declared

  ```nextflow
          .map{ meta, cram, crai, intervals, num_intervals -> [
                                  ^^^^^^^^^
  ```

- Error: `subworkflows/local/bam_variant_calling_sentieon_haplotyper/main.nf:50:48`: `cram` is already declared

  ```nextflow
          cram_intervals_for_sentieon.map{ meta, cram, crai, intervals -> [ meta, cram, crai, intervals, [] ]},
                                                 ^^^^
  ```

- Error: `subworkflows/local/bam_variant_calling_sentieon_haplotyper/main.nf:50:60`: `intervals` is already declared

  ```nextflow
          cram_intervals_for_sentieon.map{ meta, cram, crai, intervals -> [ meta, cram, crai, intervals, [] ]},
                                                             ^^^^^^^^^
  ```

- Error: `subworkflows/local/bam_variant_calling_sentieon_haplotyper/main.nf:62:25`: `gvcf` is already declared

  ```nextflow
              .map{ meta, gvcf, tbi, cram, crai, intervals -> [ meta, gvcf, tbi, intervals ] }
                          ^^^^
  ```

- Error: `subworkflows/local/bam_variant_calling_sentieon_haplotyper/main.nf:62:36`: `cram` is already declared

  ```nextflow
              .map{ meta, gvcf, tbi, cram, crai, intervals -> [ meta, gvcf, tbi, intervals ] }
                                     ^^^^
  ```

- Error: `subworkflows/local/bam_variant_calling_sentieon_haplotyper/main.nf:62:48`: `intervals` is already declared

  ```nextflow
              .map{ meta, gvcf, tbi, cram, crai, intervals -> [ meta, gvcf, tbi, intervals ] }
                                                 ^^^^^^^^^
  ```

- Error: `subworkflows/local/bam_variant_calling_sentieon_haplotyper/main.nf:67:19`: `vcf` is already declared

  ```nextflow
              meta, vcf -> [ meta - meta.subMap('interval_name'), vcf]
                    ^^^
  ```

- Error: `subworkflows/local/bam_variant_calling_sentieon_haplotyper/main.nf:83:19`: `gvcf` is already declared

  ```nextflow
              meta, gvcf -> [ meta - meta.subMap('interval_name'), gvcf]
                    ^^^^
  ```

- Error: `subworkflows/local/bam_variant_calling_sentieon_haplotyper/main.nf:99:15`: `vcf` is already declared

  ```nextflow
          meta, vcf -> [ groupKey(meta, meta.num_intervals), vcf ]}
                ^^^
  ```

- Error: `subworkflows/local/bam_variant_calling_sentieon_haplotyper/main.nf:102:15`: `vcf` is already declared

  ```nextflow
          meta, vcf -> [
                ^^^
  ```

- Error: `subworkflows/local/bam_variant_calling_sentieon_haplotyper/main.nf:119:37`: `vcf` is already declared

  ```nextflow
      vcf = haplotyper_vcf.map{ meta, vcf -> [ meta - meta.subMap('num_intervals'), vcf ] }
                                      ^^^
  ```

- Error: `subworkflows/local/bam_variant_calling_sentieon_haplotyper/main.nf:125:15`: `vcf` is already declared

  ```nextflow
          meta, vcf -> [groupKey(meta, meta.num_intervals), vcf]}
                ^^^
  ```

- Error: `subworkflows/local/bam_variant_calling_sentieon_haplotyper/main.nf:128:15`: `vcf` is already declared

  ```nextflow
          meta, vcf -> [ meta - meta.subMap('intervals_name'), vcf ]
                ^^^
  ```

- Error: `subworkflows/local/bam_variant_calling_single_strelka/main.nf:25:21`: `cram` is already declared

  ```nextflow
          .map{ meta, cram, crai, intervals, intervals_index, num_intervals -> [ meta + [ num_intervals:num_intervals ], cram, crai, intervals, intervals_index ] }
                      ^^^^
  ```

- Error: `subworkflows/local/bam_variant_calling_single_strelka/main.nf:25:33`: `intervals` is already declared

  ```nextflow
          .map{ meta, cram, crai, intervals, intervals_index, num_intervals -> [ meta + [ num_intervals:num_intervals ], cram, crai, intervals, intervals_index ] }
                                  ^^^^^^^^^
  ```

- Error: `subworkflows/local/bam_variant_calling_somatic_manta/main.nf:21:9`: Variables in a closure should be declared with `def`

  ```nextflow
          bed_gz = it.size() > 5 ? it[5] : []
          ^^^^^^
  ```

- Error: `subworkflows/local/bam_variant_calling_somatic_manta/main.nf:22:9`: Variables in a closure should be declared with `def`

  ```nextflow
          bed_tbi = it.size() > 5 ? it[6] : []
          ^^^^^^^
  ```

- Error: `subworkflows/local/bam_variant_calling_somatic_strelka/main.nf:25:93`: `intervals` is already declared

  ```nextflow
          .map{ meta, normal_cram, normal_crai, tumor_cram, tumor_crai, manta_vcf, manta_tbi, intervals, intervals_index, num_intervals -> [ meta + [ num_intervals:num_intervals ], normal_cram, normal_crai, tumor_cram, tumor_crai, manta_vcf, manta_tbi, intervals, intervals_index ] }
                                                                                              ^^^^^^^^^
  ```

- Error: `subworkflows/local/bam_variant_calling_tumor_only_lofreq/main.nf:18:45`: `intervals` is already declared

  ```nextflow
          .map {meta, tumor_cram, tumor_crai, intervals, num_intervals -> [meta + [ num_intervals:num_intervals ], tumor_cram, tumor_crai, intervals]}
                                              ^^^^^^^^^
  ```

- Error: `subworkflows/local/bam_variant_calling_tumor_only_manta/main.nf:22:9`: Variables in a closure should be declared with `def`

  ```nextflow
          bed_gz = it.size() > 3 ? it[3] : []
          ^^^^^^
  ```

- Error: `subworkflows/local/bam_variant_calling_tumor_only_manta/main.nf:23:9`: Variables in a closure should be declared with `def`

  ```nextflow
          bed_tbi = it.size() > 3 ? it[4] : []
          ^^^^^^^
  ```

- Error: `subworkflows/local/channel_align_create_csv/main.nf:14:13`: Variables in a closure should be declared with `def`

  ```nextflow
              patient = meta.patient
              ^^^^^^^
  ```

- Error: `subworkflows/local/channel_align_create_csv/main.nf:15:13`: Variables in a closure should be declared with `def`

  ```nextflow
              sample  = meta.sample
              ^^^^^^
  ```

- Error: `subworkflows/local/channel_align_create_csv/main.nf:16:13`: Variables in a closure should be declared with `def`

  ```nextflow
              sex     = meta.sex
              ^^^
  ```

- Error: `subworkflows/local/channel_align_create_csv/main.nf:17:13`: Variables in a closure should be declared with `def`

  ```nextflow
              status  = meta.status
              ^^^^^^
  ```

- Error: `subworkflows/local/channel_align_create_csv/main.nf:21:13`: Variables in a closure should be declared with `def`

  ```nextflow
              type = save_output_as_bam ? "bam" : "cram"
              ^^^^
  ```

- Error: `subworkflows/local/channel_align_create_csv/main.nf:22:13`: Variables in a closure should be declared with `def`

  ```nextflow
              type_index = save_output_as_bam ? "bai" : "crai"
              ^^^^^^^^^^
  ```

- Error: `subworkflows/local/channel_applybqsr_create_csv/main.nf:14:13`: Variables in a closure should be declared with `def`

  ```nextflow
              patient = meta.patient
              ^^^^^^^
  ```

- Error: `subworkflows/local/channel_applybqsr_create_csv/main.nf:15:13`: Variables in a closure should be declared with `def`

  ```nextflow
              sample  = meta.sample
              ^^^^^^
  ```

- Error: `subworkflows/local/channel_applybqsr_create_csv/main.nf:16:13`: Variables in a closure should be declared with `def`

  ```nextflow
              sex     = meta.sex
              ^^^
  ```

- Error: `subworkflows/local/channel_applybqsr_create_csv/main.nf:17:13`: Variables in a closure should be declared with `def`

  ```nextflow
              status  = meta.status
              ^^^^^^
  ```

- Error: `subworkflows/local/channel_applybqsr_create_csv/main.nf:21:13`: Variables in a closure should be declared with `def`

  ```nextflow
              type = save_output_as_bam ? "bam" : "cram"
              ^^^^
  ```

- Error: `subworkflows/local/channel_applybqsr_create_csv/main.nf:22:13`: Variables in a closure should be declared with `def`

  ```nextflow
              type_index = save_output_as_bam ? "bai" : "crai"
              ^^^^^^^^^^
  ```

- Error: `subworkflows/local/channel_baserecalibrator_create_csv/main.nf:18:17`: Variables in a closure should be declared with `def`

  ```nextflow
                  patient = meta.patient
                  ^^^^^^^
  ```

- Error: `subworkflows/local/channel_baserecalibrator_create_csv/main.nf:19:17`: Variables in a closure should be declared with `def`

  ```nextflow
                  sample  = meta.sample
                  ^^^^^^
  ```

- Error: `subworkflows/local/channel_baserecalibrator_create_csv/main.nf:20:17`: Variables in a closure should be declared with `def`

  ```nextflow
                  sex     = meta.sex
                  ^^^
  ```

- Error: `subworkflows/local/channel_baserecalibrator_create_csv/main.nf:21:17`: Variables in a closure should be declared with `def`

  ```nextflow
                  status  = meta.status
                  ^^^^^^
  ```

- Error: `subworkflows/local/channel_baserecalibrator_create_csv/main.nf:22:17`: Variables in a closure should be declared with `def`

  ```nextflow
                  suffix_aligned = save_output_as_bam ? "bam" : "cram"
                  ^^^^^^^^^^^^^^
  ```

- Error: `subworkflows/local/channel_baserecalibrator_create_csv/main.nf:23:17`: Variables in a closure should be declared with `def`

  ```nextflow
                  suffix_index   = save_output_as_bam ? "bam.bai" : "cram.crai"
                  ^^^^^^^^^^^^
  ```

- Error: `subworkflows/local/channel_baserecalibrator_create_csv/main.nf:28:17`: Variables in a closure should be declared with `def`

  ```nextflow
                  type = save_output_as_bam ? "bam" : "cram"
                  ^^^^
  ```

- Error: `subworkflows/local/channel_baserecalibrator_create_csv/main.nf:29:17`: Variables in a closure should be declared with `def`

  ```nextflow
                  type_index = save_output_as_bam ? "bai" : "crai"
                  ^^^^^^^^^^
  ```

- Error: `subworkflows/local/channel_markduplicates_create_csv/main.nf:15:13`: Variables in a closure should be declared with `def`

  ```nextflow
              patient        = meta.patient
              ^^^^^^^
  ```

- Error: `subworkflows/local/channel_markduplicates_create_csv/main.nf:16:13`: Variables in a closure should be declared with `def`

  ```nextflow
              sample         = meta.sample
              ^^^^^^
  ```

- Error: `subworkflows/local/channel_markduplicates_create_csv/main.nf:17:13`: Variables in a closure should be declared with `def`

  ```nextflow
              sex            = meta.sex
              ^^^
  ```

- Error: `subworkflows/local/channel_markduplicates_create_csv/main.nf:18:13`: Variables in a closure should be declared with `def`

  ```nextflow
              status         = meta.status
              ^^^^^^
  ```

- Error: `subworkflows/local/channel_markduplicates_create_csv/main.nf:19:13`: Variables in a closure should be declared with `def`

  ```nextflow
              suffix_aligned = save_output_as_bam ? "bam" : "cram"
              ^^^^^^^^^^^^^^
  ```

- Error: `subworkflows/local/channel_markduplicates_create_csv/main.nf:20:13`: Variables in a closure should be declared with `def`

  ```nextflow
              suffix_index   = save_output_as_bam ? "bam.bai" : "cram.crai"
              ^^^^^^^^^^^^
  ```

- Error: `subworkflows/local/channel_markduplicates_create_csv/main.nf:24:13`: Variables in a closure should be declared with `def`

  ```nextflow
              type = save_output_as_bam ? "bam" : "cram"
              ^^^^
  ```

- Error: `subworkflows/local/channel_markduplicates_create_csv/main.nf:25:13`: Variables in a closure should be declared with `def`

  ```nextflow
              type_index = save_output_as_bam ? "bai" : "crai"
              ^^^^^^^^^^
  ```

- Error: `subworkflows/local/channel_variant_calling_create_csv/main.nf:13:13`: Variables in a closure should be declared with `def`

  ```nextflow
              patient       = meta.patient
              ^^^^^^^
  ```

- Error: `subworkflows/local/channel_variant_calling_create_csv/main.nf:14:13`: Variables in a closure should be declared with `def`

  ```nextflow
              sample        = meta.id
              ^^^^^^
  ```

- Error: `subworkflows/local/channel_variant_calling_create_csv/main.nf:15:13`: Variables in a closure should be declared with `def`

  ```nextflow
              variantcaller = meta.variantcaller
              ^^^^^^^^^^^^^
  ```

- Error: `subworkflows/local/cram_merge_index_samtools/main.nf:20:41`: `cram` is already declared

  ```nextflow
      cram_to_merge = cram.branch { meta, cram ->
                                          ^^^^
  ```

- Error: `subworkflows/local/fastq_align/main.nf:38:62`: `bam` is already declared

  ```nextflow
      bam = bam.mix(SENTIEON_BWAMEM.out.bam_and_bai.map{ meta, bam, bai -> [ meta, bam ] })
                                                               ^^^
  ```

- Error: `subworkflows/local/fastq_align/main.nf:40:54`: `bam` is already declared

  ```nextflow
      bai = SENTIEON_BWAMEM.out.bam_and_bai.map{ meta, bam, bai -> [ meta, bai ] }
                                                       ^^^
  ```

- Error: `subworkflows/local/prepare_intervals/main.nf:77:34`: Unexpected input: '='

  ```nextflow
                      final fields = line.split('\t')
                                   ^
  ```

- Error: `subworkflows/local/vcf_variant_filtering_gatk/main.nf:20:61`: `vcf` is already declared

  ```nextflow
      cnn_in = vcf.combine(intervals_bed_combined).map{ meta, vcf, tbi, intervals -> [ meta, vcf, tbi, [], intervals ] }
                                                              ^^^
  ```

- Error: `subworkflows/local/vcf_variant_filtering_gatk/main.nf:28:21`: `vcf` is already declared

  ```nextflow
          .map{ meta, vcf -> [ meta - meta.subMap('num_intervals'), vcf ] }
                      ^^^
  ```

- Error: `tests/nextflow.config:22:1`: If statements cannot be mixed with config statements

  ```nextflow
  if (System.getenv('SENTIEON_LICSRVR_IP')) {
  ^
  ```

- Error: `tests/nextflow.config:26:1`: If statements cannot be mixed with config statements

  ```nextflow
  if (System.getenv('SENTIEON_AUTH_MECH')) {
  ^
  ```

- Error: `tests/nextflow.config:29:1`: If statements cannot be mixed with config statements

  ```nextflow
  if (secrets.SENTIEON_AUTH_DATA) {
  ^
  ```

## :warning: Warnings

- Warning: `conf/modules/contamination.config:17:55`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
                  saveAs: { params.save_bbsplit_reads ? it : null }
                                                        ^^
  ```

- Warning: `conf/modules/deepvariant.config:29:81`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
              saveAs: { meta.num_intervals > 1 ? null : "deepvariant/${meta.id}/${it}" }
                                                                                  ^^
  ```

- Warning: `conf/modules/markduplicates.config:32:52`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
              saveAs: { !params.save_output_as_bam ? it : null }
                                                     ^^
  ```

- Warning: `conf/modules/markduplicates.config:59:52`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
              saveAs: { !params.save_output_as_bam ? it : null }
                                                     ^^
  ```

- Warning: `conf/modules/markduplicates.config:88:56`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
                  saveAs: { !params.save_output_as_bam ? it : null }
                                                         ^^
  ```

- Warning: `conf/modules/markduplicates.config:94:145`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
                  saveAs: { !(params.skip_tools && params.skip_tools.split(',').contains('markduplicates_report')) ? "markduplicates/${meta.id}/${it}" : null}
                                                                                                                                                  ^^
  ```

- Warning: `conf/modules/markduplicates.config:107:52`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
              saveAs: { !params.save_output_as_bam ? it : null }
                                                     ^^
  ```

- Warning: `conf/modules/markduplicates.config:116:52`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
              saveAs: { !params.save_output_as_bam ? it : null }
                                                     ^^
  ```

- Warning: `conf/modules/prepare_genome.config:22:74`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
              saveAs: { params.save_reference || params.build_only_index ? it : null }
                                                                           ^^
  ```

- Warning: `conf/modules/prepare_genome.config:32:74`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
              saveAs: { params.save_reference || params.build_only_index ? it : null }
                                                                           ^^
  ```

- Warning: `conf/modules/prepare_genome.config:41:74`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
              saveAs: { params.save_reference || params.build_only_index ? it : null }
                                                                           ^^
  ```

- Warning: `conf/modules/prepare_genome.config:51:84`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
              saveAs: { params.save_reference || params.build_only_index ? "cnvkit/${it}" : null }
                                                                                     ^^
  ```

- Warning: `conf/modules/prepare_genome.config:62:84`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
              saveAs: { params.save_reference || params.build_only_index ? "cnvkit/${it}" : null }
                                                                                     ^^
  ```

- Warning: `conf/modules/prepare_genome.config:71:74`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
              saveAs: { params.save_reference || params.build_only_index ? it : null }
                                                                           ^^
  ```

- Warning: `conf/modules/prepare_genome.config:80:74`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
              saveAs: { params.save_reference || params.build_only_index ? it : null }
                                                                           ^^
  ```

- Warning: `conf/modules/prepare_genome.config:89:74`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
              saveAs: { params.save_reference || params.build_only_index ? it : null }
                                                                           ^^
  ```

- Warning: `conf/modules/prepare_genome.config:98:74`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
              saveAs: { params.save_reference || params.build_only_index ? it : null }
                                                                           ^^
  ```

- Warning: `conf/modules/prepare_genome.config:107:74`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
              saveAs: { params.save_reference || params.build_only_index ? it : null }
                                                                           ^^
  ```

- Warning: `conf/modules/prepare_genome.config:116:74`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
              saveAs: { params.save_reference || params.build_only_index ? it : null }
                                                                           ^^
  ```

- Warning: `conf/modules/prepare_genome.config:125:74`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
              saveAs: { params.save_reference || params.build_only_index ? it : null }
                                                                           ^^
  ```

- Warning: `conf/modules/prepare_genome.config:134:74`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
              saveAs: { params.save_reference || params.build_only_index ? it : null }
                                                                           ^^
  ```

- Warning: `conf/modules/prepare_genome.config:143:74`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
              saveAs: { params.save_reference || params.build_only_index ? it : null }
                                                                           ^^
  ```

- Warning: `conf/modules/prepare_genome.config:152:74`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
              saveAs: { params.save_reference || params.build_only_index ? it : null }
                                                                           ^^
  ```

- Warning: `conf/modules/prepare_genome.config:161:74`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
              saveAs: { params.save_reference || params.build_only_index ? it : null }
                                                                           ^^
  ```

- Warning: `conf/modules/prepare_genome.config:176:78`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
              saveAs: { (params.save_reference || params.build_only_index) && !it.equals('versions.yml') ? it : null }
                                                                               ^^
  ```

- Warning: `conf/modules/prepare_genome.config:176:106`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
              saveAs: { (params.save_reference || params.build_only_index) && !it.equals('versions.yml') ? it : null }
                                                                                                           ^^
  ```

- Warning: `conf/modules/prepare_genome.config:187:74`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
              saveAs: { params.save_reference || params.build_only_index ? it : null }
                                                                           ^^
  ```

- Warning: `conf/modules/prepare_intervals.config:28:87`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
              saveAs: { params.save_reference || params.build_only_index ? "intervals/${it}" : null }
                                                                                        ^^
  ```

- Warning: `conf/modules/prepare_intervals.config:37:87`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
              saveAs: { params.save_reference || params.build_only_index ? "intervals/${it}" : null }
                                                                                        ^^
  ```

- Warning: `conf/modules/prepare_intervals.config:47:87`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
              saveAs: { params.save_reference || params.build_only_index ? "intervals/${it}" : null }
                                                                                        ^^
  ```

- Warning: `conf/modules/prepare_recalibration.config:27:81`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
              saveAs: { meta.num_intervals > 1 ? null : "recal_table/${meta.id}/${it}" }
                                                                                  ^^
  ```

- Warning: `conf/modules/sentieon_dnascope.config:25:87`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
              saveAs: { meta.num_intervals > 1 ? null : "sentieon_dnascope/${meta.id}/${it}" }
                                                                                        ^^
  ```

- Warning: `conf/modules/sentieon_tnscope.config:28:86`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
              saveAs: { meta.num_intervals > 1 ? null : "sentieon_tnscope/${meta.id}/${it}" }
                                                                                       ^^
  ```

- Warning: `conf/modules/strelka.config:26:77`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
              saveAs: { meta.num_intervals > 1 ? null : "strelka/${meta.id}/${it}" }
                                                                              ^^
  ```

- Warning: `conf/modules/trimming.config:42:102`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
                  saveAs: { params.save_trimmed || params.save_split_fastqs ?  "fastp/${meta.sample}/${it}" : null }
                                                                                                       ^^
  ```

- Warning: `conf/modules/varlociraptor.config:67:96`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
              saveAs: { params.varlociraptor_chunk_size > 1 ? null : "varlociraptor/${meta.id}/${it}" }
                                                                                                 ^^
  ```

- Warning: `main.nf:91:16`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      versions = Channel.empty()
                 ^^^^^^^
  ```

- Warning: `main.nf:133:52`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      intervals_bed_combined = params.no_intervals ? Channel.value([]) : PREPARE_INTERVALS.out.intervals_bed_combined
                                                     ^^^^^^^
  ```

- Warning: `main.nf:134:59`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      intervals_bed_gz_tbi_combined = params.no_intervals ? Channel.value([]) : PREPARE_INTERVALS.out.intervals_bed_gz_tbi_combined
                                                            ^^^^^^^
  ```

- Warning: `main.nf:140:11`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
          : Channel.value([[id: 'null'], []])
            ^^^^^^^
  ```

- Warning: `main.nf:156:32`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
              cnvkit_reference = Channel.fromPath(params.cnvkit_reference).collect()
                                 ^^^^^^^
  ```

- Warning: `main.nf:165:28`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
          cnvkit_reference = Channel.value([])
                             ^^^^^^^
  ```

- Warning: `main.nf:180:27`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
          ensemblvep_info = Channel.of([[id: "${params.vep_cache_version}_${params.vep_genome}"], params.vep_genome, params.vep_species, params.vep_cache_version])
                            ^^^^^^^
  ```

- Warning: `main.nf:181:23`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
          snpeff_info = Channel.of([[id: "${params.snpeff_db}"], params.snpeff_db])
                        ^^^^^^^
  ```

- Warning: `main.nf:242:35`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
          params.bcftools_columns ? Channel.fromPath(params.bcftools_columns).collect() : Channel.value([]),
                                    ^^^^^^^
  ```

- Warning: `main.nf:242:89`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
          params.bcftools_columns ? Channel.fromPath(params.bcftools_columns).collect() : Channel.value([]),
                                                                                          ^^^^^^^
  ```

- Warning: `main.nf:243:40`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
          params.bcftools_header_lines ? Channel.fromPath(params.bcftools_header_lines).collect() : Channel.empty(),
                                         ^^^^^^^
  ```

- Warning: `main.nf:243:99`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
          params.bcftools_header_lines ? Channel.fromPath(params.bcftools_header_lines).collect() : Channel.empty(),
                                                                                                    ^^^^^^^
  ```

- Warning: `main.nf:244:31`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
          params.cf_chrom_len ? Channel.fromPath(params.cf_chrom_len).collect() : [],
                                ^^^^^^^
  ```

- Warning: `main.nf:249:29`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
          params.dbsnp_vqsr ? Channel.value(params.dbsnp_vqsr) : Channel.empty(),
                              ^^^^^^^
  ```

- Warning: `main.nf:249:64`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
          params.dbsnp_vqsr ? Channel.value(params.dbsnp_vqsr) : Channel.empty(),
                                                                 ^^^^^^^
  ```

- Warning: `main.nf:262:36`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
          params.known_indels_vqsr ? Channel.value(params.known_indels_vqsr) : Channel.empty(),
                                     ^^^^^^^
  ```

- Warning: `main.nf:262:78`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
          params.known_indels_vqsr ? Channel.value(params.known_indels_vqsr) : Channel.empty(),
                                                                               ^^^^^^^
  ```

- Warning: `main.nf:267:34`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
          params.known_snps_vqsr ? Channel.value(params.known_snps_vqsr) : Channel.empty(),
                                   ^^^^^^^
  ```

- Warning: `main.nf:267:74`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
          params.known_snps_vqsr ? Channel.value(params.known_snps_vqsr) : Channel.empty(),
                                                                           ^^^^^^^
  ```

- Warning: `main.nf:268:30`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
          params.mappability ? Channel.fromPath(params.mappability).collect() : Channel.value([]),
                               ^^^^^^^
  ```

- Warning: `main.nf:268:79`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
          params.mappability ? Channel.fromPath(params.mappability).collect() : Channel.value([]),
                                                                                ^^^^^^^
  ```

- Warning: `main.nf:271:35`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
          params.ngscheckmate_bed ? Channel.value(params.ngscheckmate_bed) : Channel.empty(),
                                    ^^^^^^^
  ```

- Warning: `main.nf:271:76`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
          params.ngscheckmate_bed ? Channel.value(params.ngscheckmate_bed) : Channel.empty(),
                                                                             ^^^^^^^
  ```

- Warning: `main.nf:274:42`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
          params.sentieon_dnascope_model ? Channel.fromPath(params.sentieon_dnascope_model).collect() : Channel.value([]),
                                           ^^^^^^^
  ```

- Warning: `main.nf:274:103`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
          params.sentieon_dnascope_model ? Channel.fromPath(params.sentieon_dnascope_model).collect() : Channel.value([]),
                                                                                                        ^^^^^^^
  ```

- Warning: `main.nf:275:50`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
          params.varlociraptor_scenario_germline ? Channel.fromPath(params.varlociraptor_scenario_germline).map { it -> [[id: it.baseName - '.yte'], it] }.collect() : Channel.fromPath("${projectDir}/assets/varlociraptor_germline.yte.yaml").collect(),
                                                   ^^^^^^^
  ```

- Warning: `main.nf:275:166`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
          params.varlociraptor_scenario_germline ? Channel.fromPath(params.varlociraptor_scenario_germline).map { it -> [[id: it.baseName - '.yte'], it] }.collect() : Channel.fromPath("${projectDir}/assets/varlociraptor_germline.yte.yaml").collect(),
                                                                                                                                                                       ^^^^^^^
  ```

- Warning: `main.nf:276:49`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
          params.varlociraptor_scenario_somatic ? Channel.fromPath(params.varlociraptor_scenario_somatic).map { it -> [[id: it.baseName - '.yte'], it] }.collect() : Channel.fromPath("${projectDir}/assets/varlociraptor_somatic.yte.yaml").collect(),
                                                  ^^^^^^^
  ```

- Warning: `main.nf:276:164`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
          params.varlociraptor_scenario_somatic ? Channel.fromPath(params.varlociraptor_scenario_somatic).map { it -> [[id: it.baseName - '.yte'], it] }.collect() : Channel.fromPath("${projectDir}/assets/varlociraptor_somatic.yte.yaml").collect(),
                                                                                                                                                                     ^^^^^^^
  ```

- Warning: `main.nf:277:52`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
          params.varlociraptor_scenario_tumor_only ? Channel.fromPath(params.varlociraptor_scenario_tumor_only).map { it -> [[id: it.baseName - '.yte'], it] }.collect() : Channel.fromPath("${projectDir}/assets/varlociraptor_tumor_only.yte.yaml").collect(),
                                                     ^^^^^^^
  ```

- Warning: `main.nf:277:170`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
          params.varlociraptor_scenario_tumor_only ? Channel.fromPath(params.varlociraptor_scenario_tumor_only).map { it -> [[id: it.baseName - '.yte'], it] }.collect() : Channel.fromPath("${projectDir}/assets/varlociraptor_tumor_only.yte.yaml").collect(),
                                                                                                                                                                           ^^^^^^^
  ```

- Warning: `modules/nf-core/bbmap/bbsplit/main.nf:116:43`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
      other_ref_names.eachWithIndex { name, index ->
                                            ^^^^^
  ```

- Warning: `modules/nf-core/bcftools/concat/main.nf:32:27`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
      def input = vcfs.sort{it.toString()}.join(" ")
                            ^^
  ```

- Warning: `modules/nf-core/bcftools/isec/main.nf:35:9`: Variable was declared but not used

  ```nextflow
      def args = task.ext.args   ?: ''
          ^^^^
  ```

- Warning: `modules/nf-core/bcftools/merge/main.nf:28:58`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
      def input = (vcfs.collect().size() > 1) ? vcfs.sort{ it.name } : vcfs
                                                           ^^
  ```

- Warning: `modules/nf-core/bcftools/norm/main.nf:56:65`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          if (['--write-index=tbi', '-W=tbi'].any { args.contains(it) }  && extension == 'vcf.gz') {
                                                                  ^^
  ```

- Warning: `modules/nf-core/bcftools/norm/main.nf:58:126`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          } else if (['--write-index=tbi', '-W=tbi', '--write-index=csi', '-W=csi', '--write-index', '-W'].any { args.contains(it) }) {
                                                                                                                               ^^
  ```

- Warning: `modules/nf-core/cat/cat/main.nf:23:40`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
      def file_list = files_in.collect { it.toString() }
                                         ^^
  ```

- Warning: `modules/nf-core/cat/cat/main.nf:58:42`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
      def file_list   = files_in.collect { it.toString() }
                                           ^^
  ```

- Warning: `modules/nf-core/cat/fastq/main.nf:22:60`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
      def readList = reads instanceof List ? reads.collect { it.toString() } : [reads.toString()]
                                                             ^^
  ```

- Warning: `modules/nf-core/cat/fastq/main.nf:58:60`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
      def readList = reads instanceof List ? reads.collect { it.toString() } : [reads.toString()]
                                                             ^^
  ```

- Warning: `modules/nf-core/cnvkit/batch/main.nf:40:9`: Variable was declared but not used

  ```nextflow
      def tumor_bam = tumor_exists && tumor.Extension == "bam" ? true : false
          ^^^^^^^^^
  ```

- Warning: `modules/nf-core/cnvkit/batch/main.nf:41:9`: Variable was declared but not used

  ```nextflow
      def normal_bam = normal_exists && normal.Extension == "bam" ? true : false
          ^^^^^^^^^^
  ```

- Warning: `modules/nf-core/fgbio/fastqtobam/main.nf:58:9`: Variable was declared but not used

  ```nextflow
      def args = task.ext.args ?: ''
          ^^^^
  ```

- Warning: `modules/nf-core/gatk4/baserecalibrator/main.nf:29:60`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
      def sites_command = known_sites.collect{"--known-sites $it"}.join(' ')
                                                             ^^
  ```

- Warning: `modules/nf-core/gatk4/estimatelibrarycomplexity/main.nf:26:47`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
      def input_list = input.collect(){"--INPUT $it"}.join(" ")
                                                ^^
  ```

- Warning: `modules/nf-core/gatk4/filtermutectcalls/main.nf:29:113`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
      def orientationbias_command = orientationbias ? orientationbias.collect{"--orientation-bias-artifact-priors $it"}.join(' ') : ''
                                                                                                                  ^^
  ```

- Warning: `modules/nf-core/gatk4/filtermutectcalls/main.nf:30:96`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
      def segmentation_command    = segmentation    ? segmentation.collect{"--tumor-segmentation $it"}.join(' ')                  : ''
                                                                                                 ^^
  ```

- Warning: `modules/nf-core/gatk4/filtermutectcalls/main.nf:32:90`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
      def table_command           = table           ? table.collect{"--contamination-table $it"}.join(' ')                        : ''
                                                                                           ^^
  ```

- Warning: `modules/nf-core/gatk4/filtervarianttranches/main.nf:30:55`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
      def resource_list = resources.collect{"--resource $it"}.join(' ')
                                                        ^^
  ```

- Warning: `modules/nf-core/gatk4/gatherbqsrreports/main.nf:23:45`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
      def input_list = table.collect{"--input $it"}.join(' ')
                                              ^^
  ```

- Warning: `modules/nf-core/gatk4/gatherpileupsummaries/main.nf:25:43`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
      def input_list = pileup.collect{ "--I $it" }.join(' ')
                                            ^^
  ```

- Warning: `modules/nf-core/gatk4/genomicsdbimport/main.nf:30:90`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
      input_command = input_map ? "--sample-name-map ${vcf[0]}" : vcf.collect(){"--variant $it"}.join(' ')
                                                                                           ^^
  ```

- Warning: `modules/nf-core/gatk4/learnreadorientationmodel/main.nf:23:44`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
      def input_list = f1r2.collect{"--input $it"}.join(' ')
                                             ^^
  ```

- Warning: `modules/nf-core/gatk4/markduplicates/main.nf:33:47`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
      def input_list = bam.collect { "--INPUT ${it}" }.join(' ')
                                                ^^
  ```

- Warning: `modules/nf-core/gatk4/mergemutectstats/main.nf:23:48`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
      def input_list = stats.collect{ "--stats ${it}"}.join(' ')
                                                 ^^
  ```

- Warning: `modules/nf-core/gatk4/mergevcfs/main.nf:25:44`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
      def input_list = vcf.collect{ "--INPUT $it"}.join(' ')
                                             ^^
  ```

- Warning: `modules/nf-core/gatk4/mutect2/main.nf:33:42`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
      def inputs = input.collect{ "--input $it"}.join(" ")
                                           ^^
  ```

- Warning: `modules/nf-core/gatk4spark/baserecalibrator/main.nf:29:64`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
      def sites_command = known_sites.collect { "--known-sites ${it}" }.join(' ')
                                                                 ^^
  ```

- Warning: `modules/nf-core/gatk4spark/markduplicates/main.nf:28:47`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
      def input_list = bam.collect { "--input ${it}" }.join(' ')
                                                ^^
  ```

- Warning: `modules/nf-core/gawk/main.nf:26:54`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
      suffix    = task.ext.suffix ?: "${input.collect{ it.getExtension()}.get(0)}" // use the first extension of the input files
                                                       ^^
  ```

- Warning: `modules/nf-core/gawk/main.nf:29:37`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
      lst_gz     = input.findResults{ it.getExtension().endsWith("gz") ? it.toString() : null }
                                      ^^
  ```

- Warning: `modules/nf-core/gawk/main.nf:29:72`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
      lst_gz     = input.findResults{ it.getExtension().endsWith("gz") ? it.toString() : null }
                                                                         ^^
  ```

- Warning: `modules/nf-core/gawk/main.nf:31:34`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
      input_cmd  = input.collect { it.toString() - ~/\.gz$/ }.join(" ")
                                   ^^
  ```

- Warning: `modules/nf-core/gawk/main.nf:34:49`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
      cleanup    = lst_gz ? "rm ${lst_gz.collect{ it - ~/\.gz$/ }.join(" ")}" : ""
                                                  ^^
  ```

- Warning: `modules/nf-core/gawk/main.nf:37:16`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          assert it.name != "${prefix}.${suffix}" : "Input and output names are the same, set prefix in module configuration to disambiguate!"
                 ^^
  ```

- Warning: `modules/nf-core/goleft/indexcov/main.nf:31:36`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
      def input_files = bams.findAll{it.name.endsWith(".bam")} + indexes.findAll{it.name.endsWith(".crai")}
                                     ^^
  ```

- Warning: `modules/nf-core/goleft/indexcov/main.nf:31:80`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
      def input_files = bams.findAll{it.name.endsWith(".bam")} + indexes.findAll{it.name.endsWith(".crai")}
                                                                                 ^^
  ```

- Warning: `modules/nf-core/goleft/indexcov/main.nf:32:42`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
      def extranormalize = input_files.any{it.name.endsWith(".crai")} ? " --extranormalize " : ""
                                           ^^
  ```

- Warning: `modules/nf-core/goleft/indexcov/main.nf:52:9`: Variable was declared but not used

  ```nextflow
      def args = task.ext.args ?: ''
          ^^^^
  ```

- Warning: `modules/nf-core/gunzip/main.nf:43:9`: Variable was declared but not used

  ```nextflow
      def args = task.ext.args ?: ''
          ^^^^
  ```

- Warning: `modules/nf-core/lofreq/callparallel/main.nf:29:9`: Variable was declared but not used

  ```nextflow
      def alignment_bam = bam.Extension == "bam" ? true : false
          ^^^^^^^^^^^^^
  ```

- Warning: `modules/nf-core/manta/germline/main.nf:33:46`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
      def input_files = input.collect{"--bam ${it}"}.join(' ')
                                               ^^
  ```

- Warning: `modules/nf-core/ngscheckmate/ncm/main.nf:28:29`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
      def unzip = files.any { it.toString().endsWith(".vcf.gz") }
                              ^^
  ```

- Warning: `modules/nf-core/ngscheckmate/ncm/main.nf:51:9`: Variable was declared but not used

  ```nextflow
      def args = task.ext.args ?: ''
          ^^^^
  ```

- Warning: `modules/nf-core/parabricks/fq2bam/main.nf:43:119`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
      def known_sites_command    = known_sites   ? (known_sites instanceof List ? known_sites.collect { "--knownSites ${it}" }.join(' ') : "--knownSites ${known_sites}") : ""
                                                                                                                        ^^
  ```

- Warning: `modules/nf-core/parabricks/fq2bam/main.nf:45:126`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
      def interval_file_command  = interval_file ? (interval_file instanceof List ? interval_file.collect { "--interval-file ${it}" }.join(' ') : "--interval-file ${interval_file}") : ""
                                                                                                                               ^^
  ```

- Warning: `modules/nf-core/rbt/vcfsplit/main.nf:22:9`: Variable was declared but not used

  ```nextflow
      def args   = task.ext.args ?: ''
          ^^^^
  ```

- Warning: `modules/nf-core/rbt/vcfsplit/main.nf:39:56`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
      def bcf_files = (0..chunks).collect { "${prefix}.${it}.bcf" }.join(' ')
                                                         ^^
  ```

- Warning: `modules/nf-core/sentieon/dedup/main.nf:36:42`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
      def input_list = bam.collect { "-i ${it}" }.join(' ')
                                           ^^
  ```

- Warning: `modules/nf-core/sentieon/haplotyper/main.nf:37:68`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
      def input_list = input instanceof List ? input.collect { "-i ${it}" }.join(' ') : "-i ${input}"
                                                                     ^^
  ```

- Warning: `modules/nf-core/sentieon/tnscope/main.nf:38:40`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
      def inputs = input.collect { "-i ${it}" }.join(" ")
                                         ^^
  ```

- Warning: `modules/nf-core/svdb/merge/main.nf:38:53`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
              def pairs = vcfs.indices.collect { [vcfs[it], input_priority[it]] }
                                                      ^^
  ```

- Warning: `modules/nf-core/svdb/merge/main.nf:38:73`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
              def pairs = vcfs.indices.collect { [vcfs[it], input_priority[it]] }
                                                                          ^^
  ```

- Warning: `modules/nf-core/svdb/merge/main.nf:40:36`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
              vcfs = pairs.collect { it[0] }
                                     ^^
  ```

- Warning: `modules/nf-core/svdb/merge/main.nf:41:40`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
              priority = pairs.collect { it[1] }
                                         ^^
  ```

- Warning: `modules/nf-core/svdb/merge/main.nf:55:74`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          input = (vcfs.collect().size() > 1 && sort_inputs) ? vcfs.sort { it.name } : vcfs
                                                                           ^^
  ```

- Warning: `modules/nf-core/unzip/main.nf:38:9`: Variable was declared but not used

  ```nextflow
      def args = task.ext.args ?: ''
          ^^^^
  ```

- Warning: `modules/nf-core/varlociraptor/callvariants/main.nf:28:118`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
      def scenario_samples = vcfs instanceof List &&  vcfs.size() > 1 ? [scenario_aliases,vcfs].transpose().collect{"${it[0]}=${it[1]}"}.join(' ') : "${scenario_aliases}=${vcfs}"
                                                                                                                       ^^
  ```

- Warning: `modules/nf-core/varlociraptor/callvariants/main.nf:28:127`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
      def scenario_samples = vcfs instanceof List &&  vcfs.size() > 1 ? [scenario_aliases,vcfs].transpose().collect{"${it[0]}=${it[1]}"}.join(' ') : "${scenario_aliases}=${vcfs}"
                                                                                                                                ^^
  ```

- Warning: `modules/nf-core/vcftools/main.nf:97:26`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
      args_list.removeIf { it.contains('--bed') }
                           ^^
  ```

- Warning: `modules/nf-core/vcftools/main.nf:98:26`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
      args_list.removeIf { it.contains('--exclude-bed') }
                           ^^
  ```

- Warning: `modules/nf-core/vcftools/main.nf:99:26`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
      args_list.removeIf { it.contains('--hapcount') }
                           ^^
  ```

- Warning: `modules/nf-core/vcftools/main.nf:100:26`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
      args_list.removeIf { it.contains('--positions') }
                           ^^
  ```

- Warning: `modules/nf-core/vcftools/main.nf:101:26`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
      args_list.removeIf { it.contains('--exclude-positions') }
                           ^^
  ```

- Warning: `modules/nf-core/vcftools/main.nf:106:26`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
      args_list.removeIf { it.contains('--diff') }
                           ^^
  ```

- Warning: `modules/nf-core/vcftools/main.nf:107:26`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
      args_list.removeIf { it.contains('--gzdiff') }
                           ^^
  ```

- Warning: `modules/nf-core/vcftools/main.nf:108:26`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
      args_list.removeIf { it.contains('--diff-bcf') }
                           ^^
  ```

- Warning: `modules/nf-core/yte/main.nf:23:9`: Variable was declared but not used

  ```nextflow
      def args = task.ext.args ?: ''
          ^^^^
  ```

- Warning: `modules/nf-core/yte/main.nf:39:9`: Variable was declared but not used

  ```nextflow
      def args = task.ext.args ?: ''
          ^^^^
  ```

- Warning: `subworkflows/local/annotation_cache_initialisation/main.nf:37:24`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
          snpeff_cache = Channel.fromPath(file("${snpeff_cache}/${snpeff_annotation_cache_key}"), checkIfExists: true)
                         ^^^^^^^
  ```

- Warning: `subworkflows/local/annotation_cache_initialisation/main.nf:58:28`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
          ensemblvep_cache = Channel.fromPath(file("${vep_cache}/${vep_annotation_cache_key}"), checkIfExists: true).collect()
                             ^^^^^^^
  ```

- Warning: `subworkflows/local/bam_applybqsr/main.nf:20:16`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      versions = Channel.empty()
                 ^^^^^^^
  ```

- Warning: `subworkflows/local/bam_applybqsr/main.nf:21:28`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      bam_applybqsr_single = Channel.empty()
                             ^^^^^^^
  ```

- Warning: `subworkflows/local/bam_applybqsr/main.nf:22:20`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      bam_to_merge = Channel.empty()
                     ^^^^^^^
  ```

- Warning: `subworkflows/local/bam_applybqsr/main.nf:44:25`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
                  single: it[0].num_intervals == 1
                          ^^
  ```

- Warning: `subworkflows/local/bam_applybqsr/main.nf:45:27`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
                  multiple: it[0].num_intervals > 1
                            ^^
  ```

- Warning: `subworkflows/local/bam_applybqsr_spark/main.nf:20:16`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      versions = Channel.empty()
                 ^^^^^^^
  ```

- Warning: `subworkflows/local/bam_applybqsr_spark/main.nf:21:28`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      bam_applybqsr_single = Channel.empty()
                             ^^^^^^^
  ```

- Warning: `subworkflows/local/bam_applybqsr_spark/main.nf:22:20`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      bam_to_merge = Channel.empty()
                     ^^^^^^^
  ```

- Warning: `subworkflows/local/bam_applybqsr_spark/main.nf:44:25`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
                  single: it[0].num_intervals == 1
                          ^^
  ```

- Warning: `subworkflows/local/bam_applybqsr_spark/main.nf:45:27`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
                  multiple: it[0].num_intervals > 1
                            ^^
  ```

- Warning: `subworkflows/local/bam_baserecalibrator/main.nf:21:16`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      versions = Channel.empty()
                 ^^^^^^^
  ```

- Warning: `subworkflows/local/bam_baserecalibrator/main.nf:41:19`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          single:   it[0].num_intervals <= 1
                    ^^
  ```

- Warning: `subworkflows/local/bam_baserecalibrator/main.nf:42:19`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          multiple: it[0].num_intervals > 1
                    ^^
  ```

- Warning: `subworkflows/local/bam_baserecalibrator_spark/main.nf:21:16`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      versions = Channel.empty()
                 ^^^^^^^
  ```

- Warning: `subworkflows/local/bam_baserecalibrator_spark/main.nf:29:60`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
      GATK4SPARK_BASERECALIBRATOR(cram_intervals, fasta.map{ meta, it -> [ it ] }, fasta_fai.map{ meta, it -> [ it ] }, dict.map{ meta, it -> [ it ] }, known_sites, known_sites_tbi)
                                                             ^^^^
  ```

- Warning: `subworkflows/local/bam_baserecalibrator_spark/main.nf:29:97`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
      GATK4SPARK_BASERECALIBRATOR(cram_intervals, fasta.map{ meta, it -> [ it ] }, fasta_fai.map{ meta, it -> [ it ] }, dict.map{ meta, it -> [ it ] }, known_sites, known_sites_tbi)
                                                                                                  ^^^^
  ```

- Warning: `subworkflows/local/bam_baserecalibrator_spark/main.nf:29:129`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
      GATK4SPARK_BASERECALIBRATOR(cram_intervals, fasta.map{ meta, it -> [ it ] }, fasta_fai.map{ meta, it -> [ it ] }, dict.map{ meta, it -> [ it ] }, known_sites, known_sites_tbi)
                                                                                                                                  ^^^^
  ```

- Warning: `subworkflows/local/bam_baserecalibrator_spark/main.nf:34:19`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          single:   it[0].num_intervals <= 1
                    ^^
  ```

- Warning: `subworkflows/local/bam_baserecalibrator_spark/main.nf:35:19`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          multiple: it[0].num_intervals > 1
                    ^^
  ```

- Warning: `subworkflows/local/bam_convert_samtools/main.nf:22:16`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      versions = Channel.empty()
                 ^^^^^^^
  ```

- Warning: `subworkflows/local/bam_joint_calling_germline_gatk/main.nf:34:16`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      versions = Channel.empty()
                 ^^^^^^^
  ```

- Warning: `subworkflows/local/bam_joint_calling_germline_gatk/main.nf:74:20`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          fasta.map{ meta, fasta -> [ fasta ] },
                     ^^^^
  ```

- Warning: `subworkflows/local/bam_joint_calling_germline_gatk/main.nf:75:18`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          fai.map{ meta, fai -> [ fai ] },
                   ^^^^
  ```

- Warning: `subworkflows/local/bam_joint_calling_germline_gatk/main.nf:76:19`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          dict.map{ meta, dict -> [ dict ] })
                    ^^^^
  ```

- Warning: `subworkflows/local/bam_joint_calling_germline_gatk/main.nf:83:20`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          fasta.map{ meta, fasta -> [ fasta ] },
                     ^^^^
  ```

- Warning: `subworkflows/local/bam_joint_calling_germline_gatk/main.nf:84:18`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          fai.map{ meta, fai -> [ fai ] },
                   ^^^^
  ```

- Warning: `subworkflows/local/bam_joint_calling_germline_gatk/main.nf:85:19`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          dict.map{ meta, dict -> [ dict ] })
                    ^^^^
  ```

- Warning: `subworkflows/local/bam_joint_calling_germline_gatk/main.nf:100:20`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          fasta.map{ meta, fasta -> [ fasta ] },
                     ^^^^
  ```

- Warning: `subworkflows/local/bam_joint_calling_germline_gatk/main.nf:101:18`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          fai.map{ meta, fai -> [ fai ] },
                   ^^^^
  ```

- Warning: `subworkflows/local/bam_joint_calling_germline_gatk/main.nf:102:19`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          dict.map{ meta, dict -> [ dict ] })
                    ^^^^
  ```

- Warning: `subworkflows/local/bam_joint_calling_germline_gatk/main.nf:114:20`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          fasta.map{ meta, fasta -> [ fasta ] },
                     ^^^^
  ```

- Warning: `subworkflows/local/bam_joint_calling_germline_gatk/main.nf:115:18`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          fai.map{ meta, fai -> [ fai ] },
                   ^^^^
  ```

- Warning: `subworkflows/local/bam_joint_calling_germline_gatk/main.nf:116:19`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          dict.map{ meta, dict -> [ dict ] })
                    ^^^^
  ```

- Warning: `subworkflows/local/bam_joint_calling_germline_gatk/main.nf:123:58`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
      merge_vcf_for_join = MERGE_GENOTYPEGVCFS.out.vcf.map{meta, vcf -> [[id: 'joint_variant_calling'] , vcf]}
                                                           ^^^^
  ```

- Warning: `subworkflows/local/bam_joint_calling_germline_gatk/main.nf:124:58`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
      merge_tbi_for_join = MERGE_GENOTYPEGVCFS.out.tbi.map{meta, tbi -> [[id: 'joint_variant_calling'] , tbi]}
                                                           ^^^^
  ```

- Warning: `subworkflows/local/bam_joint_calling_germline_gatk/main.nf:127:78`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
      vqsr_vcf_for_join = GATK4_APPLYVQSR_INDEL.out.vcf.ifEmpty([[:], []]).map{meta, vcf -> [[id: 'joint_variant_calling'] , vcf]}
                                                                               ^^^^
  ```

- Warning: `subworkflows/local/bam_joint_calling_germline_gatk/main.nf:128:78`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
      vqsr_tbi_for_join = GATK4_APPLYVQSR_INDEL.out.tbi.ifEmpty([[:], []]).map{meta, tbi -> [[id: 'joint_variant_calling'] , tbi]}
                                                                               ^^^^
  ```

- Warning: `subworkflows/local/bam_joint_calling_germline_gatk/main.nf:135:9`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          meta, joint_vcf, recal_vcf ->
          ^^^^
  ```

- Warning: `subworkflows/local/bam_joint_calling_germline_gatk/main.nf:143:9`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          meta, joint_tbi, recal_tbi ->
          ^^^^
  ```

- Warning: `subworkflows/local/bam_joint_calling_germline_sentieon/main.nf:33:16`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      versions = Channel.empty()
                 ^^^^^^^
  ```

- Warning: `subworkflows/local/bam_joint_calling_germline_sentieon/main.nf:54:50`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
      merged_vcf = MERGE_GENOTYPEGVCFS.out.vcf.map{meta, vcf -> [[id: 'joint_variant_calling'] , vcf]}
                                                   ^^^^
  ```

- Warning: `subworkflows/local/bam_joint_calling_germline_sentieon/main.nf:55:50`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
      merged_tbi = MERGE_GENOTYPEGVCFS.out.tbi.map{meta, tbi -> [[id: 'joint_variant_calling'] , tbi]}
                                                   ^^^^
  ```

- Warning: `subworkflows/local/bam_joint_calling_germline_sentieon/main.nf:76:23`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
              fasta.map{meta, it -> [ it ]},
                        ^^^^
  ```

- Warning: `subworkflows/local/bam_joint_calling_germline_sentieon/main.nf:77:21`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
              fai.map{meta, it -> [ it ]})
                      ^^^^
  ```

- Warning: `subworkflows/local/bam_joint_calling_germline_sentieon/main.nf:84:23`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
              fasta.map{meta, it -> [ it ]},
                        ^^^^
  ```

- Warning: `subworkflows/local/bam_joint_calling_germline_sentieon/main.nf:85:21`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
              fai.map{meta, it -> [ it ]})
                      ^^^^
  ```

- Warning: `subworkflows/local/bam_joint_calling_germline_sentieon/main.nf:115:87`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          vqsr_vcf_for_join = SENTIEON_APPLYVARCAL_INDEL.out.vcf.ifEmpty([[:], []]).map{meta, vcf -> [[id: 'joint_variant_calling'] , vcf]}
                                                                                        ^^^^
  ```

- Warning: `subworkflows/local/bam_joint_calling_germline_sentieon/main.nf:116:87`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          vqsr_tbi_for_join = SENTIEON_APPLYVARCAL_INDEL.out.tbi.ifEmpty([[:], []]).map{meta, tbi -> [[id: 'joint_variant_calling'] , tbi]}
                                                                                        ^^^^
  ```

- Warning: `subworkflows/local/bam_joint_calling_germline_sentieon/main.nf:123:13`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
              meta, joint_vcf, recal_vcf ->
              ^^^^
  ```

- Warning: `subworkflows/local/bam_joint_calling_germline_sentieon/main.nf:131:13`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
              meta, joint_tbi, recal_tbi ->
              ^^^^
  ```

- Warning: `subworkflows/local/bam_markduplicates/main.nf:18:16`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      versions = Channel.empty()
                 ^^^^^^^
  ```

- Warning: `subworkflows/local/bam_markduplicates/main.nf:19:16`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      reports  = Channel.empty()
                 ^^^^^^^
  ```

- Warning: `subworkflows/local/bam_markduplicates/main.nf:22:42`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
      GATK4_MARKDUPLICATES(bam, fasta.map{ meta, fasta -> [ fasta ] }, fasta_fai.map{ meta, fasta_fai -> [ fasta_fai ] })
                                           ^^^^
  ```

- Warning: `subworkflows/local/bam_markduplicates/main.nf:22:85`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
      GATK4_MARKDUPLICATES(bam, fasta.map{ meta, fasta -> [ fasta ] }, fasta_fai.map{ meta, fasta_fai -> [ fasta_fai ] })
                                                                                      ^^^^
  ```

- Warning: `subworkflows/local/bam_markduplicates_spark/main.nf:21:16`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      versions = Channel.empty()
                 ^^^^^^^
  ```

- Warning: `subworkflows/local/bam_markduplicates_spark/main.nf:22:15`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      reports = Channel.empty()
                ^^^^^^^
  ```

- Warning: `subworkflows/local/bam_markduplicates_spark/main.nf:25:47`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
      GATK4SPARK_MARKDUPLICATES(bam, fasta.map{ meta, fasta -> [ fasta ] }, fasta_fai.map{ meta, fasta_fai -> [ fasta_fai ] }, dict.map{ meta, dict -> [ dict ] })
                                                ^^^^
  ```

- Warning: `subworkflows/local/bam_markduplicates_spark/main.nf:25:90`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
      GATK4SPARK_MARKDUPLICATES(bam, fasta.map{ meta, fasta -> [ fasta ] }, fasta_fai.map{ meta, fasta_fai -> [ fasta_fai ] }, dict.map{ meta, dict -> [ dict ] })
                                                                                           ^^^^
  ```

- Warning: `subworkflows/local/bam_markduplicates_spark/main.nf:25:136`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
      GATK4SPARK_MARKDUPLICATES(bam, fasta.map{ meta, fasta -> [ fasta ] }, fasta_fai.map{ meta, fasta_fai -> [ fasta_fai ] }, dict.map{ meta, dict -> [ dict ] })
                                                                                                                                         ^^^^
  ```

- Warning: `subworkflows/local/bam_markduplicates_spark/main.nf:37:53`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
      GATK4_ESTIMATELIBRARYCOMPLEXITY(bam, fasta.map{ meta, fasta -> [ fasta ] }, fasta_fai.map{ meta, fasta_fai -> [ fasta_fai ] }, dict.map{ meta, dict -> [ dict ] })
                                                      ^^^^
  ```

- Warning: `subworkflows/local/bam_markduplicates_spark/main.nf:37:96`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
      GATK4_ESTIMATELIBRARYCOMPLEXITY(bam, fasta.map{ meta, fasta -> [ fasta ] }, fasta_fai.map{ meta, fasta_fai -> [ fasta_fai ] }, dict.map{ meta, dict -> [ dict ] })
                                                                                                 ^^^^
  ```

- Warning: `subworkflows/local/bam_markduplicates_spark/main.nf:37:142`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
      GATK4_ESTIMATELIBRARYCOMPLEXITY(bam, fasta.map{ meta, fasta -> [ fasta ] }, fasta_fai.map{ meta, fasta_fai -> [ fasta_fai ] }, dict.map{ meta, dict -> [ dict ] })
                                                                                                                                               ^^^^
  ```

- Warning: `subworkflows/local/bam_merge_index_samtools/main.nf:15:16`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      versions = Channel.empty()
                 ^^^^^^^
  ```

- Warning: `subworkflows/local/bam_sentieon_dedup/main.nf:16:16`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      versions = Channel.empty()
                 ^^^^^^^
  ```

- Warning: `subworkflows/local/bam_sentieon_dedup/main.nf:17:16`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      reports  = Channel.empty()
                 ^^^^^^^
  ```

- Warning: `subworkflows/local/bam_variant_calling_cnvkit/main.nf:21:16`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      versions = Channel.empty()
                 ^^^^^^^
  ```

- Warning: `subworkflows/local/bam_variant_calling_deepvariant/main.nf:21:16`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      versions = Channel.empty()
                 ^^^^^^^
  ```

- Warning: `subworkflows/local/bam_variant_calling_deepvariant/main.nf:33:23`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          intervals:    it[0].num_intervals > 1
                        ^^
  ```

- Warning: `subworkflows/local/bam_variant_calling_deepvariant/main.nf:34:23`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          no_intervals: it[0].num_intervals <= 1
                        ^^
  ```

- Warning: `subworkflows/local/bam_variant_calling_deepvariant/main.nf:40:23`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          intervals:    it[0].num_intervals > 1
                        ^^
  ```

- Warning: `subworkflows/local/bam_variant_calling_deepvariant/main.nf:41:23`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          no_intervals: it[0].num_intervals <= 1
                        ^^
  ```

- Warning: `subworkflows/local/bam_variant_calling_deepvariant/main.nf:54:23`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          intervals:    it[0].num_intervals > 1
                        ^^
  ```

- Warning: `subworkflows/local/bam_variant_calling_deepvariant/main.nf:55:23`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          no_intervals: it[0].num_intervals <= 1
                        ^^
  ```

- Warning: `subworkflows/local/bam_variant_calling_deepvariant/main.nf:59:12`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      gvcf = Channel.empty().mix(MERGE_DEEPVARIANT_GVCF.out.vcf, gvcf_out.no_intervals)
             ^^^^^^^
  ```

- Warning: `subworkflows/local/bam_variant_calling_deepvariant/main.nf:64:11`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      vcf = Channel.empty().mix(MERGE_DEEPVARIANT_VCF.out.vcf, vcf_out.no_intervals)
            ^^^^^^^
  ```

- Warning: `subworkflows/local/bam_variant_calling_deepvariant/main.nf:68:11`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      tbi = Channel.empty().mix(MERGE_DEEPVARIANT_VCF.out.tbi, tbi_out.no_intervals)
            ^^^^^^^
  ```

- Warning: `subworkflows/local/bam_variant_calling_freebayes/main.nf:23:16`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      versions = Channel.empty()
                 ^^^^^^^
  ```

- Warning: `subworkflows/local/bam_variant_calling_freebayes/main.nf:37:23`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          intervals:    it[0].num_intervals > 1
                        ^^
  ```

- Warning: `subworkflows/local/bam_variant_calling_freebayes/main.nf:38:23`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          no_intervals: it[0].num_intervals <= 1
                        ^^
  ```

- Warning: `subworkflows/local/bam_variant_calling_germline_all/main.nf:26:5`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
      bam                               // channel: [mandatory] meta, bam
      ^^^
  ```

- Warning: `subworkflows/local/bam_variant_calling_germline_all/main.nf:55:16`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      versions = Channel.empty()
                 ^^^^^^^
  ```

- Warning: `subworkflows/local/bam_variant_calling_germline_all/main.nf:58:32`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      gvcf_sentieon_dnascope   = Channel.empty()
                                 ^^^^^^^
  ```

- Warning: `subworkflows/local/bam_variant_calling_germline_all/main.nf:59:32`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      gvcf_sentieon_haplotyper = Channel.empty()
                                 ^^^^^^^
  ```

- Warning: `subworkflows/local/bam_variant_calling_germline_all/main.nf:61:32`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      out_indexcov             = Channel.empty()
                                 ^^^^^^^
  ```

- Warning: `subworkflows/local/bam_variant_calling_germline_all/main.nf:62:32`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      vcf_deepvariant          = Channel.empty()
                                 ^^^^^^^
  ```

- Warning: `subworkflows/local/bam_variant_calling_germline_all/main.nf:63:32`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      vcf_freebayes            = Channel.empty()
                                 ^^^^^^^
  ```

- Warning: `subworkflows/local/bam_variant_calling_germline_all/main.nf:64:32`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      vcf_haplotypecaller      = Channel.empty()
                                 ^^^^^^^
  ```

- Warning: `subworkflows/local/bam_variant_calling_germline_all/main.nf:65:32`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      vcf_manta                = Channel.empty()
                                 ^^^^^^^
  ```

- Warning: `subworkflows/local/bam_variant_calling_germline_all/main.nf:66:32`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      vcf_mpileup              = Channel.empty()
                                 ^^^^^^^
  ```

- Warning: `subworkflows/local/bam_variant_calling_germline_all/main.nf:67:32`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      vcf_sentieon_dnascope    = Channel.empty()
                                 ^^^^^^^
  ```

- Warning: `subworkflows/local/bam_variant_calling_germline_all/main.nf:68:32`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      vcf_sentieon_haplotyper  = Channel.empty()
                                 ^^^^^^^
  ```

- Warning: `subworkflows/local/bam_variant_calling_germline_all/main.nf:69:32`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      vcf_strelka              = Channel.empty()
                                 ^^^^^^^
  ```

- Warning: `subworkflows/local/bam_variant_calling_germline_all/main.nf:70:32`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      vcf_tiddit               = Channel.empty()
                                 ^^^^^^^
  ```

- Warning: `subworkflows/local/bam_variant_calling_germline_all/main.nf:71:32`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      tbi_deepvariant          = Channel.empty()
                                 ^^^^^^^
  ```

- Warning: `subworkflows/local/bam_variant_calling_germline_all/main.nf:72:32`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      tbi_freebayes            = Channel.empty()
                                 ^^^^^^^
  ```

- Warning: `subworkflows/local/bam_variant_calling_germline_all/main.nf:73:32`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      tbi_haplotypecaller      = Channel.empty()
                                 ^^^^^^^
  ```

- Warning: `subworkflows/local/bam_variant_calling_germline_all/main.nf:74:32`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      tbi_manta                = Channel.empty()
                                 ^^^^^^^
  ```

- Warning: `subworkflows/local/bam_variant_calling_germline_all/main.nf:75:32`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      tbi_mpileup              = Channel.empty()
                                 ^^^^^^^
  ```

- Warning: `subworkflows/local/bam_variant_calling_germline_all/main.nf:76:32`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      tbi_sentieon_dnascope    = Channel.empty()
                                 ^^^^^^^
  ```

- Warning: `subworkflows/local/bam_variant_calling_germline_all/main.nf:77:32`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      tbi_sentieon_haplotyper  = Channel.empty()
                                 ^^^^^^^
  ```

- Warning: `subworkflows/local/bam_variant_calling_germline_all/main.nf:78:32`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      tbi_strelka              = Channel.empty()
                                 ^^^^^^^
  ```

- Warning: `subworkflows/local/bam_variant_calling_germline_all/main.nf:79:32`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      tbi_tiddit               = Channel.empty()
                                 ^^^^^^^
  ```

- Warning: `subworkflows/local/bam_variant_calling_germline_all/main.nf:98:35`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
              cram.map{ meta, cram, crai -> [ meta, [], cram ] },
                                    ^^^^
  ```

- Warning: `subworkflows/local/bam_variant_calling_germline_all/main.nf:181:32`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
                      fasta.map{ meta, fasta -> [ fasta ] },
                                 ^^^^
  ```

- Warning: `subworkflows/local/bam_variant_calling_germline_all/main.nf:182:36`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
                      fasta_fai.map{ meta, fasta_fai -> [ fasta_fai ] },
                                     ^^^^
  ```

- Warning: `subworkflows/local/bam_variant_calling_germline_all/main.nf:183:31`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
                      dict.map{ meta, dict -> [ dict ] },
                                ^^^^
  ```

- Warning: `subworkflows/local/bam_variant_calling_germline_all/main.nf:243:9`: Variable was declared but not used

  ```nextflow
          gvcf_tbi_sentieon_dnascope = BAM_VARIANT_CALLING_SENTIEON_DNASCOPE.out.gvcf_tbi
          ^^^^^^^^^^^^^^^^^^^^^^^^^^
  ```

- Warning: `subworkflows/local/bam_variant_calling_germline_all/main.nf:303:9`: Variable was declared but not used

  ```nextflow
          gvcf_tbi_sentieon_haplotyper = BAM_VARIANT_CALLING_SENTIEON_HAPLOTYPER.out.gvcf_tbi
          ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  ```

- Warning: `subworkflows/local/bam_variant_calling_germline_all/main.nf:332:32`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
                      fasta.map{ meta, it -> [ it ] },
                                 ^^^^
  ```

- Warning: `subworkflows/local/bam_variant_calling_germline_all/main.nf:333:36`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
                      fasta_fai.map{ meta, it -> [ it ] },
                                     ^^^^
  ```

- Warning: `subworkflows/local/bam_variant_calling_germline_all/main.nf:334:31`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
                      dict.map{ meta, dict -> [ dict ] },
                                ^^^^
  ```

- Warning: `subworkflows/local/bam_variant_calling_germline_all/main.nf:354:24`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
              fasta.map{ meta, fasta -> [ fasta ] },
                         ^^^^
  ```

- Warning: `subworkflows/local/bam_variant_calling_germline_all/main.nf:355:28`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
              fasta_fai.map{ meta, fasta_fai -> [ fasta_fai ] },
                             ^^^^
  ```

- Warning: `subworkflows/local/bam_variant_calling_germline_all/main.nf:378:15`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      vcf_all = Channel.empty().mix(
                ^^^^^^^
  ```

- Warning: `subworkflows/local/bam_variant_calling_germline_all/main.nf:390:15`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      tbi_all = Channel.empty().mix(
                ^^^^^^^
  ```

- Warning: `subworkflows/local/bam_variant_calling_germline_manta/main.nf:18:16`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      versions = Channel.empty()
                 ^^^^^^^
  ```

- Warning: `subworkflows/local/bam_variant_calling_germline_manta/main.nf:30:5`: Variable was declared but not used

  ```nextflow
      small_indels_vcf     = MANTA_GERMLINE.out.candidate_small_indels_vcf
      ^^^^^^^^^^^^^^^^
  ```

- Warning: `subworkflows/local/bam_variant_calling_germline_manta/main.nf:31:5`: Variable was declared but not used

  ```nextflow
      sv_vcf               = MANTA_GERMLINE.out.candidate_sv_vcf
      ^^^^^^
  ```

- Warning: `subworkflows/local/bam_variant_calling_haplotypecaller/main.nf:22:16`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      versions = Channel.empty()
                 ^^^^^^^
  ```

- Warning: `subworkflows/local/bam_variant_calling_haplotypecaller/main.nf:24:21`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      vcf           = Channel.empty()
                      ^^^^^^^
  ```

- Warning: `subworkflows/local/bam_variant_calling_haplotypecaller/main.nf:25:21`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      realigned_bam = Channel.empty()
                      ^^^^^^^
  ```

- Warning: `subworkflows/local/bam_variant_calling_haplotypecaller/main.nf:45:32`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          .map{ meta, gvcf, tbi, cram, crai, intervals, dragstr_model -> [ meta, gvcf, tbi, intervals ] }
                                 ^^^^
  ```

- Warning: `subworkflows/local/bam_variant_calling_haplotypecaller/main.nf:45:38`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          .map{ meta, gvcf, tbi, cram, crai, intervals, dragstr_model -> [ meta, gvcf, tbi, intervals ] }
                                       ^^^^
  ```

- Warning: `subworkflows/local/bam_variant_calling_haplotypecaller/main.nf:45:55`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          .map{ meta, gvcf, tbi, cram, crai, intervals, dragstr_model -> [ meta, gvcf, tbi, intervals ] }
                                                        ^^^^^^^^^^^^^
  ```

- Warning: `subworkflows/local/bam_variant_calling_haplotypecaller/main.nf:53:27`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
              intervals:    it[0].num_intervals > 1
                            ^^
  ```

- Warning: `subworkflows/local/bam_variant_calling_haplotypecaller/main.nf:54:27`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
              no_intervals: it[0].num_intervals <= 1
                            ^^
  ```

- Warning: `subworkflows/local/bam_variant_calling_haplotypecaller/main.nf:62:27`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
              intervals:    it[0].num_intervals > 1
                            ^^
  ```

- Warning: `subworkflows/local/bam_variant_calling_haplotypecaller/main.nf:63:27`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
              no_intervals: it[0].num_intervals <= 1
                            ^^
  ```

- Warning: `subworkflows/local/bam_variant_calling_haplotypecaller/main.nf:71:27`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
              intervals:    it[0].num_intervals > 1
                            ^^
  ```

- Warning: `subworkflows/local/bam_variant_calling_haplotypecaller/main.nf:72:27`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
              no_intervals: it[0].num_intervals <= 1
                            ^^
  ```

- Warning: `subworkflows/local/bam_variant_calling_haplotypecaller/main.nf:78:27`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      haplotypecaller_vcf = Channel.empty().mix(
                            ^^^^^^^
  ```

- Warning: `subworkflows/local/bam_variant_calling_haplotypecaller/main.nf:82:27`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      haplotypecaller_tbi = Channel.empty().mix(
                            ^^^^^^^
  ```

- Warning: `subworkflows/local/bam_variant_calling_indexcov/main.nf:18:16`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      versions = Channel.empty()
                 ^^^^^^^
  ```

- Warning: `subworkflows/local/bam_variant_calling_indexcov/main.nf:30:65`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
      indexcov_input_ch = reindex_ch.output.map{[[id:"indexcov"], it[1], it[2]]}.groupTuple()
                                                                  ^^
  ```

- Warning: `subworkflows/local/bam_variant_calling_indexcov/main.nf:30:72`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
      indexcov_input_ch = reindex_ch.output.map{[[id:"indexcov"], it[1], it[2]]}.groupTuple()
                                                                         ^^
  ```

- Warning: `subworkflows/local/bam_variant_calling_mpileup/main.nf:20:16`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      versions = Channel.empty()
                 ^^^^^^^
  ```

- Warning: `subworkflows/local/bam_variant_calling_mpileup/main.nf:36:20`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          intervals: it[0].num_intervals > 1
                     ^^
  ```

- Warning: `subworkflows/local/bam_variant_calling_mpileup/main.nf:37:23`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          no_intervals: it[0].num_intervals <= 1
                        ^^
  ```

- Warning: `subworkflows/local/bam_variant_calling_mpileup/main.nf:42:20`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          intervals: it[0].num_intervals > 1
                     ^^
  ```

- Warning: `subworkflows/local/bam_variant_calling_mpileup/main.nf:43:23`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          no_intervals: it[0].num_intervals <= 1
                        ^^
  ```

- Warning: `subworkflows/local/bam_variant_calling_mpileup/main.nf:48:20`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          intervals: it[0].num_intervals > 1
                     ^^
  ```

- Warning: `subworkflows/local/bam_variant_calling_mpileup/main.nf:49:23`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          no_intervals: it[0].num_intervals <= 1
                        ^^
  ```

- Warning: `subworkflows/local/bam_variant_calling_sentieon_dnascope/main.nf:19:5`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
      dbsnp_vqsr                        // channel: [optional]
      ^^^^^^^^^^
  ```

- Warning: `subworkflows/local/bam_variant_calling_sentieon_dnascope/main.nf:27:16`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      versions = Channel.empty()
                 ^^^^^^^
  ```

- Warning: `subworkflows/local/bam_variant_calling_sentieon_dnascope/main.nf:29:26`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      gvcf               = Channel.empty()
                           ^^^^^^^
  ```

- Warning: `subworkflows/local/bam_variant_calling_sentieon_dnascope/main.nf:30:26`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      vcf                = Channel.empty()
                           ^^^^^^^
  ```

- Warning: `subworkflows/local/bam_variant_calling_sentieon_dnascope/main.nf:31:26`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      genotype_intervals = Channel.empty()
                           ^^^^^^^
  ```

- Warning: `subworkflows/local/bam_variant_calling_sentieon_dnascope/main.nf:60:30`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          emit_mode_items.any{ it.equals('gvcf') })
                               ^^
  ```

- Warning: `subworkflows/local/bam_variant_calling_sentieon_dnascope/main.nf:66:36`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
              .map{ meta, gvcf, tbi, cram, crai, intervals -> [ meta, gvcf, tbi, intervals ] }
                                     ^^^^
  ```

- Warning: `subworkflows/local/bam_variant_calling_sentieon_dnascope/main.nf:66:42`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
              .map{ meta, gvcf, tbi, cram, crai, intervals -> [ meta, gvcf, tbi, intervals ] }
                                           ^^^^
  ```

- Warning: `subworkflows/local/bam_variant_calling_sentieon_dnascope/main.nf:74:27`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
              intervals:    it[0].num_intervals > 1
                            ^^
  ```

- Warning: `subworkflows/local/bam_variant_calling_sentieon_dnascope/main.nf:75:27`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
              no_intervals: it[0].num_intervals <= 1
                            ^^
  ```

- Warning: `subworkflows/local/bam_variant_calling_sentieon_dnascope/main.nf:82:27`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
              intervals:    it[0].num_intervals > 1
                            ^^
  ```

- Warning: `subworkflows/local/bam_variant_calling_sentieon_dnascope/main.nf:83:27`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
              no_intervals: it[0].num_intervals <= 1
                            ^^
  ```

- Warning: `subworkflows/local/bam_variant_calling_sentieon_dnascope/main.nf:90:27`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
              intervals:    it[0].num_intervals > 1
                            ^^
  ```

- Warning: `subworkflows/local/bam_variant_calling_sentieon_dnascope/main.nf:91:27`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
              no_intervals: it[0].num_intervals <= 1
                            ^^
  ```

- Warning: `subworkflows/local/bam_variant_calling_sentieon_dnascope/main.nf:98:27`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
              intervals:    it[0].num_intervals > 1
                            ^^
  ```

- Warning: `subworkflows/local/bam_variant_calling_sentieon_dnascope/main.nf:99:27`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
              no_intervals: it[0].num_intervals <= 1
                            ^^
  ```

- Warning: `subworkflows/local/bam_variant_calling_sentieon_dnascope/main.nf:114:20`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      dnascope_vcf = Channel.empty().mix(
                     ^^^^^^^
  ```

- Warning: `subworkflows/local/bam_variant_calling_sentieon_dnascope/main.nf:118:22`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      haplotyper_tbi = Channel.empty().mix(
                       ^^^^^^^
  ```

- Warning: `subworkflows/local/bam_variant_calling_sentieon_dnascope/main.nf:137:12`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      gvcf = Channel.empty().mix(
             ^^^^^^^
  ```

- Warning: `subworkflows/local/bam_variant_calling_sentieon_dnascope/main.nf:141:16`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      gvcf_tbi = Channel.empty().mix(
                 ^^^^^^^
  ```

- Warning: `subworkflows/local/bam_variant_calling_sentieon_haplotyper/main.nf:19:5`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
      dbsnp_vqsr                     // channel: [optional]
      ^^^^^^^^^^
  ```

- Warning: `subworkflows/local/bam_variant_calling_sentieon_haplotyper/main.nf:25:16`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      versions = Channel.empty()
                 ^^^^^^^
  ```

- Warning: `subworkflows/local/bam_variant_calling_sentieon_haplotyper/main.nf:27:26`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      gvcf               = Channel.empty()
                           ^^^^^^^
  ```

- Warning: `subworkflows/local/bam_variant_calling_sentieon_haplotyper/main.nf:28:26`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      vcf                = Channel.empty()
                           ^^^^^^^
  ```

- Warning: `subworkflows/local/bam_variant_calling_sentieon_haplotyper/main.nf:29:26`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      genotype_intervals = Channel.empty()
                           ^^^^^^^
  ```

- Warning: `subworkflows/local/bam_variant_calling_sentieon_haplotyper/main.nf:56:30`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          emit_mode_items.any{ it.equals('gvcf') })
                               ^^
  ```

- Warning: `subworkflows/local/bam_variant_calling_sentieon_haplotyper/main.nf:62:36`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
              .map{ meta, gvcf, tbi, cram, crai, intervals -> [ meta, gvcf, tbi, intervals ] }
                                     ^^^^
  ```

- Warning: `subworkflows/local/bam_variant_calling_sentieon_haplotyper/main.nf:62:42`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
              .map{ meta, gvcf, tbi, cram, crai, intervals -> [ meta, gvcf, tbi, intervals ] }
                                           ^^^^
  ```

- Warning: `subworkflows/local/bam_variant_calling_sentieon_haplotyper/main.nf:70:27`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
              intervals:    it[0].num_intervals > 1
                            ^^
  ```

- Warning: `subworkflows/local/bam_variant_calling_sentieon_haplotyper/main.nf:71:27`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
              no_intervals: it[0].num_intervals <= 1
                            ^^
  ```

- Warning: `subworkflows/local/bam_variant_calling_sentieon_haplotyper/main.nf:78:27`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
              intervals:    it[0].num_intervals > 1
                            ^^
  ```

- Warning: `subworkflows/local/bam_variant_calling_sentieon_haplotyper/main.nf:79:27`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
              no_intervals: it[0].num_intervals <= 1
                            ^^
  ```

- Warning: `subworkflows/local/bam_variant_calling_sentieon_haplotyper/main.nf:86:27`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
              intervals:    it[0].num_intervals > 1
                            ^^
  ```

- Warning: `subworkflows/local/bam_variant_calling_sentieon_haplotyper/main.nf:87:27`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
              no_intervals: it[0].num_intervals <= 1
                            ^^
  ```

- Warning: `subworkflows/local/bam_variant_calling_sentieon_haplotyper/main.nf:94:27`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
              intervals:    it[0].num_intervals > 1
                            ^^
  ```

- Warning: `subworkflows/local/bam_variant_calling_sentieon_haplotyper/main.nf:95:27`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
              no_intervals: it[0].num_intervals <= 1
                            ^^
  ```

- Warning: `subworkflows/local/bam_variant_calling_sentieon_haplotyper/main.nf:110:22`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      haplotyper_vcf = Channel.empty().mix(
                       ^^^^^^^
  ```

- Warning: `subworkflows/local/bam_variant_calling_sentieon_haplotyper/main.nf:114:22`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      haplotyper_tbi = Channel.empty().mix(
                       ^^^^^^^
  ```

- Warning: `subworkflows/local/bam_variant_calling_sentieon_haplotyper/main.nf:133:12`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      gvcf = Channel.empty().mix(
             ^^^^^^^
  ```

- Warning: `subworkflows/local/bam_variant_calling_sentieon_haplotyper/main.nf:137:16`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      gvcf_tbi = Channel.empty().mix(
                 ^^^^^^^
  ```

- Warning: `subworkflows/local/bam_variant_calling_single_strelka/main.nf:20:16`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      versions = Channel.empty()
                 ^^^^^^^
  ```

- Warning: `subworkflows/local/bam_variant_calling_single_strelka/main.nf:32:23`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          intervals:    it[0].num_intervals > 1
                        ^^
  ```

- Warning: `subworkflows/local/bam_variant_calling_single_strelka/main.nf:33:23`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          no_intervals: it[0].num_intervals <= 1
                        ^^
  ```

- Warning: `subworkflows/local/bam_variant_calling_single_strelka/main.nf:39:23`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          intervals:    it[0].num_intervals > 1
                        ^^
  ```

- Warning: `subworkflows/local/bam_variant_calling_single_strelka/main.nf:40:23`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          no_intervals: it[0].num_intervals <= 1
                        ^^
  ```

- Warning: `subworkflows/local/bam_variant_calling_single_strelka/main.nf:46:23`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          intervals:    it[0].num_intervals > 1
                        ^^
  ```

- Warning: `subworkflows/local/bam_variant_calling_single_strelka/main.nf:47:23`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          no_intervals: it[0].num_intervals <= 1
                        ^^
  ```

- Warning: `subworkflows/local/bam_variant_calling_single_strelka/main.nf:59:11`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      vcf = Channel.empty().mix(MERGE_STRELKA.out.vcf, vcf_out.no_intervals)
            ^^^^^^^
  ```

- Warning: `subworkflows/local/bam_variant_calling_single_strelka/main.nf:63:11`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      tbi = Channel.empty().mix(MERGE_STRELKA.out.tbi, tbi_out.no_intervals)
            ^^^^^^^
  ```

- Warning: `subworkflows/local/bam_variant_calling_single_tiddit/main.nf:17:16`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      versions = Channel.empty()
                 ^^^^^^^
  ```

- Warning: `subworkflows/local/bam_variant_calling_single_tiddit/main.nf:24:62`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
      vcf    = TABIX_BGZIP_TIDDIT_SV.out.gz_tbi.map{ meta, gz, tbi -> [ meta + [ variantcaller: 'tiddit'], gz ] }
                                                               ^^^
  ```

- Warning: `subworkflows/local/bam_variant_calling_single_tiddit/main.nf:25:58`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
      tbi    = TABIX_BGZIP_TIDDIT_SV.out.gz_tbi.map{ meta, gz, tbi -> [ meta + [ variantcaller: 'tiddit'], tbi ] }
                                                           ^^
  ```

- Warning: `subworkflows/local/bam_variant_calling_somatic_all/main.nf:55:16`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      versions = Channel.empty()
                 ^^^^^^^
  ```

- Warning: `subworkflows/local/bam_variant_calling_somatic_all/main.nf:58:24`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      out_indexcov     = Channel.empty()
                         ^^^^^^^
  ```

- Warning: `subworkflows/local/bam_variant_calling_somatic_all/main.nf:59:24`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      out_msisensorpro = Channel.empty()
                         ^^^^^^^
  ```

- Warning: `subworkflows/local/bam_variant_calling_somatic_all/main.nf:60:24`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      vcf_freebayes    = Channel.empty()
                         ^^^^^^^
  ```

- Warning: `subworkflows/local/bam_variant_calling_somatic_all/main.nf:61:24`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      vcf_manta        = Channel.empty()
                         ^^^^^^^
  ```

- Warning: `subworkflows/local/bam_variant_calling_somatic_all/main.nf:62:24`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      vcf_muse         = Channel.empty()
                         ^^^^^^^
  ```

- Warning: `subworkflows/local/bam_variant_calling_somatic_all/main.nf:63:24`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      vcf_mutect2      = Channel.empty()
                         ^^^^^^^
  ```

- Warning: `subworkflows/local/bam_variant_calling_somatic_all/main.nf:64:24`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      vcf_strelka      = Channel.empty()
                         ^^^^^^^
  ```

- Warning: `subworkflows/local/bam_variant_calling_somatic_all/main.nf:65:24`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      vcf_tiddit       = Channel.empty()
                         ^^^^^^^
  ```

- Warning: `subworkflows/local/bam_variant_calling_somatic_all/main.nf:66:24`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      vcf_tnscope      = Channel.empty()
                         ^^^^^^^
  ```

- Warning: `subworkflows/local/bam_variant_calling_somatic_all/main.nf:67:24`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      tbi_freebayes    = Channel.empty()
                         ^^^^^^^
  ```

- Warning: `subworkflows/local/bam_variant_calling_somatic_all/main.nf:68:24`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      tbi_manta        = Channel.empty()
                         ^^^^^^^
  ```

- Warning: `subworkflows/local/bam_variant_calling_somatic_all/main.nf:69:24`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      tbi_muse         = Channel.empty()
                         ^^^^^^^
  ```

- Warning: `subworkflows/local/bam_variant_calling_somatic_all/main.nf:70:24`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      tbi_mutect2      = Channel.empty()
                         ^^^^^^^
  ```

- Warning: `subworkflows/local/bam_variant_calling_somatic_all/main.nf:71:24`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      tbi_strelka      = Channel.empty()
                         ^^^^^^^
  ```

- Warning: `subworkflows/local/bam_variant_calling_somatic_all/main.nf:72:24`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      tbi_tiddit       = Channel.empty()
                         ^^^^^^^
  ```

- Warning: `subworkflows/local/bam_variant_calling_somatic_all/main.nf:73:24`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      tbi_tnscope      = Channel.empty()
                         ^^^^^^^
  ```

- Warning: `subworkflows/local/bam_variant_calling_somatic_all/main.nf:289:15`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      vcf_all = Channel.empty()
                ^^^^^^^
  ```

- Warning: `subworkflows/local/bam_variant_calling_somatic_all/main.nf:300:15`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      tbi_all = Channel.empty()
                ^^^^^^^
  ```

- Warning: `subworkflows/local/bam_variant_calling_somatic_ascat/main.nf:22:19`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_versions = Channel.empty()
                    ^^^^^^^
  ```

- Warning: `subworkflows/local/bam_variant_calling_somatic_controlfreec/main.nf:26:19`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_versions = Channel.empty()
                    ^^^^^^^
  ```

- Warning: `subworkflows/local/bam_variant_calling_somatic_controlfreec/main.nf:34:59`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          def tumor_file = cnv instanceof List ? cnv.find { it.toString().endsWith("gz_CNVs") } : cnv //only find if its a list, else it returns only the filename without the path
                                                            ^^
  ```

- Warning: `subworkflows/local/bam_variant_calling_somatic_controlfreec/main.nf:43:63`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          def tumor_file = ratio instanceof List ? ratio.find { it.toString().endsWith("gz_ratio.txt") } : ratio //same here as cnv
                                                                ^^
  ```

- Warning: `subworkflows/local/bam_variant_calling_somatic_manta/main.nf:17:16`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      versions = Channel.empty()
                 ^^^^^^^
  ```

- Warning: `subworkflows/local/bam_variant_calling_somatic_manta/main.nf:31:5`: Variable was declared but not used

  ```nextflow
      candidate_sv_vcf = MANTA_SOMATIC.out.candidate_sv_vcf
      ^^^^^^^^^^^^^^^^
  ```

- Warning: `subworkflows/local/bam_variant_calling_somatic_manta/main.nf:39:11`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      vcf = Channel.empty().mix(diploid_sv_vcf, somatic_sv_vcf).map{ meta, vcf -> [ meta + [ variantcaller:'manta' ], vcf ] }
            ^^^^^^^
  ```

- Warning: `subworkflows/local/bam_variant_calling_somatic_manta/main.nf:40:11`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      tbi = Channel.empty().mix(diploid_sv_vcf_tbi, somatic_sv_vcf_tbi).map{ meta, tbi -> [ meta + [ variantcaller:'manta' ], tbi ] }
            ^^^^^^^
  ```

- Warning: `subworkflows/local/bam_variant_calling_somatic_muse/main.nf:19:16`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      versions = Channel.empty()
                 ^^^^^^^
  ```

- Warning: `subworkflows/local/bam_variant_calling_somatic_mutect2/main.nf:31:16`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      versions = Channel.empty()
                 ^^^^^^^
  ```

- Warning: `subworkflows/local/bam_variant_calling_somatic_mutect2/main.nf:35:59`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
      germline_resource_pileup = germline_resource.filter { it != [] }
                                                            ^^
  ```

- Warning: `subworkflows/local/bam_variant_calling_somatic_mutect2/main.nf:36:67`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
      germline_resource_pileup_tbi = germline_resource_tbi.filter { it != [] }
                                                                    ^^
  ```

- Warning: `subworkflows/local/bam_variant_calling_somatic_mutect2/main.nf:72:20`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          intervals: it[0].num_intervals > 1
                     ^^
  ```

- Warning: `subworkflows/local/bam_variant_calling_somatic_mutect2/main.nf:73:23`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          no_intervals: it[0].num_intervals <= 1
                        ^^
  ```

- Warning: `subworkflows/local/bam_variant_calling_somatic_mutect2/main.nf:78:20`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          intervals: it[0].num_intervals > 1
                     ^^
  ```

- Warning: `subworkflows/local/bam_variant_calling_somatic_mutect2/main.nf:79:23`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          no_intervals: it[0].num_intervals <= 1
                        ^^
  ```

- Warning: `subworkflows/local/bam_variant_calling_somatic_mutect2/main.nf:84:20`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          intervals: it[0].num_intervals > 1
                     ^^
  ```

- Warning: `subworkflows/local/bam_variant_calling_somatic_mutect2/main.nf:85:23`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          no_intervals: it[0].num_intervals <= 1
                        ^^
  ```

- Warning: `subworkflows/local/bam_variant_calling_somatic_mutect2/main.nf:90:20`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          intervals: it[0].num_intervals > 1
                     ^^
  ```

- Warning: `subworkflows/local/bam_variant_calling_somatic_mutect2/main.nf:91:23`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          no_intervals: it[0].num_intervals <= 1
                        ^^
  ```

- Warning: `subworkflows/local/bam_variant_calling_somatic_mutect2/main.nf:103:11`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      vcf = Channel.empty()
            ^^^^^^^
  ```

- Warning: `subworkflows/local/bam_variant_calling_somatic_mutect2/main.nf:108:11`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      tbi = Channel.empty()
            ^^^^^^^
  ```

- Warning: `subworkflows/local/bam_variant_calling_somatic_mutect2/main.nf:113:13`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      stats = Channel.empty()
              ^^^^^^^
  ```

- Warning: `subworkflows/local/bam_variant_calling_somatic_mutect2/main.nf:118:12`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      f1r2 = Channel.empty()
             ^^^^^^^
  ```

- Warning: `subworkflows/local/bam_variant_calling_somatic_mutect2/main.nf:145:20`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          intervals: it[0].num_intervals > 1
                     ^^
  ```

- Warning: `subworkflows/local/bam_variant_calling_somatic_mutect2/main.nf:146:23`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          no_intervals: it[0].num_intervals <= 1
                        ^^
  ```

- Warning: `subworkflows/local/bam_variant_calling_somatic_mutect2/main.nf:151:20`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          intervals: it[0].num_intervals > 1
                     ^^
  ```

- Warning: `subworkflows/local/bam_variant_calling_somatic_mutect2/main.nf:152:23`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          no_intervals: it[0].num_intervals <= 1
                        ^^
  ```

- Warning: `subworkflows/local/bam_variant_calling_somatic_mutect2/main.nf:165:26`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      pileup_table_tumor = Channel.empty().mix(GATHERPILEUPSUMMARIES_TUMOR.out.table, pileup_table_tumor_branch.no_intervals).map { meta, table -> [meta - meta.subMap('normal_id', 'tumor_id', 'num_intervals') + [id: meta.patient], meta.id, table] }
                           ^^^^^^^
  ```

- Warning: `subworkflows/local/bam_variant_calling_somatic_mutect2/main.nf:166:27`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      pileup_table_normal = Channel.empty().mix(GATHERPILEUPSUMMARIES_NORMAL.out.table, pileup_table_normal_branch.no_intervals).map { meta, table -> [meta - meta.subMap('normal_id', 'tumor_id', 'num_intervals') + [id: meta.patient], meta.id, table] }
                            ^^^^^^^
  ```

- Warning: `subworkflows/local/bam_variant_calling_somatic_mutect2/main.nf:186:38`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      calculatecontamination_out_seg = Channel.empty()
                                       ^^^^^^^
  ```

- Warning: `subworkflows/local/bam_variant_calling_somatic_mutect2/main.nf:187:39`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      calculatecontamination_out_cont = Channel.empty()
                                        ^^^^^^^
  ```

- Warning: `subworkflows/local/bam_variant_calling_somatic_mutect2/main.nf:223:19`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          .unique { it[0] }
                    ^^
  ```

- Warning: `subworkflows/local/bam_variant_calling_somatic_mutect2/main.nf:228:19`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          .unique { it[0] }
                    ^^
  ```

- Warning: `subworkflows/local/bam_variant_calling_somatic_strelka/main.nf:20:16`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      versions = Channel.empty()
                 ^^^^^^^
  ```

- Warning: `subworkflows/local/bam_variant_calling_somatic_strelka/main.nf:32:23`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          intervals:    it[0].num_intervals > 1
                        ^^
  ```

- Warning: `subworkflows/local/bam_variant_calling_somatic_strelka/main.nf:33:23`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          no_intervals: it[0].num_intervals <= 1
                        ^^
  ```

- Warning: `subworkflows/local/bam_variant_calling_somatic_strelka/main.nf:39:23`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          intervals:    it[0].num_intervals > 1
                        ^^
  ```

- Warning: `subworkflows/local/bam_variant_calling_somatic_strelka/main.nf:40:23`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          no_intervals: it[0].num_intervals <= 1
                        ^^
  ```

- Warning: `subworkflows/local/bam_variant_calling_somatic_strelka/main.nf:53:23`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          intervals:    it[0].num_intervals > 1
                        ^^
  ```

- Warning: `subworkflows/local/bam_variant_calling_somatic_strelka/main.nf:54:23`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          no_intervals: it[0].num_intervals <= 1
                        ^^
  ```

- Warning: `subworkflows/local/bam_variant_calling_somatic_strelka/main.nf:60:23`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          intervals:    it[0].num_intervals > 1
                        ^^
  ```

- Warning: `subworkflows/local/bam_variant_calling_somatic_strelka/main.nf:61:23`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          no_intervals: it[0].num_intervals <= 1
                        ^^
  ```

- Warning: `subworkflows/local/bam_variant_calling_somatic_strelka/main.nf:65:11`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      vcf = Channel.empty().mix(MERGE_STRELKA_INDELS.out.vcf, MERGE_STRELKA_SNVS.out.vcf, vcf_indels.no_intervals, vcf_snvs.no_intervals)
            ^^^^^^^
  ```

- Warning: `subworkflows/local/bam_variant_calling_somatic_strelka/main.nf:69:11`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      tbi = Channel.empty().mix(MERGE_STRELKA_INDELS.out.tbi, MERGE_STRELKA_SNVS.out.tbi, tbi_indels.no_intervals, tbi_snvs.no_intervals)
            ^^^^^^^
  ```

- Warning: `subworkflows/local/bam_variant_calling_somatic_tiddit/main.nf:20:16`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      versions = Channel.empty()
                 ^^^^^^^
  ```

- Warning: `subworkflows/local/bam_variant_calling_somatic_tnscope/main.nf:22:16`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      versions = Channel.empty()
                 ^^^^^^^
  ```

- Warning: `subworkflows/local/bam_variant_calling_somatic_tnscope/main.nf:45:23`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          intervals:    it[0].num_intervals > 1
                        ^^
  ```

- Warning: `subworkflows/local/bam_variant_calling_somatic_tnscope/main.nf:46:23`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          no_intervals: it[0].num_intervals <= 1
                        ^^
  ```

- Warning: `subworkflows/local/bam_variant_calling_somatic_tnscope/main.nf:51:23`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          intervals:    it[0].num_intervals > 1
                        ^^
  ```

- Warning: `subworkflows/local/bam_variant_calling_somatic_tnscope/main.nf:52:23`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          no_intervals: it[0].num_intervals <= 1
                        ^^
  ```

- Warning: `subworkflows/local/bam_variant_calling_somatic_tnscope/main.nf:63:13`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      vcf   = Channel.empty()
              ^^^^^^^
  ```

- Warning: `subworkflows/local/bam_variant_calling_somatic_tnscope/main.nf:67:13`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      index = Channel.empty()
              ^^^^^^^
  ```

- Warning: `subworkflows/local/bam_variant_calling_tumor_only_all/main.nf:34:5`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
      intervals_bed_gz_tbi          // channel: [mandatory] [ interval.bed.gz, interval.bed.gz.tbi, num_intervals ] or [ [], [], 0 ] if no intervals
      ^^^^^^^^^^^^^^^^^^^^
  ```

- Warning: `subworkflows/local/bam_variant_calling_tumor_only_all/main.nf:48:16`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      versions = Channel.empty()
                 ^^^^^^^
  ```

- Warning: `subworkflows/local/bam_variant_calling_tumor_only_all/main.nf:51:22`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      out_msisensor2 = Channel.empty()
                       ^^^^^^^
  ```

- Warning: `subworkflows/local/bam_variant_calling_tumor_only_all/main.nf:52:22`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      vcf_freebayes  = Channel.empty()
                       ^^^^^^^
  ```

- Warning: `subworkflows/local/bam_variant_calling_tumor_only_all/main.nf:53:22`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      vcf_lofreq     = Channel.empty()
                       ^^^^^^^
  ```

- Warning: `subworkflows/local/bam_variant_calling_tumor_only_all/main.nf:54:22`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      vcf_manta      = Channel.empty()
                       ^^^^^^^
  ```

- Warning: `subworkflows/local/bam_variant_calling_tumor_only_all/main.nf:55:22`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      vcf_mpileup    = Channel.empty()
                       ^^^^^^^
  ```

- Warning: `subworkflows/local/bam_variant_calling_tumor_only_all/main.nf:56:22`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      vcf_mutect2    = Channel.empty()
                       ^^^^^^^
  ```

- Warning: `subworkflows/local/bam_variant_calling_tumor_only_all/main.nf:57:22`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      vcf_tiddit     = Channel.empty()
                       ^^^^^^^
  ```

- Warning: `subworkflows/local/bam_variant_calling_tumor_only_all/main.nf:58:22`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      vcf_tnscope    = Channel.empty()
                       ^^^^^^^
  ```

- Warning: `subworkflows/local/bam_variant_calling_tumor_only_all/main.nf:61:22`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      tbi_freebayes  = Channel.empty()
                       ^^^^^^^
  ```

- Warning: `subworkflows/local/bam_variant_calling_tumor_only_all/main.nf:62:22`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      tbi_lofreq     = Channel.empty()
                       ^^^^^^^
  ```

- Warning: `subworkflows/local/bam_variant_calling_tumor_only_all/main.nf:63:22`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      tbi_manta      = Channel.empty()
                       ^^^^^^^
  ```

- Warning: `subworkflows/local/bam_variant_calling_tumor_only_all/main.nf:64:22`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      tbi_mpileup    = Channel.empty()
                       ^^^^^^^
  ```

- Warning: `subworkflows/local/bam_variant_calling_tumor_only_all/main.nf:65:22`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      tbi_mutect2    = Channel.empty()
                       ^^^^^^^
  ```

- Warning: `subworkflows/local/bam_variant_calling_tumor_only_all/main.nf:66:22`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      tbi_tiddit     = Channel.empty()
                       ^^^^^^^
  ```

- Warning: `subworkflows/local/bam_variant_calling_tumor_only_all/main.nf:67:22`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      tbi_tnscope    = Channel.empty()
                       ^^^^^^^
  ```

- Warning: `subworkflows/local/bam_variant_calling_tumor_only_all/main.nf:221:15`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      vcf_all = Channel.empty()
                ^^^^^^^
  ```

- Warning: `subworkflows/local/bam_variant_calling_tumor_only_all/main.nf:232:15`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      tbi_all = Channel.empty()
                ^^^^^^^
  ```

- Warning: `subworkflows/local/bam_variant_calling_tumor_only_controlfreec/main.nf:26:19`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_versions = Channel.empty()
                    ^^^^^^^
  ```

- Warning: `subworkflows/local/bam_variant_calling_tumor_only_lofreq/main.nf:13:16`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      versions = Channel.empty()
                 ^^^^^^^
  ```

- Warning: `subworkflows/local/bam_variant_calling_tumor_only_lofreq/main.nf:25:23`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          intervals:    it[0].num_intervals > 1
                        ^^
  ```

- Warning: `subworkflows/local/bam_variant_calling_tumor_only_lofreq/main.nf:26:23`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          no_intervals: it[0].num_intervals <= 1
                        ^^
  ```

- Warning: `subworkflows/local/bam_variant_calling_tumor_only_lofreq/main.nf:32:23`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          intervals:    it[0].num_intervals > 1
                        ^^
  ```

- Warning: `subworkflows/local/bam_variant_calling_tumor_only_lofreq/main.nf:33:23`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          no_intervals: it[0].num_intervals <= 1
                        ^^
  ```

- Warning: `subworkflows/local/bam_variant_calling_tumor_only_lofreq/main.nf:43:11`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      vcf = Channel.empty().mix(MERGE_LOFREQ.out.vcf, vcf_branch.no_intervals).map{ meta, vcf -> [ meta - meta.subMap('num_intervals') + [ variantcaller:'lofreq' ], vcf ] }
            ^^^^^^^
  ```

- Warning: `subworkflows/local/bam_variant_calling_tumor_only_lofreq/main.nf:44:11`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      tbi = Channel.empty().mix(MERGE_LOFREQ.out.tbi, tbi_branch.no_intervals).map{ meta, tbi -> [ meta - meta.subMap('num_intervals') + [ variantcaller:'lofreq' ], tbi ] }
            ^^^^^^^
  ```

- Warning: `subworkflows/local/bam_variant_calling_tumor_only_manta/main.nf:18:16`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      versions = Channel.empty()
                 ^^^^^^^
  ```

- Warning: `subworkflows/local/bam_variant_calling_tumor_only_manta/main.nf:30:5`: Variable was declared but not used

  ```nextflow
      small_indels_vcf = MANTA_TUMORONLY.out.candidate_small_indels_vcf
      ^^^^^^^^^^^^^^^^
  ```

- Warning: `subworkflows/local/bam_variant_calling_tumor_only_manta/main.nf:31:5`: Variable was declared but not used

  ```nextflow
      candidate_sv_vcf = MANTA_TUMORONLY.out.candidate_sv_vcf
      ^^^^^^^^^^^^^^^^
  ```

- Warning: `subworkflows/local/bam_variant_calling_tumor_only_mutect2/main.nf:30:16`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      versions = Channel.empty()
                 ^^^^^^^
  ```

- Warning: `subworkflows/local/bam_variant_calling_tumor_only_mutect2/main.nf:34:59`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
      germline_resource_pileup = germline_resource.filter { it != [] }
                                                            ^^
  ```

- Warning: `subworkflows/local/bam_variant_calling_tumor_only_mutect2/main.nf:35:67`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
      germline_resource_pileup_tbi = germline_resource_tbi.filter { it != [] }
                                                                    ^^
  ```

- Warning: `subworkflows/local/bam_variant_calling_tumor_only_mutect2/main.nf:62:20`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          intervals: it[0].num_intervals > 1
                     ^^
  ```

- Warning: `subworkflows/local/bam_variant_calling_tumor_only_mutect2/main.nf:63:23`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          no_intervals: it[0].num_intervals <= 1
                        ^^
  ```

- Warning: `subworkflows/local/bam_variant_calling_tumor_only_mutect2/main.nf:68:20`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          intervals: it[0].num_intervals > 1
                     ^^
  ```

- Warning: `subworkflows/local/bam_variant_calling_tumor_only_mutect2/main.nf:69:23`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          no_intervals: it[0].num_intervals <= 1
                        ^^
  ```

- Warning: `subworkflows/local/bam_variant_calling_tumor_only_mutect2/main.nf:74:20`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          intervals: it[0].num_intervals > 1
                     ^^
  ```

- Warning: `subworkflows/local/bam_variant_calling_tumor_only_mutect2/main.nf:75:23`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          no_intervals: it[0].num_intervals <= 1
                        ^^
  ```

- Warning: `subworkflows/local/bam_variant_calling_tumor_only_mutect2/main.nf:80:20`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          intervals: it[0].num_intervals > 1
                     ^^
  ```

- Warning: `subworkflows/local/bam_variant_calling_tumor_only_mutect2/main.nf:81:23`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          no_intervals: it[0].num_intervals <= 1
                        ^^
  ```

- Warning: `subworkflows/local/bam_variant_calling_tumor_only_mutect2/main.nf:94:11`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      vcf = Channel.empty().mix(MERGE_MUTECT2.out.vcf, vcf_branch.no_intervals).map { meta, vcf -> [meta - meta.subMap('num_intervals'), vcf] }
            ^^^^^^^
  ```

- Warning: `subworkflows/local/bam_variant_calling_tumor_only_mutect2/main.nf:95:11`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      tbi = Channel.empty().mix(MERGE_MUTECT2.out.tbi, tbi_branch.no_intervals).map { meta, tbi -> [meta - meta.subMap('num_intervals'), tbi] }
            ^^^^^^^
  ```

- Warning: `subworkflows/local/bam_variant_calling_tumor_only_mutect2/main.nf:96:13`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      stats = Channel.empty().mix(MERGEMUTECTSTATS.out.stats, stats_branch.no_intervals).map { meta, stats -> [meta - meta.subMap('num_intervals'), stats] }
              ^^^^^^^
  ```

- Warning: `subworkflows/local/bam_variant_calling_tumor_only_mutect2/main.nf:97:12`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      f1r2 = Channel.empty().mix(f1r2_to_merge, f1r2_branch.no_intervals).map { meta, f1r2 -> [meta - meta.subMap('num_intervals'), f1r2] }
             ^^^^^^^
  ```

- Warning: `subworkflows/local/bam_variant_calling_tumor_only_mutect2/main.nf:109:20`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          intervals: it[0].num_intervals > 1
                     ^^
  ```

- Warning: `subworkflows/local/bam_variant_calling_tumor_only_mutect2/main.nf:110:23`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          no_intervals: it[0].num_intervals <= 1
                        ^^
  ```

- Warning: `subworkflows/local/bam_variant_calling_tumor_only_mutect2/main.nf:119:20`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      pileup_table = Channel.empty().mix(GATHERPILEUPSUMMARIES.out.table, pileup_table_branch.no_intervals).map { meta, table -> [meta - meta.subMap('num_intervals') + [id: meta.sample], table] }
                     ^^^^^^^
  ```

- Warning: `subworkflows/local/bam_variant_calling_tumor_only_mutect2/main.nf:125:38`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      calculatecontamination_out_seg = Channel.empty()
                                       ^^^^^^^
  ```

- Warning: `subworkflows/local/bam_variant_calling_tumor_only_mutect2/main.nf:126:39`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      calculatecontamination_out_cont = Channel.empty()
                                        ^^^^^^^
  ```

- Warning: `subworkflows/local/bam_variant_calling_tumor_only_mutect2/main.nf:160:19`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          .unique { it[0] }
                    ^^
  ```

- Warning: `subworkflows/local/bam_variant_calling_tumor_only_mutect2/main.nf:165:19`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          .unique { it[0] }
                    ^^
  ```

- Warning: `subworkflows/local/bam_variant_calling_tumor_only_tnscope/main.nf:22:16`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      versions = Channel.empty()
                 ^^^^^^^
  ```

- Warning: `subworkflows/local/bam_variant_calling_tumor_only_tnscope/main.nf:45:23`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          intervals:    it[0].num_intervals > 1
                        ^^
  ```

- Warning: `subworkflows/local/bam_variant_calling_tumor_only_tnscope/main.nf:46:23`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          no_intervals: it[0].num_intervals <= 1
                        ^^
  ```

- Warning: `subworkflows/local/bam_variant_calling_tumor_only_tnscope/main.nf:51:23`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          intervals:    it[0].num_intervals > 1
                        ^^
  ```

- Warning: `subworkflows/local/bam_variant_calling_tumor_only_tnscope/main.nf:52:23`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          no_intervals: it[0].num_intervals <= 1
                        ^^
  ```

- Warning: `subworkflows/local/bam_variant_calling_tumor_only_tnscope/main.nf:63:13`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      vcf   = Channel.empty()
              ^^^^^^^
  ```

- Warning: `subworkflows/local/bam_variant_calling_tumor_only_tnscope/main.nf:67:13`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      index = Channel.empty()
              ^^^^^^^
  ```

- Warning: `subworkflows/local/cram_merge_index_samtools/main.nf:17:16`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      versions = Channel.empty()
                 ^^^^^^^
  ```

- Warning: `subworkflows/local/cram_qc_mosdepth_samtools/main.nf:17:16`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      versions = Channel.empty()
                 ^^^^^^^
  ```

- Warning: `subworkflows/local/cram_qc_mosdepth_samtools/main.nf:18:15`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      reports = Channel.empty()
                ^^^^^^^
  ```

- Warning: `subworkflows/local/cram_qc_mosdepth_samtools/main.nf:23:43`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
      MOSDEPTH(cram.combine(intervals.map { meta, bed -> [bed ?: []] }), fasta)
                                            ^^^^
  ```

- Warning: `subworkflows/local/cram_sampleqc/main.nf:14:16`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      versions = Channel.empty()
                 ^^^^^^^
  ```

- Warning: `subworkflows/local/cram_sampleqc/main.nf:15:15`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      reports = Channel.empty()
                ^^^^^^^
  ```

- Warning: `subworkflows/local/download_cache_snpeff_vep/main.nf:20:16`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      versions = Channel.empty()
                 ^^^^^^^
  ```

- Warning: `subworkflows/local/fastq_align/main.nf:22:16`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      versions = Channel.empty()
                 ^^^^^^^
  ```

- Warning: `subworkflows/local/fastq_align/main.nf:23:15`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      reports = Channel.empty()
                ^^^^^^^
  ```

- Warning: `subworkflows/local/fastq_align/main.nf:34:11`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      bam = Channel.empty()
            ^^^^^^^
  ```

- Warning: `subworkflows/local/fastq_align/main.nf:38:67`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
      bam = bam.mix(SENTIEON_BWAMEM.out.bam_and_bai.map{ meta, bam, bai -> [ meta, bam ] })
                                                                    ^^^
  ```

- Warning: `subworkflows/local/fastq_align/main.nf:40:54`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
      bai = SENTIEON_BWAMEM.out.bam_and_bai.map{ meta, bam, bai -> [ meta, bai ] }
                                                       ^^^
  ```

- Warning: `subworkflows/local/fastq_create_umi_consensus_fgbio/main.nf:25:19`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_versions = Channel.empty()
                    ^^^^^^^
  ```

- Warning: `subworkflows/local/fastq_preprocess_gatk/main.nf:69:24`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      reports          = Channel.empty()
                         ^^^^^^^
  ```

- Warning: `subworkflows/local/fastq_preprocess_gatk/main.nf:70:24`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      versions         = Channel.empty()
                         ^^^^^^^
  ```

- Warning: `subworkflows/local/fastq_preprocess_gatk/main.nf:185:23`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
          aligned_bam = Channel.empty()
                        ^^^^^^^
  ```

- Warning: `subworkflows/local/fastq_preprocess_gatk/main.nf:186:23`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
          aligned_bai = Channel.empty()
                        ^^^^^^^
  ```

- Warning: `subworkflows/local/fastq_preprocess_gatk/main.nf:267:40`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
          cram_markduplicates_no_spark = Channel.empty()
                                         ^^^^^^^
  ```

- Warning: `subworkflows/local/fastq_preprocess_gatk/main.nf:268:40`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
          cram_sentieon_dedup          = Channel.empty()
                                         ^^^^^^^
  ```

- Warning: `subworkflows/local/fastq_preprocess_gatk/main.nf:269:40`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
          cram_markduplicates_spark    = Channel.empty()
                                         ^^^^^^^
  ```

- Warning: `subworkflows/local/fastq_preprocess_gatk/main.nf:285:36`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
          cram_skip_markduplicates = Channel.empty()
                                     ^^^^^^^
  ```

- Warning: `subworkflows/local/fastq_preprocess_gatk/main.nf:298:44`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
                  cram_skip_markduplicates = Channel.empty().mix(input_sample)
                                             ^^^^^^^
  ```

- Warning: `subworkflows/local/fastq_preprocess_gatk/main.nf:362:34`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
          ch_md_cram_for_restart = Channel.empty().mix(cram_markduplicates_no_spark, cram_markduplicates_spark, cram_sentieon_dedup)
                                   ^^^^^^^
  ```

- Warning: `subworkflows/local/fastq_preprocess_gatk/main.nf:383:48`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
              ch_cram_for_bam_baserecalibrator = Channel.empty().mix(input_sample)
                                                 ^^^^^^^
  ```

- Warning: `subworkflows/local/fastq_preprocess_gatk/main.nf:395:48`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
              ch_cram_for_bam_baserecalibrator = Channel.empty().mix(ch_md_cram_for_restart, cram_skip_markduplicates )
                                                 ^^^^^^^
  ```

- Warning: `subworkflows/local/fastq_preprocess_gatk/main.nf:404:38`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
              ch_table_bqsr_no_spark = Channel.empty()
                                       ^^^^^^^
  ```

- Warning: `subworkflows/local/fastq_preprocess_gatk/main.nf:405:38`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
              ch_table_bqsr_spark    = Channel.empty()
                                       ^^^^^^^
  ```

- Warning: `subworkflows/local/fastq_preprocess_gatk/main.nf:441:29`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
              ch_table_bqsr = Channel.empty().mix(
                              ^^^^^^^
  ```

- Warning: `subworkflows/local/fastq_preprocess_gatk/main.nf:460:30`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
              cram_applybqsr = Channel.empty().mix(input_sample)
                               ^^^^^^^
  ```

- Warning: `subworkflows/local/fastq_preprocess_gatk/main.nf:465:45`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
              cram_variant_calling_no_spark = Channel.empty()
                                              ^^^^^^^
  ```

- Warning: `subworkflows/local/fastq_preprocess_gatk/main.nf:466:45`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
              cram_variant_calling_spark    = Channel.empty()
                                              ^^^^^^^
  ```

- Warning: `subworkflows/local/fastq_preprocess_gatk/main.nf:497:36`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
              cram_variant_calling = Channel.empty().mix(
                                     ^^^^^^^
  ```

- Warning: `subworkflows/local/fastq_preprocess_gatk/main.nf:506:33`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
              csv_recalibration = Channel.empty()
                                  ^^^^^^^
  ```

- Warning: `subworkflows/local/fastq_preprocess_gatk/main.nf:516:36`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
              cram_variant_calling = Channel.empty().mix(input_sample.map{ meta, cram, crai, _table -> [ meta, cram, crai ] })
                                     ^^^^^^^
  ```

- Warning: `subworkflows/local/fastq_preprocess_gatk/main.nf:520:36`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
              cram_variant_calling = Channel.empty().mix(ch_cram_for_bam_baserecalibrator)
                                     ^^^^^^^
  ```

- Warning: `subworkflows/local/fastq_preprocess_parabricks/main.nf:15:19`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_versions = Channel.empty()
                    ^^^^^^^
  ```

- Warning: `subworkflows/local/fastq_preprocess_parabricks/main.nf:16:19`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_reports  = Channel.empty()
                    ^^^^^^^
  ```

- Warning: `subworkflows/local/fastq_preprocess_parabricks/main.nf:25:16`: Variable was declared but not used

  ```nextflow
          .set { reads_grouping_key }
                 ^^^^^^^^^^^^^^^^^^
  ```

- Warning: `subworkflows/local/post_variantcalling/main.nf:36:16`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      versions = Channel.empty()
                 ^^^^^^^
  ```

- Warning: `subworkflows/local/post_variantcalling/main.nf:37:12`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      vcfs = Channel.empty()
             ^^^^^^^
  ```

- Warning: `subworkflows/local/post_variantcalling/main.nf:38:12`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      tbis = Channel.empty()
             ^^^^^^^
  ```

- Warning: `subworkflows/local/post_variantcalling/main.nf:84:20`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
          all_vcfs = Channel.empty().mix(germline_vcfs, tumor_only_vcfs, somatic_vcfs)
                     ^^^^^^^
  ```

- Warning: `subworkflows/local/post_variantcalling/main.nf:85:48`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
                                  .branch{ meta, vcf ->
                                                 ^^^
  ```

- Warning: `subworkflows/local/post_variantcalling/main.nf:90:20`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
          all_tbis = Channel.empty().mix(germline_tbis, tumor_only_tbis, somatic_tbis)
                     ^^^^^^^
  ```

- Warning: `subworkflows/local/post_variantcalling/main.nf:91:48`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
                                  .branch{ meta, tbi ->
                                                 ^^^
  ```

- Warning: `subworkflows/local/post_variantcalling/main.nf:97:42`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          all_vcfs.other.subscribe { meta, vcf ->
                                           ^^^
  ```

- Warning: `subworkflows/local/prepare_genome/main.nf:57:16`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      versions = Channel.empty()
                 ^^^^^^^
  ```

- Warning: `subworkflows/local/prepare_genome/main.nf:60:24`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      fasta = fasta_in ? Channel.fromPath(fasta_in).map { fasta -> [[id: fasta.baseName], fasta] }.collect() : Channel.empty()
                         ^^^^^^^
  ```

- Warning: `subworkflows/local/prepare_genome/main.nf:60:110`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      fasta = fasta_in ? Channel.fromPath(fasta_in).map { fasta -> [[id: fasta.baseName], fasta] }.collect() : Channel.empty()
                                                                                                               ^^^^^^^
  ```

- Warning: `subworkflows/local/prepare_genome/main.nf:70:31`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
              index_alignment = Channel.fromPath(bwa_in).map { index -> [[id: 'bwa'], index] }.collect()
                                ^^^^^^^
  ```

- Warning: `subworkflows/local/prepare_genome/main.nf:78:31`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
              index_alignment = Channel.fromPath(bwamem2_in).map { index -> [[id: 'bwamem2'], index] }.collect()
                                ^^^^^^^
  ```

- Warning: `subworkflows/local/prepare_genome/main.nf:86:31`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
              index_alignment = Channel.fromPath(dragmap_in).map { index -> [[id: 'dragmap'], index] }.collect()
                                ^^^^^^^
  ```

- Warning: `subworkflows/local/prepare_genome/main.nf:90:27`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
          index_alignment = Channel.empty()
                            ^^^^^^^
  ```

- Warning: `subworkflows/local/prepare_genome/main.nf:99:16`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
          dict = Channel.fromPath(dict_in).map { it -> [[id: 'dict'], it] }.collect()
                 ^^^^^^^
  ```

- Warning: `subworkflows/local/prepare_genome/main.nf:102:16`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
          dict = Channel.empty()
                 ^^^^^^^
  ```

- Warning: `subworkflows/local/prepare_genome/main.nf:111:21`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
          fasta_fai = Channel.fromPath(fasta_fai_in).map { it -> [[id: 'fai'], it] }.collect()
                      ^^^^^^^
  ```

- Warning: `subworkflows/local/prepare_genome/main.nf:114:21`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
          fasta_fai = Channel.empty()
                      ^^^^^^^
  ```

- Warning: `subworkflows/local/prepare_genome/main.nf:118:21`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      bbsplit_index = Channel.empty()
                      ^^^^^^^
  ```

- Warning: `subworkflows/local/prepare_genome/main.nf:127:33`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
                  bbsplit_index = Channel.value(file(bbsplit_index_in, checkIfExists: true))
                                  ^^^^^^^
  ```

- Warning: `subworkflows/local/prepare_genome/main.nf:132:13`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
              Channel.from(file(bbsplit_fasta_list_in, checkIfExists: true))
              ^^^^^^^
  ```

- Warning: `subworkflows/local/prepare_genome/main.nf:137:29`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
                  .collect { [it] }
                              ^^
  ```

- Warning: `subworkflows/local/prepare_genome/main.nf:151:54`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      bcftools_annotations = bcftools_annotations_in ? Channel.fromPath(bcftools_annotations_in).collect() : Channel.value([])
                                                       ^^^^^^^
  ```

- Warning: `subworkflows/local/prepare_genome/main.nf:151:108`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      bcftools_annotations = bcftools_annotations_in ? Channel.fromPath(bcftools_annotations_in).collect() : Channel.value([])
                                                                                                             ^^^^^^^
  ```

- Warning: `subworkflows/local/prepare_genome/main.nf:152:62`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      bcftools_annotations_tbi = bcftools_annotations_tbi_in ? Channel.fromPath(bcftools_annotations_tbi_in).collect() : Channel.value([])
                                                               ^^^^^^^
  ```

- Warning: `subworkflows/local/prepare_genome/main.nf:152:120`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      bcftools_annotations_tbi = bcftools_annotations_tbi_in ? Channel.fromPath(bcftools_annotations_tbi_in).collect() : Channel.value([])
                                                                                                                         ^^^^^^^
  ```

- Warning: `subworkflows/local/prepare_genome/main.nf:160:24`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      dbsnp = dbsnp_in ? Channel.fromPath(dbsnp_in).collect() : Channel.value([])
                         ^^^^^^^
  ```

- Warning: `subworkflows/local/prepare_genome/main.nf:160:63`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      dbsnp = dbsnp_in ? Channel.fromPath(dbsnp_in).collect() : Channel.value([])
                                                                ^^^^^^^
  ```

- Warning: `subworkflows/local/prepare_genome/main.nf:161:32`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      dbsnp_tbi = dbsnp_tbi_in ? Channel.fromPath(dbsnp_tbi_in).collect() : Channel.value([])
                                 ^^^^^^^
  ```

- Warning: `subworkflows/local/prepare_genome/main.nf:161:75`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      dbsnp_tbi = dbsnp_tbi_in ? Channel.fromPath(dbsnp_tbi_in).collect() : Channel.value([])
                                                                            ^^^^^^^
  ```

- Warning: `subworkflows/local/prepare_genome/main.nf:169:48`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      germline_resource = germline_resource_in ? Channel.fromPath(germline_resource_in).collect() : Channel.value([])
                                                 ^^^^^^^
  ```

- Warning: `subworkflows/local/prepare_genome/main.nf:169:99`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      germline_resource = germline_resource_in ? Channel.fromPath(germline_resource_in).collect() : Channel.value([])
                                                                                                    ^^^^^^^
  ```

- Warning: `subworkflows/local/prepare_genome/main.nf:170:56`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      germline_resource_tbi = germline_resource_tbi_in ? Channel.fromPath(germline_resource_tbi_in).collect() : Channel.value([])
                                                         ^^^^^^^
  ```

- Warning: `subworkflows/local/prepare_genome/main.nf:170:111`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      germline_resource_tbi = germline_resource_tbi_in ? Channel.fromPath(germline_resource_tbi_in).collect() : Channel.value([])
                                                                                                                ^^^^^^^
  ```

- Warning: `subworkflows/local/prepare_genome/main.nf:178:38`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      known_indels = known_indels_in ? Channel.fromPath(known_indels_in).collect() : Channel.value([])
                                       ^^^^^^^
  ```

- Warning: `subworkflows/local/prepare_genome/main.nf:178:84`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      known_indels = known_indels_in ? Channel.fromPath(known_indels_in).collect() : Channel.value([])
                                                                                     ^^^^^^^
  ```

- Warning: `subworkflows/local/prepare_genome/main.nf:179:46`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      known_indels_tbi = known_indels_tbi_in ? Channel.fromPath(known_indels_tbi_in).collect() : Channel.value([])
                                               ^^^^^^^
  ```

- Warning: `subworkflows/local/prepare_genome/main.nf:179:96`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      known_indels_tbi = known_indels_tbi_in ? Channel.fromPath(known_indels_tbi_in).collect() : Channel.value([])
                                                                                                 ^^^^^^^
  ```

- Warning: `subworkflows/local/prepare_genome/main.nf:187:34`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      known_snps = known_snps_in ? Channel.fromPath(known_snps_in).collect() : Channel.value([])
                                   ^^^^^^^
  ```

- Warning: `subworkflows/local/prepare_genome/main.nf:187:78`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      known_snps = known_snps_in ? Channel.fromPath(known_snps_in).collect() : Channel.value([])
                                                                               ^^^^^^^
  ```

- Warning: `subworkflows/local/prepare_genome/main.nf:188:42`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      known_snps_tbi = known_snps_tbi_in ? Channel.fromPath(known_snps_tbi_in).collect() : Channel.value([])
                                           ^^^^^^^
  ```

- Warning: `subworkflows/local/prepare_genome/main.nf:188:90`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      known_snps_tbi = known_snps_tbi_in ? Channel.fromPath(known_snps_tbi_in).collect() : Channel.value([])
                                                                                           ^^^^^^^
  ```

- Warning: `subworkflows/local/prepare_genome/main.nf:196:20`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      pon = pon_in ? Channel.fromPath(pon_in).collect() : Channel.value([])
                     ^^^^^^^
  ```

- Warning: `subworkflows/local/prepare_genome/main.nf:196:57`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      pon = pon_in ? Channel.fromPath(pon_in).collect() : Channel.value([])
                                                          ^^^^^^^
  ```

- Warning: `subworkflows/local/prepare_genome/main.nf:197:28`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      pon_tbi = pon_tbi_in ? Channel.fromPath(pon_tbi_in).collect() : Channel.value([])
                             ^^^^^^^
  ```

- Warning: `subworkflows/local/prepare_genome/main.nf:197:69`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      pon_tbi = pon_tbi_in ? Channel.fromPath(pon_tbi_in).collect() : Channel.value([])
                                                                      ^^^^^^^
  ```

- Warning: `subworkflows/local/prepare_genome/main.nf:214:33`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
          UNTAR_MSISENSOR2_MODELS(Channel.fromPath(file(msisensor2_models_in)).map { archive -> [[id: archive.baseName], archive] })
                                  ^^^^^^^
  ```

- Warning: `subworkflows/local/prepare_genome/main.nf:219:29`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
          msisensor2_models = Channel.fromPath(msisensor2_models_in).map { model -> [[id:model.baseName], model] }.collect()
                              ^^^^^^^
  ```

- Warning: `subworkflows/local/prepare_genome/main.nf:222:29`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
          msisensor2_models = Channel.value([])
                              ^^^^^^^
  ```

- Warning: `subworkflows/local/prepare_genome/main.nf:226:29`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
          msisensorpro_scan = Channel.fromPath(msisensorpro_scan_in)
                              ^^^^^^^
  ```

- Warning: `subworkflows/local/prepare_genome/main.nf:234:29`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
          msisensorpro_scan = Channel.value([])
                              ^^^^^^^
  ```

- Warning: `subworkflows/local/prepare_genome/main.nf:239:25`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
          ascat_alleles = Channel.empty()
                          ^^^^^^^
  ```

- Warning: `subworkflows/local/prepare_genome/main.nf:242:23`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
          UNZIP_ALLELES(Channel.fromPath(file(ascat_alleles_in)).map { archive -> [[id: archive.baseName], archive] })
                        ^^^^^^^
  ```

- Warning: `subworkflows/local/prepare_genome/main.nf:247:25`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
          ascat_alleles = Channel.fromPath(ascat_alleles_in).collect()
                          ^^^^^^^
  ```

- Warning: `subworkflows/local/prepare_genome/main.nf:251:22`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
          ascat_loci = Channel.empty()
                       ^^^^^^^
  ```

- Warning: `subworkflows/local/prepare_genome/main.nf:254:20`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
          UNZIP_LOCI(Channel.fromPath(file(ascat_loci_in)).map { archive -> [[id: archive.baseName], archive] })
                     ^^^^^^^
  ```

- Warning: `subworkflows/local/prepare_genome/main.nf:259:22`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
          ascat_loci = Channel.fromPath(ascat_loci_in).collect()
                       ^^^^^^^
  ```

- Warning: `subworkflows/local/prepare_genome/main.nf:263:25`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
          ascat_loci_gc = Channel.value([])
                          ^^^^^^^
  ```

- Warning: `subworkflows/local/prepare_genome/main.nf:266:18`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
          UNZIP_GC(Channel.fromPath(file(ascat_loci_gc_in)).map { archive -> [[id: archive.baseName], archive] })
                   ^^^^^^^
  ```

- Warning: `subworkflows/local/prepare_genome/main.nf:271:25`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
          ascat_loci_gc = Channel.fromPath(ascat_loci_gc_in).collect()
                          ^^^^^^^
  ```

- Warning: `subworkflows/local/prepare_genome/main.nf:275:25`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
          ascat_loci_rt = Channel.value([])
                          ^^^^^^^
  ```

- Warning: `subworkflows/local/prepare_genome/main.nf:278:18`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
          UNZIP_RT(Channel.fromPath(file(ascat_loci_rt_in)).map { archive -> [[id: archive.baseName], archive] })
                   ^^^^^^^
  ```

- Warning: `subworkflows/local/prepare_genome/main.nf:283:25`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
          ascat_loci_rt = Channel.fromPath(ascat_loci_rt_in).collect()
                          ^^^^^^^
  ```

- Warning: `subworkflows/local/prepare_genome/main.nf:287:19`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
          chr_dir = Channel.value([])
                    ^^^^^^^
  ```

- Warning: `subworkflows/local/prepare_genome/main.nf:290:23`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
          UNTAR_CHR_DIR(Channel.fromPath(file(chr_dir_in)).map { archive -> [[id: archive.baseName], archive] })
                        ^^^^^^^
  ```

- Warning: `subworkflows/local/prepare_genome/main.nf:295:19`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
          chr_dir = Channel.fromPath(chr_dir_in).collect()
                    ^^^^^^^
  ```

- Warning: `subworkflows/local/prepare_reference_cnvkit/main.nf:10:16`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      versions = Channel.empty()
                 ^^^^^^^
  ```

- Warning: `subworkflows/local/samplesheet_to_channel/main.nf:13:5`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
      bcftools_columns              // Path: bcftools columns
      ^^^^^^^^^^^^^^^^
  ```

- Warning: `subworkflows/local/samplesheet_to_channel/main.nf:53:49`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
              def status0_count = samples.count { it.status == 0 }
                                                  ^^
  ```

- Warning: `subworkflows/local/samplesheet_to_channel/main.nf:54:49`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
              def status1_count = samples.count { it.status == 1 }
                                                  ^^
  ```

- Warning: `subworkflows/local/samplesheet_to_channel/main.nf:70:16`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          .map { combination_key, combination_list ->
                 ^^^^^^^^^^^^^^^
  ```

- Warning: `subworkflows/local/samplesheet_to_channel/main.nf:90:41`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
              [patient, samples.collect { it.sample }]
                                          ^^
  ```

- Warning: `subworkflows/local/samplesheet_to_channel/main.nf:242:23`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
              .filter { it[0].status == 1 }
                        ^^
  ```

- Warning: `subworkflows/local/samplesheet_to_channel/main.nf:260:23`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
              .filter { it[0].status == 0 }
                        ^^
  ```

- Warning: `subworkflows/local/samplesheet_to_channel/main.nf:430:17`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
              if (it[0].sex == 'NA') {
                  ^^
  ```

- Warning: `subworkflows/local/samplesheet_to_channel/main.nf:439:17`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
              if (it[0].status == 1 && !it[0].containsKey('contamination')) {
                  ^^
  ```

- Warning: `subworkflows/local/samplesheet_to_channel/main.nf:439:39`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
              if (it[0].status == 1 && !it[0].containsKey('contamination')) {
                                        ^^
  ```

- Warning: `subworkflows/local/vcf_annotate_all/main.nf:28:15`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      reports = Channel.empty()
                ^^^^^^^
  ```

- Warning: `subworkflows/local/vcf_annotate_all/main.nf:29:15`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      vcf_ann = Channel.empty()
                ^^^^^^^
  ```

- Warning: `subworkflows/local/vcf_annotate_all/main.nf:30:15`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      tab_ann = Channel.empty()
                ^^^^^^^
  ```

- Warning: `subworkflows/local/vcf_annotate_all/main.nf:31:16`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      json_ann = Channel.empty()
                 ^^^^^^^
  ```

- Warning: `subworkflows/local/vcf_annotate_all/main.nf:32:16`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      versions = Channel.empty()
                 ^^^^^^^
  ```

- Warning: `subworkflows/local/vcf_concatenate_germline/main.nf:17:16`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      versions = Channel.empty()
                 ^^^^^^^
  ```

- Warning: `subworkflows/local/vcf_consensus/main.nf:14:19`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_versions = Channel.empty()
                    ^^^^^^^
  ```

- Warning: `subworkflows/local/vcf_consensus/main.nf:17:24`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          .branch{ meta, vcf, tbi ->
                         ^^^
  ```

- Warning: `subworkflows/local/vcf_consensus/main.nf:17:29`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          .branch{ meta, vcf, tbi ->
                              ^^^
  ```

- Warning: `subworkflows/local/vcf_consensus/main.nf:65:36`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
              def vcf = files.find { it.name == '0000.vcf.gz' }
                                     ^^
  ```

- Warning: `subworkflows/local/vcf_consensus/main.nf:66:36`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
              def tbi = files.find { it.name == '0000.vcf.gz.tbi' }
                                     ^^
  ```

- Warning: `subworkflows/local/vcf_normalization/main.nf:16:16`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      versions = Channel.empty()
                 ^^^^^^^
  ```

- Warning: `subworkflows/local/vcf_qc_bcftools_vcftools/main.nf:13:16`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      versions = Channel.empty()
                 ^^^^^^^
  ```

- Warning: `subworkflows/local/vcf_variant_filtering_gatk/main.nf:17:16`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      versions = Channel.empty()
                 ^^^^^^^
  ```

- Warning: `subworkflows/local/vcf_varlociraptor_single/main.nf:20:19`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_versions = Channel.empty()
                    ^^^^^^^
  ```

- Warning: `subworkflows/local/vcf_varlociraptor_somatic/main.nf:26:19`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_versions = Channel.empty()
                    ^^^^^^^
  ```

- Warning: `subworkflows/local/vcf_varlociraptor_somatic/main.nf:67:18`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          strelka: it[0].variantcaller == 'strelka'
                   ^^
  ```

- Warning: `subworkflows/local/vcf_varlociraptor_somatic/main.nf:68:16`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          other: it[0].variantcaller != 'strelka'
                 ^^
  ```

- Warning: `subworkflows/local/vcf_varlociraptor_somatic/main.nf:105:18`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          matched: it.size() == 7
                   ^^
  ```

- Warning: `subworkflows/local/vcf_varlociraptor_somatic/main.nf:106:20`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          unmatched: it.size() == 4
                     ^^
  ```

- Warning: `subworkflows/local/vcf_varlociraptor_somatic/main.nf:214:9`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
          Channel.value(["normal", "tumor"]),
          ^^^^^^^
  ```

- Warning: `subworkflows/nf-core/bam_ngscheckmate/main.nf:13:19`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_versions = Channel.empty()
                    ^^^^^^^
  ```

- Warning: `subworkflows/nf-core/vcf_annotate_ensemblvep/main.nf:19:19`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_versions = Channel.empty()
                    ^^^^^^^
  ```

- Warning: `subworkflows/nf-core/vcf_annotate_snpeff/main.nf:15:19`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_versions = Channel.empty()
                    ^^^^^^^
  ```

- Warning: `workflows/sarek/main.nf:140:18`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
              bam: it[0].data_type == "bam"
                   ^^
  ```

- Warning: `workflows/sarek/main.nf:141:23`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
              fastq_gz: it[0].data_type == "fastq_gz"
                        ^^
  ```

- Warning: `workflows/sarek/main.nf:142:34`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
              one_fastq_gz_spring: it[0].data_type == "one_fastq_gz_spring"
                                   ^^
  ```

- Warning: `workflows/sarek/main.nf:143:34`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
              two_fastq_gz_spring: it[0].data_type == "two_fastq_gz_spring"
                                   ^^
  ```

- Warning: `workflows/sarek/main.nf:286:77`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
              cram_variant_calling_status_tmp = cram_variant_calling.branch { meta, file, index ->
                                                                              ^^^^
  ```

- Warning: `workflows/sarek/main.nf:286:89`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
              cram_variant_calling_status_tmp = cram_variant_calling.branch { meta, file, index ->
                                                                                          ^^^^^
  ```

- Warning: `workflows/sarek/main.nf:306:75`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          cram_variant_calling_status = cram_variant_calling.branch { meta, file, index ->
                                                                            ^^^^
  ```

- Warning: `workflows/sarek/main.nf:306:81`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          cram_variant_calling_status = cram_variant_calling.branch { meta, file, index ->
                                                                                  ^^^^^
  ```

- Warning: `workflows/sarek/main.nf:312:73`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          bam_variant_calling_status = bam_variant_calling.branch { meta, file, index ->
                                                                          ^^^^
  ```

- Warning: `workflows/sarek/main.nf:312:79`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          bam_variant_calling_status = bam_variant_calling.branch { meta, file, index ->
                                                                                ^^^^^
  ```

- Warning: `workflows/sarek/main.nf:688:76`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
              def InputStream gzipStream = new java.util.zip.GZIPInputStream(it)
                                                                             ^^
  ```
