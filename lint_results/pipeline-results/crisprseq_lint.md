# Nextflow lint results

- Generated: 2026-01-16T06:30:05.765399652Z
- Nextflow version: 25.12.0-edge
- Summary: 13 errors, 45 warnings

## :x: Errors

- Error: `main.nf:36:1`: Module could not be parsed: '/home/runner/work/strict-syntax-health/strict-syntax-health/pipelines/crisprseq/workflows/crisprseq_targeted.nf'

  ```nextflow
  include { CRISPRSEQ_TARGETED  } from './workflows/crisprseq_targeted'
  ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  ```

- Error: `main.nf:56:9`: `CRISPRSEQ_TARGETED` is not defined

  ```nextflow
          CRISPRSEQ_TARGETED (
          ^^^^^^^^^^^^^^^^^^
  ```

- Error: `main.nf:62:29`: `CRISPRSEQ_TARGETED` is not defined

  ```nextflow
          multiqc_report_ch = CRISPRSEQ_TARGETED.out.multiqc_report
                              ^^^^^^^^^^^^^^^^^^
  ```

- Error: `modules/nf-core/bwa/index/main.nf:14:27`: `bwa` is not defined

  ```nextflow
      tuple val(meta), path(bwa) , emit: index
                            ^^^
  ```

- Error: `modules/nf-core/vsearch/sort/main.nf:40:13`: `prefix` is not defined

  ```nextflow
      touch ${prefix}.fasta
              ^^^^^^
  ```

- Error: `subworkflows/local/utils_nfcore_crisprseq_pipeline/main.nf:115:41`: `reference` is already declared

  ```nextflow
                  meta, fastq_1, fastq_2, reference, protospacer, template ->
                                          ^^^^^^^^^
  ```

- Error: `subworkflows/local/utils_nfcore_crisprseq_pipeline/main.nf:115:52`: `protospacer` is already declared

  ```nextflow
                  meta, fastq_1, fastq_2, reference, protospacer, template ->
                                                     ^^^^^^^^^^^
  ```

- Error: `subworkflows/local/utils_nfcore_crisprseq_pipeline/main.nf:115:65`: `template` is already declared

  ```nextflow
                  meta, fastq_1, fastq_2, reference, protospacer, template ->
                                                                  ^^^^^^^^
  ```

- Error: `subworkflows/local/utils_nfcore_crisprseq_pipeline/main.nf:117:25`: Variables in a closure should be declared with `def`

  ```nextflow
                          files = [ fastq_1, fastq_2 ]
                          ^^^^^
  ```

- Error: `subworkflows/local/utils_nfcore_crisprseq_pipeline/main.nf:501:9`: `warning` is not defined

  ```nextflow
          warning "mle_design_matrix will only be used for the MAGeCK MLE computations"
          ^^^^^^^
  ```

- Error: `subworkflows/local/utils_nfcore_crisprseq_pipeline/main.nf:513:9`: `warning` is not defined

  ```nextflow
          warning "MAGeCK MLE module will be run twice, once with the design matrix and once with day0-label"
          ^^^^^^^
  ```

- Error: `subworkflows/local/utils_nfcore_crisprseq_pipeline/main.nf:517:9`: `warning` is not defined

  ```nextflow
          warning "mle_design_matrix will only be used for the MAGeCK MLE computations"
          ^^^^^^^
  ```

- Error: `workflows/crisprseq_targeted.nf:61:22`: Unexpected input: '='

  ```nextflow
          while ( line1=it.readLine() ) {
                       ^
  ```

## :warning: Warnings

- Warning: `modules/local/bagel2/bf.nf:26:9`: Variable was declared but not used

  ```nextflow
      def prefix = task.ext.prefix ?: "${meta.id}"
          ^^^^^^
  ```

- Warning: `modules/local/bagel2/fc.nf:23:9`: Variable was declared but not used

  ```nextflow
      def prefix = task.ext.prefix ?: "${meta.id}"
          ^^^^^^
  ```

- Warning: `modules/local/bagel2/graph.nf:21:9`: Variable was declared but not used

  ```nextflow
      def args = task.ext.args ?: ''
          ^^^^
  ```

- Warning: `modules/local/bagel2/graph.nf:22:9`: Variable was declared but not used

  ```nextflow
      def prefix = task.ext.prefix ?: "${meta.id}"
          ^^^^^^
  ```

- Warning: `modules/local/bagel2/pr.nf:23:9`: Variable was declared but not used

  ```nextflow
      def prefix = task.ext.prefix ?: "${meta.id}"
          ^^^^^^
  ```

- Warning: `modules/local/extract_umis.nf:19:9`: Variable was declared but not used

  ```nextflow
      def args = task.ext.args ?: ''
          ^^^^
  ```

- Warning: `modules/local/find_adapters.nf:18:9`: Variable was declared but not used

  ```nextflow
      def args = task.ext.args ?: ''
          ^^^^
  ```

- Warning: `modules/local/hitselection.nf:26:9`: Variable was declared but not used

  ```nextflow
      def args = task.ext.args ?: ''
          ^^^^
  ```

- Warning: `modules/local/hitselection.nf:246:9`: Variable was declared but not used

  ```nextflow
      def args = task.ext.args ?: ''
          ^^^^
  ```

- Warning: `modules/local/mageck/flutemle.nf:25:5`: Variable was declared but not used

  ```nextflow
      args = task.ext.args ?: ' '
      ^^^^
  ```

- Warning: `modules/local/mageck/graphrra.nf:21:9`: Variable was declared but not used

  ```nextflow
      def args = task.ext.args ?: ''
          ^^^^
  ```

- Warning: `modules/local/orient_reference.nf:19:9`: Variable was declared but not used

  ```nextflow
      def args = task.ext.args ?: ''
          ^^^^
  ```

- Warning: `modules/local/venndiagram.nf:21:9`: Variable was declared but not used

  ```nextflow
      def args = task.ext.args ?: ''
          ^^^^
  ```

- Warning: `modules/nf-core/bowtie2/align/main.nf:93:9`: Variable was declared but not used

  ```nextflow
      def reference = fasta && extension=="cram"  ? "--reference ${fasta}" : ""
          ^^^^^^^^^
  ```

- Warning: `modules/nf-core/bwa/mem/main.nf:56:9`: Variable was declared but not used

  ```nextflow
      def args = task.ext.args ?: ''
          ^^^^
  ```

- Warning: `modules/nf-core/bwa/mem/main.nf:59:9`: Variable was declared but not used

  ```nextflow
      def samtools_command = sort_bam ? 'sort' : 'view'
          ^^^^^^^^^^^^^^^^
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

- Warning: `modules/nf-core/crisprcleanr/normalize/main.nf:26:9`: Variable was declared but not used

  ```nextflow
      def args = task.ext.args ?: ''
          ^^^^
  ```

- Warning: `modules/nf-core/mageck/count/main.nf:53:9`: Variable was declared but not used

  ```nextflow
      def args = task.ext.args ?: ''
          ^^^^
  ```

- Warning: `modules/nf-core/mageck/count/main.nf:55:9`: Variable was declared but not used

  ```nextflow
      def sample_label = ("$fastq1".endsWith(".fastq.gz") || "$fastq1".endsWith(".fq.gz")) ? "--sample-label ${meta.id}" : ''
          ^^^^^^^^^^^^
  ```

- Warning: `modules/nf-core/mageck/test/main.nf:42:9`: Variable was declared but not used

  ```nextflow
      def args = task.ext.args ?: ''
          ^^^^
  ```

- Warning: `subworkflows/local/utils_nfcore_crisprseq_pipeline/main.nf:32:5`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
      monochrome_logs   // boolean: Do not use coloured log outputs
      ^^^^^^^^^^^^^^^
  ```

- Warning: `subworkflows/local/utils_nfcore_crisprseq_pipeline/main.nf:35:5`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
      input             //  string: Path to input samplesheet
      ^^^^^
  ```

- Warning: `subworkflows/local/utils_nfcore_crisprseq_pipeline/main.nf:101:5`: Variable was declared but not used

  ```nextflow
      reads_screening  = channel.empty()
      ^^^^^^^^^^^^^^^
  ```

- Warning: `subworkflows/local/utils_nfcore_crisprseq_pipeline/main.nf:106:5`: Variable was declared but not used

  ```nextflow
      versions         = channel.empty()
      ^^^^^^^^
  ```

- Warning: `subworkflows/local/utils_nfcore_crisprseq_pipeline/main.nf:244:14`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
      .filter{ meta, sequence -> sequence instanceof String }
               ^^^^
  ```

- Warning: `subworkflows/local/utils_nfcore_crisprseq_pipeline/main.nf:252:21`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          .map{ meta, reference ->
                      ^^^^^^^^^
  ```

- Warning: `subworkflows/local/utils_nfcore_crisprseq_pipeline/main.nf:256:11`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
      .map{ metaid, new_file, meta ->
            ^^^^^^
  ```

- Warning: `subworkflows/local/utils_nfcore_crisprseq_pipeline/main.nf:267:14`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
      .filter{ meta, sequence -> sequence instanceof String }
               ^^^^
  ```

- Warning: `subworkflows/local/utils_nfcore_crisprseq_pipeline/main.nf:275:21`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          .map{ meta, template ->
                      ^^^^^^^^
  ```

- Warning: `subworkflows/local/utils_nfcore_crisprseq_pipeline/main.nf:279:11`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
      .map{ metaid, new_file, meta ->
            ^^^^^^
  ```

- Warning: `subworkflows/local/utils_nfcore_crisprseq_pipeline/main.nf:310:25`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
              .map{ meta, fastqs, reference, protospacer -> [ meta, reference, protospacer ]} // Don't add fastqs to the channel
                          ^^^^^^
  ```

- Warning: `subworkflows/local/utils_nfcore_crisprseq_pipeline/main.nf:395:39`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
      def reference_ok = metas.collect{ it.self_reference }.unique().size == 1
                                        ^^
  ```

- Warning: `subworkflows/local/utils_nfcore_crisprseq_pipeline/main.nf:401:38`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
      def template_ok = metas.collect{ it.template }.unique().size == 1
                                       ^^
  ```

- Warning: `workflows/crisprseq_screening.nf:91:72`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          ch_multiqc_files = ch_multiqc_files.mix(FASTQC.out.zip.collect{it[1]})
                                                                         ^^
  ```

- Warning: `workflows/crisprseq_screening.nf:106:89`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
              ch_multiqc_files = ch_multiqc_files.mix(CUTADAPT_FIVE_PRIME.out.log.collect{it[1]})
                                                                                          ^^
  ```

- Warning: `workflows/crisprseq_screening.nf:115:90`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
              ch_multiqc_files = ch_multiqc_files.mix(CUTADAPT_THREE_PRIME.out.log.collect{it[1]})
                                                                                           ^^
  ```

- Warning: `workflows/crisprseq_screening.nf:196:82`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          ch_multiqc_files = ch_multiqc_files.mix(MAGECK_COUNT.out.summary.collect{it[1]})
                                                                                   ^^
  ```

- Warning: `workflows/crisprseq_screening.nf:242:68`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
              .map { condition, metas -> [condition, metas.collect { it.id }]}
                                                                     ^^
  ```

- Warning: `workflows/crisprseq_screening.nf:261:63`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
                  def treatment_samples = all_conditions.find { it[0] in contrast_meta.treatment }  // Find samples for each condition
                                                                ^^
  ```

- Warning: `workflows/crisprseq_screening.nf:262:63`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
                  def reference_samples = all_conditions.find { it[0] in contrast_meta.reference }
                                                                ^^
  ```

- Warning: `workflows/crisprseq_screening.nf:359:56`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
              MATRICESCREATION(ch_contrasts_counts.map { it[0] })
                                                         ^^
  ```

- Warning: `workflows/crisprseq_screening.nf:543:26`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      def topic_versions = Channel.topic("versions")
                           ^^^^^^^
  ```
