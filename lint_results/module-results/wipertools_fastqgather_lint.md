# Nextflow lint results

- Generated: 2026-01-16T02:02:17.666339+00:00
- Nextflow version: 25.12.0-edge
- Summary: 3 warnings

## :warning: Warnings

- Warning: `modules/nf-core/wipertools/fastqgather/main.nf:23:35`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
      fastq_string = fastq.collect{ it.name }.sort().join(" ")
                                    ^^^^^^^^^^
  ```

- Warning: `modules/nf-core/wipertools/fastqgather/main.nf:26:21`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
      if (fastq.any { it.name == "${prefix}.fastq.gz" }) {
                      ^^^^^^^^^^
  ```

- Warning: `modules/nf-core/wipertools/fastqgather/main.nf:47:21`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
      if (fastq.any { it.name == "${prefix}.fastq.gz" }) {
                      ^^^^^^^^^^
  ```
