# Nextflow lint results

- Generated: 2026-01-16T06:36:03.374362214Z
- Nextflow version: 25.12.0-edge
- Summary: 44 errors, 30 warnings

## :x: Errors

- Error: `conf/base.config:14:16`: `check_max` is not defined

  ```nextflow
      cpus   = { check_max( 1    * task.attempt, 'cpus'   ) }
                 ^^^^^^^^^
  ```

- Error: `conf/base.config:15:16`: `check_max` is not defined

  ```nextflow
      memory = { check_max( 6.GB * task.attempt, 'memory' ) }
                 ^^^^^^^^^
  ```

- Error: `conf/base.config:16:16`: `check_max` is not defined

  ```nextflow
      time   = { check_max( 4.h  * task.attempt, 'time'   ) }
                 ^^^^^^^^^
  ```

- Error: `conf/base.config:30:20`: `check_max` is not defined

  ```nextflow
          cpus   = { check_max( 1                  , 'cpus'    ) }
                     ^^^^^^^^^
  ```

- Error: `conf/base.config:31:20`: `check_max` is not defined

  ```nextflow
          memory = { check_max( 6.GB * task.attempt, 'memory'  ) }
                     ^^^^^^^^^
  ```

- Error: `conf/base.config:32:20`: `check_max` is not defined

  ```nextflow
          time   = { check_max( 4.h  * task.attempt, 'time'    ) }
                     ^^^^^^^^^
  ```

- Error: `conf/base.config:35:20`: `check_max` is not defined

  ```nextflow
          cpus   = { check_max( 2     * task.attempt, 'cpus'    ) }
                     ^^^^^^^^^
  ```

- Error: `conf/base.config:36:20`: `check_max` is not defined

  ```nextflow
          memory = { check_max( 12.GB * task.attempt, 'memory'  ) }
                     ^^^^^^^^^
  ```

- Error: `conf/base.config:37:20`: `check_max` is not defined

  ```nextflow
          time   = { check_max( 4.h   * task.attempt, 'time'    ) }
                     ^^^^^^^^^
  ```

- Error: `conf/base.config:40:20`: `check_max` is not defined

  ```nextflow
          cpus   = { check_max( 6     * task.attempt, 'cpus'    ) }
                     ^^^^^^^^^
  ```

- Error: `conf/base.config:41:20`: `check_max` is not defined

  ```nextflow
          memory = { check_max( 36.GB * task.attempt, 'memory'  ) }
                     ^^^^^^^^^
  ```

- Error: `conf/base.config:42:20`: `check_max` is not defined

  ```nextflow
          time   = { check_max( 8.h   * task.attempt, 'time'    ) }
                     ^^^^^^^^^
  ```

- Error: `conf/base.config:45:20`: `check_max` is not defined

  ```nextflow
          cpus   = { check_max( 12    * task.attempt, 'cpus'    ) }
                     ^^^^^^^^^
  ```

- Error: `conf/base.config:46:20`: `check_max` is not defined

  ```nextflow
          memory = { check_max( 72.GB * task.attempt, 'memory'  ) }
                     ^^^^^^^^^
  ```

- Error: `conf/base.config:47:20`: `check_max` is not defined

  ```nextflow
          time   = { check_max( 16.h  * task.attempt, 'time'    ) }
                     ^^^^^^^^^
  ```

- Error: `conf/base.config:50:20`: `check_max` is not defined

  ```nextflow
          time   = { check_max( 20.h  * task.attempt, 'time'    ) }
                     ^^^^^^^^^
  ```

- Error: `conf/base.config:53:20`: `check_max` is not defined

  ```nextflow
          memory = { check_max( 200.GB * task.attempt, 'memory' ) }
                     ^^^^^^^^^
  ```

- Error: `main.nf:30:1`: Statements cannot be mixed with script declarations -- move statements into a process, workflow, or function

  ```nextflow
  if (params.help) {
  ^
  ```

- Error: `main.nf:31:16`: `NfcoreTemplate` is not defined

  ```nextflow
      def logo = NfcoreTemplate.logo(workflow, params.monochrome_logs)
                 ^^^^^^^^^^^^^^
  ```

- Error: `main.nf:32:27`: `WorkflowMain` is not defined

  ```nextflow
      def citation = '\n' + WorkflowMain.citation(workflow) + '\n'
                            ^^^^^^^^^^^^
  ```

- Error: `main.nf:34:54`: `NfcoreTemplate` is not defined

  ```nextflow
      log.info logo + paramsHelp(command) + citation + NfcoreTemplate.dashedLine(params.monochrome_logs)
                                                       ^^^^^^^^^^^^^^
  ```

- Error: `main.nf:43:1`: Statements cannot be mixed with script declarations -- move statements into a process, workflow, or function

  ```nextflow
  WorkflowMain.initialise(workflow, params, log, args)
  ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  ```

- Error: `main.nf:43:1`: `WorkflowMain` is not defined

  ```nextflow
  WorkflowMain.initialise(workflow, params, log, args)
  ^^^^^^^^^^^^
  ```

- Error: `modules/nf-core/multiqc/main.nf:28:31`: Unexpected input: '/'

  ```nextflow
      def logo = multiqc_logo ? /--cl-config 'custom_logo: "${multiqc_logo}"'/ : ''
                                ^
  ```

- Error: `nextflow.config:71:5`: Unexpected input: 'includeConfig'

  ```nextflow
      includeConfig "${params.custom_config_base}/nfcore_custom.config"
      ^
  ```

- Error: `subworkflows/local/mmap.nf:21:21`: Unexpected input: '->'

  ```nextflow
          .map ( gene -> gene.trim() )
                      ^
  ```

- Error: `workflows/omicsgenetraitassociation.nf:9:1`: Statements cannot be mixed with script declarations -- move statements into a process, workflow, or function

  ```nextflow
  def logo = NfcoreTemplate.logo(workflow, params.monochrome_logs)
  ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  ```

- Error: `workflows/omicsgenetraitassociation.nf:9:12`: `NfcoreTemplate` is not defined

  ```nextflow
  def logo = NfcoreTemplate.logo(workflow, params.monochrome_logs)
             ^^^^^^^^^^^^^^
  ```

- Error: `workflows/omicsgenetraitassociation.nf:10:1`: Statements cannot be mixed with script declarations -- move statements into a process, workflow, or function

  ```nextflow
  def citation = '\n' + WorkflowMain.citation(workflow) + '\n'
  ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  ```

- Error: `workflows/omicsgenetraitassociation.nf:10:23`: `WorkflowMain` is not defined

  ```nextflow
  def citation = '\n' + WorkflowMain.citation(workflow) + '\n'
                        ^^^^^^^^^^^^
  ```

- Error: `workflows/omicsgenetraitassociation.nf:11:1`: Statements cannot be mixed with script declarations -- move statements into a process, workflow, or function

  ```nextflow
  def summary_params = paramsSummaryMap(workflow)
  ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  ```

- Error: `workflows/omicsgenetraitassociation.nf:14:1`: Statements cannot be mixed with script declarations -- move statements into a process, workflow, or function

  ```nextflow
  log.info logo + paramsSummaryLog(workflow) + citation
  ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  ```

- Error: `workflows/omicsgenetraitassociation.nf:16:1`: Statements cannot be mixed with script declarations -- move statements into a process, workflow, or function

  ```nextflow
  WorkflowOmicsgenetraitassociation.initialise(params, log)
  ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  ```

- Error: `workflows/omicsgenetraitassociation.nf:16:1`: `WorkflowOmicsgenetraitassociation` is not defined

  ```nextflow
  WorkflowOmicsgenetraitassociation.initialise(params, log)
  ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  ```

- Error: `workflows/omicsgenetraitassociation.nf:52:1`: Module could not be parsed: '/home/runner/work/strict-syntax-health/strict-syntax-health/pipelines/omicsgenetraitassociation/subworkflows/local/mmap.nf'

  ```nextflow
  include { MMAP_SUBWORKFLOW }            from '../subworkflows/local/mmap'
  ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  ```

- Error: `workflows/omicsgenetraitassociation.nf:120:5`: `MMAP_SUBWORKFLOW` is not defined

  ```nextflow
      MMAP_SUBWORKFLOW (
      ^^^^^^^^^^^^^^^^
  ```

- Error: `workflows/omicsgenetraitassociation.nf:127:22`: `MMAP_SUBWORKFLOW` is not defined

  ```nextflow
      ch_mmap_parsed = MMAP_SUBWORKFLOW.out.parsed_mmap_output
                       ^^^^^^^^^^^^^^^^
  ```

- Error: `workflows/omicsgenetraitassociation.nf:128:26`: `MMAP_SUBWORKFLOW` is not defined

  ```nextflow
      ch_mmap_cma_format = MMAP_SUBWORKFLOW.out.cma_format_output
                           ^^^^^^^^^^^^^^^^
  ```

- Error: `workflows/omicsgenetraitassociation.nf:129:35`: `MMAP_SUBWORKFLOW` is not defined

  ```nextflow
      ch_versions = ch_versions.mix(MMAP_SUBWORKFLOW.out.versions)
                                    ^^^^^^^^^^^^^^^^
  ```

- Error: `workflows/omicsgenetraitassociation.nf:248:1`: Statements cannot be mixed with script declarations -- move statements into a process, workflow, or function

  ```nextflow
  workflow.onComplete {
  ^
  ```

- Error: `workflows/omicsgenetraitassociation.nf:250:9`: `NfcoreTemplate` is not defined

  ```nextflow
          NfcoreTemplate.email(workflow, params, summary_params, projectDir, log)
          ^^^^^^^^^^^^^^
  ```

- Error: `workflows/omicsgenetraitassociation.nf:252:5`: `NfcoreTemplate` is not defined

  ```nextflow
      NfcoreTemplate.dump_parameters(workflow, params)
      ^^^^^^^^^^^^^^
  ```

- Error: `workflows/omicsgenetraitassociation.nf:253:5`: `NfcoreTemplate` is not defined

  ```nextflow
      NfcoreTemplate.summary(workflow, params, log)
      ^^^^^^^^^^^^^^
  ```

- Error: `workflows/omicsgenetraitassociation.nf:255:9`: `NfcoreTemplate` is not defined

  ```nextflow
          NfcoreTemplate.IM_notification(workflow, params, summary_params, projectDir, log)
          ^^^^^^^^^^^^^^
  ```

## :warning: Warnings

- Warning: `modules/local/cma/cma/main.nf:24:9`: Variable was declared but not used

  ```nextflow
      def args = task.ext.args ?: ''
          ^^^^
  ```

- Warning: `modules/local/cma/format_cma_input/main.nf:26:9`: Variable was declared but not used

  ```nextflow
      def args = task.ext.args ?: ''
          ^^^^
  ```

- Warning: `modules/local/mea/go_analysis/main.nf:21:9`: Variable was declared but not used

  ```nextflow
      def args = task.ext.args ?: ''
          ^^^^
  ```

- Warning: `modules/local/mea/merge_ora_and_summary/main.nf:25:9`: Variable was declared but not used

  ```nextflow
      def args = task.ext.args ?: ''
          ^^^^
  ```

- Warning: `modules/local/mea/pascal/main.nf:20:9`: Variable was declared but not used

  ```nextflow
      def args = task.ext.args ?: ''
          ^^^^
  ```

- Warning: `modules/local/mea/postprocess/main.nf:28:9`: Variable was declared but not used

  ```nextflow
      def args = task.ext.args ?: ''
          ^^^^
  ```

- Warning: `modules/local/mea/preprocess/main.nf:24:9`: Variable was declared but not used

  ```nextflow
      def args = task.ext.args ?: ''
          ^^^^
  ```

- Warning: `modules/local/mmap/mmap/main.nf:23:9`: Variable was declared but not used

  ```nextflow
      def args = task.ext.args ?: ''
          ^^^^
  ```

- Warning: `modules/local/mmap/mmap_parse/main.nf:21:9`: Variable was declared but not used

  ```nextflow
      def args = task.ext.args ?: ''
          ^^^^
  ```

- Warning: `modules/local/pascal/main.nf:22:9`: Variable was declared but not used

  ```nextflow
      def args = task.ext.args ?: ''
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

- Warning: `subworkflows/local/cma.nf:15:19`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_versions = Channel.empty()
                    ^^^^^^^
  ```

- Warning: `subworkflows/local/cma.nf:16:15`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_pval = Channel.empty()
                ^^^^^^^
  ```

- Warning: `subworkflows/local/cma.nf:17:20`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_tetrachor = Channel.empty()
                     ^^^^^^^
  ```

- Warning: `subworkflows/local/cma.nf:20:23`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
          input_files = Channel.fromPath("${params.cma_two_traits}/*.csv").toList()
                        ^^^^^^^
  ```

- Warning: `subworkflows/local/input_check.nf:15:37`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          .map { create_fastq_channel(it) }
                                      ^^
  ```

- Warning: `subworkflows/local/pascal.nf:14:31`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_versions             = Channel.empty()
                                ^^^^^^^
  ```

- Warning: `subworkflows/local/pascal.nf:15:31`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_pascal_out           = Channel.empty()
                                ^^^^^^^
  ```

- Warning: `subworkflows/local/pascal.nf:21:16`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          .map { meta, file -> file}
                 ^^^^
  ```

- Warning: `workflows/omicsgenetraitassociation.nf:79:19`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_versions = Channel.empty()
                    ^^^^^^^
  ```

- Warning: `workflows/omicsgenetraitassociation.nf:80:31`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_mea_preprocess_input = Channel.empty()
                                ^^^^^^^
  ```

- Warning: `workflows/omicsgenetraitassociation.nf:86:5`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      Channel.fromSamplesheet("input")
      ^^^^^^^
  ```

- Warning: `workflows/omicsgenetraitassociation.nf:111:5`: Variable was declared but not used

  ```nextflow
      ch_pascal_output = PASCAL_SUBWORKFLOW.out.pascal_output
      ^^^^^^^^^^^^^^^^
  ```

- Warning: `workflows/omicsgenetraitassociation.nf:127:5`: Variable was declared but not used

  ```nextflow
      ch_mmap_parsed = MMAP_SUBWORKFLOW.out.parsed_mmap_output
      ^^^^^^^^^^^^^^
  ```

- Warning: `workflows/omicsgenetraitassociation.nf:160:23`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_module_files = Channel.fromPath("${params.module_file_dir}/*.txt")
                        ^^^^^^^
  ```

- Warning: `workflows/omicsgenetraitassociation.nf:225:5`: Variable was declared but not used

  ```nextflow
      ch_merge_summary_dir = MERGE_ORA_AND_SUMMARY.out.summary_dir
      ^^^^^^^^^^^^^^^^^^^^
  ```

- Warning: `workflows/omicsgenetraitassociation.nf:227:5`: Variable was declared but not used

  ```nextflow
      ch_merge_meta = MERGE_ORA_AND_SUMMARY.out.meta
      ^^^^^^^^^^^^^
  ```

- Warning: `workflows/omicsgenetraitassociation.nf:228:5`: Variable was declared but not used

  ```nextflow
      ch_merge_trait = MERGE_ORA_AND_SUMMARY.out.trait
      ^^^^^^^^^^^^^^
  ```

- Warning: `workflows/omicsgenetraitassociation.nf:233:5`: Variable was declared but not used

  ```nextflow
      ch_master_summary = ch_merge_summary_files
      ^^^^^^^^^^^^^^^^^
  ```
