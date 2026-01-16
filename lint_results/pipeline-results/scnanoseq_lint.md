# Nextflow lint results

- Generated: 2026-01-16T10:29:28.654904848Z
- Nextflow version: 25.12.0-edge
- Summary: 74 errors, 140 warnings

## :x: Errors

- Error: `conf/modules.config:47:21`: Unexpected input: ':'

  ```nextflow
              withName: '.*:FASTQC_NANOPLOT_POST_TRIM:FASTQC' {
                      ^
  ```

- Error: `modules/local/group_transcripts.nf:12:15`: `meta` is already declared

  ```nextflow
      tuple val(meta), path(gtf)
                ^^^^
  ```

- Error: `modules/local/nanofilt.nf:40:13`: `prefix` is not defined

  ```nextflow
      touch ${prefix}.filtered.fastq
              ^^^^^^
  ```

- Error: `modules/nf-core/nanocomp/main.nf:48:5`: `for` loops are no longer supported

  ```nextflow
      for (file in filelist){
      ^^^
  ```

- Error: `modules/nf-core/nanocomp/main.nf:48:10`: `file` is not defined

  ```nextflow
      for (file in filelist){
           ^^^^
  ```

- Error: `modules/nf-core/nanocomp/main.nf:49:9`: Variables in a closure should be declared with `def`

  ```nextflow
          tokenized_filename = file.getName().tokenize('.')
          ^^^^^^^^^^^^^^^^^^
  ```

- Error: `modules/nf-core/nanocomp/main.nf:49:30`: `file` is not defined

  ```nextflow
          tokenized_filename = file.getName().tokenize('.')
                               ^^^^
  ```

- Error: `modules/nf-core/nanocomp/main.nf:54:9`: Variables in a closure should be declared with `def`

  ```nextflow
          first_namepart = true
          ^^^^^^^^^^^^^^
  ```

- Error: `modules/nf-core/nanocomp/main.nf:55:9`: Variables in a closure should be declared with `def`

  ```nextflow
          extension_found = false
          ^^^^^^^^^^^^^^^
  ```

- Error: `modules/nf-core/nanocomp/main.nf:57:9`: `for` loops are no longer supported

  ```nextflow
          for (namepart in tokenized_filename){
          ^^^
  ```

- Error: `modules/nf-core/nanocomp/main.nf:57:14`: `namepart` is not defined

  ```nextflow
          for (namepart in tokenized_filename){
               ^^^^^^^^
  ```

- Error: `modules/nf-core/nanocomp/main.nf:58:17`: `namepart` is not defined

  ```nextflow
              if (namepart == ""){
                  ^^^^^^^^
  ```

- Error: `modules/nf-core/nanocomp/main.nf:59:17`: `continue` is not allowed as an identifier because it is a Groovy keyword

  ```nextflow
                  continue
                  ^^^^^^^^
  ```

- Error: `modules/nf-core/nanocomp/main.nf:59:17`: `continue` is not defined

  ```nextflow
                  continue
                  ^^^^^^^^
  ```

- Error: `modules/nf-core/nanocomp/main.nf:65:17`: `continue` is not allowed as an identifier because it is a Groovy keyword

  ```nextflow
                  continue
                  ^^^^^^^^
  ```

- Error: `modules/nf-core/nanocomp/main.nf:65:17`: `continue` is not defined

  ```nextflow
                  continue
                  ^^^^^^^^
  ```

- Error: `modules/nf-core/nanocomp/main.nf:68:41`: `namepart` is not defined

  ```nextflow
              if (["fq","fastq"].contains(namepart)){
                                          ^^^^^^^^
  ```

- Error: `modules/nf-core/nanocomp/main.nf:71:17`: `break` is not allowed as an identifier because it is a Groovy keyword

  ```nextflow
                  break
                  ^^^^^
  ```

- Error: `modules/nf-core/nanocomp/main.nf:71:17`: `break` is not defined

  ```nextflow
                  break
                  ^^^^^
  ```

- Error: `modules/nf-core/nanocomp/main.nf:72:77`: `namepart` is not defined

  ```nextflow
              } else if (["fasta", "fna", "ffn", "faa", "frn", "fa"].contains(namepart)) {
                                                                              ^^^^^^^^
  ```

- Error: `modules/nf-core/nanocomp/main.nf:75:17`: `break` is not allowed as an identifier because it is a Groovy keyword

  ```nextflow
                  break
                  ^^^^^
  ```

- Error: `modules/nf-core/nanocomp/main.nf:75:17`: `break` is not defined

  ```nextflow
                  break
                  ^^^^^
  ```

- Error: `modules/nf-core/nanocomp/main.nf:76:24`: `namepart` is not defined

  ```nextflow
              } else if (namepart == "bam") {
                         ^^^^^^^^
  ```

- Error: `modules/nf-core/nanocomp/main.nf:79:17`: `break` is not allowed as an identifier because it is a Groovy keyword

  ```nextflow
                  break
                  ^^^^^
  ```

- Error: `modules/nf-core/nanocomp/main.nf:79:17`: `break` is not defined

  ```nextflow
                  break
                  ^^^^^
  ```

- Error: `modules/nf-core/nanocomp/main.nf:80:24`: `namepart` is not defined

  ```nextflow
              } else if (namepart == "txt") {
                         ^^^^^^^^
  ```

- Error: `modules/nf-core/nanocomp/main.nf:83:17`: `break` is not allowed as an identifier because it is a Groovy keyword

  ```nextflow
                  break
                  ^^^^^
  ```

- Error: `modules/nf-core/nanocomp/main.nf:83:17`: `break` is not defined

  ```nextflow
                  break
                  ^^^^^
  ```

- Error: `modules/nf-core/nanocomp/main.nf:88:104`: `file` is not defined

  ```nextflow
              throw new java.lang.IllegalArgumentException("There was no suitable filetype found for " + file.getName() +
                                                                                                         ^^^^
  ```

- Error: `modules/nf-core/samtools/view/main.nf:66:9`: `index` is already declared

  ```nextflow
      def index = args.contains("--write-index") ? "touch ${prefix}.csi" : ""
          ^^^^^
  ```

- Error: `nextflow.config:311:33`: `manifest` is not defined

  ```nextflow
  \033[0;35m  nf-core/scnanoseq ${manifest.version}\033[0m
                                  ^^^^^^^^
  ```

- Error: `nextflow.config:314:26`: `manifest` is not defined

  ```nextflow
          afterText = """${manifest.doi ? "\n* The pipeline\n" : ""}${manifest.doi.tokenize(",").collect { "    https://doi.org/${it.trim().replace('https://doi.org/','')}"}.join("\n")}${manifest.doi ? "\n" : ""}
                           ^^^^^^^^
  ```

- Error: `nextflow.config:314:69`: `manifest` is not defined

  ```nextflow
          afterText = """${manifest.doi ? "\n* The pipeline\n" : ""}${manifest.doi.tokenize(",").collect { "    https://doi.org/${it.trim().replace('https://doi.org/','')}"}.join("\n")}${manifest.doi ? "\n" : ""}
                                                                      ^^^^^^^^
  ```

- Error: `nextflow.config:314:186`: `manifest` is not defined

  ```nextflow
          afterText = """${manifest.doi ? "\n* The pipeline\n" : ""}${manifest.doi.tokenize(",").collect { "    https://doi.org/${it.trim().replace('https://doi.org/','')}"}.join("\n")}${manifest.doi ? "\n" : ""}
                                                                                                                                                                                           ^^^^^^^^
  ```

- Error: `nextflow.config:323:22`: `validation` is not defined

  ```nextflow
          beforeText = validation.help.beforeText
                       ^^^^^^^^^^
  ```

- Error: `nextflow.config:324:21`: `validation` is not defined

  ```nextflow
          afterText = validation.help.afterText
                      ^^^^^^^^^^
  ```

- Error: `subworkflows/local/dedup_umis.nf:131:13`: `PICARD_MARKDUPLICATES` is not defined

  ```nextflow
              PICARD_MARKDUPLICATES (
              ^^^^^^^^^^^^^^^^^^^^^
  ```

- Error: `subworkflows/local/dedup_umis.nf:136:28`: `PICARD_MARKDUPLICATES` is not defined

  ```nextflow
              ch_dedup_bam = PICARD_MARKDUPLICATES.out.bam
                             ^^^^^^^^^^^^^^^^^^^^^
  ```

- Error: `subworkflows/local/dedup_umis.nf:137:43`: `PICARD_MARKDUPLICATES` is not defined

  ```nextflow
              ch_versions = ch_versions.mix(PICARD_MARKDUPLICATES.out.versions)
                                            ^^^^^^^^^^^^^^^^^^^^^
  ```

- Error: `subworkflows/local/process_longread_scrna.nf:117:25`: Variables in a closure should be declared with `def`

  ```nextflow
                          id = ['id': meta.id]
                          ^^
  ```

- Error: `subworkflows/local/quantify_scrna_oarfish.nf:41:29`: Variables in a closure should be declared with `def`

  ```nextflow
                              new_meta = [ 'id' : meta.id ]
                              ^^^^^^^^
  ```

- Error: `workflows/scnanoseq.nf:8:1`: Statements cannot be mixed with script declarations -- move statements into a process, workflow, or function

  ```nextflow
  if (params.whitelist) {
  ^
  ```

- Error: `workflows/scnanoseq.nf:29:1`: Statements cannot be mixed with script declarations -- move statements into a process, workflow, or function

  ```nextflow
  GENOME_QUANT_OPTS = [ 'isoquant' ]
  ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  ```

- Error: `workflows/scnanoseq.nf:30:1`: Statements cannot be mixed with script declarations -- move statements into a process, workflow, or function

  ```nextflow
  TRANSCRIPT_QUANT_OPTS = [ 'oarfish' ]
  ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  ```

- Error: `workflows/scnanoseq.nf:32:1`: Statements cannot be mixed with script declarations -- move statements into a process, workflow, or function

  ```nextflow
  genome_quants = []
  ^^^^^^^^^^^^^^^^^^
  ```

- Error: `workflows/scnanoseq.nf:33:1`: Statements cannot be mixed with script declarations -- move statements into a process, workflow, or function

  ```nextflow
  transcript_quants = []
  ^^^^^^^^^^^^^^^^^^^^^^
  ```

- Error: `workflows/scnanoseq.nf:34:1`: `for` loops are no longer supported

  ```nextflow
  for (quantifier in params.quantifier.split(',')) {
  ^^^
  ```

- Error: `workflows/scnanoseq.nf:34:1`: Statements cannot be mixed with script declarations -- move statements into a process, workflow, or function

  ```nextflow
  for (quantifier in params.quantifier.split(',')) {
  ^
  ```

- Error: `workflows/scnanoseq.nf:34:6`: `quantifier` is not defined

  ```nextflow
  for (quantifier in params.quantifier.split(',')) {
       ^^^^^^^^^^
  ```

- Error: `workflows/scnanoseq.nf:35:9`: `quantifier` is not defined

  ```nextflow
      if (quantifier in GENOME_QUANT_OPTS) {
          ^^^^^^^^^^
  ```

- Error: `workflows/scnanoseq.nf:36:27`: `quantifier` is not defined

  ```nextflow
          genome_quants.add(quantifier)
                            ^^^^^^^^^^
  ```

- Error: `workflows/scnanoseq.nf:39:9`: `quantifier` is not defined

  ```nextflow
      if (quantifier in TRANSCRIPT_QUANT_OPTS) {
          ^^^^^^^^^^
  ```

- Error: `workflows/scnanoseq.nf:40:31`: `quantifier` is not defined

  ```nextflow
          transcript_quants.add(quantifier)
                                ^^^^^^^^^^
  ```

- Error: `workflows/scnanoseq.nf:51:1`: Statements cannot be mixed with script declarations -- move statements into a process, workflow, or function

  ```nextflow
  ch_multiqc_config                       = Channel.fromPath("$projectDir/assets/multiqc_config.yml", checkIfExists: true)
  ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  ```

- Error: `workflows/scnanoseq.nf:52:1`: Statements cannot be mixed with script declarations -- move statements into a process, workflow, or function

  ```nextflow
  ch_multiqc_custom_config                = params.multiqc_config ? Channel.fromPath( params.multiqc_config, checkIfExists: true ) : Channel.empty()
  ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  ```

- Error: `workflows/scnanoseq.nf:53:1`: Statements cannot be mixed with script declarations -- move statements into a process, workflow, or function

  ```nextflow
  ch_multiqc_logo                         = params.multiqc_logo   ? Channel.fromPath( params.multiqc_logo, checkIfExists: true ) : Channel.empty()
  ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  ```

- Error: `workflows/scnanoseq.nf:54:1`: Statements cannot be mixed with script declarations -- move statements into a process, workflow, or function

  ```nextflow
  ch_multiqc_custom_methods_description   = params.multiqc_methods_description ? file(params.multiqc_methods_description, checkIfExists: true) : file("$projectDir/assets/methods_description_template.yml", checkIfExists: true)
  ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  ```

- Error: `workflows/scnanoseq.nf:300:26`: `blaze_whitelist` is not defined

  ```nextflow
      ch_blaze_whitelist = blaze_whitelist
                           ^^^^^^^^^^^^^^^
  ```

- Error: `workflows/scnanoseq.nf:302:9`: `blaze_whitelist` is not defined

  ```nextflow
      if (blaze_whitelist.endsWith('.gz')){
          ^^^^^^^^^^^^^^^
  ```

- Error: `workflows/scnanoseq.nf:304:34`: `blaze_whitelist` is not defined

  ```nextflow
          GUNZIP_WHITELIST ( [[:], blaze_whitelist ])
                                   ^^^^^^^^^^^^^^^
  ```

- Error: `workflows/scnanoseq.nf:438:8`: `genome_quants` is not defined

  ```nextflow
      if (genome_quants){
         ^^^^^^^^^^^^^^^
  ```

- Error: `workflows/scnanoseq.nf:446:13`: `genome_quants` is not defined

  ```nextflow
              genome_quants,
              ^^^^^^^^^^^^^
  ```

- Error: `workflows/scnanoseq.nf:497:8`: `transcript_quants` is not defined

  ```nextflow
      if (transcript_quants) {
         ^^^^^^^^^^^^^^^^^^^
  ```

- Error: `workflows/scnanoseq.nf:505:13`: `transcript_quants` is not defined

  ```nextflow
              transcript_quants,
              ^^^^^^^^^^^^^^^^^
  ```

- Error: `workflows/scnanoseq.nf:562:61`: `ch_multiqc_config` is not defined

  ```nextflow
          ch_multiqc_rawqc_files = ch_multiqc_rawqc_files.mix(ch_multiqc_config)
                                                              ^^^^^^^^^^^^^^^^^
  ```

- Error: `workflows/scnanoseq.nf:563:61`: `ch_multiqc_custom_config` is not defined

  ```nextflow
          ch_multiqc_rawqc_files = ch_multiqc_rawqc_files.mix(ch_multiqc_custom_config.collect().ifEmpty([]))
                                                              ^^^^^^^^^^^^^^^^^^^^^^^^
  ```

- Error: `workflows/scnanoseq.nf:570:13`: `ch_multiqc_config` is not defined

  ```nextflow
              ch_multiqc_config,
              ^^^^^^^^^^^^^^^^^
  ```

- Error: `workflows/scnanoseq.nf:571:13`: `ch_multiqc_custom_config` is not defined

  ```nextflow
              ch_multiqc_custom_config.collect().ifEmpty([]),
              ^^^^^^^^^^^^^^^^^^^^^^^^
  ```

- Error: `workflows/scnanoseq.nf:572:13`: `ch_multiqc_logo` is not defined

  ```nextflow
              ch_multiqc_logo.collect().ifEmpty([]),
              ^^^^^^^^^^^^^^^
  ```

- Error: `workflows/scnanoseq.nf:583:65`: `ch_multiqc_config` is not defined

  ```nextflow
          ch_multiqc_finalqc_files = ch_multiqc_finalqc_files.mix(ch_multiqc_config)
                                                                  ^^^^^^^^^^^^^^^^^
  ```

- Error: `workflows/scnanoseq.nf:584:65`: `ch_multiqc_custom_config` is not defined

  ```nextflow
          ch_multiqc_finalqc_files = ch_multiqc_finalqc_files.mix(ch_multiqc_custom_config.collect().ifEmpty([]))
                                                                  ^^^^^^^^^^^^^^^^^^^^^^^^
  ```

- Error: `workflows/scnanoseq.nf:594:13`: `ch_multiqc_config` is not defined

  ```nextflow
              ch_multiqc_config,
              ^^^^^^^^^^^^^^^^^
  ```

- Error: `workflows/scnanoseq.nf:595:13`: `ch_multiqc_custom_config` is not defined

  ```nextflow
              ch_multiqc_custom_config.collect().ifEmpty([]),
              ^^^^^^^^^^^^^^^^^^^^^^^^
  ```

- Error: `workflows/scnanoseq.nf:596:13`: `ch_multiqc_logo` is not defined

  ```nextflow
              ch_multiqc_logo.collect().ifEmpty([]),
              ^^^^^^^^^^^^^^^
  ```

## :warning: Warnings

- Warning: `modules/local/group_transcripts.nf:11:15`: Variable was declared but not used

  ```nextflow
      tuple val(meta), path(fasta)
                ^^^^
  ```

- Warning: `modules/local/group_transcripts.nf:23:9`: Variable was declared but not used

  ```nextflow
      def args      = task.ext.args ?: ''
          ^^^^
  ```

- Warning: `modules/local/merge_mtx.nf:21:9`: Variable was declared but not used

  ```nextflow
      def args   = task.ext.args ?: ''
          ^^^^
  ```

- Warning: `modules/local/split_fasta.nf:20:9`: Variable was declared but not used

  ```nextflow
      def args = task.ext.args ?: ''
          ^^^^
  ```

- Warning: `modules/local/split_file.nf:23:9`: Variable was declared but not used

  ```nextflow
      def args   = task.ext.args ?: ''
          ^^^^
  ```

- Warning: `modules/local/split_gtf.nf:20:9`: Variable was declared but not used

  ```nextflow
      def args = task.ext.args ?: ''
          ^^^^
  ```

- Warning: `modules/local/tag_barcodes.nf:21:9`: Variable was declared but not used

  ```nextflow
      def args   = task.ext.args ?: ''
          ^^^^
  ```

- Warning: `modules/nf-core/bamtools/split/main.nf:23:39`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
      def input_list = bam.collect{"-in $it"}.join(' ')
                                        ^^
  ```

- Warning: `modules/nf-core/cat/cat/main.nf:23:40`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
      def file_list = files_in.collect { it.toString() }
                                         ^^
  ```

- Warning: `modules/nf-core/cat/cat/main.nf:58:42`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
      def file_list   = files_in.collect { it.toString() }
                                           ^^
  ```

- Warning: `modules/nf-core/cat/fastq/main.nf:21:9`: Variable was declared but not used

  ```nextflow
      def args = task.ext.args ?: ''
          ^^^^
  ```

- Warning: `modules/nf-core/cat/fastq/main.nf:23:59`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
      def readList = reads instanceof List ? reads.collect{ it.toString() } : [reads.toString()]
                                                            ^^
  ```

- Warning: `modules/nf-core/cat/fastq/main.nf:54:59`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
      def readList = reads instanceof List ? reads.collect{ it.toString() } : [reads.toString()]
                                                            ^^
  ```

- Warning: `modules/nf-core/custom/dumpsoftwareversions/main.nf:22:9`: Variable was declared but not used

  ```nextflow
      def args = task.ext.args ?: ''
          ^^^^
  ```

- Warning: `modules/nf-core/minimap2/align/main.nf:67:9`: Variable was declared but not used

  ```nextflow
      def target = reference ?: (bam_input ? error("BAM input requires reference") : reads)
          ^^^^^^
  ```

- Warning: `modules/nf-core/nanoplot/main.nf:25:91`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
      def input_file = [ ".fastq.gz", ".fastq", ".fq", ".fq.gz" ].any { "$ontfile".endsWith(it) } ? "--fastq ${ontfile}" :
                                                                                            ^^
  ```

- Warning: `modules/nf-core/pigz/compress/main.nf:35:9`: Variable was declared but not used

  ```nextflow
      def args = task.ext.args ?: ''
          ^^^^
  ```

- Warning: `modules/nf-core/pigz/uncompress/main.nf:38:9`: Variable was declared but not used

  ```nextflow
      def args = task.ext.args ?: ''
          ^^^^
  ```

- Warning: `modules/nf-core/rseqc/readdistribution/main.nf:22:9`: Variable was declared but not used

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

- Warning: `nextflow.config:314:129`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          afterText = """${manifest.doi ? "\n* The pipeline\n" : ""}${manifest.doi.tokenize(",").collect { "    https://doi.org/${it.trim().replace('https://doi.org/','')}"}.join("\n")}${manifest.doi ? "\n" : ""}
                                                                                                                                  ^^
  ```

- Warning: `subworkflows/local/align_longreads.nf:21:9`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          fai         // channel: [ val(meta), path(fai) ]
          ^^^
  ```

- Warning: `subworkflows/local/align_longreads.nf:22:9`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          gtf         // channel: [ val(meta), path(gtf) ]
          ^^^
  ```

- Warning: `subworkflows/local/align_longreads.nf:32:23`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
          ch_versions = Channel.empty()
                        ^^^^^^^
  ```

- Warning: `subworkflows/local/align_longreads.nf:83:9`: Variable was declared but not used

  ```nextflow
          ch_minimap_filtered_sorted_bam = BAM_SORT_STATS_SAMTOOLS_FILTERED.out.bam
          ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  ```

- Warning: `subworkflows/local/align_longreads.nf:84:9`: Variable was declared but not used

  ```nextflow
          ch_minimap_filtered_sorted_bai = BAM_SORT_STATS_SAMTOOLS_FILTERED.out.bai
          ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  ```

- Warning: `subworkflows/local/align_longreads.nf:90:30`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
          ch_rseqc_read_dist = Channel.empty()
                               ^^^^^^^
  ```

- Warning: `subworkflows/local/align_longreads.nf:100:32`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
          ch_nanocomp_bam_html = Channel.empty()
                                 ^^^^^^^
  ```

- Warning: `subworkflows/local/align_longreads.nf:101:31`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
          ch_nanocomp_bam_txt = Channel.empty()
                                ^^^^^^^
  ```

- Warning: `subworkflows/local/align_longreads.nf:107:30`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
                      .collect{it[1]}
                               ^^
  ```

- Warning: `subworkflows/local/align_longreads.nf:109:55`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
                          [ [ 'id': 'nanocomp_bam.' ] , it ]
                                                        ^^
  ```

- Warning: `subworkflows/local/dedup_umis.nf:36:23`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
          ch_versions = Channel.empty()
                        ^^^^^^^
  ```

- Warning: `subworkflows/local/dedup_umis.nf:38:26`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
          ch_undedup_bam = Channel.empty()
                           ^^^^^^^
  ```

- Warning: `subworkflows/local/dedup_umis.nf:39:26`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
          ch_undedup_bai = Channel.empty()
                           ^^^^^^^
  ```

- Warning: `subworkflows/local/dedup_umis.nf:42:28`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
              ch_split_bam = Channel.empty()
                             ^^^^^^^
  ```

- Warning: `subworkflows/local/dedup_umis.nf:52:25`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
                          meta, bam ->
                          ^^^^
  ```

- Warning: `subworkflows/local/dedup_umis.nf:114:24`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
          ch_dedup_bam = Channel.empty()
                         ^^^^^^^
  ```

- Warning: `subworkflows/local/dedup_umis.nf:115:24`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
          ch_dedup_bai = Channel.empty()
                         ^^^^^^^
  ```

- Warning: `subworkflows/local/dedup_umis.nf:153:25`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
                          meta, bam ->
                          ^^^^
  ```

- Warning: `subworkflows/local/prepare_reference_files.nf:22:23`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
          ch_versions = Channel.empty()
                        ^^^^^^^
  ```

- Warning: `subworkflows/local/prepare_reference_files.nf:29:27`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
          ch_genome_fasta = Channel.empty()
                            ^^^^^^^
  ```

- Warning: `subworkflows/local/prepare_reference_files.nf:30:25`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
          ch_genome_fai = Channel.empty()
                          ^^^^^^^
  ```

- Warning: `subworkflows/local/prepare_reference_files.nf:59:31`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
          ch_transcript_fasta = Channel.empty()
                                ^^^^^^^
  ```

- Warning: `subworkflows/local/prepare_reference_files.nf:60:29`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
          ch_transcript_fai = Channel.empty()
                              ^^^^^^^
  ```

- Warning: `subworkflows/local/prepare_reference_files.nf:88:27`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
          ch_prepared_gtf = Channel.empty()
                            ^^^^^^^
  ```

- Warning: `subworkflows/local/process_longread_scrna.nf:43:23`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
          ch_versions = Channel.empty()
                        ^^^^^^^
  ```

- Warning: `subworkflows/local/process_longread_scrna.nf:88:18`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
          ch_bam = Channel.empty()
                   ^^^^^^^
  ```

- Warning: `subworkflows/local/process_longread_scrna.nf:89:18`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
          ch_bai = Channel.empty()
                   ^^^^^^^
  ```

- Warning: `subworkflows/local/process_longread_scrna.nf:90:23`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
          ch_flagstat = Channel.empty()
                        ^^^^^^^
  ```

- Warning: `subworkflows/local/process_longread_scrna.nf:91:23`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
          ch_idxstats = Channel.empty()
                        ^^^^^^^
  ```

- Warning: `subworkflows/local/process_longread_scrna.nf:126:28`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
          ch_gene_qc_stats = Channel.empty()
                             ^^^^^^^
  ```

- Warning: `subworkflows/local/process_longread_scrna.nf:127:34`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
          ch_transcript_qc_stats = Channel.empty()
                                   ^^^^^^^
  ```

- Warning: `subworkflows/local/qc_scrna.nf:15:23`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
          ch_versions = Channel.empty()
                        ^^^^^^^
  ```

- Warning: `subworkflows/local/qc_scrna.nf:26:64`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          COMBINE_SEURAT_STATS ( SEURAT.out.seurat_stats.collect{it[1]} )
                                                                 ^^
  ```

- Warning: `subworkflows/local/quantify_scrna_isoquant.nf:19:9`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          in_bai
          ^^^^^^
  ```

- Warning: `subworkflows/local/quantify_scrna_isoquant.nf:22:9`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          in_fai
          ^^^^^^
  ```

- Warning: `subworkflows/local/quantify_scrna_isoquant.nf:24:9`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          skip_qc
          ^^^^^^^
  ```

- Warning: `subworkflows/local/quantify_scrna_isoquant.nf:25:9`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          skip_seurat
          ^^^^^^^^^^^
  ```

- Warning: `subworkflows/local/quantify_scrna_isoquant.nf:28:23`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
          ch_versions = Channel.empty()
                        ^^^^^^^
  ```

- Warning: `subworkflows/local/quantify_scrna_isoquant.nf:70:17`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
                  meta, bam ->
                  ^^^^
  ```

- Warning: `subworkflows/local/quantify_scrna_isoquant.nf:104:20`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
              .map { chrom, meta, bam, bai, fasta, fai, gtf ->
                     ^^^^^
  ```

- Warning: `subworkflows/local/quantify_scrna_isoquant.nf:148:28`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
          ch_gene_qc_stats = Channel.empty()
                             ^^^^^^^
  ```

- Warning: `subworkflows/local/quantify_scrna_isoquant.nf:149:34`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
          ch_transcript_qc_stats = Channel.empty()
                                   ^^^^^^^
  ```

- Warning: `subworkflows/local/quantify_scrna_oarfish.nf:12:9`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          in_bai
          ^^^^^^
  ```

- Warning: `subworkflows/local/quantify_scrna_oarfish.nf:15:9`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          skip_qc
          ^^^^^^^
  ```

- Warning: `subworkflows/local/quantify_scrna_oarfish.nf:16:9`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          skip_seurat
          ^^^^^^^^^^^
  ```

- Warning: `subworkflows/local/quantify_scrna_oarfish.nf:19:23`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
          ch_versions = Channel.empty()
                        ^^^^^^^
  ```

- Warning: `subworkflows/local/quantify_scrna_oarfish.nf:33:34`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
          ch_transcript_qc_stats = Channel.empty()
                                   ^^^^^^^
  ```

- Warning: `subworkflows/local/utils_nfcore_scnanoseq_pipeline/main.nf:31:5`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
      monochrome_logs   // boolean: Do not use coloured log outputs
      ^^^^^^^^^^^^^^^
  ```

- Warning: `subworkflows/local/utils_nfcore_scnanoseq_pipeline/main.nf:34:5`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
      input             //  string: Path to input samplesheet
      ^^^^^
  ```

- Warning: `subworkflows/local/utils_nfcore_scnanoseq_pipeline/main.nf:38:19`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_versions = Channel.empty()
                    ^^^^^^^
  ```

- Warning: `subworkflows/local/utils_nfcore_scnanoseq_pipeline/main.nf:75:5`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      Channel
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

- Warning: `subworkflows/nf-core/qcfastq_nanoplot_fastqc.nf:31:24`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      nanoplot_png     = Channel.empty()
                         ^^^^^^^
  ```

- Warning: `subworkflows/nf-core/qcfastq_nanoplot_fastqc.nf:32:24`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      nanoplot_html    = Channel.empty()
                         ^^^^^^^
  ```

- Warning: `subworkflows/nf-core/qcfastq_nanoplot_fastqc.nf:33:24`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      nanoplot_txt     = Channel.empty()
                         ^^^^^^^
  ```

- Warning: `subworkflows/nf-core/qcfastq_nanoplot_fastqc.nf:34:24`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      nanoplot_log     = Channel.empty()
                         ^^^^^^^
  ```

- Warning: `subworkflows/nf-core/qcfastq_nanoplot_fastqc.nf:35:24`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      nanoplot_version = Channel.empty()
                         ^^^^^^^
  ```

- Warning: `subworkflows/nf-core/qcfastq_nanoplot_fastqc.nf:47:31`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      toulligqc_report_data   = Channel.empty()
                                ^^^^^^^
  ```

- Warning: `subworkflows/nf-core/qcfastq_nanoplot_fastqc.nf:48:31`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      toulligqc_report_html   = Channel.empty()
                                ^^^^^^^
  ```

- Warning: `subworkflows/nf-core/qcfastq_nanoplot_fastqc.nf:49:31`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      toulligqc_plots_html    = Channel.empty()
                                ^^^^^^^
  ```

- Warning: `subworkflows/nf-core/qcfastq_nanoplot_fastqc.nf:50:31`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      toulligqc_plotly_js     = Channel.empty()
                                ^^^^^^^
  ```

- Warning: `subworkflows/nf-core/qcfastq_nanoplot_fastqc.nf:51:31`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      toulligqc_version       = Channel.empty()
                                ^^^^^^^
  ```

- Warning: `subworkflows/nf-core/qcfastq_nanoplot_fastqc.nf:64:22`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      fastqc_zip     = Channel.empty()
                       ^^^^^^^
  ```

- Warning: `subworkflows/nf-core/qcfastq_nanoplot_fastqc.nf:65:22`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      fastqc_html    = Channel.empty()
                       ^^^^^^^
  ```

- Warning: `subworkflows/nf-core/qcfastq_nanoplot_fastqc.nf:66:22`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      fastqc_multiqc = Channel.empty()
                       ^^^^^^^
  ```

- Warning: `subworkflows/nf-core/qcfastq_nanoplot_fastqc.nf:67:22`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      fastqc_version = Channel.empty()
                       ^^^^^^^
  ```

- Warning: `subworkflows/nf-core/utils_nfcore_pipeline/main.nf:101:98`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      return ch_versions.unique().map { version -> processVersionsFromYAML(version) }.unique().mix(Channel.of(workflowVersionToYAML()))
                                                                                                   ^^^^^^^
  ```

- Warning: `workflows/scnanoseq.nf:51:1`: Variable was declared but not used

  ```nextflow
  ch_multiqc_config                       = Channel.fromPath("$projectDir/assets/multiqc_config.yml", checkIfExists: true)
  ^^^^^^^^^^^^^^^^^
  ```

- Warning: `workflows/scnanoseq.nf:51:43`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
  ch_multiqc_config                       = Channel.fromPath("$projectDir/assets/multiqc_config.yml", checkIfExists: true)
                                            ^^^^^^^
  ```

- Warning: `workflows/scnanoseq.nf:52:1`: Variable was declared but not used

  ```nextflow
  ch_multiqc_custom_config                = params.multiqc_config ? Channel.fromPath( params.multiqc_config, checkIfExists: true ) : Channel.empty()
  ^^^^^^^^^^^^^^^^^^^^^^^^
  ```

- Warning: `workflows/scnanoseq.nf:52:67`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
  ch_multiqc_custom_config                = params.multiqc_config ? Channel.fromPath( params.multiqc_config, checkIfExists: true ) : Channel.empty()
                                                                    ^^^^^^^
  ```

- Warning: `workflows/scnanoseq.nf:52:132`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
  ch_multiqc_custom_config                = params.multiqc_config ? Channel.fromPath( params.multiqc_config, checkIfExists: true ) : Channel.empty()
                                                                                                                                     ^^^^^^^
  ```

- Warning: `workflows/scnanoseq.nf:53:1`: Variable was declared but not used

  ```nextflow
  ch_multiqc_logo                         = params.multiqc_logo   ? Channel.fromPath( params.multiqc_logo, checkIfExists: true ) : Channel.empty()
  ^^^^^^^^^^^^^^^
  ```

- Warning: `workflows/scnanoseq.nf:53:67`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
  ch_multiqc_logo                         = params.multiqc_logo   ? Channel.fromPath( params.multiqc_logo, checkIfExists: true ) : Channel.empty()
                                                                    ^^^^^^^
  ```

- Warning: `workflows/scnanoseq.nf:53:130`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
  ch_multiqc_logo                         = params.multiqc_logo   ? Channel.fromPath( params.multiqc_logo, checkIfExists: true ) : Channel.empty()
                                                                                                                                   ^^^^^^^
  ```

- Warning: `workflows/scnanoseq.nf:54:1`: Variable was declared but not used

  ```nextflow
  ch_multiqc_custom_methods_description   = params.multiqc_methods_description ? file(params.multiqc_methods_description, checkIfExists: true) : file("$projectDir/assets/methods_description_template.yml", checkIfExists: true)
  ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  ```

- Warning: `workflows/scnanoseq.nf:128:19`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_versions = Channel.empty()
                    ^^^^^^^
  ```

- Warning: `workflows/scnanoseq.nf:129:25`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_multiqc_report = Channel.empty()
                          ^^^^^^^
  ```

- Warning: `workflows/scnanoseq.nf:158:33`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_fastqc_multiqc_pretrim = Channel.empty()
                                  ^^^^^^^
  ```

- Warning: `workflows/scnanoseq.nf:175:30`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_nanocomp_fastq_html = Channel.empty()
                               ^^^^^^^
  ```

- Warning: `workflows/scnanoseq.nf:176:29`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_nanocomp_fastq_txt = Channel.empty()
                              ^^^^^^^
  ```

- Warning: `workflows/scnanoseq.nf:181:26`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
                  .collect{it[1]}
                           ^^
  ```

- Warning: `workflows/scnanoseq.nf:183:53`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
                      [ [ 'id': 'nanocomp_fastq.' ] , it ]
                                                      ^^
  ```

- Warning: `workflows/scnanoseq.nf:217:15`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_pred = Channel.empty()
                ^^^^^^^
  ```

- Warning: `workflows/scnanoseq.nf:218:20`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_rseqc_bed = Channel.empty()
                     ^^^^^^^
  ```

- Warning: `workflows/scnanoseq.nf:239:33`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_fastqc_multiqc_postrim = Channel.empty()
                                  ^^^^^^^
  ```

- Warning: `workflows/scnanoseq.nf:240:33`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_trimmed_reads_combined = Channel.empty()
                                  ^^^^^^^
  ```

- Warning: `workflows/scnanoseq.nf:309:21`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
                      meta, whitelist ->
                      ^^^^
  ```

- Warning: `workflows/scnanoseq.nf:392:37`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_fastqc_multiqc_postextract = Channel.empty()
                                      ^^^^^^^
  ```

- Warning: `workflows/scnanoseq.nf:393:22`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_read_counts = Channel.empty()
                       ^^^^^^^
  ```

- Warning: `workflows/scnanoseq.nf:407:29`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
          ch_pretrim_counts = Channel.empty()
                              ^^^^^^^
  ```

- Warning: `workflows/scnanoseq.nf:408:30`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
          ch_posttrim_counts = Channel.empty()
                               ^^^^^^^
  ```

- Warning: `workflows/scnanoseq.nf:409:33`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
          ch_postextract_counts = Channel.empty()
                                  ^^^^^^^
  ```

- Warning: `workflows/scnanoseq.nf:411:67`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
              ch_pretrim_counts = ch_fastqc_multiqc_pretrim.collect{it[0]}
                                                                    ^^
  ```

- Warning: `workflows/scnanoseq.nf:412:68`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
              ch_posttrim_counts = ch_fastqc_multiqc_postrim.collect{it[0]}
                                                                     ^^
  ```

- Warning: `workflows/scnanoseq.nf:413:75`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
              ch_postextract_counts = ch_fastqc_multiqc_postextract.collect{it[0]}
                                                                            ^^
  ```

- Warning: `workflows/scnanoseq.nf:416:61`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
              ch_pretrim_counts = ch_nanostat_pretrim.collect{it[1]}
                                                              ^^
  ```

- Warning: `workflows/scnanoseq.nf:417:63`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
              ch_posttrim_counts = ch_nanostat_posttrim.collect{it[1]}
                                                                ^^
  ```

- Warning: `workflows/scnanoseq.nf:418:69`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
              ch_postextract_counts = ch_nanostat_postextract.collect{it[1]}
                                                                      ^^
  ```

- Warning: `workflows/scnanoseq.nf:426:42`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
              ch_corrected_bc_info.collect{it[1]})
                                           ^^
  ```

- Warning: `workflows/scnanoseq.nf:436:32`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_multiqc_finalqc_files = Channel.empty()
                                 ^^^^^^^
  ```

- Warning: `workflows/scnanoseq.nf:460:72`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
              PROCESS_LONGREAD_SCRNA_GENOME.out.minimap_flagstat.collect{it[1]}.ifEmpty([])
                                                                         ^^
  ```

- Warning: `workflows/scnanoseq.nf:463:72`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
              PROCESS_LONGREAD_SCRNA_GENOME.out.minimap_idxstats.collect{it[1]}.ifEmpty([])
                                                                         ^^
  ```

- Warning: `workflows/scnanoseq.nf:466:79`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
              PROCESS_LONGREAD_SCRNA_GENOME.out.minimap_rseqc_read_dist.collect{it[1]}.ifEmpty([])
                                                                                ^^
  ```

- Warning: `workflows/scnanoseq.nf:469:80`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
              PROCESS_LONGREAD_SCRNA_GENOME.out.minimap_nanocomp_bam_txt.collect{it[1]}.ifEmpty([])
                                                                                 ^^
  ```

- Warning: `workflows/scnanoseq.nf:473:74`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
              PROCESS_LONGREAD_SCRNA_GENOME.out.bc_tagged_flagstat.collect{it[1]}.ifEmpty([])
                                                                           ^^
  ```

- Warning: `workflows/scnanoseq.nf:478:74`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
                  PROCESS_LONGREAD_SCRNA_GENOME.out.dedup_flagstat.collect{it[1]}.ifEmpty([])
                                                                           ^^
  ```

- Warning: `workflows/scnanoseq.nf:481:74`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
                  PROCESS_LONGREAD_SCRNA_GENOME.out.dedup_idxstats.collect{it[1]}.ifEmpty([])
                                                                           ^^
  ```

- Warning: `workflows/scnanoseq.nf:520:76`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
              PROCESS_LONGREAD_SCRNA_TRANSCRIPT.out.minimap_flagstat.collect{it[1]}.ifEmpty([])
                                                                             ^^
  ```

- Warning: `workflows/scnanoseq.nf:523:83`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
              PROCESS_LONGREAD_SCRNA_TRANSCRIPT.out.minimap_rseqc_read_dist.collect{it[1]}.ifEmpty([])
                                                                                    ^^
  ```

- Warning: `workflows/scnanoseq.nf:526:84`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
              PROCESS_LONGREAD_SCRNA_TRANSCRIPT.out.minimap_nanocomp_bam_txt.collect{it[1]}.ifEmpty([])
                                                                                     ^^
  ```

- Warning: `workflows/scnanoseq.nf:530:78`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
              PROCESS_LONGREAD_SCRNA_TRANSCRIPT.out.bc_tagged_flagstat.collect{it[1]}.ifEmpty([])
                                                                               ^^
  ```

- Warning: `workflows/scnanoseq.nf:535:78`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
                  PROCESS_LONGREAD_SCRNA_TRANSCRIPT.out.dedup_flagstat.collect{it[1]}.ifEmpty([])
                                                                               ^^
  ```

- Warning: `workflows/scnanoseq.nf:561:34`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
          ch_multiqc_rawqc_files = Channel.empty()
                                   ^^^^^^^
  ```

- Warning: `workflows/scnanoseq.nf:566:91`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          ch_multiqc_rawqc_files = ch_multiqc_rawqc_files.mix(ch_nanocomp_fastq_txt.collect{it[1]}.ifEmpty([]))
                                                                                            ^^
  ```

- Warning: `workflows/scnanoseq.nf:581:34`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
          ch_workflow_summary    = Channel.value(paramsSummaryMultiqc(summary_params))
                                   ^^^^^^^
  ```
