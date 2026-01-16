# Nextflow lint results

- Generated: 2026-01-16T06:34:42.024872707Z
- Nextflow version: 25.12.0-edge
- Summary: 11 errors, 34 warnings

## :x: Errors

- Error: `modules/local/collect_stats.nf:24:5`: Invalid process output

  ```nextflow
      def score_threshold = params.pred_method != "SYFPEITHI" ? params.mhcflurry_mhcnuggets_score_threshold : params.syfpeithi_score_threshold
      ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  ```

- Error: `modules/local/collect_stats.nf:34:41`: `score_threshold` is not defined

  ```nextflow
                      --binder_threshold "$score_threshold"               \\
                                          ^^^^^^^^^^^^^^^^
  ```

- Error: `modules/local/download_proteins.nf:27:9`: `microbiome_ids` is already declared

  ```nextflow
      def microbiome_ids = microbiome_ids.join(' ')
          ^^^^^^^^^^^^^^
  ```

- Error: `modules/local/unify_model_lengths.nf:15:9`: `unified_peptide_lengths` is not defined

  ```nextflow
      env unified_peptide_lengths       , emit: unified_pep_lens
          ^^^^^^^^^^^^^^^^^^^^^^^
  ```

- Error: `nextflow.config:324:31`: `manifest` is not defined

  ```nextflow
  \033[0;35m  nf-core/metapep ${manifest.version}\033[0m
                                ^^^^^^^^
  ```

- Error: `nextflow.config:327:26`: `manifest` is not defined

  ```nextflow
          afterText = """${manifest.doi ? "\n* The pipeline\n" : ""}${manifest.doi.tokenize(",").collect { "    https://doi.org/${it.trim().replace('https://doi.org/','')}"}.join("\n")}${manifest.doi ? "\n" : ""}
                           ^^^^^^^^
  ```

- Error: `nextflow.config:327:69`: `manifest` is not defined

  ```nextflow
          afterText = """${manifest.doi ? "\n* The pipeline\n" : ""}${manifest.doi.tokenize(",").collect { "    https://doi.org/${it.trim().replace('https://doi.org/','')}"}.join("\n")}${manifest.doi ? "\n" : ""}
                                                                      ^^^^^^^^
  ```

- Error: `nextflow.config:327:186`: `manifest` is not defined

  ```nextflow
          afterText = """${manifest.doi ? "\n* The pipeline\n" : ""}${manifest.doi.tokenize(",").collect { "    https://doi.org/${it.trim().replace('https://doi.org/','')}"}.join("\n")}${manifest.doi ? "\n" : ""}
                                                                                                                                                                                           ^^^^^^^^
  ```

- Error: `nextflow.config:336:22`: `validation` is not defined

  ```nextflow
          beforeText = validation.help.beforeText
                       ^^^^^^^^^^
  ```

- Error: `nextflow.config:337:21`: `validation` is not defined

  ```nextflow
          afterText = validation.help.afterText
                      ^^^^^^^^^^
  ```

- Error: `subworkflows/local/process_input.nf:136:103`: `microbiome_id` is not defined

  ```nextflow
                      if (bin_files.isEmpty()) log.warn("WARNING - Archive provided for microbiome ID ${microbiome_id} did not yield any bin files")
                                                                                                        ^^^^^^^^^^^^^
  ```

## :warning: Warnings

- Warning: `nextflow.config:327:129`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          afterText = """${manifest.doi ? "\n* The pipeline\n" : ""}${manifest.doi.tokenize(",").collect { "    https://doi.org/${it.trim().replace('https://doi.org/','')}"}.join("\n")}${manifest.doi ? "\n" : ""}
                                                                                                                                  ^^
  ```

- Warning: `subworkflows/local/process_input.nf:15:19`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_versions = Channel.empty()
                    ^^^^^^^
  ```

- Warning: `subworkflows/local/process_input.nf:39:27`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
          peptide_lengths = Channel.fromList( params.min_pep_len..params.max_pep_len )
                            ^^^^^^^
  ```

- Warning: `subworkflows/local/process_input.nf:102:78`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
                      def bin_files = row.microbiome_path.listFiles().findAll{ it.name =~ fasta_suffix }
                                                                               ^^
  ```

- Warning: `subworkflows/local/process_input.nf:106:45`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
                          meta.bin_basename = it.name - fasta_suffix
                                              ^^
  ```

- Warning: `subworkflows/local/process_input.nf:107:40`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
                          return [ meta, it ]
                                         ^^
  ```

- Warning: `subworkflows/local/process_input.nf:132:34`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
          ch_bins_archives_input = Channel.empty()
                                   ^^^^^^^
  ```

- Warning: `subworkflows/local/process_input.nf:135:52`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
                      bin_files = bin_files.findAll{ it.name =~ fasta_suffix }
                                                     ^^
  ```

- Warning: `subworkflows/local/process_input.nf:140:49`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
                          meta_new.bin_basename = it.name - fasta_suffix
                                                  ^^
  ```

- Warning: `subworkflows/local/process_input.nf:141:44`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
                          return [ meta_new, it ]
                                             ^^
  ```

- Warning: `subworkflows/local/process_input.nf:154:22`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
          ch_weights = Channel.empty()
                       ^^^^^^^
  ```

- Warning: `subworkflows/local/utils_nfcore_metapep_pipeline/main.nf:31:5`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
      monochrome_logs   // boolean: Do not use coloured log outputs
      ^^^^^^^^^^^^^^^
  ```

- Warning: `subworkflows/local/utils_nfcore_metapep_pipeline/main.nf:38:19`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_versions = Channel.empty()
                    ^^^^^^^
  ```

- Warning: `subworkflows/local/utils_nfcore_metapep_pipeline/main.nf:69:53`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_samplesheet = params.show_supported_models ? Channel.empty() : Channel.fromPath(input, checkIfExists: true)
                                                      ^^^^^^^
  ```

- Warning: `subworkflows/local/utils_nfcore_metapep_pipeline/main.nf:69:71`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_samplesheet = params.show_supported_models ? Channel.empty() : Channel.fromPath(input, checkIfExists: true)
                                                                        ^^^^^^^
  ```

- Warning: `subworkflows/nf-core/utils_nfcore_pipeline/main.nf:101:98`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      return ch_versions.unique().map { version -> processVersionsFromYAML(version) }.unique().mix(Channel.of(workflowVersionToYAML()))
                                                                                                   ^^^^^^^
  ```

- Warning: `workflows/metapep.nf:49:19`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_versions = Channel.empty()
                    ^^^^^^^
  ```

- Warning: `workflows/metapep.nf:50:24`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_multiqc_files = Channel.empty()
                         ^^^^^^^
  ```

- Warning: `workflows/metapep.nf:71:57`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
              PROCESS_INPUT.out.ch_taxa_input.map { meta, file -> meta.id }.collect(),
                                                          ^^^^
  ```

- Warning: `workflows/metapep.nf:72:51`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
              PROCESS_INPUT.out.ch_taxa_input.map { meta, file -> file }.collect()
                                                    ^^^^
  ```

- Warning: `workflows/metapep.nf:94:54`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
              PROCESS_INPUT.out.ch_weights.map { meta, file -> meta.id }.collect().ifEmpty([]),
                                                       ^^^^
  ```

- Warning: `workflows/metapep.nf:95:48`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
              PROCESS_INPUT.out.ch_weights.map { meta, file -> file }.collect().ifEmpty([])
                                                 ^^^^
  ```

- Warning: `workflows/metapep.nf:108:47`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
              ch_pred_proteins_sorted.collect { meta, file -> file }.ifEmpty([]),
                                                ^^^^
  ```

- Warning: `workflows/metapep.nf:109:53`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
              ch_pred_proteins_sorted.collect { meta, file -> meta }.ifEmpty([]),
                                                      ^^^^
  ```

- Warning: `workflows/metapep.nf:203:61`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
              ch_merge_predictions_input_pred.collect(sort: { it.baseName }),
                                                              ^^
  ```

- Warning: `workflows/metapep.nf:204:61`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
              ch_merge_predictions_input_warn.collect(sort: { it.baseName })
                                                              ^^
  ```

- Warning: `workflows/metapep.nf:281:32`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_multiqc_config        = Channel.fromPath(
                                 ^^^^^^^
  ```

- Warning: `workflows/metapep.nf:284:9`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
          Channel.fromPath(params.multiqc_config, checkIfExists: true) :
          ^^^^^^^
  ```

- Warning: `workflows/metapep.nf:285:9`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
          Channel.empty()
          ^^^^^^^
  ```

- Warning: `workflows/metapep.nf:287:9`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
          Channel.fromPath(params.multiqc_logo, checkIfExists: true) :
          ^^^^^^^
  ```

- Warning: `workflows/metapep.nf:288:9`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
          Channel.fromPath("$projectDir/assets/nf-core-metapep_logo_light.png")
          ^^^^^^^
  ```

- Warning: `workflows/metapep.nf:292:27`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_workflow_summary = Channel.value(paramsSummaryMultiqc(summary_params))
                            ^^^^^^^
  ```

- Warning: `workflows/metapep.nf:298:45`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_methods_description                = Channel.value(
                                              ^^^^^^^
  ```

- Warning: `workflows/metapep.nf:321:5`: Variable was declared but not used

  ```nextflow
      multiqc_report = MULTIQC.out.report.toList()
      ^^^^^^^^^^^^^^
  ```
