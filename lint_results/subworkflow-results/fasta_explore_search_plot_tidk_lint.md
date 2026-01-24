# Nextflow lint results

- Generated: 2026-01-24T00:20:36.575175+00:00
- Nextflow version: 25.12.0-edge
- Summary: 9 warnings

## :warning: Warnings

- Warning: `subworkflows/nf-core/fasta_explore_search_plot_tidk/main.nf:19:19`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_versions = Channel.empty()
                    ^^^^^^^^^^
  ```

- Warning: `subworkflows/nf-core/fasta_explore_search_plot_tidk/main.nf:43:58`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
                                  ( ch_apriori_sequence ?: Channel.empty() )
                                                           ^^^^^^^^^^
  ```

- Warning: `subworkflows/nf-core/fasta_explore_search_plot_tidk/main.nf:46:37`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
                              | map { id, meta, fasta, seq -> [ meta, fasta, seq ] }
                                      ^^^^^^^^^^
  ```

- Warning: `subworkflows/nf-core/fasta_explore_search_plot_tidk/main.nf:49:46`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          ch_apriori_inputs.map { meta, fasta, seq -> [ meta, fasta ] },
                                               ^^^^^^^^^^
  ```

- Warning: `subworkflows/nf-core/fasta_explore_search_plot_tidk/main.nf:50:33`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          ch_apriori_inputs.map { meta, fasta, seq -> seq }
                                  ^^^^^^^^^^
  ```

- Warning: `subworkflows/nf-core/fasta_explore_search_plot_tidk/main.nf:50:39`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          ch_apriori_inputs.map { meta, fasta, seq -> seq }
                                        ^^^^^^^^^^
  ```

- Warning: `subworkflows/nf-core/fasta_explore_search_plot_tidk/main.nf:64:50`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          ch_aposteriori_inputs.map { meta, fasta, seq -> [ meta, fasta ] },
                                                   ^^^^^^^^^^
  ```

- Warning: `subworkflows/nf-core/fasta_explore_search_plot_tidk/main.nf:65:37`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          ch_aposteriori_inputs.map { meta, fasta, seq -> seq }
                                      ^^^^^^^^^^
  ```

- Warning: `subworkflows/nf-core/fasta_explore_search_plot_tidk/main.nf:65:43`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          ch_aposteriori_inputs.map { meta, fasta, seq -> seq }
                                            ^^^^^^^^^^
  ```
