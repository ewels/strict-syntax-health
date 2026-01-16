# Nextflow lint results

- Generated: 2026-01-16T02:02:17.644764+00:00
- Nextflow version: 25.12.0-edge
- Summary: 3 warnings

## :warning: Warnings

- Warning: `modules/nf-core/seqfu/derep/main.nf:22:40`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
      def fasta_files = fastas.collect { it.getName() }
                                         ^^^^^^^^^^
  ```

- Warning: `modules/nf-core/seqfu/derep/main.nf:23:27`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
      if (fasta_files.any { it == "${prefix}.fasta.gz" }) {
                            ^^^^^^^^^^
  ```

- Warning: `modules/nf-core/seqfu/derep/main.nf:40:9`: Variable was declared but not used

  ```nextflow
      def args = task.ext.args ?: ''
          ^^^^^^^^^^
  ```
