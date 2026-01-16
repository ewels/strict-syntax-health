# Nextflow lint results

- Generated: 2026-01-16T02:02:17.664049+00:00
- Nextflow version: 25.12.0-edge
- Summary: 2 warnings

## :warning: Warnings

- Warning: `modules/nf-core/viennarna/rnafold/main.nf:23:9`: Variable was declared but not used

  ```nextflow
      def prefix = meta.id ?: "${fasta.getName()}"
          ^^^^^^^^^^
  ```

- Warning: `modules/nf-core/viennarna/rnafold/main.nf:38:9`: Variable was declared but not used

  ```nextflow
      def args = task.ext.args ?: ''
          ^^^^^^^^^^
  ```
