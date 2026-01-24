# Nextflow lint results

- Generated: 2026-01-24T00:20:24.633429+00:00
- Nextflow version: 25.12.0-edge
- Summary: 1 warning

## :warning: Warnings

- Warning: `modules/nf-core/paftools/sam2paf/main.nf:22:9`: Variable was declared but not used

  ```nextflow
      def args    = task.ext.args     ?: ""
          ^^^^^^^^^^
  ```
