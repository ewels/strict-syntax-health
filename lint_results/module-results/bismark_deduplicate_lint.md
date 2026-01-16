# Nextflow lint results

- Generated: 2026-01-16T02:02:17.535581+00:00
- Nextflow version: 25.12.0-edge
- Summary: 2 warnings

## :warning: Warnings

- Warning: `modules/nf-core/bismark/deduplicate/main.nf:23:9`: Variable was declared but not used

  ```nextflow
      def prefix  = task.ext.prefix ?: "${meta.id}"
          ^^^^^^^^^^
  ```

- Warning: `modules/nf-core/bismark/deduplicate/main.nf:38:9`: Variable was declared but not used

  ```nextflow
      def args = task.ext.args ?: ''
          ^^^^^^^^^^
  ```
