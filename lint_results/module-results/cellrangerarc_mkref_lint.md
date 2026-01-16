# Nextflow lint results

- Generated: 2026-01-16T02:02:17.544528+00:00
- Nextflow version: 25.12.0-edge
- Summary: 1 error, 1 warning

## :x: Errors

- Error: `modules/nf-core/cellrangerarc/mkref/main.nf:30:9`: `reference_config` is already declared

  ```nextflow
      def reference_config = reference_config.name
          ^^^^^^^^^^
  ```

## :warning: Warnings

- Warning: `modules/nf-core/cellrangerarc/mkref/main.nf:90:9`: Variable was declared but not used

  ```nextflow
      def args = task.ext.args ?: ''
          ^^^^^^^^^^
  ```
