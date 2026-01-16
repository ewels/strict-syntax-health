# Nextflow lint results

- Generated: 2026-01-16T02:02:17.596323+00:00
- Nextflow version: 25.12.0-edge
- Summary: 10 errors, 6 warnings

## :x: Errors

- Error: `modules/nf-core/mafft/align/main.nf:29:9`: `add` is already declared

  ```nextflow
      def add          = add             ? "--add <(unpigz -cdf ${add})"                   : ''
          ^^^^^^^^^^
  ```

- Error: `modules/nf-core/mafft/align/main.nf:30:9`: `addfragments` is already declared

  ```nextflow
      def addfragments = addfragments    ? "--addfragments <(unpigz -cdf ${addfragments})" : ''
          ^^^^^^^^^^
  ```

- Error: `modules/nf-core/mafft/align/main.nf:31:9`: `addfull` is already declared

  ```nextflow
      def addfull      = addfull         ? "--addfull <(unpigz -cdf ${addfull})"           : ''
          ^^^^^^^^^^
  ```

- Error: `modules/nf-core/mafft/align/main.nf:32:9`: `addprofile` is already declared

  ```nextflow
      def addprofile   = addprofile      ? "--addprofile <(unpigz -cdf ${addprofile})"     : ''
          ^^^^^^^^^^
  ```

- Error: `modules/nf-core/mafft/align/main.nf:33:9`: `addlong` is already declared

  ```nextflow
      def addlong      = addlong         ? "--addlong <(unpigz -cdf ${addlong})"           : ''
          ^^^^^^^^^^
  ```

- Error: `modules/nf-core/mafft/align/main.nf:59:9`: `add` is already declared

  ```nextflow
      def add          = add             ? "--add ${add}"                   : ''
          ^^^^^^^^^^
  ```

- Error: `modules/nf-core/mafft/align/main.nf:60:9`: `addfragments` is already declared

  ```nextflow
      def addfragments = addfragments    ? "--addfragments ${addfragments}" : ''
          ^^^^^^^^^^
  ```

- Error: `modules/nf-core/mafft/align/main.nf:61:9`: `addfull` is already declared

  ```nextflow
      def addfull      = addfull         ? "--addfull ${addfull}"           : ''
          ^^^^^^^^^^
  ```

- Error: `modules/nf-core/mafft/align/main.nf:62:9`: `addprofile` is already declared

  ```nextflow
      def addprofile   = addprofile      ? "--addprofile ${addprofile}"     : ''
          ^^^^^^^^^^
  ```

- Error: `modules/nf-core/mafft/align/main.nf:63:9`: `addlong` is already declared

  ```nextflow
      def addlong      = addlong         ? "--addlong ${addlong}"           : ''
          ^^^^^^^^^^
  ```

## :warning: Warnings

- Warning: `modules/nf-core/mafft/align/main.nf:57:9`: Variable was declared but not used

  ```nextflow
      def args         = task.ext.args   ?: ''
          ^^^^^^^^^^
  ```

- Warning: `modules/nf-core/mafft/align/main.nf:59:9`: Variable was declared but not used

  ```nextflow
      def add          = add             ? "--add ${add}"                   : ''
          ^^^^^^^^^^
  ```

- Warning: `modules/nf-core/mafft/align/main.nf:60:9`: Variable was declared but not used

  ```nextflow
      def addfragments = addfragments    ? "--addfragments ${addfragments}" : ''
          ^^^^^^^^^^
  ```

- Warning: `modules/nf-core/mafft/align/main.nf:61:9`: Variable was declared but not used

  ```nextflow
      def addfull      = addfull         ? "--addfull ${addfull}"           : ''
          ^^^^^^^^^^
  ```

- Warning: `modules/nf-core/mafft/align/main.nf:62:9`: Variable was declared but not used

  ```nextflow
      def addprofile   = addprofile      ? "--addprofile ${addprofile}"     : ''
          ^^^^^^^^^^
  ```

- Warning: `modules/nf-core/mafft/align/main.nf:63:9`: Variable was declared but not used

  ```nextflow
      def addlong      = addlong         ? "--addlong ${addlong}"           : ''
          ^^^^^^^^^^
  ```
