# Nextflow lint results

- Generated: 2026-01-16T06:39:02.940261425Z
- Nextflow version: 25.12.0-edge
- Summary: 31 errors, 371 warnings

## :x: Errors

- Error: `conf/modules/variant_calling/mutect2.config:106:21`: Unexpected input: ':'

  ```nextflow
              withName: 'CALCULATECONTAMINATION' {
                      ^
  ```

- Error: `conf/modules/variant_calling/variant_calling.config:19:17`: Unexpected input: ':'

  ```nextflow
          withName: 'SAMTOOLS_BAMTOCRAM_VARIANTCALLING' {
                  ^
  ```

- Error: `subworkflows/local/prepare_intervals/main.nf:67:34`: Unexpected input: '='

  ```nextflow
                      final fields = line.split('\t')
                                   ^
  ```

- Error: `subworkflows/local/prepare_reference_and_intervals/main.nf:5:1`: Module could not be parsed: '/home/runner/work/strict-syntax-health/strict-syntax-health/pipelines/rnadnavar/subworkflows/local/prepare_intervals/main.nf'

  ```nextflow
  include { PREPARE_INTERVALS                                    } from './../prepare_intervals/main'
  ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  ```

- Error: `subworkflows/local/prepare_reference_and_intervals/main.nf:55:5`: `PREPARE_INTERVALS` is not defined

  ```nextflow
      PREPARE_INTERVALS(fasta_fai, params.intervals, params.no_intervals)
      ^^^^^^^^^^^^^^^^^
  ```

- Error: `subworkflows/local/prepare_reference_and_intervals/main.nf:56:29`: `PREPARE_INTERVALS` is not defined

  ```nextflow
      versions = versions.mix(PREPARE_INTERVALS.out.versions)
                              ^^^^^^^^^^^^^^^^^
  ```

- Error: `subworkflows/local/prepare_reference_and_intervals/main.nf:70:37`: `PREPARE_INTERVALS` is not defined

  ```nextflow
      intervals                     = PREPARE_INTERVALS.out.intervals_bed
                                      ^^^^^^^^^^^^^^^^^
  ```

- Error: `subworkflows/local/prepare_reference_and_intervals/main.nf:71:37`: `PREPARE_INTERVALS` is not defined

  ```nextflow
      intervals_bed_gz_tbi          = PREPARE_INTERVALS.out.intervals_bed_gz_tbi
                                      ^^^^^^^^^^^^^^^^^
  ```

- Error: `subworkflows/local/prepare_reference_and_intervals/main.nf:72:37`: `PREPARE_INTERVALS` is not defined

  ```nextflow
      intervals_for_preprocessing   = PREPARE_INTERVALS.out.intervals_for_preprocessing
                                      ^^^^^^^^^^^^^^^^^
  ```

- Error: `subworkflows/local/prepare_reference_and_intervals/main.nf:73:37`: `PREPARE_INTERVALS` is not defined

  ```nextflow
      intervals_bed_combined        = PREPARE_INTERVALS.out.intervals_bed_combined
                                      ^^^^^^^^^^^^^^^^^
  ```

- Error: `subworkflows/local/prepare_reference_and_intervals/main.nf:74:37`: `PREPARE_INTERVALS` is not defined

  ```nextflow
      intervals_bed_gz_tbi_combined = PREPARE_INTERVALS.out.intervals_bed_gz_tbi_combined
                                      ^^^^^^^^^^^^^^^^^
  ```

- Error: `subworkflows/local/samplesheet_to_channel/main.nf:26:14`: Variables in a closure should be declared with `def`

  ```nextflow
              (meta, fastq_1, fastq_2, table, cram, crai, bam, bai, vcf, variantcaller, maf) = ch_items
               ^^^^
  ```

- Error: `subworkflows/local/samplesheet_to_channel/main.nf:26:20`: Variables in a closure should be declared with `def`

  ```nextflow
              (meta, fastq_1, fastq_2, table, cram, crai, bam, bai, vcf, variantcaller, maf) = ch_items
                     ^^^^^^^
  ```

- Error: `subworkflows/local/samplesheet_to_channel/main.nf:26:29`: Variables in a closure should be declared with `def`

  ```nextflow
              (meta, fastq_1, fastq_2, table, cram, crai, bam, bai, vcf, variantcaller, maf) = ch_items
                              ^^^^^^^
  ```

- Error: `subworkflows/local/samplesheet_to_channel/main.nf:26:38`: Variables in a closure should be declared with `def`

  ```nextflow
              (meta, fastq_1, fastq_2, table, cram, crai, bam, bai, vcf, variantcaller, maf) = ch_items
                                       ^^^^^
  ```

- Error: `subworkflows/local/samplesheet_to_channel/main.nf:26:45`: Variables in a closure should be declared with `def`

  ```nextflow
              (meta, fastq_1, fastq_2, table, cram, crai, bam, bai, vcf, variantcaller, maf) = ch_items
                                              ^^^^
  ```

- Error: `subworkflows/local/samplesheet_to_channel/main.nf:26:51`: Variables in a closure should be declared with `def`

  ```nextflow
              (meta, fastq_1, fastq_2, table, cram, crai, bam, bai, vcf, variantcaller, maf) = ch_items
                                                    ^^^^
  ```

- Error: `subworkflows/local/samplesheet_to_channel/main.nf:26:57`: Variables in a closure should be declared with `def`

  ```nextflow
              (meta, fastq_1, fastq_2, table, cram, crai, bam, bai, vcf, variantcaller, maf) = ch_items
                                                          ^^^
  ```

- Error: `subworkflows/local/samplesheet_to_channel/main.nf:26:62`: Variables in a closure should be declared with `def`

  ```nextflow
              (meta, fastq_1, fastq_2, table, cram, crai, bam, bai, vcf, variantcaller, maf) = ch_items
                                                               ^^^
  ```

- Error: `subworkflows/local/samplesheet_to_channel/main.nf:26:67`: Variables in a closure should be declared with `def`

  ```nextflow
              (meta, fastq_1, fastq_2, table, cram, crai, bam, bai, vcf, variantcaller, maf) = ch_items
                                                                    ^^^
  ```

- Error: `subworkflows/local/samplesheet_to_channel/main.nf:26:72`: Variables in a closure should be declared with `def`

  ```nextflow
              (meta, fastq_1, fastq_2, table, cram, crai, bam, bai, vcf, variantcaller, maf) = ch_items
                                                                         ^^^^^^^^^^^^^
  ```

- Error: `subworkflows/local/samplesheet_to_channel/main.nf:26:87`: Variables in a closure should be declared with `def`

  ```nextflow
              (meta, fastq_1, fastq_2, table, cram, crai, bam, bai, vcf, variantcaller, maf) = ch_items
                                                                                        ^^^
  ```

- Error: `tests/config/test_data.config:5:5`: Unexpected input: 'includeConfig'

  ```nextflow
      includeConfig "https://raw.githubusercontent.com/nf-core/modules/master/tests/config/test_data.config"
      ^
  ```

- Error: `workflows/rnadnavar/main.nf:26:1`: Module could not be parsed: '/home/runner/work/strict-syntax-health/strict-syntax-health/pipelines/rnadnavar/subworkflows/local/prepare_intervals/main.nf'

  ```nextflow
  include { PREPARE_INTERVALS as PREPARE_INTERVALS_FOR_REALIGNMENT    } from '../../subworkflows/local/prepare_intervals'
  ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  ```

- Error: `workflows/rnadnavar/main.nf:191:9`: `PREPARE_INTERVALS_FOR_REALIGNMENT` is not defined

  ```nextflow
          PREPARE_INTERVALS_FOR_REALIGNMENT(fasta_fai, null, true)
          ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  ```

- Error: `workflows/rnadnavar/main.nf:223:13`: `PREPARE_INTERVALS_FOR_REALIGNMENT` is not defined

  ```nextflow
              PREPARE_INTERVALS_FOR_REALIGNMENT.out.intervals_bed,
              ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  ```

- Error: `workflows/rnadnavar/main.nf:224:13`: `PREPARE_INTERVALS_FOR_REALIGNMENT` is not defined

  ```nextflow
              PREPARE_INTERVALS_FOR_REALIGNMENT.out.intervals_for_preprocessing,
              ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  ```

- Error: `workflows/rnadnavar/main.nf:225:13`: `PREPARE_INTERVALS_FOR_REALIGNMENT` is not defined

  ```nextflow
              PREPARE_INTERVALS_FOR_REALIGNMENT.out.intervals_bed_gz_tbi,
              ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  ```

- Error: `workflows/rnadnavar/main.nf:226:13`: `PREPARE_INTERVALS_FOR_REALIGNMENT` is not defined

  ```nextflow
              PREPARE_INTERVALS_FOR_REALIGNMENT.out.intervals_bed_combined,
              ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  ```

- Error: `workflows/rnadnavar/main.nf:227:13`: `PREPARE_INTERVALS_FOR_REALIGNMENT` is not defined

  ```nextflow
              PREPARE_INTERVALS_FOR_REALIGNMENT.out.intervals_and_num_intervals,
              ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  ```

- Error: `workflows/rnadnavar/main.nf:228:13`: `PREPARE_INTERVALS_FOR_REALIGNMENT` is not defined

  ```nextflow
              PREPARE_INTERVALS_FOR_REALIGNMENT.out.intervals_bed_gz_tbi_combined,
              ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  ```

## :warning: Warnings

- Warning: `conf/modules/alignment/bam_align.config:48:46`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
                      ) { "mapped/${meta.id}/${it}" }
                                               ^^
  ```

- Warning: `conf/modules/alignment/bam_align.config:67:174`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          saveAs: { (params.save_output_as_bam && (params.save_mapped || params.skip_tools && params.skip_tools.split(',').contains('markduplicates'))) ? "mapped/${meta.id}/${it}" : null }
                                                                                                                                                                               ^^
  ```

- Warning: `conf/modules/alignment/bam_align.config:172:209`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
                  saveAs: { (params.save_bam_mapped || (params.skip_tools && params.skip_tools.split(',').contains('markduplicates'))) && (meta.size * meta.numLanes == 1) ? "mapped/${meta.patient}/${meta.id}/${it}" : null }
                                                                                                                                                                                                                  ^^
  ```

- Warning: `conf/modules/alignment/bam_align.config:184:209`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
                  saveAs: { (params.save_bam_mapped || (params.skip_tools && params.skip_tools.split(',').contains('markduplicates'))) && (meta.size * meta.numLanes == 1) ? "mapped/${meta.patient}/${meta.id}/${it}" : null }
                                                                                                                                                                                                                  ^^
  ```

- Warning: `conf/modules/gatk4_preprocessing/markduplicates.config:64:145`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
                  saveAs: { !(params.skip_tools && params.skip_tools.split(',').contains('markduplicates_report')) ? "markduplicates/${meta.id}/${it}" : null}
                                                                                                                                                  ^^
  ```

- Warning: `conf/modules/gatk4_preprocessing/prepare_recalibration.config:25:81`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
              saveAs: { meta.num_intervals > 1 ? null : "recal_table/${meta.id}/${it}" }
                                                                                  ^^
  ```

- Warning: `conf/modules/gatk4_preprocessing/recalibrate.config:25:82`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
              saveAs: { meta.num_intervals > 1 ? null : "recalibrated/${meta.id}/${it}" }
                                                                                   ^^
  ```

- Warning: `conf/modules/gatk4_preprocessing/splitncigarreads.config:46:102`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
                          saveAs: { params.save_bam_mapped ? "realignment/${meta.patient}/${meta.id}/${it}" : null },
                                                                                                       ^^
  ```

- Warning: `conf/modules/variant_calling/strelka.config:27:77`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
              saveAs: { meta.num_intervals > 1 ? null : "strelka/${meta.id}/${it}" },
                                                                              ^^
  ```

- Warning: `main.nf:60:5`: Variable was declared but not used

  ```nextflow
      versions = Channel.empty()
      ^^^^^^^^
  ```

- Warning: `main.nf:60:16`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      versions = Channel.empty()
                 ^^^^^^^
  ```

- Warning: `modules/local/maf2bed/main.nf:21:9`: Variable was declared but not used

  ```nextflow
      def args = task.ext.args ?: ''
          ^^^^
  ```

- Warning: `modules/local/merge_maf/main.nf:22:9`: Variable was declared but not used

  ```nextflow
      def args = task.ext.args ?: ''
          ^^^^
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

- Warning: `modules/nf-core/gatk4/baserecalibrator/main.nf:29:60`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
      def sites_command = known_sites.collect{"--known-sites $it"}.join(' ')
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

- Warning: `modules/nf-core/gatk4/learnreadorientationmodel/main.nf:23:48`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
      def input_list = f1r2.collect { "--input ${it}" }.join(' ')
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

- Warning: `modules/nf-core/gffread/main.nf:26:103`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
      def extension   = args.contains("-T")       ? 'gtf' : ( ( ['-w', '-x', '-y' ].any { args.contains(it) } ) ? 'fasta' : 'gff3' )
                                                                                                        ^^
  ```

- Warning: `modules/nf-core/gffread/main.nf:30:61`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
      def args_sorted = args.replaceAll(/(.*)(-[wxy])(.*)/) { all, pre, param, post -> "$pre $post $param" }.trim()
                                                              ^^^
  ```

- Warning: `modules/nf-core/gffread/main.nf:49:103`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
      def extension   = args.contains("-T")       ? 'gtf' : ( ( ['-w', '-x', '-y' ].any { args.contains(it) } ) ? 'fasta' : 'gff3' )
                                                                                                        ^^
  ```

- Warning: `modules/nf-core/gunzip/main.nf:43:9`: Variable was declared but not used

  ```nextflow
      def args = task.ext.args ?: ''
          ^^^^
  ```

- Warning: `modules/nf-core/hisat2/extractsplicesites/main.nf:21:9`: Variable was declared but not used

  ```nextflow
      def args = task.ext.args ?: ''
          ^^^^
  ```

- Warning: `modules/nf-core/star/align/main.nf:46:56`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
      meta.single_end ? [reads].flatten().each{reads1 << it} : reads.eachWithIndex{ v, ix -> ( ix & 1 ? reads2 : reads1) << v }
                                                         ^^
  ```

- Warning: `modules/nf-core/unzip/main.nf:38:9`: Variable was declared but not used

  ```nextflow
      def args = task.ext.args ?: ''
          ^^^^
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

- Warning: `modules/nf-core/vt/normalize/main.nf:53:9`: Variable was declared but not used

  ```nextflow
      def args = task.ext.args ?: ''
          ^^^^
  ```

- Warning: `subworkflows/local/annotation_cache_initialisation/main.nf:35:28`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
          ensemblvep_cache = Channel.fromPath(file("${vep_cache}/${vep_annotation_cache_key}"), checkIfExists: true).collect()
                             ^^^^^^^
  ```

- Warning: `subworkflows/local/bam_align/main.nf:36:17`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      reports   = Channel.empty()
                  ^^^^^^^
  ```

- Warning: `subworkflows/local/bam_align/main.nf:37:17`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      versions  = Channel.empty()
                  ^^^^^^^
  ```

- Warning: `subworkflows/local/bam_align/main.nf:40:24`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      bam_mapped_rna   = Channel.empty()
                         ^^^^^^^
  ```

- Warning: `subworkflows/local/bam_align/main.nf:41:24`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      bam_mapped_dna   = Channel.empty()
                         ^^^^^^^
  ```

- Warning: `subworkflows/local/bam_align/main.nf:42:24`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      bam_mapped       = Channel.empty()
                         ^^^^^^^
  ```

- Warning: `subworkflows/local/bam_align/main.nf:43:24`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      cram_mapped      = Channel.empty()
                         ^^^^^^^
  ```

- Warning: `subworkflows/local/bam_align/main.nf:54:20`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
              bam:   it[0].data_type == "bam"
                     ^^
  ```

- Warning: `subworkflows/local/bam_align/main.nf:55:20`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
              fastq: it[0].data_type == "fastq"
                     ^^
  ```

- Warning: `subworkflows/local/bam_align/main.nf:74:59`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
              reports = reports.mix(FASTQC.out.zip.collect{ meta, logs -> logs })
                                                            ^^^^
  ```

- Warning: `subworkflows/local/bam_align/main.nf:129:22`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
                  dna: it[0].status < 2
                       ^^
  ```

- Warning: `subworkflows/local/bam_align/main.nf:130:22`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
                  rna: it[0].status == 2
                       ^^
  ```

- Warning: `subworkflows/local/bam_align/main.nf:189:76`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          reports           = reports.mix(FASTQ_ALIGN_STAR.out.stats.collect{it[1]}.ifEmpty([]))
                                                                             ^^
  ```

- Warning: `subworkflows/local/bam_align/main.nf:190:80`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          reports           = reports.mix(FASTQ_ALIGN_STAR.out.log_final.collect{it[1]}.ifEmpty([]))
                                                                                 ^^
  ```

- Warning: `subworkflows/local/bam_applybqsr/main.nf:19:16`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      versions = Channel.empty()
                 ^^^^^^^
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

- Warning: `subworkflows/local/bam_convert_samtools/main.nf:22:16`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      versions = Channel.empty()
                 ^^^^^^^
  ```

- Warning: `subworkflows/local/bam_gatk_preprocessing/main.nf:39:17`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      reports   = Channel.empty()
                  ^^^^^^^
  ```

- Warning: `subworkflows/local/bam_gatk_preprocessing/main.nf:40:17`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      versions  = Channel.empty()
                  ^^^^^^^
  ```

- Warning: `subworkflows/local/bam_gatk_preprocessing/main.nf:41:28`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      cram_variant_calling = Channel.empty()
                             ^^^^^^^
  ```

- Warning: `subworkflows/local/bam_gatk_preprocessing/main.nf:45:40`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
          cram_markduplicates_no_spark = Channel.empty()
                                         ^^^^^^^
  ```

- Warning: `subworkflows/local/bam_gatk_preprocessing/main.nf:55:121`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          cram_for_markduplicates = params.step == 'mapping' || realignment ? bam_mapped : input_sample.map{ meta, input, index -> [ meta, input ] }
                                                                                                                          ^^^^^
  ```

- Warning: `subworkflows/local/bam_gatk_preprocessing/main.nf:59:36`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
          cram_skip_markduplicates = Channel.empty()
                                     ^^^^^^^
  ```

- Warning: `subworkflows/local/bam_gatk_preprocessing/main.nf:68:27`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
                      bam:  it[0].data_type == "bam"
                            ^^
  ```

- Warning: `subworkflows/local/bam_gatk_preprocessing/main.nf:69:27`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
                      cram: it[0].data_type == "cram"
                            ^^
  ```

- Warning: `subworkflows/local/bam_gatk_preprocessing/main.nf:73:73`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
                  BAM_TO_CRAM(input_markduplicates_convert.bam, fasta.map{meta, fa -> [fa]}, fasta_fai)
                                                                          ^^^^
  ```

- Warning: `subworkflows/local/bam_gatk_preprocessing/main.nf:76:44`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
                  cram_skip_markduplicates = Channel.empty().mix(input_markduplicates_convert.cram, BAM_TO_CRAM.out.cram)
                                             ^^^^^^^
  ```

- Warning: `subworkflows/local/bam_gatk_preprocessing/main.nf:82:70`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
              reports = reports.mix(CRAM_QC_NO_MD.out.reports.collect{ meta, report -> report })
                                                                       ^^^^
  ```

- Warning: `subworkflows/local/bam_gatk_preprocessing/main.nf:100:75`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
              reports = reports.mix(BAM_MARKDUPLICATES.out.reports.collect{ meta, report -> report })
                                                                            ^^^^
  ```

- Warning: `subworkflows/local/bam_gatk_preprocessing/main.nf:107:34`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
          ch_md_cram_for_restart = Channel.empty().mix(cram_markduplicates_no_spark)
                                   ^^^^^^^
  ```

- Warning: `subworkflows/local/bam_gatk_preprocessing/main.nf:123:36`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
          ch_md_cram_for_restart   = Channel.empty().mix(input_sample)
                                     ^^^^^^^
  ```

- Warning: `subworkflows/local/bam_gatk_preprocessing/main.nf:124:36`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
          cram_skip_markduplicates = Channel.empty().mix(input_sample)
                                     ^^^^^^^
  ```

- Warning: `subworkflows/local/bam_gatk_preprocessing/main.nf:134:27`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
                      bam:  it[0].data_type == "bam"
                            ^^
  ```

- Warning: `subworkflows/local/bam_gatk_preprocessing/main.nf:135:27`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
                      cram: it[0].data_type == "cram"
                            ^^
  ```

- Warning: `subworkflows/local/bam_gatk_preprocessing/main.nf:138:83`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
                  input_sncr_convert  = input_sncr_convert.bam.map{ meta, bam, bai, table -> [ meta, bam, bai ] }
                                                                                    ^^^^^
  ```

- Warning: `subworkflows/local/bam_gatk_preprocessing/main.nf:147:41`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
                  cram_skip_splitncigar = Channel.empty().mix(sncr_cram_from_bam, input_sncr_convert.cram)
                                          ^^^^^^^
  ```

- Warning: `subworkflows/local/bam_gatk_preprocessing/main.nf:157:37`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
          cram_splitncigar_no_spark = Channel.empty()
                                      ^^^^^^^
  ```

- Warning: `subworkflows/local/bam_gatk_preprocessing/main.nf:161:55`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
                                                  dna:  it[0].status < 2
                                                        ^^
  ```

- Warning: `subworkflows/local/bam_gatk_preprocessing/main.nf:162:55`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
                                                  rna:  it[0].status >= 2
                                                        ^^
  ```

- Warning: `subworkflows/local/bam_gatk_preprocessing/main.nf:177:37`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
              cram_skip_splitncigar = Channel.empty()
                                      ^^^^^^^
  ```

- Warning: `subworkflows/local/bam_gatk_preprocessing/main.nf:181:36`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
          ch_sncr_cram_for_restart = Channel.empty().mix(cram_splitncigar_no_spark).mix(cram_skip_splitncigar)
                                     ^^^^^^^
  ```

- Warning: `subworkflows/local/bam_gatk_preprocessing/main.nf:185:36`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
          ch_sncr_cram_for_restart = Channel.empty()
                                     ^^^^^^^
  ```

- Warning: `subworkflows/local/bam_gatk_preprocessing/main.nf:197:22`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
                  bam: it[0].data_type == "bam"
                       ^^
  ```

- Warning: `subworkflows/local/bam_gatk_preprocessing/main.nf:198:23`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
                  cram: it[0].data_type == "cram"
                        ^^
  ```

- Warning: `subworkflows/local/bam_gatk_preprocessing/main.nf:209:48`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
              ch_cram_for_bam_baserecalibrator = Channel.empty().mix(ch_cram_for_bam_baserecalibrator, input_prepare_recal_convert.cram)
                                                 ^^^^^^^
  ```

- Warning: `subworkflows/local/bam_gatk_preprocessing/main.nf:220:48`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
              ch_cram_for_bam_baserecalibrator = Channel.empty().mix(ch_sncr_cram_for_restart, cram_skip_splitncigar )
                                                 ^^^^^^^
  ```

- Warning: `subworkflows/local/bam_gatk_preprocessing/main.nf:228:38`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
              ch_table_bqsr_no_spark = Channel.empty()
                                       ^^^^^^^
  ```

- Warning: `subworkflows/local/bam_gatk_preprocessing/main.nf:247:29`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
              ch_table_bqsr = Channel.empty().mix(
                              ^^^^^^^
  ```

- Warning: `subworkflows/local/bam_gatk_preprocessing/main.nf:250:58`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
              reports = reports.mix(ch_table_bqsr.collect{ meta, table -> table })
                                                           ^^^^
  ```

- Warning: `subworkflows/local/bam_gatk_preprocessing/main.nf:269:23`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
                  bam:  it[0].data_type == "bam"
                        ^^
  ```

- Warning: `subworkflows/local/bam_gatk_preprocessing/main.nf:270:23`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
                  cram: it[0].data_type == "cram"
                        ^^
  ```

- Warning: `subworkflows/local/bam_gatk_preprocessing/main.nf:274:67`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
              input_only_table = input_recal_convert.bam.map{ meta, bam, bai, table -> [ meta, table ] }
                                                                    ^^^
  ```

- Warning: `subworkflows/local/bam_gatk_preprocessing/main.nf:274:72`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
              input_only_table = input_recal_convert.bam.map{ meta, bam, bai, table -> [ meta, table ] }
                                                                         ^^^
  ```

- Warning: `subworkflows/local/bam_gatk_preprocessing/main.nf:275:77`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
              input_only_bam   = input_recal_convert.bam.map{ meta, bam, bai, table -> [ meta, bam, bai ] }
                                                                              ^^^^^
  ```

- Warning: `subworkflows/local/bam_gatk_preprocessing/main.nf:281:30`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
              cram_applybqsr = Channel.empty().mix(
                               ^^^^^^^
  ```

- Warning: `subworkflows/local/bam_gatk_preprocessing/main.nf:289:45`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
              cram_variant_calling_no_spark = Channel.empty()
                                              ^^^^^^^
  ```

- Warning: `subworkflows/local/bam_gatk_preprocessing/main.nf:304:36`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
              cram_variant_calling = Channel.empty().mix(
                                     ^^^^^^^
  ```

- Warning: `subworkflows/local/bam_gatk_preprocessing/main.nf:313:70`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
              reports = reports.mix(CRAM_QC_RECAL.out.reports.collect{ meta, report -> report })
                                                                       ^^^^
  ```

- Warning: `subworkflows/local/bam_gatk_preprocessing/main.nf:325:33`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
              csv_recalibration = Channel.empty()
                                  ^^^^^^^
  ```

- Warning: `subworkflows/local/bam_gatk_preprocessing/main.nf:336:36`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
              cram_variant_calling = Channel.empty().mix(
                                     ^^^^^^^
  ```

- Warning: `subworkflows/local/bam_gatk_preprocessing/main.nf:338:65`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
                  input_recal_convert.cram.map{ meta, cram, crai, table -> [ meta, cram, crai ] })
                                                                  ^^^^^
  ```

- Warning: `subworkflows/local/bam_gatk_preprocessing/main.nf:342:36`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
              cram_variant_calling = Channel.empty().mix(ch_cram_for_bam_baserecalibrator)
                                     ^^^^^^^
  ```

- Warning: `subworkflows/local/bam_gatk_preprocessing/main.nf:351:19`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
              bam:  it[0].data_type == "bam"
                    ^^
  ```

- Warning: `subworkflows/local/bam_gatk_preprocessing/main.nf:352:19`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
              cram: it[0].data_type == "cram"
                    ^^
  ```

- Warning: `subworkflows/local/bam_gatk_preprocessing/main.nf:361:32`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
          cram_variant_calling = Channel.empty().mix(converted, input_variant_calling_convert.cram)
                                 ^^^^^^^
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

- Warning: `subworkflows/local/bam_merge_index_samtools/main.nf:15:16`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      versions = Channel.empty()
                 ^^^^^^^
  ```

- Warning: `subworkflows/local/bam_splitncigarreads/main.nf:19:16`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      versions = Channel.empty()
                 ^^^^^^^
  ```

- Warning: `subworkflows/local/bam_variant_calling/main.nf:36:17`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      reports   = Channel.empty()
                  ^^^^^^^
  ```

- Warning: `subworkflows/local/bam_variant_calling/main.nf:37:17`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      versions  = Channel.empty()
                  ^^^^^^^
  ```

- Warning: `subworkflows/local/bam_variant_calling/main.nf:40:43`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
              cram_variant_calling_pair   = Channel.empty()
                                            ^^^^^^^
  ```

- Warning: `subworkflows/local/bam_variant_calling/main.nf:42:43`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
              contamination_table_mutect2 = Channel.empty()
                                            ^^^^^^^
  ```

- Warning: `subworkflows/local/bam_variant_calling/main.nf:43:43`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
              segmentation_table_mutect2  = Channel.empty()
                                            ^^^^^^^
  ```

- Warning: `subworkflows/local/bam_variant_calling/main.nf:44:43`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
              artifact_priors_mutect2     = Channel.empty()
                                            ^^^^^^^
  ```

- Warning: `subworkflows/local/bam_variant_calling/main.nf:52:25`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
                  normal: it[0].status == 0
                          ^^
  ```

- Warning: `subworkflows/local/bam_variant_calling/main.nf:53:25`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
                  tumor:  it[0].status >= 1  // DNA and RNA should NOT have same sample id
                          ^^
  ```

- Warning: `subworkflows/local/bam_variant_calling/main.nf:76:13`: Variable was declared but not used

  ```nextflow
              cram_variant_calling_tumor_only = cram_variant_calling_tumor_filtered.transpose().map{ it -> [it[1], it[2], it[3]] }
              ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  ```

- Warning: `subworkflows/local/bam_variant_calling/main.nf:133:43`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
              vcf_to_normalise            = Channel.empty().mix(BAM_VARIANT_CALLING_SOMATIC.out.vcf_all)
                                            ^^^^^^^
  ```

- Warning: `subworkflows/local/bam_variant_calling/main.nf:134:43`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
              contamination_table_mutect2 = Channel.empty().mix(BAM_VARIANT_CALLING_SOMATIC.out.contamination_table_mutect2)
                                            ^^^^^^^
  ```

- Warning: `subworkflows/local/bam_variant_calling/main.nf:135:43`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
              segmentation_table_mutect2  = Channel.empty().mix(BAM_VARIANT_CALLING_SOMATIC.out.segmentation_table_mutect2)
                                            ^^^^^^^
  ```

- Warning: `subworkflows/local/bam_variant_calling/main.nf:136:43`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
              artifact_priors_mutect2     = Channel.empty().mix(BAM_VARIANT_CALLING_SOMATIC.out.artifact_priors_mutect2)
                                            ^^^^^^^
  ```

- Warning: `subworkflows/local/bam_variant_calling/main.nf:148:84`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          reports = reports.mix(VCF_QC_BCFTOOLS_VCFTOOLS.out.bcftools_stats.collect{ meta, stats -> stats })
                                                                                     ^^^^
  ```

- Warning: `subworkflows/local/bam_variant_calling/main.nf:149:90`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          reports = reports.mix(VCF_QC_BCFTOOLS_VCFTOOLS.out.vcftools_tstv_counts.collect{ meta, counts -> counts })
                                                                                           ^^^^
  ```

- Warning: `subworkflows/local/bam_variant_calling/main.nf:150:88`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          reports = reports.mix(VCF_QC_BCFTOOLS_VCFTOOLS.out.vcftools_tstv_qual.collect{ meta, qual -> qual })
                                                                                         ^^^^
  ```

- Warning: `subworkflows/local/bam_variant_calling/main.nf:151:93`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          reports = reports.mix(VCF_QC_BCFTOOLS_VCFTOOLS.out.vcftools_filter_summary.collect{ meta, summary -> summary })
                                                                                              ^^^^
  ```

- Warning: `subworkflows/local/bam_variant_calling/main.nf:155:39`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
          cram_variant_calling_pair   = Channel.empty()
                                        ^^^^^^^
  ```

- Warning: `subworkflows/local/bam_variant_calling/main.nf:156:39`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
          vcf_to_normalise            = Channel.empty()
                                        ^^^^^^^
  ```

- Warning: `subworkflows/local/bam_variant_calling/main.nf:157:39`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
          contamination_table_mutect2 = Channel.empty()
                                        ^^^^^^^
  ```

- Warning: `subworkflows/local/bam_variant_calling/main.nf:158:39`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
          segmentation_table_mutect2  = Channel.empty()
                                        ^^^^^^^
  ```

- Warning: `subworkflows/local/bam_variant_calling/main.nf:159:39`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
          artifact_priors_mutect2     = Channel.empty()
                                        ^^^^^^^
  ```

- Warning: `subworkflows/local/bam_variant_calling_pre_post_processing/main.nf:27:5`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
      dbsnp                           // channel: [optional]  germline_resource
      ^^^^^
  ```

- Warning: `subworkflows/local/bam_variant_calling_pre_post_processing/main.nf:28:5`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
      dbsnp_tbi                       // channel: [optional]  germline_resource_tbi
      ^^^^^^^^^
  ```

- Warning: `subworkflows/local/bam_variant_calling_pre_post_processing/main.nf:48:17`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      reports   = Channel.empty()
                  ^^^^^^^
  ```

- Warning: `subworkflows/local/bam_variant_calling_pre_post_processing/main.nf:49:17`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      versions  = Channel.empty()
                  ^^^^^^^
  ```

- Warning: `subworkflows/local/bam_variant_calling_pre_post_processing/main.nf:89:5`: Variable was declared but not used

  ```nextflow
      cram_variant_calling_pair     = BAM_VARIANT_CALLING.out.cram_variant_calling_pair  // use same crams for force calling later
      ^^^^^^^^^^^^^^^^^^^^^^^^^
  ```

- Warning: `subworkflows/local/bam_variant_calling_pre_post_processing/main.nf:91:5`: Variable was declared but not used

  ```nextflow
      contamination                 = BAM_VARIANT_CALLING.out.contamination_table
      ^^^^^^^^^^^^^
  ```

- Warning: `subworkflows/local/bam_variant_calling_pre_post_processing/main.nf:92:5`: Variable was declared but not used

  ```nextflow
      segmentation                  = BAM_VARIANT_CALLING.out.segmentation_table
      ^^^^^^^^^^^^
  ```

- Warning: `subworkflows/local/bam_variant_calling_pre_post_processing/main.nf:93:5`: Variable was declared but not used

  ```nextflow
      orientation                   = BAM_VARIANT_CALLING.out.artifact_priors
      ^^^^^^^^^^^
  ```

- Warning: `subworkflows/local/bam_variant_calling_somatic/main.nf:20:5`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
      intervals_bed_combined        // channel: [mandatory] intervals/target regions in one file unzipped
      ^^^^^^^^^^^^^^^^^^^^^^
  ```

- Warning: `subworkflows/local/bam_variant_calling_somatic/main.nf:29:25`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      versions          = Channel.empty()
                          ^^^^^^^
  ```

- Warning: `subworkflows/local/bam_variant_calling_somatic/main.nf:31:25`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      vcf_manta         = Channel.empty()
                          ^^^^^^^
  ```

- Warning: `subworkflows/local/bam_variant_calling_somatic/main.nf:32:25`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      vcf_strelka       = Channel.empty()
                          ^^^^^^^
  ```

- Warning: `subworkflows/local/bam_variant_calling_somatic/main.nf:33:25`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      vcf_mutect2       = Channel.empty()
                          ^^^^^^^
  ```

- Warning: `subworkflows/local/bam_variant_calling_somatic/main.nf:34:25`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      vcf_sage          = Channel.empty()
                          ^^^^^^^
  ```

- Warning: `subworkflows/local/bam_variant_calling_somatic/main.nf:84:23`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
          vcf_strelka = Channel.empty().mix(BAM_VARIANT_CALLING_SOMATIC_STRELKA.out.vcf)
                        ^^^^^^^
  ```

- Warning: `subworkflows/local/bam_variant_calling_somatic/main.nf:115:39`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
          contamination_table_mutect2 = Channel.empty()
                                        ^^^^^^^
  ```

- Warning: `subworkflows/local/bam_variant_calling_somatic/main.nf:116:39`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
          segmentation_table_mutect2  = Channel.empty()
                                        ^^^^^^^
  ```

- Warning: `subworkflows/local/bam_variant_calling_somatic/main.nf:117:39`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
          artifact_priors_mutect2     = Channel.empty()
                                        ^^^^^^^
  ```

- Warning: `subworkflows/local/bam_variant_calling_somatic/main.nf:122:15`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      vcf_all = Channel.empty().mix(
                ^^^^^^^
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

- Warning: `subworkflows/local/bam_variant_calling_somatic_manta/main.nf:37:11`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      vcf = Channel.empty().mix(diploid_sv_vcf, somatic_sv_vcf).map{ meta, vcf -> [ meta + [ variantcaller:'manta' ], vcf ] }
            ^^^^^^^
  ```

- Warning: `subworkflows/local/bam_variant_calling_somatic_mutect2/main.nf:32:16`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      versions = Channel.empty()
                 ^^^^^^^
  ```

- Warning: `subworkflows/local/bam_variant_calling_somatic_mutect2/main.nf:35:80`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      germline_resource_pileup     = germline_resource_tbi ? germline_resource : Channel.empty()
                                                                                 ^^^^^^^
  ```

- Warning: `subworkflows/local/bam_variant_calling_somatic_mutect2/main.nf:36:61`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      germline_resource_pileup_tbi = germline_resource_tbi ?: Channel.empty()
                                                              ^^^^^^^
  ```

- Warning: `subworkflows/local/bam_variant_calling_somatic_mutect2/main.nf:67:23`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          intervals:    it[0].num_intervals > 1
                        ^^
  ```

- Warning: `subworkflows/local/bam_variant_calling_somatic_mutect2/main.nf:68:23`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          no_intervals: it[0].num_intervals <= 1
                        ^^
  ```

- Warning: `subworkflows/local/bam_variant_calling_somatic_mutect2/main.nf:74:23`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          intervals:    it[0].num_intervals > 1
                        ^^
  ```

- Warning: `subworkflows/local/bam_variant_calling_somatic_mutect2/main.nf:75:23`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          no_intervals: it[0].num_intervals <= 1
                        ^^
  ```

- Warning: `subworkflows/local/bam_variant_calling_somatic_mutect2/main.nf:81:23`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          intervals:    it[0].num_intervals > 1
                        ^^
  ```

- Warning: `subworkflows/local/bam_variant_calling_somatic_mutect2/main.nf:82:23`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          no_intervals: it[0].num_intervals <= 1
                        ^^
  ```

- Warning: `subworkflows/local/bam_variant_calling_somatic_mutect2/main.nf:88:23`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          intervals:    it[0].num_intervals > 1
                        ^^
  ```

- Warning: `subworkflows/local/bam_variant_calling_somatic_mutect2/main.nf:89:23`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          no_intervals: it[0].num_intervals <= 1
                        ^^
  ```

- Warning: `subworkflows/local/bam_variant_calling_somatic_mutect2/main.nf:101:11`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      vcf = Channel.empty().mix(MERGE_MUTECT2.out.vcf, vcf_branch.no_intervals).map{ meta, vcf ->
            ^^^^^^^
  ```

- Warning: `subworkflows/local/bam_variant_calling_somatic_mutect2/main.nf:104:11`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      tbi = Channel.empty().mix(MERGE_MUTECT2.out.tbi, tbi_branch.no_intervals).map{ meta, tbi->
            ^^^^^^^
  ```

- Warning: `subworkflows/local/bam_variant_calling_somatic_mutect2/main.nf:107:13`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      stats = Channel.empty().mix(MERGEMUTECTSTATS.out.stats, stats_branch.no_intervals).map{ meta, stats ->
              ^^^^^^^
  ```

- Warning: `subworkflows/local/bam_variant_calling_somatic_mutect2/main.nf:110:12`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      f1r2 = Channel.empty().mix(f1r2_to_merge, f1r2_branch.no_intervals).map{ meta, f1r2->
             ^^^^^^^
  ```

- Warning: `subworkflows/local/bam_variant_calling_somatic_mutect2/main.nf:137:27`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
              intervals:    it[0].num_intervals > 1
                            ^^
  ```

- Warning: `subworkflows/local/bam_variant_calling_somatic_mutect2/main.nf:138:27`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
              no_intervals: it[0].num_intervals <= 1
                            ^^
  ```

- Warning: `subworkflows/local/bam_variant_calling_somatic_mutect2/main.nf:144:27`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
              intervals:    it[0].num_intervals > 1
                            ^^
  ```

- Warning: `subworkflows/local/bam_variant_calling_somatic_mutect2/main.nf:145:27`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
              no_intervals: it[0].num_intervals <= 1
                            ^^
  ```

- Warning: `subworkflows/local/bam_variant_calling_somatic_mutect2/main.nf:157:31`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
          pileup_table_tumor  = Channel.empty().mix(GATHERPILEUPSUMMARIES_TUMOR.out.table, pileup_table_tumor_branch.no_intervals).map{meta, table -> [ meta - meta.subMap('normal_id', 'tumor_id', 'num_intervals') + [id:meta.patient], meta.id, table ] }
                                ^^^^^^^
  ```

- Warning: `subworkflows/local/bam_variant_calling_somatic_mutect2/main.nf:158:31`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
          pileup_table_normal = Channel.empty().mix(GATHERPILEUPSUMMARIES_NORMAL.out.table, pileup_table_normal_branch.no_intervals).map{meta, table -> [ meta - meta.subMap('normal_id', 'tumor_id', 'num_intervals') + [id:meta.patient], meta.id, table ] }
                                ^^^^^^^
  ```

- Warning: `subworkflows/local/bam_variant_calling_somatic_mutect2/main.nf:175:39`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
          ch_seg_to_filtermutectcalls = Channel.empty()
                                        ^^^^^^^
  ```

- Warning: `subworkflows/local/bam_variant_calling_somatic_mutect2/main.nf:176:40`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
          ch_cont_to_filtermutectcalls = Channel.empty()
                                         ^^^^^^^
  ```

- Warning: `subworkflows/local/bam_variant_calling_somatic_mutect2/main.nf:209:40`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
          artifact_priors              = Channel.empty()
                                         ^^^^^^^
  ```

- Warning: `subworkflows/local/bam_variant_calling_somatic_mutect2/main.nf:210:40`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
          ch_cont_to_filtermutectcalls = Channel.empty()
                                         ^^^^^^^
  ```

- Warning: `subworkflows/local/bam_variant_calling_somatic_mutect2/main.nf:211:40`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
          ch_seg_to_filtermutectcalls  = Channel.empty()
                                         ^^^^^^^
  ```

- Warning: `subworkflows/local/bam_variant_calling_somatic_mutect2/main.nf:212:40`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
          pileup_table_normal          = Channel.empty()
                                         ^^^^^^^
  ```

- Warning: `subworkflows/local/bam_variant_calling_somatic_mutect2/main.nf:213:40`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
          pileup_table_tumor           = Channel.empty()
                                         ^^^^^^^
  ```

- Warning: `subworkflows/local/bam_variant_calling_somatic_sage/main.nf:22:16`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      versions = Channel.empty()
                 ^^^^^^^
  ```

- Warning: `subworkflows/local/bam_variant_calling_somatic_sage/main.nf:26:50`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      if (!params.sage_ensembl_dir) sage_ensembl = Channel.value([])
                                                   ^^^^^^^
  ```

- Warning: `subworkflows/local/bam_variant_calling_somatic_sage/main.nf:28:28`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
          UNTAR_SAGE_ENSEMBL(Channel.fromPath(params.sage_ensembl_dir).collect().map{ it -> [ [ id:it[0].baseName ], it ] })
                             ^^^^^^^
  ```

- Warning: `subworkflows/local/bam_variant_calling_somatic_sage/main.nf:32:28`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
          UNZIP_SAGE_ENSEMBL(Channel.fromPath(params.sage_ensembl_dir).collect().map{ it -> [ [ id:it[0].baseName ], it ] })
                             ^^^^^^^
  ```

- Warning: `subworkflows/local/bam_variant_calling_somatic_sage/main.nf:36:24`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
          sage_ensembl = Channel.fromPath(params.sage_ensembl_dir).collect().map{ it -> [ [ id:it[0].baseName ], it ] }
                         ^^^^^^^
  ```

- Warning: `subworkflows/local/bam_variant_calling_somatic_sage/main.nf:47:9`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
          Channel.fromPath(params.sage_highconfidence).collect().map{ it -> [ [ id:it[0].baseName ], it ] },
          ^^^^^^^
  ```

- Warning: `subworkflows/local/bam_variant_calling_somatic_sage/main.nf:48:9`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
          Channel.fromPath(params.sage_actionablepanel).collect().map{ it -> [ [ id:it[0].baseName ], it ] },
          ^^^^^^^
  ```

- Warning: `subworkflows/local/bam_variant_calling_somatic_sage/main.nf:49:9`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
          Channel.fromPath(params.sage_knownhotspots).collect().map{ it -> [ [ id:it[0].baseName ], it ] },
          ^^^^^^^
  ```

- Warning: `subworkflows/local/bam_variant_calling_somatic_sage/main.nf:57:23`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          intervals:    it[0].num_intervals > 1
                        ^^
  ```

- Warning: `subworkflows/local/bam_variant_calling_somatic_sage/main.nf:58:23`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          no_intervals: it[0].num_intervals <= 1
                        ^^
  ```

- Warning: `subworkflows/local/bam_variant_calling_somatic_sage/main.nf:71:26`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          .map{ meta, vcf, tbi -> [ meta - meta.subMap('normal_id', 'tumor_id','num_intervals') + [ variantcaller:'sage' ], vcf ] }
                           ^^^
  ```

- Warning: `subworkflows/local/bam_variant_calling_somatic_strelka/main.nf:22:16`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      versions = Channel.empty()
                 ^^^^^^^
  ```

- Warning: `subworkflows/local/bam_variant_calling_somatic_strelka/main.nf:28:93`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          .map{ meta, normal_cram, normal_crai, tumor_cram, tumor_crai, manta_vcf, manta_tbi, intervals_gz_tbi, num_intervals -> [ meta + [ num_intervals:0 ], normal_cram, normal_crai, tumor_cram, tumor_crai, manta_vcf, manta_tbi, [], [] ] }
                                                                                              ^^^^^^^^^^^^^^^^
  ```

- Warning: `subworkflows/local/bam_variant_calling_somatic_strelka/main.nf:28:111`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          .map{ meta, normal_cram, normal_crai, tumor_cram, tumor_crai, manta_vcf, manta_tbi, intervals_gz_tbi, num_intervals -> [ meta + [ num_intervals:0 ], normal_cram, normal_crai, tumor_cram, tumor_crai, manta_vcf, manta_tbi, [], [] ] }
                                                                                                                ^^^^^^^^^^^^^
  ```

- Warning: `subworkflows/local/bam_variant_calling_somatic_strelka/main.nf:37:5`: Variable was declared but not used

  ```nextflow
      vcf_indels = STRELKA_SOMATIC.out.vcf_indels.branch{
      ^^^^^^^^^^
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

- Warning: `subworkflows/local/bam_variant_calling_somatic_strelka/main.nf:44:5`: Variable was declared but not used

  ```nextflow
      vcf_snvs = STRELKA_SOMATIC.out.vcf_snvs.branch{
      ^^^^^^^^
  ```

- Warning: `subworkflows/local/bam_variant_calling_somatic_strelka/main.nf:46:23`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          intervals:    it[0].num_intervals > 1
                        ^^
  ```

- Warning: `subworkflows/local/bam_variant_calling_somatic_strelka/main.nf:47:23`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          no_intervals: it[0].num_intervals <= 1
                        ^^
  ```

- Warning: `subworkflows/local/channel_baserecalibrator_create_csv/main.nf:8:9`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          tools
          ^^^^^
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

- Warning: `subworkflows/local/cram_qc_mosdepth_samtools/main.nf:23:42`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
      MOSDEPTH(cram.combine(intervals.map{ meta, bed -> [ bed?:[] ] }), fasta)
                                           ^^^^
  ```

- Warning: `subworkflows/local/fastq_align/main.nf:19:16`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      versions = Channel.empty()
                 ^^^^^^^
  ```

- Warning: `subworkflows/local/fastq_align/main.nf:20:15`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      reports = Channel.empty()
                ^^^^^^^
  ```

- Warning: `subworkflows/local/fastq_align/main.nf:29:11`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      bam = Channel.empty()
            ^^^^^^^
  ```

- Warning: `subworkflows/local/maf_filtering/main.nf:17:17`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      versions  = Channel.empty()
                  ^^^^^^^
  ```

- Warning: `subworkflows/local/maf_filtering/main.nf:18:17`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      maf       = Channel.empty()
                  ^^^^^^^
  ```

- Warning: `subworkflows/local/maf_rna_filtering/main.nf:15:16`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      versions = Channel.empty()
                 ^^^^^^^
  ```

- Warning: `subworkflows/local/prepare_genome/main.nf:43:16`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      versions = Channel.empty()
                 ^^^^^^^
  ```

- Warning: `subworkflows/local/prepare_genome/main.nf:47:25`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
          UNBGZIP_FASTA ( Channel.fromPath(params.fasta).collect().map{ fa -> [ [ id:fa.baseName[0] - ~/\.fa(sta)?$/ ], fa ] } )
                          ^^^^^^^
  ```

- Warning: `subworkflows/local/prepare_genome/main.nf:71:22`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
          bwa        = Channel.empty()
                       ^^^^^^^
  ```

- Warning: `subworkflows/local/prepare_genome/main.nf:72:22`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
          bwamem2    = Channel.empty()
                       ^^^^^^^
  ```

- Warning: `subworkflows/local/prepare_genome/main.nf:73:22`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
          hashtable  = Channel.empty()
                       ^^^^^^^
  ```

- Warning: `subworkflows/local/prepare_genome/main.nf:96:21`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
                      Channel.fromPath(params.gtf).map{ it -> [[id:it[0].baseName], it] }
                      ^^^^^^^
  ```

- Warning: `subworkflows/local/prepare_genome/main.nf:101:26`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
                  ch_gtf = Channel.fromPath(params.gtf).collect().map{gtf -> [[id:"gtf"], gtf]}
                           ^^^^^^^
  ```

- Warning: `subworkflows/local/prepare_genome/main.nf:106:21`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
                      Channel.fromPath(params.gff).map{ it -> [[id:it[0].baseName], it] }
                      ^^^^^^^
  ```

- Warning: `subworkflows/local/prepare_genome/main.nf:111:26`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
                  ch_gff = Channel.fromPath(params.gff).collect().map{gff -> [[id:"gff"], gff]}
                           ^^^^^^^
  ```

- Warning: `subworkflows/local/prepare_genome/main.nf:130:21`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
                      Channel.fromPath(params.star_index).map{ it -> [[id:it[0].baseName], it] }
                      ^^^^^^^
  ```

- Warning: `subworkflows/local/prepare_genome/main.nf:135:33`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
                  ch_star_index = Channel.fromPath(params.star_index).collect().map{star_index -> [[id:"star_index"], star_index]}
                                  ^^^^^^^
  ```

- Warning: `subworkflows/local/prepare_genome/main.nf:148:35`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
                  ch_splicesites  = Channel.fromPath(params.splicesites).collect().map{ it -> [ [ id:'null' ], it ]}
                                    ^^^^^^^
  ```

- Warning: `subworkflows/local/prepare_genome/main.nf:156:36`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
                  ch_hisat2_index  = Channel.fromPath(params.hisat2_index).collect().map{it -> [ [ id:"hisat2_index" ], it ]}
                                     ^^^^^^^
  ```

- Warning: `subworkflows/local/prepare_genome/main.nf:171:27`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
          ch_star_index   = Channel.empty()
                            ^^^^^^^
  ```

- Warning: `subworkflows/local/prepare_genome/main.nf:172:27`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
          ch_gtf          = Channel.empty()
                            ^^^^^^^
  ```

- Warning: `subworkflows/local/prepare_genome/main.nf:173:27`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
          ch_hisat2_index = Channel.empty()
                            ^^^^^^^
  ```

- Warning: `subworkflows/local/prepare_genome/main.nf:174:27`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
          ch_splicesites  = Channel.value([])
                            ^^^^^^^
  ```

- Warning: `subworkflows/local/prepare_genome/main.nf:191:58`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          dbsnp_tbi             = TABIX_DBSNP.out.tbi.map{ meta, tbi -> [tbi] }.collect()               // path: dbsnb.vcf.gz.tbi
                                                           ^^^^
  ```

- Warning: `subworkflows/local/prepare_genome/main.nf:194:61`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          fasta_fai             = SAMTOOLS_FAIDX.out.fai.map{ meta, fai -> [fai] }                      // path: genome.fasta.fai
                                                              ^^^^
  ```

- Warning: `subworkflows/local/prepare_genome/main.nf:195:70`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          germline_resource_tbi = TABIX_GERMLINE_RESOURCE.out.tbi.map{ meta, tbi -> [tbi] }.collect()   // path: germline_resource.vcf.gz.tbi
                                                                       ^^^^
  ```

- Warning: `subworkflows/local/prepare_genome/main.nf:196:63`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          known_snps_tbi        = TABIX_KNOWN_SNPS.out.tbi.map{ meta, tbi -> [tbi] }.collect()          // path: {known_indels*}.vcf.gz.tbi
                                                                ^^^^
  ```

- Warning: `subworkflows/local/prepare_genome/main.nf:197:65`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          known_indels_tbi      = TABIX_KNOWN_INDELS.out.tbi.map{ meta, tbi -> [tbi] }.collect()        // path: {known_indels*}.vcf.gz.tbi
                                                                  ^^^^
  ```

- Warning: `subworkflows/local/prepare_genome/main.nf:198:56`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          pon_tbi               = TABIX_PON.out.tbi.map{ meta, tbi -> [tbi] }.collect()                 // path: pon.vcf.gz.tbi
                                                         ^^^^
  ```

- Warning: `subworkflows/local/prepare_realignment/main.nf:24:9`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          dict
          ^^^^
  ```

- Warning: `subworkflows/local/prepare_realignment/main.nf:31:22`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
          versions   = Channel.empty()
                       ^^^^^^^
  ```

- Warning: `subworkflows/local/prepare_realignment/main.nf:32:22`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
          bam_mapped = Channel.empty()
                       ^^^^^^^
  ```

- Warning: `subworkflows/local/prepare_realignment/main.nf:39:52`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
                                          norealign: it[0].status == 1
                                                     ^^
  ```

- Warning: `subworkflows/local/prepare_realignment/main.nf:40:52`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
                                          realign:   it[0].status == 2 || it[0].status == 0
                                                     ^^
  ```

- Warning: `subworkflows/local/prepare_realignment/main.nf:40:73`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
                                          realign:   it[0].status == 2 || it[0].status == 0
                                                                          ^^
  ```

- Warning: `subworkflows/local/prepare_realignment/main.nf:45:54`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
                                          isconsensus: it[0].consensus == true
                                                       ^^
  ```

- Warning: `subworkflows/local/prepare_realignment/main.nf:46:54`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
                                          noconsensus: it[0].consensus == false
                                                       ^^
  ```

- Warning: `subworkflows/local/prepare_realignment/main.nf:63:52`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
                                          norealign: it[0].status == 1
                                                     ^^
  ```

- Warning: `subworkflows/local/prepare_realignment/main.nf:64:52`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
                                          realign:   it[0].status == 2 || it[0].status == 0
                                                     ^^
  ```

- Warning: `subworkflows/local/prepare_realignment/main.nf:64:73`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
                                          realign:   it[0].status == 2 || it[0].status == 0
                                                                          ^^
  ```

- Warning: `subworkflows/local/prepare_realignment/main.nf:67:52`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
                                          norealign: it[0].status == 1
                                                     ^^
  ```

- Warning: `subworkflows/local/prepare_realignment/main.nf:68:52`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
                                          realign:   it[0].status == 2 || it[0].status == 0
                                                     ^^
  ```

- Warning: `subworkflows/local/prepare_realignment/main.nf:68:73`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
                                          realign:   it[0].status == 2 || it[0].status == 0
                                                                          ^^
  ```

- Warning: `subworkflows/local/prepare_realignment/main.nf:138:44`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
      bam_mapped = bam_mapped.map{meta, bam, bai -> [meta - meta.subMap('single_end'), bam]}
                                             ^^^
  ```

- Warning: `subworkflows/local/prepare_reference_and_intervals/main.nf:11:16`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      versions = Channel.empty()
                 ^^^^^^^
  ```

- Warning: `subworkflows/local/prepare_reference_and_intervals/main.nf:14:54`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      dbsnp              = params.dbsnp              ? Channel.fromPath(params.dbsnp).collect()                    : Channel.value([])
                                                       ^^^^^^^
  ```

- Warning: `subworkflows/local/prepare_reference_and_intervals/main.nf:14:116`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      dbsnp              = params.dbsnp              ? Channel.fromPath(params.dbsnp).collect()                    : Channel.value([])
                                                                                                                     ^^^^^^^
  ```

- Warning: `subworkflows/local/prepare_reference_and_intervals/main.nf:15:54`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      known_snps         = params.known_snps         ? Channel.fromPath(params.known_snps).collect()               : Channel.value([])
                                                       ^^^^^^^
  ```

- Warning: `subworkflows/local/prepare_reference_and_intervals/main.nf:15:116`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      known_snps         = params.known_snps         ? Channel.fromPath(params.known_snps).collect()               : Channel.value([])
                                                                                                                     ^^^^^^^
  ```

- Warning: `subworkflows/local/prepare_reference_and_intervals/main.nf:16:54`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      fasta              = params.fasta              ? Channel.fromPath(params.fasta).collect()                    : Channel.empty()
                                                       ^^^^^^^
  ```

- Warning: `subworkflows/local/prepare_reference_and_intervals/main.nf:16:116`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      fasta              = params.fasta              ? Channel.fromPath(params.fasta).collect()                    : Channel.empty()
                                                                                                                     ^^^^^^^
  ```

- Warning: `subworkflows/local/prepare_reference_and_intervals/main.nf:17:54`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      germline_resource  = params.germline_resource  ? Channel.fromPath(params.germline_resource).collect()        : Channel.value([]) //Mutec2 does not require a germline resource, so set to optional input
                                                       ^^^^^^^
  ```

- Warning: `subworkflows/local/prepare_reference_and_intervals/main.nf:17:116`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      germline_resource  = params.germline_resource  ? Channel.fromPath(params.germline_resource).collect()        : Channel.value([]) //Mutec2 does not require a germline resource, so set to optional input
                                                                                                                     ^^^^^^^
  ```

- Warning: `subworkflows/local/prepare_reference_and_intervals/main.nf:18:54`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      known_indels       = params.known_indels       ? Channel.fromPath(params.known_indels).collect()             : Channel.value([])
                                                       ^^^^^^^
  ```

- Warning: `subworkflows/local/prepare_reference_and_intervals/main.nf:18:116`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      known_indels       = params.known_indels       ? Channel.fromPath(params.known_indels).collect()             : Channel.value([])
                                                                                                                     ^^^^^^^
  ```

- Warning: `subworkflows/local/prepare_reference_and_intervals/main.nf:19:54`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      pon                = params.pon                ? Channel.fromPath(params.pon).collect()                      : Channel.value([]) //PON is optional for Mutect2 (but highly recommended)
                                                       ^^^^^^^
  ```

- Warning: `subworkflows/local/prepare_reference_and_intervals/main.nf:19:116`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      pon                = params.pon                ? Channel.fromPath(params.pon).collect()                      : Channel.value([]) //PON is optional for Mutect2 (but highly recommended)
                                                                                                                     ^^^^^^^
  ```

- Warning: `subworkflows/local/prepare_reference_and_intervals/main.nf:20:5`: Variable was declared but not used

  ```nextflow
      whitelist          = params.whitelist          ? Channel.fromPath(params.whitelist).collect()                : Channel.value([]) // whitelist optional for filtering
      ^^^^^^^^^
  ```

- Warning: `subworkflows/local/prepare_reference_and_intervals/main.nf:20:54`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      whitelist          = params.whitelist          ? Channel.fromPath(params.whitelist).collect()                : Channel.value([]) // whitelist optional for filtering
                                                       ^^^^^^^
  ```

- Warning: `subworkflows/local/prepare_reference_and_intervals/main.nf:20:116`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      whitelist          = params.whitelist          ? Channel.fromPath(params.whitelist).collect()                : Channel.value([]) // whitelist optional for filtering
                                                                                                                     ^^^^^^^
  ```

- Warning: `subworkflows/local/prepare_reference_and_intervals/main.nf:34:99`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      bwa                    = params.fasta                   ? params.bwa                        ? Channel.fromPath(params.bwa).collect()                           : PREPARE_GENOME.out.bwa                   : []
                                                                                                    ^^^^^^^
  ```

- Warning: `subworkflows/local/prepare_reference_and_intervals/main.nf:35:99`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      bwamem2                = params.fasta                   ? params.bwamem2                    ? Channel.fromPath(params.bwamem2).collect()                       : PREPARE_GENOME.out.bwamem2               : []
                                                                                                    ^^^^^^^
  ```

- Warning: `subworkflows/local/prepare_reference_and_intervals/main.nf:36:99`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      dragmap                = params.fasta                   ? params.dragmap                    ? Channel.fromPath(params.dragmap).collect()                       : PREPARE_GENOME.out.hashtable             : []
                                                                                                    ^^^^^^^
  ```

- Warning: `subworkflows/local/prepare_reference_and_intervals/main.nf:37:99`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      hisat2_index           = params.fasta                   ? params.hisat2_index               ? Channel.fromPath(params.hisat2_index).map{ it -> [ [id:'ht_idx'], it ] }.collect()                          : PREPARE_GENOME.out.hisat2_index : []
                                                                                                    ^^^^^^^
  ```

- Warning: `subworkflows/local/prepare_reference_and_intervals/main.nf:38:99`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      splicesites            = params.fasta                   ? params.splicesites                ? Channel.fromPath(params.splicesites).collect()                   : PREPARE_GENOME.out.splicesites           : []
                                                                                                    ^^^^^^^
  ```

- Warning: `subworkflows/local/prepare_reference_and_intervals/main.nf:39:63`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      dict                   = params.dict                    ? Channel.fromPath(params.dict).map{ it -> [ [id:'dict'], it ] }.collect()                             : PREPARE_GENOME.out.dict
                                                                ^^^^^^^
  ```

- Warning: `subworkflows/local/prepare_reference_and_intervals/main.nf:40:99`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      fasta_fai              = params.fasta                   ? params.fasta_fai                  ? Channel.fromPath(params.fasta_fai).collect()                     : PREPARE_GENOME.out.fasta_fai             : []
                                                                                                    ^^^^^^^
  ```

- Warning: `subworkflows/local/prepare_reference_and_intervals/main.nf:41:99`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      dbsnp_tbi              = params.dbsnp                   ? params.dbsnp_tbi                  ? Channel.fromPath(params.dbsnp_tbi).collect()                     : PREPARE_GENOME.out.dbsnp_tbi             : Channel.value([])
                                                                                                    ^^^^^^^
  ```

- Warning: `subworkflows/local/prepare_reference_and_intervals/main.nf:41:209`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      dbsnp_tbi              = params.dbsnp                   ? params.dbsnp_tbi                  ? Channel.fromPath(params.dbsnp_tbi).collect()                     : PREPARE_GENOME.out.dbsnp_tbi             : Channel.value([])
                                                                                                                                                                                                                  ^^^^^^^
  ```

- Warning: `subworkflows/local/prepare_reference_and_intervals/main.nf:42:99`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      germline_resource_tbi  = params.germline_resource       ? params.germline_resource_tbi      ? Channel.fromPath(params.germline_resource_tbi).collect()         : PREPARE_GENOME.out.germline_resource_tbi : []
                                                                                                    ^^^^^^^
  ```

- Warning: `subworkflows/local/prepare_reference_and_intervals/main.nf:43:99`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      known_indels_tbi       = params.known_indels            ? params.known_indels_tbi           ? Channel.fromPath(params.known_indels_tbi).collect()              : PREPARE_GENOME.out.known_indels_tbi      : Channel.value([])
                                                                                                    ^^^^^^^
  ```

- Warning: `subworkflows/local/prepare_reference_and_intervals/main.nf:43:209`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      known_indels_tbi       = params.known_indels            ? params.known_indels_tbi           ? Channel.fromPath(params.known_indels_tbi).collect()              : PREPARE_GENOME.out.known_indels_tbi      : Channel.value([])
                                                                                                                                                                                                                  ^^^^^^^
  ```

- Warning: `subworkflows/local/prepare_reference_and_intervals/main.nf:44:99`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      known_snps_tbi         = params.known_snps              ? params.known_snps_tbi             ? Channel.fromPath(params.known_snps_tbi).collect()                : PREPARE_GENOME.out.known_snps_tbi        : Channel.value([])
                                                                                                    ^^^^^^^
  ```

- Warning: `subworkflows/local/prepare_reference_and_intervals/main.nf:44:209`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      known_snps_tbi         = params.known_snps              ? params.known_snps_tbi             ? Channel.fromPath(params.known_snps_tbi).collect()                : PREPARE_GENOME.out.known_snps_tbi        : Channel.value([])
                                                                                                                                                                                                                  ^^^^^^^
  ```

- Warning: `subworkflows/local/prepare_reference_and_intervals/main.nf:45:99`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      pon_tbi                = params.pon                     ? params.pon_tbi                    ? Channel.fromPath(params.pon_tbi).collect()                       : PREPARE_GENOME.out.pon_tbi               : []
                                                                                                    ^^^^^^^
  ```

- Warning: `subworkflows/local/samplesheet_to_channel/main.nf:24:16`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          .map { patient_sample, num_lanes, ch_items ->
                 ^^^^^^^^^^^^^^
  ```

- Warning: `subworkflows/local/samplesheet_to_channel/main.nf:164:30`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          input_sample.filter{ it[0].status == 1 | it[0].status == 2 }.ifEmpty{ // In this case, the sample-sheet contains no tumor-samples
                               ^^
  ```

- Warning: `subworkflows/local/samplesheet_to_channel/main.nf:164:50`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          input_sample.filter{ it[0].status == 1 | it[0].status == 2 }.ifEmpty{ // In this case, the sample-sheet contains no tumor-samples
                                                   ^^
  ```

- Warning: `subworkflows/local/samplesheet_to_channel/main.nf:176:30`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          input_sample.filter{ it[0].status == 0 }.ifEmpty{ // In this case, the sample-sheet contains no normal/germline-samples
                               ^^
  ```

- Warning: `subworkflows/local/samplesheet_to_channel/main.nf:245:68`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          InputStream gzipStream = new java.util.zip.GZIPInputStream(it)
                                                                     ^^
  ```

- Warning: `subworkflows/local/utils_nfcore_rnadnavar_pipeline/main.nf:40:16`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      versions = Channel.empty()
                 ^^^^^^^
  ```

- Warning: `subworkflows/local/utils_nfcore_rnadnavar_pipeline/main.nf:99:9`: Variable was declared but not used

  ```nextflow
      def checkPathParamList = [
          ^^^^^^^^^^^^^^^^^^
  ```

- Warning: `subworkflows/local/utils_nfcore_rnadnavar_pipeline/main.nf:129:11`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
          ? Channel.empty()
            ^^^^^^^
  ```

- Warning: `subworkflows/local/utils_nfcore_rnadnavar_pipeline/main.nf:131:15`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
              ? Channel.fromList(samplesheetToList(input, "${projectDir}/assets/schema_input.json"))
                ^^^^^^^
  ```

- Warning: `subworkflows/local/utils_nfcore_rnadnavar_pipeline/main.nf:132:15`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
              : Channel.fromList(samplesheetToList(params.input_restart, "${projectDir}/assets/schema_input.json"))
                ^^^^^^^
  ```

- Warning: `subworkflows/local/vcf_annotate/main.nf:18:16`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      reports  = Channel.empty()
                 ^^^^^^^
  ```

- Warning: `subworkflows/local/vcf_annotate/main.nf:19:16`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      vcf_ann  = Channel.empty()
                 ^^^^^^^
  ```

- Warning: `subworkflows/local/vcf_annotate/main.nf:20:16`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      tab_ann  = Channel.empty()
                 ^^^^^^^
  ```

- Warning: `subworkflows/local/vcf_annotate/main.nf:21:16`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      json_ann = Channel.empty()
                 ^^^^^^^
  ```

- Warning: `subworkflows/local/vcf_annotate/main.nf:22:16`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      versions = Channel.empty()
                 ^^^^^^^
  ```

- Warning: `subworkflows/local/vcf_annotate/main.nf:29:63`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
              vep_cache_version  = params.vep_cache_version  ?: Channel.empty()
                                                                ^^^^^^^
  ```

- Warning: `subworkflows/local/vcf_annotate/main.nf:30:63`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
              vep_genome         = params.vep_genome         ?: Channel.empty()
                                                                ^^^^^^^
  ```

- Warning: `subworkflows/local/vcf_annotate/main.nf:31:63`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
              vep_species        = params.vep_species        ?: Channel.empty()
                                                                ^^^^^^^
  ```

- Warning: `subworkflows/local/vcf_consensus/main.nf:23:31`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      versions                = Channel.empty()
                                ^^^^^^^
  ```

- Warning: `subworkflows/local/vcf_consensus/main.nf:25:31`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      maf_from_consensus_dna  = Channel.empty()
                                ^^^^^^^
  ```

- Warning: `subworkflows/local/vcf_consensus/main.nf:26:31`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      mafs_from_varcal_dna    = Channel.empty()
                                ^^^^^^^
  ```

- Warning: `subworkflows/local/vcf_consensus/main.nf:27:31`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      consensus_maf           = Channel.empty()
                                ^^^^^^^
  ```

- Warning: `subworkflows/local/vcf_consensus/main.nf:38:38`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
                                  vcf: it[0].data_type == "vcf"
                                       ^^
  ```

- Warning: `subworkflows/local/vcf_consensus/main.nf:39:38`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
                                  maf: it[0].data_type == "maf"
                                       ^^
  ```

- Warning: `subworkflows/local/vcf_consensus/main.nf:45:69`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
              tools_list = params.tools.split(',').toList().findAll { it in ['sage', 'strelka', 'mutect2'] }.unique()
                                                                      ^^
  ```

- Warning: `subworkflows/local/vcf_consensus/main.nf:68:38`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
                                  dna: it[0].status <= 1
                                       ^^
  ```

- Warning: `subworkflows/local/vcf_consensus/main.nf:69:38`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
                                  rna: it[0].status == 2
                                       ^^
  ```

- Warning: `subworkflows/local/vcf_consensus/main.nf:73:38`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
                                  dna: it[0].status <= 1
                                       ^^
  ```

- Warning: `subworkflows/local/vcf_consensus/main.nf:74:38`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
                                  rna: it[0].status == 2
                                       ^^
  ```

- Warning: `subworkflows/local/vcf_consensus/main.nf:145:13`: Variable was declared but not used

  ```nextflow
              mafs_to_rescue = mafs_dna_crossed_with_rna_rescue.mix(mafs_rna_crossed_with_dna_rescue)
              ^^^^^^^^^^^^^^
  ```

- Warning: `subworkflows/local/vcf_consensus/main.nf:149:38`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
                                  dna: it[0].status <= 1
                                       ^^
  ```

- Warning: `subworkflows/local/vcf_consensus/main.nf:150:38`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
                                  rna: it[0].status == 2
                                       ^^
  ```

- Warning: `subworkflows/local/vcf_consensus/main.nf:154:13`: Variable was declared but not used

  ```nextflow
              run_rescue_out = RUN_CONSENSUS_RESCUE.out.maf.branch{
              ^^^^^^^^^^^^^^
  ```

- Warning: `subworkflows/local/vcf_consensus/main.nf:155:31`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
                  intervals:    it[0].num_intervals > 1
                                ^^
  ```

- Warning: `subworkflows/local/vcf_consensus/main.nf:156:31`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
                  no_intervals: it[0].num_intervals <= 1
                                ^^
  ```

- Warning: `subworkflows/local/vcf_consensus/main.nf:179:38`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
                                  vcf: it[0].data_type == "vcf"
                                       ^^
  ```

- Warning: `subworkflows/local/vcf_consensus/main.nf:180:38`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
                                  maf: it[0].data_type == "maf"
                                       ^^
  ```

- Warning: `subworkflows/local/vcf_normalize/main.nf:22:24`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      version          = Channel.empty()
                         ^^^^^^^
  ```

- Warning: `subworkflows/local/vcf_normalize/main.nf:32:27`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
          vcf_decomposed  = Channel.empty()
                            ^^^^^^^
  ```

- Warning: `subworkflows/local/vcf_qc_bcftools_vcftools/main.nf:13:16`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      versions = Channel.empty()
                 ^^^^^^^
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

- Warning: `subworkflows/nf-core/fastq_align_hisat2/main.nf:14:19`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_versions = Channel.empty()
                    ^^^^^^^
  ```

- Warning: `subworkflows/nf-core/fastq_align_star/main.nf:20:19`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_versions = Channel.empty()
                    ^^^^^^^
  ```

- Warning: `subworkflows/nf-core/vcf_annotate_ensemblvep/main.nf:19:19`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_versions = Channel.empty()
                    ^^^^^^^
  ```

- Warning: `workflows/rnadnavar/main.nf:54:5`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
      ch_samplesheet // channel: samplesheet read in from --input
      ^^^^^^^^^^^^^^
  ```

- Warning: `workflows/rnadnavar/main.nf:58:24`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_multiqc_files = Channel.empty()
                         ^^^^^^^
  ```

- Warning: `workflows/rnadnavar/main.nf:59:22`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      multiqc_report = Channel.empty()
                       ^^^^^^^
  ```

- Warning: `workflows/rnadnavar/main.nf:60:15`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      reports = Channel.empty()
                ^^^^^^^
  ```

- Warning: `workflows/rnadnavar/main.nf:62:16`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      versions = Channel.empty()
                 ^^^^^^^
  ```

- Warning: `workflows/rnadnavar/main.nf:66:57`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
          ch_from_samplesheet = params.build_only_index ? Channel.empty() : Channel.fromList(samplesheetToList(params.input, "${projectDir}/assets/schema_input.json"))
                                                          ^^^^^^^
  ```

- Warning: `workflows/rnadnavar/main.nf:66:75`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
          ch_from_samplesheet = params.build_only_index ? Channel.empty() : Channel.fromList(samplesheetToList(params.input, "${projectDir}/assets/schema_input.json"))
                                                                            ^^^^^^^
  ```

- Warning: `workflows/rnadnavar/main.nf:69:57`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
          ch_from_samplesheet = params.build_only_index ? Channel.empty() : Channel.fromList(samplesheetToList(params.input, "${projectDir}/assets/schema_input.json"))
                                                          ^^^^^^^
  ```

- Warning: `workflows/rnadnavar/main.nf:69:75`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
          ch_from_samplesheet = params.build_only_index ? Channel.empty() : Channel.fromList(samplesheetToList(params.input, "${projectDir}/assets/schema_input.json"))
                                                                            ^^^^^^^
  ```

- Warning: `workflows/rnadnavar/main.nf:78:5`: Variable was declared but not used

  ```nextflow
      multiqc_config = Channel.fromPath("${projectDir}/assets/multiqc_config.yml", checkIfExists: true)
      ^^^^^^^^^^^^^^
  ```

- Warning: `workflows/rnadnavar/main.nf:78:22`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      multiqc_config = Channel.fromPath("${projectDir}/assets/multiqc_config.yml", checkIfExists: true)
                       ^^^^^^^
  ```

- Warning: `workflows/rnadnavar/main.nf:79:5`: Variable was declared but not used

  ```nextflow
      multiqc_custom_config = params.multiqc_config ? Channel.fromPath(params.multiqc_config, checkIfExists: true) : Channel.empty()
      ^^^^^^^^^^^^^^^^^^^^^
  ```

- Warning: `workflows/rnadnavar/main.nf:79:53`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      multiqc_custom_config = params.multiqc_config ? Channel.fromPath(params.multiqc_config, checkIfExists: true) : Channel.empty()
                                                      ^^^^^^^
  ```

- Warning: `workflows/rnadnavar/main.nf:79:116`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      multiqc_custom_config = params.multiqc_config ? Channel.fromPath(params.multiqc_config, checkIfExists: true) : Channel.empty()
                                                                                                                     ^^^^^^^
  ```

- Warning: `workflows/rnadnavar/main.nf:80:5`: Variable was declared but not used

  ```nextflow
      multiqc_logo = params.multiqc_logo ? Channel.fromPath(params.multiqc_logo, checkIfExists: true) : Channel.empty()
      ^^^^^^^^^^^^
  ```

- Warning: `workflows/rnadnavar/main.nf:80:42`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      multiqc_logo = params.multiqc_logo ? Channel.fromPath(params.multiqc_logo, checkIfExists: true) : Channel.empty()
                                           ^^^^^^^
  ```

- Warning: `workflows/rnadnavar/main.nf:80:103`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      multiqc_logo = params.multiqc_logo ? Channel.fromPath(params.multiqc_logo, checkIfExists: true) : Channel.empty()
                                                                                                        ^^^^^^^
  ```

- Warning: `workflows/rnadnavar/main.nf:85:27`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
          ensemblvep_info = Channel.of([[id: "${params.vep_cache_version}_${params.vep_genome}"], params.vep_genome, params.vep_species, params.vep_cache_version])
                            ^^^^^^^
  ```

- Warning: `workflows/rnadnavar/main.nf:87:67`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          vep_cache = ENSEMBLVEP_DOWNLOAD.out.cache.collect().map { meta, cache -> [cache] }
                                                                    ^^^^
  ```

- Warning: `workflows/rnadnavar/main.nf:91:25`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
          UNZIP_VEP_CACHE(Channel.fromPath(params.vep_cache).collect().map { it -> [[id: it[0].baseName], it] })
                          ^^^^^^^
  ```

- Warning: `workflows/rnadnavar/main.nf:92:64`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          vep_cache = UNZIP_VEP_CACHE.out.unzipped_archive.map { it[1] }
                                                                 ^^
  ```

- Warning: `workflows/rnadnavar/main.nf:131:5`: Variable was declared but not used

  ```nextflow
      known_sites_snps = PREPARE_REFERENCE_AND_INTERVALS.out.known_sites_snps
      ^^^^^^^^^^^^^^^^
  ```

- Warning: `workflows/rnadnavar/main.nf:132:5`: Variable was declared but not used

  ```nextflow
      known_sites_snps_tbi = PREPARE_REFERENCE_AND_INTERVALS.out.known_sites_snps_tbi
      ^^^^^^^^^^^^^^^^^^^^
  ```

- Warning: `workflows/rnadnavar/main.nf:209:13`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
              Channel.empty(),
              ^^^^^^^
  ```

- Warning: `workflows/rnadnavar/main.nf:211:13`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
              Channel.empty(),
              ^^^^^^^
  ```

- Warning: `workflows/rnadnavar/main.nf:241:34`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
          realigned_filtered_maf = Channel.empty()
                                   ^^^^^^^
  ```

- Warning: `workflows/rnadnavar/main.nf:247:18`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
              dna: it[0].status < 2
                   ^^
  ```

- Warning: `workflows/rnadnavar/main.nf:248:18`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
              rna: it[0].status >= 2
                   ^^
  ```

- Warning: `workflows/rnadnavar/main.nf:251:18`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
              dna: it[0].status < 2
                   ^^
  ```

- Warning: `workflows/rnadnavar/main.nf:252:18`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
              rna: it[0].status >= 2
                   ^^
  ```

- Warning: `workflows/rnadnavar/main.nf:262:20`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      version_yaml = Channel.empty()
                     ^^^^^^^
  ```

- Warning: `workflows/rnadnavar/main.nf:269:29`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
          ch_multiqc_config = Channel.fromPath("${projectDir}/assets/multiqc_config.yml", checkIfExists: true)
                              ^^^^^^^
  ```

- Warning: `workflows/rnadnavar/main.nf:270:60`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
          ch_multiqc_custom_config = params.multiqc_config ? Channel.fromPath(params.multiqc_config, checkIfExists: true) : Channel.empty()
                                                             ^^^^^^^
  ```

- Warning: `workflows/rnadnavar/main.nf:270:123`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
          ch_multiqc_custom_config = params.multiqc_config ? Channel.fromPath(params.multiqc_config, checkIfExists: true) : Channel.empty()
                                                                                                                            ^^^^^^^
  ```

- Warning: `workflows/rnadnavar/main.nf:271:49`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
          ch_multiqc_logo = params.multiqc_logo ? Channel.fromPath(params.multiqc_logo, checkIfExists: true) : Channel.empty()
                                                  ^^^^^^^
  ```

- Warning: `workflows/rnadnavar/main.nf:271:110`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
          ch_multiqc_logo = params.multiqc_logo ? Channel.fromPath(params.multiqc_logo, checkIfExists: true) : Channel.empty()
                                                                                                               ^^^^^^^
  ```

- Warning: `workflows/rnadnavar/main.nf:273:31`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
          ch_workflow_summary = Channel.value(paramsSummaryMultiqc(summary_params))
                                ^^^^^^^
  ```

- Warning: `workflows/rnadnavar/main.nf:275:34`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
          ch_methods_description = Channel.value(methodsDescriptionText(ch_multiqc_custom_methods_description))
                                   ^^^^^^^
  ```

- Warning: `workflows/rnadnavar/main.nf:310:72`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          def InputStream gzipStream = new java.util.zip.GZIPInputStream(it)
                                                                         ^^
  ```
