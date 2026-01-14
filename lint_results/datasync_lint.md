# Nextflow lint results

- Generated: 2026-01-14T09:11:05.449329556Z
- Nextflow version: 25.12.0-edge
- Summary: 19 errors, 20 warnings

## :x: Errors

- Error: `modules/local/sync/sync.nf:13:38`: Unexpected input: '\_sha256_checksums'

  ```nextflow
      tuple val(run_id), path(${run_id}_sha256_checksums.txt) , emit: synced
                                       ^
  ```

- Error: `nextflow.config:204:1`: Variable declarations cannot be mixed with config statements

  ```nextflow
  def trace_timestamp = new java.util.Date().format( 'yyyy-MM-dd_HH-mm-ss')
  ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  ```

- Error: `nextflow.config:207:68`: `trace_timestamp` is not defined

  ```nextflow
      file    = "${params.outdir}/pipeline_info/execution_timeline_${trace_timestamp}.html"
                                                                     ^^^^^^^^^^^^^^^
  ```

- Error: `nextflow.config:211:66`: `trace_timestamp` is not defined

  ```nextflow
      file    = "${params.outdir}/pipeline_info/execution_report_${trace_timestamp}.html"
                                                                   ^^^^^^^^^^^^^^^
  ```

- Error: `nextflow.config:215:65`: `trace_timestamp` is not defined

  ```nextflow
      file    = "${params.outdir}/pipeline_info/execution_trace_${trace_timestamp}.txt"
                                                                  ^^^^^^^^^^^^^^^
  ```

- Error: `nextflow.config:219:62`: `trace_timestamp` is not defined

  ```nextflow
      file    = "${params.outdir}/pipeline_info/pipeline_dag_${trace_timestamp}.html"
                                                               ^^^^^^^^^^^^^^^
  ```

- Error: `nextflow.config:242:34`: `manifest` is not defined

  ```nextflow
          command = "nextflow run $manifest.name -profile <docker/singularity/.../institute> --input samplesheet.csv --outdir <OUTDIR>"
                                   ^^^^^^^^
  ```

- Error: `nextflow.config:252:15`: `manifest` is not defined

  ```nextflow
  \033[0;35m  ${manifest.name} ${manifest.version}\033[0m
                ^^^^^^^^
  ```

- Error: `nextflow.config:252:32`: `manifest` is not defined

  ```nextflow
  \033[0;35m  ${manifest.name} ${manifest.version}\033[0m
                                 ^^^^^^^^
  ```

- Error: `nextflow.config:255:26`: `manifest` is not defined

  ```nextflow
          afterText = """${manifest.doi ? "* The pipeline\n" : ""}${manifest.doi.tokenize(",").collect { "  https://doi.org/${it.trim().replace('https://doi.org/','')}"}.join("\n")}${manifest.doi ? "\n" : ""}
                           ^^^^^^^^
  ```

- Error: `nextflow.config:255:67`: `manifest` is not defined

  ```nextflow
          afterText = """${manifest.doi ? "* The pipeline\n" : ""}${manifest.doi.tokenize(",").collect { "  https://doi.org/${it.trim().replace('https://doi.org/','')}"}.join("\n")}${manifest.doi ? "\n" : ""}
                                                                    ^^^^^^^^
  ```

- Error: `nextflow.config:255:182`: `manifest` is not defined

  ```nextflow
          afterText = """${manifest.doi ? "* The pipeline\n" : ""}${manifest.doi.tokenize(",").collect { "  https://doi.org/${it.trim().replace('https://doi.org/','')}"}.join("\n")}${manifest.doi ? "\n" : ""}
                                                                                                                                                                                       ^^^^^^^^
  ```

- Error: `nextflow.config:260:26`: `manifest` is not defined

  ```nextflow
      https://github.com/${manifest.name}/blob/master/CITATIONS.md
                           ^^^^^^^^
  ```

- Error: `nextflow.config:264:22`: `validation` is not defined

  ```nextflow
          beforeText = validation.help.beforeText
                       ^^^^^^^^^^
  ```

- Error: `nextflow.config:265:21`: `validation` is not defined

  ```nextflow
          afterText = validation.help.afterText
                      ^^^^^^^^^^
  ```

- Error: `workflows/datasync.nf:6:1`: Invalid include source: '/home/runner/work/strict-syntax-health/strict-syntax-health/pipelines/datasync/modules/nf-core/fastqc/main.nf'

  ```nextflow
  include { FASTQC                 } from '../modules/nf-core/fastqc/main'
  ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  ```

- Error: `workflows/datasync.nf:30:5`: `FASTQC` is not defined

  ```nextflow
      FASTQC (
      ^^^^^^
  ```

- Error: `workflows/datasync.nf:33:45`: `FASTQC` is not defined

  ```nextflow
      ch_multiqc_files = ch_multiqc_files.mix(FASTQC.out.zip.collect{it[1]})
                                              ^^^^^^
  ```

- Error: `workflows/datasync.nf:34:35`: `FASTQC` is not defined

  ```nextflow
      ch_versions = ch_versions.mix(FASTQC.out.versions.first())
                                    ^^^^^^
  ```

## :warning: Warnings

- Warning: `nextflow.config:255:125`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          afterText = """${manifest.doi ? "* The pipeline\n" : ""}${manifest.doi.tokenize(",").collect { "  https://doi.org/${it.trim().replace('https://doi.org/','')}"}.join("\n")}${manifest.doi ? "\n" : ""}
                                                                                                                              ^^
  ```

- Warning: `subworkflows/local/utils_nfcore_datasync_pipeline/main.nf:31:5`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
      monochrome_logs   // boolean: Do not use coloured log outputs
      ^^^^^^^^^^^^^^^
  ```

- Warning: `subworkflows/local/utils_nfcore_datasync_pipeline/main.nf:34:5`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
      input             //  string: Path to input samplesheet
      ^^^^^
  ```

- Warning: `subworkflows/local/utils_nfcore_datasync_pipeline/main.nf:38:19`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_versions = Channel.empty()
                    ^^^^^^^
  ```

- Warning: `subworkflows/local/utils_nfcore_datasync_pipeline/main.nf:75:5`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      Channel
      ^^^^^^^
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

- Warning: `workflows/datasync.nf:25:19`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_versions = Channel.empty()
                    ^^^^^^^
  ```

- Warning: `workflows/datasync.nf:26:24`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_multiqc_files = Channel.empty()
                         ^^^^^^^
  ```

- Warning: `workflows/datasync.nf:33:68`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
      ch_multiqc_files = ch_multiqc_files.mix(FASTQC.out.zip.collect{it[1]})
                                                                     ^^
  ```

- Warning: `workflows/datasync.nf:51:32`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_multiqc_config        = Channel.fromPath(
                                 ^^^^^^^
  ```

- Warning: `workflows/datasync.nf:54:9`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
          Channel.fromPath(params.multiqc_config, checkIfExists: true) :
          ^^^^^^^
  ```

- Warning: `workflows/datasync.nf:55:9`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
          Channel.empty()
          ^^^^^^^
  ```

- Warning: `workflows/datasync.nf:57:9`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
          Channel.fromPath(params.multiqc_logo, checkIfExists: true) :
          ^^^^^^^
  ```

- Warning: `workflows/datasync.nf:58:9`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
          Channel.empty()
          ^^^^^^^
  ```

- Warning: `workflows/datasync.nf:62:27`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_workflow_summary = Channel.value(paramsSummaryMultiqc(summary_params))
                            ^^^^^^^
  ```

- Warning: `workflows/datasync.nf:68:45`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_methods_description                = Channel.value(
                                              ^^^^^^^
  ```
