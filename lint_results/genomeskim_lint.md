# Nextflow lint results

- Generated: 2026-01-14T09:18:23.989193076Z
- Nextflow version: 25.12.0-edge
- Summary: 40 errors, 13 warnings

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
          cpus   = { check_max( 2     * task.attempt, 'cpus'    ) }
                     ^^^^^^^^^
  ```

- Error: `conf/base.config:31:20`: `check_max` is not defined

  ```nextflow
          memory = { check_max( 12.GB * task.attempt, 'memory'  ) }
                     ^^^^^^^^^
  ```

- Error: `conf/base.config:32:20`: `check_max` is not defined

  ```nextflow
          time   = { check_max( 4.h   * task.attempt, 'time'    ) }
                     ^^^^^^^^^
  ```

- Error: `conf/base.config:35:20`: `check_max` is not defined

  ```nextflow
          cpus   = { check_max( 6     * task.attempt, 'cpus'    ) }
                     ^^^^^^^^^
  ```

- Error: `conf/base.config:36:20`: `check_max` is not defined

  ```nextflow
          memory = { check_max( 36.GB * task.attempt, 'memory'  ) }
                     ^^^^^^^^^
  ```

- Error: `conf/base.config:37:20`: `check_max` is not defined

  ```nextflow
          time   = { check_max( 8.h   * task.attempt, 'time'    ) }
                     ^^^^^^^^^
  ```

- Error: `conf/base.config:40:20`: `check_max` is not defined

  ```nextflow
          cpus   = { check_max( 12    * task.attempt, 'cpus'    ) }
                     ^^^^^^^^^
  ```

- Error: `conf/base.config:41:20`: `check_max` is not defined

  ```nextflow
          memory = { check_max( 72.GB * task.attempt, 'memory'  ) }
                     ^^^^^^^^^
  ```

- Error: `conf/base.config:42:20`: `check_max` is not defined

  ```nextflow
          time   = { check_max( 16.h  * task.attempt, 'time'    ) }
                     ^^^^^^^^^
  ```

- Error: `conf/base.config:45:20`: `check_max` is not defined

  ```nextflow
          time   = { check_max( 20.h  * task.attempt, 'time'    ) }
                     ^^^^^^^^^
  ```

- Error: `conf/base.config:48:20`: `check_max` is not defined

  ```nextflow
          memory = { check_max( 200.GB * task.attempt, 'memory' ) }
                     ^^^^^^^^^
  ```

- Error: `main.nf:20:16`: `WorkflowMain` is not defined

  ```nextflow
  params.fasta = WorkflowMain.getGenomeAttribute(params, 'fasta')
                 ^^^^^^^^^^^^
  ```

- Error: `main.nf:28:1`: Statements cannot be mixed with script declarations -- move statements into a process or workflow

  ```nextflow
  WorkflowMain.initialise(workflow, params, log)
  ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  ```

- Error: `main.nf:28:1`: `WorkflowMain` is not defined

  ```nextflow
  WorkflowMain.initialise(workflow, params, log)
  ^^^^^^^^^^^^
  ```

- Error: `nextflow.config:61:5`: Unexpected input: 'includeConfig'

  ```nextflow
      includeConfig "${params.custom_config_base}/nfcore_custom.config"
      ^
  ```

- Error: `workflows/genomeskim.nf:7:1`: Statements cannot be mixed with script declarations -- move statements into a process or workflow

  ```nextflow
  def summary_params = NfcoreSchema.paramsSummaryMap(workflow, params)
  ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  ```

- Error: `workflows/genomeskim.nf:7:22`: `NfcoreSchema` is not defined

  ```nextflow
  def summary_params = NfcoreSchema.paramsSummaryMap(workflow, params)
                       ^^^^^^^^^^^^
  ```

- Error: `workflows/genomeskim.nf:10:1`: Statements cannot be mixed with script declarations -- move statements into a process or workflow

  ```nextflow
  WorkflowGenomeskim.initialise(params, log)
  ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  ```

- Error: `workflows/genomeskim.nf:10:1`: `WorkflowGenomeskim` is not defined

  ```nextflow
  WorkflowGenomeskim.initialise(params, log)
  ^^^^^^^^^^^^^^^^^^
  ```

- Error: `workflows/genomeskim.nf:14:1`: Statements cannot be mixed with script declarations -- move statements into a process or workflow

  ```nextflow
  def checkPathParamList = [ params.input, params.multiqc_config, params.fasta ]
  ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  ```

- Error: `workflows/genomeskim.nf:15:1`: `for` loops are no longer supported

  ```nextflow
  for (param in checkPathParamList) { if (param) { file(param, checkIfExists: true) } }
  ^^^
  ```

- Error: `workflows/genomeskim.nf:15:1`: Statements cannot be mixed with script declarations -- move statements into a process or workflow

  ```nextflow
  for (param in checkPathParamList) { if (param) { file(param, checkIfExists: true) } }
  ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  ```

- Error: `workflows/genomeskim.nf:15:6`: `param` is not defined

  ```nextflow
  for (param in checkPathParamList) { if (param) { file(param, checkIfExists: true) } }
       ^^^^^
  ```

- Error: `workflows/genomeskim.nf:15:40`: `param` is not defined

  ```nextflow
  for (param in checkPathParamList) { if (param) { file(param, checkIfExists: true) } }
                                         ^^^^^^^
  ```

- Error: `workflows/genomeskim.nf:15:55`: `param` is not defined

  ```nextflow
  for (param in checkPathParamList) { if (param) { file(param, checkIfExists: true) } }
                                                        ^^^^^
  ```

- Error: `workflows/genomeskim.nf:18:1`: Statements cannot be mixed with script declarations -- move statements into a process or workflow

  ```nextflow
  if (params.input) { ch_input = file(params.input) } else { exit 1, 'Input samplesheet not specified!' }
  ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  ```

- Error: `workflows/genomeskim.nf:26:1`: Statements cannot be mixed with script declarations -- move statements into a process or workflow

  ```nextflow
  ch_multiqc_config        = file("$projectDir/assets/multiqc_config.yml", checkIfExists: true)
  ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  ```

- Error: `workflows/genomeskim.nf:27:1`: Statements cannot be mixed with script declarations -- move statements into a process or workflow

  ```nextflow
  ch_multiqc_custom_config = params.multiqc_config ? Channel.fromPath(params.multiqc_config) : Channel.empty()
  ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  ```

- Error: `workflows/genomeskim.nf:60:1`: Statements cannot be mixed with script declarations -- move statements into a process or workflow

  ```nextflow
  def multiqc_report = []
  ^^^^^^^^^^^^^^^^^^^^^^^
  ```

- Error: `workflows/genomeskim.nf:70:9`: `ch_input` is not defined

  ```nextflow
          ch_input
          ^^^^^^^^
  ```

- Error: `workflows/genomeskim.nf:89:27`: `WorkflowGenomeskim` is not defined

  ```nextflow
      workflow_summary    = WorkflowGenomeskim.paramsSummaryMultiqc(workflow, summary_params)
                            ^^^^^^^^^^^^^^^^^^
  ```

- Error: `workflows/genomeskim.nf:89:77`: `summary_params` is not defined

  ```nextflow
      workflow_summary    = WorkflowGenomeskim.paramsSummaryMultiqc(workflow, summary_params)
                                                                              ^^^^^^^^^^^^^^
  ```

- Error: `workflows/genomeskim.nf:93:58`: `ch_multiqc_config` is not defined

  ```nextflow
      ch_multiqc_files = ch_multiqc_files.mix(Channel.from(ch_multiqc_config))
                                                           ^^^^^^^^^^^^^^^^^
  ```

- Error: `workflows/genomeskim.nf:94:45`: `ch_multiqc_custom_config` is not defined

  ```nextflow
      ch_multiqc_files = ch_multiqc_files.mix(ch_multiqc_custom_config.collect().ifEmpty([]))
                                              ^^^^^^^^^^^^^^^^^^^^^^^^
  ```

- Error: `workflows/genomeskim.nf:112:1`: Statements cannot be mixed with script declarations -- move statements into a process or workflow

  ```nextflow
  workflow.onComplete {
  ^
  ```

- Error: `workflows/genomeskim.nf:114:9`: `NfcoreTemplate` is not defined

  ```nextflow
          NfcoreTemplate.email(workflow, params, summary_params, projectDir, log, multiqc_report)
          ^^^^^^^^^^^^^^
  ```

- Error: `workflows/genomeskim.nf:116:5`: `NfcoreTemplate` is not defined

  ```nextflow
      NfcoreTemplate.summary(workflow, params, log)
      ^^^^^^^^^^^^^^
  ```

## :warning: Warnings

- Warning: `modules/nf-core/modules/custom/dumpsoftwareversions/main.nf:22:9`: Variable was declared but not used

  ```nextflow
      def args = task.ext.args ?: ''
          ^^^^
  ```

- Warning: `subworkflows/local/input_check.nf:15:37`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          .map { create_fastq_channel(it) }
                                      ^^
  ```

- Warning: `workflows/genomeskim.nf:18:21`: Variable was declared but not used

  ```nextflow
  if (params.input) { ch_input = file(params.input) } else { exit 1, 'Input samplesheet not specified!' }
                      ^^^^^^^^
  ```

- Warning: `workflows/genomeskim.nf:26:1`: Variable was declared but not used

  ```nextflow
  ch_multiqc_config        = file("$projectDir/assets/multiqc_config.yml", checkIfExists: true)
  ^^^^^^^^^^^^^^^^^
  ```

- Warning: `workflows/genomeskim.nf:27:1`: Variable was declared but not used

  ```nextflow
  ch_multiqc_custom_config = params.multiqc_config ? Channel.fromPath(params.multiqc_config) : Channel.empty()
  ^^^^^^^^^^^^^^^^^^^^^^^^
  ```

- Warning: `workflows/genomeskim.nf:27:52`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
  ch_multiqc_custom_config = params.multiqc_config ? Channel.fromPath(params.multiqc_config) : Channel.empty()
                                                     ^^^^^^^
  ```

- Warning: `workflows/genomeskim.nf:27:94`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
  ch_multiqc_custom_config = params.multiqc_config ? Channel.fromPath(params.multiqc_config) : Channel.empty()
                                                                                               ^^^^^^^
  ```

- Warning: `workflows/genomeskim.nf:64:19`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_versions = Channel.empty()
                    ^^^^^^^
  ```

- Warning: `workflows/genomeskim.nf:90:27`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_workflow_summary = Channel.value(workflow_summary)
                            ^^^^^^^
  ```

- Warning: `workflows/genomeskim.nf:92:24`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_multiqc_files = Channel.empty()
                         ^^^^^^^
  ```

- Warning: `workflows/genomeskim.nf:93:45`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_multiqc_files = ch_multiqc_files.mix(Channel.from(ch_multiqc_config))
                                              ^^^^^^^
  ```

- Warning: `workflows/genomeskim.nf:97:68`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
      ch_multiqc_files = ch_multiqc_files.mix(FASTQC.out.zip.collect{it[1]}.ifEmpty([]))
                                                                     ^^
  ```

- Warning: `workflows/genomeskim.nf:102:5`: Variable was declared but not used

  ```nextflow
      multiqc_report = MULTIQC.out.report.toList()
      ^^^^^^^^^^^^^^
  ```
