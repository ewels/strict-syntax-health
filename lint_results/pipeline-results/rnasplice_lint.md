# Nextflow lint results

- Generated: 2026-01-16T10:28:30.475825624Z
- Nextflow version: 25.12.0-edge
- Summary: 49 errors, 190 warnings

## :x: Errors

- Error: `conf/modules.config:915:13`: Unexpected input: ':'

  ```nextflow
      withName: 'MULTIQC' {
              ^
  ```

- Error: `main.nf:41:1`: Module could not be parsed: '/home/runner/work/strict-syntax-health/strict-syntax-health/pipelines/rnasplice/workflows/rnasplice.nf'

  ```nextflow
  include { RNASPLICE } from './workflows/rnasplice'
  ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  ```

- Error: `main.nf:67:5`: `RNASPLICE` is not defined

  ```nextflow
      RNASPLICE ()
      ^^^^^^^^^
  ```

- Error: `main.nf:79:9`: `RNASPLICE` is not defined

  ```nextflow
          RNASPLICE.out.final_multiqc_report
          ^^^^^^^^^
  ```

- Error: `modules/local/create_bamlist_single.nf:13:34`: `cond` is not defined

  ```nextflow
      tuple val(contrast), path("${cond}_bamlist.txt"), emit: bamlist
                                   ^^^^
  ```

- Error: `modules/local/create_bamlist_single.nf:21:10`: `bam` is not defined

  ```nextflow
      echo $bam | sed 's: :,:g' > ${cond}_bamlist.txt
           ^^^^
  ```

- Error: `modules/local/create_bamlist_single.nf:21:35`: `cond` is not defined

  ```nextflow
      echo $bam | sed 's: :,:g' > ${cond}_bamlist.txt
                                    ^^^^
  ```

- Error: `modules/local/dexseq_annotation.nf:26:9`: `aggregation` is already declared

  ```nextflow
      def aggregation = aggregation ? '' : '-r no'
          ^^^^^^^^^^^
  ```

- Error: `modules/local/dexseq_count.nf:28:9`: `alignment_quality` is already declared

  ```nextflow
      def alignment_quality = "-a ${alignment_quality}"
          ^^^^^^^^^^^^^^^^^
  ```

- Error: `modules/local/rmats_prep_single.nf:60:14`: `bam_group1` is not defined

  ```nextflow
          --b1 $bam_group1 \\
               ^^^^^^^^^^^
  ```

- Error: `modules/local/samplesheet_check.nf:24:22`: Unexpected input: '\n'

  ```nextflow
          case 'fastq':
                       ^
  ```

- Error: `modules/local/star_align_igenomes.nf:40:9`: `seq_platform` is already declared

  ```nextflow
      def seq_platform    = seq_platform ? "'PL:$seq_platform'" : ""
          ^^^^^^^^^^^^
  ```

- Error: `modules/local/star_align_igenomes.nf:41:9`: `seq_center` is already declared

  ```nextflow
      def seq_center      = seq_center ? "--outSAMattrRGline ID:$prefix 'CN:$seq_center' 'SM:$prefix' $seq_platform " : "--outSAMattrRGline ID:$prefix 'SM:$prefix' $seq_platform "
          ^^^^^^^^^^
  ```

- Error: `modules/local/suppa_clusterevents.nf:4:5`: Invalid process directive

  ```nextflow
      stageInMode = 'copy'
      ^^^^^^^^^^^^^^^^^^^^
  ```

- Error: `modules/local/suppa_clusterevents.nf:13:15`: `cond1` is already declared

  ```nextflow
      tuple val(cond1), val(cond2), path(psivec)
                ^^^^^
  ```

- Error: `modules/local/suppa_clusterevents.nf:13:27`: `cond2` is already declared

  ```nextflow
      tuple val(cond1), val(cond2), path(psivec)
                            ^^^^^
  ```

- Error: `modules/local/suppa_clusterevents.nf:14:15`: `cond1` is already declared

  ```nextflow
      tuple val(cond1), val(cond2), val(group_ranges) // e.g. 1-3,4-6
                ^^^^^
  ```

- Error: `modules/local/suppa_clusterevents.nf:14:27`: `cond2` is already declared

  ```nextflow
      tuple val(cond1), val(cond2), val(group_ranges) // e.g. 1-3,4-6
                            ^^^^^
  ```

- Error: `modules/local/suppa_clusterevents.nf:34:9`: `clusterevents_sigthreshold` is already declared

  ```nextflow
      def clusterevents_sigthreshold  = clusterevents_sigthreshold ? "-st ${params.clusterevents_sigthreshold}" : ''
          ^^^^^^^^^^^^^^^^^^^^^^^^^^
  ```

- Error: `modules/local/suppa_clusterevents.nf:35:9`: `clusterevents_separation` is already declared

  ```nextflow
      def clusterevents_separation = clusterevents_separation ? "-s ${params.clusterevents_separation}" : ''
          ^^^^^^^^^^^^^^^^^^^^^^^^
  ```

- Error: `modules/local/suppa_diffsplice.nf:13:15`: `cond1` is already declared

  ```nextflow
      tuple val(cond1), val(cond2), path(psi1), path(psi2)
                ^^^^^
  ```

- Error: `modules/local/suppa_diffsplice.nf:13:27`: `cond2` is already declared

  ```nextflow
      tuple val(cond1), val(cond2), path(psi1), path(psi2)
                            ^^^^^
  ```

- Error: `modules/nf-core/multiqc/main.nf:28:31`: Unexpected input: '/'

  ```nextflow
      def logo = multiqc_logo ? /--cl-config 'custom_logo: "${multiqc_logo}"'/ : ''
                                ^
  ```

- Error: `modules/nf-core/star/align/main.nf:43:20`: Unexpected input: ','

  ```nextflow
      def reads1 = [], reads2 = []
                     ^
  ```

- Error: `nextflow.config:302:5`: Unexpected input: 'includeConfig'

  ```nextflow
      includeConfig 'conf/igenomes.config'
      ^
  ```

- Error: `subworkflows/local/align_star.nf:5:1`: Module could not be parsed: '/home/runner/work/strict-syntax-health/strict-syntax-health/pipelines/rnasplice/modules/nf-core/star/align/main.nf'

  ```nextflow
  include { STAR_ALIGN               } from '../../modules/nf-core/star/align/main'
  ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  ```

- Error: `subworkflows/local/align_star.nf:51:9`: `STAR_ALIGN` is not defined

  ```nextflow
          STAR_ALIGN ( reads, index, gtf, star_ignore_sjdbgtf, seq_platform, seq_center )
          ^^^^^^^^^^
  ```

- Error: `subworkflows/local/align_star.nf:52:29`: `STAR_ALIGN` is not defined

  ```nextflow
          ch_orig_bam       = STAR_ALIGN.out.bam
                              ^^^^^^^^^^
  ```

- Error: `subworkflows/local/align_star.nf:53:29`: `STAR_ALIGN` is not defined

  ```nextflow
          ch_log_final      = STAR_ALIGN.out.log_final
                              ^^^^^^^^^^
  ```

- Error: `subworkflows/local/align_star.nf:54:29`: `STAR_ALIGN` is not defined

  ```nextflow
          ch_log_out        = STAR_ALIGN.out.log_out
                              ^^^^^^^^^^
  ```

- Error: `subworkflows/local/align_star.nf:55:29`: `STAR_ALIGN` is not defined

  ```nextflow
          ch_log_progress   = STAR_ALIGN.out.log_progress
                              ^^^^^^^^^^
  ```

- Error: `subworkflows/local/align_star.nf:56:29`: `STAR_ALIGN` is not defined

  ```nextflow
          ch_bam_sorted     = STAR_ALIGN.out.bam_sorted
                              ^^^^^^^^^^
  ```

- Error: `subworkflows/local/align_star.nf:57:29`: `STAR_ALIGN` is not defined

  ```nextflow
          ch_bam_transcript = STAR_ALIGN.out.bam_transcript
                              ^^^^^^^^^^
  ```

- Error: `subworkflows/local/align_star.nf:58:29`: `STAR_ALIGN` is not defined

  ```nextflow
          ch_fastq          = STAR_ALIGN.out.fastq
                              ^^^^^^^^^^
  ```

- Error: `subworkflows/local/align_star.nf:59:29`: `STAR_ALIGN` is not defined

  ```nextflow
          ch_tab            = STAR_ALIGN.out.tab
                              ^^^^^^^^^^
  ```

- Error: `subworkflows/local/align_star.nf:60:45`: `STAR_ALIGN` is not defined

  ```nextflow
          ch_versions       = ch_versions.mix(STAR_ALIGN.out.versions.first())
                                              ^^^^^^^^^^
  ```

- Error: `subworkflows/local/input_check.nf:15:22`: Unexpected input: '\n'

  ```nextflow
          case 'fastq':
                       ^
  ```

- Error: `subworkflows/local/tx2gene_tximport.nf:27:13`: Variables in a closure should be declared with `def`

  ```nextflow
              tgz = prefix[0].toString().endsWith(".tar.gz") ? true : false
              ^^^
  ```

- Error: `subworkflows/nf-core/fastq_fastqc_umitools_trimgalore/main.nf:59:31`: `reads` is already declared

  ```nextflow
                          meta, reads ->
                                ^^^^^
  ```

- Error: `subworkflows/nf-core/fastq_fastqc_umitools_trimgalore/main.nf:88:23`: `reads` is already declared

  ```nextflow
                  meta, reads, trim_log ->
                        ^^^^^
  ```

- Error: `subworkflows/nf-core/fastq_fastqc_umitools_trimgalore/main.nf:88:30`: `trim_log` is already declared

  ```nextflow
                  meta, reads, trim_log ->
                               ^^^^^^^^
  ```

- Error: `subworkflows/nf-core/fastq_fastqc_umitools_trimgalore/main.nf:90:25`: Variables in a closure should be declared with `def`

  ```nextflow
                          num_reads = getTrimGaloreReadsAfterFiltering(meta.single_end ? trim_log : trim_log[-1])
                          ^^^^^^^^^
  ```

- Error: `subworkflows/nf-core/fastq_fastqc_umitools_trimgalore/main.nf:99:29`: `reads` is already declared

  ```nextflow
              .filter { meta, reads, num_reads -> num_reads >= min_trimmed_reads.toFloat() }
                              ^^^^^
  ```

- Error: `subworkflows/nf-core/fastq_fastqc_umitools_trimgalore/main.nf:99:36`: `num_reads` is already declared

  ```nextflow
              .filter { meta, reads, num_reads -> num_reads >= min_trimmed_reads.toFloat() }
                                     ^^^^^^^^^
  ```

- Error: `subworkflows/nf-core/fastq_fastqc_umitools_trimgalore/main.nf:100:26`: `reads` is already declared

  ```nextflow
              .map { meta, reads, num_reads -> [ meta, reads ] }
                           ^^^^^
  ```

- Error: `subworkflows/nf-core/fastq_fastqc_umitools_trimgalore/main.nf:100:33`: `num_reads` is already declared

  ```nextflow
              .map { meta, reads, num_reads -> [ meta, reads ] }
                                  ^^^^^^^^^
  ```

- Error: `subworkflows/nf-core/fastq_fastqc_umitools_trimgalore/main.nf:104:26`: `reads` is already declared

  ```nextflow
              .map { meta, reads, num_reads -> [ meta, num_reads ] }
                           ^^^^^
  ```

- Error: `subworkflows/nf-core/fastq_fastqc_umitools_trimgalore/main.nf:104:33`: `num_reads` is already declared

  ```nextflow
              .map { meta, reads, num_reads -> [ meta, num_reads ] }
                                  ^^^^^^^^^
  ```

- Error: `workflows/rnasplice.nf:155:22`: Unexpected input: '\n'

  ```nextflow
          case 'fastq':
                       ^
  ```

## :warning: Warnings

- Warning: `modules/local/dexseq_annotation.nf:23:9`: Variable was declared but not used

  ```nextflow
      def args = task.ext.args ?: ''
          ^^^^
  ```

- Warning: `modules/local/dexseq_count.nf:23:9`: Variable was declared but not used

  ```nextflow
      def args = task.ext.args ?: ''
          ^^^^
  ```

- Warning: `modules/local/drimseq_filter.nf:30:9`: Variable was declared but not used

  ```nextflow
      def args = task.ext.args ?: ''
          ^^^^
  ```

- Warning: `modules/local/isoformswitchanalyzer.nf:29:9`: Variable was declared but not used

  ```nextflow
      def args = task.ext.args ?: ''
          ^^^^
  ```

- Warning: `modules/local/rmats_post.nf:33:9`: Variable was declared but not used

  ```nextflow
      def args = task.ext.args ?: ''
          ^^^^
  ```

- Warning: `modules/local/rmats_post_single.nf:32:9`: Variable was declared but not used

  ```nextflow
      def args = task.ext.args ?: ''
          ^^^^
  ```

- Warning: `modules/local/rmats_prep.nf:31:9`: Variable was declared but not used

  ```nextflow
      def args = task.ext.args ?: ''
          ^^^^
  ```

- Warning: `modules/local/rmats_prep_single.nf:31:9`: Variable was declared but not used

  ```nextflow
      def args = task.ext.args ?: ''
          ^^^^
  ```

- Warning: `modules/local/stager.nf:23:9`: Variable was declared but not used

  ```nextflow
      def args = task.ext.args ?: ''
          ^^^^
  ```

- Warning: `modules/local/suppa_clusterevents.nf:12:15`: Variable was declared but not used

  ```nextflow
      tuple val(cond1), val(cond2), path(dpsi)
                ^^^^^
  ```

- Warning: `modules/local/suppa_clusterevents.nf:12:27`: Variable was declared but not used

  ```nextflow
      tuple val(cond1), val(cond2), path(dpsi)
                            ^^^^^
  ```

- Warning: `modules/local/suppa_clusterevents.nf:13:15`: Variable was declared but not used

  ```nextflow
      tuple val(cond1), val(cond2), path(psivec)
                ^^^^^
  ```

- Warning: `modules/local/suppa_clusterevents.nf:13:27`: Variable was declared but not used

  ```nextflow
      tuple val(cond1), val(cond2), path(psivec)
                            ^^^^^
  ```

- Warning: `modules/local/suppa_diffsplice.nf:12:15`: Variable was declared but not used

  ```nextflow
      tuple val(cond1), val(cond2), path(tpm1), path(tpm2)
                ^^^^^
  ```

- Warning: `modules/local/suppa_diffsplice.nf:12:27`: Variable was declared but not used

  ```nextflow
      tuple val(cond1), val(cond2), path(tpm1), path(tpm2)
                            ^^^^^
  ```

- Warning: `modules/nf-core/cat/fastq/main.nf:21:9`: Variable was declared but not used

  ```nextflow
      def args = task.ext.args ?: ''
          ^^^^
  ```

- Warning: `modules/nf-core/cat/fastq/main.nf:23:59`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
      def readList = reads instanceof List ? reads.collect{ it.toString() } : [reads.toString()]
                                                            ^^
  ```

- Warning: `modules/nf-core/cat/fastq/main.nf:54:59`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
      def readList = reads instanceof List ? reads.collect{ it.toString() } : [reads.toString()]
                                                            ^^
  ```

- Warning: `modules/nf-core/custom/dumpsoftwareversions/main.nf:22:9`: Variable was declared but not used

  ```nextflow
      def args = task.ext.args ?: ''
          ^^^^
  ```

- Warning: `modules/nf-core/custom/getchromsizes/main.nf:23:9`: Variable was declared but not used

  ```nextflow
      def args = task.ext.args ?: ''
          ^^^^
  ```

- Warning: `modules/nf-core/fastqc/main.nf:27:48`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
      def renamed_files = old_new_pairs.collect{ old_name, new_name -> new_name }.join(' ')
                                                 ^^^^^^^^
  ```

- Warning: `modules/nf-core/rsem/preparereference/main.nf:27:30`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          args_list.removeIf { it.contains('--star') }
                               ^^
  ```

- Warning: `modules/nf-core/samtools/flagstat/main.nf:21:9`: Variable was declared but not used

  ```nextflow
      def args = task.ext.args ?: ''
          ^^^^
  ```

- Warning: `modules/nf-core/samtools/idxstats/main.nf:21:9`: Variable was declared but not used

  ```nextflow
      def args = task.ext.args ?: ''
          ^^^^
  ```

- Warning: `modules/nf-core/samtools/stats/main.nf:22:9`: Variable was declared but not used

  ```nextflow
      def args = task.ext.args ?: ''
          ^^^^
  ```

- Warning: `modules/nf-core/trimgalore/main.nf:41:31`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          args_list.removeAll { it.toLowerCase().contains('_r2 ') }
                                ^^
  ```

- Warning: `modules/nf-core/ucsc/bedclip/main.nf:23:9`: Variable was declared but not used

  ```nextflow
      def args = task.ext.args ?: ''
          ^^^^
  ```

- Warning: `modules/nf-core/ucsc/bedgraphtobigwig/main.nf:23:9`: Variable was declared but not used

  ```nextflow
      def args = task.ext.args ?: ''
          ^^^^
  ```

- Warning: `subworkflows/local/align_star.nf:24:19`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_versions = Channel.empty()
                    ^^^^^^^
  ```

- Warning: `subworkflows/local/align_star.nf:30:25`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_orig_bam       = Channel.empty()
                          ^^^^^^^
  ```

- Warning: `subworkflows/local/align_star.nf:31:25`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_log_final      = Channel.empty()
                          ^^^^^^^
  ```

- Warning: `subworkflows/local/align_star.nf:32:25`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_log_out        = Channel.empty()
                          ^^^^^^^
  ```

- Warning: `subworkflows/local/align_star.nf:33:25`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_log_progress   = Channel.empty()
                          ^^^^^^^
  ```

- Warning: `subworkflows/local/align_star.nf:34:25`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_bam_sorted     = Channel.empty()
                          ^^^^^^^
  ```

- Warning: `subworkflows/local/align_star.nf:35:25`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_bam_transcript = Channel.empty()
                          ^^^^^^^
  ```

- Warning: `subworkflows/local/align_star.nf:36:25`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_fastq          = Channel.empty()
                          ^^^^^^^
  ```

- Warning: `subworkflows/local/align_star.nf:37:25`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_tab            = Channel.empty()
                          ^^^^^^^
  ```

- Warning: `subworkflows/local/dexseq_deu.nf:24:19`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_versions = Channel.empty()
                    ^^^^^^^
  ```

- Warning: `subworkflows/local/dexseq_deu.nf:61:48`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          DEXSEQ_COUNT.out.dexseq_clean_txt.map{ it[1] }.collect(),
                                                 ^^
  ```

- Warning: `subworkflows/local/dexseq_deu.nf:72:70`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
      dexseq_clean_txt        = DEXSEQ_COUNT.out.dexseq_clean_txt.map{ it[1] }.collect()
                                                                       ^^
  ```

- Warning: `subworkflows/local/drimseq_dexseq_dtu.nf:27:19`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_versions = Channel.empty()
                    ^^^^^^^
  ```

- Warning: `subworkflows/local/edger_deu.nf:21:19`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_versions = Channel.empty()
                    ^^^^^^^
  ```

- Warning: `subworkflows/local/edger_deu.nf:42:51`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          SUBREAD_FEATURECOUNTS.out.counts.collect({it[1]}),
                                                    ^^
  ```

- Warning: `subworkflows/local/leafcutter.nf:13:19`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_versions = Channel.empty()
                    ^^^^^^^
  ```

- Warning: `subworkflows/local/leafcutter.nf:18:16`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          .map { it[1] }
                 ^^
  ```

- Warning: `subworkflows/local/prepare_genome.nf:43:19`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_versions = Channel.empty()
                    ^^^^^^^
  ```

- Warning: `subworkflows/local/prepare_genome.nf:49:68`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          ch_fasta    = GUNZIP_FASTA ( [ [:], fasta ] ).gunzip.map { it[1] }
                                                                     ^^
  ```

- Warning: `subworkflows/local/prepare_genome.nf:52:20`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
          ch_fasta = Channel.value(file(fasta))
                     ^^^^^^^
  ```

- Warning: `subworkflows/local/prepare_genome.nf:60:68`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
              ch_gtf      = GUNZIP_GTF ( [ [:], gtf ] ).gunzip.map { it[1] }
                                                                     ^^
  ```

- Warning: `subworkflows/local/prepare_genome.nf:63:22`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
              ch_gtf = Channel.value(file(gtf))
                       ^^^^^^^
  ```

- Warning: `subworkflows/local/prepare_genome.nf:67:68`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
              ch_gff      = GUNZIP_GFF ( [ [:], gff ] ).gunzip.map { it[1] }
                                                                     ^^
  ```

- Warning: `subworkflows/local/prepare_genome.nf:70:22`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
              ch_gff = Channel.value(file(gff))
                       ^^^^^^^
  ```

- Warning: `subworkflows/local/prepare_genome.nf:82:102`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
              ch_transcript_fasta = GUNZIP_TRANSCRIPT_FASTA ( [ [:], transcript_fasta ] ).gunzip.map { it[1] }
                                                                                                       ^^
  ```

- Warning: `subworkflows/local/prepare_genome.nf:85:35`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
              ch_transcript_fasta = Channel.value(file(transcript_fasta))
                                    ^^^^^^^
  ```

- Warning: `subworkflows/local/prepare_genome.nf:102:50`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
      CUSTOM_GETCHROMSIZES ( ch_fasta.map { [ [:], it ] } )
                                                   ^^
  ```

- Warning: `subworkflows/local/prepare_genome.nf:103:57`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
      ch_fai         = CUSTOM_GETCHROMSIZES.out.fai.map { it[1] }
                                                          ^^
  ```

- Warning: `subworkflows/local/prepare_genome.nf:104:59`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
      ch_chrom_sizes = CUSTOM_GETCHROMSIZES.out.sizes.map { it[1] }
                                                            ^^
  ```

- Warning: `subworkflows/local/prepare_genome.nf:110:21`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_star_index = Channel.empty()
                      ^^^^^^^
  ```

- Warning: `subworkflows/local/prepare_genome.nf:114:86`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
                  ch_star_index = UNTAR_STAR_INDEX ( [ [:], star_index ] ).untar.map { it[1] }
                                                                                       ^^
  ```

- Warning: `subworkflows/local/prepare_genome.nf:117:33`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
                  ch_star_index = Channel.value(file(star_index))
                                  ^^^^^^^
  ```

- Warning: `subworkflows/local/prepare_genome.nf:133:23`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_salmon_index = Channel.empty()
                        ^^^^^^^
  ```

- Warning: `subworkflows/local/prepare_genome.nf:137:92`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
                  ch_salmon_index = UNTAR_SALMON_INDEX ( [ [:], salmon_index ] ).untar.map { it[1] }
                                                                                             ^^
  ```

- Warning: `subworkflows/local/prepare_genome.nf:140:35`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
                  ch_salmon_index = Channel.value(file(salmon_index))
                                    ^^^^^^^
  ```

- Warning: `subworkflows/local/prepare_genome.nf:153:21`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_dexseq_gff = Channel.empty()
                      ^^^^^^^
  ```

- Warning: `subworkflows/local/prepare_genome.nf:156:84`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
              ch_dexseq_gff = GUNZIP_GFF_DEXSEQ ( [ [:], gff_dexseq ] ).gunzip.map { it[1] }
                                                                                     ^^
  ```

- Warning: `subworkflows/local/prepare_genome.nf:159:29`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
              ch_dexseq_gff = Channel.value(file(gff_dexseq))
                              ^^^^^^^
  ```

- Warning: `subworkflows/local/prepare_genome.nf:166:20`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_suppa_tpm = Channel.empty()
                     ^^^^^^^
  ```

- Warning: `subworkflows/local/prepare_genome.nf:169:81`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
              ch_suppa_tpm = GUNZIP_SUPPA_TPM ( [ [:], suppa_tpm ] ).gunzip.map { it[1] }
                                                                                  ^^
  ```

- Warning: `subworkflows/local/prepare_genome.nf:172:28`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
              ch_suppa_tpm = Channel.value(file(suppa_tpm))
                             ^^^^^^^
  ```

- Warning: `subworkflows/local/rmats.nf:29:19`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_versions = Channel.empty()
                    ^^^^^^^
  ```

- Warning: `subworkflows/local/rmats.nf:57:39`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          ch_bam = ch_contrasts.map { [ it.contrast, it.treatment, it.bam1 ] }
                                        ^^
  ```

- Warning: `subworkflows/local/rmats.nf:57:52`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          ch_bam = ch_contrasts.map { [ it.contrast, it.treatment, it.bam1 ] }
                                                     ^^
  ```

- Warning: `subworkflows/local/rmats.nf:57:66`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          ch_bam = ch_contrasts.map { [ it.contrast, it.treatment, it.bam1 ] }
                                                                   ^^
  ```

- Warning: `subworkflows/local/rmats.nf:82:53`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          ch_contrasts_bamlist = ch_contrasts.map { [ it.contrast, it.treatment, it.meta1, it.bam1, it.bam1_text ] }
                                                      ^^
  ```

- Warning: `subworkflows/local/rmats.nf:82:66`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          ch_contrasts_bamlist = ch_contrasts.map { [ it.contrast, it.treatment, it.meta1, it.bam1, it.bam1_text ] }
                                                                   ^^
  ```

- Warning: `subworkflows/local/rmats.nf:82:80`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          ch_contrasts_bamlist = ch_contrasts.map { [ it.contrast, it.treatment, it.meta1, it.bam1, it.bam1_text ] }
                                                                                 ^^
  ```

- Warning: `subworkflows/local/rmats.nf:82:90`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          ch_contrasts_bamlist = ch_contrasts.map { [ it.contrast, it.treatment, it.meta1, it.bam1, it.bam1_text ] }
                                                                                           ^^
  ```

- Warning: `subworkflows/local/rmats.nf:82:99`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          ch_contrasts_bamlist = ch_contrasts.map { [ it.contrast, it.treatment, it.meta1, it.bam1, it.bam1_text ] }
                                                                                                    ^^
  ```

- Warning: `subworkflows/local/rmats.nf:113:53`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          ch_contrasts_bamlist = ch_contrasts.map { [ it.contrast, it.treatment, it.meta1, it.bam1, it.bam1_text, it.rmats_temp ] }
                                                      ^^
  ```

- Warning: `subworkflows/local/rmats.nf:113:66`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          ch_contrasts_bamlist = ch_contrasts.map { [ it.contrast, it.treatment, it.meta1, it.bam1, it.bam1_text, it.rmats_temp ] }
                                                                   ^^
  ```

- Warning: `subworkflows/local/rmats.nf:113:80`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          ch_contrasts_bamlist = ch_contrasts.map { [ it.contrast, it.treatment, it.meta1, it.bam1, it.bam1_text, it.rmats_temp ] }
                                                                                 ^^
  ```

- Warning: `subworkflows/local/rmats.nf:113:90`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          ch_contrasts_bamlist = ch_contrasts.map { [ it.contrast, it.treatment, it.meta1, it.bam1, it.bam1_text, it.rmats_temp ] }
                                                                                           ^^
  ```

- Warning: `subworkflows/local/rmats.nf:113:99`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          ch_contrasts_bamlist = ch_contrasts.map { [ it.contrast, it.treatment, it.meta1, it.bam1, it.bam1_text, it.rmats_temp ] }
                                                                                                    ^^
  ```

- Warning: `subworkflows/local/rmats.nf:113:113`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          ch_contrasts_bamlist = ch_contrasts.map { [ it.contrast, it.treatment, it.meta1, it.bam1, it.bam1_text, it.rmats_temp ] }
                                                                                                                  ^^
  ```

- Warning: `subworkflows/local/rmats.nf:143:39`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          ch_bam = ch_contrasts.map { [ it.contrast, it.treatment, it.control, it.bam1, it.bam2 ] }
                                        ^^
  ```

- Warning: `subworkflows/local/rmats.nf:143:52`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          ch_bam = ch_contrasts.map { [ it.contrast, it.treatment, it.control, it.bam1, it.bam2 ] }
                                                     ^^
  ```

- Warning: `subworkflows/local/rmats.nf:143:66`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          ch_bam = ch_contrasts.map { [ it.contrast, it.treatment, it.control, it.bam1, it.bam2 ] }
                                                                   ^^
  ```

- Warning: `subworkflows/local/rmats.nf:143:78`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          ch_bam = ch_contrasts.map { [ it.contrast, it.treatment, it.control, it.bam1, it.bam2 ] }
                                                                               ^^
  ```

- Warning: `subworkflows/local/rmats.nf:143:87`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          ch_bam = ch_contrasts.map { [ it.contrast, it.treatment, it.control, it.bam1, it.bam2 ] }
                                                                                        ^^
  ```

- Warning: `subworkflows/local/rmats.nf:168:53`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          ch_contrasts_bamlist = ch_contrasts.map { [ it.contrast, it.treatment, it.control, it.meta1, it.meta2, it.bam1, it.bam2, it.bam1_text, it.bam2_text ] }
                                                      ^^
  ```

- Warning: `subworkflows/local/rmats.nf:168:66`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          ch_contrasts_bamlist = ch_contrasts.map { [ it.contrast, it.treatment, it.control, it.meta1, it.meta2, it.bam1, it.bam2, it.bam1_text, it.bam2_text ] }
                                                                   ^^
  ```

- Warning: `subworkflows/local/rmats.nf:168:80`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          ch_contrasts_bamlist = ch_contrasts.map { [ it.contrast, it.treatment, it.control, it.meta1, it.meta2, it.bam1, it.bam2, it.bam1_text, it.bam2_text ] }
                                                                                 ^^
  ```

- Warning: `subworkflows/local/rmats.nf:168:92`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          ch_contrasts_bamlist = ch_contrasts.map { [ it.contrast, it.treatment, it.control, it.meta1, it.meta2, it.bam1, it.bam2, it.bam1_text, it.bam2_text ] }
                                                                                             ^^
  ```

- Warning: `subworkflows/local/rmats.nf:168:102`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          ch_contrasts_bamlist = ch_contrasts.map { [ it.contrast, it.treatment, it.control, it.meta1, it.meta2, it.bam1, it.bam2, it.bam1_text, it.bam2_text ] }
                                                                                                       ^^
  ```

- Warning: `subworkflows/local/rmats.nf:168:112`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          ch_contrasts_bamlist = ch_contrasts.map { [ it.contrast, it.treatment, it.control, it.meta1, it.meta2, it.bam1, it.bam2, it.bam1_text, it.bam2_text ] }
                                                                                                                 ^^
  ```

- Warning: `subworkflows/local/rmats.nf:168:121`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          ch_contrasts_bamlist = ch_contrasts.map { [ it.contrast, it.treatment, it.control, it.meta1, it.meta2, it.bam1, it.bam2, it.bam1_text, it.bam2_text ] }
                                                                                                                          ^^
  ```

- Warning: `subworkflows/local/rmats.nf:168:130`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          ch_contrasts_bamlist = ch_contrasts.map { [ it.contrast, it.treatment, it.control, it.meta1, it.meta2, it.bam1, it.bam2, it.bam1_text, it.bam2_text ] }
                                                                                                                                   ^^
  ```

- Warning: `subworkflows/local/rmats.nf:168:144`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          ch_contrasts_bamlist = ch_contrasts.map { [ it.contrast, it.treatment, it.control, it.meta1, it.meta2, it.bam1, it.bam2, it.bam1_text, it.bam2_text ] }
                                                                                                                                                 ^^
  ```

- Warning: `subworkflows/local/rmats.nf:199:53`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          ch_contrasts_bamlist = ch_contrasts.map { [ it.contrast, it.treatment, it.control, it.meta1, it.meta2, it.bam1, it.bam2, it.bam1_text, it.bam2_text, it.rmats_temp ] }
                                                      ^^
  ```

- Warning: `subworkflows/local/rmats.nf:199:66`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          ch_contrasts_bamlist = ch_contrasts.map { [ it.contrast, it.treatment, it.control, it.meta1, it.meta2, it.bam1, it.bam2, it.bam1_text, it.bam2_text, it.rmats_temp ] }
                                                                   ^^
  ```

- Warning: `subworkflows/local/rmats.nf:199:80`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          ch_contrasts_bamlist = ch_contrasts.map { [ it.contrast, it.treatment, it.control, it.meta1, it.meta2, it.bam1, it.bam2, it.bam1_text, it.bam2_text, it.rmats_temp ] }
                                                                                 ^^
  ```

- Warning: `subworkflows/local/rmats.nf:199:92`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          ch_contrasts_bamlist = ch_contrasts.map { [ it.contrast, it.treatment, it.control, it.meta1, it.meta2, it.bam1, it.bam2, it.bam1_text, it.bam2_text, it.rmats_temp ] }
                                                                                             ^^
  ```

- Warning: `subworkflows/local/rmats.nf:199:102`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          ch_contrasts_bamlist = ch_contrasts.map { [ it.contrast, it.treatment, it.control, it.meta1, it.meta2, it.bam1, it.bam2, it.bam1_text, it.bam2_text, it.rmats_temp ] }
                                                                                                       ^^
  ```

- Warning: `subworkflows/local/rmats.nf:199:112`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          ch_contrasts_bamlist = ch_contrasts.map { [ it.contrast, it.treatment, it.control, it.meta1, it.meta2, it.bam1, it.bam2, it.bam1_text, it.bam2_text, it.rmats_temp ] }
                                                                                                                 ^^
  ```

- Warning: `subworkflows/local/rmats.nf:199:121`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          ch_contrasts_bamlist = ch_contrasts.map { [ it.contrast, it.treatment, it.control, it.meta1, it.meta2, it.bam1, it.bam2, it.bam1_text, it.bam2_text, it.rmats_temp ] }
                                                                                                                          ^^
  ```

- Warning: `subworkflows/local/rmats.nf:199:130`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          ch_contrasts_bamlist = ch_contrasts.map { [ it.contrast, it.treatment, it.control, it.meta1, it.meta2, it.bam1, it.bam2, it.bam1_text, it.bam2_text, it.rmats_temp ] }
                                                                                                                                   ^^
  ```

- Warning: `subworkflows/local/rmats.nf:199:144`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          ch_contrasts_bamlist = ch_contrasts.map { [ it.contrast, it.treatment, it.control, it.meta1, it.meta2, it.bam1, it.bam2, it.bam1_text, it.bam2_text, it.rmats_temp ] }
                                                                                                                                                 ^^
  ```

- Warning: `subworkflows/local/rmats.nf:199:158`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          ch_contrasts_bamlist = ch_contrasts.map { [ it.contrast, it.treatment, it.control, it.meta1, it.meta2, it.bam1, it.bam2, it.bam1_text, it.bam2_text, it.rmats_temp ] }
                                                                                                                                                               ^^
  ```

- Warning: `subworkflows/local/suppa.nf:63:19`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_versions = Channel.empty()
                    ^^^^^^^
  ```

- Warning: `subworkflows/local/suppa.nf:84:33`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_ioe_events             = Channel.empty()
                                  ^^^^^^^
  ```

- Warning: `subworkflows/local/suppa.nf:85:33`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_suppa_local_psi        = Channel.empty()
                                  ^^^^^^^
  ```

- Warning: `subworkflows/local/suppa.nf:86:33`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_split_suppa_local_psi  = Channel.empty()
                                  ^^^^^^^
  ```

- Warning: `subworkflows/local/suppa.nf:88:33`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_dpsi_local             = Channel.empty()
                                  ^^^^^^^
  ```

- Warning: `subworkflows/local/suppa.nf:89:33`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_psivec_local           = Channel.empty()
                                  ^^^^^^^
  ```

- Warning: `subworkflows/local/suppa.nf:91:33`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_groups_ioe             = Channel.empty()
                                  ^^^^^^^
  ```

- Warning: `subworkflows/local/suppa.nf:92:33`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_cluster_vec_local      = Channel.empty()
                                  ^^^^^^^
  ```

- Warning: `subworkflows/local/suppa.nf:93:33`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_cluster_log_local      = Channel.empty()
                                  ^^^^^^^
  ```

- Warning: `subworkflows/local/suppa.nf:151:25`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
                  .map { [it.baseName, it ] }
                          ^^
  ```

- Warning: `subworkflows/local/suppa.nf:151:38`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
                  .map { [it.baseName, it ] }
                                       ^^
  ```

- Warning: `subworkflows/local/suppa.nf:167:26`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
                  .map { [ it.baseName.toString().replaceAll("local_", ""), it ] }
                           ^^
  ```

- Warning: `subworkflows/local/suppa.nf:167:75`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
                  .map { [ it.baseName.toString().replaceAll("local_", ""), it ] }
                                                                            ^^
  ```

- Warning: `subworkflows/local/suppa.nf:181:68`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
              ch_split_suppa_tpms = ch_suppa_local_contrasts.map { [ it.treatment, it.control, it.tpm1, it.tpm2 ] }
                                                                     ^^
  ```

- Warning: `subworkflows/local/suppa.nf:181:82`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
              ch_split_suppa_tpms = ch_suppa_local_contrasts.map { [ it.treatment, it.control, it.tpm1, it.tpm2 ] }
                                                                                   ^^
  ```

- Warning: `subworkflows/local/suppa.nf:181:94`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
              ch_split_suppa_tpms = ch_suppa_local_contrasts.map { [ it.treatment, it.control, it.tpm1, it.tpm2 ] }
                                                                                               ^^
  ```

- Warning: `subworkflows/local/suppa.nf:181:103`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
              ch_split_suppa_tpms = ch_suppa_local_contrasts.map { [ it.treatment, it.control, it.tpm1, it.tpm2 ] }
                                                                                                        ^^
  ```

- Warning: `subworkflows/local/suppa.nf:183:73`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
              ch_split_suppa_local_psi = ch_suppa_local_contrasts.map { [ it.treatment, it.control, it.psi1, it.psi2 ] }
                                                                          ^^
  ```

- Warning: `subworkflows/local/suppa.nf:183:87`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
              ch_split_suppa_local_psi = ch_suppa_local_contrasts.map { [ it.treatment, it.control, it.psi1, it.psi2 ] }
                                                                                        ^^
  ```

- Warning: `subworkflows/local/suppa.nf:183:99`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
              ch_split_suppa_local_psi = ch_suppa_local_contrasts.map { [ it.treatment, it.control, it.psi1, it.psi2 ] }
                                                                                                    ^^
  ```

- Warning: `subworkflows/local/suppa.nf:183:108`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
              ch_split_suppa_local_psi = ch_suppa_local_contrasts.map { [ it.treatment, it.control, it.psi1, it.psi2 ] }
                                                                                                             ^^
  ```

- Warning: `subworkflows/local/suppa.nf:245:34`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_ioi_events              = Channel.empty()
                                   ^^^^^^^
  ```

- Warning: `subworkflows/local/suppa.nf:246:34`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_suppa_isoform_psi       = Channel.empty()
                                   ^^^^^^^
  ```

- Warning: `subworkflows/local/suppa.nf:247:34`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_split_suppa_isoform_psi = Channel.empty()
                                   ^^^^^^^
  ```

- Warning: `subworkflows/local/suppa.nf:249:34`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_dpsi_isoform            = Channel.empty()
                                   ^^^^^^^
  ```

- Warning: `subworkflows/local/suppa.nf:250:34`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_psivec_isoform          = Channel.empty()
                                   ^^^^^^^
  ```

- Warning: `subworkflows/local/suppa.nf:252:34`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_groups_ioi              = Channel.empty()
                                   ^^^^^^^
  ```

- Warning: `subworkflows/local/suppa.nf:253:34`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_cluster_vec_isoform     = Channel.empty()
                                   ^^^^^^^
  ```

- Warning: `subworkflows/local/suppa.nf:254:34`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_cluster_log_isoform     = Channel.empty()
                                   ^^^^^^^
  ```

- Warning: `subworkflows/local/suppa.nf:311:25`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
                  .map { [it.baseName, it ] }
                          ^^
  ```

- Warning: `subworkflows/local/suppa.nf:311:38`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
                  .map { [it.baseName, it ] }
                                       ^^
  ```

- Warning: `subworkflows/local/suppa.nf:327:26`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
                  .map { [ it.baseName.toString().replaceAll("transcript_", ""), it ] }
                           ^^
  ```

- Warning: `subworkflows/local/suppa.nf:327:80`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
                  .map { [ it.baseName.toString().replaceAll("transcript_", ""), it ] }
                                                                                 ^^
  ```

- Warning: `subworkflows/local/suppa.nf:341:70`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
              ch_split_suppa_tpms = ch_suppa_isoform_contrasts.map { [ it.treatment, it.control, it.tpm1, it.tpm2 ] }
                                                                       ^^
  ```

- Warning: `subworkflows/local/suppa.nf:341:84`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
              ch_split_suppa_tpms = ch_suppa_isoform_contrasts.map { [ it.treatment, it.control, it.tpm1, it.tpm2 ] }
                                                                                     ^^
  ```

- Warning: `subworkflows/local/suppa.nf:341:96`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
              ch_split_suppa_tpms = ch_suppa_isoform_contrasts.map { [ it.treatment, it.control, it.tpm1, it.tpm2 ] }
                                                                                                 ^^
  ```

- Warning: `subworkflows/local/suppa.nf:341:105`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
              ch_split_suppa_tpms = ch_suppa_isoform_contrasts.map { [ it.treatment, it.control, it.tpm1, it.tpm2 ] }
                                                                                                          ^^
  ```

- Warning: `subworkflows/local/suppa.nf:343:77`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
              ch_split_suppa_isoform_psi = ch_suppa_isoform_contrasts.map { [ it.treatment, it.control, it.psi1, it.psi2 ] }
                                                                              ^^
  ```

- Warning: `subworkflows/local/suppa.nf:343:91`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
              ch_split_suppa_isoform_psi = ch_suppa_isoform_contrasts.map { [ it.treatment, it.control, it.psi1, it.psi2 ] }
                                                                                            ^^
  ```

- Warning: `subworkflows/local/suppa.nf:343:103`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
              ch_split_suppa_isoform_psi = ch_suppa_isoform_contrasts.map { [ it.treatment, it.control, it.psi1, it.psi2 ] }
                                                                                                        ^^
  ```

- Warning: `subworkflows/local/suppa.nf:343:112`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
              ch_split_suppa_isoform_psi = ch_suppa_isoform_contrasts.map { [ it.treatment, it.control, it.psi1, it.psi2 ] }
                                                                                                                 ^^
  ```

- Warning: `subworkflows/local/tx2gene_tximport.nf:18:19`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_versions = Channel.empty()
                    ^^^^^^^
  ```

- Warning: `subworkflows/local/tx2gene_tximport.nf:31:14`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          tar: it[0].tgz == true
               ^^
  ```

- Warning: `subworkflows/local/tx2gene_tximport.nf:32:14`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          dir: it[0].tgz == false
               ^^
  ```

- Warning: `subworkflows/local/tx2gene_tximport.nf:48:39`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
      TXIMPORT ( salmon_results.collect{it[1]}, tx2gene )
                                        ^^
  ```

- Warning: `subworkflows/local/utils_nfcore_rnasplice_pipeline/main.nf:31:5`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
      monochrome_logs   // boolean: Do not use coloured log outputs
      ^^^^^^^^^^^^^^^
  ```

- Warning: `subworkflows/local/utils_nfcore_rnasplice_pipeline/main.nf:37:19`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_versions = Channel.empty()
                    ^^^^^^^
  ```

- Warning: `subworkflows/local/utils_nfcore_rnasplice_pipeline/main.nf:71:5`: Variable was declared but not used

  ```nextflow
      versions    = ch_versions
      ^^^^^^^^
  ```

- Warning: `subworkflows/local/utils_nfcore_rnasplice_pipeline/main.nf:419:22`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          .map { meta, fastq -> meta.single_end }
                       ^^^^^
  ```

- Warning: `subworkflows/local/utils_nfcore_rnasplice_pipeline/main.nf:423:17`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
              if (it.size() > 1) {
                  ^^
  ```

- Warning: `subworkflows/local/utils_nfcore_rnasplice_pipeline/main.nf:434:22`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          .map { meta, fastq -> meta.strandedness }
                       ^^^^^
  ```

- Warning: `subworkflows/local/utils_nfcore_rnasplice_pipeline/main.nf:438:17`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
              if (it.size() > 1) {
                  ^^
  ```

- Warning: `subworkflows/local/visualise_miso.nf:27:19`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_versions = Channel.empty()
                    ^^^^^^^
  ```

- Warning: `subworkflows/local/visualise_miso.nf:71:38`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
      ch_bams = ch_genome_bam.collect({it[1]})
                                       ^^
  ```

- Warning: `subworkflows/local/visualise_miso.nf:72:41`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
      ch_miso_run = MISO_RUN.out.miso.map{it[1]}.collect()
                                          ^^
  ```

- Warning: `subworkflows/local/visualise_miso.nf:87:71`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
      def miso_genes_list = miso_genes ? miso_genes.split(',').collect{ it.trim() } : [""]
                                                                        ^^
  ```

- Warning: `subworkflows/local/visualise_miso.nf:88:26`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_miso_genes_list = Channel.fromList( miso_genes_list )
                           ^^^^^^^
  ```

- Warning: `subworkflows/local/visualise_miso.nf:91:30`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
          ch_miso_genes_file = Channel.fromPath(miso_genes_file)
                               ^^^^^^^
  ```

- Warning: `subworkflows/local/visualise_miso.nf:96:30`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
          ch_miso_genes_file = Channel.fromPath(miso_genes_file)
                               ^^^^^^^
  ```

- Warning: `subworkflows/local/visualise_miso.nf:105:17`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          .map { [it[1], it[2] ] }
                  ^^
  ```

- Warning: `subworkflows/local/visualise_miso.nf:105:24`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          .map { [it[1], it[2] ] }
                         ^^
  ```

- Warning: `subworkflows/nf-core/bam_sort_stats_samtools/main.nf:16:19`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_versions = Channel.empty()
                    ^^^^^^^
  ```

- Warning: `subworkflows/nf-core/bam_stats_samtools/main.nf:15:19`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_versions = Channel.empty()
                    ^^^^^^^
  ```

- Warning: `subworkflows/nf-core/bedgraph_bedclip_bedgraphtobigwig/main.nf:15:19`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_versions = Channel.empty()
                    ^^^^^^^
  ```

- Warning: `subworkflows/nf-core/fastq_fastqc_umitools_trimgalore/main.nf:35:19`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_versions = Channel.empty()
                    ^^^^^^^
  ```

- Warning: `subworkflows/nf-core/fastq_fastqc_umitools_trimgalore/main.nf:36:19`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      fastqc_html = Channel.empty()
                    ^^^^^^^
  ```

- Warning: `subworkflows/nf-core/fastq_fastqc_umitools_trimgalore/main.nf:37:19`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      fastqc_zip  = Channel.empty()
                    ^^^^^^^
  ```

- Warning: `subworkflows/nf-core/fastq_fastqc_umitools_trimgalore/main.nf:46:17`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      umi_log   = Channel.empty()
                  ^^^^^^^
  ```

- Warning: `subworkflows/nf-core/fastq_fastqc_umitools_trimgalore/main.nf:67:23`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      trim_unpaired   = Channel.empty()
                        ^^^^^^^
  ```

- Warning: `subworkflows/nf-core/fastq_fastqc_umitools_trimgalore/main.nf:68:23`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      trim_html       = Channel.empty()
                        ^^^^^^^
  ```

- Warning: `subworkflows/nf-core/fastq_fastqc_umitools_trimgalore/main.nf:69:23`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      trim_zip        = Channel.empty()
                        ^^^^^^^
  ```

- Warning: `subworkflows/nf-core/fastq_fastqc_umitools_trimgalore/main.nf:70:23`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      trim_log        = Channel.empty()
                        ^^^^^^^
  ```

- Warning: `subworkflows/nf-core/fastq_fastqc_umitools_trimgalore/main.nf:71:23`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      trim_read_count = Channel.empty()
                        ^^^^^^^
  ```

- Warning: `subworkflows/nf-core/fastq_fastqc_umitools_trimgalore/main.nf:99:23`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
              .filter { meta, reads, num_reads -> num_reads >= min_trimmed_reads.toFloat() }
                        ^^^^
  ```

- Warning: `subworkflows/nf-core/fastq_fastqc_umitools_trimgalore/main.nf:99:29`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
              .filter { meta, reads, num_reads -> num_reads >= min_trimmed_reads.toFloat() }
                              ^^^^^
  ```

- Warning: `subworkflows/nf-core/fastq_fastqc_umitools_trimgalore/main.nf:100:33`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
              .map { meta, reads, num_reads -> [ meta, reads ] }
                                  ^^^^^^^^^
  ```

- Warning: `subworkflows/nf-core/fastq_fastqc_umitools_trimgalore/main.nf:104:26`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
              .map { meta, reads, num_reads -> [ meta, num_reads ] }
                           ^^^^^
  ```

- Warning: `subworkflows/nf-core/utils_nextflow_pipeline/main.nf:94:33`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
      catch (NullPointerException e) {
                                  ^
  ```

- Warning: `subworkflows/nf-core/utils_nextflow_pipeline/main.nf:98:24`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
      catch (IOException e) {
                         ^
  ```

- Warning: `subworkflows/nf-core/utils_nfcore_pipeline/main.nf:116:98`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      return ch_versions.unique().map { version -> processVersionsFromYAML(version) }.unique().mix(Channel.of(workflowVersionToYAML()))
                                                                                                   ^^^^^^^
  ```

- Warning: `subworkflows/nf-core/utils_nfcore_pipeline/main.nf:264:22`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
      catch (Exception all) {
                       ^^^
  ```

- Warning: `subworkflows/nf-core/utils_nfcore_pipeline/main.nf:361:26`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          catch (Exception all) {
                           ^^^
  ```
