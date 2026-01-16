# Nextflow lint results

- Generated: 2026-01-16T06:41:03.113790446Z
- Nextflow version: 25.12.0-edge
- Summary: 11 errors, 74 warnings

## :x: Errors

- Error: `modules/local/format_fasta_mirna/main.nf:1:1`: Statements cannot be mixed with script declarations -- move statements into a process, workflow, or function

  ```nextflow
  def VERSION = '0.0.14'
  ^^^^^^^^^^^^^^^^^^^^^^
  ```

- Error: `modules/local/format_fasta_mirna/main.nf:28:34`: `VERSION` is not defined

  ```nextflow
          fastx_toolkit:  \$(echo "$VERSION")
                                   ^^^^^^^^
  ```

- Error: `subworkflows/local/prepare_genome/main.nf:24:5`: `for` loops are no longer supported

  ```nextflow
      for (file_path in files) {
      ^^^
  ```

- Error: `subworkflows/local/prepare_genome/main.nf:24:10`: `file_path` is not defined

  ```nextflow
      for (file_path in files) {
           ^^^^^^^^^
  ```

- Error: `subworkflows/local/prepare_genome/main.nf:25:25`: `file_path` is not defined

  ```nextflow
          def file_name = file_path.getName()
                          ^^^^^^^^^
  ```

- Error: `subworkflows/local/prepare_genome/main.nf:28:13`: `break` is not allowed as an identifier because it is a Groovy keyword

  ```nextflow
              break
              ^^^^^
  ```

- Error: `subworkflows/local/prepare_genome/main.nf:28:13`: `break` is not defined

  ```nextflow
              break
              ^^^^^
  ```

- Error: `workflows/smrnaseq.nf:34:1`: Statements cannot be mixed with script declarations -- move statements into a process, workflow, or function

  ```nextflow
  ch_multiqc_config                     = channel.fromPath("$projectDir/assets/multiqc_config.yml", checkIfExists: true)
  ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  ```

- Error: `workflows/smrnaseq.nf:35:1`: Statements cannot be mixed with script declarations -- move statements into a process, workflow, or function

  ```nextflow
  ch_multiqc_custom_config              = params.multiqc_config ? channel.fromPath( params.multiqc_config, checkIfExists: true ) : channel.empty()
  ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  ```

- Error: `workflows/smrnaseq.nf:36:1`: Statements cannot be mixed with script declarations -- move statements into a process, workflow, or function

  ```nextflow
  ch_multiqc_logo                       = params.multiqc_logo   ? channel.fromPath( params.multiqc_logo, checkIfExists: true ) : channel.empty()
  ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  ```

- Error: `workflows/smrnaseq.nf:37:1`: Statements cannot be mixed with script declarations -- move statements into a process, workflow, or function

  ```nextflow
  ch_fastp_adapters                     = channel.fromPath(params.fastp_known_mirna_adapters, checkIfExists: true).collect() // collect to consume for all incoming samples to FASTP
  ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  ```

## :warning: Warnings

- Warning: `modules/local/format_fasta_mirna/main.nf:1:5`: Variable was declared but not used

  ```nextflow
  def VERSION = '0.0.14'
      ^^^^^^^
  ```

- Warning: `modules/nf-core/blat/main.nf:52:9`: Variable was declared but not used

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

- Warning: `modules/nf-core/mirdeep2/mapper/main.nf:41:9`: Variable was declared but not used

  ```nextflow
      def args = task.ext.args ?: ''
          ^^^^
  ```

- Warning: `modules/nf-core/mirdeep2/mirdeep2/main.nf:51:9`: Variable was declared but not used

  ```nextflow
      def args = task.ext.args ?: ''
          ^^^^
  ```

- Warning: `modules/nf-core/mirtop/counts/main.nf:24:9`: Variable was declared but not used

  ```nextflow
      def prefix = task.ext.prefix ?: "${meta.id}"
          ^^^^^^
  ```

- Warning: `modules/nf-core/mirtop/counts/main.nf:42:9`: Variable was declared but not used

  ```nextflow
      def args = task.ext.args ?: ''
          ^^^^
  ```

- Warning: `modules/nf-core/mirtop/counts/main.nf:43:9`: Variable was declared but not used

  ```nextflow
      def prefix = task.ext.prefix ?: "${meta.id}"
          ^^^^^^
  ```

- Warning: `modules/nf-core/mirtop/export/main.nf:26:9`: Variable was declared but not used

  ```nextflow
      def prefix = task.ext.prefix ?: "${meta.id}"
          ^^^^^^
  ```

- Warning: `modules/nf-core/mirtop/export/main.nf:44:9`: Variable was declared but not used

  ```nextflow
      def args = task.ext.args ?: ''
          ^^^^
  ```

- Warning: `modules/nf-core/mirtop/gff/main.nf:44:9`: Variable was declared but not used

  ```nextflow
      def args = task.ext.args ?: ''
          ^^^^
  ```

- Warning: `modules/nf-core/mirtop/gff/main.nf:45:9`: Variable was declared but not used

  ```nextflow
      def prefix = task.ext.prefix ?: "${meta.id}"
          ^^^^^^
  ```

- Warning: `modules/nf-core/mirtop/stats/main.nf:24:9`: Variable was declared but not used

  ```nextflow
      def prefix = task.ext.prefix ?: "${meta.id}"
          ^^^^^^
  ```

- Warning: `modules/nf-core/mirtop/stats/main.nf:39:9`: Variable was declared but not used

  ```nextflow
      def args = task.ext.args ?: ''
          ^^^^
  ```

- Warning: `modules/nf-core/mirtrace/qc/main.nf:26:9`: Variable was declared but not used

  ```nextflow
      def args = task.ext.args ?: ''
          ^^^^
  ```

- Warning: `modules/nf-core/mirtrace/qc/main.nf:27:9`: Variable was declared but not used

  ```nextflow
      def prefix = task.ext.prefix ?: "${meta.id}"
          ^^^^^^
  ```

- Warning: `modules/nf-core/mirtrace/qc/main.nf:45:9`: Variable was declared but not used

  ```nextflow
      def args = task.ext.args ?: ''
          ^^^^
  ```

- Warning: `modules/nf-core/seqcluster/collapse/main.nf:41:9`: Variable was declared but not used

  ```nextflow
      def args = task.ext.args ?: ''
          ^^^^
  ```

- Warning: `modules/nf-core/seqkit/grep/main.nf:45:9`: Variable was declared but not used

  ```nextflow
      def args = task.ext.args ?: ''
          ^^^^
  ```

- Warning: `subworkflows/local/contaminant_filter/main.nf:59:5`: Variable was declared but not used

  ```nextflow
      ch_mqc_results  = channel.empty()
      ^^^^^^^^^^^^^^
  ```

- Warning: `subworkflows/local/contaminant_filter/main.nf:135:24`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
                  .map { meta, file -> file.text.readLines() }
                         ^^^^
  ```

- Warning: `subworkflows/local/contaminant_filter/main.nf:181:24`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
                  .map { meta, file -> file.text.readLines() }
                         ^^^^
  ```

- Warning: `subworkflows/local/contaminant_filter/main.nf:227:24`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
                  .map { meta, file -> file.text.readLines() }
                         ^^^^
  ```

- Warning: `subworkflows/local/contaminant_filter/main.nf:273:24`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
                  .map { meta, file -> file.text.readLines() }
                         ^^^^
  ```

- Warning: `subworkflows/local/mirna_quant/main.nf:53:27`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          .map { add_suffix(it, "mature") }
                            ^^
  ```

- Warning: `subworkflows/local/mirna_quant/main.nf:59:27`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          .map { add_suffix(it, "hairpin") }
                            ^^
  ```

- Warning: `subworkflows/local/mirna_quant/main.nf:81:60`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
      ch_edger_input = BAM_STATS_MATURE.out.idxstats.collect{it[1]}
                                                             ^^
  ```

- Warning: `subworkflows/local/mirna_quant/main.nf:82:53`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          .mix(BAM_STATS_HAIRPIN.out.idxstats.collect{it[1]})
                                                      ^^
  ```

- Warning: `subworkflows/local/mirna_quant/main.nf:106:5`: Variable was declared but not used

  ```nextflow
      ch_tsvs = BAM_STATS_MIRNA_MIRTOP.out.counts
      ^^^^^^^
  ```

- Warning: `subworkflows/local/mirna_quant/main.nf:107:18`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          .collect{it[1]}
                   ^^
  ```

- Warning: `subworkflows/local/mirna_quant/main.nf:114:16`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          .map { meta, file -> file }
                 ^^^^
  ```

- Warning: `subworkflows/local/mirna_quant/main.nf:127:27`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          .map { add_suffix(it, "genome") }
                            ^^
  ```

- Warning: `subworkflows/local/prepare_genome/main.nf:98:27`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
                      .map{ meta, index_dir ->
                            ^^^^
  ```

- Warning: `subworkflows/local/utils_nfcore_smrnaseq_pipeline/main.nf:34:5`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
      monochrome_logs         // boolean: Do not use coloured log outputs
      ^^^^^^^^^^^^^^^
  ```

- Warning: `subworkflows/local/utils_nfcore_smrnaseq_pipeline/main.nf:37:5`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
      input                   //  string: Path to input samplesheet
      ^^^^^
  ```

- Warning: `subworkflows/local/utils_nfcore_smrnaseq_pipeline/main.nf:246:35`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          fastqs = fastqs.collect { it.take(1) }
                                    ^^
  ```

- Warning: `subworkflows/nf-core/bam_sort_stats_samtools/main.nf:16:19`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_versions = Channel.empty()
                    ^^^^^^^
  ```

- Warning: `subworkflows/nf-core/bam_stats_mirna_mirtop/main.nf:16:19`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_versions = Channel.empty()
                    ^^^^^^^
  ```

- Warning: `subworkflows/nf-core/bam_stats_samtools/main.nf:15:19`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_versions = Channel.empty()
                    ^^^^^^^
  ```

- Warning: `subworkflows/nf-core/fastq_fastqc_umitools_fastp/main.nf:33:22`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
      catch (Exception ex) {
                       ^^
  ```

- Warning: `subworkflows/nf-core/fastq_fastqc_umitools_fastp/main.nf:51:19`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_versions = Channel.empty()
                    ^^^^^^^
  ```

- Warning: `subworkflows/nf-core/fastq_fastqc_umitools_fastp/main.nf:52:23`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      fastqc_raw_html = Channel.empty()
                        ^^^^^^^
  ```

- Warning: `subworkflows/nf-core/fastq_fastqc_umitools_fastp/main.nf:53:22`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      fastqc_raw_zip = Channel.empty()
                       ^^^^^^^
  ```

- Warning: `subworkflows/nf-core/fastq_fastqc_umitools_fastp/main.nf:54:15`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      umi_log = Channel.empty()
                ^^^^^^^
  ```

- Warning: `subworkflows/nf-core/fastq_fastqc_umitools_fastp/main.nf:55:17`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      trim_json = Channel.empty()
                  ^^^^^^^
  ```

- Warning: `subworkflows/nf-core/fastq_fastqc_umitools_fastp/main.nf:56:17`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      trim_html = Channel.empty()
                  ^^^^^^^
  ```

- Warning: `subworkflows/nf-core/fastq_fastqc_umitools_fastp/main.nf:57:16`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      trim_log = Channel.empty()
                 ^^^^^^^
  ```

- Warning: `subworkflows/nf-core/fastq_fastqc_umitools_fastp/main.nf:58:23`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      trim_reads_fail = Channel.empty()
                        ^^^^^^^
  ```

- Warning: `subworkflows/nf-core/fastq_fastqc_umitools_fastp/main.nf:59:25`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      trim_reads_merged = Channel.empty()
                          ^^^^^^^
  ```

- Warning: `subworkflows/nf-core/fastq_fastqc_umitools_fastp/main.nf:60:24`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      fastqc_trim_html = Channel.empty()
                         ^^^^^^^
  ```

- Warning: `subworkflows/nf-core/fastq_fastqc_umitools_fastp/main.nf:61:23`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      fastqc_trim_zip = Channel.empty()
                        ^^^^^^^
  ```

- Warning: `subworkflows/nf-core/fastq_fastqc_umitools_fastp/main.nf:62:23`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      trim_read_count = Channel.empty()
                        ^^^^^^^
  ```

- Warning: `subworkflows/nf-core/fastq_fastqc_umitools_fastp/main.nf:63:19`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      adapter_seq = Channel.empty()
                    ^^^^^^^
  ```

- Warning: `subworkflows/nf-core/fastq_fastqc_umitools_fastp/main.nf:66:49`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
      reads_only = reads.map { meta, reads_files, adapter_fasta -> [ meta, reads_files ] }
                                                  ^^^^^^^^^^^^^
  ```

- Warning: `subworkflows/nf-core/fastq_fastqc_umitools_fastp/main.nf:104:20`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
              .map { sample_id, meta, umi_reads_files, adapter_fasta -> [meta, umi_reads_files, adapter_fasta] }
                     ^^^^^^^^^
  ```

- Warning: `subworkflows/nf-core/fastq_find_mirna_mirdeep2/main.nf:16:19`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_versions = Channel.empty()
                    ^^^^^^^
  ```

- Warning: `subworkflows/nf-core/utils_nfcore_pipeline/main.nf:101:98`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      return ch_versions.unique().map { version -> processVersionsFromYAML(version) }.unique().mix(Channel.of(workflowVersionToYAML()))
                                                                                                   ^^^^^^^
  ```

- Warning: `workflows/smrnaseq.nf:34:1`: Variable was declared but not used

  ```nextflow
  ch_multiqc_config                     = channel.fromPath("$projectDir/assets/multiqc_config.yml", checkIfExists: true)
  ^^^^^^^^^^^^^^^^^
  ```

- Warning: `workflows/smrnaseq.nf:35:1`: Variable was declared but not used

  ```nextflow
  ch_multiqc_custom_config              = params.multiqc_config ? channel.fromPath( params.multiqc_config, checkIfExists: true ) : channel.empty()
  ^^^^^^^^^^^^^^^^^^^^^^^^
  ```

- Warning: `workflows/smrnaseq.nf:36:1`: Variable was declared but not used

  ```nextflow
  ch_multiqc_logo                       = params.multiqc_logo   ? channel.fromPath( params.multiqc_logo, checkIfExists: true ) : channel.empty()
  ^^^^^^^^^^^^^^^
  ```

- Warning: `workflows/smrnaseq.nf:37:1`: Variable was declared but not used

  ```nextflow
  ch_fastp_adapters                     = channel.fromPath(params.fastp_known_mirna_adapters, checkIfExists: true).collect() // collect to consume for all incoming samples to FASTP
  ^^^^^^^^^^^^^^^^^
  ```

- Warning: `workflows/smrnaseq.nf:295:9`: Variable was declared but not used

  ```nextflow
          ch_multiqc_custom_methods_description = params.multiqc_methods_description ?
          ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  ```

- Warning: `workflows/smrnaseq.nf:314:104`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          ch_multiqc_files = ch_multiqc_files.mix(FASTQ_FASTQC_UMITOOLS_FASTP.out.fastqc_raw_zip.collect{it[1]}.ifEmpty([]))
                                                                                                         ^^
  ```

- Warning: `workflows/smrnaseq.nf:315:105`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          ch_multiqc_files = ch_multiqc_files.mix(FASTQ_FASTQC_UMITOOLS_FASTP.out.fastqc_trim_zip.collect{it[1]}.ifEmpty([]))
                                                                                                          ^^
  ```

- Warning: `workflows/smrnaseq.nf:316:99`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          ch_multiqc_files = ch_multiqc_files.mix(FASTQ_FASTQC_UMITOOLS_FASTP.out.trim_json.collect{it[1]}.ifEmpty([]))
                                                                                                    ^^
  ```

- Warning: `workflows/smrnaseq.nf:318:87`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
              ch_multiqc_files = ch_multiqc_files.mix(UMICOLLAPSE_FASTQ.out.log.collect{it[1]}.ifEmpty([]))
                                                                                        ^^
  ```

- Warning: `workflows/smrnaseq.nf:321:71`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          ch_multiqc_files = ch_multiqc_files.mix(genome_stats.collect({it[1]}).ifEmpty([]))
                                                                        ^^
  ```

- Warning: `workflows/smrnaseq.nf:322:87`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          ch_multiqc_files = ch_multiqc_files.mix(MIRNA_QUANT.out.mature_stats.collect({it[1]}).ifEmpty([]))
                                                                                        ^^
  ```

- Warning: `workflows/smrnaseq.nf:323:88`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          ch_multiqc_files = ch_multiqc_files.mix(MIRNA_QUANT.out.hairpin_stats.collect({it[1]}).ifEmpty([]))
                                                                                         ^^
  ```

- Warning: `workflows/smrnaseq.nf:324:86`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          ch_multiqc_files = ch_multiqc_files.mix(MIRNA_QUANT.out.mirtop_logs.collect({it[1]}).ifEmpty([]))
                                                                                       ^^
  ```

- Warning: `workflows/smrnaseq.nf:326:83`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
              ch_multiqc_files = ch_multiqc_files.mix(MIRTRACE_QC.out.html.collect({it[1]}).ifEmpty([]))
                                                                                    ^^
  ```

- Warning: `workflows/smrnaseq.nf:327:83`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
              ch_multiqc_files = ch_multiqc_files.mix(MIRTRACE_QC.out.json.collect({it[1]}).ifEmpty([]))
                                                                                    ^^
  ```

- Warning: `workflows/smrnaseq.nf:328:82`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
              ch_multiqc_files = ch_multiqc_files.mix(MIRTRACE_QC.out.tsv.collect({it[1]}).ifEmpty([]))
                                                                                   ^^
  ```
