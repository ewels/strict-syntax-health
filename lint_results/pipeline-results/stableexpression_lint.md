# Nextflow lint results

- Generated: 2026-09-05T00:21:08.466477174Z
- Nextflow version: 26.08.0-edge
- Summary: 32 warnings

## :warning: Warnings

- Warning: `main.nf:169:16`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          path { meta, file ->
                 ^^^^
  ```

- Warning: `main.nf:175:16`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          path { meta, file ->
                 ^^^^
  ```

- Warning: `modules/local/compute_dataset_statistics/main.nf:21:9`: Variable was declared but not used

  ```nextflow
      def prefix = task.ext.prefix ?: "${meta.dataset}"
          ^^^^^^
  ```

- Warning: `modules/local/expressionatlas/getaccessions/main.nf:31:57`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
      def keywords_string = keywords.split(',').collect { it.trim() }.join(' ')
                                                          ^^
  ```

- Warning: `modules/local/geo/getaccessions/main.nf:33:57`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
      def keywords_string = keywords.split(',').collect { it.trim() }.join(' ')
                                                          ^^
  ```

- Warning: `subworkflows/local/download_public_datasets/main.nf:24:5`: Variable was declared but not used

  ```nextflow
      ch_fetched_accessions = channel.empty()
      ^^^^^^^^^^^^^^^^^^^^^
  ```

- Warning: `subworkflows/local/expression_normalisation/main.nf:34:15`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          meta, file ->
                ^^^^
  ```

- Warning: `subworkflows/local/expression_normalisation/main.nf:39:74`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
      ch_raw_rnaseq_datasets_to_normalise = ch_datasets.raw.filter { meta, file -> meta.platform == 'rnaseq' }
                                                                           ^^^^
  ```

- Warning: `subworkflows/local/genorm/main.nf:94:17`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
                  meta, i, file_i, j, file_j -> i <= j } // keeps only pairs where i <= j
                  ^^^^
  ```

- Warning: `subworkflows/local/genorm/main.nf:94:26`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
                  meta, i, file_i, j, file_j -> i <= j } // keeps only pairs where i <= j
                           ^^^^^^
  ```

- Warning: `subworkflows/local/genorm/main.nf:94:37`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
                  meta, i, file_i, j, file_j -> i <= j } // keeps only pairs where i <= j
                                      ^^^^^^
  ```

- Warning: `subworkflows/local/get_public_accessions/main.nf:79:35`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
                          .filter { species_name, quota -> quota == "ok" }
                                    ^^^^^^^^^^^^
  ```

- Warning: `subworkflows/local/get_public_accessions/main.nf:80:46`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
                          .map { species_name, quota -> species_name }
                                               ^^^^^
  ```

- Warning: `subworkflows/local/get_public_accessions/main.nf:117:55`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
                                      .map { accession, excluded_accessions -> accession }
                                                        ^^^^^^^^^^^^^^^^^^^
  ```

- Warning: `subworkflows/local/idmapping/main.nf:63:40`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
                                  .map { it.trim() }
                                         ^^
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

- Warning: `subworkflows/local/merge_data/main.nf:71:35`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
                              meta, file -> // extracts design file and adds batch column whenever missing (for custom datasets)
                                    ^^^^
  ```

- Warning: `subworkflows/local/reporting/main.nf:46:32`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
                          .map { it.trim() }
                                 ^^
  ```

- Warning: `subworkflows/local/reporting/main.nf:47:35`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
                          .filter { it != "" }
                                    ^^
  ```

- Warning: `subworkflows/local/reporting/main.nf:57:28`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          ch_all_counts.map{ meta, file -> file }.collect(), // 1 file
                             ^^^^
  ```

- Warning: `subworkflows/local/reporting/main.nf:76:28`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          ch_all_counts.map{ meta, file -> file }.collect(),
                             ^^^^
  ```

- Warning: `subworkflows/local/reporting/main.nf:397:50`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
      ch_multiqc_report = MULTIQC.out.report.map { meta, file -> file }
                                                   ^^^^
  ```

- Warning: `subworkflows/local/utils_nfcore_stableexpression_pipeline/main.nf:33:5`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
      input             //  string: Path to input samplesheet
      ^^^^^
  ```

- Warning: `subworkflows/local/utils_nfcore_stableexpression_pipeline/main.nf:249:19`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
              meta, file ->
                    ^^^^
  ```

- Warning: `subworkflows/local/utils_nfcore_stableexpression_pipeline/main.nf:266:16`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          .map { meta, file ->
                 ^^^^
  ```

- Warning: `subworkflows/local/utils_nfcore_stableexpression_pipeline/main.nf:387:13`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
              it.get(1).size() == 2 // only groups with two files
              ^^
  ```

- Warning: `subworkflows/local/utils_nfcore_stableexpression_pipeline/main.nf:390:13`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
              meta, files ->
              ^^^^
  ```

- Warning: `workflows/stableexpression.nf:195:40`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
              ch_all_imputed_counts.map{ meta, file -> file },
                                         ^^^^
  ```
