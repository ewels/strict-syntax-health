# Nextflow lint results

- Generated: 2026-01-16T02:02:17.607580+00:00
- Nextflow version: 25.12.0-edge
- Summary: 3 warnings

## :warning: Warnings

- Warning: `modules/nf-core/motus/profile/main.nf:58:9`: Variable was declared but not used

  ```nextflow
      def args = task.ext.args ?: ''
          ^^^^^^^^^^
  ```

- Warning: `modules/nf-core/motus/profile/main.nf:60:9`: Variable was declared but not used

  ```nextflow
      def inputs = reads[0].getExtension() == 'bam' ?
          ^^^^^^^^^^
  ```

- Warning: `modules/nf-core/motus/profile/main.nf:65:9`: Variable was declared but not used

  ```nextflow
      def refdb = db ? "-db ${db}" : ""
          ^^^^^^^^^^
  ```
