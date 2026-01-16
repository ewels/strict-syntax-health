# Nextflow lint results

- Generated: 2026-01-16T10:21:42.231691035Z
- Nextflow version: 25.12.0-edge
- Summary: 10 errors, 69 warnings

## :x: Errors

- Error: `nextflow.config:302:30`: `manifest` is not defined

  ```nextflow
  \033[0;35m  nf-core/hgtseq ${manifest.version}\033[0m
                               ^^^^^^^^
  ```

- Error: `nextflow.config:305:26`: `manifest` is not defined

  ```nextflow
          afterText = """${manifest.doi ? "\n* The pipeline\n" : ""}${manifest.doi.tokenize(",").collect { "    https://doi.org/${it.trim().replace('https://doi.org/','')}"}.join("\n")}${manifest.doi ? "\n" : ""}
                           ^^^^^^^^
  ```

- Error: `nextflow.config:305:69`: `manifest` is not defined

  ```nextflow
          afterText = """${manifest.doi ? "\n* The pipeline\n" : ""}${manifest.doi.tokenize(",").collect { "    https://doi.org/${it.trim().replace('https://doi.org/','')}"}.join("\n")}${manifest.doi ? "\n" : ""}
                                                                      ^^^^^^^^
  ```

- Error: `nextflow.config:305:186`: `manifest` is not defined

  ```nextflow
          afterText = """${manifest.doi ? "\n* The pipeline\n" : ""}${manifest.doi.tokenize(",").collect { "    https://doi.org/${it.trim().replace('https://doi.org/','')}"}.join("\n")}${manifest.doi ? "\n" : ""}
                                                                                                                                                                                           ^^^^^^^^
  ```

- Error: `nextflow.config:314:22`: `validation` is not defined

  ```nextflow
          beforeText = validation.help.beforeText
                       ^^^^^^^^^^
  ```

- Error: `nextflow.config:315:21`: `validation` is not defined

  ```nextflow
          afterText = validation.help.afterText
                      ^^^^^^^^^^
  ```

- Error: `workflows/hgtseq.nf:13:1`: Statements cannot be mixed with script declarations -- move statements into a process, workflow, or function

  ```nextflow
  ch_multiqc_config          = Channel.fromPath("$projectDir/assets/multiqc_config.yml", checkIfExists: true)
  ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  ```

- Error: `workflows/hgtseq.nf:14:1`: Statements cannot be mixed with script declarations -- move statements into a process, workflow, or function

  ```nextflow
  ch_multiqc_custom_config   = params.multiqc_config ? Channel.fromPath( params.multiqc_config, checkIfExists: true ) : Channel.empty()
  ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  ```

- Error: `workflows/hgtseq.nf:15:1`: Statements cannot be mixed with script declarations -- move statements into a process, workflow, or function

  ```nextflow
  ch_multiqc_logo            = params.multiqc_logo   ? Channel.fromPath( params.multiqc_logo, checkIfExists: true ) : Channel.empty()
  ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  ```

- Error: `workflows/hgtseq.nf:16:1`: Statements cannot be mixed with script declarations -- move statements into a process, workflow, or function

  ```nextflow
  ch_multiqc_custom_methods_description = params.multiqc_methods_description ? file(params.multiqc_methods_description, checkIfExists: true) : file("$projectDir/assets/methods_description_template.yml", checkIfExists: true)
  ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  ```

## :warning: Warnings

- Warning: `modules/local/gawk/main.nf:22:9`: Variable was declared but not used

  ```nextflow
      def args = task.ext.args ?: ''
          ^^^^
  ```

- Warning: `modules/local/ranalysis/main.nf:27:9`: Variable was declared but not used

  ```nextflow
      def args = task.ext.args ?: ''
          ^^^^
  ```

- Warning: `modules/local/ranalysis/main.nf:28:9`: Variable was declared but not used

  ```nextflow
      def prefix = task.ext.prefix ?: ''
          ^^^^^^
  ```

- Warning: `modules/nf-core/bamtools/stats/main.nf:21:9`: Variable was declared but not used

  ```nextflow
      def args = task.ext.args ?: ''
          ^^^^
  ```

- Warning: `modules/nf-core/custom/dumpsoftwareversions/main.nf:22:9`: Variable was declared but not used

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

- Warning: `modules/nf-core/trimgalore/main.nf:47:31`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          args_list.removeAll { it.toLowerCase().contains('_r2 ') }
                                ^^
  ```

- Warning: `nextflow.config:305:129`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          afterText = """${manifest.doi ? "\n* The pipeline\n" : ""}${manifest.doi.tokenize(",").collect { "    https://doi.org/${it.trim().replace('https://doi.org/','')}"}.join("\n")}${manifest.doi ? "\n" : ""}
                                                                                                                                  ^^
  ```

- Warning: `subworkflows/local/bam_qc/main.nf:17:5`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
      fasta      // channel: [mandatory] path(fasta)
      ^^^^^
  ```

- Warning: `subworkflows/local/bam_qc/main.nf:21:19`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_versions = Channel.empty()
                    ^^^^^^^
  ```

- Warning: `subworkflows/local/classify_unmapped/main.nf:20:19`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_versions = Channel.empty()
                    ^^^^^^^
  ```

- Warning: `subworkflows/local/classify_unmapped/main.nf:22:37`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      SAMTOOLS_VIEW_SINGLE ( bam_bai, Channel.value([]), Channel.value([]) )
                                      ^^^^^^^
  ```

- Warning: `subworkflows/local/classify_unmapped/main.nf:22:56`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      SAMTOOLS_VIEW_SINGLE ( bam_bai, Channel.value([]), Channel.value([]) )
                                                         ^^^^^^^
  ```

- Warning: `subworkflows/local/prepare_reads/main.nf:22:19`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_versions = Channel.empty()
                    ^^^^^^^
  ```

- Warning: `subworkflows/local/prepare_reads/main.nf:23:19`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      aligned_bam = Channel.empty()
                    ^^^^^^^
  ```

- Warning: `subworkflows/local/prepare_reads/main.nf:25:18`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      fasta_meta = Channel.value(file(fasta)).map{ it -> [[id:it[0].baseName], it] }
                   ^^^^^^^
  ```

- Warning: `subworkflows/local/prepare_reads/main.nf:36:63`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
          bwaindex      = params.fasta ? params.bwaindex      ? Channel.fromPath(params.bwaindex).collect().map{ it -> [[id:it[0].baseName], it] } : BWAMEM1_INDEX.out.index : []
                                                                ^^^^^^^
  ```

- Warning: `subworkflows/local/prepare_reads/main.nf:48:63`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
          bwamem2index  = params.fasta ? params.bwamem2index  ? Channel.fromPath(params.bwamem2index).collect()  : BWAMEM2_INDEX.out.index : []
                                                                ^^^^^^^
  ```

- Warning: `subworkflows/local/reads_qc/main.nf:15:19`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_versions = Channel.empty()
                    ^^^^^^^
  ```

- Warning: `subworkflows/local/reporting/main.nf:20:19`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_versions = Channel.empty()
                    ^^^^^^^
  ```

- Warning: `subworkflows/local/reporting/main.nf:28:16`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      fakemeta = Channel.value([id: "group"])
                 ^^^^^^^
  ```

- Warning: `subworkflows/local/reporting/main.nf:39:20`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_rmarkdown = Channel.value(file("$projectDir/assets/analysis_report.Rmd"))
                     ^^^^^^^
  ```

- Warning: `subworkflows/local/sortbam/main.nf:11:5`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
      fasta      // channel: [mandatory] /path/to/reference/fasta
      ^^^^^
  ```

- Warning: `subworkflows/local/sortbam/main.nf:14:19`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_versions = Channel.empty()
                    ^^^^^^^
  ```

- Warning: `subworkflows/local/utils_nfcore_hgtseq_pipeline/main.nf:31:5`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
      monochrome_logs   // boolean: Do not use coloured log outputs
      ^^^^^^^^^^^^^^^
  ```

- Warning: `subworkflows/local/utils_nfcore_hgtseq_pipeline/main.nf:34:5`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
      input             //  string: Path to input samplesheet
      ^^^^^
  ```

- Warning: `subworkflows/local/utils_nfcore_hgtseq_pipeline/main.nf:38:19`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_versions = Channel.empty()
                    ^^^^^^^
  ```

- Warning: `subworkflows/local/utils_nfcore_hgtseq_pipeline/main.nf:75:1`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
  Channel
  ^^^^^^^
  ```

- Warning: `subworkflows/local/utils_nfcore_hgtseq_pipeline/main.nf:81:59`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
              return [ meta, [ fastq_1, fastq_2 ].findAll { it != null && it != 'null' } ]
                                                            ^^
  ```

- Warning: `subworkflows/local/utils_nfcore_hgtseq_pipeline/main.nf:81:73`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
              return [ meta, [ fastq_1, fastq_2 ].findAll { it != null && it != 'null' } ]
                                                                          ^^
  ```

- Warning: `subworkflows/nf-core/utils_nfcore_pipeline/main.nf:101:98`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      return ch_versions.unique().map { version -> processVersionsFromYAML(version) }.unique().mix(Channel.of(workflowVersionToYAML()))
                                                                                                   ^^^^^^^
  ```

- Warning: `workflows/hgtseq.nf:13:1`: Variable was declared but not used

  ```nextflow
  ch_multiqc_config          = Channel.fromPath("$projectDir/assets/multiqc_config.yml", checkIfExists: true)
  ^^^^^^^^^^^^^^^^^
  ```

- Warning: `workflows/hgtseq.nf:13:30`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
  ch_multiqc_config          = Channel.fromPath("$projectDir/assets/multiqc_config.yml", checkIfExists: true)
                               ^^^^^^^
  ```

- Warning: `workflows/hgtseq.nf:14:1`: Variable was declared but not used

  ```nextflow
  ch_multiqc_custom_config   = params.multiqc_config ? Channel.fromPath( params.multiqc_config, checkIfExists: true ) : Channel.empty()
  ^^^^^^^^^^^^^^^^^^^^^^^^
  ```

- Warning: `workflows/hgtseq.nf:14:54`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
  ch_multiqc_custom_config   = params.multiqc_config ? Channel.fromPath( params.multiqc_config, checkIfExists: true ) : Channel.empty()
                                                       ^^^^^^^
  ```

- Warning: `workflows/hgtseq.nf:14:119`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
  ch_multiqc_custom_config   = params.multiqc_config ? Channel.fromPath( params.multiqc_config, checkIfExists: true ) : Channel.empty()
                                                                                                                        ^^^^^^^
  ```

- Warning: `workflows/hgtseq.nf:15:1`: Variable was declared but not used

  ```nextflow
  ch_multiqc_logo            = params.multiqc_logo   ? Channel.fromPath( params.multiqc_logo, checkIfExists: true ) : Channel.empty()
  ^^^^^^^^^^^^^^^
  ```

- Warning: `workflows/hgtseq.nf:15:54`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
  ch_multiqc_logo            = params.multiqc_logo   ? Channel.fromPath( params.multiqc_logo, checkIfExists: true ) : Channel.empty()
                                                       ^^^^^^^
  ```

- Warning: `workflows/hgtseq.nf:15:117`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
  ch_multiqc_logo            = params.multiqc_logo   ? Channel.fromPath( params.multiqc_logo, checkIfExists: true ) : Channel.empty()
                                                                                                                      ^^^^^^^
  ```

- Warning: `workflows/hgtseq.nf:16:1`: Variable was declared but not used

  ```nextflow
  ch_multiqc_custom_methods_description = params.multiqc_methods_description ? file(params.multiqc_methods_description, checkIfExists: true) : file("$projectDir/assets/methods_description_template.yml", checkIfExists: true)
  ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  ```

- Warning: `workflows/hgtseq.nf:65:19`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_versions = Channel.empty()
                    ^^^^^^^
  ```

- Warning: `workflows/hgtseq.nf:66:24`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_multiqc_files = Channel.empty()
                         ^^^^^^^
  ```

- Warning: `workflows/hgtseq.nf:76:51`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          ch_krakendb = UNTAR_KRAKEN.out.untar.map{ it[1] }
                                                    ^^
  ```

- Warning: `workflows/hgtseq.nf:78:23`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
          ch_krakendb = Channel.value(krakendb)
                        ^^^^^^^
  ```

- Warning: `workflows/hgtseq.nf:85:49`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          ch_kronadb = UNTAR_KRONA.out.untar.map{ it[1] }
                                                  ^^
  ```

- Warning: `workflows/hgtseq.nf:87:22`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
          ch_kronadb = Channel.value(kronadb)
                       ^^^^^^^
  ```

- Warning: `workflows/hgtseq.nf:155:66`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
                  CLASSIFY_UNMAPPED.out.classified_single.collect{ it[1] },
                                                                   ^^
  ```

- Warning: `workflows/hgtseq.nf:156:64`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
                  CLASSIFY_UNMAPPED.out.classified_both.collect{ it[1] },
                                                                 ^^
  ```

- Warning: `workflows/hgtseq.nf:157:71`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
                  CLASSIFY_UNMAPPED.out.candidate_integrations.collect{ it[1] },
                                                                        ^^
  ```

- Warning: `workflows/hgtseq.nf:159:66`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
                  CLASSIFY_UNMAPPED.out.classified_single.collect{ it[0].id }
                                                                   ^^
  ```

- Warning: `workflows/hgtseq.nf:179:32`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_multiqc_config        = Channel.fromPath(
                                 ^^^^^^^
  ```

- Warning: `workflows/hgtseq.nf:182:9`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
          Channel.fromPath(params.multiqc_config, checkIfExists: true) :
          ^^^^^^^
  ```

- Warning: `workflows/hgtseq.nf:183:9`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
          Channel.empty()
          ^^^^^^^
  ```

- Warning: `workflows/hgtseq.nf:185:9`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
          Channel.fromPath(params.multiqc_logo, checkIfExists: true) :
          ^^^^^^^
  ```

- Warning: `workflows/hgtseq.nf:186:9`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
          Channel.empty()
          ^^^^^^^
  ```

- Warning: `workflows/hgtseq.nf:190:27`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_workflow_summary = Channel.value(paramsSummaryMultiqc(summary_params))
                            ^^^^^^^
  ```

- Warning: `workflows/hgtseq.nf:196:45`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_methods_description                = Channel.value(
                                              ^^^^^^^
  ```

- Warning: `workflows/hgtseq.nf:203:87`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          ch_multiqc_files = ch_multiqc_files.mix(READS_QC.out.fastqc_untrimmed.collect{it[1]}.ifEmpty([]))
                                                                                        ^^
  ```

- Warning: `workflows/hgtseq.nf:204:85`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          ch_multiqc_files = ch_multiqc_files.mix(READS_QC.out.fastqc_trimmed.collect{it[1]}.ifEmpty([]))
                                                                                      ^^
  ```

- Warning: `workflows/hgtseq.nf:207:70`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
      ch_multiqc_files = ch_multiqc_files.mix(BAM_QC.out.stats.collect{it[1]}.ifEmpty([]))
                                                                       ^^
  ```

- Warning: `workflows/hgtseq.nf:208:73`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
      ch_multiqc_files = ch_multiqc_files.mix(BAM_QC.out.flagstat.collect{it[1]}.ifEmpty([]))
                                                                          ^^
  ```

- Warning: `workflows/hgtseq.nf:209:73`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
      ch_multiqc_files = ch_multiqc_files.mix(BAM_QC.out.idxstats.collect{it[1]}.ifEmpty([]))
                                                                          ^^
  ```

- Warning: `workflows/hgtseq.nf:210:73`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
      ch_multiqc_files = ch_multiqc_files.mix(BAM_QC.out.qualimap.collect{it[1]}.ifEmpty([]))
                                                                          ^^
  ```

- Warning: `workflows/hgtseq.nf:211:73`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
      ch_multiqc_files = ch_multiqc_files.mix(BAM_QC.out.bamstats.collect{it[1]}.ifEmpty([]))
                                                                          ^^
  ```

- Warning: `workflows/hgtseq.nf:215:93`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          ch_multiqc_files = ch_multiqc_files.mix(CLASSIFY_UNMAPPED.out.report_single.collect{it[1]}.ifEmpty([]))
                                                                                              ^^
  ```

- Warning: `workflows/hgtseq.nf:216:91`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          ch_multiqc_files = ch_multiqc_files.mix(CLASSIFY_UNMAPPED.out.report_both.collect{it[1]}.ifEmpty([]))
                                                                                            ^^
  ```
