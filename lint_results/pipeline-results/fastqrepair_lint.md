# Nextflow lint results

- Generated: 2026-08-24T00:09:41.854897399Z
- Nextflow version: 26.08.0-edge
- Summary: 9 warnings

## :warning: Warnings

- Warning: `modules/nf-core/wipertools/fastqgather/main.nf:25:21`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
      if (fastq.any { it.name == "${prefix}.fastq.gz" }) {
                      ^^
  ```

- Warning: `modules/nf-core/wipertools/fastqgather/main.nf:46:21`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
      if (fastq.any { it.name == "${prefix}.fastq.gz" }) {
                      ^^
  ```

- Warning: `modules/nf-core/wipertools/reportgather/main.nf:25:22`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
      if (report.any { it.name == "${prefix}.report" }) {
                       ^^
  ```

- Warning: `modules/nf-core/wipertools/reportgather/main.nf:46:22`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
      if (report.any { it.name == "${prefix}.report" }) {
                       ^^
  ```

- Warning: `subworkflows/local/fastq_repair_wipertools/main.nf:12:19`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_versions = Channel.empty()
                    ^^^^^^^
  ```

- Warning: `subworkflows/local/fastq_repair_wipertools/main.nf:48:24`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_cleaned_fastq = Channel.empty()
                         ^^^^^^^
  ```

- Warning: `subworkflows/local/fastq_repair_wipertools/main.nf:53:65`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          def fq = id_fq.sort { a, b -> a[0] <=> b[0] }.collect { it[1] }
                                                                  ^^
  ```

- Warning: `subworkflows/local/fastq_repair_wipertools/main.nf:65:26`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_gathered_report = Channel.empty()
                           ^^^^^^^
  ```

- Warning: `subworkflows/local/fastq_repair_wipertools/main.nf:73:24`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_final_reports = Channel.empty()
                         ^^^^^^^
  ```
