# Nextflow lint results

- Generated: 2026-09-09T00:23:32.871433+00:00
- Nextflow version: 26.08.0-edge
- Summary: 1 warning

## :warning: Warnings

- Warning: `modules/nf-core/rpbp/getperiodiclengthsoffsets/main.nf:21:5`: Variable was declared but not used

  ```nextflow
      task_ext_args = task.ext.args ?: ''
      ^^^^^^^^^^
  ```
