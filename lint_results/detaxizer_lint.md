# Nextflow lint results

- Generated: 2026-01-14T09:16:41.802986323Z
- Nextflow version: 25.12.0-edge
- Summary: 13 errors, 61 warnings

## :x: Errors

- Error: `subworkflows/local/generate_downstream_samplesheets/main.nf:47:17`: Variables in a closure should be declared with `def`

  ```nextflow
                  new_meta = [
                  ^^^^^^^^
  ```

- Error: `subworkflows/local/generate_downstream_samplesheets/main.nf:54:17`: Variables in a closure should be declared with `def`

  ```nextflow
                  read_files = reads.flatten().sort(false){ a, b -> a.getName().tokenize('.')[0] <=> b.getName().tokenize('.')[0] }
                  ^^^^^^^^^^
  ```

- Error: `subworkflows/local/generate_downstream_samplesheets/main.nf:108:5`: `format_sep` was assigned but not declared

  ```nextflow
      format_sep = ["csv":",", "tsv":"\t", "txt":"\t"][format]
      ^^^^^^^^^^
  ```

- Error: `subworkflows/local/generate_downstream_samplesheets/main.nf:110:5`: `ch_header` was assigned but not declared

  ```nextflow
      ch_header = ch_list_for_samplesheet
      ^^^^^^^^^
  ```

- Error: `subworkflows/local/generate_downstream_samplesheets/main.nf:112:5`: `ch_header` is not defined

  ```nextflow
      ch_header
      ^^^^^^^^^
  ```

- Error: `subworkflows/local/generate_downstream_samplesheets/main.nf:114:32`: `format_sep` is not defined

  ```nextflow
          .map{ it.keySet().join(format_sep) }
                                 ^^^^^^^^^^
  ```

- Error: `subworkflows/local/generate_downstream_samplesheets/main.nf:115:64`: `format_sep` is not defined

  ```nextflow
          .concat( ch_list_for_samplesheet.map{ it.values().join(format_sep) })
                                                                 ^^^^^^^^^^
  ```

- Error: `workflows/detaxizer.nf:46:1`: Statements cannot be mixed with script declarations -- move statements into a process or workflow

  ```nextflow
  def ch_fasta_blastn = Channel.empty()
  ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  ```

- Error: `workflows/detaxizer.nf:48:1`: Statements cannot be mixed with script declarations -- move statements into a process or workflow

  ```nextflow
  if ( !params.fasta_blastn && params.validation_blastn ) {
  ^
  ```

- Error: `workflows/detaxizer.nf:57:1`: Statements cannot be mixed with script declarations -- move statements into a process or workflow

  ```nextflow
  def ch_fasta_bbduk = Channel.empty()
  ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  ```

- Error: `workflows/detaxizer.nf:59:1`: Statements cannot be mixed with script declarations -- move statements into a process or workflow

  ```nextflow
  if ( !params.fasta_bbduk && params.classification_bbduk ) {
  ^
  ```

- Error: `workflows/detaxizer.nf:212:13`: `ch_fasta_bbduk` is not defined

  ```nextflow
              ch_fasta_bbduk.first()
              ^^^^^^^^^^^^^^
  ```

- Error: `workflows/detaxizer.nf:305:30`: `ch_fasta_blastn` is not defined

  ```nextflow
          ch_reference_fasta = ch_fasta_blastn
                               ^^^^^^^^^^^^^^^
  ```

## :warning: Warnings

- Warning: `modules/nf-core/bbmap/bbduk/main.nf:48:9`: Variable was declared but not used

  ```nextflow
      def args = task.ext.args ?: ''
          ^^^^
  ```

- Warning: `modules/nf-core/blast/blastn/main.nf:65:9`: Variable was declared but not used

  ```nextflow
      def args = task.ext.args ?: ''
          ^^^^
  ```

- Warning: `modules/nf-core/blast/makeblastdb/main.nf:42:9`: Variable was declared but not used

  ```nextflow
      def args           = task.ext.args ?: ''
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

- Warning: `subworkflows/local/generate_downstream_samplesheets/main.nf:73:18`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          .filter{ it.short_reads_1!="" } // MAG doesn't support standalone long reads
                   ^^
  ```

- Warning: `subworkflows/local/generate_downstream_samplesheets/main.nf:75:17`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
              se: it.short_reads_2 ==""
                  ^^
  ```

- Warning: `subworkflows/local/generate_downstream_samplesheets/main.nf:81:18`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          .filter{ it.long_reads !="" && it.short_reads_1=="" }
                   ^^
  ```

- Warning: `subworkflows/local/generate_downstream_samplesheets/main.nf:81:40`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          .filter{ it.long_reads !="" && it.short_reads_1=="" }
                                         ^^
  ```

- Warning: `subworkflows/local/generate_downstream_samplesheets/main.nf:82:169`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          .collect{ log.warn("Standalone long reads are not yet supported by the nf-core/mag pipeline and ARE REMOVED from the samplesheet 'mag-{se,pe}.csv' \n sample: ${it.sample}" )}
                                                                                                                                                                          ^^
  ```

- Warning: `subworkflows/local/generate_downstream_samplesheets/main.nf:114:15`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          .map{ it.keySet().join(format_sep) }
                ^^
  ```

- Warning: `subworkflows/local/generate_downstream_samplesheets/main.nf:115:47`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          .concat( ch_list_for_samplesheet.map{ it.values().join(format_sep) })
                                                ^^
  ```

- Warning: `subworkflows/local/utils_nfcore_detaxizer_pipeline/main.nf:32:5`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
      monochrome_logs   // boolean: Do not use coloured log outputs
      ^^^^^^^^^^^^^^^
  ```

- Warning: `subworkflows/local/utils_nfcore_detaxizer_pipeline/main.nf:35:5`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
      input             //  string: Path to input samplesheet
      ^^^^^
  ```

- Warning: `subworkflows/local/utils_nfcore_detaxizer_pipeline/main.nf:42:19`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_versions = Channel.empty()
                    ^^^^^^^
  ```

- Warning: `subworkflows/local/utils_nfcore_detaxizer_pipeline/main.nf:67:144`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
      after_text = """${workflow.manifest.doi ? "\n* The pipeline\n" : ""}${workflow.manifest.doi.tokenize(",").collect { "    https://doi.org/${it.trim().replace('https://doi.org/','')}"}.join("\n")}${workflow.manifest.doi ? "\n" : ""}
                                                                                                                                                 ^^
  ```

- Warning: `subworkflows/local/utils_nfcore_detaxizer_pipeline/main.nf:104:5`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      Channel
      ^^^^^^^
  ```

- Warning: `subworkflows/nf-core/utils_nfcore_pipeline/main.nf:101:98`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      return ch_versions.unique().map { version -> processVersionsFromYAML(version) }.unique().mix(Channel.of(workflowVersionToYAML()))
                                                                                                   ^^^^^^^
  ```

- Warning: `workflows/detaxizer.nf:46:23`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
  def ch_fasta_blastn = Channel.empty()
                        ^^^^^^^
  ```

- Warning: `workflows/detaxizer.nf:49:23`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_fasta_blastn = Channel.fromPath(getGenomeAttribute('fasta'))
                        ^^^^^^^
  ```

- Warning: `workflows/detaxizer.nf:52:23`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_fasta_blastn = Channel.fromPath(params.fasta_blastn)
                        ^^^^^^^
  ```

- Warning: `workflows/detaxizer.nf:57:22`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
  def ch_fasta_bbduk = Channel.empty()
                       ^^^^^^^
  ```

- Warning: `workflows/detaxizer.nf:60:22`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_fasta_bbduk = Channel.fromPath(getGenomeAttribute('fasta'))
                       ^^^^^^^
  ```

- Warning: `workflows/detaxizer.nf:63:22`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_fasta_bbduk = Channel.fromPath(params.fasta_bbduk)
                       ^^^^^^^
  ```

- Warning: `workflows/detaxizer.nf:71:19`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_versions = Channel.empty()
                    ^^^^^^^
  ```

- Warning: `workflows/detaxizer.nf:72:24`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_multiqc_files = Channel.empty()
                         ^^^^^^^
  ```

- Warning: `workflows/detaxizer.nf:73:25`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_filtered_reads = Channel.empty()
                          ^^^^^^^
  ```

- Warning: `workflows/detaxizer.nf:74:25`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_removed_reads  = Channel.empty()
                          ^^^^^^^
  ```

- Warning: `workflows/detaxizer.nf:77:21`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          shortReads: it[1]
                      ^^
  ```

- Warning: `workflows/detaxizer.nf:79:57`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          meta, short_reads_fastq_1, short_reads_fastq_2, long_reads_fastq_1 ->
                                                          ^^^^^^^^^^^^^^^^^^
  ```

- Warning: `workflows/detaxizer.nf:88:20`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          longReads: it[3]
                     ^^
  ```

- Warning: `workflows/detaxizer.nf:90:15`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          meta, short_reads_fastq_1, short_reads_fastq_2, long_reads_fastq_1 ->
                ^^^^^^^^^^^^^^^^^^^
  ```

- Warning: `workflows/detaxizer.nf:90:36`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          meta, short_reads_fastq_1, short_reads_fastq_2, long_reads_fastq_1 ->
                                     ^^^^^^^^^^^^^^^^^^^
  ```

- Warning: `workflows/detaxizer.nf:112:68`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
      ch_multiqc_files = ch_multiqc_files.mix(FASTQC.out.zip.collect{it[1]})
                                                                     ^^
  ```

- Warning: `workflows/detaxizer.nf:140:25`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
          ch_kraken2_db = Channel.fromPath(params.kraken2db).map {
                          ^^^^^^^
  ```

- Warning: `workflows/detaxizer.nf:184:75`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          ch_parsed_kraken2_report = PARSE_KRAKEN2REPORT.out.to_filter.map {meta, path -> path}
                                                                            ^^^^
  ```

- Warning: `workflows/detaxizer.nf:277:13`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
              meta, path -> [path]
              ^^^^
  ```

- Warning: `workflows/detaxizer.nf:398:17`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
                  meta, path -> [path]
                  ^^^^
  ```

- Warning: `workflows/detaxizer.nf:438:49`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
                  ch_to_filter.map { meta, reads, ids -> tuple(meta, reads) },
                                                  ^^^
  ```

- Warning: `workflows/detaxizer.nf:439:36`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
                  ch_to_filter.map { meta, reads, ids -> ids.toString() },
                                     ^^^^
  ```

- Warning: `workflows/detaxizer.nf:439:42`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
                  ch_to_filter.map { meta, reads, ids -> ids.toString() },
                                           ^^^^^
  ```

- Warning: `workflows/detaxizer.nf:440:17`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
                  Channel.value('fastq.gz'),
                  ^^^^^^^
  ```

- Warning: `workflows/detaxizer.nf:441:17`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
                  Channel.value(false)
                  ^^^^^^^
  ```

- Warning: `workflows/detaxizer.nf:447:53`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
                      ch_to_filter.map { meta, reads, ids -> tuple(meta, reads) },
                                                      ^^^
  ```

- Warning: `workflows/detaxizer.nf:448:40`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
                      ch_to_filter.map { meta, reads, ids -> ids.toString() },
                                         ^^^^
  ```

- Warning: `workflows/detaxizer.nf:448:46`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
                      ch_to_filter.map { meta, reads, ids -> ids.toString() },
                                               ^^^^^
  ```

- Warning: `workflows/detaxizer.nf:449:21`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
                      Channel.value('fastq.gz'),
                      ^^^^^^^
  ```

- Warning: `workflows/detaxizer.nf:450:21`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
                      Channel.value(false)
                      ^^^^^^^
  ```

- Warning: `workflows/detaxizer.nf:455:37`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
                  ch_filter_removed = Channel.empty()
                                      ^^^^^^^
  ```

- Warning: `workflows/detaxizer.nf:473:33`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
              ch_removed2rename = Channel.empty()
                                  ^^^^^^^
  ```

- Warning: `workflows/detaxizer.nf:496:110`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
              ch_removed_reads  = params.output_removed_reads ? RENAME_FASTQ_HEADERS_AFTER.out.fastq_removed : Channel.empty()
                                                                                                               ^^^^^^^
  ```

- Warning: `workflows/detaxizer.nf:501:32`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
              ch_removed_reads = Channel.empty()
                                 ^^^^^^^
  ```

- Warning: `workflows/detaxizer.nf:580:32`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_multiqc_config        = Channel.fromPath(
                                 ^^^^^^^
  ```

- Warning: `workflows/detaxizer.nf:583:9`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
          Channel.fromPath(params.multiqc_config, checkIfExists: true) :
          ^^^^^^^
  ```

- Warning: `workflows/detaxizer.nf:584:9`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
          Channel.empty()
          ^^^^^^^
  ```

- Warning: `workflows/detaxizer.nf:586:9`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
          Channel.fromPath(params.multiqc_logo, checkIfExists: true) :
          ^^^^^^^
  ```

- Warning: `workflows/detaxizer.nf:587:9`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
          Channel.empty()
          ^^^^^^^
  ```

- Warning: `workflows/detaxizer.nf:591:27`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_workflow_summary = Channel.value(paramsSummaryMultiqc(summary_params))
                            ^^^^^^^
  ```

- Warning: `workflows/detaxizer.nf:597:45`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_methods_description                = Channel.value(
                                              ^^^^^^^
  ```
