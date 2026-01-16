# Nextflow lint results

- Generated: 2026-01-16T02:02:17.602485+00:00
- Nextflow version: 25.12.0-edge
- Summary: 3 warnings

## :warning: Warnings

- Warning: `modules/nf-core/metaphlan/metaphlan/main.nf:58:9`: Variable was declared but not used

  ```nextflow
      def input_data = ("${input_type}".contains("fastq")) && !meta.single_end ? "${input[0]},${input[1]}" : "${input}"
          ^^^^^^^^^^
  ```

- Warning: `modules/nf-core/metaphlan/metaphlan/main.nf:59:9`: Variable was declared but not used

  ```nextflow
      def bowtie2_out = "${input_type}" == "--input_type bowtie2out" || "${input_type}" == "--input_type sam" ? '' : "--bowtie2out ${prefix}.bowtie2out.txt"
          ^^^^^^^^^^
  ```

- Warning: `modules/nf-core/metaphlan/metaphlan/main.nf:60:9`: Variable was declared but not used

  ```nextflow
      def samfile_out = save_samfile ? "-s ${prefix}.sam" : ''
          ^^^^^^^^^^
  ```
