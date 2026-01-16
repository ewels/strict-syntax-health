# Nextflow lint results

- Generated: 2026-01-16T06:32:09.523010604Z
- Nextflow version: 25.12.0-edge
- Summary: 6 errors, 25 warnings

## :x: Errors

- Error: `nextflow.config:344:32`: `manifest` is not defined

  ```nextflow
  \033[0;35m  nf-core/fetchngs ${manifest.version}\033[0m
                                 ^^^^^^^^
  ```

- Error: `nextflow.config:347:26`: `manifest` is not defined

  ```nextflow
          afterText = """${manifest.doi ? "\n* The pipeline\n" : ""}${manifest.doi.tokenize(",").collect { "    https://doi.org/${it.trim().replace('https://doi.org/','')}"}.join("\n")}${manifest.doi ? "\n" : ""}
                           ^^^^^^^^
  ```

- Error: `nextflow.config:347:69`: `manifest` is not defined

  ```nextflow
          afterText = """${manifest.doi ? "\n* The pipeline\n" : ""}${manifest.doi.tokenize(",").collect { "    https://doi.org/${it.trim().replace('https://doi.org/','')}"}.join("\n")}${manifest.doi ? "\n" : ""}
                                                                      ^^^^^^^^
  ```

- Error: `nextflow.config:347:186`: `manifest` is not defined

  ```nextflow
          afterText = """${manifest.doi ? "\n* The pipeline\n" : ""}${manifest.doi.tokenize(",").collect { "    https://doi.org/${it.trim().replace('https://doi.org/','')}"}.join("\n")}${manifest.doi ? "\n" : ""}
                                                                                                                                                                                           ^^^^^^^^
  ```

- Error: `nextflow.config:356:22`: `validation` is not defined

  ```nextflow
          beforeText = validation.help.beforeText
                       ^^^^^^^^^^
  ```

- Error: `nextflow.config:357:21`: `validation` is not defined

  ```nextflow
          afterText = validation.help.afterText
                      ^^^^^^^^^^
  ```

## :warning: Warnings

- Warning: `modules/local/sra_to_samplesheet/main.nf:52:57`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
      samplesheet  = pipeline_map.keySet().collect{ '"' + it + '"'}.join(",") + '\n'
                                                          ^^
  ```

- Warning: `modules/local/sra_to_samplesheet/main.nf:53:57`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
      samplesheet += pipeline_map.values().collect{ '"' + it + '"'}.join(",")
                                                          ^^
  ```

- Warning: `modules/local/sra_to_samplesheet/main.nf:63:83`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
      def fields = mapping_fields ? ['sample'] + mapping_fields.split(',').collect{ it.trim().toLowerCase() } : []
                                                                                    ^^
  ```

- Warning: `modules/local/sra_to_samplesheet/main.nf:69:39`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
      mappings  = fields.collect{ '"' + it + '"'}.join(",") + '\n'
                                        ^^
  ```

- Warning: `modules/local/sra_to_samplesheet/main.nf:70:69`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
      mappings += mappings_map.subMap(fields).values().collect{ '"' + it + '"'}.join(",")
                                                                      ^^
  ```

- Warning: `modules/nf-core/custom/sratoolsncbisettings/main.nf:20:5`: The `shell` block is deprecated, use `script` instead

  ```nextflow
      shell:
      ^^^^^
  ```

- Warning: `modules/nf-core/custom/sratoolsncbisettings/main.nf:21:5`: Variable was declared but not used

  ```nextflow
      config = "/LIBS/GUID = \"${UUID.randomUUID().toString()}\"\\n/libs/cloud/report_instance_identity = \"true\"\\n"
      ^^^^^^
  ```

- Warning: `modules/nf-core/fastqdl/main.nf:40:9`: Variable was declared but not used

  ```nextflow
      def args = task.ext.args ?: ''
          ^^^^
  ```

- Warning: `modules/nf-core/sratools/prefetch/main.nf:22:5`: The `shell` block is deprecated, use `script` instead

  ```nextflow
      shell:
      ^^^^^
  ```

- Warning: `modules/nf-core/sratools/prefetch/main.nf:24:5`: Variable was declared but not used

  ```nextflow
      args2 = task.ext.args2 ?: '5 1 100'  // <num retries> <base delay in seconds> <max delay in seconds>
      ^^^^^
  ```

- Warning: `nextflow.config:347:129`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          afterText = """${manifest.doi ? "\n* The pipeline\n" : ""}${manifest.doi.tokenize(",").collect { "    https://doi.org/${it.trim().replace('https://doi.org/','')}"}.join("\n")}${manifest.doi ? "\n" : ""}
                                                                                                                                  ^^
  ```

- Warning: `subworkflows/local/utils_nfcore_fetchngs_pipeline/main.nf:30:5`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
      monochrome_logs     // boolean: Do not use coloured log outputs
      ^^^^^^^^^^^^^^^
  ```

- Warning: `subworkflows/local/utils_nfcore_fetchngs_pipeline/main.nf:76:5`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      Channel.from(ch_input)
      ^^^^^^^
  ```

- Warning: `subworkflows/local/utils_nfcore_fetchngs_pipeline/main.nf:78:16`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          .map { it[0] }
                 ^^
  ```

- Warning: `subworkflows/local/utils_nfcore_fetchngs_pipeline/main.nf:172:101`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
      def actual_ena_metadata_fields = ena_metadata_fields ? ena_metadata_fields.split(',').collect { it.trim().toLowerCase() } : valid_ena_metadata_fields
                                                                                                      ^^
  ```

- Warning: `subworkflows/nf-core/fastq_download_prefetch_fasterqdump_sratools/main.nf:15:19`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_versions = Channel.empty()
                    ^^^^^^^
  ```

- Warning: `subworkflows/nf-core/utils_nfcore_pipeline/main.nf:101:98`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      return ch_versions.unique().map { version -> processVersionsFromYAML(version) }.unique().mix(Channel.of(workflowVersionToYAML()))
                                                                                                   ^^^^^^^
  ```

- Warning: `workflows/sra/main.nf:36:19`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_versions = Channel.empty()
                    ^^^^^^^
  ```

- Warning: `workflows/sra/main.nf:163:16`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          .map { it[1] }
                 ^^
  ```

- Warning: `workflows/sra/main.nf:164:91`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          .collectFile(name:'tmp_samplesheet.csv', newLine: true, keepHeader: true, sort: { it.baseName })
                                                                                            ^^
  ```

- Warning: `workflows/sra/main.nf:165:16`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          .map { it.text.tokenize('\n').join('\n') }
                 ^^
  ```

- Warning: `workflows/sra/main.nf:172:16`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          .map { it[1] }
                 ^^
  ```

- Warning: `workflows/sra/main.nf:173:91`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          .collectFile(name:'tmp_id_mappings.csv', newLine: true, keepHeader: true, sort: { it.baseName })
                                                                                            ^^
  ```

- Warning: `workflows/sra/main.nf:174:16`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          .map { it.text.tokenize('\n').join('\n') }
                 ^^
  ```

- Warning: `workflows/sra/main.nf:181:30`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_sample_mappings_yml = Channel.empty()
                               ^^^^^^^
  ```
