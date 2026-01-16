# Nextflow lint results

- Generated: 2026-01-16T02:02:17.546308+00:00
- Nextflow version: 25.12.0-edge
- Summary: 2 errors, 2 warnings

## :x: Errors

- Error: `modules/nf-core/chewbbaca/createschema/main.nf:28:9`: `prodigal_tf` is already declared

  ```nextflow
      def prodigal_tf = prodigal_tf ? "--ptf ${prodigal_tf}" : ""
          ^^^^^^^^^^
  ```

- Error: `modules/nf-core/chewbbaca/createschema/main.nf:29:9`: `cds` is already declared

  ```nextflow
      def cds = cds ? "--cds ${cds}" : ""
          ^^^^^^^^^^
  ```

## :warning: Warnings

- Warning: `modules/nf-core/chewbbaca/createschema/main.nf:51:9`: Variable was declared but not used

  ```nextflow
      def args = task.ext.args ?: ''
          ^^^^^^^^^^
  ```

- Warning: `modules/nf-core/chewbbaca/createschema/main.nf:53:9`: Variable was declared but not used

  ```nextflow
      def schema = "--n ${prefix}"
          ^^^^^^^^^^
  ```
