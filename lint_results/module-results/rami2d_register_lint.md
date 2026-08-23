# Nextflow lint results

- Generated: 2026-08-22T00:13:30.985910+00:00
- Nextflow version: 26.08.0-edge
- Summary: 1 warning

## :warning: Warnings

- Warning: `modules/nf-core/rami2d/register/main.nf:52:9`: Variable was declared but not used

  ```nextflow
      def args = task.ext.args ?: ''
          ^^^^^^^^^^
  ```
