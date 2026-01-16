# Nextflow lint results

- Generated: 2026-01-16T02:02:17.540688+00:00
- Nextflow version: 25.12.0-edge
- Summary: 1 warning

## :warning: Warnings

- Warning: `modules/nf-core/cellbender/merge/main.nf:22:5`: Variable was declared but not used

  ```nextflow
      output_layer = task.ext.output_layer ?: "cellbender"
      ^^^^^^^^^^
  ```
