# Nextflow lint results

- Generated: 2026-01-16T02:02:17.601222+00:00
- Nextflow version: 25.12.0-edge
- Summary: 3 warnings

## :warning: Warnings

- Warning: `modules/nf-core/metabat2/metabat2/main.nf:51:9`: Variable was declared but not used

  ```nextflow
      def args             = task.ext.args   ?: ''
          ^^^^^^^^^^
  ```

- Warning: `modules/nf-core/metabat2/metabat2/main.nf:53:9`: Variable was declared but not used

  ```nextflow
      def decompress_depth = depth           ? "gzip -d -f $depth"    : ""
          ^^^^^^^^^^
  ```

- Warning: `modules/nf-core/metabat2/metabat2/main.nf:54:9`: Variable was declared but not used

  ```nextflow
      def depth_file       = depth           ? "-a ${depth.baseName}" : ""
          ^^^^^^^^^^
  ```
