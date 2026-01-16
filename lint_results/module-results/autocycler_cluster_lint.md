# Nextflow lint results

- Generated: 2026-01-16T02:02:17.526159+00:00
- Nextflow version: 25.12.0-edge
- Summary: 1 warning

## :warning: Warnings

- Warning: `modules/nf-core/autocycler/cluster/main.nf:43:9`: Variable was declared but not used

  ```nextflow
      def args = task.ext.args   ?: ''
          ^^^^^^^^^^
  ```
