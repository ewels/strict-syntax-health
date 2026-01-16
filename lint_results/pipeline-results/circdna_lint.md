# Nextflow lint results

- Generated: 2026-01-16T06:29:25.577827150Z
- Nextflow version: 25.12.0-edge
- Summary: 38 errors, 30 warnings

## :x: Errors

- Error: `conf/base.config:13:16`: `check_max` is not defined

  ```nextflow
      cpus   = { check_max( 1    * task.attempt, 'cpus'   ) }
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

- Error: `conf/base.config:28:20`: `check_max` is not defined

  ```nextflow
          cpus   = { check_max( 1                  , 'cpus'    ) }
                     ^^^^^^^^^
  ```

- Error: `conf/base.config:29:20`: `check_max` is not defined

  ```nextflow
          memory = { check_max( 6.GB * task.attempt, 'memory'  ) }
                     ^^^^^^^^^
  ```

- Error: `conf/base.config:30:20`: `check_max` is not defined

  ```nextflow
          time   = { check_max( 4.h  * task.attempt, 'time'    ) }
                     ^^^^^^^^^
  ```

- Error: `conf/base.config:33:20`: `check_max` is not defined

  ```nextflow
          cpus   = { check_max( 2     * task.attempt, 'cpus'    ) }
                     ^^^^^^^^^
  ```

- Error: `conf/base.config:34:20`: `check_max` is not defined

  ```nextflow
          memory = { check_max( 12.GB * task.attempt, 'memory'  ) }
                     ^^^^^^^^^
  ```

- Error: `conf/base.config:35:20`: `check_max` is not defined

  ```nextflow
          time   = { check_max( 4.h   * task.attempt, 'time'    ) }
                     ^^^^^^^^^
  ```

- Error: `conf/base.config:38:20`: `check_max` is not defined

  ```nextflow
          cpus   = { check_max( 6     * task.attempt, 'cpus'    ) }
                     ^^^^^^^^^
  ```

- Error: `conf/base.config:39:20`: `check_max` is not defined

  ```nextflow
          memory = { check_max( 36.GB * task.attempt, 'memory'  ) }
                     ^^^^^^^^^
  ```

- Error: `conf/base.config:40:20`: `check_max` is not defined

  ```nextflow
          time   = { check_max( 8.h   * task.attempt, 'time'    ) }
                     ^^^^^^^^^
  ```

- Error: `conf/base.config:43:20`: `check_max` is not defined

  ```nextflow
          cpus   = { check_max( 12    * task.attempt, 'cpus'    ) }
                     ^^^^^^^^^
  ```

- Error: `conf/base.config:44:20`: `check_max` is not defined

  ```nextflow
          memory = { check_max( 72.GB * task.attempt, 'memory'  ) }
                     ^^^^^^^^^
  ```

- Error: `conf/base.config:45:20`: `check_max` is not defined

  ```nextflow
          time   = { check_max( 16.h  * task.attempt, 'time'    ) }
                     ^^^^^^^^^
  ```

- Error: `conf/base.config:48:20`: `check_max` is not defined

  ```nextflow
          time   = { check_max( 20.h  * task.attempt, 'time'    ) }
                     ^^^^^^^^^
  ```

- Error: `conf/base.config:52:20`: `check_max` is not defined

  ```nextflow
          time   = { check_max( max_time, 'time'    ) }
                     ^^^^^^^^^
  ```

- Error: `conf/base.config:56:20`: `check_max` is not defined

  ```nextflow
          memory = { check_max( 200.GB * task.attempt, 'memory' ) }
                     ^^^^^^^^^
  ```

- Error: `conf/base.config:59:20`: `check_max` is not defined

  ```nextflow
          cpus   = { check_max( params.max_cpus, 'cpus'    ) }
                     ^^^^^^^^^
  ```

- Error: `conf/base.config:60:20`: `check_max` is not defined

  ```nextflow
          memory = { check_max( params.max_memory, 'memory'  ) }
                     ^^^^^^^^^
  ```

- Error: `conf/base.config:61:20`: `check_max` is not defined

  ```nextflow
          time   = { check_max( max_time, 'time'    ) }
                     ^^^^^^^^^
  ```

- Error: `conf/modules.config:73:1`: If statements cannot be mixed with config statements

  ```nextflow
  if(!params.skip_qc) {
  ^
  ```

- Error: `conf/modules.config:515:1`: If statements cannot be mixed with config statements

  ```nextflow
  if (!params.skip_multiqc) {
  ^
  ```

- Error: `main.nf:22:16`: `WorkflowMain` is not defined

  ```nextflow
  params.fasta = WorkflowMain.getGenomeAttribute(params, 'fasta')
                 ^^^^^^^^^^^^
  ```

- Error: `main.nf:33:1`: Statements cannot be mixed with script declarations -- move statements into a process, workflow, or function

  ```nextflow
  if (params.help) {
  ^
  ```

- Error: `main.nf:34:16`: `NfcoreTemplate` is not defined

  ```nextflow
      def logo = NfcoreTemplate.logo(workflow, params.monochrome_logs)
                 ^^^^^^^^^^^^^^
  ```

- Error: `main.nf:35:27`: `WorkflowMain` is not defined

  ```nextflow
      def citation = '\n' + WorkflowMain.citation(workflow) + '\n'
                            ^^^^^^^^^^^^
  ```

- Error: `main.nf:37:54`: `NfcoreTemplate` is not defined

  ```nextflow
      log.info logo + paramsHelp(command) + citation + NfcoreTemplate.dashedLine(params.monochrome_logs)
                                                       ^^^^^^^^^^^^^^
  ```

- Error: `main.nf:42:1`: Statements cannot be mixed with script declarations -- move statements into a process, workflow, or function

  ```nextflow
  if (params.validate_params) {
  ^
  ```

- Error: `main.nf:46:1`: Statements cannot be mixed with script declarations -- move statements into a process, workflow, or function

  ```nextflow
  WorkflowMain.initialise(workflow, params, log, args)
  ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  ```

- Error: `main.nf:46:1`: `WorkflowMain` is not defined

  ```nextflow
  WorkflowMain.initialise(workflow, params, log, args)
  ^^^^^^^^^^^^
  ```

- Error: `main.nf:54:1`: Module could not be parsed: '/home/runner/work/strict-syntax-health/strict-syntax-health/pipelines/circdna/workflows/circdna.nf'

  ```nextflow
  include { CIRCDNA } from './workflows/circdna'
  ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  ```

- Error: `main.nf:60:5`: `CIRCDNA` is not defined

  ```nextflow
      CIRCDNA ()
      ^^^^^^^
  ```

- Error: `modules/local/circexplorer2/parse.nf:6:5`: Invalid process directive

  ```nextflow
      if (workflow.containerEngine == 'singularity' && !params.singularity_pull_docker_container) {
      ^
  ```

- Error: `modules/nf-core/bwa/index/main.nf:14:27`: `bwa` is not defined

  ```nextflow
      tuple val(meta), path(bwa) , emit: index
                            ^^^
  ```

- Error: `modules/nf-core/samtools/view/main.nf:64:9`: `index` is already declared

  ```nextflow
      def index = args.contains("--write-index") ? "touch ${prefix}.csi" : ""
          ^^^^^
  ```

- Error: `nextflow.config:109:5`: Unexpected input: 'includeConfig'

  ```nextflow
      includeConfig "${params.custom_config_base}/nfcore_custom.config"
      ^
  ```

- Error: `workflows/circdna.nf:329:21`: Unexpected input: 'map'

  ```nextflow
                      map { meta, bam, bai -> [meta, bam, bai] },
                      ^
  ```

## :warning: Warnings

- Warning: `modules/local/ampliconsuite/ampliconsuite.nf:34:9`: Variable was declared but not used

  ```nextflow
      def cngain = params.aa_cngain
          ^^^^^^
  ```

- Warning: `modules/local/ampliconsuite/ampliconsuite.nf:65:9`: Variable was declared but not used

  ```nextflow
      def args = task.ext.args ?: ''
          ^^^^
  ```

- Warning: `modules/local/ampliconsuite/ampliconsuite.nf:67:9`: Variable was declared but not used

  ```nextflow
      def cngain = params.aa_cngain
          ^^^^^^
  ```

- Warning: `modules/local/ampliconsuite/ampliconsuite.nf:68:9`: Variable was declared but not used

  ```nextflow
      def ref = params.reference_build
          ^^^
  ```

- Warning: `modules/local/bwa/mem/main.nf:45:9`: Variable was declared but not used

  ```nextflow
      def args = task.ext.args ?: ''
          ^^^^
  ```

- Warning: `modules/local/bwa/mem/main.nf:46:9`: Variable was declared but not used

  ```nextflow
      def args2 = task.ext.args2 ?: ''
          ^^^^^
  ```

- Warning: `modules/local/bwa/mem/main.nf:48:9`: Variable was declared but not used

  ```nextflow
      def samtools_command = sort_bam ? 'sort' : 'view'
          ^^^^^^^^^^^^^^^^
  ```

- Warning: `modules/local/circlefinder.nf:16:9`: Variable was declared but not used

  ```nextflow
      def args = task.ext.args ?: ''
          ^^^^
  ```

- Warning: `modules/local/circlemap/readextractor.nf:18:9`: Variable was declared but not used

  ```nextflow
      def args = task.ext.args ?: ''
          ^^^^
  ```

- Warning: `modules/local/cnvkit/batch/main.nf:47:9`: Variable was declared but not used

  ```nextflow
      def args = task.ext.args ?: ''
          ^^^^
  ```

- Warning: `modules/local/cnvkit/batch/main.nf:49:9`: Variable was declared but not used

  ```nextflow
      def fasta_args = cnn ? "" : "--fasta $fasta"
          ^^^^^^^^^^
  ```

- Warning: `modules/local/cnvkit/batch/main.nf:50:9`: Variable was declared but not used

  ```nextflow
      def reference_args = cnn ? "--reference $cnn" : ""
          ^^^^^^^^^^^^^^
  ```

- Warning: `modules/local/cnvkit/segment.nf:18:9`: Variable was declared but not used

  ```nextflow
      def args = task.ext.args ?: ''
          ^^^^
  ```

- Warning: `modules/local/cnvkit/segment.nf:35:9`: Variable was declared but not used

  ```nextflow
      def args = task.ext.args ?: ''
          ^^^^
  ```

- Warning: `modules/local/getcircularreads.nf:15:9`: Variable was declared but not used

  ```nextflow
      def args = task.ext.args ?: ''
          ^^^^
  ```

- Warning: `modules/local/samtools/flagstat/main.nf:21:9`: Variable was declared but not used

  ```nextflow
      def args = task.ext.args ?: ''
          ^^^^
  ```

- Warning: `modules/local/samtools/idxstats/main.nf:21:9`: Variable was declared but not used

  ```nextflow
      def args = task.ext.args ?: ''
          ^^^^
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

- Warning: `modules/nf-core/fastqc/main.nf:27:48`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
      def renamed_files = old_new_pairs.collect{ old_name, new_name -> new_name }.join(' ')
                                                 ^^^^^^^^
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

- Warning: `subworkflows/local/input_check.nf:16:42`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
              .map { create_fastq_channels(it) }
                                           ^^
  ```

- Warning: `subworkflows/local/input_check.nf:22:40`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
              .map { create_bam_channels(it) }
                                         ^^
  ```

- Warning: `subworkflows/nf-core/bam_markduplicates_picard/main.nf:18:19`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_versions = Channel.empty()
                    ^^^^^^^
  ```

- Warning: `subworkflows/nf-core/bam_stats_samtools/main.nf:15:19`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_versions = Channel.empty()
                    ^^^^^^^
  ```
