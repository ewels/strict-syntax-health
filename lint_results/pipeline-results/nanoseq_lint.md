# Nextflow lint results

- Generated: 2026-01-16T10:24:36.533844921Z
- Nextflow version: 25.12.0-edge
- Summary: 36 errors, 43 warnings

## :x: Errors

- Error: `main.nf:18:1`: Included name 'NANOSEQ' is not defined in module '/home/runner/work/strict-syntax-health/strict-syntax-health/pipelines/nanoseq/workflows/nanoseq.nf'

  ```nextflow
  include { NANOSEQ  } from './workflows/nanoseq'
  ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  ```

- Error: `main.nf:53:5`: `NANOSEQ` is not defined

  ```nextflow
      NANOSEQ ()
      ^^^^^^^
  ```

- Error: `main.nf:58:22`: `NANOSEQ` is not defined

  ```nextflow
      multiqc_report = NANOSEQ.out.multiqc_report // channel: /path/to/multiqc_report.html
                       ^^^^^^^
  ```

- Error: `modules/local/blue-crab.nf:14:87`: `blow5` is not defined

  ```nextflow
      tuple val(meta), path(genome), path(gtf), path(fastq), path(bam), path(bai), path(blow5), emit: nanopolish_outputs
                                                                                        ^^^^^
  ```

- Error: `modules/local/blue-crab.nf:22:28`: `blow5` is not defined

  ```nextflow
      blue-crab p2s $pod5 -o $blow5
                             ^^^^^^
  ```

- Error: `modules/local/jaffal.nf:2:5`: Unrecognized process directive `echo`

  ```nextflow
      echo true
      ^^^^^^^^^
  ```

- Error: `modules/local/m6anet_inference.nf:3:5`: Unrecognized process directive `echo`

  ```nextflow
      echo true
      ^^^^^^^^^
  ```

- Error: `modules/nf-core/custom/dumpsoftwareversions/main.nf:1:1`: Statements cannot be mixed with script declarations -- move statements into a process, workflow, or function

  ```nextflow
  def deprecation_message = """
  ^^^
  ```

- Error: `modules/nf-core/custom/dumpsoftwareversions/main.nf:30:18`: `deprecation_message` is not defined

  ```nextflow
      assert true: deprecation_message
                   ^^^^^^^^^^^^^^^^^^^
  ```

- Error: `nextflow.config:343:31`: `manifest` is not defined

  ```nextflow
  \033[0;35m  nf-core/nanoseq ${manifest.version}\033[0m
                                ^^^^^^^^
  ```

- Error: `nextflow.config:346:26`: `manifest` is not defined

  ```nextflow
          afterText = """${manifest.doi ? "\n* The pipeline\n" : ""}${manifest.doi.tokenize(",").collect { "    https://doi.org/${it.trim().replace('https://doi.org/','')}"}.join("\n")}${manifest.doi ? "\n" : ""}
                           ^^^^^^^^
  ```

- Error: `nextflow.config:346:69`: `manifest` is not defined

  ```nextflow
          afterText = """${manifest.doi ? "\n* The pipeline\n" : ""}${manifest.doi.tokenize(",").collect { "    https://doi.org/${it.trim().replace('https://doi.org/','')}"}.join("\n")}${manifest.doi ? "\n" : ""}
                                                                      ^^^^^^^^
  ```

- Error: `nextflow.config:346:186`: `manifest` is not defined

  ```nextflow
          afterText = """${manifest.doi ? "\n* The pipeline\n" : ""}${manifest.doi.tokenize(",").collect { "    https://doi.org/${it.trim().replace('https://doi.org/','')}"}.join("\n")}${manifest.doi ? "\n" : ""}
                                                                                                                                                                                           ^^^^^^^^
  ```

- Error: `nextflow.config:355:22`: `validation` is not defined

  ```nextflow
          beforeText = validation.help.beforeText
                       ^^^^^^^^^^
  ```

- Error: `nextflow.config:356:21`: `validation` is not defined

  ```nextflow
          afterText = validation.help.afterText
                      ^^^^^^^^^^
  ```

- Error: `subworkflows/local/input_check.nf:32:5`: `input_file` was assigned but not declared

  ```nextflow
      input_file            = row.reads //? file(row.reads, checkIfExists: true) : null
      ^^^^^^^^^^
  ```

- Error: `subworkflows/local/input_check.nf:34:5`: `fastq_meta` was assigned but not declared

  ```nextflow
      fastq_meta = [ meta, input_file ]
      ^^^^^^^^^^
  ```

- Error: `subworkflows/local/input_check.nf:34:26`: `input_file` is not defined

  ```nextflow
      fastq_meta = [ meta, input_file ]
                           ^^^^^^^^^^
  ```

- Error: `subworkflows/local/input_check.nf:36:12`: `fastq_meta` is not defined

  ```nextflow
      return fastq_meta
             ^^^^^^^^^^
  ```

- Error: `workflows/nanoseq.nf:14:1`: Statements cannot be mixed with script declarations -- move statements into a process, workflow, or function

  ```nextflow
  checkPathParamList = [ params.input, params.multiqc_config ]
  ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  ```

- Error: `workflows/nanoseq.nf:15:1`: `for` loops are no longer supported

  ```nextflow
  for (param in checkPathParamList) { if (param) { file(param, checkIfExists: true) } }
  ^^^
  ```

- Error: `workflows/nanoseq.nf:15:1`: Statements cannot be mixed with script declarations -- move statements into a process, workflow, or function

  ```nextflow
  for (param in checkPathParamList) { if (param) { file(param, checkIfExists: true) } }
  ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  ```

- Error: `workflows/nanoseq.nf:15:6`: `param` is not defined

  ```nextflow
  for (param in checkPathParamList) { if (param) { file(param, checkIfExists: true) } }
       ^^^^^
  ```

- Error: `workflows/nanoseq.nf:15:40`: `param` is not defined

  ```nextflow
  for (param in checkPathParamList) { if (param) { file(param, checkIfExists: true) } }
                                         ^^^^^^^
  ```

- Error: `workflows/nanoseq.nf:15:55`: `param` is not defined

  ```nextflow
  for (param in checkPathParamList) { if (param) { file(param, checkIfExists: true) } }
                                                        ^^^^^
  ```

- Error: `workflows/nanoseq.nf:18:1`: Statements cannot be mixed with script declarations -- move statements into a process, workflow, or function

  ```nextflow
  if (params.input) {
  ^
  ```

- Error: `workflows/nanoseq.nf:24:1`: Statements cannot be mixed with script declarations -- move statements into a process, workflow, or function

  ```nextflow
  if (params.fasta){
  ^
  ```

- Error: `workflows/nanoseq.nf:34:1`: Statements cannot be mixed with script declarations -- move statements into a process, workflow, or function

  ```nextflow
  if (params.gtf){
  ^
  ```

- Error: `workflows/nanoseq.nf:45:16`: `NXF_OFFLINE` is not defined

  ```nextflow
          return NXF_OFFLINE as Boolean
                 ^^^^^^^^^^^
  ```

- Error: `workflows/nanoseq.nf:52:1`: Statements cannot be mixed with script declarations -- move statements into a process, workflow, or function

  ```nextflow
  if (params.protocol != 'DNA' && params.protocol != 'cDNA' && params.protocol != 'directRNA') {
  ^
  ```

- Error: `workflows/nanoseq.nf:56:1`: Statements cannot be mixed with script declarations -- move statements into a process, workflow, or function

  ```nextflow
  if (!params.skip_demultiplexing) {
  ^
  ```

- Error: `workflows/nanoseq.nf:81:1`: Statements cannot be mixed with script declarations -- move statements into a process, workflow, or function

  ```nextflow
  if (!params.skip_alignment) {
  ^
  ```

- Error: `workflows/nanoseq.nf:90:1`: Statements cannot be mixed with script declarations -- move statements into a process, workflow, or function

  ```nextflow
  if (!params.skip_quantification) {
  ^
  ```

- Error: `workflows/nanoseq.nf:103:1`: Statements cannot be mixed with script declarations -- move statements into a process, workflow, or function

  ```nextflow
  ch_multiqc_config        = file("$baseDir/assets/multiqc_config.yml", checkIfExists: true)
  ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  ```

- Error: `workflows/nanoseq.nf:104:1`: Statements cannot be mixed with script declarations -- move statements into a process, workflow, or function

  ```nextflow
  ch_multiqc_custom_config = params.multiqc_config ? Channel.fromPath(params.multiqc_config) : Channel.empty()
  ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  ```

- Error: `workflows/nanoseq.nf:157:1`: Invalid workflow definition -- check for missing or out-of-order section labels

  ```nextflow
  workflow NANOSEQ{
  ^
  ```

## :warning: Warnings

- Warning: `modules/nf-core/custom/dumpsoftwareversions/main.nf:1:5`: Variable was declared but not used

  ```nextflow
  def deprecation_message = """
      ^^^^^^^^^^^^^^^^^^^
  ```

- Warning: `modules/nf-core/custom/dumpsoftwareversions/main.nf:31:9`: Variable was declared but not used

  ```nextflow
      def args = task.ext.args ?: ''
          ^^^^
  ```

- Warning: `modules/nf-core/custom/getchromsizes/main.nf:23:9`: Variable was declared but not used

  ```nextflow
      def args = task.ext.args ?: ''
          ^^^^
  ```

- Warning: `modules/nf-core/graphmap2/index/main.nf:36:9`: Variable was declared but not used

  ```nextflow
      def args = task.ext.args ?: ''
          ^^^^
  ```

- Warning: `modules/nf-core/minimap2/align/main.nf:67:9`: Variable was declared but not used

  ```nextflow
      def target = reference ?: (bam_input ? error("BAM input requires reference") : reads)
          ^^^^^^
  ```

- Warning: `modules/nf-core/nanolyse/main.nf:23:9`: Variable was declared but not used

  ```nextflow
      def args = task.ext.args ?: ''
          ^^^^
  ```

- Warning: `modules/nf-core/qcat/main.nf:22:9`: Variable was declared but not used

  ```nextflow
      def args = task.ext.args ?: ''
          ^^^^
  ```

- Warning: `modules/nf-core/qcat/main.nf:23:9`: Variable was declared but not used

  ```nextflow
      def prefix = task.ext.prefix ?: "${meta.id}"
          ^^^^^^
  ```

- Warning: `modules/nf-core/toulligqc/main.nf:45:9`: Variable was declared but not used

  ```nextflow
      def args = task.ext.args ?: ''
          ^^^^
  ```

- Warning: `modules/nf-core/ucsc/bedgraphtobigwig/main.nf:23:9`: Variable was declared but not used

  ```nextflow
      def args = task.ext.args ?: ''
          ^^^^
  ```

- Warning: `nextflow.config:346:129`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          afterText = """${manifest.doi ? "\n* The pipeline\n" : ""}${manifest.doi.tokenize(",").collect { "    https://doi.org/${it.trim().replace('https://doi.org/','')}"}.join("\n")}${manifest.doi ? "\n" : ""}
                                                                                                                                  ^^
  ```

- Warning: `subworkflows/local/input_check.nf:19:32`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          .map { get_sample_info(it) }
                                 ^^
  ```

- Warning: `subworkflows/local/qcfastq_nanoplot_fastqc.nf:24:24`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      nanoplot_png     = Channel.empty()
                         ^^^^^^^
  ```

- Warning: `subworkflows/local/qcfastq_nanoplot_fastqc.nf:25:24`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      nanoplot_html    = Channel.empty()
                         ^^^^^^^
  ```

- Warning: `subworkflows/local/qcfastq_nanoplot_fastqc.nf:26:24`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      nanoplot_txt     = Channel.empty()
                         ^^^^^^^
  ```

- Warning: `subworkflows/local/qcfastq_nanoplot_fastqc.nf:27:24`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      nanoplot_log     = Channel.empty()
                         ^^^^^^^
  ```

- Warning: `subworkflows/local/qcfastq_nanoplot_fastqc.nf:28:24`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      nanoplot_version = Channel.empty()
                         ^^^^^^^
  ```

- Warning: `subworkflows/local/qcfastq_nanoplot_fastqc.nf:40:31`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      toulligqc_report_data   = Channel.empty()
                                ^^^^^^^
  ```

- Warning: `subworkflows/local/qcfastq_nanoplot_fastqc.nf:41:31`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      toulligqc_report_html   = Channel.empty()
                                ^^^^^^^
  ```

- Warning: `subworkflows/local/qcfastq_nanoplot_fastqc.nf:42:31`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      toulligqc_plots_html    = Channel.empty()
                                ^^^^^^^
  ```

- Warning: `subworkflows/local/qcfastq_nanoplot_fastqc.nf:43:31`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      toulligqc_plotly_js     = Channel.empty()
                                ^^^^^^^
  ```

- Warning: `subworkflows/local/qcfastq_nanoplot_fastqc.nf:44:31`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      toulligqc_version       = Channel.empty()
                                ^^^^^^^
  ```

- Warning: `subworkflows/local/qcfastq_nanoplot_fastqc.nf:56:22`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      fastqc_zip     = Channel.empty()
                       ^^^^^^^
  ```

- Warning: `subworkflows/local/qcfastq_nanoplot_fastqc.nf:57:22`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      fastqc_html    = Channel.empty()
                       ^^^^^^^
  ```

- Warning: `subworkflows/local/qcfastq_nanoplot_fastqc.nf:58:22`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      fastqc_multiqc = Channel.empty()
                       ^^^^^^^
  ```

- Warning: `subworkflows/local/qcfastq_nanoplot_fastqc.nf:59:22`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      fastqc_version = Channel.empty()
                       ^^^^^^^
  ```

- Warning: `subworkflows/local/quantify_stringtie_featurecounts.nf:19:25`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_annotation_gtf = Channel.from(file(params.gtf))
                          ^^^^^^^
  ```

- Warning: `subworkflows/local/quantify_stringtie_featurecounts.nf:32:48`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
      STRINGTIE_MERGE ( ch_stringtie_gtf.collect{it[1]}, ch_annotation_gtf.unique() )
                                                 ^^
  ```

- Warning: `subworkflows/local/quantify_stringtie_featurecounts.nf:40:42`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          .combine( [ch_sorted_bam.collect{it[1]}])
                                           ^^
  ```

- Warning: `subworkflows/local/quantify_stringtie_featurecounts.nf:45:42`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          .combine( [ch_sorted_bam.collect{it[1]}])
                                           ^^
  ```

- Warning: `subworkflows/local/utils_nfcore_nanoseq_pipeline/main.nf:31:5`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
      monochrome_logs   // boolean: Do not use coloured log outputs
      ^^^^^^^^^^^^^^^
  ```

- Warning: `subworkflows/local/utils_nfcore_nanoseq_pipeline/main.nf:34:5`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
      input             //  string: Path to input samplesheet
      ^^^^^
  ```

- Warning: `subworkflows/local/utils_nfcore_nanoseq_pipeline/main.nf:38:19`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_versions = Channel.empty()
                    ^^^^^^^
  ```

- Warning: `subworkflows/nf-core/bam_stats_samtools/main.nf:15:19`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_versions = Channel.empty()
                    ^^^^^^^
  ```

- Warning: `subworkflows/nf-core/utils_nfcore_pipeline/main.nf:101:98`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      return ch_versions.unique().map { version -> processVersionsFromYAML(version) }.unique().mix(Channel.of(workflowVersionToYAML()))
                                                                                                   ^^^^^^^
  ```

- Warning: `workflows/nanoseq.nf:19:5`: Variable was declared but not used

  ```nextflow
      ch_input = file(params.input)
      ^^^^^^^^
  ```

- Warning: `workflows/nanoseq.nf:47:22`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
      catch( Exception e ) {
                       ^
  ```

- Warning: `workflows/nanoseq.nf:58:9`: Params should be declared at the top-level (i.e. outside the workflow)

  ```nextflow
          params.barcode_kit = 'Auto'
          ^^^^^^
  ```

- Warning: `workflows/nanoseq.nf:70:33`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
                  ch_input_path = Channel.fromPath(params.input_path, checkIfExists: true)
                                  ^^^^^^^
  ```

- Warning: `workflows/nanoseq.nf:103:1`: Variable was declared but not used

  ```nextflow
  ch_multiqc_config        = file("$baseDir/assets/multiqc_config.yml", checkIfExists: true)
  ^^^^^^^^^^^^^^^^^
  ```

- Warning: `workflows/nanoseq.nf:104:1`: Variable was declared but not used

  ```nextflow
  ch_multiqc_custom_config = params.multiqc_config ? Channel.fromPath(params.multiqc_config) : Channel.empty()
  ^^^^^^^^^^^^^^^^^^^^^^^^
  ```

- Warning: `workflows/nanoseq.nf:104:52`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
  ch_multiqc_custom_config = params.multiqc_config ? Channel.fromPath(params.multiqc_config) : Channel.empty()
                                                     ^^^^^^^
  ```

- Warning: `workflows/nanoseq.nf:104:94`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
  ch_multiqc_custom_config = params.multiqc_config ? Channel.fromPath(params.multiqc_config) : Channel.empty()
                                                                                               ^^^^^^^
  ```
