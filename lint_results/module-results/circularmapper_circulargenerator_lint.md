# Nextflow lint results

- Generated: 2026-01-16T02:02:17.546908+00:00
- Nextflow version: 25.12.0-edge
- Summary: 1 warning

## :warning: Warnings

- Warning: `modules/nf-core/circularmapper/circulargenerator/main.nf:50:9`: Variable was declared but not used

  ```nextflow
      def args   = task.ext.args ?: ''
          ^^^^^^^^^^
  ```
