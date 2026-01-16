# Nextflow lint results

- Generated: 2026-01-16T02:02:17.532441+00:00
- Nextflow version: 25.12.0-edge
- Summary: 1 error

## :x: Errors

- Error: `modules/nf-core/bedtools/groupby/main.nf:24:9`: `summary_col` is already declared

  ```nextflow
      def summary_col = task.ext.summary_col ? "-c ${task.ext.summary_col}" : "-c 5"
          ^^^^^^^^^^
  ```
