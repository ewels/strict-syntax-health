# Nextflow lint results

- Generated: 2026-01-16T02:02:17.634648+00:00
- Nextflow version: 25.12.0-edge
- Summary: 1 error, 1 warning

## :x: Errors

- Error: `modules/nf-core/sam2lca/analyze/main.nf:28:9`: `database` is already declared

  ```nextflow
      def database = database ? "${database}" : "sam2lca_db"
          ^^^^^^^^^^
  ```

## :warning: Warnings

- Warning: `modules/nf-core/sam2lca/analyze/main.nf:45:9`: Variable was declared but not used

  ```nextflow
      def args = task.ext.args ?: ''
          ^^^^^^^^^^
  ```
