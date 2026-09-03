# Nextflow lint results

- Generated: 2026-09-03T00:30:18.800435+00:00
- Nextflow version: 26.08.0-edge
- Summary: 2 warnings

## :warning: Warnings

- Warning: `modules/nf-core/custom/orfnormalise/main.nf:24:5`: Variable was declared but not used

  ```nextflow
      sample_id = meta.id ?: 'unknown'
      ^^^^^^^^^^
  ```

- Warning: `modules/nf-core/custom/orfnormalise/main.nf:25:5`: Variable was declared but not used

  ```nextflow
      args      = task.ext.args ?: ''
      ^^^^^^^^^^
  ```
