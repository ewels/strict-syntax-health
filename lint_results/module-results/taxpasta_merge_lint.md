# Nextflow lint results

- Generated: 2026-01-16T02:02:17.656968+00:00
- Nextflow version: 25.12.0-edge
- Summary: 3 warnings

## :warning: Warnings

- Warning: `modules/nf-core/taxpasta/merge/main.nf:46:9`: Variable was declared but not used

  ```nextflow
      def args = task.ext.args ?: ''
          ^^^^^^^^^^
  ```

- Warning: `modules/nf-core/taxpasta/merge/main.nf:48:9`: Variable was declared but not used

  ```nextflow
      def taxonomy_option = taxonomy ? "--taxonomy ${taxonomy}" : ''
          ^^^^^^^^^^
  ```

- Warning: `modules/nf-core/taxpasta/merge/main.nf:49:9`: Variable was declared but not used

  ```nextflow
      def samplesheet_input = samplesheet ? "-s ${samplesheet}" : ''
          ^^^^^^^^^^
  ```
