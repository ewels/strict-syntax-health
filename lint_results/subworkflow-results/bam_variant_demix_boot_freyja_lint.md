# Nextflow lint results

- Generated: 2026-01-21T13:35:35.507580+00:00
- Nextflow version: 25.12.0-edge
- Summary: 4 warnings

## :warning: Warnings

- Warning: `subworkflows/nf-core/bam_variant_demix_boot_freyja/main.nf:18:19`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_versions = Channel.empty()
                    ^^^^^^^^^^
  ```

- Warning: `subworkflows/nf-core/bam_variant_demix_boot_freyja/main.nf:51:5`: Variable was declared but not used

  ```nextflow
      ch_freyja_demix = FREYJA_DEMIX.out.demix
      ^^^^^^^^^^
  ```

- Warning: `subworkflows/nf-core/bam_variant_demix_boot_freyja/main.nf:58:21`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_lineages   = Channel.empty()
                      ^^^^^^^^^^
  ```

- Warning: `subworkflows/nf-core/bam_variant_demix_boot_freyja/main.nf:59:21`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_summarized = Channel.empty()
                      ^^^^^^^^^^
  ```
