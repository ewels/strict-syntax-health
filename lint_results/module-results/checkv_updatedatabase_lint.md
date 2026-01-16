# Nextflow lint results

- Generated: 2026-01-16T02:02:17.545922+00:00
- Nextflow version: 25.12.0-edge
- Summary: 3 warnings

## :warning: Warnings

- Warning: `modules/nf-core/checkv/updatedatabase/main.nf:40:9`: Variable was declared but not used

  ```nextflow
      def args = task.ext.args ?: ''
          ^^^^^^^^^^
  ```

- Warning: `modules/nf-core/checkv/updatedatabase/main.nf:42:9`: Variable was declared but not used

  ```nextflow
      def checkv_db = db ?: ''
          ^^^^^^^^^^
  ```

- Warning: `modules/nf-core/checkv/updatedatabase/main.nf:43:9`: Variable was declared but not used

  ```nextflow
      def update_sequence = fasta ?: ''
          ^^^^^^^^^^
  ```
