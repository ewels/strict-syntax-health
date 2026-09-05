# Nextflow lint results

- Generated: 2026-09-05T00:22:14.742254743Z
- Nextflow version: 26.08.0-edge
- Summary: 3 warnings

## :warning: Warnings

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
