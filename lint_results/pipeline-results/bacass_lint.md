# Nextflow lint results

- Generated: 2026-09-01T00:23:21.986861032Z
- Nextflow version: 26.08.0-edge
- Summary: 16 warnings

## :warning: Warnings

- Warning: `modules/nf-core/quast/main.nf:48:9`: Variable was declared but not used

  ```nextflow
      def args      = task.ext.args   ?: ''
          ^^^^
  ```

- Warning: `modules/nf-core/quast/main.nf:50:9`: Variable was declared but not used

  ```nextflow
      def features  = gff             ? "--features $gff" : ''
          ^^^^^^^^
  ```

- Warning: `modules/nf-core/quast/main.nf:51:9`: Variable was declared but not used

  ```nextflow
      def reference = fasta           ? "-r $fasta" : ''
          ^^^^^^^^^
  ```

- Warning: `subworkflows/nf-core/fastq_trim_fastp_fastqc/main.nf:34:19`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_versions = Channel.empty()
                    ^^^^^^^
  ```

- Warning: `subworkflows/nf-core/fastq_trim_fastp_fastqc/main.nf:37:49`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
      ch_reads_only = ch_reads.map { meta, reads, adapter_fasta -> [ meta, reads ] }
                                                  ^^^^^^^^^^^^^
  ```

- Warning: `subworkflows/nf-core/fastq_trim_fastp_fastqc/main.nf:39:26`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_fastqc_raw_html = Channel.empty()
                           ^^^^^^^
  ```

- Warning: `subworkflows/nf-core/fastq_trim_fastp_fastqc/main.nf:40:26`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_fastqc_raw_zip  = Channel.empty()
                           ^^^^^^^
  ```

- Warning: `subworkflows/nf-core/fastq_trim_fastp_fastqc/main.nf:50:28`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_trim_json         = Channel.empty()
                             ^^^^^^^
  ```

- Warning: `subworkflows/nf-core/fastq_trim_fastp_fastqc/main.nf:51:28`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_trim_html         = Channel.empty()
                             ^^^^^^^
  ```

- Warning: `subworkflows/nf-core/fastq_trim_fastp_fastqc/main.nf:52:28`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_trim_log          = Channel.empty()
                             ^^^^^^^
  ```

- Warning: `subworkflows/nf-core/fastq_trim_fastp_fastqc/main.nf:53:28`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_trim_reads_fail   = Channel.empty()
                             ^^^^^^^
  ```

- Warning: `subworkflows/nf-core/fastq_trim_fastp_fastqc/main.nf:54:28`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_trim_reads_merged = Channel.empty()
                             ^^^^^^^
  ```

- Warning: `subworkflows/nf-core/fastq_trim_fastp_fastqc/main.nf:55:28`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_fastqc_trim_html  = Channel.empty()
                             ^^^^^^^
  ```

- Warning: `subworkflows/nf-core/fastq_trim_fastp_fastqc/main.nf:56:28`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_fastqc_trim_zip   = Channel.empty()
                             ^^^^^^^
  ```

- Warning: `workflows/bacass.nf:261:33`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
                  .branch { meta, reads ->
                                  ^^^^^
  ```

- Warning: `workflows/bacass.nf:276:13`: Variable was declared but not used

  ```nextflow
              ch_rasusa_log = RASUSA.out.log
              ^^^^^^^^^^^^^
  ```
