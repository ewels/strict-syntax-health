# Nextflow lint results

- Generated: 2026-01-16T02:02:17.540891+00:00
- Nextflow version: 25.12.0-edge
- Summary: 1 error, 2 warnings

## :x: Errors

- Error: `modules/nf-core/cellranger/count/main.nf:32:9`: `prefix` is already declared

  ```nextflow
      def prefix = task.ext.prefix ?: "${meta.id}"
          ^^^^^^^^^^
  ```

## :warning: Warnings

- Warning: `modules/nf-core/cellranger/count/main.nf:23:5`: Variable was declared but not used

  ```nextflow
      args = task.ext.args ?: ''
      ^^^^^^^^^^
  ```

- Warning: `modules/nf-core/cellranger/count/main.nf:24:5`: Variable was declared but not used

  ```nextflow
      prefix = task.ext.prefix ?: "${meta.id}"
      ^^^^^^^^^^
  ```
