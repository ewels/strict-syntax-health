# Nextflow lint results

- Generated: 2026-01-16T10:17:39.959474057Z
- Nextflow version: 25.12.0-edge
- Summary: 21 warnings

## :warning: Warnings

- Warning: `modules/local/check_paired_end.nf:23:9`: Variable was declared but not used

  ```nextflow
      def args = task.ext.args ?: ''
          ^^^^
  ```

- Warning: `modules/nf-core/cat/fastq/main.nf:22:60`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
      def readList = reads instanceof List ? reads.collect { it.toString() } : [reads.toString()]
                                                             ^^
  ```

- Warning: `modules/nf-core/cat/fastq/main.nf:58:60`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
      def readList = reads instanceof List ? reads.collect { it.toString() } : [reads.toString()]
                                                             ^^
  ```

- Warning: `modules/nf-core/fastqutils/info/main.nf:37:9`: Variable was declared but not used

  ```nextflow
      def args = task.ext.args ?: ''
          ^^^^
  ```

- Warning: `subworkflows/local/alignment_to_fastq.nf:22:19`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_versions = Channel.empty()
                    ^^^^^^^
  ```

- Warning: `subworkflows/local/alignment_to_fastq.nf:54:28`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_unmapped_bam_cram = Channel.empty().mix(all_unmapped_bam,all_unmapped_cram)
                             ^^^^^^^
  ```

- Warning: `subworkflows/local/pre_conversion_qc.nf:17:19`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_versions = Channel.empty()
                    ^^^^^^^
  ```

- Warning: `subworkflows/local/pre_conversion_qc.nf:30:15`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          bam:  it[0].filetype == 'bam'
                ^^
  ```

- Warning: `subworkflows/local/pre_conversion_qc.nf:31:15`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          cram: it[0].filetype == 'cram'
                ^^
  ```

- Warning: `subworkflows/local/prepare_indices.nf:20:19`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_versions = Channel.empty()
                    ^^^^^^^
  ```

- Warning: `subworkflows/local/prepare_indices.nf:22:14`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_out = Channel.empty()
               ^^^^^^^
  ```

- Warning: `subworkflows/local/prepare_indices.nf:26:22`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          is_indexed:  it[0].index == true
                       ^^
  ```

- Warning: `subworkflows/local/prepare_indices.nf:27:22`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          to_index:    it[0].index == false
                       ^^
  ```

- Warning: `subworkflows/local/prepare_indices.nf:36:22`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_index_files = Channel.empty().mix(SAMTOOLS_INDEX.out.bai, SAMTOOLS_INDEX.out.crai)
                       ^^^^^^^
  ```

- Warning: `subworkflows/local/prepare_indices.nf:44:17`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      fasta_fai = Channel.empty()
                  ^^^^^^^
  ```

- Warning: `subworkflows/local/prepare_indices.nf:48:51`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          fasta_fai   = SAMTOOLS_FAIDX.out.fai.map{ meta, fai -> [fai] }
                                                    ^^^^
  ```

- Warning: `subworkflows/local/utils_nfcore_bamtofastq_pipeline/main.nf:31:5`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
      monochrome_logs // boolean: Do not use coloured log outputs
      ^^^^^^^^^^^^^^^
  ```

- Warning: `subworkflows/local/utils_nfcore_bamtofastq_pipeline/main.nf:34:5`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
      input //  string: Path to input samplesheet
      ^^^^^
  ```

- Warning: `workflows/bamtofastq.nf:61:5`: Variable was declared but not used

  ```nextflow
      chr = params.chr ?: channel.empty()
      ^^^
  ```

- Warning: `workflows/bamtofastq.nf:162:24`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
              ch_single: it[0].single_end == true
                         ^^
  ```

- Warning: `workflows/bamtofastq.nf:163:24`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
              ch_paired: it[0].single_end == false
                         ^^
  ```
