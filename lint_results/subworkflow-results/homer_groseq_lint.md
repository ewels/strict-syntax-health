# Nextflow lint results

- Generated: 2026-01-24T00:20:36.580198+00:00
- Nextflow version: 25.12.0-edge
- Summary: 3 warnings

## :warning: Warnings

- Warning: `subworkflows/nf-core/homer_groseq/main.nf:20:19`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_versions = Channel.empty()
                    ^^^^^^^^^^
  ```

- Warning: `subworkflows/nf-core/homer_groseq/main.nf:22:18`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_uniqmap = Channel.empty()
                   ^^^^^^^^^^
  ```

- Warning: `subworkflows/nf-core/homer_groseq/main.nf:28:67`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          ch_uniqmap = UNZIP([[:], uniqmap]).unzipped_archive.map { it[1] }
                                                                    ^^^^^^^
  ```
