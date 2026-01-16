# Nextflow lint results

- Generated: 2026-01-16T02:02:17.581313+00:00
- Nextflow version: 25.12.0-edge
- Summary: 2 warnings

## :warning: Warnings

- Warning: `modules/nf-core/happy/prepy/main.nf:44:9`: Variable was declared but not used

  ```nextflow
      def args = task.ext.args ?: ''
          ^^^^^^^^^^
  ```

- Warning: `modules/nf-core/happy/prepy/main.nf:46:9`: Variable was declared but not used

  ```nextflow
      def restrict_region = bed ? "-R ${bed}": ""
          ^^^^^^^^^^
  ```
