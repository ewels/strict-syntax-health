# Nextflow lint results

- Generated: 2026-09-08T00:23:04.258013+00:00
- Nextflow version: 26.08.0-edge
- Summary: 1 warning

## :warning: Warnings

- Warning: `modules/nf-core/gapseq/findtransport/main.nf:24:9`: Variable was declared but not used

  ```nextflow
      def prefix = task.ext.prefix ?: "${meta.id}"
          ^^^^^^^^^^
  ```
