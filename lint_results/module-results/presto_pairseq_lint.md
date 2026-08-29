# Nextflow lint results

- Generated: 2026-08-29T00:21:12.249466+00:00
- Nextflow version: 26.08.0-edge
- Summary: 1 warning

## :warning: Warnings

- Warning: `modules/nf-core/presto/pairseq/main.nf:42:9`: Variable was declared but not used

  ```nextflow
      def args = task.ext.args?: ''
          ^^^^^^^^^^
  ```
