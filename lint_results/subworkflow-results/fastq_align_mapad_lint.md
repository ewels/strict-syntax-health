# Nextflow lint results

- Generated: 2026-01-21T13:35:35.514893+00:00
- Nextflow version: 25.12.0-edge
- Summary: 2 warnings

## :warning: Warnings

- Warning: `subworkflows/nf-core/fastq_align_mapad/main.nf:25:19`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_versions = Channel.empty()
                    ^^^^^^^^^^
  ```

- Warning: `subworkflows/nf-core/fastq_align_mapad/main.nf:52:42`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
                              meta, reads, meta_index, index ->
                                           ^^^^^^^^^^
  ```
