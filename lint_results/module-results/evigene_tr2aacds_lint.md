# Nextflow lint results

- Generated: 2026-01-16T02:02:17.560964+00:00
- Nextflow version: 25.12.0-edge
- Summary: 2 warnings

## :warning: Warnings

- Warning: `modules/nf-core/evigene/tr2aacds/main.nf:68:9`: Variable was declared but not used

  ```nextflow
      def args        = task.ext.args ?: ''
          ^^^^^^^^^^
  ```

- Warning: `modules/nf-core/evigene/tr2aacds/main.nf:70:9`: Variable was declared but not used

  ```nextflow
      def max_memory  = 7*1024
          ^^^^^^^^^^
  ```
