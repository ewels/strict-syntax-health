# Nextflow lint results

- Generated: 2026-01-16T02:02:17.653460+00:00
- Nextflow version: 25.12.0-edge
- Summary: 2 warnings

## :warning: Warnings

- Warning: `modules/nf-core/survivor/filter/main.nf:25:9`: Variable was declared but not used

  ```nextflow
      def args = task.ext.args ?: ''
          ^^^^^^^^^^
  ```

- Warning: `modules/nf-core/survivor/filter/main.nf:51:9`: Variable was declared but not used

  ```nextflow
      def bed_file = bed ? "${bed}" : "NA"
          ^^^^^^^^^^
  ```
