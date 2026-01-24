# Nextflow lint results

- Generated: 2026-01-24T00:20:24.613046+00:00
- Nextflow version: 25.12.0-edge
- Summary: 3 warnings

## :warning: Warnings

- Warning: `modules/nf-core/instrain/profile/main.nf:52:9`: Variable was declared but not used

  ```nextflow
      def args = task.ext.args ?: ''
          ^^^^^^^^^^
  ```

- Warning: `modules/nf-core/instrain/profile/main.nf:54:9`: Variable was declared but not used

  ```nextflow
      def genes_args = genes_fasta ? "-g ${genes_fasta}": ''
          ^^^^^^^^^^
  ```

- Warning: `modules/nf-core/instrain/profile/main.nf:55:9`: Variable was declared but not used

  ```nextflow
      def stb_args = stb_file ? "-s ${stb_file}": ''
          ^^^^^^^^^^
  ```
