# Nextflow lint results

- Generated: 2026-01-24T00:20:24.567307+00:00
- Nextflow version: 25.12.0-edge
- Summary: 1 warning

## :warning: Warnings

- Warning: `modules/nf-core/agat/spmergeannotations/main.nf:26:54`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
      def gff_param    = file_names.collect { "--gff ${it}" }.join(' ')
                                                       ^^^^^^^^^^
  ```
