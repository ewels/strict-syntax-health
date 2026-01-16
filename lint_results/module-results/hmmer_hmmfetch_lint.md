# Nextflow lint results

- Generated: 2026-01-16T02:02:17.583678+00:00
- Nextflow version: 25.12.0-edge
- Summary: 1 error, 1 warning

## :x: Errors

- Error: `modules/nf-core/hmmer/hmmfetch/main.nf:32:9`: `index` is already declared

  ```nextflow
      def index   = ! key && ! keyfile ? '--index' : ''
          ^^^^^^^^^^
  ```

## :warning: Warnings

- Warning: `modules/nf-core/hmmer/hmmfetch/main.nf:52:9`: Variable was declared but not used

  ```nextflow
      def args = task.ext.args ?: ''
          ^^^^^^^^^^
  ```
