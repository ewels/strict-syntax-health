# Nextflow lint results

- Generated: 2026-08-25T00:10:04.446343444Z
- Nextflow version: 26.08.0-edge
- Summary: 2 warnings

## :warning: Warnings

- Warning: `modules/local/shinyapp/main.nf:24:9`: Variable was declared but not used

  ```nextflow
      def prefix                    = task.ext.prefix ?: "${meta.id}"
          ^^^^^^
  ```

- Warning: `modules/local/treesummary/main.nf:39:9`: Variable was declared but not used

  ```nextflow
      def prefix = task.ext.prefix ?: "${meta.id}"
          ^^^^^^
  ```
