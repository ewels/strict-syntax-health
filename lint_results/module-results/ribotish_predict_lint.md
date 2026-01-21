# Nextflow lint results

- Generated: 2026-01-21T13:35:22.839055+00:00
- Nextflow version: 25.12.0-edge
- Summary: 1 error, 1 warning

## :x: Errors

- Error: `modules/nf-core/ribotish/predict/main.nf:41:12`: `para_tis` is not defined

  ```nextflow
          if (para_tis){
             ^^^^^^^^^^
  ```

## :warning: Warnings

- Warning: `modules/nf-core/ribotish/predict/main.nf:64:9`: Variable was declared but not used

  ```nextflow
      def args = task.ext.args ?: ''
          ^^^^^^^^^^
  ```
