# Nextflow lint results

- Generated: 2026-09-10T00:21:23.560176782Z
- Nextflow version: 26.08.0-edge
- Summary: 1 warning

## :warning: Warnings

- Warning: `workflows/rnastructurome.nf:74:9`: Variable was declared but not used

  ```nextflow
      def ch_fastqc_post_gate = FASTQ_QC_TRIM.out.fastqc_post_zip.map { meta, zips ->
          ^^^^^^^^^^^^^^^^^^^
  ```
