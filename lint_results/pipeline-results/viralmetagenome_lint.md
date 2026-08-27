# Nextflow lint results

- Generated: 2026-08-27T01:29:14.861046354Z
- Nextflow version: 26.08.0-edge
- Summary: 4 warnings

## :warning: Warnings

- Warning: `subworkflows/local/fasta_contig_preclust/main.nf:16:5`: Variable was declared but not used

  ```nextflow
      ch_versions = channel.empty()
      ^^^^^^^^^^^
  ```

- Warning: `subworkflows/local/utils_nfcore_viralmetagenome_pipeline/tests/lazymap_test.nf:19:23`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      parsed          = Channel.value(parsed_map)
                        ^^^^^^^
  ```

- Warning: `subworkflows/local/utils_nfcore_viralmetagenome_pipeline/tests/lazymap_test.nf:20:23`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      class_name      = Channel.value(parsed_map.getClass().name)
                        ^^^^^^^
  ```

- Warning: `subworkflows/local/utils_nfcore_viralmetagenome_pipeline/tests/lazymap_test.nf:21:23`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      is_serializable = Channel.value(parsed_map instanceof java.io.Serializable)
                        ^^^^^^^
  ```
