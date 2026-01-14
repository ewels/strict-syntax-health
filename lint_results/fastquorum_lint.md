# Nextflow lint results

- Generated: 2026-01-14T09:17:46.867396690Z
- Nextflow version: 25.12.0-edge
- Summary: 6 errors, 28 warnings

## :x: Errors

- Error: `nextflow.config:303:34`: `manifest` is not defined

  ```nextflow
  \033[0;35m  nf-core/fastquorum ${manifest.version}\033[0m
                                   ^^^^^^^^
  ```

- Error: `nextflow.config:306:26`: `manifest` is not defined

  ```nextflow
          afterText = """${manifest.doi ? "\n* The pipeline\n" : ""}${manifest.doi.tokenize(",").collect { "    https://doi.org/${it.trim().replace('https://doi.org/', '')}" }.join("\n")}${manifest.doi ? "\n" : ""}
                           ^^^^^^^^
  ```

- Error: `nextflow.config:306:69`: `manifest` is not defined

  ```nextflow
          afterText = """${manifest.doi ? "\n* The pipeline\n" : ""}${manifest.doi.tokenize(",").collect { "    https://doi.org/${it.trim().replace('https://doi.org/', '')}" }.join("\n")}${manifest.doi ? "\n" : ""}
                                                                      ^^^^^^^^
  ```

- Error: `nextflow.config:306:188`: `manifest` is not defined

  ```nextflow
          afterText = """${manifest.doi ? "\n* The pipeline\n" : ""}${manifest.doi.tokenize(",").collect { "    https://doi.org/${it.trim().replace('https://doi.org/', '')}" }.join("\n")}${manifest.doi ? "\n" : ""}
                                                                                                                                                                                             ^^^^^^^^
  ```

- Error: `nextflow.config:315:22`: `validation` is not defined

  ```nextflow
          beforeText = validation.help.beforeText
                       ^^^^^^^^^^
  ```

- Error: `nextflow.config:316:21`: `validation` is not defined

  ```nextflow
          afterText = validation.help.afterText
                      ^^^^^^^^^^
  ```

## :warning: Warnings

- Warning: `main.nf:89:28`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      fasta = params.fasta ? Channel.fromPath(params.fasta).map { it -> [[id: it.baseName], it] }.collect() : Channel.empty()
                             ^^^^^^^
  ```

- Warning: `main.nf:89:109`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      fasta = params.fasta ? Channel.fromPath(params.fasta).map { it -> [[id: it.baseName], it] }.collect() : Channel.empty()
                                                                                                              ^^^^^^^
  ```

- Warning: `main.nf:129:11`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
          ? Channel.fromPath(params.dict).map { it -> [[id: 'dict'], it] }.collect()
            ^^^^^^^
  ```

- Warning: `main.nf:132:11`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
          ? Channel.fromPath(params.fasta_fai).map { it -> [[id: 'fai'], it] }.collect()
            ^^^^^^^
  ```

- Warning: `main.nf:135:11`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
          ? Channel.fromPath(params.bwa).map { it -> [[id: 'bwa'], it] }.collect()
            ^^^^^^^
  ```

- Warning: `nextflow.config:306:129`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          afterText = """${manifest.doi ? "\n* The pipeline\n" : ""}${manifest.doi.tokenize(",").collect { "    https://doi.org/${it.trim().replace('https://doi.org/', '')}" }.join("\n")}${manifest.doi ? "\n" : ""}
                                                                                                                                  ^^
  ```

- Warning: `subworkflows/local/prepare_genome/main.nf:20:16`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      versions = Channel.empty()
                 ^^^^^^^
  ```

- Warning: `subworkflows/local/utils_nfcore_fastquorum_pipeline/main.nf:31:5`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
      monochrome_logs // boolean: Do not use coloured log outputs
      ^^^^^^^^^^^^^^^
  ```

- Warning: `subworkflows/local/utils_nfcore_fastquorum_pipeline/main.nf:34:5`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
      input //  string: Path to input samplesheet
      ^^^^^
  ```

- Warning: `subworkflows/local/utils_nfcore_fastquorum_pipeline/main.nf:38:19`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_versions = Channel.empty()
                    ^^^^^^^
  ```

- Warning: `subworkflows/local/utils_nfcore_fastquorum_pipeline/main.nf:75:5`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      Channel
      ^^^^^^^
  ```

- Warning: `subworkflows/local/utils_nfcore_fastquorum_pipeline/main.nf:83:41`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
              validateInputSamplesheetRow(it)
                                          ^^
  ```

- Warning: `subworkflows/local/utils_nfcore_fastquorum_pipeline/main.nf:88:38`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
              validateInputSamplesheet(it)
                                       ^^
  ```

- Warning: `subworkflows/local/utils_nfcore_fastquorum_pipeline/main.nf:94:31`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
                  return [meta, it]
                                ^^
  ```

- Warning: `subworkflows/local/utils_nfcore_fastquorum_pipeline/main.nf:223:49`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
      def fastqs_per_sample_ok = fastqs.collect { it.size() }.unique().size == 1
                                                  ^^
  ```

- Warning: `subworkflows/local/utils_nfcore_fastquorum_pipeline/main.nf:227:46`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
      def read_structures_ok = metas.collect { it.read_structure }.unique().size == 1
                                               ^^
  ```

- Warning: `subworkflows/nf-core/utils_nfcore_pipeline/main.nf:101:98`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      return ch_versions.unique().map { version -> processVersionsFromYAML(version) }.unique().mix(Channel.of(workflowVersionToYAML()))
                                                                                                   ^^^^^^^
  ```

- Warning: `workflows/fastquorum.nf:45:19`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_versions = Channel.empty()
                    ^^^^^^^
  ```

- Warning: `workflows/fastquorum.nf:46:24`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_multiqc_files = Channel.empty()
                         ^^^^^^^
  ```

- Warning: `workflows/fastquorum.nf:54:70`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
      ch_multiqc_files = ch_multiqc_files.mix(FASTQC.out.zip.collect { it[1] })
                                                                       ^^
  ```

- Warning: `workflows/fastquorum.nf:103:81`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
      ch_multiqc_files = ch_multiqc_files.mix(GROUPREADSBYUMI.out.histogram.map { it[1] }.collect())
                                                                                  ^^
  ```

- Warning: `workflows/fastquorum.nf:194:25`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_multiqc_config = Channel.fromPath(
                          ^^^^^^^
  ```

- Warning: `workflows/fastquorum.nf:199:11`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
          ? Channel.fromPath(params.multiqc_config, checkIfExists: true)
            ^^^^^^^
  ```

- Warning: `workflows/fastquorum.nf:200:11`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
          : Channel.empty()
            ^^^^^^^
  ```

- Warning: `workflows/fastquorum.nf:202:11`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
          ? Channel.fromPath(params.multiqc_logo, checkIfExists: true)
            ^^^^^^^
  ```

- Warning: `workflows/fastquorum.nf:203:11`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
          : Channel.empty()
            ^^^^^^^
  ```

- Warning: `workflows/fastquorum.nf:209:27`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_workflow_summary = Channel.value(paramsSummaryMultiqc(summary_params))
                            ^^^^^^^
  ```

- Warning: `workflows/fastquorum.nf:216:30`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_methods_description = Channel.value(
                               ^^^^^^^
  ```
