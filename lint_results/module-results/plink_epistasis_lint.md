# Nextflow lint results

- Generated: 2026-01-16T02:02:17.621437+00:00
- Nextflow version: 25.12.0-edge
- Summary: 2 errors, 3 warnings

## :x: Errors

- Error: `modules/nf-core/plink/epistasis/main.nf:74:60`: `pheno` is not defined

  ```nextflow
          prefix = task.ext.prefix ?: "${meta2.id} --pheno ${pheno}"
                                                             ^^^^^^^
  ```

- Error: `modules/nf-core/plink/epistasis/main.nf:77:49`: `pheno` is not defined

  ```nextflow
          input_command = "--bcf ${bcf} --pheno ${pheno}"
                                                  ^^^^^^^
  ```

## :warning: Warnings

- Warning: `modules/nf-core/plink/epistasis/main.nf:33:9`: Variable was declared but not used

  ```nextflow
      def outmeta = ""
          ^^^^^^^^^^
  ```

- Warning: `modules/nf-core/plink/epistasis/main.nf:63:9`: Variable was declared but not used

  ```nextflow
      def args = task.ext.args ?: ''
          ^^^^^^^^^^
  ```

- Warning: `modules/nf-core/plink/epistasis/main.nf:68:9`: Variable was declared but not used

  ```nextflow
      def outmeta = ""
          ^^^^^^^^^^
  ```
