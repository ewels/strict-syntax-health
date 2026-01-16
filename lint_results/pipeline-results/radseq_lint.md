# Nextflow lint results

- Generated: 2026-01-16T10:26:39.790798200Z
- Nextflow version: 25.12.0-edge
- Summary: 45 errors, 42 warnings

## :x: Errors

- Error: `conf/base.config:13:16`: `check_max` is not defined

  ```nextflow
      cpus   = { check_max( 3    * task.attempt, 'cpus'   ) }
                 ^^^^^^^^^
  ```

- Error: `conf/base.config:14:16`: `check_max` is not defined

  ```nextflow
      memory = { check_max( 6.GB * task.attempt, 'memory' ) }
                 ^^^^^^^^^
  ```

- Error: `conf/base.config:15:16`: `check_max` is not defined

  ```nextflow
      time   = { check_max( 4.h  * task.attempt, 'time'   ) }
                 ^^^^^^^^^
  ```

- Error: `conf/base.config:29:20`: `check_max` is not defined

  ```nextflow
          cpus   = { check_max( 1                  , 'cpus'    ) }
                     ^^^^^^^^^
  ```

- Error: `conf/base.config:30:20`: `check_max` is not defined

  ```nextflow
          memory = { check_max( 15.GB * task.attempt, 'memory'  ) }
                     ^^^^^^^^^
  ```

- Error: `conf/base.config:31:20`: `check_max` is not defined

  ```nextflow
          time   = { check_max( 4.h  * task.attempt, 'time'    ) }
                     ^^^^^^^^^
  ```

- Error: `conf/base.config:34:20`: `check_max` is not defined

  ```nextflow
          cpus   = { check_max( 2     * task.attempt, 'cpus'    ) }
                     ^^^^^^^^^
  ```

- Error: `conf/base.config:35:20`: `check_max` is not defined

  ```nextflow
          memory = { check_max( 1.GB * task.attempt, 'memory'  ) }
                     ^^^^^^^^^
  ```

- Error: `conf/base.config:36:20`: `check_max` is not defined

  ```nextflow
          time   = { check_max( 4.h   * task.attempt, 'time'    ) }
                     ^^^^^^^^^
  ```

- Error: `conf/base.config:39:20`: `check_max` is not defined

  ```nextflow
          cpus   = { check_max( 5     * task.attempt, 'cpus'    ) }
                     ^^^^^^^^^
  ```

- Error: `conf/base.config:40:20`: `check_max` is not defined

  ```nextflow
          memory = { check_max( 5.GB * task.attempt, 'memory'  ) }
                     ^^^^^^^^^
  ```

- Error: `conf/base.config:41:20`: `check_max` is not defined

  ```nextflow
          time   = { check_max( 4.h   * task.attempt, 'time'    ) }
                     ^^^^^^^^^
  ```

- Error: `conf/base.config:44:20`: `check_max` is not defined

  ```nextflow
          cpus   = { check_max( 6     * task.attempt, 'cpus'    ) }
                     ^^^^^^^^^
  ```

- Error: `conf/base.config:45:20`: `check_max` is not defined

  ```nextflow
          memory = { check_max( 15.GB * task.attempt, 'memory'  ) }
                     ^^^^^^^^^
  ```

- Error: `conf/base.config:46:20`: `check_max` is not defined

  ```nextflow
          time   = { check_max( 8.h   * task.attempt, 'time'    ) }
                     ^^^^^^^^^
  ```

- Error: `conf/base.config:49:20`: `check_max` is not defined

  ```nextflow
          cpus   = { check_max( 12    * task.attempt, 'cpus'    ) }
                     ^^^^^^^^^
  ```

- Error: `conf/base.config:50:20`: `check_max` is not defined

  ```nextflow
          memory = { check_max( 55.GB * task.attempt, 'memory'  ) }
                     ^^^^^^^^^
  ```

- Error: `conf/base.config:51:20`: `check_max` is not defined

  ```nextflow
          time   = { check_max( 16.h  * task.attempt, 'time'    ) }
                     ^^^^^^^^^
  ```

- Error: `conf/base.config:54:20`: `check_max` is not defined

  ```nextflow
          cpus   = { check_max( 1    * task.attempt, 'cpus'    ) }
                     ^^^^^^^^^
  ```

- Error: `conf/base.config:55:20`: `check_max` is not defined

  ```nextflow
          memory = { check_max( 100.GB * task.attempt, 'memory'  ) }
                     ^^^^^^^^^
  ```

- Error: `conf/base.config:56:20`: `check_max` is not defined

  ```nextflow
          time   = { check_max( 16.h  * task.attempt, 'time'    ) }
                     ^^^^^^^^^
  ```

- Error: `conf/base.config:59:20`: `check_max` is not defined

  ```nextflow
          time   = { check_max( 20.h  * task.attempt, 'time'    ) }
                     ^^^^^^^^^
  ```

- Error: `conf/base.config:62:20`: `check_max` is not defined

  ```nextflow
          memory = { check_max( 200.GB * task.attempt, 'memory' ) }
                     ^^^^^^^^^
  ```

- Error: `conf/base.config:63:20`: `check_max` is not defined

  ```nextflow
          time   = { check_max( 8.h   * task.attempt, 'time'    ) }
                     ^^^^^^^^^
  ```

- Error: `main.nf:28:1`: Statements cannot be mixed with script declarations -- move statements into a process, workflow, or function

  ```nextflow
  WorkflowMain.initialise(workflow, params, log)
  ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  ```

- Error: `main.nf:28:1`: `WorkflowMain` is not defined

  ```nextflow
  WorkflowMain.initialise(workflow, params, log)
  ^^^^^^^^^^^^
  ```

- Error: `main.nf:36:1`: Module could not be parsed: '/home/runner/work/strict-syntax-health/strict-syntax-health/pipelines/radseq/workflows/radseq.nf'

  ```nextflow
  include { RADSEQ } from './workflows/radseq'
  ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  ```

- Error: `main.nf:42:5`: `RADSEQ` is not defined

  ```nextflow
      RADSEQ ()
      ^^^^^^
  ```

- Error: `modules/local/bcftools/main.nf:78:23`: `extension` is not defined

  ```nextflow
      touch ${prefix}.${extension}
                        ^^^^^^^^^
  ```

- Error: `modules/local/prepare_forward_reads.nf:91:86`: `assembled_fastq` is not defined

  ```nextflow
          awk 'BEGIN{P=1}{if(P==1||P==2){gsub(/^[@]/,">");print}; if(P==4)P=0; P++}' ${assembled_fastq} | \\
                                                                                       ^^^^^^^^^^^^^^^
  ```

- Error: `modules/local/rbmerge2fasta.nf:12:16`: `meta` is already declared

  ```nextflow
      tuple val (meta), path (rbmerge)
                 ^^^^
  ```

- Error: `modules/nf-core/bcftools/view/main.nf:57:23`: `extension` is not defined

  ```nextflow
      touch ${prefix}.${extension}
                        ^^^^^^^^^
  ```

- Error: `modules/nf-core/bwa/index/main.nf:14:27`: `bwa` is not defined

  ```nextflow
      tuple val(meta), path(bwa) , emit: index
                            ^^^
  ```

- Error: `modules/nf-core/fgbio/zipperbams/main.nf:12:15`: `meta` is already declared

  ```nextflow
      tuple val(meta), path(mapped_bam)
                ^^^^
  ```

- Error: `modules/nf-core/freebayes/main.nf:27:9`: `targets_file` is already declared

  ```nextflow
      def targets_file     = target_bed     ? "--target ${target_bed}"       : ""
          ^^^^^^^^^^^^
  ```

- Error: `nextflow.config:190:5`: Unexpected input: 'includeConfig'

  ```nextflow
      includeConfig "${params.custom_config_base}/nfcore_custom.config"
      ^
  ```

- Error: `subworkflows/local/bam_intervals_bedtools.nf:30:36`: `WorkflowRadseq` is not defined

  ```nextflow
      ch_bed_to_merge = ch_bed.map { WorkflowRadseq.groupMetaID(it) }.groupTuple() // [meta, bed]
                                     ^^^^^^^^^^^^^^
  ```

- Error: `subworkflows/local/bam_intervals_bedtools.nf:44:37`: `WorkflowRadseq` is not defined

  ```nextflow
          ch_cov_to_merge = cov.map { WorkflowRadseq.groupMetaID(it) }.groupTuple()
                                      ^^^^^^^^^^^^^^
  ```

- Error: `subworkflows/local/bam_intervals_bedtools.nf:69:41`: `WorkflowRadseq` is not defined

  ```nextflow
          ch_intervals = ch_fai_bed.map { WorkflowRadseq.splitBedFile(params, log, it) }.transpose()
                                          ^^^^^^^^^^^^^^
  ```

- Error: `subworkflows/nf-core/bam_dedup_stats_samtools_umitools/main.nf:43:5`: Incorrect number of call arguments, expected 1 but received 2

  ```nextflow
      BAM_STATS_SAMTOOLS ( ch_bam_bai, [] )
      ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  ```

- Error: `subworkflows/nf-core/fastq_create_umi_consensus_fgbio/main.nf:83:9`: Incorrect number of call arguments, expected 4 but received 5

  ```nextflow
          BWAMEM1_MEM_PRE ( BAM2FASTQ_PRE.out.fastq, bwaindex, true, params.sequence_type, read_lengths.collect() )
          ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  ```

- Error: `subworkflows/nf-core/fastq_create_umi_consensus_fgbio/main.nf:100:9`: Incorrect number of call arguments, expected 4 but received 5

  ```nextflow
          BWAMEM2_MEM_PRE ( BAM2FASTQ_PRE.out.fastq, bwaindex, true, params.sequence_type, read_lengths.collect() ) // reads, BWAMEM2_INDEX.out.index.first(), true, params.sequence_type, read_lengths.collect()
          ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  ```

- Error: `subworkflows/nf-core/fastq_create_umi_consensus_fgbio/main.nf:182:9`: Incorrect number of call arguments, expected 4 but received 5

  ```nextflow
          BWAMEM1_MEM_POST ( BAM2FASTQ_POST.out.fastq, bwaindex, false, params.sequence_type, read_lengths.collect() )
          ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  ```

- Error: `subworkflows/nf-core/fastq_create_umi_consensus_fgbio/main.nf:187:9`: Incorrect number of call arguments, expected 4 but received 5

  ```nextflow
          BWAMEM2_MEM_POST ( BAM2FASTQ_POST.out.fastq, bwaindex, false, params.sequence_type, read_lengths.collect() )
          ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  ```

- Error: `workflows/radseq.nf:92:26`: Unexpected input: '\n'

  ```nextflow
          case 'reference':
                           ^
  ```

## :warning: Warnings

- Warning: `modules/local/rbmerge2fasta.nf:11:16`: Variable was declared but not used

  ```nextflow
      tuple val (meta), path (rbdiv)
                 ^^^^
  ```

- Warning: `modules/nf-core/custom/dumpsoftwareversions/main.nf:22:9`: Variable was declared but not used

  ```nextflow
      def args = task.ext.args ?: ''
          ^^^^
  ```

- Warning: `modules/nf-core/fastqc/main.nf:27:48`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
      def renamed_files = old_new_pairs.collect{ old_name, new_name -> new_name }.join(' ')
                                                 ^^^^^^^^
  ```

- Warning: `modules/nf-core/fgbio/zipperbams/main.nf:11:15`: Variable was declared but not used

  ```nextflow
      tuple val(meta), path(unmapped_bam)
                ^^^^
  ```

- Warning: `modules/nf-core/fgbio/zipperbams/main.nf:25:9`: Variable was declared but not used

  ```nextflow
      def args2 = task.ext.args2 ?: ''
          ^^^^^
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

- Warning: `modules/nf-core/samtools/stats/main.nf:21:9`: Variable was declared but not used

  ```nextflow
      def args = task.ext.args ?: ''
          ^^^^
  ```

- Warning: `modules/nf-core/tabix/tabix/main.nf:33:9`: Variable was declared but not used

  ```nextflow
      def prefix = task.ext.prefix ?: "${meta.id}"
          ^^^^^^
  ```

- Warning: `subworkflows/local/bam_intervals_bedtools.nf:20:19`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_versions = Channel.empty()
                    ^^^^^^^
  ```

- Warning: `subworkflows/local/bam_intervals_bedtools.nf:30:63`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
      ch_bed_to_merge = ch_bed.map { WorkflowRadseq.groupMetaID(it) }.groupTuple() // [meta, bed]
                                                                ^^
  ```

- Warning: `subworkflows/local/bam_intervals_bedtools.nf:37:60`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          ch_sorted_mbed = BEDTOOLS_SORT (ch_mbed, faidx.map{it[1]}).sorted
                                                             ^^
  ```

- Warning: `subworkflows/local/bam_intervals_bedtools.nf:41:68`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          cov = BEDTOOLS_COVERAGE (ch_bed.combine(ch_sorted_mbed.map{it[1]}).map{meta,bed,mbed -> [meta,mbed,bed]}, faidx.map{it[1]}).bed
                                                                     ^^
  ```

- Warning: `subworkflows/local/bam_intervals_bedtools.nf:41:125`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          cov = BEDTOOLS_COVERAGE (ch_bed.combine(ch_sorted_mbed.map{it[1]}).map{meta,bed,mbed -> [meta,mbed,bed]}, faidx.map{it[1]}).bed
                                                                                                                              ^^
  ```

- Warning: `subworkflows/local/bam_intervals_bedtools.nf:44:64`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          ch_cov_to_merge = cov.map { WorkflowRadseq.groupMetaID(it) }.groupTuple()
                                                                 ^^
  ```

- Warning: `subworkflows/local/bam_intervals_bedtools.nf:47:66`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          ch_mcov = BEDTOOLS_MERGE_COV (ch_cov_to_merge, faidx.map{it[1]}).cov
                                                                   ^^
  ```

- Warning: `subworkflows/local/bam_intervals_bedtools.nf:69:82`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          ch_intervals = ch_fai_bed.map { WorkflowRadseq.splitBedFile(params, log, it) }.transpose()
                                                                                   ^^
  ```

- Warning: `subworkflows/local/fastq_unzip.nf:9:19`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_versions = Channel.empty()
                    ^^^^^^^
  ```

- Warning: `subworkflows/local/fastq_unzip.nf:15:23`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
          ch_fasta    = Channel.fromPath(fasta).map{[ [:], it ]}
                        ^^^^^^^
  ```

- Warning: `subworkflows/local/fastq_unzip.nf:15:58`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          ch_fasta    = Channel.fromPath(fasta).map{[ [:], it ]}
                                                           ^^
  ```

- Warning: `subworkflows/local/input_check.nf:15:38`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          .map { create_fastq_channels(it) }
                                       ^^
  ```

- Warning: `subworkflows/local/vcf_bcftools_radseq_filters.nf:15:19`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_versions = Channel.empty()
                    ^^^^^^^
  ```

- Warning: `subworkflows/local/vcf_bcftools_radseq_filters.nf:24:15`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_miss = Channel.fromList(params.fraction_missingness_list)
                ^^^^^^^
  ```

- Warning: `subworkflows/local/vcf_bcftools_radseq_filters.nf:25:14`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_mac = Channel.fromList(params.minor_allele_count_list)
               ^^^^^^^
  ```

- Warning: `subworkflows/nf-core/bam_dedup_stats_samtools_umitools/main.nf:16:19`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_versions = Channel.empty()
                    ^^^^^^^
  ```

- Warning: `subworkflows/nf-core/bam_stats_samtools/main.nf:14:19`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_versions = Channel.empty()
                    ^^^^^^^
  ```

- Warning: `subworkflows/nf-core/bam_stats_samtools/main.nf:19:56`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
      SAMTOOLS_FLAGSTAT ( bam_bai_fasta.map{meta,bam,bai,fasta-> [meta,bam,bai]} )
                                                         ^^^^^
  ```

- Warning: `subworkflows/nf-core/bam_stats_samtools/main.nf:22:56`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
      SAMTOOLS_IDXSTATS ( bam_bai_fasta.map{meta,bam,bai,fasta-> [meta,bam,bai]} )
                                                         ^^^^^
  ```

- Warning: `subworkflows/nf-core/fastq_create_umi_consensus_fgbio/main.nf:40:19`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_versions = Channel.empty()
                    ^^^^^^^
  ```

- Warning: `subworkflows/nf-core/fastq_create_umi_consensus_fgbio/main.nf:57:5`: Variable was declared but not used

  ```nextflow
      check_bam = FASTQTOBAM.out.bam.dump(tag: 'fastq_to_bam')
      ^^^^^^^^^
  ```

- Warning: `subworkflows/nf-core/fastq_create_umi_consensus_fgbio/main.nf:64:19`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      aligned_bam = Channel.empty()
                    ^^^^^^^
  ```

- Warning: `subworkflows/nf-core/fastq_create_umi_consensus_fgbio/main.nf:71:13`: Variable was declared but not used

  ```nextflow
              check_module_out = BWAMEM1_INDEX.out.index.dump(tag: 'index_out')
              ^^^^^^^^^^^^^^^^
  ```

- Warning: `subworkflows/nf-core/fastq_create_umi_consensus_fgbio/main.nf:75:48`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
          bwaindex    = fasta_meta ? bwa_index ? Channel.fromPath(bwa_index).collect().map{ it -> [[id:it[0].baseName], it] } : BWAMEM1_INDEX.out.index : []
                                                 ^^^^^^^
  ```

- Warning: `subworkflows/nf-core/fastq_create_umi_consensus_fgbio/main.nf:94:48`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
          bwaindex    = fasta_meta ? bwa_index ? Channel.fromPath(bwa_index).collect().map{ it -> [[id:it[0].baseName], it] } : BWAMEM2_INDEX.out.index : []
                                                 ^^^^^^^
  ```

- Warning: `subworkflows/nf-core/fastq_create_umi_consensus_fgbio/main.nf:107:65`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
      ZIPPERBAMS_PRE ( FASTQTOBAM.out.bam, aligned_bam, fasta.map{it[1]}, dict.map{it[1]} )
                                                                  ^^
  ```

- Warning: `subworkflows/nf-core/fastq_create_umi_consensus_fgbio/main.nf:107:82`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
      ZIPPERBAMS_PRE ( FASTQTOBAM.out.bam, aligned_bam, fasta.map{it[1]}, dict.map{it[1]} )
                                                                                   ^^
  ```

- Warning: `subworkflows/nf-core/fastq_create_umi_consensus_fgbio/main.nf:114:22`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      groupready_bam = Channel.empty()
                       ^^^^^^^
  ```

- Warning: `subworkflows/nf-core/fastq_create_umi_consensus_fgbio/main.nf:125:9`: Variable was declared but not used

  ```nextflow
          check_dummy_bam_bai = dummy_bam_bai.dump(tag: 'dummy_index')
          ^^^^^^^^^^^^^^^^^^^
  ```

- Warning: `subworkflows/nf-core/fastq_create_umi_consensus_fgbio/main.nf:151:21`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      consensus_bam = Channel.empty()
                      ^^^^^^^
  ```

- Warning: `subworkflows/nf-core/fastq_create_umi_consensus_fgbio/main.nf:172:48`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
      FILTERCONSENSUS ( consensus_bam, fasta.map{it[1]} )
                                                 ^^
  ```

- Warning: `subworkflows/nf-core/fastq_create_umi_consensus_fgbio/main.nf:194:66`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
      ZIPPERBAMS_POST ( consensus_bam, aligned_bam_post, fasta.map{it[1]}, dict.map{it[1]} )
                                                                   ^^
  ```

- Warning: `subworkflows/nf-core/fastq_create_umi_consensus_fgbio/main.nf:194:83`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
      ZIPPERBAMS_POST ( consensus_bam, aligned_bam_post, fasta.map{it[1]}, dict.map{it[1]} )
                                                                                    ^^
  ```
