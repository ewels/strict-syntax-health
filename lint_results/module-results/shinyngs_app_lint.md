# Nextflow lint results

- Generated: 2026-01-16T02:02:17.647870+00:00
- Nextflow version: 25.12.0-edge
- Summary: 1 error, 1 warning

## :x: Errors

- Error: `modules/nf-core/shinyngs/app/tests/nextflow.config:6:32`: Unexpected input: ':'

  ```nextflow
      withName: test_shinyngs_app:SHINYNGS_APP {
                                 ^^^^^^^^^^
  ```

## :warning: Warnings

- Warning: `modules/nf-core/shinyngs/app/main.nf:56:9`: Variable was declared but not used

  ```nextflow
      def args = task.ext.args ?: ''
          ^^^^^^^^^^
  ```
