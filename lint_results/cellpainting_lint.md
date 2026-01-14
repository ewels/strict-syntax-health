# Nextflow lint results

- Generated: 2026-01-14T09:10:00.288797798Z
- Nextflow version: 25.12.0-edge
- Summary: 6 errors, 35 warnings

## :x: Errors

- Error: `nextflow.config:293:36`: `manifest` is not defined

  ```nextflow
  \033[0;35m  nf-core/cellpainting ${manifest.version}\033[0m
                                     ^^^^^^^^
  ```

- Error: `nextflow.config:296:26`: `manifest` is not defined

  ```nextflow
          afterText = """${manifest.doi ? "\n* The pipeline\n" : ""}${manifest.doi.tokenize(",").collect { "    https://doi.org/${it.trim().replace('https://doi.org/','')}"}.join("\n")}${manifest.doi ? "\n" : ""}
                           ^^^^^^^^
  ```

- Error: `nextflow.config:296:69`: `manifest` is not defined

  ```nextflow
          afterText = """${manifest.doi ? "\n* The pipeline\n" : ""}${manifest.doi.tokenize(",").collect { "    https://doi.org/${it.trim().replace('https://doi.org/','')}"}.join("\n")}${manifest.doi ? "\n" : ""}
                                                                      ^^^^^^^^
  ```

- Error: `nextflow.config:296:186`: `manifest` is not defined

  ```nextflow
          afterText = """${manifest.doi ? "\n* The pipeline\n" : ""}${manifest.doi.tokenize(",").collect { "    https://doi.org/${it.trim().replace('https://doi.org/','')}"}.join("\n")}${manifest.doi ? "\n" : ""}
                                                                                                                                                                                           ^^^^^^^^
  ```

- Error: `nextflow.config:305:22`: `validation` is not defined

  ```nextflow
          beforeText = validation.help.beforeText
                       ^^^^^^^^^^
  ```

- Error: `nextflow.config:306:21`: `validation` is not defined

  ```nextflow
          afterText = validation.help.afterText
                      ^^^^^^^^^^
  ```

## :warning: Warnings

- Warning: `modules/local/cellprofiler/analysis.nf:77:9`: Variable was declared but not used

  ```nextflow
      def args = task.ext.args ?: ''
          ^^^^
  ```

- Warning: `modules/local/cellprofiler/assaydevelopment.nf:27:9`: Variable was declared but not used

  ```nextflow
      def args = task.ext.args ?: ''
          ^^^^
  ```

- Warning: `modules/local/cellprofiler/assaydevelopment.nf:28:9`: Variable was declared but not used

  ```nextflow
      def prefix = task.ext.prefix ?: "${meta.id}"
          ^^^^^^
  ```

- Warning: `modules/local/cellprofiler/assaydevelopment.nf:43:9`: Variable was declared but not used

  ```nextflow
      def args = task.ext.args ?: ''
          ^^^^
  ```

- Warning: `modules/local/cellprofiler/illuminationcorrection/main.nf:24:9`: Variable was declared but not used

  ```nextflow
      def prefix = task.ext.prefix ?: "${meta.id}"
          ^^^^^^
  ```

- Warning: `modules/local/cellprofiler/illuminationcorrection/main.nf:45:9`: Variable was declared but not used

  ```nextflow
      def args = task.ext.args ?: ''
          ^^^^
  ```

- Warning: `modules/local/cellprofiler/illuminationcorrection/main.nf:46:9`: Variable was declared but not used

  ```nextflow
      def prefix = task.ext.prefix ?: "${meta.id}"
          ^^^^^^
  ```

- Warning: `nextflow.config:296:129`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          afterText = """${manifest.doi ? "\n* The pipeline\n" : ""}${manifest.doi.tokenize(",").collect { "    https://doi.org/${it.trim().replace('https://doi.org/','')}"}.join("\n")}${manifest.doi ? "\n" : ""}
                                                                                                                                  ^^
  ```

- Warning: `subworkflows/local/cellprofiler_load_data_csv/main.nf:20:47`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
              def group_id = keys.collect { meta[it] }.join('_')
                                                ^^
  ```

- Warning: `subworkflows/local/cellprofiler_load_data_csv/main.nf:31:54`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
              def image_channels = meta_list.collect { it.channel }.unique().sort()
                                                       ^^
  ```

- Warning: `subworkflows/local/cellprofiler_load_data_csv/main.nf:38:25`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
              }.groupBy { it[0] }
                          ^^
  ```

- Warning: `subworkflows/local/cellprofiler_load_data_csv/main.nf:43:54`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
                  def row_channels = entries.collect { it[1] }  // Extract channels
                                                       ^^
  ```

- Warning: `subworkflows/local/cellprofiler_load_data_csv/main.nf:44:52`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
                  def row_images = entries.collect { it[2] }    // Extract images
                                                     ^^
  ```

- Warning: `subworkflows/local/cellprofiler_load_data_csv_with_illum/main.nf:19:92`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
              def group_meta = meta.subMap(grouping_keys) + [id: grouping_keys.collect { meta[it] }.join('_')]
                                                                                             ^^
  ```

- Warning: `subworkflows/local/cellprofiler_load_data_csv_with_illum/main.nf:29:48`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
              def channels = meta_list.collect { it.channel }.unique().sort()
                                                 ^^
  ```

- Warning: `subworkflows/local/cellprofiler_load_data_csv_with_illum/main.nf:42:67`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
              def orig_headers = channels.collect { "FileName_Orig${it}" }
                                                                    ^^
  ```

- Warning: `subworkflows/local/cellprofiler_load_data_csv_with_illum/main.nf:43:69`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
              def illum_headers = channels.collect { "FileName_Illum${it}" }
                                                                      ^^
  ```

- Warning: `subworkflows/local/cellprofiler_load_data_csv_with_illum/main.nf:94:86`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
              def illum_grouping_keys = grouping_keys.findAll { illum_meta.containsKey(it) }
                                                                                       ^^
  ```

- Warning: `subworkflows/local/cellprofiler_load_data_csv_with_illum/main.nf:95:116`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
              def group_meta = illum_meta.subMap(illum_grouping_keys) + [id: illum_grouping_keys.collect { illum_meta[it] }.join('_')]
                                                                                                                     ^^
  ```

- Warning: `subworkflows/local/cellprofiler_load_data_csv_with_illum/main.nf:111:82`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
              def illum_keys = ['batch', 'plate'].findAll { first_meta.containsKey(it) }
                                                                                   ^^
  ```

- Warning: `subworkflows/local/cellprofiler_load_data_csv_with_illum/main.nf:112:60`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
              def illum_key = illum_keys.collect { first_meta[it] }.join('_')
                                                             ^^
  ```

- Warning: `subworkflows/local/utils_nfcore_cellpainting_pipeline/main.nf:31:5`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
      monochrome_logs   // boolean: Do not use coloured log outputs
      ^^^^^^^^^^^^^^^
  ```

- Warning: `subworkflows/local/utils_nfcore_cellpainting_pipeline/main.nf:38:19`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_versions = Channel.empty()
                    ^^^^^^^
  ```

- Warning: `subworkflows/local/utils_nfcore_cellpainting_pipeline/main.nf:70:5`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      Channel
      ^^^^^^^
  ```

- Warning: `subworkflows/nf-core/utils_nfcore_pipeline/main.nf:101:98`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      return ch_versions.unique().map { version -> processVersionsFromYAML(version) }.unique().mix(Channel.of(workflowVersionToYAML()))
                                                                                                   ^^^^^^^
  ```

- Warning: `workflows/cellpainting.nf:32:5`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
      cellprofiler_analysis_cppipe // value: path to analysis cppipe
      ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  ```

- Warning: `workflows/cellpainting.nf:37:19`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_versions = Channel.empty()
                    ^^^^^^^
  ```

- Warning: `workflows/cellpainting.nf:38:24`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_multiqc_files = Channel.empty()
                         ^^^^^^^
  ```

- Warning: `workflows/cellpainting.nf:93:32`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_multiqc_config        = Channel.fromPath(
                                 ^^^^^^^
  ```

- Warning: `workflows/cellpainting.nf:96:9`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
          Channel.fromPath(params.multiqc_config, checkIfExists: true) :
          ^^^^^^^
  ```

- Warning: `workflows/cellpainting.nf:97:9`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
          Channel.empty()
          ^^^^^^^
  ```

- Warning: `workflows/cellpainting.nf:99:9`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
          Channel.fromPath(params.multiqc_logo, checkIfExists: true) :
          ^^^^^^^
  ```

- Warning: `workflows/cellpainting.nf:100:9`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
          Channel.empty()
          ^^^^^^^
  ```

- Warning: `workflows/cellpainting.nf:104:27`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_workflow_summary = Channel.value(paramsSummaryMultiqc(summary_params))
                            ^^^^^^^
  ```

- Warning: `workflows/cellpainting.nf:110:45`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_methods_description                = Channel.value(
                                              ^^^^^^^
  ```
