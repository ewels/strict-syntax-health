# Nextflow lint results

- Generated: 2026-01-16T06:39:27.126020047Z
- Nextflow version: 25.12.0-edge
- Summary: 89 errors, 284 warnings

## :x: Errors

- Error: `modules/local/multiqc_custom_biotype/nextflow.config:1:1`: If statements cannot be mixed with config statements

  ```nextflow
  if (!params.skip_qc) {
  ^
  ```

- Error: `modules/local/star_align_igenomes/main.nf:43:9`: `seq_platform` is already declared

  ```nextflow
      def seq_platform    = seq_platform ? "'PL:$seq_platform'" : ""
          ^^^^^^^^^^^^
  ```

- Error: `modules/local/star_align_igenomes/main.nf:44:9`: `seq_center` is already declared

  ```nextflow
      def seq_center      = seq_center ? "--outSAMattrRGline ID:$prefix 'CN:$seq_center' 'SM:$prefix' $seq_platform " : "--outSAMattrRGline ID:$prefix 'SM:$prefix' $seq_platform "
          ^^^^^^^^^^
  ```

- Error: `modules/nf-core/bbmap/bbsplit/main.nf:41:43`: `index` is already declared

  ```nextflow
      other_ref_names.eachWithIndex { name, index ->
                                            ^^^^^
  ```

- Error: `modules/nf-core/bbmap/bbsplit/main.nf:116:43`: `index` is already declared

  ```nextflow
      other_ref_names.eachWithIndex { name, index ->
                                            ^^^^^
  ```

- Error: `modules/nf-core/bbmap/bbsplit/nextflow.config:1:1`: If statements cannot be mixed with config statements

  ```nextflow
  if (!params.skip_bbsplit) {
  ^
  ```

- Error: `modules/nf-core/bracken/bracken/nextflow.config:1:1`: If statements cannot be mixed with config statements

  ```nextflow
  if (!params.skip_qc) {
  ^
  ```

- Error: `modules/nf-core/dupradar/nextflow.config:1:1`: If statements cannot be mixed with config statements

  ```nextflow
  if (!params.skip_qc) {
  ^
  ```

- Error: `modules/nf-core/kraken2/kraken2/nextflow.config:1:1`: If statements cannot be mixed with config statements

  ```nextflow
  if (!params.skip_qc) {
  ^
  ```

- Error: `modules/nf-core/multiqc/nextflow.config:1:1`: If statements cannot be mixed with config statements

  ```nextflow
  if (!params.skip_multiqc) {
  ^
  ```

- Error: `modules/nf-core/preseq/lcextrap/nextflow.config:1:1`: If statements cannot be mixed with config statements

  ```nextflow
  if (!params.skip_qc) {
  ^
  ```

- Error: `modules/nf-core/qualimap/rnaseq/nextflow.config:1:1`: If statements cannot be mixed with config statements

  ```nextflow
  if (!params.skip_qc) {
  ^
  ```

- Error: `modules/nf-core/sentieon/rsemcalculateexpression/tests/nextflow.config:17:25`: `SENTIEON_LICSRVR_IP` is not defined (hint: use `env('...')` to access environment variable)

  ```nextflow
      SENTIEON_LICENSE = "$SENTIEON_LICSRVR_IP"
                          ^^^^^^^^^^^^^^^^^^^^
  ```

- Error: `modules/nf-core/sentieon/rsemcalculateexpression/tests/nextflow.config:19:27`: `SENTIEON_AUTH_MECH` is not defined (hint: use `env('...')` to access environment variable)

  ```nextflow
      SENTIEON_AUTH_MECH = "$SENTIEON_AUTH_MECH"
                            ^^^^^^^^^^^^^^^^^^^
  ```

- Error: `modules/nf-core/sentieon/rsempreparereference/tests/nextflow.config:3:25`: `SENTIEON_LICSRVR_IP` is not defined (hint: use `env('...')` to access environment variable)

  ```nextflow
      SENTIEON_LICENSE = "$SENTIEON_LICSRVR_IP"
                          ^^^^^^^^^^^^^^^^^^^^
  ```

- Error: `modules/nf-core/sentieon/rsempreparereference/tests/nextflow.config:5:27`: `SENTIEON_AUTH_MECH` is not defined (hint: use `env('...')` to access environment variable)

  ```nextflow
      SENTIEON_AUTH_MECH = "$SENTIEON_AUTH_MECH"
                            ^^^^^^^^^^^^^^^^^^^
  ```

- Error: `modules/nf-core/sentieon/staralign/tests/nextflow.arriba.config:15:25`: `SENTIEON_LICSRVR_IP` is not defined (hint: use `env('...')` to access environment variable)

  ```nextflow
      SENTIEON_LICENSE = "$SENTIEON_LICSRVR_IP"
                          ^^^^^^^^^^^^^^^^^^^^
  ```

- Error: `modules/nf-core/sentieon/staralign/tests/nextflow.arriba.config:17:27`: `SENTIEON_AUTH_MECH` is not defined (hint: use `env('...')` to access environment variable)

  ```nextflow
      SENTIEON_AUTH_MECH = "$SENTIEON_AUTH_MECH"
                            ^^^^^^^^^^^^^^^^^^^
  ```

- Error: `modules/nf-core/sentieon/staralign/tests/nextflow.config:15:25`: `SENTIEON_LICSRVR_IP` is not defined (hint: use `env('...')` to access environment variable)

  ```nextflow
      SENTIEON_LICENSE = "$SENTIEON_LICSRVR_IP"
                          ^^^^^^^^^^^^^^^^^^^^
  ```

- Error: `modules/nf-core/sentieon/staralign/tests/nextflow.config:17:27`: `SENTIEON_AUTH_MECH` is not defined (hint: use `env('...')` to access environment variable)

  ```nextflow
      SENTIEON_AUTH_MECH = "$SENTIEON_AUTH_MECH"
                            ^^^^^^^^^^^^^^^^^^^
  ```

- Error: `modules/nf-core/sentieon/staralign/tests/nextflow.starfusion.config:15:25`: `SENTIEON_LICSRVR_IP` is not defined (hint: use `env('...')` to access environment variable)

  ```nextflow
      SENTIEON_LICENSE = "$SENTIEON_LICSRVR_IP"
                          ^^^^^^^^^^^^^^^^^^^^
  ```

- Error: `modules/nf-core/sentieon/staralign/tests/nextflow.starfusion.config:17:27`: `SENTIEON_AUTH_MECH` is not defined (hint: use `env('...')` to access environment variable)

  ```nextflow
      SENTIEON_AUTH_MECH = "$SENTIEON_AUTH_MECH"
                            ^^^^^^^^^^^^^^^^^^^
  ```

- Error: `modules/nf-core/sortmerna/nextflow.config:1:1`: If statements cannot be mixed with config statements

  ```nextflow
  if (params.remove_ribo_rna) {
  ^
  ```

- Error: `modules/nf-core/stringtie/stringtie/nextflow.config:1:1`: If statements cannot be mixed with config statements

  ```nextflow
  if (!params.skip_stringtie) {
  ^
  ```

- Error: `modules/nf-core/subread/featurecounts/nextflow.config:1:1`: If statements cannot be mixed with config statements

  ```nextflow
  if (!params.skip_qc) {
  ^
  ```

- Error: `modules/nf-core/sylph/profile/nextflow.config:1:1`: If statements cannot be mixed with config statements

  ```nextflow
  if (!params.skip_qc) {
  ^
  ```

- Error: `modules/nf-core/sylphtax/taxprof/nextflow.config:1:1`: If statements cannot be mixed with config statements

  ```nextflow
  if (!params.skip_qc) {
  ^
  ```

- Error: `subworkflows/local/align_star/nextflow.config:1:26`: Unexpected input: '('

  ```nextflow
  def generateStarAlignArgs(save_unaligned, contaminant_screening, extra_star_align_args, quantifier = 'salmon') {
                           ^
  ```

- Error: `subworkflows/local/align_star/tests/nextflow.config:15:1`: If statements cannot be mixed with config statements

  ```nextflow
  if (System.getenv('SENTIEON_LICSRVR_IP')) {
  ^
  ```

- Error: `subworkflows/local/align_star/tests/nextflow.config:19:1`: If statements cannot be mixed with config statements

  ```nextflow
  if (System.getenv('SENTIEON_AUTH_MECH')) {
  ^
  ```

- Error: `subworkflows/local/align_star/tests/nextflow.config:22:1`: If statements cannot be mixed with config statements

  ```nextflow
  if (secrets.SENTIEON_AUTH_DATA) {
  ^
  ```

- Error: `subworkflows/local/prepare_genome/main.nf:141:44`: `fasta` is already declared

  ```nextflow
              ch_fasta.combine(ch_gtf).map { fasta, gtf -> [ [:], fasta, gtf ] },
                                             ^^^^^
  ```

- Error: `subworkflows/local/prepare_genome/main.nf:141:51`: `gtf` is already declared

  ```nextflow
              ch_fasta.combine(ch_gtf).map { fasta, gtf -> [ [:], fasta, gtf ] },
                                                    ^^^
  ```

- Error: `subworkflows/local/prepare_genome/nextflow.config:103:1`: If statements cannot be mixed with config statements

  ```nextflow
  if (!params.skip_bbsplit && params.bbsplit_fasta_list) {
  ^
  ```

- Error: `subworkflows/local/prepare_genome/nextflow.config:116:1`: If statements cannot be mixed with config statements

  ```nextflow
  if (params.remove_ribo_rna && params.ribo_removal_tool == 'sortmerna' && params.ribo_database_manifest) {
  ^
  ```

- Error: `subworkflows/local/prepare_genome/tests/nextflow.config:27:1`: If statements cannot be mixed with config statements

  ```nextflow
  if (System.getenv('SENTIEON_LICSRVR_IP')) {
  ^
  ```

- Error: `subworkflows/local/prepare_genome/tests/nextflow.config:31:1`: If statements cannot be mixed with config statements

  ```nextflow
  if (System.getenv('SENTIEON_AUTH_MECH')) {
  ^
  ```

- Error: `subworkflows/local/prepare_genome/tests/nextflow.config:34:1`: If statements cannot be mixed with config statements

  ```nextflow
  if (secrets.SENTIEON_AUTH_DATA) {
  ^
  ```

- Error: `subworkflows/local/quantify_rsem/nextflow.config:1:1`: If statements cannot be mixed with config statements

  ```nextflow
  if (!params.skip_alignment && params.aligner == 'star_rsem') {
  ^
  ```

- Error: `subworkflows/local/quantify_rsem/tests/nextflow.config:2:1`: If statements cannot be mixed with config statements

  ```nextflow
  if (System.getenv('SENTIEON_LICSRVR_IP')) {
  ^
  ```

- Error: `subworkflows/local/quantify_rsem/tests/nextflow.config:6:1`: If statements cannot be mixed with config statements

  ```nextflow
  if (System.getenv('SENTIEON_AUTH_MECH')) {
  ^
  ```

- Error: `subworkflows/local/quantify_rsem/tests/nextflow.config:9:1`: If statements cannot be mixed with config statements

  ```nextflow
  if (secrets.SENTIEON_AUTH_DATA) {
  ^
  ```

- Error: `subworkflows/nf-core/bam_markduplicates_picard/nextflow.config:1:1`: If statements cannot be mixed with config statements

  ```nextflow
  if (!params.skip_markduplicates && !params.with_umi) {
  ^
  ```

- Error: `subworkflows/nf-core/bam_rseqc/nextflow.config:1:1`: Variable declarations cannot be mixed with config statements

  ```nextflow
  def rseqc_modules = params.rseqc_modules ? params.rseqc_modules.split(',').collect{ it.trim().toLowerCase() } : []
  ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  ```

- Error: `subworkflows/nf-core/bam_rseqc/nextflow.config:3:1`: If statements cannot be mixed with config statements

  ```nextflow
  if (!params.skip_qc && !params.skip_rseqc) {
  ^
  ```

- Error: `subworkflows/nf-core/fastq_align_hisat2/nextflow.config:1:1`: If statements cannot be mixed with config statements

  ```nextflow
  if (!params.skip_alignment && params.aligner == 'hisat2') {
  ^
  ```

- Error: `subworkflows/nf-core/fastq_fastqc_umitools_fastp/nextflow.config:1:1`: If statements cannot be mixed with config statements

  ```nextflow
  if (!(params.skip_fastqc || params.skip_qc)) {
  ^
  ```

- Error: `subworkflows/nf-core/fastq_fastqc_umitools_fastp/nextflow.config:27:1`: If statements cannot be mixed with config statements

  ```nextflow
  if (!params.skip_trimming) {
  ^
  ```

- Error: `subworkflows/nf-core/fastq_fastqc_umitools_fastp/nextflow.config:55:1`: If statements cannot be mixed with config statements

  ```nextflow
  if (params.with_umi && !params.skip_umi_extract) {
  ^
  ```

- Error: `subworkflows/nf-core/fastq_fastqc_umitools_trimgalore/main.nf:59:30`: `reads` is already declared

  ```nextflow
                  .map { meta, reads ->
                               ^^^^^
  ```

- Error: `subworkflows/nf-core/fastq_fastqc_umitools_trimgalore/nextflow.config:1:1`: If statements cannot be mixed with config statements

  ```nextflow
  if (!(params.skip_fastqc || params.skip_qc)) {
  ^
  ```

- Error: `subworkflows/nf-core/fastq_fastqc_umitools_trimgalore/nextflow.config:17:1`: If statements cannot be mixed with config statements

  ```nextflow
  if (!params.skip_trimming) {
  ^
  ```

- Error: `subworkflows/nf-core/fastq_fastqc_umitools_trimgalore/nextflow.config:65:1`: If statements cannot be mixed with config statements

  ```nextflow
  if (params.with_umi && !params.skip_umi_extract) {
  ^
  ```

- Error: `subworkflows/nf-core/fastq_qc_trim_filter_setstrandedness/nextflow.config:42:1`: If statements cannot be mixed with config statements

  ```nextflow
  if (params.remove_ribo_rna && params.ribo_removal_tool in ['sortmerna', 'bowtie2']) {
  ^
  ```

- Error: `subworkflows/nf-core/fastq_qc_trim_filter_setstrandedness/nextflow.config:60:1`: If statements cannot be mixed with config statements

  ```nextflow
  if (params.remove_ribo_rna && params.ribo_removal_tool == 'ribodetector') {
  ^
  ```

- Error: `subworkflows/nf-core/fastq_qc_trim_filter_setstrandedness/nextflow.config:96:1`: If statements cannot be mixed with config statements

  ```nextflow
  if (params.remove_ribo_rna && params.ribo_removal_tool == 'bowtie2') {
  ^
  ```

- Error: `subworkflows/nf-core/quantify_pseudo_alignment/nextflow.config:1:1`: If statements cannot be mixed with config statements

  ```nextflow
  if (!params.skip_pseudo_alignment && params.pseudo_aligner == 'salmon') {
  ^
  ```

- Error: `subworkflows/nf-core/quantify_pseudo_alignment/nextflow.config:14:1`: If statements cannot be mixed with config statements

  ```nextflow
  if (!params.skip_pseudo_alignment && params.pseudo_aligner == 'kallisto') {
  ^
  ```

- Error: `subworkflows/nf-core/quantify_pseudo_alignment/nextflow.config:27:1`: If statements cannot be mixed with config statements

  ```nextflow
  if (!params.skip_pseudo_alignment && params.pseudo_aligner) {
  ^
  ```

- Error: `tests/nextflow.config:36:1`: If statements cannot be mixed with config statements

  ```nextflow
  if (System.getenv('SENTIEON_LICSRVR_IP')) {
  ^
  ```

- Error: `tests/nextflow.config:40:1`: If statements cannot be mixed with config statements

  ```nextflow
  if (System.getenv('SENTIEON_AUTH_MECH')) {
  ^
  ```

- Error: `tests/nextflow.config:43:1`: If statements cannot be mixed with config statements

  ```nextflow
  if (secrets.SENTIEON_AUTH_DATA) {
  ^
  ```

- Error: `workflows/rnaseq/main.nf:77:1`: Statements cannot be mixed with script declarations -- move statements into a process, workflow, or function

  ```nextflow
  ch_pca_header_multiqc           = file("$projectDir/workflows/rnaseq/assets/multiqc/deseq2_pca_header.txt", checkIfExists: true)
  ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  ```

- Error: `workflows/rnaseq/main.nf:78:1`: Statements cannot be mixed with script declarations -- move statements into a process, workflow, or function

  ```nextflow
  sample_status_header_multiqc    = file("$projectDir/workflows/rnaseq/assets/multiqc/sample_status_header.txt", checkIfExists: true)
  ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  ```

- Error: `workflows/rnaseq/main.nf:79:1`: Statements cannot be mixed with script declarations -- move statements into a process, workflow, or function

  ```nextflow
  ch_clustering_header_multiqc    = file("$projectDir/workflows/rnaseq/assets/multiqc/deseq2_clustering_header.txt", checkIfExists: true)
  ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  ```

- Error: `workflows/rnaseq/main.nf:80:1`: Statements cannot be mixed with script declarations -- move statements into a process, workflow, or function

  ```nextflow
  ch_biotypes_header_multiqc      = file("$projectDir/workflows/rnaseq/assets/multiqc/biotypes_header.txt", checkIfExists: true)
  ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  ```

- Error: `workflows/rnaseq/main.nf:81:1`: Statements cannot be mixed with script declarations -- move statements into a process, workflow, or function

  ```nextflow
  ch_dummy_file                   = ch_pca_header_multiqc
  ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  ```

- Error: `workflows/rnaseq/main.nf:318:17`: `ch_pca_header_multiqc` is not defined

  ```nextflow
                  ch_pca_header_multiqc,
                  ^^^^^^^^^^^^^^^^^^^^^
  ```

- Error: `workflows/rnaseq/main.nf:319:17`: `ch_clustering_header_multiqc` is not defined

  ```nextflow
                  ch_clustering_header_multiqc
                  ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  ```

- Error: `workflows/rnaseq/main.nf:334:13`: `ch_dummy_file` is not defined

  ```nextflow
              ch_dummy_file,
              ^^^^^^^^^^^^^
  ```

- Error: `workflows/rnaseq/main.nf:350:17`: `ch_pca_header_multiqc` is not defined

  ```nextflow
                  ch_pca_header_multiqc,
                  ^^^^^^^^^^^^^^^^^^^^^
  ```

- Error: `workflows/rnaseq/main.nf:351:17`: `ch_clustering_header_multiqc` is not defined

  ```nextflow
                  ch_clustering_header_multiqc
                  ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  ```

- Error: `workflows/rnaseq/main.nf:445:17`: `sample_status_header_multiqc` is not defined

  ```nextflow
                  sample_status_header_multiqc.text + multiqcTsvFromList(tsv_data, header)
                  ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  ```

- Error: `workflows/rnaseq/main.nf:529:13`: `ch_biotypes_header_multiqc` is not defined

  ```nextflow
              ch_biotypes_header_multiqc
              ^^^^^^^^^^^^^^^^^^^^^^^^^^
  ```

- Error: `workflows/rnaseq/main.nf:605:13`: `for` loops are no longer supported

  ```nextflow
              for (rseqc_module in ['read_distribution', 'inner_distance', 'tin']) {
              ^^^
  ```

- Error: `workflows/rnaseq/main.nf:605:18`: `rseqc_module` is not defined

  ```nextflow
              for (rseqc_module in ['read_distribution', 'inner_distance', 'tin']) {
                   ^^^^^^^^^^^^
  ```

- Error: `workflows/rnaseq/main.nf:606:44`: `rseqc_module` is not defined

  ```nextflow
                  if (rseqc_modules.contains(rseqc_module)) {
                                             ^^^^^^^^^^^^
  ```

- Error: `workflows/rnaseq/main.nf:607:42`: `rseqc_module` is not defined

  ```nextflow
                      rseqc_modules.remove(rseqc_module)
                                           ^^^^^^^^^^^^
  ```

- Error: `workflows/rnaseq/main.nf:631:25`: Variables in a closure should be declared with `def`

  ```nextflow
                          rseqc_strandedness = rseqc_inferred_strand.inferred_strandedness
                          ^^^^^^^^^^^^^^^^^^
  ```

- Error: `workflows/rnaseq/main.nf:636:29`: Variables in a closure should be declared with `def`

  ```nextflow
                              salmon_strandedness = meta.salmon_strand_analysis.inferred_strandedness
                              ^^^^^^^^^^^^^^^^^^^
  ```

- Error: `workflows/rnaseq/main.nf:679:25`: `sample_status_header_multiqc` is not defined

  ```nextflow
                          sample_status_header_multiqc.text + multiqcTsvFromList(tsv_data, header)
                          ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  ```

- Error: `workflows/rnaseq/main.nf:742:13`: `ch_dummy_file` is not defined

  ```nextflow
              ch_dummy_file,
              ^^^^^^^^^^^^^
  ```

- Error: `workflows/rnaseq/main.nf:759:17`: `ch_pca_header_multiqc` is not defined

  ```nextflow
                  ch_pca_header_multiqc,
                  ^^^^^^^^^^^^^^^^^^^^^
  ```

- Error: `workflows/rnaseq/main.nf:760:17`: `ch_clustering_header_multiqc` is not defined

  ```nextflow
                  ch_clustering_header_multiqc
                  ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  ```

- Error: `workflows/rnaseq/nextflow.config:30:1`: If statements cannot be mixed with config statements

  ```nextflow
  if (params.aligner == 'star_salmon') {
  ^
  ```

- Error: `workflows/rnaseq/nextflow.config:224:1`: If statements cannot be mixed with config statements

  ```nextflow
  if (params.with_umi && ['star_salmon','hisat2'].contains(params.aligner)) {
  ^
  ```

- Error: `workflows/rnaseq/nextflow.config:316:1`: If statements cannot be mixed with config statements

  ```nextflow
  if (!params.skip_bigwig) {
  ^
  ```

- Error: `workflows/rnaseq/nextflow.config:364:1`: If statements cannot be mixed with config statements

  ```nextflow
  if (params.aligner in ['star_salmon', 'star_rsem'] && !params.skip_qc && !params.skip_deseq2_qc) {
  ^
  ```

- Error: `workflows/rnaseq/nextflow.config:387:1`: If statements cannot be mixed with config statements

  ```nextflow
  if (!params.skip_pseudo_alignment && params.pseudo_aligner) {
  ^
  ```

## :warning: Warnings

- Warning: `main.nf:57:19`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_versions = Channel.empty()
                    ^^^^^^^
  ```

- Warning: `main.nf:97:39`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
              .map { checkMaxContigSize(it) }
                                        ^^
  ```

- Warning: `main.nf:103:22`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_samplesheet = Channel.value(file(params.input, checkIfExists: true))
                       ^^^^^^^
  ```

- Warning: `main.nf:107:24`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_bowtie2_index = Channel.empty()
                         ^^^^^^^
  ```

- Warning: `modules/local/star_align_igenomes/main.nf:41:56`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
      meta.single_end ? [reads].flatten().each{reads1 << it} : reads.eachWithIndex{ v, ix -> ( ix & 1 ? reads2 : reads1) << v }
                                                         ^^
  ```

- Warning: `modules/nf-core/bbmap/bbsplit/main.nf:116:43`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
      other_ref_names.eachWithIndex { name, index ->
                                            ^^^^^
  ```

- Warning: `modules/nf-core/bracken/bracken/main.nf:42:9`: Variable was declared but not used

  ```nextflow
      def args = task.ext.args ?: ''
          ^^^^
  ```

- Warning: `modules/nf-core/cat/fastq/main.nf:22:60`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
      def readList = reads instanceof List ? reads.collect { it.toString() } : [reads.toString()]
                                                             ^^
  ```

- Warning: `modules/nf-core/cat/fastq/main.nf:48:60`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
      def readList = reads instanceof List ? reads.collect { it.toString() } : [reads.toString()]
                                                             ^^
  ```

- Warning: `modules/nf-core/custom/catadditionalfasta/main.nf:26:9`: Variable was declared but not used

  ```nextflow
      def prefix = task.ext.prefix ?: "${meta.id}"
          ^^^^^^
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
      def args = task.ext.args ?: ''
          ^^^^
  ```

- Warning: `modules/nf-core/hisat2/extractsplicesites/main.nf:21:9`: Variable was declared but not used

  ```nextflow
      def args = task.ext.args ?: ''
          ^^^^
  ```

- Warning: `modules/nf-core/kraken2/kraken2/main.nf:60:9`: Variable was declared but not used

  ```nextflow
      def args = task.ext.args ?: ''
          ^^^^
  ```

- Warning: `modules/nf-core/kraken2/kraken2/main.nf:62:9`: Variable was declared but not used

  ```nextflow
      def paired       = meta.single_end ? "" : "--paired"
          ^^^^^^
  ```

- Warning: `modules/nf-core/kraken2/kraken2/main.nf:65:9`: Variable was declared but not used

  ```nextflow
      def readclassification_option = save_reads_assignment ? "--output ${prefix}.kraken2.classifiedreads.txt" : "--output /dev/null"
          ^^^^^^^^^^^^^^^^^^^^^^^^^
  ```

- Warning: `modules/nf-core/kraken2/kraken2/main.nf:66:9`: Variable was declared but not used

  ```nextflow
      def compress_reads_command = save_output_fastqs ? "pigz -p $task.cpus *.fastq" : ""
          ^^^^^^^^^^^^^^^^^^^^^^
  ```

- Warning: `modules/nf-core/rsem/preparereference/main.nf:27:30`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          args_list.removeIf { it.contains('--star') }
                               ^^
  ```

- Warning: `modules/nf-core/rseqc/readdistribution/main.nf:22:9`: Variable was declared but not used

  ```nextflow
      def args = task.ext.args ?: ''
          ^^^^
  ```

- Warning: `modules/nf-core/rseqc/tin/main.nf:24:9`: Variable was declared but not used

  ```nextflow
      def prefix = task.ext.prefix ?: "${meta.id}"
          ^^^^^^
  ```

- Warning: `modules/nf-core/rseqc/tin/main.nf:33:9`: Variable was declared but not used

  ```nextflow
      def prefix = task.ext.prefix ?: "${meta.id}"
          ^^^^^^
  ```

- Warning: `modules/nf-core/salmon/quant/main.nf:34:58`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
      meta.single_end ? [reads].flatten().each { reads1 << it } : reads.eachWithIndex { v, ix -> (ix & 1 ? reads2 : reads1) << v }
                                                           ^^
  ```

- Warning: `modules/nf-core/sentieon/rsemcalculateexpression/main.nf:47:9`: Variable was declared but not used

  ```nextflow
      def sentieonLicense = secrets.SENTIEON_LICENSE_BASE64
          ^^^^^^^^^^^^^^^
  ```

- Warning: `modules/nf-core/sentieon/rsempreparereference/main.nf:28:30`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          args_list.removeIf { it.contains('--star') }
                               ^^
  ```

- Warning: `modules/nf-core/sentieon/staralign/main.nf:47:58`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
      meta.single_end ? [reads].flatten().each { reads1 << it } : reads.eachWithIndex { v, ix -> (ix & 1 ? reads2 : reads1) << v }
                                                           ^^
  ```

- Warning: `modules/nf-core/sentieon/staralign/main.nf:55:9`: Variable was declared but not used

  ```nextflow
      def sentieonLicense = secrets.SENTIEON_LICENSE_BASE64
          ^^^^^^^^^^^^^^^
  ```

- Warning: `modules/nf-core/sortmerna/main.nf:29:9`: Variable was declared but not used

  ```nextflow
      def skip_index    = args.contains('--index 0')? true : false
          ^^^^^^^^^^
  ```

- Warning: `modules/nf-core/sortmerna/main.nf:40:59`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          reads_input = paired_end ? reads.collect{"--reads $it"}.join(' ') : "--reads $reads"
                                                            ^^
  ```

- Warning: `modules/nf-core/sortmerna/main.nf:83:9`: Variable was declared but not used

  ```nextflow
      def paired_cmd    = ''
          ^^^^^^^^^^
  ```

- Warning: `modules/nf-core/sortmerna/main.nf:84:9`: Variable was declared but not used

  ```nextflow
      def out2_cmd      = ''
          ^^^^^^^^
  ```

- Warning: `modules/nf-core/sortmerna/main.nf:89:59`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          reads_input = paired_end ? reads.collect{"--reads $it"}.join(' ') : "--reads $reads"
                                                            ^^
  ```

- Warning: `modules/nf-core/sylph/profile/main.nf:40:9`: Variable was declared but not used

  ```nextflow
      def args = task.ext.args ?: ''
          ^^^^
  ```

- Warning: `modules/nf-core/sylph/profile/main.nf:42:9`: Variable was declared but not used

  ```nextflow
      def input = meta.single_end ? "${reads}" : "-1 ${reads[0]} -2 ${reads[1]}"
          ^^^^^
  ```

- Warning: `modules/nf-core/trimgalore/main.nf:47:31`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          args_list.removeAll { it.toLowerCase().contains('_r2 ') }
                                ^^
  ```

- Warning: `modules/nf-core/ucsc/bedclip/main.nf:23:9`: Variable was declared but not used

  ```nextflow
      def args = task.ext.args ?: ''
          ^^^^
  ```

- Warning: `modules/nf-core/ucsc/bedgraphtobigwig/main.nf:23:9`: Variable was declared but not used

  ```nextflow
      def args = task.ext.args ?: ''
          ^^^^
  ```

- Warning: `subworkflows/local/align_star/main.nf:13:26`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
  def getStarPercentMapped(params, align_log) {
                           ^^^^^^
  ```

- Warning: `subworkflows/local/align_star/main.nf:40:19`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_versions = Channel.empty()
                    ^^^^^^^
  ```

- Warning: `subworkflows/local/prepare_genome/main.nf:72:19`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_versions = Channel.empty()
                    ^^^^^^^
  ```

- Warning: `subworkflows/local/prepare_genome/main.nf:77:14`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_gtf = Channel.empty()
               ^^^^^^^
  ```

- Warning: `subworkflows/local/prepare_genome/main.nf:80:93`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
              ch_gtf      = GUNZIP_GTF ([ [:], file(gtf, checkIfExists: true) ]).gunzip.map { it[1] }
                                                                                              ^^
  ```

- Warning: `subworkflows/local/prepare_genome/main.nf:83:22`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
              ch_gtf = Channel.value(file(gtf, checkIfExists: true))
                       ^^^^^^^
  ```

- Warning: `subworkflows/local/prepare_genome/main.nf:91:22`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
              ch_gff = Channel.value(file(gff, checkIfExists: true)).map { [ [:], it ] }
                       ^^^^^^^
  ```

- Warning: `subworkflows/local/prepare_genome/main.nf:91:81`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
              ch_gff = Channel.value(file(gff, checkIfExists: true)).map { [ [:], it ] }
                                                                                  ^^
  ```

- Warning: `subworkflows/local/prepare_genome/main.nf:93:53`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          ch_gtf      = GFFREAD(ch_gff, []).gtf.map { it[1] }
                                                      ^^
  ```

- Warning: `subworkflows/local/prepare_genome/main.nf:102:16`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_fasta = Channel.of([])
                 ^^^^^^^
  ```

- Warning: `subworkflows/local/prepare_genome/main.nf:106:97`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
              ch_fasta    = GUNZIP_FASTA ([ [:], file(fasta, checkIfExists: true) ]).gunzip.map { it[1] }
                                                                                                  ^^
  ```

- Warning: `subworkflows/local/prepare_genome/main.nf:109:24`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
              ch_fasta = Channel.value(file(fasta, checkIfExists: true))
                         ^^^^^^^
  ```

- Warning: `subworkflows/local/prepare_genome/main.nf:131:20`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_add_fasta = Channel.empty()
                     ^^^^^^^
  ```

- Warning: `subworkflows/local/prepare_genome/main.nf:134:119`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
              ch_add_fasta = GUNZIP_ADDITIONAL_FASTA([ [:], file(additional_fasta, checkIfExists: true) ]).gunzip.map { it[1] }
                                                                                                                        ^^
  ```

- Warning: `subworkflows/local/prepare_genome/main.nf:137:28`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
              ch_add_fasta = Channel.value(file(additional_fasta, checkIfExists: true))
                             ^^^^^^^
  ```

- Warning: `subworkflows/local/prepare_genome/main.nf:142:39`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
              ch_add_fasta.map { [ [:], it ] },
                                        ^^
  ```

- Warning: `subworkflows/local/prepare_genome/main.nf:145:65`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          ch_fasta    = CUSTOM_CATADDITIONALFASTA.out.fasta.map { it[1] }.first()
                                                                  ^^
  ```

- Warning: `subworkflows/local/prepare_genome/main.nf:146:63`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          ch_gtf      = CUSTOM_CATADDITIONALFASTA.out.gtf.map { it[1] }.first()
                                                                ^^
  ```

- Warning: `subworkflows/local/prepare_genome/main.nf:153:19`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_gene_bed = Channel.empty()
                    ^^^^^^^
  ```

- Warning: `subworkflows/local/prepare_genome/main.nf:156:103`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
              ch_gene_bed = GUNZIP_GENE_BED ([ [:], file(gene_bed, checkIfExists: true) ]).gunzip.map { it[1] }
                                                                                                        ^^
  ```

- Warning: `subworkflows/local/prepare_genome/main.nf:159:27`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
              ch_gene_bed = Channel.value(file(gene_bed, checkIfExists: true))
                            ^^^^^^^
  ```

- Warning: `subworkflows/local/prepare_genome/main.nf:171:27`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_transcript_fasta = Channel.empty()
                            ^^^^^^^
  ```

- Warning: `subworkflows/local/prepare_genome/main.nf:175:127`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
              ch_transcript_fasta = GUNZIP_TRANSCRIPT_FASTA ([ [:], file(transcript_fasta, checkIfExists: true) ]).gunzip.map { it[1] }
                                                                                                                                ^^
  ```

- Warning: `subworkflows/local/prepare_genome/main.nf:178:35`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
              ch_transcript_fasta = Channel.value(file(transcript_fasta, checkIfExists: true))
                                    ^^^^^^^
  ```

- Warning: `subworkflows/local/prepare_genome/main.nf:202:22`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_fai         = Channel.empty()
                       ^^^^^^^
  ```

- Warning: `subworkflows/local/prepare_genome/main.nf:203:22`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_chrom_sizes = Channel.empty()
                       ^^^^^^^
  ```

- Warning: `subworkflows/local/prepare_genome/main.nf:205:46`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          SAMTOOLS_FAIDX(ch_fasta.map { [ [:], it ] }, [ [:], [] ], true)
                                               ^^
  ```

- Warning: `subworkflows/local/prepare_genome/main.nf:206:55`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          ch_fai         = SAMTOOLS_FAIDX.out.fai.map { it[1] }
                                                        ^^
  ```

- Warning: `subworkflows/local/prepare_genome/main.nf:207:57`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          ch_chrom_sizes = SAMTOOLS_FAIDX.out.sizes.map { it[1] }
                                                          ^^
  ```

- Warning: `subworkflows/local/prepare_genome/main.nf:223:24`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_bbsplit_index = Channel.empty()
                         ^^^^^^^
  ```

- Warning: `subworkflows/local/prepare_genome/main.nf:228:120`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
                  ch_bbsplit_index = UNTAR_BBSPLIT_INDEX ([ [:], file(bbsplit_index, checkIfExists: true) ]).untar.map { it[1] }
                                                                                                                         ^^
  ```

- Warning: `subworkflows/local/prepare_genome/main.nf:231:36`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
                  ch_bbsplit_index = Channel.value(file(bbsplit_index, checkIfExists: true))
                                     ^^^^^^^
  ```

- Warning: `subworkflows/local/prepare_genome/main.nf:236:13`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
              Channel
              ^^^^^^^
  ```

- Warning: `subworkflows/local/prepare_genome/main.nf:242:30`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
                  .collect { [ it ] } // Collect entries as a list to pass as "tuple val(short_names), path(path_to_fasta)" to module
                               ^^
  ```

- Warning: `subworkflows/local/prepare_genome/main.nf:260:26`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_sortmerna_index = Channel.empty()
                           ^^^^^^^
  ```

- Warning: `subworkflows/local/prepare_genome/main.nf:261:26`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_rrna_fastas     = Channel.empty()
                           ^^^^^^^
  ```

- Warning: `subworkflows/local/prepare_genome/main.nf:266:26`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
          ch_rrna_fastas = Channel.from(ribo_db.readLines())
                           ^^^^^^^
  ```

- Warning: `subworkflows/local/prepare_genome/main.nf:274:126`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
                  ch_sortmerna_index = UNTAR_SORTMERNA_INDEX ([ [:], file(sortmerna_index, checkIfExists: true) ]).untar.map { it[1] }
                                                                                                                               ^^
  ```

- Warning: `subworkflows/local/prepare_genome/main.nf:277:38`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
                  ch_sortmerna_index = Channel.value([ [:], file(sortmerna_index, checkIfExists: true) ])
                                       ^^^^^^^
  ```

- Warning: `subworkflows/local/prepare_genome/main.nf:282:17`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
                  Channel.of([ [], [] ]),
                  ^^^^^^^
  ```

- Warning: `subworkflows/local/prepare_genome/main.nf:283:63`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
                  ch_rrna_fastas.collect().map { [ 'rrna_refs', it ] },
                                                                ^^
  ```

- Warning: `subworkflows/local/prepare_genome/main.nf:284:17`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
                  Channel.of([ [], [] ])
                  ^^^^^^^
  ```

- Warning: `subworkflows/local/prepare_genome/main.nf:294:21`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_star_index = Channel.empty()
                      ^^^^^^^
  ```

- Warning: `subworkflows/local/prepare_genome/main.nf:298:111`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
                  ch_star_index = UNTAR_STAR_INDEX ([ [:], file(star_index, checkIfExists: true) ]).untar.map { it[1] }
                                                                                                                ^^
  ```

- Warning: `subworkflows/local/prepare_genome/main.nf:301:33`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
                  ch_star_index = Channel.value(file(star_index, checkIfExists: true))
                                  ^^^^^^^
  ```

- Warning: `subworkflows/local/prepare_genome/main.nf:316:43`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
                      ch_fasta.map { [ [:], it ] },
                                            ^^
  ```

- Warning: `subworkflows/local/prepare_genome/main.nf:317:43`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
                      ch_gtf.map   { [ [:], it ] }
                                            ^^
  ```

- Warning: `subworkflows/local/prepare_genome/main.nf:318:31`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
                  ).index.map { it[1] }
                                ^^
  ```

- Warning: `subworkflows/local/prepare_genome/main.nf:327:21`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_rsem_index = Channel.empty()
                      ^^^^^^^
  ```

- Warning: `subworkflows/local/prepare_genome/main.nf:331:111`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
                  ch_rsem_index = UNTAR_RSEM_INDEX ([ [:], file(rsem_index, checkIfExists: true) ]).untar.map { it[1] }
                                                                                                                ^^
  ```

- Warning: `subworkflows/local/prepare_genome/main.nf:334:33`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
                  ch_rsem_index = Channel.value(file(rsem_index, checkIfExists: true))
                                  ^^^^^^^
  ```

- Warning: `subworkflows/local/prepare_genome/main.nf:353:23`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_splicesites  = Channel.empty()
                        ^^^^^^^
  ```

- Warning: `subworkflows/local/prepare_genome/main.nf:354:23`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_hisat2_index = Channel.empty()
                        ^^^^^^^
  ```

- Warning: `subworkflows/local/prepare_genome/main.nf:358:30`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
              ch_splicesites = Channel.value(file(splicesites, checkIfExists: true))
                               ^^^^^^^
  ```

- Warning: `subworkflows/local/prepare_genome/main.nf:361:76`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
              ch_splicesites = HISAT2_EXTRACTSPLICESITES(ch_gtf.map { [ [:], it ] }).txt.map { it[1] }
                                                                             ^^
  ```

- Warning: `subworkflows/local/prepare_genome/main.nf:361:94`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
              ch_splicesites = HISAT2_EXTRACTSPLICESITES(ch_gtf.map { [ [:], it ] }).txt.map { it[1] }
                                                                                               ^^
  ```

- Warning: `subworkflows/local/prepare_genome/main.nf:367:117`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
                  ch_hisat2_index = UNTAR_HISAT2_INDEX ([ [:], file(hisat2_index, checkIfExists: true) ]).untar.map { it[1] }
                                                                                                                      ^^
  ```

- Warning: `subworkflows/local/prepare_genome/main.nf:370:35`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
                  ch_hisat2_index = Channel.value(file(hisat2_index, checkIfExists: true))
                                    ^^^^^^^
  ```

- Warning: `subworkflows/local/prepare_genome/main.nf:375:39`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
                  ch_fasta.map { [ [:], it ] },
                                        ^^
  ```

- Warning: `subworkflows/local/prepare_genome/main.nf:376:39`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
                  ch_gtf.map   { [ [:], it ] },
                                        ^^
  ```

- Warning: `subworkflows/local/prepare_genome/main.nf:377:45`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
                  ch_splicesites.map { [ [:], it ] }
                                              ^^
  ```

- Warning: `subworkflows/local/prepare_genome/main.nf:378:27`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
              ).index.map { it[1] }
                            ^^
  ```

- Warning: `subworkflows/local/prepare_genome/main.nf:387:23`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_salmon_index = Channel.empty()
                        ^^^^^^^
  ```

- Warning: `subworkflows/local/prepare_genome/main.nf:390:88`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
              ch_salmon_index = UNTAR_SALMON_INDEX ( [ [:], salmon_index ] ).untar.map { it[1] }
                                                                                         ^^
  ```

- Warning: `subworkflows/local/prepare_genome/main.nf:393:31`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
              ch_salmon_index = Channel.value(file(salmon_index))
                                ^^^^^^^
  ```

- Warning: `subworkflows/local/prepare_genome/main.nf:411:25`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_kallisto_index = Channel.empty()
                          ^^^^^^^
  ```

- Warning: `subworkflows/local/prepare_genome/main.nf:417:33`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
              ch_kallisto_index = Channel.value([[:], file(kallisto_index)])
                                  ^^^^^^^
  ```

- Warning: `subworkflows/local/prepare_genome/main.nf:421:83`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
              ch_kallisto_index = KALLISTO_INDEX ( ch_transcript_fasta.map { [ [:], it] } ).index
                                                                                    ^^
  ```

- Warning: `subworkflows/local/quantify_rsem/main.nf:17:19`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_versions = Channel.empty()
                    ^^^^^^^
  ```

- Warning: `subworkflows/local/quantify_rsem/main.nf:41:32`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          ch_counts_gene.collect{it[1]},       // [meta, counts]: Collect the second element (counts files) in the channel across all samples
                                 ^^
  ```

- Warning: `subworkflows/local/quantify_rsem/main.nf:42:38`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          ch_counts_transcript.collect{it[1]}
                                       ^^
  ```

- Warning: `subworkflows/local/utils_nfcore_rnaseq_pipeline/main.nf:34:5`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
      monochrome_logs   // boolean: Do not use coloured log outputs
      ^^^^^^^^^^^^^^^
  ```

- Warning: `subworkflows/local/utils_nfcore_rnaseq_pipeline/main.nf:37:5`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
      input             //  string: Path to input samplesheet
      ^^^^^
  ```

- Warning: `subworkflows/local/utils_nfcore_rnaseq_pipeline/main.nf:188:9`: Variable was declared but not used

  ```nextflow
      def id = input[0]
          ^^
  ```

- Warning: `subworkflows/local/utils_nfcore_rnaseq_pipeline/main.nf:195:42`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
      def strandedness_ok = metas.collect{ it.strandedness }.unique().size == 1
                                           ^^
  ```

- Warning: `subworkflows/local/utils_nfcore_rnaseq_pipeline/main.nf:208:46`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          def genome_bam = genome_bams?.find { it != null }
                                               ^^
  ```

- Warning: `subworkflows/local/utils_nfcore_rnaseq_pipeline/main.nf:209:60`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          def transcriptome_bam = transcriptome_bams?.find { it != null }
                                                             ^^
  ```

- Warning: `subworkflows/local/utils_nfcore_rnaseq_pipeline/main.nf:361:89`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
      def rseqc_modules = params.rseqc_modules ? params.rseqc_modules.split(',').collect{ it.trim().toLowerCase() } : []
                                                                                          ^^
  ```

- Warning: `subworkflows/local/utils_nfcore_rnaseq_pipeline/main.nf:705:57`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
      def fail_mapped_count  = pass_mapped_reads.count  { key, value -> value == false }
                                                          ^^^
  ```

- Warning: `subworkflows/local/utils_nfcore_rnaseq_pipeline/main.nf:706:57`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
      def fail_trimmed_count = pass_trimmed_reads.count { key, value -> value == false }
                                                          ^^^
  ```

- Warning: `subworkflows/local/utils_nfcore_rnaseq_pipeline/main.nf:707:57`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
      def fail_strand_count  = pass_strand_check.count  { key, value -> value == false }
                                                          ^^^
  ```

- Warning: `subworkflows/nf-core/bam_dedup_stats_samtools_umicollapse/main.nf:15:19`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_versions = Channel.empty()
                    ^^^^^^^
  ```

- Warning: `subworkflows/nf-core/bam_dedup_stats_samtools_umitools/main.nf:16:19`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_versions = Channel.empty()
                    ^^^^^^^
  ```

- Warning: `subworkflows/nf-core/bam_dedup_umi/main.nf:25:19`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_versions = Channel.empty()
                    ^^^^^^^
  ```

- Warning: `subworkflows/nf-core/bam_dedup_umi/main.nf:115:14`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          .map{it[1]}
               ^^
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

- Warning: `subworkflows/nf-core/bedgraph_bedclip_bedgraphtobigwig/main.nf:15:19`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_versions = Channel.empty()
                    ^^^^^^^
  ```

- Warning: `subworkflows/nf-core/fastq_align_hisat2/main.nf:14:19`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

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

- Warning: `subworkflows/nf-core/fastq_fastqc_umitools_trimgalore/main.nf:39:19`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_versions = Channel.empty()
                    ^^^^^^^
  ```

- Warning: `subworkflows/nf-core/fastq_fastqc_umitools_trimgalore/main.nf:40:19`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      fastqc_html = Channel.empty()
                    ^^^^^^^
  ```

- Warning: `subworkflows/nf-core/fastq_fastqc_umitools_trimgalore/main.nf:41:18`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      fastqc_zip = Channel.empty()
                   ^^^^^^^
  ```

- Warning: `subworkflows/nf-core/fastq_fastqc_umitools_trimgalore/main.nf:49:15`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      umi_log = Channel.empty()
                ^^^^^^^
  ```

- Warning: `subworkflows/nf-core/fastq_fastqc_umitools_trimgalore/main.nf:67:21`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      trim_unpaired = Channel.empty()
                      ^^^^^^^
  ```

- Warning: `subworkflows/nf-core/fastq_fastqc_umitools_trimgalore/main.nf:68:17`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      trim_html = Channel.empty()
                  ^^^^^^^
  ```

- Warning: `subworkflows/nf-core/fastq_fastqc_umitools_trimgalore/main.nf:69:16`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      trim_zip = Channel.empty()
                 ^^^^^^^
  ```

- Warning: `subworkflows/nf-core/fastq_fastqc_umitools_trimgalore/main.nf:70:16`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      trim_log = Channel.empty()
                 ^^^^^^^
  ```

- Warning: `subworkflows/nf-core/fastq_fastqc_umitools_trimgalore/main.nf:71:23`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      trim_read_count = Channel.empty()
                        ^^^^^^^
  ```

- Warning: `subworkflows/nf-core/fastq_qc_trim_filter_setstrandedness/main.nf:64:59`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
      def forwardFragments = forwardKeys.collect { libCounts[it] ?: 0 }.sum()
                                                            ^^
  ```

- Warning: `subworkflows/nf-core/fastq_qc_trim_filter_setstrandedness/main.nf:65:59`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
      def reverseFragments = reverseKeys.collect { libCounts[it] ?: 0 }.sum()
                                                            ^^
  ```

- Warning: `subworkflows/nf-core/fastq_qc_trim_filter_setstrandedness/main.nf:66:65`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
      def unstrandedFragments = unstrandedKeys.collect { libCounts[it] ?: 0 }.sum()
                                                                  ^^
  ```

- Warning: `subworkflows/nf-core/fastq_qc_trim_filter_setstrandedness/main.nf:129:19`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_versions = Channel.empty()
                    ^^^^^^^
  ```

- Warning: `subworkflows/nf-core/fastq_qc_trim_filter_setstrandedness/main.nf:130:25`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_filtered_reads = Channel.empty()
                          ^^^^^^^
  ```

- Warning: `subworkflows/nf-core/fastq_qc_trim_filter_setstrandedness/main.nf:131:26`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_trim_read_count = Channel.empty()
                           ^^^^^^^
  ```

- Warning: `subworkflows/nf-core/fastq_qc_trim_filter_setstrandedness/main.nf:132:24`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_multiqc_files = Channel.empty()
                         ^^^^^^^
  ```

- Warning: `subworkflows/nf-core/fastq_qc_trim_filter_setstrandedness/main.nf:133:19`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_lint_log = Channel.empty()
                    ^^^^^^^
  ```

- Warning: `subworkflows/nf-core/fastq_qc_trim_filter_setstrandedness/main.nf:161:75`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          ch_filtered_reads = ch_filtered_reads.join(FQ_LINT.out.lint.map { it[0] })
                                                                            ^^
  ```

- Warning: `subworkflows/nf-core/fastq_qc_trim_filter_setstrandedness/main.nf:236:96`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          ch_fail_trimming_multiqc.collectFile(name: 'fail_trimmed_samples_mqc.tsv').map { [[:], it] }
                                                                                                 ^^
  ```

- Warning: `subworkflows/nf-core/fastq_qc_trim_filter_setstrandedness/main.nf:244:90`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          ch_filtered_reads = ch_filtered_reads.join(FQ_LINT_AFTER_TRIMMING.out.lint.map { it[0] })
                                                                                           ^^
  ```

- Warning: `subworkflows/nf-core/fastq_qc_trim_filter_setstrandedness/main.nf:269:93`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
              ch_filtered_reads = ch_filtered_reads.join(FQ_LINT_AFTER_BBSPLIT.out.lint.map { it[0] })
                                                                                              ^^
  ```

- Warning: `subworkflows/nf-core/fastq_qc_trim_filter_setstrandedness/main.nf:296:98`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
              ch_filtered_reads = ch_filtered_reads.join(FQ_LINT_AFTER_RIBO_REMOVAL.out.lint.map { it[0] })
                                                                                                   ^^
  ```

- Warning: `subworkflows/nf-core/fastq_qc_trim_filter_setstrandedness/main.nf:317:16`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          .map { it.first() }
                 ^^
  ```

- Warning: `subworkflows/nf-core/fastq_qc_trim_filter_setstrandedness/main.nf:348:58`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
      multiqc_files   = ch_multiqc_files.transpose().map { it[1] }
                                                           ^^
  ```

- Warning: `subworkflows/nf-core/fastq_remove_rrna/main.nf:24:42`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
      def avgLenIdx = header.findIndexOf { it == 'avg_len' }
                                           ^^
  ```

- Warning: `subworkflows/nf-core/fastq_remove_rrna/main.nf:30:42`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
      def avgLens = lines[1..-1].collect { it.split('\t')[avgLenIdx] as float }
                                           ^^
  ```

- Warning: `subworkflows/nf-core/fastq_remove_rrna/main.nf:48:19`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_versions = Channel.empty()
                    ^^^^^^^
  ```

- Warning: `subworkflows/nf-core/fastq_remove_rrna/main.nf:49:24`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_multiqc_files = Channel.empty()
                         ^^^^^^^
  ```

- Warning: `subworkflows/nf-core/fastq_remove_rrna/main.nf:55:40`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
              .map { [[id: 'rrna_refs'], it] }
                                         ^^
  ```

- Warning: `subworkflows/nf-core/fastq_remove_rrna/main.nf:130:24`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
                  .map { meta, fasta -> fasta }
                         ^^^^
  ```

- Warning: `subworkflows/nf-core/fastq_remove_rrna/main.nf:144:29`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
              .branch { meta, reads ->
                              ^^^^^
  ```

- Warning: `subworkflows/nf-core/fastq_subsample_fq_salmon/main.nf:21:19`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_versions = Channel.empty()
                    ^^^^^^^
  ```

- Warning: `subworkflows/nf-core/quantify_pseudo_alignment/main.nf:29:19`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_versions = Channel.empty()
                    ^^^^^^^
  ```

- Warning: `subworkflows/nf-core/quantify_pseudo_alignment/main.nf:62:26`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          gtf.map { [ [:], it ] },
                           ^^
  ```

- Warning: `subworkflows/nf-core/quantify_pseudo_alignment/main.nf:63:36`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          ch_pseudo_results.collect{ it[1] }.map { [ [:], it ] },
                                     ^^
  ```

- Warning: `subworkflows/nf-core/quantify_pseudo_alignment/main.nf:63:57`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          ch_pseudo_results.collect{ it[1] }.map { [ [:], it ] },
                                                          ^^
  ```

- Warning: `subworkflows/nf-core/quantify_pseudo_alignment/main.nf:71:36`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          ch_pseudo_results.collect{ it[1] }.map { [ ['id': 'all_samples'], it ] },
                                     ^^
  ```

- Warning: `subworkflows/nf-core/quantify_pseudo_alignment/main.nf:71:75`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          ch_pseudo_results.collect{ it[1] }.map { [ ['id': 'all_samples'], it ] },
                                                                            ^^
  ```

- Warning: `subworkflows/nf-core/quantify_pseudo_alignment/main.nf:82:36`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
                          .map{tuple(it[0], it.tail())}
                                     ^^
  ```

- Warning: `subworkflows/nf-core/quantify_pseudo_alignment/main.nf:82:43`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
                          .map{tuple(it[0], it.tail())}
                                            ^^
  ```

- Warning: `subworkflows/nf-core/quantify_pseudo_alignment/main.nf:94:36`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
                          .map{tuple(it[0], it.tail())}
                                     ^^
  ```

- Warning: `subworkflows/nf-core/quantify_pseudo_alignment/main.nf:94:43`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
                          .map{tuple(it[0], it.tail())}
                                            ^^
  ```

- Warning: `workflows/rnaseq/main.nf:78:1`: Variable was declared but not used

  ```nextflow
  sample_status_header_multiqc    = file("$projectDir/workflows/rnaseq/assets/multiqc/sample_status_header.txt", checkIfExists: true)
  ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  ```

- Warning: `workflows/rnaseq/main.nf:79:1`: Variable was declared but not used

  ```nextflow
  ch_clustering_header_multiqc    = file("$projectDir/workflows/rnaseq/assets/multiqc/deseq2_clustering_header.txt", checkIfExists: true)
  ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  ```

- Warning: `workflows/rnaseq/main.nf:80:1`: Variable was declared but not used

  ```nextflow
  ch_biotypes_header_multiqc      = file("$projectDir/workflows/rnaseq/assets/multiqc/biotypes_header.txt", checkIfExists: true)
  ^^^^^^^^^^^^^^^^^^^^^^^^^^
  ```

- Warning: `workflows/rnaseq/main.nf:81:1`: Variable was declared but not used

  ```nextflow
  ch_dummy_file                   = ch_pca_header_multiqc
  ^^^^^^^^^^^^^
  ```

- Warning: `workflows/rnaseq/main.nf:107:24`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_multiqc_files = Channel.empty()
                         ^^^^^^^
  ```

- Warning: `workflows/rnaseq/main.nf:108:22`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_trim_status = Channel.empty()
                       ^^^^^^^
  ```

- Warning: `workflows/rnaseq/main.nf:109:21`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_map_status = Channel.empty()
                      ^^^^^^^
  ```

- Warning: `workflows/rnaseq/main.nf:110:24`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_strand_status = Channel.empty()
                         ^^^^^^^
  ```

- Warning: `workflows/rnaseq/main.nf:111:25`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_percent_mapped = Channel.empty()
                          ^^^^^^^
  ```

- Warning: `workflows/rnaseq/main.nf:116:26`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      def topic_versions = Channel.topic('versions')
                           ^^^^^^^
  ```

- Warning: `workflows/rnaseq/main.nf:136:5`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      Channel
      ^^^^^^^
  ```

- Warning: `workflows/rnaseq/main.nf:155:44`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
                      return [ meta.findAll {it.key != 'percent_mapped'}, reads ]
                                             ^^
  ```

- Warning: `workflows/rnaseq/main.nf:162:67`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
      ch_genome_bam = ch_input_branched.bam.map { meta, genome_bam, transcriptome_bam -> [ meta, genome_bam ] }.distinct()
                                                                    ^^^^^^^^^^^^^^^^^
  ```

- Warning: `workflows/rnaseq/main.nf:163:62`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
      ch_transcriptome_bam = ch_input_branched.bam.map { meta, genome_bam, transcriptome_bam -> [ meta, transcriptome_bam ] }.distinct()
                                                               ^^^^^^^^^^
  ```

- Warning: `workflows/rnaseq/main.nf:168:24`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          .filter{ meta, genome_bam, transcriptome_bam -> meta.percent_mapped }
                         ^^^^^^^^^^
  ```

- Warning: `workflows/rnaseq/main.nf:168:36`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          .filter{ meta, genome_bam, transcriptome_bam -> meta.percent_mapped }
                                     ^^^^^^^^^^^^^^^^^
  ```

- Warning: `workflows/rnaseq/main.nf:169:22`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          .map { meta, genome_bam, transcriptome_bam -> [ meta, meta.percent_mapped ] }
                       ^^^^^^^^^^
  ```

- Warning: `workflows/rnaseq/main.nf:169:34`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          .map { meta, genome_bam, transcriptome_bam -> [ meta, meta.percent_mapped ] }
                                   ^^^^^^^^^^^^^^^^^
  ```

- Warning: `workflows/rnaseq/main.nf:234:30`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_star_log            = Channel.empty()
                               ^^^^^^^
  ```

- Warning: `workflows/rnaseq/main.nf:235:30`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_unaligned_sequences = Channel.empty()
                               ^^^^^^^
  ```

- Warning: `workflows/rnaseq/main.nf:248:40`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
              ch_star_index.map { [ [:], it ] },
                                         ^^
  ```

- Warning: `workflows/rnaseq/main.nf:249:33`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
              ch_gtf.map { [ [:], it ] },
                                  ^^
  ```

- Warning: `workflows/rnaseq/main.nf:254:35`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
              ch_fasta.map { [ [:], it ] },
                                    ^^
  ```

- Warning: `workflows/rnaseq/main.nf:265:85`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          ch_multiqc_files                 = ch_multiqc_files.mix(ch_star_log.collect{it[1]})
                                                                                      ^^
  ```

- Warning: `workflows/rnaseq/main.nf:276:39`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
                  ch_fasta.map { [ [:], it ] },
                                        ^^
  ```

- Warning: `workflows/rnaseq/main.nf:281:50`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
                  ch_transcript_fasta.map { [ [:], it ] }
                                                   ^^
  ```

- Warning: `workflows/rnaseq/main.nf:299:51`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
                  .mix(ALIGN_STAR.out.stats.collect{it[1]})
                                                    ^^
  ```

- Warning: `workflows/rnaseq/main.nf:300:54`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
                  .mix(ALIGN_STAR.out.flagstat.collect{it[1]})
                                                       ^^
  ```

- Warning: `workflows/rnaseq/main.nf:301:54`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
                  .mix(ALIGN_STAR.out.idxstats.collect{it[1]})
                                                       ^^
  ```

- Warning: `workflows/rnaseq/main.nf:312:80`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          ch_multiqc_files = ch_multiqc_files.mix(QUANTIFY_RSEM.out.stat.collect{it[1]})
                                                                                 ^^
  ```

- Warning: `workflows/rnaseq/main.nf:332:41`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
              ch_samplesheet.map { [ [:], it ] },
                                          ^^
  ```

- Warning: `workflows/rnaseq/main.nf:349:74`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
                  QUANTIFY_STAR_SALMON.out.counts_gene_length_scaled.map { it[1] },
                                                                           ^^
  ```

- Warning: `workflows/rnaseq/main.nf:365:42`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
              ch_hisat2_index.map { [ [:], it ] },
                                           ^^
  ```

- Warning: `workflows/rnaseq/main.nf:366:41`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
              ch_splicesites.map { [ [:], it ] },
                                          ^^
  ```

- Warning: `workflows/rnaseq/main.nf:367:35`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
              ch_fasta.map { [ [:], it ] }
                                    ^^
  ```

- Warning: `workflows/rnaseq/main.nf:373:88`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          ch_multiqc_files = ch_multiqc_files.mix(FASTQ_ALIGN_HISAT2.out.summary.collect{it[1]})
                                                                                         ^^
  ```

- Warning: `workflows/rnaseq/main.nf:385:39`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
                  ch_fasta.map { [ [:], it ] },
                                        ^^
  ```

- Warning: `workflows/rnaseq/main.nf:390:50`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
                  ch_transcript_fasta.map { [ [:], it ] }
                                                   ^^
  ```

- Warning: `workflows/rnaseq/main.nf:406:59`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
                  .mix(FASTQ_ALIGN_HISAT2.out.stats.collect{it[1]})
                                                            ^^
  ```

- Warning: `workflows/rnaseq/main.nf:407:62`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
                  .mix(FASTQ_ALIGN_HISAT2.out.flagstat.collect{it[1]})
                                                               ^^
  ```

- Warning: `workflows/rnaseq/main.nf:408:62`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
                  .mix(FASTQ_ALIGN_HISAT2.out.idxstats.collect{it[1]})
                                                               ^^
  ```

- Warning: `workflows/rnaseq/main.nf:435:19`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          .filter { id, pass -> pass != null }
                    ^^
  ```

- Warning: `workflows/rnaseq/main.nf:439:19`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          .filter { id, percent_mapped, pass -> pass != null && !pass }
                    ^^
  ```

- Warning: `workflows/rnaseq/main.nf:439:23`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          .filter { id, percent_mapped, pass -> pass != null && !pass }
                        ^^^^^^^^^^^^^^
  ```

- Warning: `workflows/rnaseq/main.nf:440:36`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          .map { id, percent_mapped, pass -> [ "${id}\t${percent_mapped}" ] }
                                     ^^^^
  ```

- Warning: `workflows/rnaseq/main.nf:454:19`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          .filter { meta, bam, index, pass -> pass || pass == null }
                    ^^^^
  ```

- Warning: `workflows/rnaseq/main.nf:454:25`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          .filter { meta, bam, index, pass -> pass || pass == null }
                          ^^^
  ```

- Warning: `workflows/rnaseq/main.nf:454:30`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          .filter { meta, bam, index, pass -> pass || pass == null }
                               ^^^^^
  ```

- Warning: `workflows/rnaseq/main.nf:455:39`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          .multiMap { meta, bam, index, pass ->
                                        ^^^^
  ```

- Warning: `workflows/rnaseq/main.nf:470:87`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          ch_multiqc_files = ch_multiqc_files.mix(PRESEQ_LCEXTRAP.out.lc_extrap.collect{it[1]})
                                                                                        ^^
  ```

- Warning: `workflows/rnaseq/main.nf:480:35`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
              ch_fasta.map { [ [:], it ] },
                                    ^^
  ```

- Warning: `workflows/rnaseq/main.nf:481:33`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
              ch_fai.map { [ [:], it ] }
                                  ^^
  ```

- Warning: `workflows/rnaseq/main.nf:485:93`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          ch_multiqc_files = ch_multiqc_files.mix(BAM_MARKDUPLICATES_PICARD.out.stats.collect{it[1]})
                                                                                              ^^
  ```

- Warning: `workflows/rnaseq/main.nf:486:96`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          ch_multiqc_files = ch_multiqc_files.mix(BAM_MARKDUPLICATES_PICARD.out.flagstat.collect{it[1]})
                                                                                                 ^^
  ```

- Warning: `workflows/rnaseq/main.nf:487:96`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          ch_multiqc_files = ch_multiqc_files.mix(BAM_MARKDUPLICATES_PICARD.out.idxstats.collect{it[1]})
                                                                                                 ^^
  ```

- Warning: `workflows/rnaseq/main.nf:488:95`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          ch_multiqc_files = ch_multiqc_files.mix(BAM_MARKDUPLICATES_PICARD.out.metrics.collect{it[1]})
                                                                                                ^^
  ```

- Warning: `workflows/rnaseq/main.nf:511:33`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
              .map { biotypeInGtf(it, biotype) }
                                  ^^
  ```

- Warning: `workflows/rnaseq/main.nf:518:23`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
              .filter { it[-1] }
                        ^^
  ```

- Warning: `workflows/rnaseq/main.nf:519:20`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
              .map { it[0..<it.size()-1] }
                     ^^
  ```

- Warning: `workflows/rnaseq/main.nf:519:27`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
              .map { it[0..<it.size()-1] }
                            ^^
  ```

- Warning: `workflows/rnaseq/main.nf:531:88`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          ch_multiqc_files = ch_multiqc_files.mix(MULTIQC_CUSTOM_BIOTYPE.out.tsv.collect{it[1]})
                                                                                         ^^
  ```

- Warning: `workflows/rnaseq/main.nf:581:39`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
                  ch_fasta.map { [ [:], it ] },
                                        ^^
  ```

- Warning: `workflows/rnaseq/main.nf:587:37`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
                  ch_gtf.map { [ [:], it ] }
                                      ^^
  ```

- Warning: `workflows/rnaseq/main.nf:589:89`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
              ch_multiqc_files = ch_multiqc_files.mix(QUALIMAP_RNASEQ.out.results.collect{it[1]})
                                                                                          ^^
  ```

- Warning: `workflows/rnaseq/main.nf:596:37`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
                  ch_gtf.map { [ [:], it ] }
                                      ^^
  ```

- Warning: `workflows/rnaseq/main.nf:598:82`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
              ch_multiqc_files = ch_multiqc_files.mix(DUPRADAR.out.multiqc.collect{it[1]})
                                                                                   ^^
  ```

- Warning: `workflows/rnaseq/main.nf:603:93`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          def rseqc_modules = params.rseqc_modules ? params.rseqc_modules.split(',').collect{ it.trim().toLowerCase() } : []
                                                                                              ^^
  ```

- Warning: `workflows/rnaseq/main.nf:617:87`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
              ch_multiqc_files = ch_multiqc_files.mix(BAM_RSEQC.out.bamstat_txt.collect{it[1]})
                                                                                        ^^
  ```

- Warning: `workflows/rnaseq/main.nf:618:95`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
              ch_multiqc_files = ch_multiqc_files.mix(BAM_RSEQC.out.inferexperiment_txt.collect{it[1]})
                                                                                                ^^
  ```

- Warning: `workflows/rnaseq/main.nf:619:94`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
              ch_multiqc_files = ch_multiqc_files.mix(BAM_RSEQC.out.innerdistance_freq.collect{it[1]})
                                                                                               ^^
  ```

- Warning: `workflows/rnaseq/main.nf:620:98`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
              ch_multiqc_files = ch_multiqc_files.mix(BAM_RSEQC.out.junctionannotation_log.collect{it[1]})
                                                                                                   ^^
  ```

- Warning: `workflows/rnaseq/main.nf:621:102`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
              ch_multiqc_files = ch_multiqc_files.mix(BAM_RSEQC.out.junctionsaturation_rscript.collect{it[1]})
                                                                                                       ^^
  ```

- Warning: `workflows/rnaseq/main.nf:622:96`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
              ch_multiqc_files = ch_multiqc_files.mix(BAM_RSEQC.out.readdistribution_txt.collect{it[1]})
                                                                                                 ^^
  ```

- Warning: `workflows/rnaseq/main.nf:623:99`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
              ch_multiqc_files = ch_multiqc_files.mix(BAM_RSEQC.out.readduplication_pos_xls.collect{it[1]})
                                                                                                    ^^
  ```

- Warning: `workflows/rnaseq/main.nf:624:83`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
              ch_multiqc_files = ch_multiqc_files.mix(BAM_RSEQC.out.tin_txt.collect{it[1]})
                                                                                    ^^
  ```

- Warning: `workflows/rnaseq/main.nf:697:84`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
                  ch_multiqc_files = ch_multiqc_files.mix(KRAKEN2.out.report.collect{it[1]})
                                                                                     ^^
  ```

- Warning: `workflows/rnaseq/main.nf:704:81`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
                  ch_multiqc_files = ch_multiqc_files.mix(BRACKEN.out.txt.collect{it[1]})
                                                                                  ^^
  ```

- Warning: `workflows/rnaseq/main.nf:707:94`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
              def sylph_databases = params.sylph_db ? params.sylph_db.split(',').collect{ file(it.trim()) } : []
                                                                                               ^^
  ```

- Warning: `workflows/rnaseq/main.nf:713:70`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
              ch_sylph_profile = SYLPH_PROFILE.out.profile_out.filter{!it[1].isEmpty()}
                                                                       ^^
  ```

- Warning: `workflows/rnaseq/main.nf:716:107`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
              def sylph_taxonomies = params.sylph_taxonomy ? params.sylph_taxonomy.split(',').collect{ file(it.trim()) } : []
                                                                                                            ^^
  ```

- Warning: `workflows/rnaseq/main.nf:723:97`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
              ch_multiqc_files = ch_multiqc_files.mix(SYLPHTAX_TAXPROF.out.taxprof_output.collect{it[1]})
                                                                                                  ^^
  ```

- Warning: `workflows/rnaseq/main.nf:739:41`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
              ch_samplesheet.map { [ [:], it ] },
                                          ^^
  ```

- Warning: `workflows/rnaseq/main.nf:753:95`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          ch_multiqc_files = ch_multiqc_files.mix(QUANTIFY_PSEUDO_ALIGNMENT.out.multiqc.collect{it[1]})
                                                                                                ^^
  ```

- Warning: `workflows/rnaseq/main.nf:758:52`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
                  ch_counts_gene_length_scaled.map { it[1] },
                                                     ^^
  ```

- Warning: `workflows/rnaseq/main.nf:779:25`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_multiqc_report = Channel.empty()
                          ^^^^^^^
  ```

- Warning: `workflows/rnaseq/main.nf:784:36`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
          ch_multiqc_config        = Channel.fromPath("$projectDir/workflows/rnaseq/assets/multiqc/multiqc_config.yml", checkIfExists: true)
                                     ^^^^^^^
  ```

- Warning: `workflows/rnaseq/main.nf:785:60`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
          ch_multiqc_custom_config = params.multiqc_config ? Channel.fromPath(params.multiqc_config) : Channel.empty()
                                                             ^^^^^^^
  ```

- Warning: `workflows/rnaseq/main.nf:785:102`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
          ch_multiqc_custom_config = params.multiqc_config ? Channel.fromPath(params.multiqc_config) : Channel.empty()
                                                                                                       ^^^^^^^
  ```

- Warning: `workflows/rnaseq/main.nf:786:60`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
          ch_multiqc_logo          = params.multiqc_logo   ? Channel.fromPath(params.multiqc_logo)   : Channel.empty()
                                                             ^^^^^^^
  ```

- Warning: `workflows/rnaseq/main.nf:786:102`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
          ch_multiqc_logo          = params.multiqc_logo   ? Channel.fromPath(params.multiqc_logo)   : Channel.empty()
                                                                                                       ^^^^^^^
  ```

- Warning: `workflows/rnaseq/main.nf:789:31`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
          ch_workflow_summary = Channel.value(
                                ^^^^^^^
  ```

- Warning: `workflows/rnaseq/main.nf:796:34`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
          ch_methods_description = Channel.value(
                                   ^^^^^^^
  ```

- Warning: `workflows/rnaseq/main.nf:832:43`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
                  return mappings.collect { it.join('\t') }
                                            ^^
  ```

- Warning: `workflows/rnaseq/main.nf:853:5`: Variable was declared but not used

  ```nextflow
      ch_samplesheet_with_bams = Channel.empty()
      ^^^^^^^^^^^^^^^^^^^^^^^^
  ```

- Warning: `workflows/rnaseq/main.nf:853:32`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_samplesheet_with_bams = Channel.empty()
                                 ^^^^^^^
  ```

- Warning: `workflows/rnaseq/main.nf:860:20`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
              .map { id, fastq_meta, reads, meta, genome_bam, transcriptome_bam, percent_mapped ->
                     ^^
  ```

- Warning: `workflows/rnaseq/main.nf:860:24`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
              .map { id, fastq_meta, reads, meta, genome_bam, transcriptome_bam, percent_mapped ->
                         ^^^^^^^^^^
  ```

- Warning: `workflows/rnaseq/nextflow.config:207:83`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
              saveAs: { params.save_align_intermeds || params.skip_markduplicates ? it : null }
                                                                                    ^^
  ```
