# Nextflow lint results

- Generated: 2026-01-21T13:35:22.776667+00:00
- Nextflow version: 25.12.0-edge
- Summary: 1 warning

## :warning: Warnings

- Warning: `modules/nf-core/gnu/split/main.nf:47:9`: Variable was declared but not used

  ```nextflow
      def args        = task.ext.args   ?: ''
          ^^^^^^^^^^
  ```
