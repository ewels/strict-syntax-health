# Nextflow lint results

- Generated: 2026-01-16T02:02:17.538063+00:00
- Nextflow version: 25.12.0-edge
- Summary: 2 warnings

## :warning: Warnings

- Warning: `modules/nf-core/busco/download/main.nf:22:9`: Variable was declared but not used

  ```nextflow
      def prefix = task.ext.prefix ?: "${lineage}"
          ^^^^^^^^^^
  ```

- Warning: `modules/nf-core/busco/download/main.nf:35:9`: Variable was declared but not used

  ```nextflow
      def args = task.ext.args ?: ''
          ^^^^^^^^^^
  ```
