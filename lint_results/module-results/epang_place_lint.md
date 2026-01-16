# Nextflow lint results

- Generated: 2026-01-16T02:02:17.560543+00:00
- Nextflow version: 25.12.0-edge
- Summary: 6 warnings

## :warning: Warnings

- Warning: `modules/nf-core/epang/place/main.nf:56:9`: Variable was declared but not used

  ```nextflow
      def args       = task.ext.args   ?: ''
          ^^^^^^^^^^
  ```

- Warning: `modules/nf-core/epang/place/main.nf:58:9`: Variable was declared but not used

  ```nextflow
      def queryarg   = queryaln        ? "--query $queryaln"       : ""
          ^^^^^^^^^^
  ```

- Warning: `modules/nf-core/epang/place/main.nf:59:9`: Variable was declared but not used

  ```nextflow
      def refalnarg  = referencealn    ? "--ref-msa $referencealn" : ""
          ^^^^^^^^^^
  ```

- Warning: `modules/nf-core/epang/place/main.nf:60:9`: Variable was declared but not used

  ```nextflow
      def reftreearg = referencetree   ? "--tree $referencetree"   : ""
          ^^^^^^^^^^
  ```

- Warning: `modules/nf-core/epang/place/main.nf:61:9`: Variable was declared but not used

  ```nextflow
      def bfastarg   = bfastfile       ? "--bfast $bfastfile"      : ""
          ^^^^^^^^^^
  ```

- Warning: `modules/nf-core/epang/place/main.nf:62:9`: Variable was declared but not used

  ```nextflow
      def binaryarg  = binaryfile      ? "--binary $binaryfile"    : ""
          ^^^^^^^^^^
  ```
