# Nextflow lint results

- Generated: 2026-01-16T02:02:17.599321+00:00
- Nextflow version: 25.12.0-edge
- Summary: 2 warnings

## :warning: Warnings

- Warning: `modules/nf-core/megan/rma2info/main.nf:40:9`: Variable was declared but not used

  ```nextflow
      def args = task.ext.args ?: ''
          ^^^^^^^^^^
  ```

- Warning: `modules/nf-core/megan/rma2info/main.nf:42:9`: Variable was declared but not used

  ```nextflow
      def summary = megan_summary ? "-es ${prefix}.megan" : ""
          ^^^^^^^^^^
  ```
