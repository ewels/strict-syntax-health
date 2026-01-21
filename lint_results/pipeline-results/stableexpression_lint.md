# Nextflow lint results

- Generated: 2026-01-21T13:34:39.721898593Z
- Nextflow version: 25.12.0-edge
- Summary: 30 warnings

## :warning: Warnings

- Warning: `modules/local/compute_dataset_statistics/main.nf:22:9`: Variable was declared but not used

  ```nextflow
      def prefix = task.ext.prefix ?: "${meta.dataset}"
          ^^^^^^
  ```

- Warning: `modules/local/expressionatlas/getaccessions/main.nf:33:57`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
      def keywords_string = keywords.split(',').collect { it.trim() }.join(' ')
                                                          ^^
  ```

- Warning: `modules/local/genorm/expression_ratio/main.nf:20:9`: Variable was declared but not used

  ```nextflow
      def args = "--task-attempts ${task.attempt}"
          ^^^^
  ```

- Warning: `modules/local/geo/getaccessions/main.nf:34:57`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
      def keywords_string = keywords.split(',').collect { it.trim() }.join(' ')
                                                          ^^
  ```

- Warning: `subworkflows/local/download_public_datasets/main.nf:24:5`: Variable was declared but not used

  ```nextflow
      ch_fetched_accessions = channel.empty()
      ^^^^^^^^^^^^^^^^^^^^^
  ```

- Warning: `subworkflows/local/expression_normalisation/main.nf:20:5`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
      gene_length
      ^^^^^^^^^^^
  ```

- Warning: `subworkflows/local/expression_normalisation/main.nf:30:15`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          meta, file ->
                ^^^^
  ```

- Warning: `subworkflows/local/expression_normalisation/main.nf:35:74`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
      ch_raw_rnaseq_datasets_to_normalise = ch_datasets.raw.filter { meta, file -> meta.platform == 'rnaseq' }
                                                                           ^^^^
  ```

- Warning: `subworkflows/local/get_public_accessions/main.nf:77:35`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
                          .filter { species_name, quota -> quota == "ok" }
                                    ^^^^^^^^^^^^
  ```

- Warning: `subworkflows/local/get_public_accessions/main.nf:78:46`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
                          .map { species_name, quota -> species_name }
                                               ^^^^^
  ```

- Warning: `subworkflows/local/get_public_accessions/main.nf:114:55`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
                                      .map { accession, excluded_accessions -> accession }
                                                        ^^^^^^^^^^^^^^^^^^^
  ```

- Warning: `subworkflows/local/merge_data/main.nf:25:71`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
      ch_normalised_rnaseq_counts = ch_normalised_counts.filter { meta, file -> meta.platform == "rnaseq" }
                                                                        ^^^^
  ```

- Warning: `subworkflows/local/merge_data/main.nf:26:75`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
      ch_normalised_microarray_counts = ch_normalised_counts.filter { meta, file -> meta.platform == "microarray" }
                                                                            ^^^^
  ```

- Warning: `subworkflows/local/merge_data/main.nf:29:44`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
                                      .map { meta, file -> file }
                                             ^^^^
  ```

- Warning: `subworkflows/local/merge_data/main.nf:34:48`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
                                          .map { meta, file -> file }
                                                 ^^^^
  ```

- Warning: `subworkflows/local/merge_data/main.nf:49:44`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
                                      .map { meta, file -> file }
                                             ^^^^
  ```

- Warning: `subworkflows/local/merge_data/main.nf:61:35`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
                              meta, file -> // extracts design file and adds batch column whenever missing (for custom datasets)
                                    ^^^^
  ```

- Warning: `subworkflows/local/merge_data/main.nf:87:43`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
                                  .filter { it != [] } // handle case where there are no mappings
                                            ^^
  ```

- Warning: `subworkflows/local/merge_data/main.nf:106:43`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
                                  .filter { it != [] } // handle case where there are no mappings
                                            ^^
  ```

- Warning: `subworkflows/local/utils_nfcore_stableexpression_pipeline/main.nf:31:5`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
      monochrome_logs   // boolean: Do not use coloured log outputs
      ^^^^^^^^^^^^^^^
  ```

- Warning: `subworkflows/local/utils_nfcore_stableexpression_pipeline/main.nf:34:5`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
      input             //  string: Path to input samplesheet
      ^^^^^
  ```

- Warning: `subworkflows/local/utils_nfcore_stableexpression_pipeline/main.nf:235:19`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
              meta, file ->
                    ^^^^
  ```

- Warning: `subworkflows/local/utils_nfcore_stableexpression_pipeline/main.nf:252:16`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          .map { meta, file ->
                 ^^^^
  ```

- Warning: `subworkflows/local/utils_nfcore_stableexpression_pipeline/main.nf:354:13`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
              it.get(1).size() == 2 // only groups with two files
              ^^
  ```

- Warning: `subworkflows/local/utils_nfcore_stableexpression_pipeline/main.nf:357:13`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
              meta, files ->
              ^^^^
  ```

- Warning: `subworkflows/nf-core/utils_nfcore_pipeline/main.nf:101:98`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      return ch_versions.unique().map { version -> processVersionsFromYAML(version) }.unique().mix(Channel.of(workflowVersionToYAML()))
                                                                                                   ^^^^^^^
  ```

- Warning: `workflows/stableexpression.nf:44:5`: Variable was declared but not used

  ```nextflow
      ch_all_genes_statistics = channel.empty()
      ^^^^^^^^^^^^^^^^^^^^^^^
  ```

- Warning: `workflows/stableexpression.nf:163:32`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
              ch_all_counts.map{ meta, file -> file },
                                 ^^^^
  ```

- Warning: `workflows/stableexpression.nf:180:32`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
              ch_all_counts.map{ meta, file -> file }.collect(),
                                 ^^^^
  ```

- Warning: `workflows/stableexpression.nf:196:32`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
              ch_all_counts.map{ meta, file -> file }.collect(),
                                 ^^^^
  ```
