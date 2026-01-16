# Nextflow lint results

- Generated: 2026-01-16T06:38:35.810643994Z
- Nextflow version: 25.12.0-edge
- Summary: 27 warnings

## :warning: Warnings

- Warning: `subworkflows/local/utils_nfcore_ribomsqc_pipeline/main.nf:32:5`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
      monochrome_logs   // boolean: Do not use coloured log outputs
      ^^^^^^^^^^^^^^^
  ```

- Warning: `subworkflows/local/utils_nfcore_ribomsqc_pipeline/main.nf:35:5`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
      input             //  string: Path to input samplesheet
      ^^^^^
  ```

- Warning: `subworkflows/local/utils_nfcore_ribomsqc_pipeline/main.nf:42:19`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_versions = Channel.empty()
                    ^^^^^^^
  ```

- Warning: `subworkflows/local/utils_nfcore_ribomsqc_pipeline/main.nf:67:144`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
      after_text = """${workflow.manifest.doi ? "\n* The pipeline\n" : ""}${workflow.manifest.doi.tokenize(",").collect { "    https://doi.org/${it.trim().replace('https://doi.org/','')}"}.join("\n")}${workflow.manifest.doi ? "\n" : ""}
                                                                                                                                                 ^^
  ```

- Warning: `subworkflows/local/utils_nfcore_ribomsqc_pipeline/main.nf:99:5`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      Channel
      ^^^^^^^
  ```

- Warning: `subworkflows/nf-core/utils_nfcore_pipeline/main.nf:101:98`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      return ch_versions.unique().map { version -> processVersionsFromYAML(version) }.unique().mix(Channel.of(workflowVersionToYAML()))
                                                                                                   ^^^^^^^
  ```

- Warning: `workflows/ribomsqc.nf:26:23`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
          ch_versions = Channel.empty()
                        ^^^^^^^
  ```

- Warning: `workflows/ribomsqc.nf:45:31`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
          analytes_tsv_ch     = Channel.value(file(params.analytes_tsv, checkIfExists: true))
                                ^^^^^^^
  ```

- Warning: `workflows/ribomsqc.nf:46:9`: Variable was declared but not used

  ```nextflow
          analyte_ch          = Channel.value(params.analyte)
          ^^^^^^^^^^
  ```

- Warning: `workflows/ribomsqc.nf:46:31`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
          analyte_ch          = Channel.value(params.analyte)
                                ^^^^^^^
  ```

- Warning: `workflows/ribomsqc.nf:47:9`: Variable was declared but not used

  ```nextflow
          rt_tol_ch           = Channel.value(params.rt_tolerance)
          ^^^^^^^^^
  ```

- Warning: `workflows/ribomsqc.nf:47:31`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
          rt_tol_ch           = Channel.value(params.rt_tolerance)
                                ^^^^^^^
  ```

- Warning: `workflows/ribomsqc.nf:48:9`: Variable was declared but not used

  ```nextflow
          mz_tol_ch           = Channel.value(params.mz_tolerance)
          ^^^^^^^^^
  ```

- Warning: `workflows/ribomsqc.nf:48:31`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
          mz_tol_ch           = Channel.value(params.mz_tolerance)
                                ^^^^^^^
  ```

- Warning: `workflows/ribomsqc.nf:49:9`: Variable was declared but not used

  ```nextflow
          ms_level_ch         = Channel.value(params.ms_level)
          ^^^^^^^^^^^
  ```

- Warning: `workflows/ribomsqc.nf:49:31`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
          ms_level_ch         = Channel.value(params.ms_level)
                                ^^^^^^^
  ```

- Warning: `workflows/ribomsqc.nf:50:9`: Variable was declared but not used

  ```nextflow
          plot_xic_ms1_ch     = Channel.value(params.plot_xic_ms1)
          ^^^^^^^^^^^^^^^
  ```

- Warning: `workflows/ribomsqc.nf:50:31`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
          plot_xic_ms1_ch     = Channel.value(params.plot_xic_ms1)
                                ^^^^^^^
  ```

- Warning: `workflows/ribomsqc.nf:51:9`: Variable was declared but not used

  ```nextflow
          plot_xic_ms2_ch     = Channel.value(params.plot_xic_ms2)
          ^^^^^^^^^^^^^^^
  ```

- Warning: `workflows/ribomsqc.nf:51:31`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
          plot_xic_ms2_ch     = Channel.value(params.plot_xic_ms2)
                                ^^^^^^^
  ```

- Warning: `workflows/ribomsqc.nf:52:9`: Variable was declared but not used

  ```nextflow
          plot_output_path_ch = Channel.value(params.plot_output_path)
          ^^^^^^^^^^^^^^^^^^^
  ```

- Warning: `workflows/ribomsqc.nf:52:31`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
          plot_output_path_ch = Channel.value(params.plot_output_path)
                                ^^^^^^^
  ```

- Warning: `workflows/ribomsqc.nf:53:9`: Variable was declared but not used

  ```nextflow
          overwrite_tsv_ch    = Channel.value(params.overwrite_tsv)
          ^^^^^^^^^^^^^^^^
  ```

- Warning: `workflows/ribomsqc.nf:53:31`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
          overwrite_tsv_ch    = Channel.value(params.overwrite_tsv)
                                ^^^^^^^
  ```

- Warning: `workflows/ribomsqc.nf:78:13`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
              Channel.fromPath("${outdir_path}/**/*_mqc.json") :
              ^^^^^^^
  ```

- Warning: `workflows/ribomsqc.nf:79:13`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
              Channel.empty()
              ^^^^^^^
  ```

- Warning: `workflows/ribomsqc.nf:111:21`: Variable was declared but not used

  ```nextflow
              ).set { ch_collated_versions }
                      ^^^^^^^^^^^^^^^^^^^^
  ```
