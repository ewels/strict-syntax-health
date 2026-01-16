# Nextflow lint results

- Generated: 2026-01-16T02:02:17.580897+00:00
- Nextflow version: 25.12.0-edge
- Summary: 4 warnings

## :warning: Warnings

- Warning: `modules/nf-core/happy/ftxpy/main.nf:48:9`: Variable was declared but not used

  ```nextflow
      def args = task.ext.args ?: ''
          ^^^^^^^^^^
  ```

- Warning: `modules/nf-core/happy/ftxpy/main.nf:50:9`: Variable was declared but not used

  ```nextflow
      def regions = regions_bed ? "-R ${regions_bed}" : ""
          ^^^^^^^^^^
  ```

- Warning: `modules/nf-core/happy/ftxpy/main.nf:51:9`: Variable was declared but not used

  ```nextflow
      def targets = targets_bed ? "-T ${targets_bed}" : ""
          ^^^^^^^^^^
  ```

- Warning: `modules/nf-core/happy/ftxpy/main.nf:52:9`: Variable was declared but not used

  ```nextflow
      def bams = bam ? "--bam ${bam}" : ""
          ^^^^^^^^^^
  ```
