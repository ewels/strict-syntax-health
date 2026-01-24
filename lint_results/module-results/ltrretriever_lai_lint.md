# Nextflow lint results

- Generated: 2026-01-24T00:20:24.619029+00:00
- Nextflow version: 25.12.0-edge
- Summary: 2 warnings

## :warning: Warnings

- Warning: `modules/nf-core/ltrretriever/lai/main.nf:53:9`: Variable was declared but not used

  ```nextflow
      def args            = task.ext.args     ?: ''
          ^^^^^^^^^^
  ```

- Warning: `modules/nf-core/ltrretriever/lai/main.nf:55:9`: Variable was declared but not used

  ```nextflow
      def monoploid_param = monoploid_seqs    ? "-mono $monoploid_seqs"                       : ''
          ^^^^^^^^^^
  ```
