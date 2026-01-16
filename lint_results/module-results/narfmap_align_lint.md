# Nextflow lint results

- Generated: 2026-01-16T02:02:17.609601+00:00
- Nextflow version: 25.12.0-edge
- Summary: 4 warnings

## :warning: Warnings

- Warning: `modules/nf-core/narfmap/align/main.nf:54:9`: Variable was declared but not used

  ```nextflow
      def args = task.ext.args ?: ''
          ^^^^^^^^^^
  ```

- Warning: `modules/nf-core/narfmap/align/main.nf:57:9`: Variable was declared but not used

  ```nextflow
      def reads_command = meta.single_end ? "-1 $reads" : "-1 ${reads[0]} -2 ${reads[1]}"
          ^^^^^^^^^^
  ```

- Warning: `modules/nf-core/narfmap/align/main.nf:58:9`: Variable was declared but not used

  ```nextflow
      def samtools_command = sort_bam ? 'sort' : 'view'
          ^^^^^^^^^^
  ```

- Warning: `modules/nf-core/narfmap/align/main.nf:62:9`: Variable was declared but not used

  ```nextflow
      def reference = fasta && extension=="cram"  ? "--reference ${fasta}" : ""
          ^^^^^^^^^^
  ```
