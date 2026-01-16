# Nextflow lint results

- Generated: 2026-01-16T10:22:24.001433080Z
- Nextflow version: 25.12.0-edge
- Summary: 40 errors, 176 warnings

## :x: Errors

- Error: `modules/nf-core/bbmap/bbsplit/main.nf:41:43`: `index` is already declared

  ```nextflow
      other_ref_names.eachWithIndex { name, index ->
                                            ^^^^^
  ```

- Error: `modules/nf-core/bbmap/bbsplit/main.nf:110:43`: `index` is already declared

  ```nextflow
      other_ref_names.eachWithIndex { name, index ->
                                            ^^^^^
  ```

- Error: `nextflow.config:378:31`: `manifest` is not defined

  ```nextflow
  \033[0;35m  nf-core/lncpipe ${manifest.version}\033[0m
                                ^^^^^^^^
  ```

- Error: `nextflow.config:381:26`: `manifest` is not defined

  ```nextflow
          afterText = """${manifest.doi ? "\n* The pipeline\n" : ""}${manifest.doi.tokenize(",").collect { "    https://doi.org/${it.trim().replace('https://doi.org/','')}"}.join("\n")}${manifest.doi ? "\n" : ""}
                           ^^^^^^^^
  ```

- Error: `nextflow.config:381:69`: `manifest` is not defined

  ```nextflow
          afterText = """${manifest.doi ? "\n* The pipeline\n" : ""}${manifest.doi.tokenize(",").collect { "    https://doi.org/${it.trim().replace('https://doi.org/','')}"}.join("\n")}${manifest.doi ? "\n" : ""}
                                                                      ^^^^^^^^
  ```

- Error: `nextflow.config:381:186`: `manifest` is not defined

  ```nextflow
          afterText = """${manifest.doi ? "\n* The pipeline\n" : ""}${manifest.doi.tokenize(",").collect { "    https://doi.org/${it.trim().replace('https://doi.org/','')}"}.join("\n")}${manifest.doi ? "\n" : ""}
                                                                                                                                                                                           ^^^^^^^^
  ```

- Error: `nextflow.config:390:22`: `validation` is not defined

  ```nextflow
          beforeText = validation.help.beforeText
                       ^^^^^^^^^^
  ```

- Error: `nextflow.config:391:21`: `validation` is not defined

  ```nextflow
          afterText = validation.help.afterText
                      ^^^^^^^^^^
  ```

- Error: `subworkflows/local/prepare_genome/main.nf:140:44`: `fasta` is already declared

  ```nextflow
              ch_fasta.combine(ch_gtf).map { fasta, gtf -> [ [:], fasta, gtf ] },
                                             ^^^^^
  ```

- Error: `subworkflows/local/prepare_genome/main.nf:140:51`: `gtf` is already declared

  ```nextflow
              ch_fasta.combine(ch_gtf).map { fasta, gtf -> [ [:], fasta, gtf ] },
                                                    ^^^
  ```

- Error: `subworkflows/local/prepare_genome/main.nf:217:32`: `fasta` is already declared

  ```nextflow
                  .flatMap { id, fasta -> [ [ 'id', id ], [ 'fasta', file(fasta, checkIfExists: true) ] ] } // Flatten entries to be able to groupTuple by a common key
                                 ^^^^^
  ```

- Error: `subworkflows/local/prepare_genome/nextflow.config:103:1`: If statements cannot be mixed with config statements

  ```nextflow
  if (!params.skip_bbsplit && params.bbsplit_fasta_list) {
  ^
  ```

- Error: `subworkflows/local/prepare_genome/nextflow.config:116:1`: If statements cannot be mixed with config statements

  ```nextflow
  if (params.remove_ribo_rna && params.ribo_database_manifest) {
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

- Error: `subworkflows/nf-core/fastq_qc_trim_filter_setstrandedness/main.nf:345:100`: Unexpected input: '='

  ```nextflow
                  def salmon_strand_analysis = getSalmonInferredStrandedness(json, stranded_threshold=stranded_threshold, unstranded_threshold=unstranded_threshold)
                                                                                                     ^
  ```

- Error: `workflows/lncpipe.nf:17:1`: Module could not be parsed: '/home/runner/work/strict-syntax-health/strict-syntax-health/pipelines/lncpipe/subworkflows/nf-core/fastq_qc_trim_filter_setstrandedness/main.nf'

  ```nextflow
  include { FASTQ_QC_TRIM_FILTER_SETSTRANDEDNESS  } from '../subworkflows/nf-core/fastq_qc_trim_filter_setstrandedness'
  ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  ```

- Error: `workflows/lncpipe.nf:66:5`: `FASTQ_QC_TRIM_FILTER_SETSTRANDEDNESS` is not defined

  ```nextflow
      FASTQ_QC_TRIM_FILTER_SETSTRANDEDNESS (
      ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  ```

- Error: `workflows/lncpipe.nf:93:62`: `FASTQ_QC_TRIM_FILTER_SETSTRANDEDNESS` is not defined

  ```nextflow
      ch_multiqc_files                  = ch_multiqc_files.mix(FASTQ_QC_TRIM_FILTER_SETSTRANDEDNESS.out.multiqc_files)
                                                               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  ```

- Error: `workflows/lncpipe.nf:94:57`: `FASTQ_QC_TRIM_FILTER_SETSTRANDEDNESS` is not defined

  ```nextflow
      ch_versions                       = ch_versions.mix(FASTQ_QC_TRIM_FILTER_SETSTRANDEDNESS.out.versions)
                                                          ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  ```

- Error: `workflows/lncpipe.nf:95:41`: `FASTQ_QC_TRIM_FILTER_SETSTRANDEDNESS` is not defined

  ```nextflow
      ch_strand_inferred_filtered_fastq = FASTQ_QC_TRIM_FILTER_SETSTRANDEDNESS.out.reads
                                          ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  ```

- Error: `workflows/lncpipe.nf:96:41`: `FASTQ_QC_TRIM_FILTER_SETSTRANDEDNESS` is not defined

  ```nextflow
      ch_trim_read_count                = FASTQ_QC_TRIM_FILTER_SETSTRANDEDNESS.out.trim_read_count
                                          ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  ```

- Error: `workflows/lncpipe.nf:128:13`: `FASTQ_QC_TRIM_FILTER_SETSTRANDEDNESS` is not defined

  ```nextflow
              FASTQ_QC_TRIM_FILTER_SETSTRANDEDNESS.out.reads,
              ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  ```

- Error: `workflows/lncpipe.nf:248:50`: `getStarPercentMapped` is not defined

  ```nextflow
              .map { meta, align_log -> [ meta ] + getStarPercentMapped(params, align_log) }
                                                   ^^^^^^^^^^^^^^^^^^^^
  ```

- Error: `workflows/lncpipe.nf:273:21`: `sample_status_header_multiqc` is not defined

  ```nextflow
                      sample_status_header_multiqc.text + multiqcTsvFromList(tsv_data, header)
                      ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  ```

- Error: `workflows/lncpipe.nf:273:57`: `multiqcTsvFromList` is not defined

  ```nextflow
                      sample_status_header_multiqc.text + multiqcTsvFromList(tsv_data, header)
                                                          ^^^^^^^^^^^^^^^^^^
  ```

## :warning: Warnings

- Warning: `main.nf:62:19`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_versions = Channel.empty()
                    ^^^^^^^
  ```

- Warning: `main.nf:101:39`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
              .map { checkMaxContigSize(it) }
                                        ^^
  ```

- Warning: `main.nf:107:5`: Variable was declared but not used

  ```nextflow
      ch_samplesheet = Channel.value(file(params.input, checkIfExists: true))
      ^^^^^^^^^^^^^^
  ```

- Warning: `main.nf:107:22`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_samplesheet = Channel.value(file(params.input, checkIfExists: true))
                       ^^^^^^^
  ```

- Warning: `modules/nf-core/bbmap/bbsplit/main.nf:110:43`: Parameter was not used -- prefix with `_` to suppress warning

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

- Warning: `modules/nf-core/hisat2/extractsplicesites/main.nf:21:9`: Variable was declared but not used

  ```nextflow
      def args = task.ext.args ?: ''
          ^^^^
  ```

- Warning: `modules/nf-core/rsem/preparereference/main.nf:27:30`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          args_list.removeIf { it.contains('--star') }
                               ^^
  ```

- Warning: `modules/nf-core/salmon/quant/main.nf:34:56`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
      meta.single_end ? [reads].flatten().each{reads1 << it} : reads.eachWithIndex{ v, ix -> ( ix & 1 ? reads2 : reads1) << v }
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

- Warning: `modules/nf-core/star/align/main.nf:46:56`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
      meta.single_end ? [reads].flatten().each{reads1 << it} : reads.eachWithIndex{ v, ix -> ( ix & 1 ? reads2 : reads1) << v }
                                                         ^^
  ```

- Warning: `modules/nf-core/trimgalore/main.nf:47:31`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          args_list.removeAll { it.toLowerCase().contains('_r2 ') }
                                ^^
  ```

- Warning: `nextflow.config:381:129`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          afterText = """${manifest.doi ? "\n* The pipeline\n" : ""}${manifest.doi.tokenize(",").collect { "    https://doi.org/${it.trim().replace('https://doi.org/','')}"}.join("\n")}${manifest.doi ? "\n" : ""}
                                                                                                                                  ^^
  ```

- Warning: `subworkflows/local/prepare_genome/main.nf:68:19`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_versions = Channel.empty()
                    ^^^^^^^
  ```

- Warning: `subworkflows/local/prepare_genome/main.nf:74:95`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          ch_fasta    = GUNZIP_FASTA ( [ [:], file(fasta, checkIfExists: true) ] ).gunzip.map { it[1] }
                                                                                                ^^
  ```

- Warning: `subworkflows/local/prepare_genome/main.nf:77:20`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
          ch_fasta = Channel.value(file(fasta, checkIfExists: true))
                     ^^^^^^^
  ```

- Warning: `subworkflows/local/prepare_genome/main.nf:86:99`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
                  ch_gtf      = GUNZIP_GTF ( [ [:], file(gtf, checkIfExists: true) ] ).gunzip.map { it[1] }
                                                                                                    ^^
  ```

- Warning: `subworkflows/local/prepare_genome/main.nf:89:26`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
                  ch_gtf = Channel.value(file(gtf, checkIfExists: true))
                           ^^^^^^^
  ```

- Warning: `subworkflows/local/prepare_genome/main.nf:96:26`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
                  ch_gff = Channel.value(file(gff, checkIfExists: true)).map { [ [:], it ] }
                           ^^^^^^^
  ```

- Warning: `subworkflows/local/prepare_genome/main.nf:96:85`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
                  ch_gff = Channel.value(file(gff, checkIfExists: true)).map { [ [:], it ] }
                                                                                      ^^
  ```

- Warning: `subworkflows/local/prepare_genome/main.nf:98:60`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
              ch_gtf      = GFFREAD ( ch_gff, [] ).gtf.map { it[1] }
                                                             ^^
  ```

- Warning: `subworkflows/local/prepare_genome/main.nf:133:122`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
              ch_add_fasta = GUNZIP_ADDITIONAL_FASTA ( [ [:], file(additional_fasta, checkIfExists: true) ] ).gunzip.map { it[1] }
                                                                                                                           ^^
  ```

- Warning: `subworkflows/local/prepare_genome/main.nf:136:28`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
              ch_add_fasta = Channel.value(file(additional_fasta, checkIfExists: true))
                             ^^^^^^^
  ```

- Warning: `subworkflows/local/prepare_genome/main.nf:141:39`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
              ch_add_fasta.map { [ [:], it ] },
                                        ^^
  ```

- Warning: `subworkflows/local/prepare_genome/main.nf:144:65`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          ch_fasta    = CUSTOM_CATADDITIONALFASTA.out.fasta.map { it[1] }.first()
                                                                  ^^
  ```

- Warning: `subworkflows/local/prepare_genome/main.nf:145:63`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          ch_gtf      = CUSTOM_CATADDITIONALFASTA.out.gtf.map { it[1] }.first()
                                                                ^^
  ```

- Warning: `subworkflows/local/prepare_genome/main.nf:154:105`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
              ch_gene_bed = GUNZIP_GENE_BED ( [ [:], file(gene_bed, checkIfExists: true) ] ).gunzip.map { it[1] }
                                                                                                          ^^
  ```

- Warning: `subworkflows/local/prepare_genome/main.nf:157:27`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
              ch_gene_bed = Channel.value(file(gene_bed, checkIfExists: true))
                            ^^^^^^^
  ```

- Warning: `subworkflows/local/prepare_genome/main.nf:169:129`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
              ch_transcript_fasta = GUNZIP_TRANSCRIPT_FASTA ( [ [:], file(transcript_fasta, checkIfExists: true) ] ).gunzip.map { it[1] }
                                                                                                                                  ^^
  ```

- Warning: `subworkflows/local/prepare_genome/main.nf:172:35`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
              ch_transcript_fasta = Channel.value(file(transcript_fasta, checkIfExists: true))
                                    ^^^^^^^
  ```

- Warning: `subworkflows/local/prepare_genome/main.nf:187:50`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
      CUSTOM_GETCHROMSIZES ( ch_fasta.map { [ [:], it ] } )
                                                   ^^
  ```

- Warning: `subworkflows/local/prepare_genome/main.nf:188:57`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
      ch_fai         = CUSTOM_GETCHROMSIZES.out.fai.map { it[1] }
                                                          ^^
  ```

- Warning: `subworkflows/local/prepare_genome/main.nf:189:59`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
      ch_chrom_sizes = CUSTOM_GETCHROMSIZES.out.sizes.map { it[1] }
                                                            ^^
  ```

- Warning: `subworkflows/local/prepare_genome/main.nf:204:24`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_bbsplit_index = Channel.empty()
                         ^^^^^^^
  ```

- Warning: `subworkflows/local/prepare_genome/main.nf:208:95`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
                  ch_bbsplit_index = UNTAR_BBSPLIT_INDEX ( [ [:], bbsplit_index ] ).untar.map { it[1] }
                                                                                                ^^
  ```

- Warning: `subworkflows/local/prepare_genome/main.nf:211:36`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
                  ch_bbsplit_index = Channel.value(file(bbsplit_index))
                                     ^^^^^^^
  ```

- Warning: `subworkflows/local/prepare_genome/main.nf:214:13`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
              Channel
              ^^^^^^^
  ```

- Warning: `subworkflows/local/prepare_genome/main.nf:220:30`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
                  .collect { [ it ] } // Collect entries as a list to pass as "tuple val(short_names), path(path_to_fasta)" to module
                               ^^
  ```

- Warning: `subworkflows/local/prepare_genome/main.nf:231:26`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_sortmerna_index = Channel.empty()
                           ^^^^^^^
  ```

- Warning: `subworkflows/local/prepare_genome/main.nf:232:22`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_rrna_fastas = Channel.empty()
                       ^^^^^^^
  ```

- Warning: `subworkflows/local/prepare_genome/main.nf:238:26`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
          ch_rrna_fastas = Channel.from(ribo_db.readLines())
                           ^^^^^^^
  ```

- Warning: `subworkflows/local/prepare_genome/main.nf:243:101`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
                  ch_sortmerna_index = UNTAR_SORTMERNA_INDEX ( [ [:], sortmerna_index ] ).untar.map { it[1] }
                                                                                                      ^^
  ```

- Warning: `subworkflows/local/prepare_genome/main.nf:246:38`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
                  ch_sortmerna_index = Channel.value([[:], file(sortmerna_index)])
                                       ^^^^^^^
  ```

- Warning: `subworkflows/local/prepare_genome/main.nf:251:17`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
                  Channel.of([ [],[] ]),
                  ^^^^^^^
  ```

- Warning: `subworkflows/local/prepare_genome/main.nf:252:63`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
                  ch_rrna_fastas.collect().map { [ 'rrna_refs', it ] },
                                                                ^^
  ```

- Warning: `subworkflows/local/prepare_genome/main.nf:253:17`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
                  Channel.of([ [],[] ])
                  ^^^^^^^
  ```

- Warning: `subworkflows/local/prepare_genome/main.nf:263:21`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_star_index = Channel.empty()
                      ^^^^^^^
  ```

- Warning: `subworkflows/local/prepare_genome/main.nf:267:86`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
                  ch_star_index = UNTAR_STAR_INDEX ( [ [:], star_index ] ).untar.map { it[1] }
                                                                                       ^^
  ```

- Warning: `subworkflows/local/prepare_genome/main.nf:270:33`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
                  ch_star_index = Channel.value(file(star_index))
                                  ^^^^^^^
  ```

- Warning: `subworkflows/local/prepare_genome/main.nf:284:77`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
                  ch_star_index = STAR_GENOMEGENERATE ( ch_fasta.map { [ [:], it ] }, ch_gtf.map { [ [:], it ] } ).index.map { it[1] }
                                                                              ^^
  ```

- Warning: `subworkflows/local/prepare_genome/main.nf:284:105`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
                  ch_star_index = STAR_GENOMEGENERATE ( ch_fasta.map { [ [:], it ] }, ch_gtf.map { [ [:], it ] } ).index.map { it[1] }
                                                                                                          ^^
  ```

- Warning: `subworkflows/local/prepare_genome/main.nf:284:126`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
                  ch_star_index = STAR_GENOMEGENERATE ( ch_fasta.map { [ [:], it ] }, ch_gtf.map { [ [:], it ] } ).index.map { it[1] }
                                                                                                                               ^^
  ```

- Warning: `subworkflows/local/prepare_genome/main.nf:293:21`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_rsem_index = Channel.empty()
                      ^^^^^^^
  ```

- Warning: `subworkflows/local/prepare_genome/main.nf:297:86`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
                  ch_rsem_index = UNTAR_RSEM_INDEX ( [ [:], rsem_index ] ).untar.map { it[1] }
                                                                                       ^^
  ```

- Warning: `subworkflows/local/prepare_genome/main.nf:300:33`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
                  ch_rsem_index = Channel.value(file(rsem_index))
                                  ^^^^^^^
  ```

- Warning: `subworkflows/local/prepare_genome/main.nf:311:23`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_splicesites  = Channel.empty()
                        ^^^^^^^
  ```

- Warning: `subworkflows/local/prepare_genome/main.nf:312:23`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_hisat2_index = Channel.empty()
                        ^^^^^^^
  ```

- Warning: `subworkflows/local/prepare_genome/main.nf:315:78`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
              ch_splicesites = HISAT2_EXTRACTSPLICESITES ( ch_gtf.map { [ [:], it ] } ).txt.map { it[1] }
                                                                               ^^
  ```

- Warning: `subworkflows/local/prepare_genome/main.nf:315:97`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
              ch_splicesites = HISAT2_EXTRACTSPLICESITES ( ch_gtf.map { [ [:], it ] } ).txt.map { it[1] }
                                                                                                  ^^
  ```

- Warning: `subworkflows/local/prepare_genome/main.nf:318:30`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
              ch_splicesites = Channel.value(file(splicesites))
                               ^^^^^^^
  ```

- Warning: `subworkflows/local/prepare_genome/main.nf:322:92`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
                  ch_hisat2_index = UNTAR_HISAT2_INDEX ( [ [:], hisat2_index ] ).untar.map { it[1] }
                                                                                             ^^
  ```

- Warning: `subworkflows/local/prepare_genome/main.nf:325:35`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
                  ch_hisat2_index = Channel.value(file(hisat2_index))
                                    ^^^^^^^
  ```

- Warning: `subworkflows/local/prepare_genome/main.nf:328:68`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
              ch_hisat2_index = HISAT2_BUILD ( ch_fasta.map { [ [:], it ] }, ch_gtf.map { [ [:], it ] }, ch_splicesites.map { [ [:], it ] } ).index.map { it[1] }
                                                                     ^^
  ```

- Warning: `subworkflows/local/prepare_genome/main.nf:328:96`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
              ch_hisat2_index = HISAT2_BUILD ( ch_fasta.map { [ [:], it ] }, ch_gtf.map { [ [:], it ] }, ch_splicesites.map { [ [:], it ] } ).index.map { it[1] }
                                                                                                 ^^
  ```

- Warning: `subworkflows/local/prepare_genome/main.nf:328:132`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
              ch_hisat2_index = HISAT2_BUILD ( ch_fasta.map { [ [:], it ] }, ch_gtf.map { [ [:], it ] }, ch_splicesites.map { [ [:], it ] } ).index.map { it[1] }
                                                                                                                                     ^^
  ```

- Warning: `subworkflows/local/prepare_genome/main.nf:328:153`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
              ch_hisat2_index = HISAT2_BUILD ( ch_fasta.map { [ [:], it ] }, ch_gtf.map { [ [:], it ] }, ch_splicesites.map { [ [:], it ] } ).index.map { it[1] }
                                                                                                                                                          ^^
  ```

- Warning: `subworkflows/local/prepare_genome/main.nf:336:23`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_salmon_index = Channel.empty()
                        ^^^^^^^
  ```

- Warning: `subworkflows/local/prepare_genome/main.nf:339:88`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
              ch_salmon_index = UNTAR_SALMON_INDEX ( [ [:], salmon_index ] ).untar.map { it[1] }
                                                                                         ^^
  ```

- Warning: `subworkflows/local/prepare_genome/main.nf:342:31`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
              ch_salmon_index = Channel.value(file(salmon_index))
                                ^^^^^^^
  ```

- Warning: `subworkflows/local/prepare_genome/main.nf:354:25`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_kallisto_index = Channel.empty()
                          ^^^^^^^
  ```

- Warning: `subworkflows/local/prepare_genome/main.nf:360:33`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
              ch_kallisto_index = Channel.value([[:], file(kallisto_index)])
                                  ^^^^^^^
  ```

- Warning: `subworkflows/local/prepare_genome/main.nf:364:83`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
              ch_kallisto_index = KALLISTO_INDEX ( ch_transcript_fasta.map { [ [:], it] } ).index
                                                                                    ^^
  ```

- Warning: `subworkflows/local/stringtie/main.nf:11:23`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
          ch_versions = Channel.empty()
                        ^^^^^^^
  ```

- Warning: `subworkflows/local/stringtie/main.nf:12:28`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
          ch_stringtie_gtf = Channel.empty()
                             ^^^^^^^
  ```

- Warning: `subworkflows/local/stringtie/main.nf:19:73`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          ch_stringtie_gtf = STRINGTIE_STRINGTIE.out.transcript_gtf.map { meta, transcript_gtf -> [ transcript_gtf ] }.collect()
                                                                          ^^^^
  ```

- Warning: `subworkflows/local/utils_nfcore_lncpipe_pipeline/main.nf:31:5`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
      monochrome_logs   // boolean: Do not use coloured log outputs
      ^^^^^^^^^^^^^^^
  ```

- Warning: `subworkflows/local/utils_nfcore_lncpipe_pipeline/main.nf:34:5`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
      input             //  string: Path to input samplesheet
      ^^^^^
  ```

- Warning: `subworkflows/local/utils_nfcore_lncpipe_pipeline/main.nf:38:19`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_versions = Channel.empty()
                    ^^^^^^^
  ```

- Warning: `subworkflows/local/utils_nfcore_lncpipe_pipeline/main.nf:75:5`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      Channel
      ^^^^^^^
  ```

- Warning: `subworkflows/local/utils_nfcore_lncpipe_pipeline/main.nf:161:42`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
      def strandedness_ok = metas.collect{ it.strandedness }.unique().size == 1
                                           ^^
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

- Warning: `subworkflows/nf-core/fastq_align_hisat2/main.nf:14:19`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_versions = Channel.empty()
                    ^^^^^^^
  ```

- Warning: `subworkflows/nf-core/fastq_align_star/main.nf:20:19`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_versions = Channel.empty()
                    ^^^^^^^
  ```

- Warning: `subworkflows/nf-core/fastq_align_star/nextflow.config:31:61`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
                      saveAs: { params.save_align_intermeds ? it : null }
                                                              ^^
  ```

- Warning: `subworkflows/nf-core/fastq_align_star/nextflow.config:42:55`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
                      saveAs: { params.save_unaligned ? it : null }
                                                        ^^
  ```

- Warning: `subworkflows/nf-core/fastq_fastqc_umitools_fastp/main.nf:54:25`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_versions       = Channel.empty()
                          ^^^^^^^
  ```

- Warning: `subworkflows/nf-core/fastq_fastqc_umitools_fastp/main.nf:55:25`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      fastqc_raw_html   = Channel.empty()
                          ^^^^^^^
  ```

- Warning: `subworkflows/nf-core/fastq_fastqc_umitools_fastp/main.nf:56:25`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      fastqc_raw_zip    = Channel.empty()
                          ^^^^^^^
  ```

- Warning: `subworkflows/nf-core/fastq_fastqc_umitools_fastp/main.nf:57:25`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      umi_log           = Channel.empty()
                          ^^^^^^^
  ```

- Warning: `subworkflows/nf-core/fastq_fastqc_umitools_fastp/main.nf:58:25`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      trim_json         = Channel.empty()
                          ^^^^^^^
  ```

- Warning: `subworkflows/nf-core/fastq_fastqc_umitools_fastp/main.nf:59:25`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      trim_html         = Channel.empty()
                          ^^^^^^^
  ```

- Warning: `subworkflows/nf-core/fastq_fastqc_umitools_fastp/main.nf:60:25`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      trim_log          = Channel.empty()
                          ^^^^^^^
  ```

- Warning: `subworkflows/nf-core/fastq_fastqc_umitools_fastp/main.nf:61:25`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      trim_reads_fail   = Channel.empty()
                          ^^^^^^^
  ```

- Warning: `subworkflows/nf-core/fastq_fastqc_umitools_fastp/main.nf:62:25`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      trim_reads_merged = Channel.empty()
                          ^^^^^^^
  ```

- Warning: `subworkflows/nf-core/fastq_fastqc_umitools_fastp/main.nf:63:25`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      fastqc_trim_html  = Channel.empty()
                          ^^^^^^^
  ```

- Warning: `subworkflows/nf-core/fastq_fastqc_umitools_fastp/main.nf:64:25`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      fastqc_trim_zip   = Channel.empty()
                          ^^^^^^^
  ```

- Warning: `subworkflows/nf-core/fastq_fastqc_umitools_fastp/main.nf:65:25`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      trim_read_count   = Channel.empty()
                          ^^^^^^^
  ```

- Warning: `subworkflows/nf-core/fastq_fastqc_umitools_fastp/main.nf:66:25`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      adapter_seq       = Channel.empty()
                          ^^^^^^^
  ```

- Warning: `subworkflows/nf-core/fastq_fastqc_umitools_fastp/main.nf:126:23`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
              .filter { meta, _reads, num_reads -> num_reads >= min_trimmed_reads.toLong() }
                        ^^^^
  ```

- Warning: `subworkflows/nf-core/fastq_fastqc_umitools_fastp/main.nf:127:34`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
              .map { meta, _reads, num_reads -> [ meta, _reads ] }
                                   ^^^^^^^^^
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

- Warning: `subworkflows/nf-core/fastq_subsample_fq_salmon/main.nf:21:19`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_versions = Channel.empty()
                    ^^^^^^^
  ```

- Warning: `subworkflows/nf-core/utils_nfcore_pipeline/main.nf:101:98`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      return ch_versions.unique().map { version -> processVersionsFromYAML(version) }.unique().mix(Channel.of(workflowVersionToYAML()))
                                                                                                   ^^^^^^^
  ```

- Warning: `workflows/lncpipe.nf:41:5`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
      ch_chrom_sizes       // channel: path(genome.sizes)
      ^^^^^^^^^^^^^^
  ```

- Warning: `workflows/lncpipe.nf:42:5`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
      ch_gene_bed          // channel: path(gene.bed)
      ^^^^^^^^^^^
  ```

- Warning: `workflows/lncpipe.nf:45:5`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
      ch_rsem_index        // channel: path(rsem/index/)
      ^^^^^^^^^^^^^
  ```

- Warning: `workflows/lncpipe.nf:48:5`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
      ch_kallisto_index    // channel: [ meta, path(kallisto/index/) ] // this should not be ready yet..
      ^^^^^^^^^^^^^^^^^
  ```

- Warning: `workflows/lncpipe.nf:53:5`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
      make_sortmerna_index // boolean: Whether to create an index before running sortmerna
      ^^^^^^^^^^^^^^^^^^^^
  ```

- Warning: `workflows/lncpipe.nf:56:24`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_multiqc_files = Channel.empty()
                         ^^^^^^^
  ```

- Warning: `workflows/lncpipe.nf:98:5`: Variable was declared but not used

  ```nextflow
      ch_trim_status = ch_trim_read_count
      ^^^^^^^^^^^^^^
  ```

- Warning: `workflows/lncpipe.nf:112:30`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_genome_bam          = Channel.empty()
                               ^^^^^^^
  ```

- Warning: `workflows/lncpipe.nf:113:30`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_genome_bam_index    = Channel.empty()
                               ^^^^^^^
  ```

- Warning: `workflows/lncpipe.nf:114:30`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_star_log            = Channel.empty()
                               ^^^^^^^
  ```

- Warning: `workflows/lncpipe.nf:115:30`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_unaligned_sequences = Channel.empty()
                               ^^^^^^^
  ```

- Warning: `workflows/lncpipe.nf:116:30`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_transcriptome_bam   = Channel.empty()
                               ^^^^^^^
  ```

- Warning: `workflows/lncpipe.nf:129:40`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
              ch_star_index.map { [ [:], it ] },
                                         ^^
  ```

- Warning: `workflows/lncpipe.nf:130:33`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
              ch_gtf.map { [ [:], it ] },
                                  ^^
  ```

- Warning: `workflows/lncpipe.nf:134:35`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
              ch_fasta.map { [ [:], it ] },
                                    ^^
  ```

- Warning: `workflows/lncpipe.nf:135:46`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
              ch_transcript_fasta.map { [ [:], it ] }
                                               ^^
  ```

- Warning: `workflows/lncpipe.nf:141:9`: Variable was declared but not used

  ```nextflow
          ch_transcriptome_bai       = FASTQ_ALIGN_STAR.out.bai_transcript
          ^^^^^^^^^^^^^^^^^^^^
  ```

- Warning: `workflows/lncpipe.nf:145:53`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
              .mix(FASTQ_ALIGN_STAR.out.stats.collect{it[1]})
                                                      ^^
  ```

- Warning: `workflows/lncpipe.nf:146:56`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
              .mix(FASTQ_ALIGN_STAR.out.flagstat.collect{it[1]})
                                                         ^^
  ```

- Warning: `workflows/lncpipe.nf:147:56`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
              .mix(FASTQ_ALIGN_STAR.out.idxstats.collect{it[1]})
                                                         ^^
  ```

- Warning: `workflows/lncpipe.nf:148:57`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
              .mix(FASTQ_ALIGN_STAR.out.log_final.collect{it[1]})
                                                          ^^
  ```

- Warning: `workflows/lncpipe.nf:162:39`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
                  ch_fasta.map { [ [:], it ] },
                                        ^^
  ```

- Warning: `workflows/lncpipe.nf:167:50`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
                  ch_transcript_fasta.map { [ [:], it ] }
                                                   ^^
  ```

- Warning: `workflows/lncpipe.nf:183:57`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
                  .mix(FASTQ_ALIGN_STAR.out.stats.collect{it[1]})
                                                          ^^
  ```

- Warning: `workflows/lncpipe.nf:184:60`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
                  .mix(FASTQ_ALIGN_STAR.out.flagstat.collect{it[1]})
                                                             ^^
  ```

- Warning: `workflows/lncpipe.nf:185:60`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
                  .mix(FASTQ_ALIGN_STAR.out.idxstats.collect{it[1]})
                                                             ^^
  ```

- Warning: `workflows/lncpipe.nf:196:42`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
              ch_hisat2_index.map { [ [:], it ] },
                                           ^^
  ```

- Warning: `workflows/lncpipe.nf:197:41`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
              ch_splicesites.map { [ [:], it ] },
                                          ^^
  ```

- Warning: `workflows/lncpipe.nf:198:35`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
              ch_fasta.map { [ [:], it ] }
                                    ^^
  ```

- Warning: `workflows/lncpipe.nf:203:88`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          ch_multiqc_files = ch_multiqc_files.mix(FASTQ_ALIGN_HISAT2.out.summary.collect{it[1]})
                                                                                         ^^
  ```

- Warning: `workflows/lncpipe.nf:218:39`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
                  ch_fasta.map { [ [:], it ] },
                                        ^^
  ```

- Warning: `workflows/lncpipe.nf:223:50`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
                  ch_transcript_fasta.map { [ [:], it ] }
                                                   ^^
  ```

- Warning: `workflows/lncpipe.nf:237:59`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
                  .mix(FASTQ_ALIGN_HISAT2.out.stats.collect{it[1]})
                                                            ^^
  ```

- Warning: `workflows/lncpipe.nf:238:62`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
                  .mix(FASTQ_ALIGN_HISAT2.out.flagstat.collect{it[1]})
                                                               ^^
  ```

- Warning: `workflows/lncpipe.nf:239:62`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
                  .mix(FASTQ_ALIGN_HISAT2.out.idxstats.collect{it[1]})
                                                               ^^
  ```

- Warning: `workflows/lncpipe.nf:252:9`: Variable was declared but not used

  ```nextflow
          ch_map_status = ch_percent_mapped
          ^^^^^^^^^^^^^
  ```

- Warning: `workflows/lncpipe.nf:254:23`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
                  meta, mapped, pass ->
                        ^^^^^^
  ```

- Warning: `workflows/lncpipe.nf:306:43`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          .mix(GFFCOMPARE.out.stats.collect{it[1]})
                                            ^^
  ```

- Warning: `workflows/lncpipe.nf:416:32`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_multiqc_config        = Channel.fromPath(
                                 ^^^^^^^
  ```

- Warning: `workflows/lncpipe.nf:419:9`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
          Channel.fromPath(params.multiqc_config, checkIfExists: true) :
          ^^^^^^^
  ```

- Warning: `workflows/lncpipe.nf:420:9`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
          Channel.empty()
          ^^^^^^^
  ```

- Warning: `workflows/lncpipe.nf:422:9`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
          Channel.fromPath(params.multiqc_logo, checkIfExists: true) :
          ^^^^^^^
  ```

- Warning: `workflows/lncpipe.nf:423:9`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
          Channel.empty()
          ^^^^^^^
  ```

- Warning: `workflows/lncpipe.nf:427:27`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_workflow_summary = Channel.value(paramsSummaryMultiqc(summary_params))
                            ^^^^^^^
  ```

- Warning: `workflows/lncpipe.nf:433:45`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_methods_description                = Channel.value(
                                              ^^^^^^^
  ```
