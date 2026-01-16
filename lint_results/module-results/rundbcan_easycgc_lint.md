# Nextflow lint results

- Generated: 2026-01-16T02:02:17.633825+00:00
- Nextflow version: 25.12.0-edge
- Summary: 1 warning

## :warning: Warnings

- Warning: `modules/nf-core/rundbcan/easycgc/main.nf:61:9`: Variable was declared but not used

  ```nextflow
      def args = task.ext.args ?: ''
          ^^^^^^^^^^
  ```
