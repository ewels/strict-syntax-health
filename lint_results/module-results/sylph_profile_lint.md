# Nextflow lint results

- Generated: 2026-01-16T02:02:17.655624+00:00
- Nextflow version: 25.12.0-edge
- Summary: 2 warnings

## :warning: Warnings

- Warning: `modules/nf-core/sylph/profile/main.nf:40:9`: Variable was declared but not used

  ```nextflow
      def args = task.ext.args ?: ''
          ^^^^^^^^^^
  ```

- Warning: `modules/nf-core/sylph/profile/main.nf:42:9`: Variable was declared but not used

  ```nextflow
      def input = meta.single_end ? "${reads}" : "-1 ${reads[0]} -2 ${reads[1]}"
          ^^^^^^^^^^
  ```
