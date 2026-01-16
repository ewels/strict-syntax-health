# Nextflow lint results

- Generated: 2026-01-16T10:18:08.015620331Z
- Nextflow version: 25.12.0-edge
- Summary: 47 errors, 181 warnings

## :x: Errors

- Error: `conf/modules.config:112:1`: If statements cannot be mixed with config statements

  ```nextflow
  if (!(params.skip_fastqc || params.skip_qc)) {
  ^
  ```

- Error: `conf/modules.config:132:1`: If statements cannot be mixed with config statements

  ```nextflow
  if (!params.skip_trimming) {
  ^
  ```

- Error: `conf/modules.config:203:1`: If statements cannot be mixed with config statements

  ```nextflow
  if (params.aligner == 'bwa') {
  ^
  ```

- Error: `conf/modules.config:225:1`: If statements cannot be mixed with config statements

  ```nextflow
  if (params.aligner == 'bowtie2') {
  ^
  ```

- Error: `conf/modules.config:253:1`: If statements cannot be mixed with config statements

  ```nextflow
  if (params.aligner == 'chromap') {
  ^
  ```

- Error: `conf/modules.config:277:1`: If statements cannot be mixed with config statements

  ```nextflow
  if (params.aligner == 'star') {
  ^
  ```

- Error: `conf/modules.config:491:1`: If statements cannot be mixed with config statements

  ```nextflow
  if (!params.skip_picard_metrics) {
  ^
  ```

- Error: `conf/modules.config:512:1`: If statements cannot be mixed with config statements

  ```nextflow
  if (!params.skip_preseq) {
  ^
  ```

- Error: `conf/modules.config:526:1`: If statements cannot be mixed with config statements

  ```nextflow
  if (!params.skip_plot_profile) {
  ^
  ```

- Error: `conf/modules.config:558:1`: If statements cannot be mixed with config statements

  ```nextflow
  if (!params.skip_plot_fingerprint) {
  ^
  ```

- Error: `conf/modules.config:610:1`: If statements cannot be mixed with config statements

  ```nextflow
  if (!params.skip_peak_annotation) {
  ^
  ```

- Error: `conf/modules.config:647:1`: If statements cannot be mixed with config statements

  ```nextflow
  if (!params.skip_consensus_peaks) {
  ^
  ```

- Error: `conf/modules.config:714:1`: If statements cannot be mixed with config statements

  ```nextflow
  if (!params.skip_igv) {
  ^
  ```

- Error: `conf/modules.config:733:1`: If statements cannot be mixed with config statements

  ```nextflow
  if (!params.skip_multiqc) {
  ^
  ```

- Error: `modules/nf-core/bwa/index/main.nf:14:27`: `bwa` is not defined

  ```nextflow
      tuple val(meta), path(bwa) , emit: index
                            ^^^
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

- Error: `workflows/chipseq.nf:65:1`: Statements cannot be mixed with script declarations -- move statements into a process, workflow, or function

  ```nextflow
  ch_bamtools_filter_se_config = file(params.bamtools_filter_se_config)
  ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  ```

- Error: `workflows/chipseq.nf:66:1`: Statements cannot be mixed with script declarations -- move statements into a process, workflow, or function

  ```nextflow
  ch_bamtools_filter_pe_config = file(params.bamtools_filter_pe_config)
  ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  ```

- Error: `workflows/chipseq.nf:69:1`: Statements cannot be mixed with script declarations -- move statements into a process, workflow, or function

  ```nextflow
  ch_spp_nsc_header           = file("$projectDir/assets/multiqc/spp_nsc_header.txt", checkIfExists: true)
  ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  ```

- Error: `workflows/chipseq.nf:70:1`: Statements cannot be mixed with script declarations -- move statements into a process, workflow, or function

  ```nextflow
  ch_spp_rsc_header           = file("$projectDir/assets/multiqc/spp_rsc_header.txt", checkIfExists: true)
  ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  ```

- Error: `workflows/chipseq.nf:71:1`: Statements cannot be mixed with script declarations -- move statements into a process, workflow, or function

  ```nextflow
  ch_spp_correlation_header   = file("$projectDir/assets/multiqc/spp_correlation_header.txt", checkIfExists: true)
  ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  ```

- Error: `workflows/chipseq.nf:72:1`: Statements cannot be mixed with script declarations -- move statements into a process, workflow, or function

  ```nextflow
  ch_peak_count_header        = file("$projectDir/assets/multiqc/peak_count_header.txt", checkIfExists: true)
  ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  ```

- Error: `workflows/chipseq.nf:73:1`: Statements cannot be mixed with script declarations -- move statements into a process, workflow, or function

  ```nextflow
  ch_frip_score_header        = file("$projectDir/assets/multiqc/frip_score_header.txt", checkIfExists: true)
  ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  ```

- Error: `workflows/chipseq.nf:74:1`: Statements cannot be mixed with script declarations -- move statements into a process, workflow, or function

  ```nextflow
  ch_peak_annotation_header   = file("$projectDir/assets/multiqc/peak_annotation_header.txt", checkIfExists: true)
  ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  ```

- Error: `workflows/chipseq.nf:75:1`: Statements cannot be mixed with script declarations -- move statements into a process, workflow, or function

  ```nextflow
  ch_deseq2_pca_header        = Channel.value(file("$projectDir/assets/multiqc/deseq2_pca_header.txt", checkIfExists: true))
  ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  ```

- Error: `workflows/chipseq.nf:76:1`: Statements cannot be mixed with script declarations -- move statements into a process, workflow, or function

  ```nextflow
  ch_deseq2_clustering_header = Channel.value(file("$projectDir/assets/multiqc/deseq2_clustering_header.txt", checkIfExists: true))
  ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  ```

- Error: `workflows/chipseq.nf:79:1`: Statements cannot be mixed with script declarations -- move statements into a process, workflow, or function

  ```nextflow
  def anno_readme = params.genomes[ params.genome ]?.readme
  ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  ```

- Error: `workflows/chipseq.nf:80:1`: Statements cannot be mixed with script declarations -- move statements into a process, workflow, or function

  ```nextflow
  if (anno_readme && file(anno_readme).exists()) {
  ^
  ```

- Error: `workflows/chipseq.nf:278:9`: `ch_bamtools_filter_se_config` is not defined

  ```nextflow
          ch_bamtools_filter_se_config,
          ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  ```

- Error: `workflows/chipseq.nf:279:9`: `ch_bamtools_filter_pe_config` is not defined

  ```nextflow
          ch_bamtools_filter_pe_config
          ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  ```

- Error: `workflows/chipseq.nf:339:13`: `ch_spp_nsc_header` is not defined

  ```nextflow
              ch_spp_nsc_header,
              ^^^^^^^^^^^^^^^^^
  ```

- Error: `workflows/chipseq.nf:340:13`: `ch_spp_rsc_header` is not defined

  ```nextflow
              ch_spp_rsc_header,
              ^^^^^^^^^^^^^^^^^
  ```

- Error: `workflows/chipseq.nf:341:13`: `ch_spp_correlation_header` is not defined

  ```nextflow
              ch_spp_correlation_header
              ^^^^^^^^^^^^^^^^^^^^^^^^^
  ```

- Error: `workflows/chipseq.nf:455:9`: `ch_peak_count_header` is not defined

  ```nextflow
          ch_peak_count_header,
          ^^^^^^^^^^^^^^^^^^^^
  ```

- Error: `workflows/chipseq.nf:456:9`: `ch_frip_score_header` is not defined

  ```nextflow
          ch_frip_score_header,
          ^^^^^^^^^^^^^^^^^^^^
  ```

- Error: `workflows/chipseq.nf:457:9`: `ch_peak_annotation_header` is not defined

  ```nextflow
          ch_peak_annotation_header,
          ^^^^^^^^^^^^^^^^^^^^^^^^^
  ```

- Error: `workflows/chipseq.nf:491:13`: `ch_deseq2_pca_header` is not defined

  ```nextflow
              ch_deseq2_pca_header,
              ^^^^^^^^^^^^^^^^^^^^
  ```

- Error: `workflows/chipseq.nf:492:13`: `ch_deseq2_clustering_header` is not defined

  ```nextflow
              ch_deseq2_clustering_header,
              ^^^^^^^^^^^^^^^^^^^^^^^^^^^
  ```

## :warning: Warnings

- Warning: `conf/modules.config:375:77`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
              saveAs: { (meta.single_end || params.save_align_intermeds) ? "${it}" : null }
                                                                              ^^
  ```

- Warning: `main.nf:52:19`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_versions = Channel.empty()
                    ^^^^^^^
  ```

- Warning: `main.nf:74:22`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_samplesheet = Channel.value(file(params.input, checkIfExists: true))
                       ^^^^^^^
  ```

- Warning: `modules/local/macs3_consensus.nf:37:46`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
      sort -T '.' -k1,1 -k2,2n ${peaks.collect{it.toString()}.sort().join(' ')} \\
                                               ^^
  ```

- Warning: `modules/local/macs3_consensus.nf:42:25`: Implicit closure parameter is deprecated, declare an explicit parameter instead

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

- Warning: `modules/nf-core/gffread/main.nf:26:103`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
      def extension   = args.contains("-T")       ? 'gtf' : ( ( ['-w', '-x', '-y' ].any { args.contains(it) } ) ? 'fasta' : 'gff3' )
                                                                                                        ^^
  ```

- Warning: `modules/nf-core/gffread/main.nf:30:61`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
      def args_sorted = args.replaceAll(/(.*)(-[wxy])(.*)/) { all, pre, param, post -> "$pre $post $param" }.trim()
                                                              ^^^
  ```

- Warning: `modules/nf-core/gffread/main.nf:49:103`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
      def extension   = args.contains("-T")       ? 'gtf' : ( ( ['-w', '-x', '-y' ].any { args.contains(it) } ) ? 'fasta' : 'gff3' )
                                                                                                        ^^
  ```

- Warning: `modules/nf-core/gunzip/main.nf:43:9`: Variable was declared but not used

  ```nextflow
      def args        = task.ext.args ?: ''
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

- Warning: `subworkflows/local/bam_bedgraph_bigwig_bedtools_ucsc.nf:15:19`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

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

- Warning: `subworkflows/local/bed_consensus_quantify_qc_bedtools_featurecounts_deseq2.nf:26:19`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_versions = Channel.empty()
                    ^^^^^^^
  ```

- Warning: `subworkflows/local/bed_consensus_quantify_qc_bedtools_featurecounts_deseq2.nf:40:57`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
                      groups.groupBy().collectEntries { [(it.key) : it.value.size()] },
                                                          ^^
  ```

- Warning: `subworkflows/local/bed_consensus_quantify_qc_bedtools_featurecounts_deseq2.nf:40:67`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
                      groups.groupBy().collectEntries { [(it.key) : it.value.size()] },
                                                                    ^^
  ```

- Warning: `subworkflows/local/bed_consensus_quantify_qc_bedtools_featurecounts_deseq2.nf:49:58`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
                  meta_new.replicates_exist = groups.max { it.value }.value > 1
                                                           ^^
  ```

- Warning: `subworkflows/local/bed_consensus_quantify_qc_bedtools_featurecounts_deseq2.nf:93:13`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
              antibody, meta, saf, bams, meta_single_end ->
              ^^^^^^^^
  ```

- Warning: `subworkflows/local/bed_consensus_quantify_qc_bedtools_featurecounts_deseq2.nf:109:34`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_deseq2_qc_pdf           = Channel.empty()
                                   ^^^^^^^
  ```

- Warning: `subworkflows/local/bed_consensus_quantify_qc_bedtools_featurecounts_deseq2.nf:110:34`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_deseq2_qc_rdata         = Channel.empty()
                                   ^^^^^^^
  ```

- Warning: `subworkflows/local/bed_consensus_quantify_qc_bedtools_featurecounts_deseq2.nf:111:34`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_deseq2_qc_rds           = Channel.empty()
                                   ^^^^^^^
  ```

- Warning: `subworkflows/local/bed_consensus_quantify_qc_bedtools_featurecounts_deseq2.nf:112:34`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_deseq2_qc_pca_txt       = Channel.empty()
                                   ^^^^^^^
  ```

- Warning: `subworkflows/local/bed_consensus_quantify_qc_bedtools_featurecounts_deseq2.nf:113:34`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_deseq2_qc_pca_multiqc   = Channel.empty()
                                   ^^^^^^^
  ```

- Warning: `subworkflows/local/bed_consensus_quantify_qc_bedtools_featurecounts_deseq2.nf:114:34`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_deseq2_qc_dists_txt     = Channel.empty()
                                   ^^^^^^^
  ```

- Warning: `subworkflows/local/bed_consensus_quantify_qc_bedtools_featurecounts_deseq2.nf:115:34`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_deseq2_qc_dists_multiqc = Channel.empty()
                                   ^^^^^^^
  ```

- Warning: `subworkflows/local/bed_consensus_quantify_qc_bedtools_featurecounts_deseq2.nf:116:34`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_deseq2_qc_log           = Channel.empty()
                                   ^^^^^^^
  ```

- Warning: `subworkflows/local/bed_consensus_quantify_qc_bedtools_featurecounts_deseq2.nf:117:34`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_deseq2_qc_size_factors  = Channel.empty()
                                   ^^^^^^^
  ```

- Warning: `subworkflows/local/input_check.nf:16:37`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          .map { create_fastq_channel(it, seq_center) }
                                      ^^
  ```

- Warning: `subworkflows/local/prepare_genome.nf:47:19`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_versions = Channel.empty()
                    ^^^^^^^
  ```

- Warning: `subworkflows/local/prepare_genome.nf:52:16`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_fasta = Channel.empty()
                 ^^^^^^^
  ```

- Warning: `subworkflows/local/prepare_genome.nf:54:63`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          ch_fasta    = GUNZIP_FASTA([[:], fasta]).gunzip.map { it[1] }
                                                                ^^
  ```

- Warning: `subworkflows/local/prepare_genome.nf:58:20`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
          ch_fasta = Channel.value(file(fasta, checkIfExists: true))
                     ^^^^^^^
  ```

- Warning: `subworkflows/local/prepare_genome.nf:66:63`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
              ch_gtf      = GUNZIP_GTF([[:], gtf]).gunzip.map { it[1] }
                                                                ^^
  ```

- Warning: `subworkflows/local/prepare_genome.nf:69:22`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
              ch_gtf = Channel.value(file(gtf, checkIfExists: true))
                       ^^^^^^^
  ```

- Warning: `subworkflows/local/prepare_genome.nf:73:90`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
              ch_gff      = GUNZIP_GFF([[:], file(gff, checkIfExists: true)]).gunzip.map { it[1] }
                                                                                           ^^
  ```

- Warning: `subworkflows/local/prepare_genome.nf:76:22`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
              ch_gff = Channel.value(file(gff, checkIfExists: true)).map { [ [:], it ] }
                       ^^^^^^^
  ```

- Warning: `subworkflows/local/prepare_genome.nf:76:81`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
              ch_gff = Channel.value(file(gff, checkIfExists: true)).map { [ [:], it ] }
                                                                                  ^^
  ```

- Warning: `subworkflows/local/prepare_genome.nf:79:53`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          ch_gtf      = GFFREAD(ch_gff, []).gtf.map { it[1] }
                                                      ^^
  ```

- Warning: `subworkflows/local/prepare_genome.nf:86:20`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_blacklist = Channel.empty()
                     ^^^^^^^
  ```

- Warning: `subworkflows/local/prepare_genome.nf:89:76`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
              ch_blacklist = GUNZIP_BLACKLIST([[:], blacklist]).gunzip.map { it[1] }
                                                                             ^^
  ```

- Warning: `subworkflows/local/prepare_genome.nf:92:28`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
              ch_blacklist = Channel.value(file(blacklist))
                             ^^^^^^^
  ```

- Warning: `subworkflows/local/prepare_genome.nf:116:73`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
              ch_gene_bed = GUNZIP_GENE_BED([[:], gene_bed]).gunzip.map { it[1] }
                                                                          ^^
  ```

- Warning: `subworkflows/local/prepare_genome.nf:119:27`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
              ch_gene_bed = Channel.value(file(gene_bed))
                            ^^^^^^^
  ```

- Warning: `subworkflows/local/prepare_genome.nf:126:47`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
      CUSTOM_GETCHROMSIZES(ch_fasta.map { [[:], it] })
                                                ^^
  ```

- Warning: `subworkflows/local/prepare_genome.nf:127:59`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
      ch_chrom_sizes = CUSTOM_GETCHROMSIZES.out.sizes.map { it[1] }
                                                            ^^
  ```

- Warning: `subworkflows/local/prepare_genome.nf:128:57`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
      ch_fai         = CUSTOM_GETCHROMSIZES.out.fai.map { it[1] }
                                                          ^^
  ```

- Warning: `subworkflows/local/prepare_genome.nf:134:30`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_genome_filtered_bed = Channel.empty()
                               ^^^^^^^
  ```

- Warning: `subworkflows/local/prepare_genome.nf:146:20`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_bwa_index = Channel.empty()
                     ^^^^^^^
  ```

- Warning: `subworkflows/local/prepare_genome.nf:156:59`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
              ch_bwa_index = BWA_INDEX(ch_fasta.map { [[:], it] }).index
                                                            ^^
  ```

- Warning: `subworkflows/local/prepare_genome.nf:164:24`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_bowtie2_index = Channel.empty()
                         ^^^^^^^
  ```

- Warning: `subworkflows/local/prepare_genome.nf:174:67`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
              ch_bowtie2_index = BOWTIE2_BUILD(ch_fasta.map { [[:], it] }).index
                                                                    ^^
  ```

- Warning: `subworkflows/local/prepare_genome.nf:182:24`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_chromap_index = Channel.empty()
                         ^^^^^^^
  ```

- Warning: `subworkflows/local/prepare_genome.nf:192:67`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
              ch_chromap_index = CHROMAP_INDEX(ch_fasta.map { [[:], it] }).index
                                                                    ^^
  ```

- Warning: `subworkflows/local/prepare_genome.nf:200:21`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_star_index = Channel.empty()
                      ^^^^^^^
  ```

- Warning: `subworkflows/local/prepare_genome.nf:204:81`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
                  ch_star_index = UNTAR_STAR_INDEX([[:], star_index]).untar.map { it[1] }
                                                                                  ^^
  ```

- Warning: `subworkflows/local/prepare_genome.nf:207:33`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
                  ch_star_index = Channel.value(file(star_index))
                                  ^^^^^^^
  ```

- Warning: `subworkflows/local/utils_nfcore_chipseq_pipeline/main.nf:32:5`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
      monochrome_logs   // boolean: Do not use coloured log outputs
      ^^^^^^^^^^^^^^^
  ```

- Warning: `subworkflows/local/utils_nfcore_chipseq_pipeline/main.nf:104:22`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_samplesheet = Channel.fromList(samplesheetToList(input, "assets/schema_input.json"))
                       ^^^^^^^
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

- Warning: `workflows/chipseq.nf:65:1`: Variable was declared but not used

  ```nextflow
  ch_bamtools_filter_se_config = file(params.bamtools_filter_se_config)
  ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  ```

- Warning: `workflows/chipseq.nf:66:1`: Variable was declared but not used

  ```nextflow
  ch_bamtools_filter_pe_config = file(params.bamtools_filter_pe_config)
  ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  ```

- Warning: `workflows/chipseq.nf:69:1`: Variable was declared but not used

  ```nextflow
  ch_spp_nsc_header           = file("$projectDir/assets/multiqc/spp_nsc_header.txt", checkIfExists: true)
  ^^^^^^^^^^^^^^^^^
  ```

- Warning: `workflows/chipseq.nf:70:1`: Variable was declared but not used

  ```nextflow
  ch_spp_rsc_header           = file("$projectDir/assets/multiqc/spp_rsc_header.txt", checkIfExists: true)
  ^^^^^^^^^^^^^^^^^
  ```

- Warning: `workflows/chipseq.nf:71:1`: Variable was declared but not used

  ```nextflow
  ch_spp_correlation_header   = file("$projectDir/assets/multiqc/spp_correlation_header.txt", checkIfExists: true)
  ^^^^^^^^^^^^^^^^^^^^^^^^^
  ```

- Warning: `workflows/chipseq.nf:72:1`: Variable was declared but not used

  ```nextflow
  ch_peak_count_header        = file("$projectDir/assets/multiqc/peak_count_header.txt", checkIfExists: true)
  ^^^^^^^^^^^^^^^^^^^^
  ```

- Warning: `workflows/chipseq.nf:73:1`: Variable was declared but not used

  ```nextflow
  ch_frip_score_header        = file("$projectDir/assets/multiqc/frip_score_header.txt", checkIfExists: true)
  ^^^^^^^^^^^^^^^^^^^^
  ```

- Warning: `workflows/chipseq.nf:74:1`: Variable was declared but not used

  ```nextflow
  ch_peak_annotation_header   = file("$projectDir/assets/multiqc/peak_annotation_header.txt", checkIfExists: true)
  ^^^^^^^^^^^^^^^^^^^^^^^^^
  ```

- Warning: `workflows/chipseq.nf:75:1`: Variable was declared but not used

  ```nextflow
  ch_deseq2_pca_header        = Channel.value(file("$projectDir/assets/multiqc/deseq2_pca_header.txt", checkIfExists: true))
  ^^^^^^^^^^^^^^^^^^^^
  ```

- Warning: `workflows/chipseq.nf:75:31`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
  ch_deseq2_pca_header        = Channel.value(file("$projectDir/assets/multiqc/deseq2_pca_header.txt", checkIfExists: true))
                                ^^^^^^^
  ```

- Warning: `workflows/chipseq.nf:76:1`: Variable was declared but not used

  ```nextflow
  ch_deseq2_clustering_header = Channel.value(file("$projectDir/assets/multiqc/deseq2_clustering_header.txt", checkIfExists: true))
  ^^^^^^^^^^^^^^^^^^^^^^^^^^^
  ```

- Warning: `workflows/chipseq.nf:76:31`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
  ch_deseq2_clustering_header = Channel.value(file("$projectDir/assets/multiqc/deseq2_clustering_header.txt", checkIfExists: true))
                                ^^^^^^^
  ```

- Warning: `workflows/chipseq.nf:136:28`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_genome_bam        = Channel.empty()
                             ^^^^^^^
  ```

- Warning: `workflows/chipseq.nf:137:28`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_genome_bam_index  = Channel.empty()
                             ^^^^^^^
  ```

- Warning: `workflows/chipseq.nf:138:28`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_samtools_stats    = Channel.empty()
                             ^^^^^^^
  ```

- Warning: `workflows/chipseq.nf:139:28`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_samtools_flagstat = Channel.empty()
                             ^^^^^^^
  ```

- Warning: `workflows/chipseq.nf:140:28`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_samtools_idxstats = Channel.empty()
                             ^^^^^^^
  ```

- Warning: `workflows/chipseq.nf:148:28`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
                      [ [:], it ]
                             ^^
  ```

- Warning: `workflows/chipseq.nf:170:28`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
                      [ [:], it ]
                             ^^
  ```

- Warning: `workflows/chipseq.nf:190:28`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
                      [ [:], it ]
                             ^^
  ```

- Warning: `workflows/chipseq.nf:214:32`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
                          [ [:], it ]
                                 ^^
  ```

- Warning: `workflows/chipseq.nf:220:9`: Variable was declared but not used

  ```nextflow
          ch_transcriptome_bam = ALIGN_STAR.out.bam_transcript
          ^^^^^^^^^^^^^^^^^^^^
  ```

- Warning: `workflows/chipseq.nf:224:9`: Variable was declared but not used

  ```nextflow
          ch_star_multiqc      = ALIGN_STAR.out.log_final
          ^^^^^^^^^^^^^^^
  ```

- Warning: `workflows/chipseq.nf:259:24`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
                  [ [:], it ]
                         ^^
  ```

- Warning: `workflows/chipseq.nf:263:24`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
                  [ [:], it ]
                         ^^
  ```

- Warning: `workflows/chipseq.nf:276:24`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
                  [ [:], it ]
                         ^^
  ```

- Warning: `workflows/chipseq.nf:286:25`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_preseq_multiqc = Channel.empty()
                          ^^^^^^^
  ```

- Warning: `workflows/chipseq.nf:298:47`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_picardcollectmultiplemetrics_multiqc = Channel.empty()
                                                ^^^^^^^
  ```

- Warning: `workflows/chipseq.nf:305:23`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
                      [ it[0], it[1], [] ]
                        ^^
  ```

- Warning: `workflows/chipseq.nf:305:30`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
                      [ it[0], it[1], [] ]
                               ^^
  ```

- Warning: `workflows/chipseq.nf:309:28`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
                      [ [:], it ]
                             ^^
  ```

- Warning: `workflows/chipseq.nf:313:28`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
                      [ [:], it ]
                             ^^
  ```

- Warning: `workflows/chipseq.nf:323:59`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_phantompeakqualtools_spp_multiqc                 = Channel.empty()
                                                            ^^^^^^^
  ```

- Warning: `workflows/chipseq.nf:324:59`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_multiqc_phantompeakqualtools_nsc_multiqc         = Channel.empty()
                                                            ^^^^^^^
  ```

- Warning: `workflows/chipseq.nf:325:59`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_multiqc_phantompeakqualtools_rsc_multiqc         = Channel.empty()
                                                            ^^^^^^^
  ```

- Warning: `workflows/chipseq.nf:326:59`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_multiqc_phantompeakqualtools_correlation_multiqc = Channel.empty()
                                                            ^^^^^^^
  ```

- Warning: `workflows/chipseq.nf:358:39`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_deeptoolsplotprofile_multiqc = Channel.empty()
                                        ^^^^^^^
  ```

- Warning: `workflows/chipseq.nf:415:43`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_deeptoolsplotfingerprint_multiqc = Channel.empty()
                                            ^^^^^^^
  ```

- Warning: `workflows/chipseq.nf:427:41`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_macs_gsize                     = Channel.empty()
                                          ^^^^^^^
  ```

- Warning: `workflows/chipseq.nf:428:41`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_subreadfeaturecounts_multiqc   = Channel.empty()
                                          ^^^^^^^
  ```

- Warning: `workflows/chipseq.nf:435:59`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          ch_macs_gsize = KHMER_UNIQUEKMERS.out.kmers.map { it.text.trim() }
                                                            ^^
  ```

- Warning: `workflows/chipseq.nf:441:25`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
              meta, bams, bais ->
                          ^^^^
  ```

- Warning: `workflows/chipseq.nf:467:36`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_macs3_consensus_bed_lib   = Channel.empty()
                                     ^^^^^^^
  ```

- Warning: `workflows/chipseq.nf:468:36`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_macs3_consensus_txt_lib   = Channel.empty()
                                     ^^^^^^^
  ```

- Warning: `workflows/chipseq.nf:469:36`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_deseq2_pca_multiqc        = Channel.empty()
                                     ^^^^^^^
  ```

- Warning: `workflows/chipseq.nf:470:36`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_deseq2_clustering_multiqc = Channel.empty()
                                     ^^^^^^^
  ```

- Warning: `workflows/chipseq.nf:475:31`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
                  meta, ip_bam, control_bam ->
                                ^^^^^^^^^^^
  ```

- Warning: `workflows/chipseq.nf:513:66`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
              BAM_BEDGRAPH_BIGWIG_BEDTOOLS_UCSC.out.bigwig.collect{it[1]}.ifEmpty([]),
                                                                   ^^
  ```

- Warning: `workflows/chipseq.nf:514:70`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
              BAM_PEAKS_CALL_QC_ANNOTATE_MACS3_HOMER.out.peaks.collect{it[1]}.ifEmpty([]),
                                                                       ^^
  ```

- Warning: `workflows/chipseq.nf:515:48`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
              ch_macs3_consensus_bed_lib.collect{it[1]}.ifEmpty([]),
                                                 ^^
  ```

- Warning: `workflows/chipseq.nf:516:48`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
              ch_macs3_consensus_txt_lib.collect{it[1]}.ifEmpty([])
                                                 ^^
  ```

- Warning: `workflows/chipseq.nf:524:26`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      def topic_versions = Channel.topic("versions")
                           ^^^^^^^
  ```

- Warning: `workflows/chipseq.nf:553:25`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_multiqc_report = Channel.empty()
                          ^^^^^^^
  ```

- Warning: `workflows/chipseq.nf:556:36`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
          ch_multiqc_config        = Channel.fromPath("$projectDir/assets/multiqc_config.yml", checkIfExists: true)
                                     ^^^^^^^
  ```

- Warning: `workflows/chipseq.nf:557:60`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
          ch_multiqc_custom_config = params.multiqc_config ? Channel.fromPath( params.multiqc_config ): Channel.empty()
                                                             ^^^^^^^
  ```

- Warning: `workflows/chipseq.nf:557:103`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
          ch_multiqc_custom_config = params.multiqc_config ? Channel.fromPath( params.multiqc_config ): Channel.empty()
                                                                                                        ^^^^^^^
  ```

- Warning: `workflows/chipseq.nf:558:60`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
          ch_multiqc_logo          = params.multiqc_logo   ? Channel.fromPath( params.multiqc_logo )  : Channel.empty()
                                                             ^^^^^^^
  ```

- Warning: `workflows/chipseq.nf:558:103`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
          ch_multiqc_logo          = params.multiqc_logo   ? Channel.fromPath( params.multiqc_logo )  : Channel.empty()
                                                                                                        ^^^^^^^
  ```

- Warning: `workflows/chipseq.nf:560:36`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
          ch_workflow_summary      = Channel.value(paramsSummaryMultiqc(summary_params))
                                     ^^^^^^^
  ```

- Warning: `workflows/chipseq.nf:570:69`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
              FASTQ_FASTQC_UMITOOLS_TRIMGALORE.out.fastqc_zip.collect{it[1]}.ifEmpty([]),
                                                                      ^^
  ```

- Warning: `workflows/chipseq.nf:571:67`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
              FASTQ_FASTQC_UMITOOLS_TRIMGALORE.out.trim_zip.collect{it[1]}.ifEmpty([]),
                                                                    ^^
  ```

- Warning: `workflows/chipseq.nf:572:67`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
              FASTQ_FASTQC_UMITOOLS_TRIMGALORE.out.trim_log.collect{it[1]}.ifEmpty([]),
                                                                    ^^
  ```

- Warning: `workflows/chipseq.nf:574:39`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
              ch_samtools_stats.collect{it[1]}.ifEmpty([]),
                                        ^^
  ```

- Warning: `workflows/chipseq.nf:575:42`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
              ch_samtools_flagstat.collect{it[1]}.ifEmpty([]),
                                           ^^
  ```

- Warning: `workflows/chipseq.nf:576:42`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
              ch_samtools_idxstats.collect{it[1]}.ifEmpty([]),
                                           ^^
  ```

- Warning: `workflows/chipseq.nf:578:57`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
              BAM_MARKDUPLICATES_PICARD.out.stats.collect{it[1]}.ifEmpty([]),
                                                          ^^
  ```

- Warning: `workflows/chipseq.nf:579:60`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
              BAM_MARKDUPLICATES_PICARD.out.flagstat.collect{it[1]}.ifEmpty([]),
                                                             ^^
  ```

- Warning: `workflows/chipseq.nf:580:60`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
              BAM_MARKDUPLICATES_PICARD.out.idxstats.collect{it[1]}.ifEmpty([]),
                                                             ^^
  ```

- Warning: `workflows/chipseq.nf:581:59`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
              BAM_MARKDUPLICATES_PICARD.out.metrics.collect{it[1]}.ifEmpty([]),
                                                            ^^
  ```

- Warning: `workflows/chipseq.nf:583:51`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
              BAM_FILTER_BAMTOOLS.out.stats.collect{it[1]}.ifEmpty([]),
                                                    ^^
  ```

- Warning: `workflows/chipseq.nf:584:54`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
              BAM_FILTER_BAMTOOLS.out.flagstat.collect{it[1]}.ifEmpty([]),
                                                       ^^
  ```

- Warning: `workflows/chipseq.nf:585:54`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
              BAM_FILTER_BAMTOOLS.out.idxstats.collect{it[1]}.ifEmpty([]),
                                                       ^^
  ```

- Warning: `workflows/chipseq.nf:586:61`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
              ch_picardcollectmultiplemetrics_multiqc.collect{it[1]}.ifEmpty([]),
                                                              ^^
  ```

- Warning: `workflows/chipseq.nf:588:39`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
              ch_preseq_multiqc.collect{it[1]}.ifEmpty([]),
                                        ^^
  ```

- Warning: `workflows/chipseq.nf:590:53`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
              ch_deeptoolsplotprofile_multiqc.collect{it[1]}.ifEmpty([]),
                                                      ^^
  ```

- Warning: `workflows/chipseq.nf:591:57`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
              ch_deeptoolsplotfingerprint_multiqc.collect{it[1]}.ifEmpty([]),
                                                          ^^
  ```

- Warning: `workflows/chipseq.nf:593:57`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
              ch_phantompeakqualtools_spp_multiqc.collect{it[1]}.ifEmpty([]),
                                                          ^^
  ```

- Warning: `workflows/chipseq.nf:594:65`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
              ch_multiqc_phantompeakqualtools_nsc_multiqc.collect{it[1]}.ifEmpty([]),
                                                                  ^^
  ```

- Warning: `workflows/chipseq.nf:595:65`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
              ch_multiqc_phantompeakqualtools_rsc_multiqc.collect{it[1]}.ifEmpty([]),
                                                                  ^^
  ```

- Warning: `workflows/chipseq.nf:596:73`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
              ch_multiqc_phantompeakqualtools_correlation_multiqc.collect{it[1]}.ifEmpty([]),
                                                                          ^^
  ```

- Warning: `workflows/chipseq.nf:598:77`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
              BAM_PEAKS_CALL_QC_ANNOTATE_MACS3_HOMER.out.frip_multiqc.collect{it[1]}.ifEmpty([]),
                                                                              ^^
  ```

- Warning: `workflows/chipseq.nf:599:83`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
              BAM_PEAKS_CALL_QC_ANNOTATE_MACS3_HOMER.out.peak_count_multiqc.collect{it[1]}.ifEmpty([]),
                                                                                    ^^
  ```

- Warning: `workflows/chipseq.nf:601:53`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
              ch_subreadfeaturecounts_multiqc.collect{it[1]}.ifEmpty([]),
                                                      ^^
  ```
