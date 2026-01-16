# Nextflow lint results

- Generated: 2026-01-16T02:02:17.544354+00:00
- Nextflow version: 25.12.0-edge
- Summary: 1 error, 1 warning

## :x: Errors

- Error: `modules/nf-core/cellrangerarc/mkgtf/main.nf:8:5`: Invalid process directive

  ```nextflow
      if (workflow.profile.tokenize(',').intersect(['conda', 'mamba']).size() >= 1) {
      ^^^^^^^^^^
  ```

## :warning: Warnings

- Warning: `modules/nf-core/cellrangerarc/mkgtf/main.nf:38:9`: Variable was declared but not used

  ```nextflow
      def args = task.ext.args ?: ''
          ^^^^^^^^^^
  ```
