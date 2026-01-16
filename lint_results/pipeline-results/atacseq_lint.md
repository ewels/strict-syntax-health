# Nextflow lint results

- Generated: 2026-01-16T06:28:33.069500195Z
- Nextflow version: 25.12.0-edge
- Summary: 56 errors, 205 warnings

## :x: Errors

- Error: `conf/modules.config:136:1`: If statements cannot be mixed with config statements

  ```nextflow
  if (!(params.skip_fastqc || params.skip_qc)) {
  ^
  ```

- Error: `conf/modules.config:156:1`: If statements cannot be mixed with config statements

  ```nextflow
  if (!params.skip_trimming) {
  ^
  ```

- Error: `conf/modules.config:228:1`: If statements cannot be mixed with config statements

  ```nextflow
  if (params.aligner == 'bwa') {
  ^
  ```

- Error: `conf/modules.config:250:1`: If statements cannot be mixed with config statements

  ```nextflow
  if (params.aligner == 'bowtie2') {
  ^
  ```

- Error: `conf/modules.config:278:1`: If statements cannot be mixed with config statements

  ```nextflow
  if (params.aligner == 'chromap') {
  ^
  ```

- Error: `conf/modules.config:306:1`: If statements cannot be mixed with config statements

  ```nextflow
  if (params.aligner == 'star') {
  ^
  ```

- Error: `conf/modules.config:527:1`: If statements cannot be mixed with config statements

  ```nextflow
  if (!params.skip_picard_metrics) {
  ^
  ```

- Error: `conf/modules.config:548:1`: If statements cannot be mixed with config statements

  ```nextflow
  if (!params.skip_preseq) {
  ^
  ```

- Error: `conf/modules.config:562:1`: If statements cannot be mixed with config statements

  ```nextflow
  if (!params.skip_plot_profile) {
  ^
  ```

- Error: `conf/modules.config:604:1`: If statements cannot be mixed with config statements

  ```nextflow
  if (!params.skip_plot_fingerprint) {
  ^
  ```

- Error: `conf/modules.config:660:1`: If statements cannot be mixed with config statements

  ```nextflow
  if (!params.skip_peak_annotation) {
  ^
  ```

- Error: `conf/modules.config:697:1`: If statements cannot be mixed with config statements

  ```nextflow
  if (!params.skip_consensus_peaks) {
  ^
  ```

- Error: `conf/modules.config:740:1`: If statements cannot be mixed with config statements

  ```nextflow
  if (!params.skip_peak_annotation) {
  ^
  ```

- Error: `conf/modules.config:754:1`: If statements cannot be mixed with config statements

  ```nextflow
  if (!params.skip_ataqv) {
  ^
  ```

- Error: `conf/modules.config:774:1`: If statements cannot be mixed with config statements

  ```nextflow
  if (!params.skip_merge_replicates) {
  ^
  ```

- Error: `conf/modules.config:1009:1`: If statements cannot be mixed with config statements

  ```nextflow
  if (!params.skip_igv) {
  ^
  ```

- Error: `conf/modules.config:1028:1`: If statements cannot be mixed with config statements

  ```nextflow
  if (!params.skip_multiqc) {
  ^
  ```

- Error: `modules/nf-core/bwa/index/main.nf:14:27`: `bwa` is not defined

  ```nextflow
      tuple val(meta), path(bwa) , emit: index
                            ^^^
  ```

- Error: `subworkflows/local/prepare_genome.nf:213:48`: `UNTAR` is not defined

  ```nextflow
                  ch_versions  = ch_versions.mix(UNTAR.out.versions)
                                                 ^^^^^
  ```

- Error: `subworkflows/nf-core/fastq_fastqc_umitools_trimgalore/main.nf:59:31`: `reads` is already declared

  ```nextflow
                          meta, reads ->
                                ^^^^^
  ```

- Error: `subworkflows/nf-core/fastq_fastqc_umitools_trimgalore/main.nf:88:23`: `reads` is already declared

  ```nextflow
                  meta, reads, trim_log ->
                        ^^^^^
  ```

- Error: `subworkflows/nf-core/fastq_fastqc_umitools_trimgalore/main.nf:88:30`: `trim_log` is already declared

  ```nextflow
                  meta, reads, trim_log ->
                               ^^^^^^^^
  ```

- Error: `subworkflows/nf-core/fastq_fastqc_umitools_trimgalore/main.nf:90:25`: Variables in a closure should be declared with `def`

  ```nextflow
                          num_reads = getTrimGaloreReadsAfterFiltering(meta.single_end ? trim_log : trim_log[-1])
                          ^^^^^^^^^
  ```

- Error: `subworkflows/nf-core/fastq_fastqc_umitools_trimgalore/main.nf:99:29`: `reads` is already declared

  ```nextflow
              .filter { meta, reads, num_reads -> num_reads >= min_trimmed_reads.toFloat() }
                              ^^^^^
  ```

- Error: `subworkflows/nf-core/fastq_fastqc_umitools_trimgalore/main.nf:99:36`: `num_reads` is already declared

  ```nextflow
              .filter { meta, reads, num_reads -> num_reads >= min_trimmed_reads.toFloat() }
                                     ^^^^^^^^^
  ```

- Error: `subworkflows/nf-core/fastq_fastqc_umitools_trimgalore/main.nf:100:26`: `reads` is already declared

  ```nextflow
              .map { meta, reads, num_reads -> [ meta, reads ] }
                           ^^^^^
  ```

- Error: `subworkflows/nf-core/fastq_fastqc_umitools_trimgalore/main.nf:100:33`: `num_reads` is already declared

  ```nextflow
              .map { meta, reads, num_reads -> [ meta, reads ] }
                                  ^^^^^^^^^
  ```

- Error: `subworkflows/nf-core/fastq_fastqc_umitools_trimgalore/main.nf:104:26`: `reads` is already declared

  ```nextflow
              .map { meta, reads, num_reads -> [ meta, num_reads ] }
                           ^^^^^
  ```

- Error: `subworkflows/nf-core/fastq_fastqc_umitools_trimgalore/main.nf:104:33`: `num_reads` is already declared

  ```nextflow
              .map { meta, reads, num_reads -> [ meta, num_reads ] }
                                  ^^^^^^^^^
  ```

- Error: `workflows/atacseq.nf:70:1`: Statements cannot be mixed with script declarations -- move statements into a process, workflow, or function

  ```nextflow
  ch_bamtools_filter_se_config = file(params.bamtools_filter_se_config)
  ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  ```

- Error: `workflows/atacseq.nf:71:1`: Statements cannot be mixed with script declarations -- move statements into a process, workflow, or function

  ```nextflow
  ch_bamtools_filter_pe_config = file(params.bamtools_filter_pe_config)
  ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  ```

- Error: `workflows/atacseq.nf:74:1`: Statements cannot be mixed with script declarations -- move statements into a process, workflow, or function

  ```nextflow
  ch_multiqc_merged_library_peak_count_header        = file("$projectDir/assets/multiqc/merged_library_peak_count_header.txt", checkIfExists: true)
  ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  ```

- Error: `workflows/atacseq.nf:75:1`: Statements cannot be mixed with script declarations -- move statements into a process, workflow, or function

  ```nextflow
  ch_multiqc_merged_library_frip_score_header        = file("$projectDir/assets/multiqc/merged_library_frip_score_header.txt", checkIfExists: true)
  ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  ```

- Error: `workflows/atacseq.nf:76:1`: Statements cannot be mixed with script declarations -- move statements into a process, workflow, or function

  ```nextflow
  ch_multiqc_merged_library_peak_annotation_header   = file("$projectDir/assets/multiqc/merged_library_peak_annotation_header.txt", checkIfExists: true)
  ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  ```

- Error: `workflows/atacseq.nf:77:1`: Statements cannot be mixed with script declarations -- move statements into a process, workflow, or function

  ```nextflow
  ch_multiqc_merged_library_deseq2_pca_header        = file("$projectDir/assets/multiqc/merged_library_deseq2_pca_header.txt", checkIfExists: true)
  ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  ```

- Error: `workflows/atacseq.nf:78:1`: Statements cannot be mixed with script declarations -- move statements into a process, workflow, or function

  ```nextflow
  ch_multiqc_merged_library_deseq2_clustering_header = file("$projectDir/assets/multiqc/merged_library_deseq2_clustering_header.txt", checkIfExists: true)
  ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  ```

- Error: `workflows/atacseq.nf:80:1`: Statements cannot be mixed with script declarations -- move statements into a process, workflow, or function

  ```nextflow
  ch_multiqc_merged_replicate_peak_count_header        = file("$projectDir/assets/multiqc/merged_replicate_peak_count_header.txt", checkIfExists: true)
  ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  ```

- Error: `workflows/atacseq.nf:81:1`: Statements cannot be mixed with script declarations -- move statements into a process, workflow, or function

  ```nextflow
  ch_multiqc_merged_replicate_frip_score_header        = file("$projectDir/assets/multiqc/merged_replicate_frip_score_header.txt", checkIfExists: true)
  ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  ```

- Error: `workflows/atacseq.nf:82:1`: Statements cannot be mixed with script declarations -- move statements into a process, workflow, or function

  ```nextflow
  ch_multiqc_merged_replicate_peak_annotation_header   = file("$projectDir/assets/multiqc/merged_replicate_peak_annotation_header.txt", checkIfExists: true)
  ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  ```

- Error: `workflows/atacseq.nf:83:1`: Statements cannot be mixed with script declarations -- move statements into a process, workflow, or function

  ```nextflow
  ch_multiqc_merged_replicate_deseq2_pca_header        = file("$projectDir/assets/multiqc/merged_replicate_deseq2_pca_header.txt", checkIfExists: true)
  ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  ```

- Error: `workflows/atacseq.nf:84:1`: Statements cannot be mixed with script declarations -- move statements into a process, workflow, or function

  ```nextflow
  ch_multiqc_merged_replicate_deseq2_clustering_header = file("$projectDir/assets/multiqc/merged_replicate_deseq2_clustering_header.txt", checkIfExists: true)
  ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  ```

- Error: `workflows/atacseq.nf:87:1`: Statements cannot be mixed with script declarations -- move statements into a process, workflow, or function

  ```nextflow
  ataqv_mito_reference = params.ataqv_mito_reference
  ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  ```

- Error: `workflows/atacseq.nf:88:1`: Statements cannot be mixed with script declarations -- move statements into a process, workflow, or function

  ```nextflow
  if (!params.ataqv_mito_reference && params.mito_name) {
  ^
  ```

- Error: `workflows/atacseq.nf:310:9`: `ch_bamtools_filter_se_config` is not defined

  ```nextflow
          ch_bamtools_filter_se_config,
          ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  ```

- Error: `workflows/atacseq.nf:311:9`: `ch_bamtools_filter_pe_config` is not defined

  ```nextflow
          ch_bamtools_filter_pe_config
          ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  ```

- Error: `workflows/atacseq.nf:472:9`: `ch_multiqc_merged_library_peak_count_header` is not defined

  ```nextflow
          ch_multiqc_merged_library_peak_count_header,
          ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  ```

- Error: `workflows/atacseq.nf:473:9`: `ch_multiqc_merged_library_frip_score_header` is not defined

  ```nextflow
          ch_multiqc_merged_library_frip_score_header,
          ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  ```

- Error: `workflows/atacseq.nf:474:9`: `ch_multiqc_merged_library_peak_annotation_header` is not defined

  ```nextflow
          ch_multiqc_merged_library_peak_annotation_header,
          ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  ```

- Error: `workflows/atacseq.nf:494:13`: `ch_multiqc_merged_library_deseq2_pca_header` is not defined

  ```nextflow
              ch_multiqc_merged_library_deseq2_pca_header,
              ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  ```

- Error: `workflows/atacseq.nf:495:13`: `ch_multiqc_merged_library_deseq2_clustering_header` is not defined

  ```nextflow
              ch_multiqc_merged_library_deseq2_clustering_header,
              ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  ```

- Error: `workflows/atacseq.nf:531:13`: `ataqv_mito_reference` is not defined

  ```nextflow
              ataqv_mito_reference ?: '',
              ^^^^^^^^^^^^^^^^^^^^
  ```

- Error: `workflows/atacseq.nf:680:13`: `ch_multiqc_merged_replicate_peak_count_header` is not defined

  ```nextflow
              ch_multiqc_merged_replicate_peak_count_header,
              ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  ```

- Error: `workflows/atacseq.nf:681:13`: `ch_multiqc_merged_replicate_frip_score_header` is not defined

  ```nextflow
              ch_multiqc_merged_replicate_frip_score_header,
              ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  ```

- Error: `workflows/atacseq.nf:682:13`: `ch_multiqc_merged_replicate_peak_annotation_header` is not defined

  ```nextflow
              ch_multiqc_merged_replicate_peak_annotation_header,
              ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  ```

- Error: `workflows/atacseq.nf:702:17`: `ch_multiqc_merged_replicate_deseq2_pca_header` is not defined

  ```nextflow
                  ch_multiqc_merged_replicate_deseq2_pca_header,
                  ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  ```

- Error: `workflows/atacseq.nf:703:17`: `ch_multiqc_merged_replicate_deseq2_clustering_header` is not defined

  ```nextflow
                  ch_multiqc_merged_replicate_deseq2_clustering_header,
                  ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  ```

## :warning: Warnings

- Warning: `conf/modules.config:403:77`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
              saveAs: { (meta.single_end || params.save_align_intermeds) ? "${it}" : null }
                                                                              ^^
  ```

- Warning: `main.nf:54:19`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_versions = Channel.empty()
                    ^^^^^^^
  ```

- Warning: `main.nf:81:22`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_samplesheet = Channel.value(file(params.input, checkIfExists: true))
                       ^^^^^^^
  ```

- Warning: `modules/local/macs3_consensus.nf:33:46`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
      sort -T '.' -k1,1 -k2,2n ${peaks.collect{it.toString()}.sort().join(' ')} \\
                                               ^^
  ```

- Warning: `modules/local/macs3_consensus.nf:38:25`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          ${peaks.collect{it.toString()}.sort().join(',').replaceAll("_peaks.${peak_type}","")} \\
                          ^^
  ```

- Warning: `modules/nf-core/bowtie2/align/main.nf:93:9`: Variable was declared but not used

  ```nextflow
      def reference = fasta && extension=="cram"  ? "--reference ${fasta}" : ""
          ^^^^^^^^^
  ```

- Warning: `modules/nf-core/bwa/mem/main.nf:56:9`: Variable was declared but not used

  ```nextflow
      def args = task.ext.args ?: ''
          ^^^^
  ```

- Warning: `modules/nf-core/bwa/mem/main.nf:59:9`: Variable was declared but not used

  ```nextflow
      def samtools_command = sort_bam ? 'sort' : 'view'
          ^^^^^^^^^^^^^^^^
  ```

- Warning: `modules/nf-core/custom/getchromsizes/main.nf:23:9`: Variable was declared but not used

  ```nextflow
      def args = task.ext.args ?: ''
          ^^^^
  ```

- Warning: `modules/nf-core/macs3/callpeak/main.nf:34:40`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          def id = args_list.findIndexOf{it=='--format'}
                                         ^^
  ```

- Warning: `modules/nf-core/macs3/callpeak/main.nf:56:9`: Variable was declared but not used

  ```nextflow
      def args = task.ext.args ?: ''
          ^^^^
  ```

- Warning: `modules/nf-core/samtools/flagstat/main.nf:21:9`: Variable was declared but not used

  ```nextflow
      def args = task.ext.args ?: ''
          ^^^^
  ```

- Warning: `modules/nf-core/samtools/idxstats/main.nf:21:9`: Variable was declared but not used

  ```nextflow
      def args = task.ext.args ?: ''
          ^^^^
  ```

- Warning: `modules/nf-core/samtools/stats/main.nf:22:9`: Variable was declared but not used

  ```nextflow
      def args = task.ext.args ?: ''
          ^^^^
  ```

- Warning: `modules/nf-core/trimgalore/main.nf:41:31`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          args_list.removeAll { it.toLowerCase().contains('_r2 ') }
                                ^^
  ```

- Warning: `modules/nf-core/ucsc/bedgraphtobigwig/main.nf:23:9`: Variable was declared but not used

  ```nextflow
      def args = task.ext.args ?: ''
          ^^^^
  ```

- Warning: `subworkflows/local/align_star.nf:17:19`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_versions = Channel.empty()
                    ^^^^^^^
  ```

- Warning: `subworkflows/local/bam_bedgraph_bigwig_bedtools_ucsc.nf:16:19`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_versions = Channel.empty()
                    ^^^^^^^
  ```

- Warning: `subworkflows/local/bam_filter_bamtools.nf:19:19`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_versions = Channel.empty()
                    ^^^^^^^
  ```

- Warning: `subworkflows/local/bam_peaks_call_qc_annotate_macs3_homer.nf:29:19`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_versions = Channel.empty()
                    ^^^^^^^
  ```

- Warning: `subworkflows/local/bam_peaks_call_qc_annotate_macs3_homer.nf:47:13`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
              meta, peaks ->
              ^^^^
  ```

- Warning: `subworkflows/local/bam_peaks_call_qc_annotate_macs3_homer.nf:56:27`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
              meta, ip_bam, control_bam, peaks ->
                            ^^^^^^^^^^^
  ```

- Warning: `subworkflows/local/bam_peaks_call_qc_annotate_macs3_homer.nf:73:19`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
              meta, ip_bam, peaks, frip ->
                    ^^^^^^
  ```

- Warning: `subworkflows/local/bam_peaks_call_qc_annotate_macs3_homer.nf:88:39`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_homer_annotatepeaks          = Channel.empty()
                                        ^^^^^^^
  ```

- Warning: `subworkflows/local/bam_peaks_call_qc_annotate_macs3_homer.nf:89:39`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_plot_macs3_qc_txt            = Channel.empty()
                                        ^^^^^^^
  ```

- Warning: `subworkflows/local/bam_peaks_call_qc_annotate_macs3_homer.nf:90:39`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_plot_macs3_qc_pdf            = Channel.empty()
                                        ^^^^^^^
  ```

- Warning: `subworkflows/local/bam_peaks_call_qc_annotate_macs3_homer.nf:91:39`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_plot_homer_annotatepeaks_txt = Channel.empty()
                                        ^^^^^^^
  ```

- Warning: `subworkflows/local/bam_peaks_call_qc_annotate_macs3_homer.nf:92:39`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_plot_homer_annotatepeaks_pdf = Channel.empty()
                                        ^^^^^^^
  ```

- Warning: `subworkflows/local/bam_peaks_call_qc_annotate_macs3_homer.nf:93:39`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_plot_homer_annotatepeaks_tsv = Channel.empty()
                                        ^^^^^^^
  ```

- Warning: `subworkflows/local/bam_peaks_call_qc_annotate_macs3_homer.nf:111:40`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
                  ch_macs3_peaks.collect{it[1]},
                                         ^^
  ```

- Warning: `subworkflows/local/bam_peaks_call_qc_annotate_macs3_homer.nf:122:53`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
                  HOMER_ANNOTATEPEAKS.out.txt.collect{it[1]},
                                                      ^^
  ```

- Warning: `subworkflows/local/bam_shift_reads.nf:12:19`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_versions = Channel.empty()
                    ^^^^^^^
  ```

- Warning: `subworkflows/local/bed_consensus_quantify_qc_bedtools_featurecounts_deseq2.nf:25:19`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_versions = Channel.empty()
                    ^^^^^^^
  ```

- Warning: `subworkflows/local/bed_consensus_quantify_qc_bedtools_featurecounts_deseq2.nf:30:20`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          .collect { it[1] }
                     ^^
  ```

- Warning: `subworkflows/local/bed_consensus_quantify_qc_bedtools_featurecounts_deseq2.nf:31:19`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          .filter { it.size() > 1 }
                    ^^
  ```

- Warning: `subworkflows/local/bed_consensus_quantify_qc_bedtools_featurecounts_deseq2.nf:50:30`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_homer_annotatepeaks = Channel.empty()
                               ^^^^^^^
  ```

- Warning: `subworkflows/local/bed_consensus_quantify_qc_bedtools_featurecounts_deseq2.nf:64:20`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          .collect { it[1] }
                     ^^
  ```

- Warning: `subworkflows/local/bed_consensus_quantify_qc_bedtools_featurecounts_deseq2.nf:65:19`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          .filter { it.size() > 1 }
                    ^^
  ```

- Warning: `subworkflows/local/bed_consensus_quantify_qc_bedtools_featurecounts_deseq2.nf:66:18`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          .map { [ it ] }
                   ^^
  ```

- Warning: `subworkflows/local/bed_consensus_quantify_qc_bedtools_featurecounts_deseq2.nf:69:19`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          .filter { it.size() == 3 }
                    ^^
  ```

- Warning: `subworkflows/local/bed_consensus_quantify_qc_bedtools_featurecounts_deseq2.nf:87:34`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_deseq2_qc_pdf           = Channel.empty()
                                   ^^^^^^^
  ```

- Warning: `subworkflows/local/bed_consensus_quantify_qc_bedtools_featurecounts_deseq2.nf:88:34`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_deseq2_qc_rdata         = Channel.empty()
                                   ^^^^^^^
  ```

- Warning: `subworkflows/local/bed_consensus_quantify_qc_bedtools_featurecounts_deseq2.nf:89:34`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_deseq2_qc_rds           = Channel.empty()
                                   ^^^^^^^
  ```

- Warning: `subworkflows/local/bed_consensus_quantify_qc_bedtools_featurecounts_deseq2.nf:90:34`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_deseq2_qc_pca_txt       = Channel.empty()
                                   ^^^^^^^
  ```

- Warning: `subworkflows/local/bed_consensus_quantify_qc_bedtools_featurecounts_deseq2.nf:91:34`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_deseq2_qc_pca_multiqc   = Channel.empty()
                                   ^^^^^^^
  ```

- Warning: `subworkflows/local/bed_consensus_quantify_qc_bedtools_featurecounts_deseq2.nf:92:34`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_deseq2_qc_dists_txt     = Channel.empty()
                                   ^^^^^^^
  ```

- Warning: `subworkflows/local/bed_consensus_quantify_qc_bedtools_featurecounts_deseq2.nf:93:34`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_deseq2_qc_dists_multiqc = Channel.empty()
                                   ^^^^^^^
  ```

- Warning: `subworkflows/local/bed_consensus_quantify_qc_bedtools_featurecounts_deseq2.nf:94:34`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_deseq2_qc_log           = Channel.empty()
                                   ^^^^^^^
  ```

- Warning: `subworkflows/local/bed_consensus_quantify_qc_bedtools_featurecounts_deseq2.nf:95:34`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_deseq2_qc_size_factors  = Channel.empty()
                                   ^^^^^^^
  ```

- Warning: `subworkflows/local/bigwig_plot_deeptools.nf:19:19`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_versions = Channel.empty()
                    ^^^^^^^
  ```

- Warning: `subworkflows/local/input_check.nf:11:5`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
      with_control // boolean: samplesheet contains controls
      ^^^^^^^^^^^^
  ```

- Warning: `subworkflows/local/input_check.nf:18:37`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          .map { create_fastq_channel(it, seq_center) }
                                      ^^
  ```

- Warning: `subworkflows/local/prepare_genome.nf:53:19`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_versions = Channel.empty()
                    ^^^^^^^
  ```

- Warning: `subworkflows/local/prepare_genome.nf:58:16`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_fasta = Channel.empty()
                 ^^^^^^^
  ```

- Warning: `subworkflows/local/prepare_genome.nf:60:67`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          ch_fasta    = GUNZIP_FASTA ( [ [:], fasta ] ).gunzip.map{ it[1] }
                                                                    ^^
  ```

- Warning: `subworkflows/local/prepare_genome.nf:63:20`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
          ch_fasta = Channel.value(file(fasta))
                     ^^^^^^^
  ```

- Warning: `subworkflows/local/prepare_genome.nf:71:67`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
              ch_gtf      = GUNZIP_GTF ( [ [:], gtf ] ).gunzip.map{ it[1] }
                                                                    ^^
  ```

- Warning: `subworkflows/local/prepare_genome.nf:74:22`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
              ch_gtf = Channel.value(file(gtf))
                       ^^^^^^^
  ```

- Warning: `subworkflows/local/prepare_genome.nf:78:67`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
              ch_gff      = GUNZIP_GFF ( [ [:], gff ] ).gunzip.map{ it[1] }
                                                                    ^^
  ```

- Warning: `subworkflows/local/prepare_genome.nf:81:22`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
              ch_gff = Channel.value(file(gff))
                       ^^^^^^^
  ```

- Warning: `subworkflows/local/prepare_genome.nf:90:20`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_blacklist = Channel.empty()
                     ^^^^^^^
  ```

- Warning: `subworkflows/local/prepare_genome.nf:93:80`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
              ch_blacklist = GUNZIP_BLACKLIST ( [ [:], blacklist ] ).gunzip.map{ it[1] }
                                                                                 ^^
  ```

- Warning: `subworkflows/local/prepare_genome.nf:96:28`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
              ch_blacklist = Channel.value(file(blacklist))
                             ^^^^^^^
  ```

- Warning: `subworkflows/local/prepare_genome.nf:118:84`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
              ch_gene_bed = GUNZIP_GENE_BED ( [ [:], params.gene_bed ] ).gunzip.map{ it[1] }
                                                                                     ^^
  ```

- Warning: `subworkflows/local/prepare_genome.nf:121:27`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
              ch_gene_bed = Channel.value(file(gene_bed))
                            ^^^^^^^
  ```

- Warning: `subworkflows/local/prepare_genome.nf:130:74`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
              ch_tss_bed = GUNZIP_TSS_BED ( [ [:], tss_bed ] ).gunzip.map{ it[1] }
                                                                           ^^
  ```

- Warning: `subworkflows/local/prepare_genome.nf:133:26`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
              ch_tss_bed = Channel.value(file(tss_bed))
                           ^^^^^^^
  ```

- Warning: `subworkflows/local/prepare_genome.nf:140:50`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
      CUSTOM_GETCHROMSIZES ( ch_fasta.map { [ [:], it ] } )
                                                   ^^
  ```

- Warning: `subworkflows/local/prepare_genome.nf:141:59`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
      ch_chrom_sizes = CUSTOM_GETCHROMSIZES.out.sizes.map { it[1] }
                                                            ^^
  ```

- Warning: `subworkflows/local/prepare_genome.nf:142:56`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
      ch_fai         = CUSTOM_GETCHROMSIZES.out.fai.map{ it[1] }
                                                         ^^
  ```

- Warning: `subworkflows/local/prepare_genome.nf:148:27`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_genome_autosomes = Channel.empty()
                            ^^^^^^^
  ```

- Warning: `subworkflows/local/prepare_genome.nf:159:30`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_genome_filtered_bed = Channel.empty()
                               ^^^^^^^
  ```

- Warning: `subworkflows/local/prepare_genome.nf:172:20`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_bwa_index = Channel.empty()
                     ^^^^^^^
  ```

- Warning: `subworkflows/local/prepare_genome.nf:182:62`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
              ch_bwa_index = BWA_INDEX ( ch_fasta.map { [ [:], it ] } ).index
                                                               ^^
  ```

- Warning: `subworkflows/local/prepare_genome.nf:190:24`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_bowtie2_index = Channel.empty()
                         ^^^^^^^
  ```

- Warning: `subworkflows/local/prepare_genome.nf:200:70`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
              ch_bowtie2_index = BOWTIE2_BUILD ( ch_fasta.map { [ [:], it ] } ).index
                                                                       ^^
  ```

- Warning: `subworkflows/local/prepare_genome.nf:208:24`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_chromap_index = Channel.empty()
                         ^^^^^^^
  ```

- Warning: `subworkflows/local/prepare_genome.nf:218:70`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
              ch_chromap_index = CHROMAP_INDEX ( ch_fasta.map { [ [:], it ] } ).index
                                                                       ^^
  ```

- Warning: `subworkflows/local/prepare_genome.nf:226:21`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_star_index = Channel.empty()
                      ^^^^^^^
  ```

- Warning: `subworkflows/local/prepare_genome.nf:230:85`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
                  ch_star_index = UNTAR_STAR_INDEX ( [ [:], star_index ] ).untar.map{ it[1] }
                                                                                      ^^
  ```

- Warning: `subworkflows/local/prepare_genome.nf:233:33`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
                  ch_star_index = Channel.value(file(star_index))
                                  ^^^^^^^
  ```

- Warning: `subworkflows/local/prepare_genome.nf:250:59`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          ch_macs_gsize = KHMER_UNIQUEKMERS.out.kmers.map { it.text.trim() }
                                                            ^^
  ```

- Warning: `subworkflows/local/utils_nfcore_atacseq_pipeline/main.nf:32:5`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
      monochrome_logs   // boolean: Do not use coloured log outputs
      ^^^^^^^^^^^^^^^
  ```

- Warning: `subworkflows/local/utils_nfcore_atacseq_pipeline/main.nf:35:5`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
      input             //  string: Path to input samplesheet
      ^^^^^
  ```

- Warning: `subworkflows/local/utils_nfcore_atacseq_pipeline/main.nf:42:5`: Variable was declared but not used

  ```nextflow
      ch_versions = channel.empty()
      ^^^^^^^^^^^
  ```

- Warning: `subworkflows/nf-core/bam_markduplicates_picard/main.nf:18:19`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_versions = Channel.empty()
                    ^^^^^^^
  ```

- Warning: `subworkflows/nf-core/bam_sort_stats_samtools/main.nf:16:19`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_versions = Channel.empty()
                    ^^^^^^^
  ```

- Warning: `subworkflows/nf-core/bam_stats_samtools/main.nf:15:19`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_versions = Channel.empty()
                    ^^^^^^^
  ```

- Warning: `subworkflows/nf-core/fastq_align_bowtie2/main.nf:18:19`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_versions = Channel.empty()
                    ^^^^^^^
  ```

- Warning: `subworkflows/nf-core/fastq_align_bwa/main.nf:16:19`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_versions = Channel.empty()
                    ^^^^^^^
  ```

- Warning: `subworkflows/nf-core/fastq_align_chromap/main.nf:19:19`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_versions = Channel.empty()
                    ^^^^^^^
  ```

- Warning: `subworkflows/nf-core/fastq_fastqc_umitools_trimgalore/main.nf:35:19`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_versions = Channel.empty()
                    ^^^^^^^
  ```

- Warning: `subworkflows/nf-core/fastq_fastqc_umitools_trimgalore/main.nf:36:19`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      fastqc_html = Channel.empty()
                    ^^^^^^^
  ```

- Warning: `subworkflows/nf-core/fastq_fastqc_umitools_trimgalore/main.nf:37:19`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      fastqc_zip  = Channel.empty()
                    ^^^^^^^
  ```

- Warning: `subworkflows/nf-core/fastq_fastqc_umitools_trimgalore/main.nf:46:17`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      umi_log   = Channel.empty()
                  ^^^^^^^
  ```

- Warning: `subworkflows/nf-core/fastq_fastqc_umitools_trimgalore/main.nf:67:23`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      trim_unpaired   = Channel.empty()
                        ^^^^^^^
  ```

- Warning: `subworkflows/nf-core/fastq_fastqc_umitools_trimgalore/main.nf:68:23`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      trim_html       = Channel.empty()
                        ^^^^^^^
  ```

- Warning: `subworkflows/nf-core/fastq_fastqc_umitools_trimgalore/main.nf:69:23`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      trim_zip        = Channel.empty()
                        ^^^^^^^
  ```

- Warning: `subworkflows/nf-core/fastq_fastqc_umitools_trimgalore/main.nf:70:23`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      trim_log        = Channel.empty()
                        ^^^^^^^
  ```

- Warning: `subworkflows/nf-core/fastq_fastqc_umitools_trimgalore/main.nf:71:23`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      trim_read_count = Channel.empty()
                        ^^^^^^^
  ```

- Warning: `subworkflows/nf-core/fastq_fastqc_umitools_trimgalore/main.nf:99:23`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
              .filter { meta, reads, num_reads -> num_reads >= min_trimmed_reads.toFloat() }
                        ^^^^
  ```

- Warning: `subworkflows/nf-core/fastq_fastqc_umitools_trimgalore/main.nf:99:29`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
              .filter { meta, reads, num_reads -> num_reads >= min_trimmed_reads.toFloat() }
                              ^^^^^
  ```

- Warning: `subworkflows/nf-core/fastq_fastqc_umitools_trimgalore/main.nf:100:33`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
              .map { meta, reads, num_reads -> [ meta, reads ] }
                                  ^^^^^^^^^
  ```

- Warning: `subworkflows/nf-core/fastq_fastqc_umitools_trimgalore/main.nf:104:26`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
              .map { meta, reads, num_reads -> [ meta, num_reads ] }
                           ^^^^^
  ```

- Warning: `workflows/atacseq.nf:70:1`: Variable was declared but not used

  ```nextflow
  ch_bamtools_filter_se_config = file(params.bamtools_filter_se_config)
  ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  ```

- Warning: `workflows/atacseq.nf:71:1`: Variable was declared but not used

  ```nextflow
  ch_bamtools_filter_pe_config = file(params.bamtools_filter_pe_config)
  ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  ```

- Warning: `workflows/atacseq.nf:74:1`: Variable was declared but not used

  ```nextflow
  ch_multiqc_merged_library_peak_count_header        = file("$projectDir/assets/multiqc/merged_library_peak_count_header.txt", checkIfExists: true)
  ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  ```

- Warning: `workflows/atacseq.nf:75:1`: Variable was declared but not used

  ```nextflow
  ch_multiqc_merged_library_frip_score_header        = file("$projectDir/assets/multiqc/merged_library_frip_score_header.txt", checkIfExists: true)
  ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  ```

- Warning: `workflows/atacseq.nf:76:1`: Variable was declared but not used

  ```nextflow
  ch_multiqc_merged_library_peak_annotation_header   = file("$projectDir/assets/multiqc/merged_library_peak_annotation_header.txt", checkIfExists: true)
  ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  ```

- Warning: `workflows/atacseq.nf:77:1`: Variable was declared but not used

  ```nextflow
  ch_multiqc_merged_library_deseq2_pca_header        = file("$projectDir/assets/multiqc/merged_library_deseq2_pca_header.txt", checkIfExists: true)
  ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  ```

- Warning: `workflows/atacseq.nf:78:1`: Variable was declared but not used

  ```nextflow
  ch_multiqc_merged_library_deseq2_clustering_header = file("$projectDir/assets/multiqc/merged_library_deseq2_clustering_header.txt", checkIfExists: true)
  ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  ```

- Warning: `workflows/atacseq.nf:80:1`: Variable was declared but not used

  ```nextflow
  ch_multiqc_merged_replicate_peak_count_header        = file("$projectDir/assets/multiqc/merged_replicate_peak_count_header.txt", checkIfExists: true)
  ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  ```

- Warning: `workflows/atacseq.nf:81:1`: Variable was declared but not used

  ```nextflow
  ch_multiqc_merged_replicate_frip_score_header        = file("$projectDir/assets/multiqc/merged_replicate_frip_score_header.txt", checkIfExists: true)
  ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  ```

- Warning: `workflows/atacseq.nf:82:1`: Variable was declared but not used

  ```nextflow
  ch_multiqc_merged_replicate_peak_annotation_header   = file("$projectDir/assets/multiqc/merged_replicate_peak_annotation_header.txt", checkIfExists: true)
  ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  ```

- Warning: `workflows/atacseq.nf:83:1`: Variable was declared but not used

  ```nextflow
  ch_multiqc_merged_replicate_deseq2_pca_header        = file("$projectDir/assets/multiqc/merged_replicate_deseq2_pca_header.txt", checkIfExists: true)
  ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  ```

- Warning: `workflows/atacseq.nf:84:1`: Variable was declared but not used

  ```nextflow
  ch_multiqc_merged_replicate_deseq2_clustering_header = file("$projectDir/assets/multiqc/merged_replicate_deseq2_clustering_header.txt", checkIfExists: true)
  ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  ```

- Warning: `workflows/atacseq.nf:112:24`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_multiqc_files = Channel.empty()
                         ^^^^^^^
  ```

- Warning: `workflows/atacseq.nf:134:29`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
              .filter { meta, reads -> meta.single_end }
                              ^^^^^
  ```

- Warning: `workflows/atacseq.nf:162:28`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_genome_bam        = Channel.empty()
                             ^^^^^^^
  ```

- Warning: `workflows/atacseq.nf:163:28`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_samtools_stats    = Channel.empty()
                             ^^^^^^^
  ```

- Warning: `workflows/atacseq.nf:164:28`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_samtools_flagstat = Channel.empty()
                             ^^^^^^^
  ```

- Warning: `workflows/atacseq.nf:165:28`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_samtools_idxstats = Channel.empty()
                             ^^^^^^^
  ```

- Warning: `workflows/atacseq.nf:173:32`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
                          [ [:], it ]
                                 ^^
  ```

- Warning: `workflows/atacseq.nf:194:28`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
                      [ [:], it ]
                             ^^
  ```

- Warning: `workflows/atacseq.nf:213:28`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
                      [ [:], it ]
                             ^^
  ```

- Warning: `workflows/atacseq.nf:221:9`: Variable was declared but not used

  ```nextflow
          ch_genome_bam_index  = FASTQ_ALIGN_CHROMAP.out.bai
          ^^^^^^^^^^^^^^^^^^^
  ```

- Warning: `workflows/atacseq.nf:231:23`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_star_multiqc = Channel.empty()
                        ^^^^^^^
  ```

- Warning: `workflows/atacseq.nf:238:28`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
                      [ [:], it ]
                             ^^
  ```

- Warning: `workflows/atacseq.nf:281:24`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
                  [ [:], it ]
                         ^^
  ```

- Warning: `workflows/atacseq.nf:285:24`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
                  [ [:], it ]
                         ^^
  ```

- Warning: `workflows/atacseq.nf:308:24`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
                  [ [:], it ]
                         ^^
  ```

- Warning: `workflows/atacseq.nf:318:25`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_preseq_multiqc = Channel.empty()
                          ^^^^^^^
  ```

- Warning: `workflows/atacseq.nf:330:47`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_picardcollectmultiplemetrics_multiqc = Channel.empty()
                                                ^^^^^^^
  ```

- Warning: `workflows/atacseq.nf:337:23`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
                      [ it[0], it[1], [] ]
                        ^^
  ```

- Warning: `workflows/atacseq.nf:337:30`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
                      [ it[0], it[1], [] ]
                               ^^
  ```

- Warning: `workflows/atacseq.nf:341:28`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
                      [ [:], it ]
                             ^^
  ```

- Warning: `workflows/atacseq.nf:345:28`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
                      [ [:], it ]
                             ^^
  ```

- Warning: `workflows/atacseq.nf:365:24`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
                  [ [:], it ]
                         ^^
  ```

- Warning: `workflows/atacseq.nf:391:39`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_deeptoolsplotprofile_multiqc = Channel.empty()
                                        ^^^^^^^
  ```

- Warning: `workflows/atacseq.nf:437:43`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_deeptoolsplotfingerprint_multiqc = Channel.empty()
                                            ^^^^^^^
  ```

- Warning: `workflows/atacseq.nf:450:29`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
                  meta, bams, bais ->
                              ^^^^
  ```

- Warning: `workflows/atacseq.nf:457:28`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
                  meta, bam, bai ->
                             ^^^
  ```

- Warning: `workflows/atacseq.nf:484:44`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_macs3_consensus_library_bed       = Channel.empty()
                                             ^^^^^^^
  ```

- Warning: `workflows/atacseq.nf:485:44`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_featurecounts_library_multiqc     = Channel.empty()
                                             ^^^^^^^
  ```

- Warning: `workflows/atacseq.nf:486:44`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_deseq2_pca_library_multiqc        = Channel.empty()
                                             ^^^^^^^
  ```

- Warning: `workflows/atacseq.nf:487:44`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_deseq2_clustering_library_multiqc = Channel.empty()
                                             ^^^^^^^
  ```

- Warning: `workflows/atacseq.nf:539:57`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
              MERGED_LIBRARY_ATAQV_ATAQV.out.json.collect{it[1]}
                                                          ^^
  ```

- Warning: `workflows/atacseq.nf:547:59`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_markduplicates_replicate_stats                   = Channel.empty()
                                                            ^^^^^^^
  ```

- Warning: `workflows/atacseq.nf:548:59`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_markduplicates_replicate_flagstat                = Channel.empty()
                                                            ^^^^^^^
  ```

- Warning: `workflows/atacseq.nf:549:59`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_markduplicates_replicate_idxstats                = Channel.empty()
                                                            ^^^^^^^
  ```

- Warning: `workflows/atacseq.nf:550:59`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_markduplicates_replicate_metrics                 = Channel.empty()
                                                            ^^^^^^^
  ```

- Warning: `workflows/atacseq.nf:551:59`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_ucsc_bedgraphtobigwig_replicate_bigwig           = Channel.empty()
                                                            ^^^^^^^
  ```

- Warning: `workflows/atacseq.nf:552:59`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_macs3_replicate_peaks                            = Channel.empty()
                                                            ^^^^^^^
  ```

- Warning: `workflows/atacseq.nf:553:59`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_macs3_frip_replicate_multiqc                     = Channel.empty()
                                                            ^^^^^^^
  ```

- Warning: `workflows/atacseq.nf:554:59`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_macs3_peak_count_replicate_multiqc               = Channel.empty()
                                                            ^^^^^^^
  ```

- Warning: `workflows/atacseq.nf:555:59`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_macs3_plot_homer_annotatepeaks_replicate_multiqc = Channel.empty()
                                                            ^^^^^^^
  ```

- Warning: `workflows/atacseq.nf:556:59`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_macs3_consensus_replicate_bed                    = Channel.empty()
                                                            ^^^^^^^
  ```

- Warning: `workflows/atacseq.nf:557:59`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_featurecounts_replicate_multiqc                  = Channel.empty()
                                                            ^^^^^^^
  ```

- Warning: `workflows/atacseq.nf:558:59`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_deseq2_pca_replicate_multiqc                     = Channel.empty()
                                                            ^^^^^^^
  ```

- Warning: `workflows/atacseq.nf:559:59`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_deseq2_clustering_replicate_multiqc              = Channel.empty()
                                                            ^^^^^^^
  ```

- Warning: `workflows/atacseq.nf:575:17`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
                  id, metas, bams ->
                  ^^
  ```

- Warning: `workflows/atacseq.nf:597:28`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
                      [ [:], it ]
                             ^^
  ```

- Warning: `workflows/atacseq.nf:601:28`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
                      [ [:], it ]
                             ^^
  ```

- Warning: `workflows/atacseq.nf:624:28`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
                      [ [:], it ]
                             ^^
  ```

- Warning: `workflows/atacseq.nf:723:61`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
              MERGED_LIBRARY_BAM_TO_BIGWIG.out.bigwig.collect{it[1]}.ifEmpty([]),
                                                              ^^
  ```

- Warning: `workflows/atacseq.nf:724:66`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
              MERGED_LIBRARY_CALL_ANNOTATE_PEAKS.out.peaks.collect{it[1]}.ifEmpty([]),
                                                                   ^^
  ```

- Warning: `workflows/atacseq.nf:725:52`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
              ch_macs3_consensus_library_bed.collect{it[1]}.ifEmpty([]),
                                                     ^^
  ```

- Warning: `workflows/atacseq.nf:726:63`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
              ch_ucsc_bedgraphtobigwig_replicate_bigwig.collect{it[1]}.ifEmpty([]),
                                                                ^^
  ```

- Warning: `workflows/atacseq.nf:727:46`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
              ch_macs3_replicate_peaks.collect{it[1]}.ifEmpty([]),
                                               ^^
  ```

- Warning: `workflows/atacseq.nf:728:54`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
              ch_macs3_consensus_replicate_bed.collect{it[1]}.ifEmpty([]),
                                                       ^^
  ```

- Warning: `workflows/atacseq.nf:752:26`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      def topic_versions = Channel.topic("versions")
                           ^^^^^^^
  ```

- Warning: `workflows/atacseq.nf:783:49`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
          ch_multiqc_config                     = Channel.fromPath("$projectDir/assets/multiqc_config.yml", checkIfExists: true)
                                                  ^^^^^^^
  ```

- Warning: `workflows/atacseq.nf:784:73`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
          ch_multiqc_custom_config              = params.multiqc_config ? Channel.fromPath(params.multiqc_config) : Channel.empty()
                                                                          ^^^^^^^
  ```

- Warning: `workflows/atacseq.nf:784:115`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
          ch_multiqc_custom_config              = params.multiqc_config ? Channel.fromPath(params.multiqc_config) : Channel.empty()
                                                                                                                    ^^^^^^^
  ```

- Warning: `workflows/atacseq.nf:785:73`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
          ch_multiqc_logo                       = params.multiqc_logo   ? Channel.fromPath(params.multiqc_logo)   : Channel.empty()
                                                                          ^^^^^^^
  ```

- Warning: `workflows/atacseq.nf:785:115`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
          ch_multiqc_logo                       = params.multiqc_logo   ? Channel.fromPath(params.multiqc_logo)   : Channel.empty()
                                                                                                                    ^^^^^^^
  ```

- Warning: `workflows/atacseq.nf:787:49`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
          ch_workflow_summary                   = Channel.value(paramsSummaryMultiqc(summary_params))
                                                  ^^^^^^^
  ```

- Warning: `workflows/atacseq.nf:789:49`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
          ch_methods_description                = Channel.value(methodsDescriptionText(ch_multiqc_custom_methods_description))
                                                  ^^^^^^^
  ```

- Warning: `workflows/atacseq.nf:800:69`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
              FASTQ_FASTQC_UMITOOLS_TRIMGALORE.out.fastqc_zip.collect{it[1]}.ifEmpty([]),
                                                                      ^^
  ```

- Warning: `workflows/atacseq.nf:801:67`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
              FASTQ_FASTQC_UMITOOLS_TRIMGALORE.out.trim_zip.collect{it[1]}.ifEmpty([]),
                                                                    ^^
  ```

- Warning: `workflows/atacseq.nf:802:67`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
              FASTQ_FASTQC_UMITOOLS_TRIMGALORE.out.trim_log.collect{it[1]}.ifEmpty([]),
                                                                    ^^
  ```

- Warning: `workflows/atacseq.nf:804:39`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
              ch_samtools_stats.collect{it[1]}.ifEmpty([]),
                                        ^^
  ```

- Warning: `workflows/atacseq.nf:805:42`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
              ch_samtools_flagstat.collect{it[1]}.ifEmpty([]),
                                           ^^
  ```

- Warning: `workflows/atacseq.nf:806:42`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
              ch_samtools_idxstats.collect{it[1]}.ifEmpty([]),
                                           ^^
  ```

- Warning: `workflows/atacseq.nf:808:68`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
              MERGED_LIBRARY_MARKDUPLICATES_PICARD.out.stats.collect{it[1]}.ifEmpty([]),
                                                                     ^^
  ```

- Warning: `workflows/atacseq.nf:809:71`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
              MERGED_LIBRARY_MARKDUPLICATES_PICARD.out.flagstat.collect{it[1]}.ifEmpty([]),
                                                                        ^^
  ```

- Warning: `workflows/atacseq.nf:810:71`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
              MERGED_LIBRARY_MARKDUPLICATES_PICARD.out.idxstats.collect{it[1]}.ifEmpty([]),
                                                                        ^^
  ```

- Warning: `workflows/atacseq.nf:811:70`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
              MERGED_LIBRARY_MARKDUPLICATES_PICARD.out.metrics.collect{it[1]}.ifEmpty([]),
                                                                       ^^
  ```

- Warning: `workflows/atacseq.nf:813:57`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
              MERGED_LIBRARY_FILTER_BAM.out.stats.collect{it[1]}.ifEmpty([]),
                                                          ^^
  ```

- Warning: `workflows/atacseq.nf:814:60`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
              MERGED_LIBRARY_FILTER_BAM.out.flagstat.collect{it[1]}.ifEmpty([]),
                                                             ^^
  ```

- Warning: `workflows/atacseq.nf:815:60`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
              MERGED_LIBRARY_FILTER_BAM.out.idxstats.collect{it[1]}.ifEmpty([]),
                                                             ^^
  ```

- Warning: `workflows/atacseq.nf:816:61`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
              ch_picardcollectmultiplemetrics_multiqc.collect{it[1]}.ifEmpty([]),
                                                              ^^
  ```

- Warning: `workflows/atacseq.nf:818:39`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
              ch_preseq_multiqc.collect{it[1]}.ifEmpty([]),
                                        ^^
  ```

- Warning: `workflows/atacseq.nf:820:53`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
              ch_deeptoolsplotprofile_multiqc.collect{it[1]}.ifEmpty([]),
                                                      ^^
  ```

- Warning: `workflows/atacseq.nf:821:57`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
              ch_deeptoolsplotfingerprint_multiqc.collect{it[1]}.ifEmpty([]),
                                                          ^^
  ```

- Warning: `workflows/atacseq.nf:823:73`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
              MERGED_LIBRARY_CALL_ANNOTATE_PEAKS.out.frip_multiqc.collect{it[1]}.ifEmpty([]),
                                                                          ^^
  ```

- Warning: `workflows/atacseq.nf:824:79`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
              MERGED_LIBRARY_CALL_ANNOTATE_PEAKS.out.peak_count_multiqc.collect{it[1]}.ifEmpty([]),
                                                                                ^^
  ```

- Warning: `workflows/atacseq.nf:826:54`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
              ch_featurecounts_library_multiqc.collect{it[1]}.ifEmpty([]),
                                                       ^^
  ```

- Warning: `workflows/atacseq.nf:828:55`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
              ch_markduplicates_replicate_stats.collect{it[1]}.ifEmpty([]),
                                                        ^^
  ```

- Warning: `workflows/atacseq.nf:829:58`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
              ch_markduplicates_replicate_flagstat.collect{it[1]}.ifEmpty([]),
                                                           ^^
  ```

- Warning: `workflows/atacseq.nf:830:58`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
              ch_markduplicates_replicate_idxstats.collect{it[1]}.ifEmpty([]),
                                                           ^^
  ```

- Warning: `workflows/atacseq.nf:831:57`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
              ch_markduplicates_replicate_metrics.collect{it[1]}.ifEmpty([]),
                                                          ^^
  ```

- Warning: `workflows/atacseq.nf:833:53`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
              ch_macs3_frip_replicate_multiqc.collect{it[1]}.ifEmpty([]),
                                                      ^^
  ```

- Warning: `workflows/atacseq.nf:834:59`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
              ch_macs3_peak_count_replicate_multiqc.collect{it[1]}.ifEmpty([]),
                                                            ^^
  ```

- Warning: `workflows/atacseq.nf:836:56`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
              ch_featurecounts_replicate_multiqc.collect{it[1]}.ifEmpty([]),
                                                         ^^
  ```
