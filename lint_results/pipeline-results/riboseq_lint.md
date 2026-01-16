# Nextflow lint results

- Generated: 2026-01-16T10:27:41.635039625Z
- Nextflow version: 25.12.0-edge
- Summary: 42 errors, 195 warnings

## :x: Errors

- Error: `conf/modules.config:125:1`: If statements cannot be mixed with config statements

  ```nextflow
  if (!params.skip_bbsplit && params.bbsplit_fasta_list) {
  ^
  ```

- Error: `conf/modules.config:138:1`: If statements cannot be mixed with config statements

  ```nextflow
  if (params.remove_ribo_rna && params.ribo_database_manifest) {
  ^
  ```

- Error: `conf/modules.config:176:1`: If statements cannot be mixed with config statements

  ```nextflow
  if (! params.skip_linting) {
  ^
  ```

- Error: `conf/modules.config:219:1`: If statements cannot be mixed with config statements

  ```nextflow
  if (!(params.skip_fastqc || params.skip_qc)) {
  ^
  ```

- Error: `conf/modules.config:259:1`: If statements cannot be mixed with config statements

  ```nextflow
  if (!params.skip_trimming) {
  ^
  ```

- Error: `conf/modules.config:345:1`: If statements cannot be mixed with config statements

  ```nextflow
  if (params.with_umi && !params.skip_umi_extract) {
  ^
  ```

- Error: `conf/modules.config:375:1`: If statements cannot be mixed with config statements

  ```nextflow
  if (!params.skip_bbsplit) {
  ^
  ```

- Error: `conf/modules.config:396:1`: If statements cannot be mixed with config statements

  ```nextflow
  if (params.remove_ribo_rna) {
  ^
  ```

- Error: `conf/modules.config:530:1`: If statements cannot be mixed with config statements

  ```nextflow
  if (!params.skip_alignment) {
  ^
  ```

- Error: `conf/modules.config:616:1`: If statements cannot be mixed with config statements

  ```nextflow
  if (!params.skip_alignment && params.aligner == 'star') {
  ^
  ```

- Error: `conf/modules.config:895:1`: If statements cannot be mixed with config statements

  ```nextflow
  if (!params.skip_multiqc) {
  ^
  ```

- Error: `conf/modules.config:912:1`: If statements cannot be mixed with config statements

  ```nextflow
  if (!params.skip_ribotish) {
  ^
  ```

- Error: `conf/modules.config:941:1`: If statements cannot be mixed with config statements

  ```nextflow
  if (!params.skip_ribotricer) {
  ^
  ```

- Error: `conf/modules.config:972:1`: If statements cannot be mixed with config statements

  ```nextflow
  if (!params.skip_ribocode) {
  ^
  ```

- Error: `conf/modules.config:1009:1`: If statements cannot be mixed with config statements

  ```nextflow
  if (!params.skip_ribowaltz) {
  ^
  ```

- Error: `conf/modules.config:1022:1`: If statements cannot be mixed with config statements

  ```nextflow
  if (!params.skip_plastid) {
  ^
  ```

- Error: `conf/modules.config:1064:1`: If statements cannot be mixed with config statements

  ```nextflow
  if (params.contrasts) {
  ^
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

- Error: `modules/nf-core/ribotish/predict/main.nf:41:12`: `para_tis` is not defined

  ```nextflow
          if (para_tis){
             ^^^^^^^^^^
  ```

- Error: `modules/nf-core/ribotricer/detectorfs/main.nf:36:24`: Unexpected input: '\n'

  ```nextflow
          case "forward":
                         ^
  ```

- Error: `modules/nf-core/star/align/main.nf:44:20`: Unexpected input: ','

  ```nextflow
      def reads1 = [], reads2 = []
                     ^
  ```

- Error: `subworkflows/local/prepare_genome/main.nf:124:42`: `fasta` is already declared

  ```nextflow
              ch_fasta.combine(ch_gtf).map{fasta, gtf -> [[:], fasta, gtf]},
                                           ^^^^^
  ```

- Error: `subworkflows/local/prepare_genome/main.nf:124:49`: `gtf` is already declared

  ```nextflow
              ch_fasta.combine(ch_gtf).map{fasta, gtf -> [[:], fasta, gtf]},
                                                  ^^^
  ```

- Error: `subworkflows/local/prepare_genome/main.nf:185:32`: `fasta` is already declared

  ```nextflow
                  .flatMap { id, fasta -> [ [ 'id', id ], [ 'fasta', file(fasta, checkIfExists: true) ] ] } // Flatten entries to be able to groupTuple by a common key
                                 ^^^^^
  ```

- Error: `subworkflows/nf-core/fastq_align_star/main.nf:1:1`: Module could not be parsed: '/home/runner/work/strict-syntax-health/strict-syntax-health/pipelines/riboseq/modules/nf-core/star/align/main.nf'

  ```nextflow
  include { STAR_ALIGN                                                       } from '../../../modules/nf-core/star/align/main'
  ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  ```

- Error: `subworkflows/nf-core/fastq_align_star/main.nf:25:5`: `STAR_ALIGN` is not defined

  ```nextflow
      STAR_ALIGN ( ch_reads, ch_index, ch_gtf, val_star_ignore_sjdbgtf, val_seq_platform, val_seq_center )
      ^^^^^^^^^^
  ```

- Error: `subworkflows/nf-core/fastq_align_star/main.nf:26:35`: `STAR_ALIGN` is not defined

  ```nextflow
      ch_versions = ch_versions.mix(STAR_ALIGN.out.versions.first())
                                    ^^^^^^^^^^
  ```

- Error: `subworkflows/nf-core/fastq_align_star/main.nf:31:38`: `STAR_ALIGN` is not defined

  ```nextflow
      BAM_SORT_STATS_SAMTOOLS_GENOME ( STAR_ALIGN.out.bam, ch_fasta )
                                       ^^^^^^^^^^
  ```

- Error: `subworkflows/nf-core/fastq_align_star/main.nf:41:45`: `STAR_ALIGN` is not defined

  ```nextflow
      BAM_SORT_STATS_SAMTOOLS_TRANSCRIPTOME ( STAR_ALIGN.out.bam_transcript, ch_transcripts_fasta )
                                              ^^^^^^^^^^
  ```

- Error: `subworkflows/nf-core/fastq_align_star/main.nf:46:27`: `STAR_ALIGN` is not defined

  ```nextflow
      orig_bam            = STAR_ALIGN.out.bam                                 // channel: [ val(meta), path(bam)            ]
                            ^^^^^^^^^^
  ```

- Error: `subworkflows/nf-core/fastq_align_star/main.nf:47:27`: `STAR_ALIGN` is not defined

  ```nextflow
      log_final           = STAR_ALIGN.out.log_final                           // channel: [ val(meta), path(log_final)      ]
                            ^^^^^^^^^^
  ```

- Error: `subworkflows/nf-core/fastq_align_star/main.nf:48:27`: `STAR_ALIGN` is not defined

  ```nextflow
      log_out             = STAR_ALIGN.out.log_out                             // channel: [ val(meta), path(log_out)        ]
                            ^^^^^^^^^^
  ```

- Error: `subworkflows/nf-core/fastq_align_star/main.nf:49:27`: `STAR_ALIGN` is not defined

  ```nextflow
      log_progress        = STAR_ALIGN.out.log_progress                        // channel: [ val(meta), path(log_progress)   ]
                            ^^^^^^^^^^
  ```

- Error: `subworkflows/nf-core/fastq_align_star/main.nf:50:27`: `STAR_ALIGN` is not defined

  ```nextflow
      bam_sorted          = STAR_ALIGN.out.bam_sorted                          // channel: [ val(meta), path(bam)            ]
                            ^^^^^^^^^^
  ```

- Error: `subworkflows/nf-core/fastq_align_star/main.nf:51:27`: `STAR_ALIGN` is not defined

  ```nextflow
      fastq               = STAR_ALIGN.out.fastq                               // channel: [ val(meta), path(fastq)          ]
                            ^^^^^^^^^^
  ```

- Error: `subworkflows/nf-core/fastq_align_star/main.nf:52:27`: `STAR_ALIGN` is not defined

  ```nextflow
      tab                 = STAR_ALIGN.out.tab                                 // channel: [ val(meta), path(tab)            ]
                            ^^^^^^^^^^
  ```

- Error: `subworkflows/nf-core/fastq_align_star/main.nf:53:27`: `STAR_ALIGN` is not defined

  ```nextflow
      orig_bam_transcript = STAR_ALIGN.out.bam_transcript                      // channel: [ val(meta), path(bam)            ]
                            ^^^^^^^^^^
  ```

- Error: `subworkflows/nf-core/fastq_fastqc_umitools_trimgalore/main.nf:59:30`: `reads` is already declared

  ```nextflow
                  .map { meta, reads ->
                               ^^^^^
  ```

- Error: `workflows/riboseq/main.nf:34:1`: Module could not be parsed: '/home/runner/work/strict-syntax-health/strict-syntax-health/pipelines/riboseq/modules/nf-core/ribotricer/detectorfs/main.nf'

  ```nextflow
  include { RIBOTRICER_DETECTORFS                                } from '../../modules/nf-core/ribotricer/detectorfs'
  ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  ```

- Error: `workflows/riboseq/main.nf:326:9`: `RIBOTRICER_DETECTORFS` is not defined

  ```nextflow
          RIBOTRICER_DETECTORFS(
          ^^^^^^^^^^^^^^^^^^^^^
  ```

- Error: `workflows/riboseq/main.nf:330:39`: `RIBOTRICER_DETECTORFS` is not defined

  ```nextflow
          ch_versions = ch_versions.mix(RIBOTRICER_DETECTORFS.out.versions)
                                        ^^^^^^^^^^^^^^^^^^^^^
  ```

## :warning: Warnings

- Warning: `conf/modules.config:340:45`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
              saveAs: { params.save_trimmed ? it : null }
                                              ^^
  ```

- Warning: `main.nf:54:19`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_versions = Channel.empty()
                    ^^^^^^^
  ```

- Warning: `main.nf:87:39`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
              .map { checkMaxContigSize(it) }
                                        ^^
  ```

- Warning: `main.nf:93:22`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_samplesheet = Channel.value(file(params.input, checkIfExists: true))
                       ^^^^^^^
  ```

- Warning: `main.nf:95:29`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
          ch_contrasts_file = Channel.value(file(params.contrasts))
                              ^^^^^^^
  ```

- Warning: `main.nf:101:24`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_bowtie2_index = Channel.empty()
                         ^^^^^^^
  ```

- Warning: `modules/nf-core/bbmap/bbsplit/main.nf:116:43`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
      other_ref_names.eachWithIndex { name, index ->
                                            ^^^^^
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

- Warning: `modules/nf-core/custom/catadditionalfasta/main.nf:26:9`: Variable was declared but not used

  ```nextflow
      def prefix = task.ext.prefix ?: "${meta.id}"
          ^^^^^^
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
      def args = task.ext.args ?: ''
          ^^^^
  ```

- Warning: `modules/nf-core/ribocode/gtfupdate/main.nf:32:9`: Variable was declared but not used

  ```nextflow
      def args = task.ext.args ?: ''
          ^^^^
  ```

- Warning: `modules/nf-core/ribocode/metaplots/main.nf:34:9`: Variable was declared but not used

  ```nextflow
      def args = task.ext.args ?: ''
          ^^^^
  ```

- Warning: `modules/nf-core/ribocode/prepare/main.nf:33:9`: Variable was declared but not used

  ```nextflow
      def args = task.ext.args ?: ''
          ^^^^
  ```

- Warning: `modules/nf-core/ribocode/ribocode/main.nf:38:9`: Variable was declared but not used

  ```nextflow
      def args = task.ext.args ?: ''
          ^^^^
  ```

- Warning: `modules/nf-core/ribotish/predict/main.nf:64:9`: Variable was declared but not used

  ```nextflow
      def args = task.ext.args ?: ''
          ^^^^
  ```

- Warning: `modules/nf-core/ribotish/quality/main.nf:43:9`: Variable was declared but not used

  ```nextflow
      def args = task.ext.args ?: ''
          ^^^^
  ```

- Warning: `modules/nf-core/ribotricer/prepareorfs/main.nf:38:9`: Variable was declared but not used

  ```nextflow
      def args = task.ext.args ?: ''
          ^^^^
  ```

- Warning: `modules/nf-core/rsem/preparereference/main.nf:27:30`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          args_list.removeIf { it.contains('--star') }
                               ^^
  ```

- Warning: `modules/nf-core/salmon/quant/main.nf:34:58`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
      meta.single_end ? [reads].flatten().each { reads1 << it } : reads.eachWithIndex { v, ix -> (ix & 1 ? reads2 : reads1) << v }
                                                           ^^
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

- Warning: `modules/nf-core/trimgalore/main.nf:47:31`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          args_list.removeAll { it.toLowerCase().contains('_r2 ') }
                                ^^
  ```

- Warning: `subworkflows/local/fastq_equalise_read_lengths/main.nf:25:19`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_versions = Channel.empty()
                    ^^^^^^^
  ```

- Warning: `subworkflows/local/fastq_equalise_read_lengths/main.nf:69:25`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          .filter { meta, reads -> meta.pair != null }
                          ^^^^^
  ```

- Warning: `subworkflows/local/fastq_equalise_read_lengths/main.nf:70:22`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          .map { meta, reads -> meta.pair }
                       ^^^^^
  ```

- Warning: `subworkflows/local/fastq_equalise_read_lengths/main.nf:77:25`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          .filter { meta, reads, pairs_needed ->
                          ^^^^^
  ```

- Warning: `subworkflows/local/fastq_equalise_read_lengths/main.nf:80:29`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          .map { meta, reads, pairs_needed -> [ meta, reads ] }
                              ^^^^^^^^^^^^
  ```

- Warning: `subworkflows/local/fastq_equalise_read_lengths/main.nf:93:56`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
                  def avg_len_idx = header.findIndexOf { it == 'avg_len' }
                                                         ^^
  ```

- Warning: `subworkflows/local/fastq_equalise_read_lengths/main.nf:104:16`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          .map { pair, meta, reads, riboseq_trim_len ->
                 ^^^^
  ```

- Warning: `subworkflows/local/fastq_equalise_read_lengths/main.nf:133:19`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          .filter { it }  // Remove empty elements
                    ^^
  ```

- Warning: `subworkflows/local/prepare_genome/main.nf:56:19`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_versions = Channel.empty()
                    ^^^^^^^
  ```

- Warning: `subworkflows/local/prepare_genome/main.nf:62:68`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          ch_fasta    = GUNZIP_FASTA ( [ [:], fasta ] ).gunzip.map { it[1] }
                                                                     ^^
  ```

- Warning: `subworkflows/local/prepare_genome/main.nf:65:20`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
          ch_fasta = Channel.value(file(fasta))
                     ^^^^^^^
  ```

- Warning: `subworkflows/local/prepare_genome/main.nf:74:72`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
                  ch_gtf      = GUNZIP_GTF ( [ [:], gtf ] ).gunzip.map { it[1] }
                                                                         ^^
  ```

- Warning: `subworkflows/local/prepare_genome/main.nf:77:26`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
                  ch_gtf = Channel.value(file(gtf))
                           ^^^^^^^
  ```

- Warning: `subworkflows/local/prepare_genome/main.nf:81:72`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
                  ch_gff      = GUNZIP_GFF ( [ [:], gff ] ).gunzip.map { it[1] }
                                                                         ^^
  ```

- Warning: `subworkflows/local/prepare_genome/main.nf:84:26`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
                  ch_gff = Channel.value(file(gff))
                           ^^^^^^^
  ```

- Warning: `subworkflows/local/prepare_genome/main.nf:117:95`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
              ch_add_fasta = GUNZIP_ADDITIONAL_FASTA ( [ [:], additional_fasta ] ).gunzip.map { it[1] }
                                                                                                ^^
  ```

- Warning: `subworkflows/local/prepare_genome/main.nf:120:28`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
              ch_add_fasta = Channel.value(file(additional_fasta))
                             ^^^^^^^
  ```

- Warning: `subworkflows/local/prepare_genome/main.nf:125:36`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
              ch_add_fasta.map{[[:], it]},
                                     ^^
  ```

- Warning: `subworkflows/local/prepare_genome/main.nf:128:63`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          ch_fasta    = CUSTOM_CATADDITIONALFASTA.out.fasta.map{it[1]}.first()
                                                                ^^
  ```

- Warning: `subworkflows/local/prepare_genome/main.nf:129:61`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          ch_gtf      = CUSTOM_CATADDITIONALFASTA.out.gtf.map{it[1]}.first()
                                                              ^^
  ```

- Warning: `subworkflows/local/prepare_genome/main.nf:138:102`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
              ch_transcript_fasta = GUNZIP_TRANSCRIPT_FASTA ( [ [:], transcript_fasta ] ).gunzip.map { it[1] }
                                                                                                       ^^
  ```

- Warning: `subworkflows/local/prepare_genome/main.nf:141:35`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
              ch_transcript_fasta = Channel.value(file(transcript_fasta))
                                    ^^^^^^^
  ```

- Warning: `subworkflows/local/prepare_genome/main.nf:156:50`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
      CUSTOM_GETCHROMSIZES ( ch_fasta.map { [ [:], it ] } )
                                                   ^^
  ```

- Warning: `subworkflows/local/prepare_genome/main.nf:157:57`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
      ch_fai         = CUSTOM_GETCHROMSIZES.out.fai.map { it[1] }
                                                          ^^
  ```

- Warning: `subworkflows/local/prepare_genome/main.nf:158:59`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
      ch_chrom_sizes = CUSTOM_GETCHROMSIZES.out.sizes.map { it[1] }
                                                            ^^
  ```

- Warning: `subworkflows/local/prepare_genome/main.nf:172:24`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_bbsplit_index = Channel.empty()
                         ^^^^^^^
  ```

- Warning: `subworkflows/local/prepare_genome/main.nf:176:95`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
                  ch_bbsplit_index = UNTAR_BBSPLIT_INDEX ( [ [:], bbsplit_index ] ).untar.map { it[1] }
                                                                                                ^^
  ```

- Warning: `subworkflows/local/prepare_genome/main.nf:179:36`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
                  ch_bbsplit_index = Channel.value(file(bbsplit_index))
                                     ^^^^^^^
  ```

- Warning: `subworkflows/local/prepare_genome/main.nf:182:13`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
              Channel
              ^^^^^^^
  ```

- Warning: `subworkflows/local/prepare_genome/main.nf:188:30`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
                  .collect { [ it ] } // Collect entries as a list to pass as "tuple val(short_names), path(path_to_fasta)" to module
                               ^^
  ```

- Warning: `subworkflows/local/prepare_genome/main.nf:199:26`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_sortmerna_index = Channel.empty()
                           ^^^^^^^
  ```

- Warning: `subworkflows/local/prepare_genome/main.nf:200:22`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_rrna_fastas = Channel.empty()
                       ^^^^^^^
  ```

- Warning: `subworkflows/local/prepare_genome/main.nf:205:26`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
          ch_rrna_fastas = Channel.from(ribo_db.readLines())
                           ^^^^^^^
  ```

- Warning: `subworkflows/local/prepare_genome/main.nf:213:101`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
                  ch_sortmerna_index = UNTAR_SORTMERNA_INDEX ( [ [:], sortmerna_index ] ).untar.map { it[1] }
                                                                                                      ^^
  ```

- Warning: `subworkflows/local/prepare_genome/main.nf:216:38`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
                  ch_sortmerna_index = Channel.value(file(sortmerna_index))
                                       ^^^^^^^
  ```

- Warning: `subworkflows/local/prepare_genome/main.nf:220:17`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
                  Channel.of([ [],[] ]),
                  ^^^^^^^
  ```

- Warning: `subworkflows/local/prepare_genome/main.nf:221:63`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
                  ch_rrna_fastas.collect().map { [ 'rrna_refs', it ] },
                                                                ^^
  ```

- Warning: `subworkflows/local/prepare_genome/main.nf:222:17`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
                  Channel.of([ [],[] ])
                  ^^^^^^^
  ```

- Warning: `subworkflows/local/prepare_genome/main.nf:232:21`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_star_index = Channel.empty()
                      ^^^^^^^
  ```

- Warning: `subworkflows/local/prepare_genome/main.nf:236:86`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
                  ch_star_index = UNTAR_STAR_INDEX ( [ [:], star_index ] ).untar.map { it[1] }
                                                                                       ^^
  ```

- Warning: `subworkflows/local/prepare_genome/main.nf:239:33`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
                  ch_star_index = Channel.value(file(star_index))
                                  ^^^^^^^
  ```

- Warning: `subworkflows/local/prepare_genome/main.nf:253:77`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
                  ch_star_index = STAR_GENOMEGENERATE ( ch_fasta.map { [ [:], it ] }, ch_gtf.map { [ [:], it ] } ).index.map { it[1] }
                                                                              ^^
  ```

- Warning: `subworkflows/local/prepare_genome/main.nf:253:105`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
                  ch_star_index = STAR_GENOMEGENERATE ( ch_fasta.map { [ [:], it ] }, ch_gtf.map { [ [:], it ] } ).index.map { it[1] }
                                                                                                          ^^
  ```

- Warning: `subworkflows/local/prepare_genome/main.nf:253:126`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
                  ch_star_index = STAR_GENOMEGENERATE ( ch_fasta.map { [ [:], it ] }, ch_gtf.map { [ [:], it ] } ).index.map { it[1] }
                                                                                                                               ^^
  ```

- Warning: `subworkflows/local/prepare_genome/main.nf:262:23`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_salmon_index = Channel.empty()
                        ^^^^^^^
  ```

- Warning: `subworkflows/local/prepare_genome/main.nf:265:88`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
              ch_salmon_index = UNTAR_SALMON_INDEX ( [ [:], salmon_index ] ).untar.map { it[1] }
                                                                                         ^^
  ```

- Warning: `subworkflows/local/prepare_genome/main.nf:268:31`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
              ch_salmon_index = Channel.value(file(salmon_index))
                                ^^^^^^^
  ```

- Warning: `subworkflows/local/prepare_genome/main.nf:280:26`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_salmon_index_te = Channel.empty()
                           ^^^^^^^
  ```

- Warning: `subworkflows/local/utils_nfcore_riboseq_pipeline/main.nf:32:5`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
      monochrome_logs   // boolean: Do not use coloured log outputs
      ^^^^^^^^^^^^^^^
  ```

- Warning: `subworkflows/local/utils_nfcore_riboseq_pipeline/main.nf:35:5`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
      input             //  string: Path to input samplesheet
      ^^^^^
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

- Warning: `subworkflows/nf-core/bam_dedup_umi/main.nf:114:14`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          .map{it[1]}
               ^^
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

- Warning: `subworkflows/nf-core/fastq_align_star/main.nf:20:19`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

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

- Warning: `workflows/riboseq/main.nf:75:5`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
      ch_fai              // channel: path(genome.fai)
      ^^^^^^
  ```

- Warning: `workflows/riboseq/main.nf:76:5`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
      ch_chrom_sizes      // channel: path(genome.sizes)
      ^^^^^^^^^^^^^^
  ```

- Warning: `workflows/riboseq/main.nf:99:22`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
          ch_ribo_db = Channel.empty()
                       ^^^^^^^
  ```

- Warning: `workflows/riboseq/main.nf:114:24`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_multiqc_files = Channel.empty()
                         ^^^^^^^
  ```

- Warning: `workflows/riboseq/main.nf:119:5`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      Channel
      ^^^^^^^
  ```

- Warning: `workflows/riboseq/main.nf:131:38`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
              validateInputSamplesheet(it)
                                       ^^
  ```

- Warning: `workflows/riboseq/main.nf:208:103`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          ch_multiqc_files = ch_multiqc_files.mix(FASTQ_EQUALISE_READ_LENGTHS.out.riboseq_stats.collect{it[1]})
                                                                                                        ^^
  ```

- Warning: `workflows/riboseq/main.nf:218:36`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          ch_star_index.map { [ [:], it ] },
                                     ^^
  ```

- Warning: `workflows/riboseq/main.nf:219:29`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          ch_gtf.map { [ [:], it ] },
                              ^^
  ```

- Warning: `workflows/riboseq/main.nf:223:31`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          ch_fasta.map { [ [:], it ] },
                                ^^
  ```

- Warning: `workflows/riboseq/main.nf:224:42`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          ch_transcript_fasta.map { [ [:], it ] }
                                           ^^
  ```

- Warning: `workflows/riboseq/main.nf:230:5`: Variable was declared but not used

  ```nextflow
      ch_transcriptome_bai       = FASTQ_ALIGN_STAR.out.bai_transcript
      ^^^^^^^^^^^^^^^^^^^^
  ```

- Warning: `workflows/riboseq/main.nf:234:49`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          .mix(FASTQ_ALIGN_STAR.out.stats.collect{it[1]})
                                                  ^^
  ```

- Warning: `workflows/riboseq/main.nf:235:52`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          .mix(FASTQ_ALIGN_STAR.out.flagstat.collect{it[1]})
                                                     ^^
  ```

- Warning: `workflows/riboseq/main.nf:236:52`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          .mix(FASTQ_ALIGN_STAR.out.idxstats.collect{it[1]})
                                                     ^^
  ```

- Warning: `workflows/riboseq/main.nf:237:53`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          .mix(FASTQ_ALIGN_STAR.out.log_final.collect{it[1]})
                                                      ^^
  ```

- Warning: `workflows/riboseq/main.nf:247:35`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
              ch_fasta.map { [ [:], it ] },
                                    ^^
  ```

- Warning: `workflows/riboseq/main.nf:252:46`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
              ch_transcript_fasta.map { [ [:], it ] }
                                               ^^
  ```

- Warning: `workflows/riboseq/main.nf:287:33`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
              ch_gtf.map { [ [:], it ] }.first()
                                  ^^
  ```

- Warning: `workflows/riboseq/main.nf:290:99`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          ch_multiqc_files = ch_multiqc_files.mix(RIBOTISH_QUALITY_RIBOSEQ.out.distribution.collect{it[1]})
                                                                                                    ^^
  ```

- Warning: `workflows/riboseq/main.nf:310:45`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
              ribotish_predict_inputs.bam.map{meta, bam, bai -> [[id:'allsamples'], bam, bai]}.groupTuple(),
                                              ^^^^
  ```

- Warning: `workflows/riboseq/main.nf:314:48`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
              ribotish_predict_inputs.offset.map{meta, offset -> [[id:'allsamples'], offset]}.groupTuple(),
                                                 ^^^^
  ```

- Warning: `workflows/riboseq/main.nf:344:33`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
              ch_gtf.map { [ [:], it ] }.first()
                                  ^^
  ```

- Warning: `workflows/riboseq/main.nf:349:35`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
              ch_fasta.map { [ [:], it ] }.first(),
                                    ^^
  ```

- Warning: `workflows/riboseq/main.nf:365:49`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
              ch_ribocode_inputs.map { meta, bam, config -> [ meta, bam ] },
                                                  ^^^^^^
  ```

- Warning: `workflows/riboseq/main.nf:367:44`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
              ch_ribocode_inputs.map { meta, bam, config -> [ meta, config ] }
                                             ^^^
  ```

- Warning: `workflows/riboseq/main.nf:391:33`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
              ch_gtf.map { [ [:], it ] },
                                  ^^
  ```

- Warning: `workflows/riboseq/main.nf:392:35`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
              ch_fasta.map { [ [:], it ] })
                                    ^^
  ```

- Warning: `workflows/riboseq/main.nf:399:55`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          PLASTID_METAGENE_GENERATE(ch_gtf.map { [ [:], it ] })
                                                        ^^
  ```

- Warning: `workflows/riboseq/main.nf:421:37`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          ch_samplesheet.map { [ [:], it ] },
                                      ^^
  ```

- Warning: `workflows/riboseq/main.nf:435:86`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
      ch_multiqc_files = ch_multiqc_files.mix(QUANTIFY_STAR_SALMON.out.multiqc.collect{it[1]}.ifEmpty([]))
                                                                                       ^^
  ```

- Warning: `workflows/riboseq/main.nf:447:29`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
              .filter { meta, reads -> meta.sample_type in ['riboseq', 'rnaseq'] }
                              ^^^^^
  ```

- Warning: `workflows/riboseq/main.nf:450:41`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
              ch_samplesheet.map { [ [:], it ] },
                                          ^^
  ```

- Warning: `workflows/riboseq/main.nf:464:88`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          ch_multiqc_files = ch_multiqc_files.mix(QUANTIFY_PSEUDO_TE.out.multiqc.collect{it[1]}.ifEmpty([]))
                                                                                         ^^
  ```

- Warning: `workflows/riboseq/main.nf:476:19`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
              .map{[it, it.variable, it.reference, it.target]}
                    ^^
  ```

- Warning: `workflows/riboseq/main.nf:476:23`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
              .map{[it, it.variable, it.reference, it.target]}
                        ^^
  ```

- Warning: `workflows/riboseq/main.nf:476:36`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
              .map{[it, it.variable, it.reference, it.target]}
                                     ^^
  ```

- Warning: `workflows/riboseq/main.nf:476:50`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
              .map{[it, it.variable, it.reference, it.target]}
                                                   ^^
  ```

- Warning: `workflows/riboseq/main.nf:480:19`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
              .map{[it[0], it[2], it[1]]}
                    ^^
  ```

- Warning: `workflows/riboseq/main.nf:480:26`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
              .map{[it[0], it[2], it[1]]}
                           ^^
  ```

- Warning: `workflows/riboseq/main.nf:480:33`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
              .map{[it[0], it[2], it[1]]}
                                  ^^
  ```

- Warning: `workflows/riboseq/main.nf:503:38`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
      ch_versions = ch_versions.filter{it != null}
                                       ^^
  ```

- Warning: `workflows/riboseq/main.nf:513:49`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
          ch_multiqc_config                     = Channel.fromPath("$projectDir/assets/multiqc_config.yml", checkIfExists: true)
                                                  ^^^^^^^
  ```

- Warning: `workflows/riboseq/main.nf:514:73`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
          ch_multiqc_custom_config              = params.multiqc_config ? Channel.fromPath(params.multiqc_config, checkIfExists: true) : Channel.empty()
                                                                          ^^^^^^^
  ```

- Warning: `workflows/riboseq/main.nf:514:136`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
          ch_multiqc_custom_config              = params.multiqc_config ? Channel.fromPath(params.multiqc_config, checkIfExists: true) : Channel.empty()
                                                                                                                                         ^^^^^^^
  ```

- Warning: `workflows/riboseq/main.nf:515:71`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
          ch_multiqc_logo                       = params.multiqc_logo ? Channel.fromPath(params.multiqc_logo, checkIfExists: true) : Channel.empty()
                                                                        ^^^^^^^
  ```

- Warning: `workflows/riboseq/main.nf:515:132`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
          ch_multiqc_logo                       = params.multiqc_logo ? Channel.fromPath(params.multiqc_logo, checkIfExists: true) : Channel.empty()
                                                                                                                                     ^^^^^^^
  ```

- Warning: `workflows/riboseq/main.nf:517:49`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
          ch_workflow_summary                   = Channel.value(paramsSummaryMultiqc(summary_params))
                                                  ^^^^^^^
  ```

- Warning: `workflows/riboseq/main.nf:519:49`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
          ch_methods_description                = Channel.value(methodsDescriptionText(ch_multiqc_custom_methods_description))
                                                  ^^^^^^^
  ```

- Warning: `workflows/riboseq/main.nf:550:29`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
          ch_multiqc_report = Channel.empty()
                              ^^^^^^^
  ```
