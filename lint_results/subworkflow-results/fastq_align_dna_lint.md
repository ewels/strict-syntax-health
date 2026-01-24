# Nextflow lint results

- Generated: 2026-01-24T00:20:36.577428+00:00
- Nextflow version: 25.12.0-edge
- Summary: 4 warnings

## :warning: Warnings

- Warning: `subworkflows/nf-core/fastq_align_dna/main.nf:27:27`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
          ch_bam_index    = Channel.empty()
                            ^^^^^^^^^^
  ```

- Warning: `subworkflows/nf-core/fastq_align_dna/main.nf:28:27`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
          ch_bam          = Channel.empty()
                            ^^^^^^^^^^
  ```

- Warning: `subworkflows/nf-core/fastq_align_dna/main.nf:29:27`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
          ch_reports      = Channel.empty()
                            ^^^^^^^^^^
  ```

- Warning: `subworkflows/nf-core/fastq_align_dna/main.nf:30:27`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
          ch_versions     = Channel.empty()
                            ^^^^^^^^^^
  ```
