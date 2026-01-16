# Nextflow lint results

- Generated: 2026-01-16T06:30:49.356154143Z
- Nextflow version: 25.12.0-edge
- Summary: 31 errors, 51 warnings

## :x: Errors

- Error: `conf/modules.config:22:21`: Unexpected input: ':'

  ```nextflow
              withName: '.*FASTQC_RAW' {
                      ^
  ```

- Error: `modules/local/orp_transrate/main.nf:12:15`: `meta` is already declared

  ```nextflow
      tuple val(meta), path(reads)         // processed reads
                ^^^^
  ```

- Error: `modules/nf-core/salmon/quant/main.nf:30:20`: Unexpected input: ','

  ```nextflow
      def reads1 = [], reads2 = []
                     ^
  ```

- Error: `modules/nf-core/trinity/main.nf:26:20`: Unexpected input: ','

  ```nextflow
      def reads1 = [], reads2 = []
                     ^
  ```

- Error: `nextflow.config:317:40`: `manifest` is not defined

  ```nextflow
  \033[0;35m  nf-core/denovotranscript ${manifest.version}\033[0m
                                         ^^^^^^^^
  ```

- Error: `nextflow.config:320:26`: `manifest` is not defined

  ```nextflow
          afterText = """${manifest.doi ? "\n* The pipeline\n" : ""}${manifest.doi.tokenize(",").collect { "    https://doi.org/${it.trim().replace('https://doi.org/','')}"}.join("\n")}${manifest.doi ? "\n" : ""}
                           ^^^^^^^^
  ```

- Error: `nextflow.config:320:69`: `manifest` is not defined

  ```nextflow
          afterText = """${manifest.doi ? "\n* The pipeline\n" : ""}${manifest.doi.tokenize(",").collect { "    https://doi.org/${it.trim().replace('https://doi.org/','')}"}.join("\n")}${manifest.doi ? "\n" : ""}
                                                                      ^^^^^^^^
  ```

- Error: `nextflow.config:320:186`: `manifest` is not defined

  ```nextflow
          afterText = """${manifest.doi ? "\n* The pipeline\n" : ""}${manifest.doi.tokenize(",").collect { "    https://doi.org/${it.trim().replace('https://doi.org/','')}"}.join("\n")}${manifest.doi ? "\n" : ""}
                                                                                                                                                                                           ^^^^^^^^
  ```

- Error: `nextflow.config:329:22`: `validation` is not defined

  ```nextflow
          beforeText = validation.help.beforeText
                       ^^^^^^^^^^
  ```

- Error: `nextflow.config:330:21`: `validation` is not defined

  ```nextflow
          afterText = validation.help.afterText
                      ^^^^^^^^^^
  ```

- Error: `subworkflows/nf-core/fastq_trim_fastp_fastqc/main.nf:15:26`: Unexpected input: 'new'

  ```nextflow
      def Map json = (Map) new JsonSlurper().parseText(json_file.text).get('summary')
                           ^
  ```

- Error: `workflows/denovotranscript.nf:8:1`: Statements cannot be mixed with script declarations -- move statements into a process, workflow, or function

  ```nextflow
  if (params.remove_ribo_rna) {
  ^
  ```

- Error: `workflows/denovotranscript.nf:53:1`: Module could not be parsed: '/home/runner/work/strict-syntax-health/strict-syntax-health/pipelines/denovotranscript/modules/nf-core/trinity/main.nf'

  ```nextflow
  include { TRINITY                     } from '../modules/nf-core/trinity/main'
  ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  ```

- Error: `workflows/denovotranscript.nf:54:1`: Module could not be parsed: '/home/runner/work/strict-syntax-health/strict-syntax-health/pipelines/denovotranscript/modules/nf-core/trinity/main.nf'

  ```nextflow
  include { TRINITY as TRINITY_NO_NORM  } from '../modules/nf-core/trinity/main'
  ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  ```

- Error: `workflows/denovotranscript.nf:56:1`: Module could not be parsed: '/home/runner/work/strict-syntax-health/strict-syntax-health/pipelines/denovotranscript/modules/nf-core/salmon/quant/main.nf'

  ```nextflow
  include { SALMON_QUANT                } from '../modules/nf-core/salmon/quant/main'
  ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  ```

- Error: `workflows/denovotranscript.nf:61:1`: Module could not be parsed: '/home/runner/work/strict-syntax-health/strict-syntax-health/pipelines/denovotranscript/subworkflows/nf-core/fastq_trim_fastp_fastqc/main.nf'

  ```nextflow
  include { FASTQ_TRIM_FASTP_FASTQC     } from '../subworkflows/nf-core/fastq_trim_fastp_fastqc/main'
  ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  ```

- Error: `workflows/denovotranscript.nf:83:5`: `FASTQ_TRIM_FASTP_FASTQC` is not defined

  ```nextflow
      FASTQ_TRIM_FASTP_FASTQC (
      ^^^^^^^^^^^^^^^^^^^^^^^
  ```

- Error: `workflows/denovotranscript.nf:91:45`: `FASTQ_TRIM_FASTP_FASTQC` is not defined

  ```nextflow
      ch_multiqc_files = ch_multiqc_files.mix(FASTQ_TRIM_FASTP_FASTQC.out.fastqc_raw_zip.collect{it[1]})
                                              ^^^^^^^^^^^^^^^^^^^^^^^
  ```

- Error: `workflows/denovotranscript.nf:92:45`: `FASTQ_TRIM_FASTP_FASTQC` is not defined

  ```nextflow
      ch_multiqc_files = ch_multiqc_files.mix(FASTQ_TRIM_FASTP_FASTQC.out.fastqc_trim_zip.collect{it[1]})
                                              ^^^^^^^^^^^^^^^^^^^^^^^
  ```

- Error: `workflows/denovotranscript.nf:93:35`: `FASTQ_TRIM_FASTP_FASTQC` is not defined

  ```nextflow
      ch_versions = ch_versions.mix(FASTQ_TRIM_FASTP_FASTQC.out.versions)
                                    ^^^^^^^^^^^^^^^^^^^^^^^
  ```

- Error: `workflows/denovotranscript.nf:94:25`: `FASTQ_TRIM_FASTP_FASTQC` is not defined

  ```nextflow
      ch_filtered_reads = FASTQ_TRIM_FASTP_FASTQC.out.reads
                          ^^^^^^^^^^^^^^^^^^^^^^^
  ```

- Error: `workflows/denovotranscript.nf:97:44`: `ch_ribo_db` is not defined

  ```nextflow
          ch_sortmerna_fastas = Channel.from(ch_ribo_db.readLines()).map { row -> file(row, checkIfExists: true) }.collect()
                                             ^^^^^^^^^^
  ```

- Error: `workflows/denovotranscript.nf:142:17`: `TRINITY` is not defined

  ```nextflow
                  TRINITY (
                  ^^^^^^^
  ```

- Error: `workflows/denovotranscript.nf:145:47`: `TRINITY` is not defined

  ```nextflow
                  ch_versions = ch_versions.mix(TRINITY.out.versions)
                                                ^^^^^^^
  ```

- Error: `workflows/denovotranscript.nf:146:51`: `TRINITY` is not defined

  ```nextflow
                  ch_assemblies = ch_assemblies.mix(TRINITY.out.transcript_fasta)
                                                    ^^^^^^^
  ```

- Error: `workflows/denovotranscript.nf:153:17`: `TRINITY_NO_NORM` is not defined

  ```nextflow
                  TRINITY_NO_NORM (
                  ^^^^^^^^^^^^^^^
  ```

- Error: `workflows/denovotranscript.nf:156:47`: `TRINITY_NO_NORM` is not defined

  ```nextflow
                  ch_versions = ch_versions.mix(TRINITY_NO_NORM.out.versions)
                                                ^^^^^^^^^^^^^^^
  ```

- Error: `workflows/denovotranscript.nf:157:51`: `TRINITY_NO_NORM` is not defined

  ```nextflow
                  ch_assemblies = ch_assemblies.mix(TRINITY_NO_NORM.out.transcript_fasta)
                                                    ^^^^^^^^^^^^^^^
  ```

- Error: `workflows/denovotranscript.nf:276:9`: `SALMON_QUANT` is not defined

  ```nextflow
          SALMON_QUANT (
          ^^^^^^^^^^^^
  ```

- Error: `workflows/denovotranscript.nf:282:49`: `SALMON_QUANT` is not defined

  ```nextflow
          ch_multiqc_files = ch_multiqc_files.mix(SALMON_QUANT.out.results.collect{it[1]})
                                                  ^^^^^^^^^^^^
  ```

- Error: `workflows/denovotranscript.nf:283:39`: `SALMON_QUANT` is not defined

  ```nextflow
          ch_versions = ch_versions.mix(SALMON_QUANT.out.versions)
                                        ^^^^^^^^^^^^
  ```

## :warning: Warnings

- Warning: `modules/local/orp_transrate/main.nf:11:15`: Variable was declared but not used

  ```nextflow
      tuple val(meta), path(fasta)         // assembly file
                ^^^^
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

- Warning: `modules/nf-core/evigene/tr2aacds/main.nf:68:9`: Variable was declared but not used

  ```nextflow
      def args        = task.ext.args ?: ''
          ^^^^
  ```

- Warning: `modules/nf-core/evigene/tr2aacds/main.nf:70:9`: Variable was declared but not used

  ```nextflow
      def max_memory  = 7*1024
          ^^^^^^^^^^
  ```

- Warning: `modules/nf-core/sortmerna/main.nf:25:70`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
      def reads_input = reads instanceof List ? reads.collect{"--reads $it"}.join(' ') : "--reads $reads"
                                                                       ^^
  ```

- Warning: `modules/nf-core/sortmerna/main.nf:62:9`: Variable was declared but not used

  ```nextflow
      def args = task.ext.args ?: ''
          ^^^^
  ```

- Warning: `modules/nf-core/sortmerna/main.nf:64:9`: Variable was declared but not used

  ```nextflow
      def reads_input = reads instanceof List ? reads.collect{"--reads $it"}.join(' ') : "--reads $reads"
          ^^^^^^^^^^^
  ```

- Warning: `modules/nf-core/sortmerna/main.nf:64:70`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
      def reads_input = reads instanceof List ? reads.collect{"--reads $it"}.join(' ') : "--reads $reads"
                                                                       ^^
  ```

- Warning: `modules/nf-core/spades/main.nf:88:9`: Variable was declared but not used

  ```nextflow
      def args = task.ext.args ?: ''
          ^^^^
  ```

- Warning: `modules/nf-core/spades/main.nf:90:9`: Variable was declared but not used

  ```nextflow
      def maxmem = task.memory.toGiga()
          ^^^^^^
  ```

- Warning: `modules/nf-core/spades/main.nf:94:9`: Variable was declared but not used

  ```nextflow
      def custom_hmms = hmm ? "--custom-hmms $hmm" : ""
          ^^^^^^^^^^^
  ```

- Warning: `modules/nf-core/spades/main.nf:95:9`: Variable was declared but not used

  ```nextflow
      def reads = yml ? "--dataset $yml" : "$illumina_reads $pacbio_reads $nanopore_reads"
          ^^^^^
  ```

- Warning: `modules/nf-core/spades/main.nf:96:9`: Variable was declared but not used

  ```nextflow
      def ss = params.ss ? "--ss ${params.ss}" : ""
          ^^
  ```

- Warning: `nextflow.config:320:129`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          afterText = """${manifest.doi ? "\n* The pipeline\n" : ""}${manifest.doi.tokenize(",").collect { "    https://doi.org/${it.trim().replace('https://doi.org/','')}"}.join("\n")}${manifest.doi ? "\n" : ""}
                                                                                                                                  ^^
  ```

- Warning: `subworkflows/local/utils_nfcore_denovotranscript_pipeline/main.nf:31:5`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
      monochrome_logs   // boolean: Do not use coloured log outputs
      ^^^^^^^^^^^^^^^
  ```

- Warning: `subworkflows/local/utils_nfcore_denovotranscript_pipeline/main.nf:34:5`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
      input             //  string: Path to input samplesheet
      ^^^^^
  ```

- Warning: `subworkflows/local/utils_nfcore_denovotranscript_pipeline/main.nf:38:19`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_versions = Channel.empty()
                    ^^^^^^^
  ```

- Warning: `subworkflows/local/utils_nfcore_denovotranscript_pipeline/main.nf:75:5`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      Channel
      ^^^^^^^
  ```

- Warning: `subworkflows/local/utils_nfcore_denovotranscript_pipeline/main.nf:183:55`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          def invalid_assemblers = assemblers.findAll { it != "trinity" && it != "trinity_no_norm" && it != "rnaspades" }
                                                        ^^
  ```

- Warning: `subworkflows/local/utils_nfcore_denovotranscript_pipeline/main.nf:183:74`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          def invalid_assemblers = assemblers.findAll { it != "trinity" && it != "trinity_no_norm" && it != "rnaspades" }
                                                                           ^^
  ```

- Warning: `subworkflows/local/utils_nfcore_denovotranscript_pipeline/main.nf:183:101`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          def invalid_assemblers = assemblers.findAll { it != "trinity" && it != "trinity_no_norm" && it != "rnaspades" }
                                                                                                      ^^
  ```

- Warning: `subworkflows/nf-core/utils_nfcore_pipeline/main.nf:101:98`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      return ch_versions.unique().map { version -> processVersionsFromYAML(version) }.unique().mix(Channel.of(workflowVersionToYAML()))
                                                                                                   ^^^^^^^
  ```

- Warning: `workflows/denovotranscript.nf:12:18`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_ribo_db = Channel.empty()
                   ^^^^^^^
  ```

- Warning: `workflows/denovotranscript.nf:77:19`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_versions = Channel.empty()
                    ^^^^^^^
  ```

- Warning: `workflows/denovotranscript.nf:78:24`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_multiqc_files = Channel.empty()
                         ^^^^^^^
  ```

- Warning: `workflows/denovotranscript.nf:91:96`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
      ch_multiqc_files = ch_multiqc_files.mix(FASTQ_TRIM_FASTP_FASTQC.out.fastqc_raw_zip.collect{it[1]})
                                                                                                 ^^
  ```

- Warning: `workflows/denovotranscript.nf:92:97`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
      ch_multiqc_files = ch_multiqc_files.mix(FASTQ_TRIM_FASTP_FASTQC.out.fastqc_trim_zip.collect{it[1]})
                                                                                                  ^^
  ```

- Warning: `workflows/denovotranscript.nf:97:31`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
          ch_sortmerna_fastas = Channel.from(ch_ribo_db.readLines()).map { row -> file(row, checkIfExists: true) }.collect()
                                ^^^^^^^
  ```

- Warning: `workflows/denovotranscript.nf:106:75`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          ch_multiqc_files = ch_multiqc_files.mix(SORTMERNA.out.log.collect{it[1]}.ifEmpty([]))
                                                                            ^^
  ```

- Warning: `workflows/denovotranscript.nf:115:78`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          ch_multiqc_files = ch_multiqc_files.mix(FASTQC_FINAL.out.zip.collect{it[1]})
                                                                               ^^
  ```

- Warning: `workflows/denovotranscript.nf:124:51`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
              ch_pool = ch_filtered_reads.collect { meta, fastq -> fastq }.map { [[id:'pooled_reads', single_end:false], it] }
                                                    ^^^^
  ```

- Warning: `workflows/denovotranscript.nf:124:120`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
              ch_pool = ch_filtered_reads.collect { meta, fastq -> fastq }.map { [[id:'pooled_reads', single_end:false], it] }
                                                                                                                         ^^
  ```

- Warning: `workflows/denovotranscript.nf:134:29`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
              ch_assemblies = Channel.empty()
                              ^^^^^^^
  ```

- Warning: `workflows/denovotranscript.nf:185:28`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
                  .collect { meta, fasta -> fasta }
                             ^^^^
  ```

- Warning: `workflows/denovotranscript.nf:186:65`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
                  .map { [[id:'all_assembled', single_end:false], it ] }
                                                                  ^^
  ```

- Warning: `workflows/denovotranscript.nf:205:56`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
                  def mrna_file = dir.listFiles().find { it.name.endsWith('.okay.mrna') }
                                                         ^^
  ```

- Warning: `workflows/denovotranscript.nf:211:58`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
                  def pubids_file = dir.listFiles().find { it.name.endsWith('.pubids') }
                                                           ^^
  ```

- Warning: `workflows/denovotranscript.nf:234:97`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
              ch_multiqc_files = ch_multiqc_files.mix(BUSCO_BUSCO.out.short_summaries_txt.collect{it[1]})
                                                                                                  ^^
  ```

- Warning: `workflows/denovotranscript.nf:262:58`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
              ch_transcripts_fa = ch_transcripts.collect { meta, fasta -> fasta }
                                                           ^^^^
  ```

- Warning: `workflows/denovotranscript.nf:282:82`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          ch_multiqc_files = ch_multiqc_files.mix(SALMON_QUANT.out.results.collect{it[1]})
                                                                                   ^^
  ```

- Warning: `workflows/denovotranscript.nf:302:32`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_multiqc_config        = Channel.fromPath(
                                 ^^^^^^^
  ```

- Warning: `workflows/denovotranscript.nf:305:9`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
          Channel.fromPath(params.multiqc_config, checkIfExists: true) :
          ^^^^^^^
  ```

- Warning: `workflows/denovotranscript.nf:306:9`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
          Channel.empty()
          ^^^^^^^
  ```

- Warning: `workflows/denovotranscript.nf:308:9`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
          Channel.fromPath(params.multiqc_logo, checkIfExists: true) :
          ^^^^^^^
  ```

- Warning: `workflows/denovotranscript.nf:309:9`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
          Channel.empty()
          ^^^^^^^
  ```

- Warning: `workflows/denovotranscript.nf:313:27`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_workflow_summary = Channel.value(paramsSummaryMultiqc(summary_params))
                            ^^^^^^^
  ```

- Warning: `workflows/denovotranscript.nf:319:45`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_methods_description                = Channel.value(
                                              ^^^^^^^
  ```
