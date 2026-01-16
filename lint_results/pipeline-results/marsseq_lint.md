# Nextflow lint results

- Generated: 2026-01-16T06:34:20.197908906Z
- Nextflow version: 25.12.0-edge
- Summary: 37 errors, 64 warnings

## :x: Errors

- Error: `modules/local/qc/report/main.nf:15:15`: `meta` is already declared

  ```nextflow
      tuple val(meta), path(pdf)
                ^^^^
  ```

- Error: `modules/nf-core/star/starsolo/main.nf:33:30`: Unexpected input: '\n'

  ```nextflow
          case "CB_UMI_Simple":
                               ^
  ```

- Error: `nextflow.config:211:1`: Variable declarations cannot be mixed with config statements

  ```nextflow
  def trace_timestamp = new java.util.Date().format( 'yyyy-MM-dd_HH-mm-ss')
  ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  ```

- Error: `nextflow.config:214:68`: `trace_timestamp` is not defined

  ```nextflow
      file    = "${params.outdir}/pipeline_info/execution_timeline_${trace_timestamp}.html"
                                                                     ^^^^^^^^^^^^^^^
  ```

- Error: `nextflow.config:218:66`: `trace_timestamp` is not defined

  ```nextflow
      file    = "${params.outdir}/pipeline_info/execution_report_${trace_timestamp}.html"
                                                                   ^^^^^^^^^^^^^^^
  ```

- Error: `nextflow.config:222:65`: `trace_timestamp` is not defined

  ```nextflow
      file    = "${params.outdir}/pipeline_info/execution_trace_${trace_timestamp}.txt"
                                                                  ^^^^^^^^^^^^^^^
  ```

- Error: `nextflow.config:226:62`: `trace_timestamp` is not defined

  ```nextflow
      file    = "${params.outdir}/pipeline_info/pipeline_dag_${trace_timestamp}.html"
                                                               ^^^^^^^^^^^^^^^
  ```

- Error: `nextflow.config:249:34`: `manifest` is not defined

  ```nextflow
          command = "nextflow run $manifest.name -profile <docker/singularity/.../institute> --input samplesheet.csv --outdir <OUTDIR>"
                                   ^^^^^^^^
  ```

- Error: `nextflow.config:259:15`: `manifest` is not defined

  ```nextflow
  \033[0;35m  ${manifest.name} ${manifest.version}\033[0m
                ^^^^^^^^
  ```

- Error: `nextflow.config:259:32`: `manifest` is not defined

  ```nextflow
  \033[0;35m  ${manifest.name} ${manifest.version}\033[0m
                                 ^^^^^^^^
  ```

- Error: `nextflow.config:262:26`: `manifest` is not defined

  ```nextflow
          afterText = """${manifest.doi ? "* The pipeline\n" : ""}${manifest.doi.tokenize(",").collect { "  https://doi.org/${it.trim().replace('https://doi.org/','')}"}.join("\n")}${manifest.doi ? "\n" : ""}
                           ^^^^^^^^
  ```

- Error: `nextflow.config:262:67`: `manifest` is not defined

  ```nextflow
          afterText = """${manifest.doi ? "* The pipeline\n" : ""}${manifest.doi.tokenize(",").collect { "  https://doi.org/${it.trim().replace('https://doi.org/','')}"}.join("\n")}${manifest.doi ? "\n" : ""}
                                                                    ^^^^^^^^
  ```

- Error: `nextflow.config:262:182`: `manifest` is not defined

  ```nextflow
          afterText = """${manifest.doi ? "* The pipeline\n" : ""}${manifest.doi.tokenize(",").collect { "  https://doi.org/${it.trim().replace('https://doi.org/','')}"}.join("\n")}${manifest.doi ? "\n" : ""}
                                                                                                                                                                                       ^^^^^^^^
  ```

- Error: `nextflow.config:267:26`: `manifest` is not defined

  ```nextflow
      https://github.com/${manifest.name}/blob/master/CITATIONS.md
                           ^^^^^^^^
  ```

- Error: `nextflow.config:271:22`: `validation` is not defined

  ```nextflow
          beforeText = validation.help.beforeText
                       ^^^^^^^^^^
  ```

- Error: `nextflow.config:272:21`: `validation` is not defined

  ```nextflow
          afterText = validation.help.afterText
                      ^^^^^^^^^^
  ```

- Error: `subworkflows/local/align_reads.nf:19:22`: `reads` is already declared

  ```nextflow
          .map { meta, reads -> [ [ "id": meta.id, "single_end": true, "filename": reads.baseName ], reads ]}
                       ^^^^^
  ```

- Error: `subworkflows/local/demultiplex_reads.nf:26:47`: `reads` is already declared

  ```nextflow
          .map { amp_batch, pool_barcode, meta, reads -> [
                                                ^^^^^
  ```

- Error: `subworkflows/local/prepare_genome.nf:38:31`: `fasta` is already declared

  ```nextflow
      ch_fasta = ch_fasta.map { fasta -> [ [id: fasta.baseName], fasta ] }
                                ^^^^^
  ```

- Error: `subworkflows/local/prepare_genome.nf:49:27`: `gtf` is already declared

  ```nextflow
      ch_gtf = ch_gtf.map { gtf -> [ [id: gtf.baseName], gtf ] }
                            ^^^
  ```

- Error: `subworkflows/local/prepare_genome.nf:64:29`: `fasta` is already declared

  ```nextflow
                  .map{ meta, fasta, ercc -> [ [id:"${meta.id}_ercc"], [fasta, ercc] ] }
                              ^^^^^
  ```

- Error: `subworkflows/local/velocity.nf:9:1`: Module could not be parsed: '/home/runner/work/strict-syntax-health/strict-syntax-health/pipelines/marsseq/modules/nf-core/star/starsolo/main.nf'

  ```nextflow
  include { STARSOLO                        } from '../../modules/nf-core/star/starsolo/main'
  ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  ```

- Error: `subworkflows/local/velocity.nf:23:22`: `reads` is already declared

  ```nextflow
          .map { meta, reads -> return [ meta, reads.sort().collate(2) ] }
                       ^^^^^
  ```

- Error: `subworkflows/local/velocity.nf:30:69`: `reads` is already declared

  ```nextflow
      CAT_FASTQ ( VELOCITY_CONVERT.out.reads.groupTuple().map { meta, reads -> [ meta, reads.flatten() ] } )
                                                                      ^^^^^
  ```

- Error: `subworkflows/local/velocity.nf:43:15`: `reads` is already declared

  ```nextflow
          meta, reads -> [
                ^^^^^
  ```

- Error: `subworkflows/local/velocity.nf:54:5`: `STARSOLO` is not defined

  ```nextflow
      STARSOLO ( ch_reads, VELOCITY_WHITELIST.out.whitelist, index )
      ^^^^^^^^
  ```

- Error: `subworkflows/local/velocity.nf:55:35`: `STARSOLO` is not defined

  ```nextflow
      ch_versions = ch_versions.mix(STARSOLO.out.versions)
                                    ^^^^^^^^
  ```

- Error: `subworkflows/local/velocity.nf:59:24`: `STARSOLO` is not defined

  ```nextflow
      star_multiqc     = STARSOLO.out.log_final
                         ^^^^^^^^
  ```

- Error: `workflows/marsseq.nf:29:1`: Statements cannot be mixed with script declarations -- move statements into a process, workflow, or function

  ```nextflow
  ercc_regions            = file("$projectDir/data/ercc-regions.tsv")
  ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  ```

- Error: `workflows/marsseq.nf:30:1`: Statements cannot be mixed with script declarations -- move statements into a process, workflow, or function

  ```nextflow
  ch_oligos               = Channel.fromPath("$projectDir/data/oligos.txt", checkIfExists: true)
  ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  ```

- Error: `workflows/marsseq.nf:31:1`: Statements cannot be mixed with script declarations -- move statements into a process, workflow, or function

  ```nextflow
  ch_spike_seq            = Channel.fromPath("$projectDir/data/spike-seq.txt", checkIfExists: true)
  ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  ```

- Error: `workflows/marsseq.nf:32:1`: Statements cannot be mixed with script declarations -- move statements into a process, workflow, or function

  ```nextflow
  ch_spike_concentrations = Channel.fromPath("$projectDir/data/spike-concentrations.txt", checkIfExists: true)
  ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  ```

- Error: `workflows/marsseq.nf:63:9`: `ercc_regions` is not defined

  ```nextflow
          ercc_regions,
          ^^^^^^^^^^^^
  ```

- Error: `workflows/marsseq.nf:71:13`: `ch_oligos` is not defined

  ```nextflow
              ch_oligos,
              ^^^^^^^^^
  ```

- Error: `workflows/marsseq.nf:97:13`: `ch_spike_seq` is not defined

  ```nextflow
              ch_spike_seq,
              ^^^^^^^^^^^^
  ```

- Error: `workflows/marsseq.nf:98:13`: `ch_spike_concentrations` is not defined

  ```nextflow
              ch_spike_concentrations,
              ^^^^^^^^^^^^^^^^^^^^^^^
  ```

- Error: `workflows/marsseq.nf:99:13`: `ch_oligos` is not defined

  ```nextflow
              ch_oligos
              ^^^^^^^^^
  ```

## :warning: Warnings

- Warning: `modules/local/ercc/main.nf:21:9`: Variable was declared but not used

  ```nextflow
      def args = task.ext.args ?: ''
          ^^^^
  ```

- Warning: `modules/local/extract/main.nf:26:9`: Variable was declared but not used

  ```nextflow
      def args = task.ext.args ?: ''
          ^^^^
  ```

- Warning: `modules/local/extract/main.nf:52:9`: Variable was declared but not used

  ```nextflow
      def args = task.ext.args ?: ''
          ^^^^
  ```

- Warning: `modules/local/qc/align/main.nf:25:9`: Variable was declared but not used

  ```nextflow
      def args = task.ext.args ?: ''
          ^^^^
  ```

- Warning: `modules/local/qc/report/main.nf:14:15`: Variable was declared but not used

  ```nextflow
      tuple val(meta), path(rds)
                ^^^^
  ```

- Warning: `modules/local/wget/main.nf:37:9`: Variable was declared but not used

  ```nextflow
      def args = task.ext.args ?: ""
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

- Warning: `modules/nf-core/custom/dumpsoftwareversions/main.nf:22:9`: Variable was declared but not used

  ```nextflow
      def args = task.ext.args ?: ''
          ^^^^
  ```

- Warning: `modules/nf-core/gunzip/main.nf:43:9`: Variable was declared but not used

  ```nextflow
      def args        = task.ext.args ?: ''
          ^^^^
  ```

- Warning: `nextflow.config:262:125`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          afterText = """${manifest.doi ? "* The pipeline\n" : ""}${manifest.doi.tokenize(",").collect { "  https://doi.org/${it.trim().replace('https://doi.org/','')}"}.join("\n")}${manifest.doi ? "\n" : ""}
                                                                                                                              ^^
  ```

- Warning: `subworkflows/local/align_reads.nf:17:19`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_versions = Channel.empty()
                    ^^^^^^^
  ```

- Warning: `subworkflows/local/demultiplex_reads.nf:20:19`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_versions = Channel.empty()
                    ^^^^^^^
  ```

- Warning: `subworkflows/local/prepare_genome.nf:23:24`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_versions      = Channel.empty()
                         ^^^^^^^
  ```

- Warning: `subworkflows/local/prepare_genome.nf:24:24`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_fasta         = Channel.empty()
                         ^^^^^^^
  ```

- Warning: `subworkflows/local/prepare_genome.nf:25:24`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_gtf           = Channel.empty()
                         ^^^^^^^
  ```

- Warning: `subworkflows/local/prepare_genome.nf:26:24`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_bowtie2_index = Channel.empty()
                         ^^^^^^^
  ```

- Warning: `subworkflows/local/prepare_genome.nf:27:24`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_star_index    = Channel.empty()
                         ^^^^^^^
  ```

- Warning: `subworkflows/local/prepare_genome.nf:33:95`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          ch_fasta    = GUNZIP_FASTA ( [ [:], file(fasta, checkIfExists: true) ] ).gunzip.map { it[1] }
                                                                                                ^^
  ```

- Warning: `subworkflows/local/prepare_genome.nf:36:20`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
          ch_fasta = Channel.value(file(fasta, checkIfExists: true))
                     ^^^^^^^
  ```

- Warning: `subworkflows/local/prepare_genome.nf:44:91`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          ch_gtf      = GUNZIP_GTF ( [ [:], file(gtf, checkIfExists: true) ] ).gunzip.map { it[1] }
                                                                                            ^^
  ```

- Warning: `subworkflows/local/prepare_genome.nf:47:18`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
          ch_gtf = Channel.value(file(gtf, checkIfExists: true))
                   ^^^^^^^
  ```

- Warning: `subworkflows/local/prepare_genome.nf:71:32`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
              ch_bowtie2_index = Channel.fromPath(bowtie2_index, checkIfExists: true).map { index -> [ [id:"target_index"], index ] }
                                 ^^^^^^^
  ```

- Warning: `subworkflows/local/prepare_genome.nf:80:29`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
              ch_star_index = Channel.fromPath(star_index, checkIfExists: true).map { index -> [ [id:"target_index"], index ] }
                              ^^^^^^^
  ```

- Warning: `subworkflows/local/prepare_pipeline.nf:19:16`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_reads = Channel.empty()
                 ^^^^^^^
  ```

- Warning: `subworkflows/local/prepare_pipeline.nf:20:19`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_versions = Channel.empty()
                    ^^^^^^^
  ```

- Warning: `subworkflows/local/prepare_pipeline.nf:27:19`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          gtf.map { it[1] },
                    ^^
  ```

- Warning: `subworkflows/local/utils_nfcore_marsseq_pipeline/main.nf:31:5`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
      monochrome_logs   // boolean: Do not use coloured log outputs
      ^^^^^^^^^^^^^^^
  ```

- Warning: `subworkflows/local/utils_nfcore_marsseq_pipeline/main.nf:34:5`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
      input             //  string: Path to input samplesheet
      ^^^^^
  ```

- Warning: `subworkflows/local/utils_nfcore_marsseq_pipeline/main.nf:38:19`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_versions = Channel.empty()
                    ^^^^^^^
  ```

- Warning: `subworkflows/local/utils_nfcore_marsseq_pipeline/main.nf:75:5`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      Channel
      ^^^^^^^
  ```

- Warning: `subworkflows/local/velocity.nf:19:19`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_versions = Channel.empty()
                    ^^^^^^^
  ```

- Warning: `subworkflows/nf-core/utils_nextflow_pipeline/main.nf:94:33`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
      catch (NullPointerException e) {
                                  ^
  ```

- Warning: `subworkflows/nf-core/utils_nextflow_pipeline/main.nf:98:24`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
      catch (IOException e) {
                         ^
  ```

- Warning: `subworkflows/nf-core/utils_nfcore_pipeline/main.nf:116:98`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      return ch_versions.unique().map { version -> processVersionsFromYAML(version) }.unique().mix(Channel.of(workflowVersionToYAML()))
                                                                                                   ^^^^^^^
  ```

- Warning: `subworkflows/nf-core/utils_nfcore_pipeline/main.nf:264:22`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
      catch (Exception all) {
                       ^^^
  ```

- Warning: `subworkflows/nf-core/utils_nfcore_pipeline/main.nf:361:26`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          catch (Exception all) {
                           ^^^
  ```

- Warning: `workflows/marsseq.nf:29:1`: Variable was declared but not used

  ```nextflow
  ercc_regions            = file("$projectDir/data/ercc-regions.tsv")
  ^^^^^^^^^^^^
  ```

- Warning: `workflows/marsseq.nf:30:1`: Variable was declared but not used

  ```nextflow
  ch_oligos               = Channel.fromPath("$projectDir/data/oligos.txt", checkIfExists: true)
  ^^^^^^^^^
  ```

- Warning: `workflows/marsseq.nf:30:27`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
  ch_oligos               = Channel.fromPath("$projectDir/data/oligos.txt", checkIfExists: true)
                            ^^^^^^^
  ```

- Warning: `workflows/marsseq.nf:31:1`: Variable was declared but not used

  ```nextflow
  ch_spike_seq            = Channel.fromPath("$projectDir/data/spike-seq.txt", checkIfExists: true)
  ^^^^^^^^^^^^
  ```

- Warning: `workflows/marsseq.nf:31:27`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
  ch_spike_seq            = Channel.fromPath("$projectDir/data/spike-seq.txt", checkIfExists: true)
                            ^^^^^^^
  ```

- Warning: `workflows/marsseq.nf:32:1`: Variable was declared but not used

  ```nextflow
  ch_spike_concentrations = Channel.fromPath("$projectDir/data/spike-concentrations.txt", checkIfExists: true)
  ^^^^^^^^^^^^^^^^^^^^^^^
  ```

- Warning: `workflows/marsseq.nf:32:27`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
  ch_spike_concentrations = Channel.fromPath("$projectDir/data/spike-concentrations.txt", checkIfExists: true)
                            ^^^^^^^
  ```

- Warning: `workflows/marsseq.nf:47:24`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_multiqc_files = Channel.empty()
                         ^^^^^^^
  ```

- Warning: `workflows/marsseq.nf:55:68`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
      ch_multiqc_files = ch_multiqc_files.mix(FASTQC.out.zip.collect{it[1]})
                                                                     ^^
  ```

- Warning: `workflows/marsseq.nf:59:30`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          ch_samplesheet.map { it[0].amp_batches },
                               ^^
  ```

- Warning: `workflows/marsseq.nf:60:30`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          ch_samplesheet.map { it[0].seq_batches },
                               ^^
  ```

- Warning: `workflows/marsseq.nf:61:30`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          ch_samplesheet.map { it[0].well_cells },
                               ^^
  ```

- Warning: `workflows/marsseq.nf:84:42`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
              .groupTuple(by: [0], sort: { it.name })
                                           ^^
  ```

- Warning: `workflows/marsseq.nf:119:34`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
              ch_samplesheet.map { it[0].amp_batches },
                                   ^^
  ```

- Warning: `workflows/marsseq.nf:120:34`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
              ch_samplesheet.map { it[0].well_cells },
                                   ^^
  ```

- Warning: `workflows/marsseq.nf:126:87`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          ch_multiqc_files = ch_multiqc_files.mix(VELOCITY.out.catadapt_multiqc.collect{it[1]}.ifEmpty([]))
                                                                                        ^^
  ```

- Warning: `workflows/marsseq.nf:127:83`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          ch_multiqc_files = ch_multiqc_files.mix(VELOCITY.out.star_multiqc.collect{it[1]}.ifEmpty([]))
                                                                                    ^^
  ```

- Warning: `workflows/marsseq.nf:145:32`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_multiqc_config        = Channel.fromPath(
                                 ^^^^^^^
  ```

- Warning: `workflows/marsseq.nf:148:9`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
          Channel.fromPath(params.multiqc_config, checkIfExists: true) :
          ^^^^^^^
  ```

- Warning: `workflows/marsseq.nf:149:9`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
          Channel.empty()
          ^^^^^^^
  ```

- Warning: `workflows/marsseq.nf:151:9`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
          Channel.fromPath(params.multiqc_logo, checkIfExists: true) :
          ^^^^^^^
  ```

- Warning: `workflows/marsseq.nf:152:9`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
          Channel.empty()
          ^^^^^^^
  ```

- Warning: `workflows/marsseq.nf:156:27`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_workflow_summary = Channel.value(paramsSummaryMultiqc(summary_params))
                            ^^^^^^^
  ```

- Warning: `workflows/marsseq.nf:162:45`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_methods_description                = Channel.value(
                                              ^^^^^^^
  ```
