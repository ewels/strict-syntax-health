# Nextflow lint results

- Generated: 2026-01-16T02:02:17.566803+00:00
- Nextflow version: 25.12.0-edge
- Summary: 2 warnings

## :warning: Warnings

- Warning: `modules/nf-core/ganon/classify/main.nf:48:9`: Variable was declared but not used

  ```nextflow
      def args = task.ext.args ?: ''
          ^^^^^^^^^^
  ```

- Warning: `modules/nf-core/ganon/classify/main.nf:50:9`: Variable was declared but not used

  ```nextflow
      def input = meta.single_end ? "--single-reads ${fastqs}" : "--paired-reads ${fastqs}"
          ^^^^^^^^^^
  ```
