# Nextflow lint results

- Generated: 2026-01-16T02:02:17.591190+00:00
- Nextflow version: 25.12.0-edge
- Summary: 1 error, 1 warning

## :x: Errors

- Error: `modules/nf-core/kraken2/buildstandard/main.nf:21:57`: `db` is not defined

  ```nextflow
      runclean = cleaning ? "kraken2-build --clean --db ${db}" : ""
                                                          ^^^^^^^^^
  ```

## :warning: Warnings

- Warning: `modules/nf-core/kraken2/buildstandard/main.nf:36:9`: Variable was declared but not used

  ```nextflow
      def args = task.ext.args ?: ''
          ^^^^^^^^^^
  ```
