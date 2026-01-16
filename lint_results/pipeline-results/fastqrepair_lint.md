# Nextflow lint results

- Generated: 2026-01-16T10:20:46.897160443Z
- Nextflow version: 25.12.0-edge
- Summary: 9 errors, 32 warnings

## :x: Errors

- Error: `nextflow.config:270:35`: `manifest` is not defined

  ```nextflow
          command = "nextflow run ${manifest.name} -profile <docker/singularity/.../institute> --input samplesheet.csv --outdir <OUTDIR>"
                                    ^^^^^^^^
  ```

- Error: `nextflow.config:280:15`: `manifest` is not defined

  ```nextflow
  \033[0;35m  ${manifest.name} ${manifest.version}\033[0m
                ^^^^^^^^
  ```

- Error: `nextflow.config:280:32`: `manifest` is not defined

  ```nextflow
  \033[0;35m  ${manifest.name} ${manifest.version}\033[0m
                                 ^^^^^^^^
  ```

- Error: `nextflow.config:283:26`: `manifest` is not defined

  ```nextflow
          afterText = """${manifest.doi ? "* The pipeline\n" : ""}${manifest.doi.tokenize(",").collect { "  https://doi.org/${it.trim().replace('https://doi.org/', '')}" }.join("\n")}${manifest.doi ? "\n" : ""}
                           ^^^^^^^^
  ```

- Error: `nextflow.config:283:67`: `manifest` is not defined

  ```nextflow
          afterText = """${manifest.doi ? "* The pipeline\n" : ""}${manifest.doi.tokenize(",").collect { "  https://doi.org/${it.trim().replace('https://doi.org/', '')}" }.join("\n")}${manifest.doi ? "\n" : ""}
                                                                    ^^^^^^^^
  ```

- Error: `nextflow.config:283:184`: `manifest` is not defined

  ```nextflow
          afterText = """${manifest.doi ? "* The pipeline\n" : ""}${manifest.doi.tokenize(",").collect { "  https://doi.org/${it.trim().replace('https://doi.org/', '')}" }.join("\n")}${manifest.doi ? "\n" : ""}
                                                                                                                                                                                         ^^^^^^^^
  ```

- Error: `nextflow.config:288:26`: `manifest` is not defined

  ```nextflow
      https://github.com/${manifest.name}/blob/master/CITATIONS.md
                           ^^^^^^^^
  ```

- Error: `nextflow.config:292:22`: `validation` is not defined

  ```nextflow
          beforeText = validation.help.beforeText
                       ^^^^^^^^^^
  ```

- Error: `nextflow.config:293:21`: `validation` is not defined

  ```nextflow
          afterText = validation.help.afterText
                      ^^^^^^^^^^
  ```

## :warning: Warnings

- Warning: `modules/nf-core/wipertools/fastqgather/main.nf:25:21`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
      if (fastq.any { it.name == "${prefix}.fastq.gz" }) {
                      ^^
  ```

- Warning: `modules/nf-core/wipertools/fastqgather/main.nf:46:21`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
      if (fastq.any { it.name == "${prefix}.fastq.gz" }) {
                      ^^
  ```

- Warning: `modules/nf-core/wipertools/reportgather/main.nf:25:22`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
      if (report.any { it.name == "${prefix}.report" }) {
                       ^^
  ```

- Warning: `modules/nf-core/wipertools/reportgather/main.nf:46:22`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
      if (report.any { it.name == "${prefix}.report" }) {
                       ^^
  ```

- Warning: `nextflow.config:283:125`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          afterText = """${manifest.doi ? "* The pipeline\n" : ""}${manifest.doi.tokenize(",").collect { "  https://doi.org/${it.trim().replace('https://doi.org/', '')}" }.join("\n")}${manifest.doi ? "\n" : ""}
                                                                                                                              ^^
  ```

- Warning: `subworkflows/local/fastq_repair_wipertools/main.nf:12:19`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_versions = Channel.empty()
                    ^^^^^^^
  ```

- Warning: `subworkflows/local/fastq_repair_wipertools/main.nf:46:24`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_cleaned_fastq = Channel.empty()
                         ^^^^^^^
  ```

- Warning: `subworkflows/local/fastq_repair_wipertools/main.nf:60:26`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_gathered_report = Channel.empty()
                           ^^^^^^^
  ```

- Warning: `subworkflows/local/fastq_repair_wipertools/main.nf:68:24`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_final_reports = Channel.empty()
                         ^^^^^^^
  ```

- Warning: `subworkflows/local/utils_nfcore_fastqrepair_pipeline/main.nf:31:5`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
      monochrome_logs   // boolean: Do not use coloured log outputs
      ^^^^^^^^^^^^^^^
  ```

- Warning: `subworkflows/local/utils_nfcore_fastqrepair_pipeline/main.nf:34:5`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
      input             //  string: Path to input samplesheet
      ^^^^^
  ```

- Warning: `subworkflows/local/utils_nfcore_fastqrepair_pipeline/main.nf:37:19`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_versions = Channel.empty()
                    ^^^^^^^
  ```

- Warning: `subworkflows/local/utils_nfcore_fastqrepair_pipeline/main.nf:69:5`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      Channel
      ^^^^^^^
  ```

- Warning: `subworkflows/nf-core/utils_nfcore_pipeline/main.nf:101:98`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      return ch_versions.unique().map { version -> processVersionsFromYAML(version) }.unique().mix(Channel.of(workflowVersionToYAML()))
                                                                                                   ^^^^^^^
  ```

- Warning: `workflows/fastqrepair.nf:29:16`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_final = Channel.empty()      // channel: repaired fastq files
                 ^^^^^^^
  ```

- Warning: `workflows/fastqrepair.nf:30:19`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_versions = Channel.empty()   // channel: versions of the software used in the pipeline
                    ^^^^^^^
  ```

- Warning: `workflows/fastqrepair.nf:33:20`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_fastq_ext = Channel.empty()
                     ^^^^^^^
  ```

- Warning: `workflows/fastqrepair.nf:47:26`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_tobewiped_fastq = Channel.empty()
                           ^^^^^^^
  ```

- Warning: `workflows/fastqrepair.nf:76:25`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_repaired_fastq = Channel.empty()
                          ^^^^^^^
  ```

- Warning: `workflows/fastqrepair.nf:84:21`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          single_end: it[0].single_end == true
                      ^^
  ```

- Warning: `workflows/fastqrepair.nf:85:21`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          paired_end: it[0].single_end == false }
                      ^^
  ```

- Warning: `workflows/fastqrepair.nf:89:36`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_repaired_fastq_paired_end = Channel.empty()
                                     ^^^^^^^
  ```

- Warning: `workflows/fastqrepair.nf:101:50`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
          ch_repaired_fastq_paired_end_singleton = Channel.empty()
                                                   ^^^^^^^
  ```

- Warning: `workflows/fastqrepair.nf:131:24`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_multiqc_files = Channel.empty()
                         ^^^^^^^
  ```

- Warning: `workflows/fastqrepair.nf:132:68`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
      ch_multiqc_files = ch_multiqc_files.mix(FASTQC.out.zip.collect{it[1]})
                                                                     ^^
  ```

- Warning: `workflows/fastqrepair.nf:134:25`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_multiqc_config = Channel.fromPath("$projectDir/assets/multiqc_config.yml", checkIfExists: true)
                          ^^^^^^^
  ```

- Warning: `workflows/fastqrepair.nf:135:56`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_multiqc_custom_config = params.multiqc_config ? Channel.fromPath(params.multiqc_config, checkIfExists: true) : Channel.empty()
                                                         ^^^^^^^
  ```

- Warning: `workflows/fastqrepair.nf:135:119`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_multiqc_custom_config = params.multiqc_config ? Channel.fromPath(params.multiqc_config, checkIfExists: true) : Channel.empty()
                                                                                                                        ^^^^^^^
  ```

- Warning: `workflows/fastqrepair.nf:137:9`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
          Channel.fromPath(params.multiqc_logo, checkIfExists: true) :
          ^^^^^^^
  ```

- Warning: `workflows/fastqrepair.nf:138:9`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
          Channel.empty()
          ^^^^^^^
  ```

- Warning: `workflows/fastqrepair.nf:142:27`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_workflow_summary = Channel.value(paramsSummaryMultiqc(summary_params))
                            ^^^^^^^
  ```

- Warning: `workflows/fastqrepair.nf:148:45`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_methods_description                = Channel.value(
                                              ^^^^^^^
  ```
