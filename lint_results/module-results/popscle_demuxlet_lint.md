# Nextflow lint results

- Generated: 2026-01-16T02:02:17.624722+00:00
- Nextflow version: 25.12.0-edge
- Summary: 2 warnings

## :warning: Warnings

- Warning: `modules/nf-core/popscle/demuxlet/main.nf:40:9`: Variable was declared but not used

  ```nextflow
      def args = task.ext.args ?: ''
          ^^^^^^^^^^
  ```

- Warning: `modules/nf-core/popscle/demuxlet/main.nf:42:9`: Variable was declared but not used

  ```nextflow
      def input = plp_prefix ? "--plp ${plp_prefix}" : "--sam $bam"
          ^^^^^^^^^^
  ```
