# Nextflow lint results

- Generated: 2026-01-16T06:33:15.916914992Z
- Nextflow version: 25.12.0-edge
- Summary: 52 errors, 14 warnings

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
          cpus   = { check_max( 2     * task.attempt, 'cpus'    ) }
                     ^^^^^^^^^
  ```

- Error: `conf/base.config:29:20`: `check_max` is not defined

  ```nextflow
          memory = { check_max( 12.GB * task.attempt, 'memory'  ) }
                     ^^^^^^^^^
  ```

- Error: `conf/base.config:30:20`: `check_max` is not defined

  ```nextflow
          time   = { check_max( 4.h   * task.attempt, 'time'    ) }
                     ^^^^^^^^^
  ```

- Error: `conf/base.config:33:20`: `check_max` is not defined

  ```nextflow
          cpus   = { check_max( 6     * task.attempt, 'cpus'    ) }
                     ^^^^^^^^^
  ```

- Error: `conf/base.config:34:20`: `check_max` is not defined

  ```nextflow
          memory = { check_max( 36.GB * task.attempt, 'memory'  ) }
                     ^^^^^^^^^
  ```

- Error: `conf/base.config:35:20`: `check_max` is not defined

  ```nextflow
          time   = { check_max( 8.h   * task.attempt, 'time'    ) }
                     ^^^^^^^^^
  ```

- Error: `conf/base.config:38:20`: `check_max` is not defined

  ```nextflow
          cpus   = { check_max( 12    * task.attempt, 'cpus'    ) }
                     ^^^^^^^^^
  ```

- Error: `conf/base.config:39:20`: `check_max` is not defined

  ```nextflow
          memory = { check_max( 72.GB * task.attempt, 'memory'  ) }
                     ^^^^^^^^^
  ```

- Error: `conf/base.config:40:20`: `check_max` is not defined

  ```nextflow
          time   = { check_max( 16.h  * task.attempt, 'time'    ) }
                     ^^^^^^^^^
  ```

- Error: `conf/base.config:43:20`: `check_max` is not defined

  ```nextflow
          time   = { check_max( 20.h  * task.attempt, 'time'    ) }
                     ^^^^^^^^^
  ```

- Error: `conf/base.config:46:20`: `check_max` is not defined

  ```nextflow
          memory = { check_max( 200.GB * task.attempt, 'memory' ) }
                     ^^^^^^^^^
  ```

- Error: `conf/modules.config:58:17`: Unexpected input: ':'

  ```nextflow
          withName: 'ILASTIK' {
                  ^
  ```

- Error: `main.nf:20:1`: Statements cannot be mixed with script declarations -- move statements into a process, workflow, or function

  ```nextflow
  WorkflowMain.initialise(workflow, params, log)
  ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  ```

- Error: `main.nf:20:1`: `WorkflowMain` is not defined

  ```nextflow
  WorkflowMain.initialise(workflow, params, log)
  ^^^^^^^^^^^^
  ```

- Error: `nextflow.config:58:5`: Unexpected input: 'includeConfig'

  ```nextflow
      includeConfig "${params.custom_config_base}/nfcore_custom.config"
      ^
  ```

- Error: `workflows/imcyto.nf:7:1`: Statements cannot be mixed with script declarations -- move statements into a process, workflow, or function

  ```nextflow
  def summary_params = NfcoreSchema.paramsSummaryMap(workflow, params)
  ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  ```

- Error: `workflows/imcyto.nf:7:22`: `NfcoreSchema` is not defined

  ```nextflow
  def summary_params = NfcoreSchema.paramsSummaryMap(workflow, params)
                       ^^^^^^^^^^^^
  ```

- Error: `workflows/imcyto.nf:10:1`: Statements cannot be mixed with script declarations -- move statements into a process, workflow, or function

  ```nextflow
  WorkflowImcyto.initialise(params, log)
  ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  ```

- Error: `workflows/imcyto.nf:10:1`: `WorkflowImcyto` is not defined

  ```nextflow
  WorkflowImcyto.initialise(params, log)
  ^^^^^^^^^^^^^^
  ```

- Error: `workflows/imcyto.nf:13:1`: Statements cannot be mixed with script declarations -- move statements into a process, workflow, or function

  ```nextflow
  def checkPathParamList = [
  ^
  ```

- Error: `workflows/imcyto.nf:23:1`: `for` loops are no longer supported

  ```nextflow
  for (param in checkPathParamList) { if (param) { file(param, checkIfExists: true) } }
  ^^^
  ```

- Error: `workflows/imcyto.nf:23:1`: Statements cannot be mixed with script declarations -- move statements into a process, workflow, or function

  ```nextflow
  for (param in checkPathParamList) { if (param) { file(param, checkIfExists: true) } }
  ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  ```

- Error: `workflows/imcyto.nf:23:6`: `param` is not defined

  ```nextflow
  for (param in checkPathParamList) { if (param) { file(param, checkIfExists: true) } }
       ^^^^^
  ```

- Error: `workflows/imcyto.nf:23:40`: `param` is not defined

  ```nextflow
  for (param in checkPathParamList) { if (param) { file(param, checkIfExists: true) } }
                                         ^^^^^^^
  ```

- Error: `workflows/imcyto.nf:23:55`: `param` is not defined

  ```nextflow
  for (param in checkPathParamList) { if (param) { file(param, checkIfExists: true) } }
                                                        ^^^^^
  ```

- Error: `workflows/imcyto.nf:26:1`: Statements cannot be mixed with script declarations -- move statements into a process, workflow, or function

  ```nextflow
  if (params.input) {
  ^
  ```

- Error: `workflows/imcyto.nf:36:1`: Statements cannot be mixed with script declarations -- move statements into a process, workflow, or function

  ```nextflow
  if (params.metadata)             { ch_metadata             = file(params.metadata)             }
  ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  ```

- Error: `workflows/imcyto.nf:37:1`: Statements cannot be mixed with script declarations -- move statements into a process, workflow, or function

  ```nextflow
  if (params.full_stack_cppipe)    { ch_full_stack_cppipe    = file(params.full_stack_cppipe)    }
  ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  ```

- Error: `workflows/imcyto.nf:38:1`: Statements cannot be mixed with script declarations -- move statements into a process, workflow, or function

  ```nextflow
  if (params.ilastik_stack_cppipe) { ch_ilastik_stack_cppipe = file(params.ilastik_stack_cppipe) }
  ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  ```

- Error: `workflows/imcyto.nf:39:1`: Statements cannot be mixed with script declarations -- move statements into a process, workflow, or function

  ```nextflow
  if (params.segmentation_cppipe)  { ch_segmentation_cppipe  = file(params.segmentation_cppipe)  }
  ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  ```

- Error: `workflows/imcyto.nf:41:1`: Statements cannot be mixed with script declarations -- move statements into a process, workflow, or function

  ```nextflow
  if (!params.skip_ilastik) {
  ^
  ```

- Error: `workflows/imcyto.nf:47:1`: Statements cannot be mixed with script declarations -- move statements into a process, workflow, or function

  ```nextflow
  ch_compensation_tiff = params.compensation_tiff ? file(params.compensation_tiff) : []
  ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  ```

- Error: `workflows/imcyto.nf:50:1`: Statements cannot be mixed with script declarations -- move statements into a process, workflow, or function

  ```nextflow
  ch_plugins_dir = file(params.plugins_dir)
  ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  ```

- Error: `workflows/imcyto.nf:92:9`: `ch_mcd` is not defined

  ```nextflow
          ch_mcd,
          ^^^^^^
  ```

- Error: `workflows/imcyto.nf:93:9`: `ch_metadata` is not defined

  ```nextflow
          ch_metadata
          ^^^^^^^^^^^
  ```

- Error: `workflows/imcyto.nf:103:16`: `WorkflowImcyto` is not defined

  ```nextflow
          .map { WorkflowImcyto.flattenTiff(it) }
                 ^^^^^^^^^^^^^^
  ```

- Error: `workflows/imcyto.nf:116:16`: `WorkflowImcyto` is not defined

  ```nextflow
          .map { WorkflowImcyto.flattenTiff(it) }
                 ^^^^^^^^^^^^^^
  ```

- Error: `workflows/imcyto.nf:128:9`: `ch_full_stack_cppipe` is not defined

  ```nextflow
          ch_full_stack_cppipe,
          ^^^^^^^^^^^^^^^^^^^^
  ```

- Error: `workflows/imcyto.nf:129:9`: `ch_plugins_dir` is not defined

  ```nextflow
          ch_plugins_dir,
          ^^^^^^^^^^^^^^
  ```

- Error: `workflows/imcyto.nf:130:9`: `ch_compensation_tiff` is not defined

  ```nextflow
          ch_compensation_tiff
          ^^^^^^^^^^^^^^^^^^^^
  ```

- Error: `workflows/imcyto.nf:139:9`: `ch_ilastik_stack_cppipe` is not defined

  ```nextflow
          ch_ilastik_stack_cppipe,
          ^^^^^^^^^^^^^^^^^^^^^^^
  ```

- Error: `workflows/imcyto.nf:140:9`: `ch_plugins_dir` is not defined

  ```nextflow
          ch_plugins_dir,
          ^^^^^^^^^^^^^^
  ```

- Error: `workflows/imcyto.nf:141:9`: `ch_compensation_tiff` is not defined

  ```nextflow
          ch_compensation_tiff
          ^^^^^^^^^^^^^^^^^^^^
  ```

- Error: `workflows/imcyto.nf:157:13`: `ch_ilastik_training_ilp` is not defined

  ```nextflow
              ch_ilastik_training_ilp
              ^^^^^^^^^^^^^^^^^^^^^^^
  ```

- Error: `workflows/imcyto.nf:174:9`: `ch_segmentation_cppipe` is not defined

  ```nextflow
          ch_segmentation_cppipe,
          ^^^^^^^^^^^^^^^^^^^^^^
  ```

- Error: `workflows/imcyto.nf:175:9`: `ch_plugins_dir` is not defined

  ```nextflow
          ch_plugins_dir,
          ^^^^^^^^^^^^^^
  ```

- Error: `workflows/imcyto.nf:193:1`: Statements cannot be mixed with script declarations -- move statements into a process, workflow, or function

  ```nextflow
  workflow.onComplete {
  ^
  ```

- Error: `workflows/imcyto.nf:195:9`: `NfcoreTemplate` is not defined

  ```nextflow
          NfcoreTemplate.email(workflow, params, summary_params, projectDir, log, [])
          ^^^^^^^^^^^^^^
  ```

- Error: `workflows/imcyto.nf:197:5`: `NfcoreTemplate` is not defined

  ```nextflow
      NfcoreTemplate.summary(workflow, params, log)
      ^^^^^^^^^^^^^^
  ```

## :warning: Warnings

- Warning: `modules/local/ilastik.nf:20:9`: Variable was declared but not used

  ```nextflow
      def prefix = task.ext.prefix ?: "${meta.id}"
          ^^^^^^
  ```

- Warning: `modules/nf-core/modules/custom/dumpsoftwareversions/main.nf:22:9`: Variable was declared but not used

  ```nextflow
      def args = task.ext.args ?: ''
          ^^^^
  ```

- Warning: `workflows/imcyto.nf:27:5`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      Channel
      ^^^^^^^
  ```

- Warning: `workflows/imcyto.nf:31:16`: Variable was declared but not used

  ```nextflow
          .set { ch_mcd }
                 ^^^^^^
  ```

- Warning: `workflows/imcyto.nf:36:36`: Variable was declared but not used

  ```nextflow
  if (params.metadata)             { ch_metadata             = file(params.metadata)             }
                                     ^^^^^^^^^^^
  ```

- Warning: `workflows/imcyto.nf:37:36`: Variable was declared but not used

  ```nextflow
  if (params.full_stack_cppipe)    { ch_full_stack_cppipe    = file(params.full_stack_cppipe)    }
                                     ^^^^^^^^^^^^^^^^^^^^
  ```

- Warning: `workflows/imcyto.nf:38:36`: Variable was declared but not used

  ```nextflow
  if (params.ilastik_stack_cppipe) { ch_ilastik_stack_cppipe = file(params.ilastik_stack_cppipe) }
                                     ^^^^^^^^^^^^^^^^^^^^^^^
  ```

- Warning: `workflows/imcyto.nf:39:36`: Variable was declared but not used

  ```nextflow
  if (params.segmentation_cppipe)  { ch_segmentation_cppipe  = file(params.segmentation_cppipe)  }
                                     ^^^^^^^^^^^^^^^^^^^^^^
  ```

- Warning: `workflows/imcyto.nf:43:9`: Variable was declared but not used

  ```nextflow
          ch_ilastik_training_ilp = file(params.ilastik_training_ilp)
          ^^^^^^^^^^^^^^^^^^^^^^^
  ```

- Warning: `workflows/imcyto.nf:47:1`: Variable was declared but not used

  ```nextflow
  ch_compensation_tiff = params.compensation_tiff ? file(params.compensation_tiff) : []
  ^^^^^^^^^^^^^^^^^^^^
  ```

- Warning: `workflows/imcyto.nf:50:1`: Variable was declared but not used

  ```nextflow
  ch_plugins_dir = file(params.plugins_dir)
  ^^^^^^^^^^^^^^
  ```

- Warning: `workflows/imcyto.nf:86:19`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_versions = Channel.empty()
                    ^^^^^^^
  ```

- Warning: `workflows/imcyto.nf:103:43`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          .map { WorkflowImcyto.flattenTiff(it) }
                                            ^^
  ```

- Warning: `workflows/imcyto.nf:116:43`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          .map { WorkflowImcyto.flattenTiff(it) }
                                            ^^
  ```
