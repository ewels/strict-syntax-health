# Nextflow lint results

- Generated: 2026-01-16T06:31:49.089545176Z
- Nextflow version: 25.12.0-edge
- Summary: 20 errors, 22 warnings

## :x: Errors

- Error: `conf/modules.config:12:1`: Variable declarations cannot be mixed with config statements

  ```nextflow
  def genome_reference = params.genome_reference.toLowerCase()
  ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  ```

- Error: `conf/modules.config:50:13`: `genome_reference` is not defined

  ```nextflow
              genome_reference != 'grch37' & genome_reference != 'grch38' ? "--genome_reference '${genome_reference}'" : '',
              ^^^^^^^^^^^^^^^^
  ```

- Error: `conf/modules.config:50:44`: `genome_reference` is not defined

  ```nextflow
              genome_reference != 'grch37' & genome_reference != 'grch38' ? "--genome_reference '${genome_reference}'" : '',
                                             ^^^^^^^^^^^^^^^^
  ```

- Error: `conf/modules.config:50:98`: `genome_reference` is not defined

  ```nextflow
              genome_reference != 'grch37' & genome_reference != 'grch38' ? "--genome_reference '${genome_reference}'" : '',
                                                                                                   ^^^^^^^^^^^^^^^^
  ```

- Error: `conf/modules.config:51:13`: `genome_reference` is not defined

  ```nextflow
              genome_reference == 'grch37'                                ? "--genome_reference 'https://grch37.ensembl.org/'" : '',
              ^^^^^^^^^^^^^^^^
  ```

- Error: `conf/modules.config:52:13`: `genome_reference` is not defined

  ```nextflow
              genome_reference == 'grch38'                                ? "--genome_reference 'https://www.ensembl.org'" : '',
              ^^^^^^^^^^^^^^^^
  ```

- Error: `modules/local/mhcflurry/main.nf:11:5`: Invalid process directive

  ```nextflow
      containerOptions = (workflow.containerEngine == 'docker') ? '-u $(id -u) -e "HOME=${HOME}" -v /etc/passwd:/etc/passwd:ro -v /etc/shadow:/etc/shadow:ro -v /etc/group:/etc/group:ro -v $HOME:$HOME' : ''
      ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  ```

- Error: `nextflow.config:371:5`: Variable declarations cannot be mixed with config statements

  ```nextflow
      String co2_timestamp = new java.util.Date().format( 'yyyy-MM-dd_HH-mm-ss')
      ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  ```

- Error: `nextflow.config:372:70`: `co2_timestamp` is not defined

  ```nextflow
      traceFile = "${params.outdir}/pipeline_info/co2footprint_trace_${co2_timestamp}.txt"
                                                                       ^^^^^^^^^^^^^
  ```

- Error: `nextflow.config:373:74`: `co2_timestamp` is not defined

  ```nextflow
      summaryFile = "${params.outdir}/pipeline_info/co2footprint_summary_${co2_timestamp}.txt"
                                                                           ^^^^^^^^^^^^^
  ```

- Error: `nextflow.config:374:72`: `co2_timestamp` is not defined

  ```nextflow
      reportFile = "${params.outdir}/pipeline_info/co2footprint_report_${co2_timestamp}.html"
                                                                         ^^^^^^^^^^^^^
  ```

- Error: `subworkflows/local/mhc_binding_prediction/main.nf:112:5`: `valid_tools` was assigned but not declared

  ```nextflow
      valid_tools = [ 'mhcnuggets', 'mhcnuggetsii', 'mhcflurry', 'netmhcpan', 'netmhciipan' ]
      ^^^^^^^^^^^
  ```

- Error: `subworkflows/local/mhc_binding_prediction/main.nf:113:5`: `tool_list` was assigned but not declared

  ```nextflow
      tool_list = tools.tokenize(',')
      ^^^^^^^^^
  ```

- Error: `subworkflows/local/mhc_binding_prediction/main.nf:115:25`: `tool_list` is not defined

  ```nextflow
      def invalid_tools = tool_list.findAll { it.trim() !in valid_tools }
                          ^^^^^^^^^
  ```

- Error: `subworkflows/local/mhc_binding_prediction/main.nf:115:59`: `valid_tools` is not defined

  ```nextflow
      def invalid_tools = tool_list.findAll { it.trim() !in valid_tools }
                                                            ^^^^^^^^^^^
  ```

- Error: `subworkflows/local/mhc_binding_prediction/main.nf:117:110`: `valid_tools` is not defined

  ```nextflow
          throw new IllegalArgumentException("Invalid tools found: ${invalid_tools.join(',')}.\nValid tools: ${valid_tools.join(',')}")
                                                                                                               ^^^^^^^^^^^
  ```

- Error: `subworkflows/local/mhc_binding_prediction/main.nf:137:5`: `ch_netmhc_exe` was assigned but not declared

  ```nextflow
      ch_netmhc_exe = channel.empty()
      ^^^^^^^^^^^^^
  ```

- Error: `subworkflows/local/mhc_binding_prediction/main.nf:138:5`: `ch_netmhc_exe` is not defined

  ```nextflow
      ch_netmhc_exe.bind([
      ^^^^^^^^^^^^^
  ```

- Error: `subworkflows/local/mhc_binding_prediction/main.nf:147:12`: `ch_netmhc_exe` is not defined

  ```nextflow
      return ch_netmhc_exe
             ^^^^^^^^^^^^^
  ```

- Error: `subworkflows/local/utils_nfcore_epitopeprediction_pipeline/main.nf:116:48`: `readAlleles` is not defined

  ```nextflow
          .map { meta, file -> [meta + [alleles: readAlleles(meta.alleles)], file]} // Parse alleles from file
                                                 ^^^^^^^^^^^
  ```

## :warning: Warnings

- Warning: `modules/local/netmhciipan/main.nf:26:25`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
                          it.contains('DRB') ?
                          ^^
  ```

- Warning: `modules/local/netmhciipan/main.nf:27:29`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
                              it.replace('*', '_').replace(':', '').replace('HLA-', '') :
                              ^^
  ```

- Warning: `modules/local/netmhciipan/main.nf:28:29`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
                              it.replace('*', '').replace(':', '').replace('/','-').replace('H2','H-2')
                              ^^
  ```

- Warning: `modules/local/netmhciipan/main.nf:47:9`: Variable was declared but not used

  ```nextflow
      def args       = task.ext.args ?: ''
          ^^^^
  ```

- Warning: `modules/local/netmhcpan/main.nf:23:66`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
      def alleles = meta.alleles_supported.tokenize(';').collect { it.replace('*', '').replace('H2','H-2') }.join(',')
                                                                   ^^
  ```

- Warning: `modules/local/netmhcpan/main.nf:40:9`: Variable was declared but not used

  ```nextflow
      def args   = task.ext.args ?: ''
          ^^^^
  ```

- Warning: `modules/local/prepare_prediction_input/main.nf:22:9`: Variable was declared but not used

  ```nextflow
      def args       = task.ext.args ?: ''
          ^^^^
  ```

- Warning: `modules/nf-core/bcftools/norm/main.nf:56:65`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          if (['--write-index=tbi', '-W=tbi'].any { args.contains(it) }  && extension == 'vcf.gz') {
                                                                  ^^
  ```

- Warning: `modules/nf-core/bcftools/norm/main.nf:58:126`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          } else if (['--write-index=tbi', '-W=tbi', '--write-index=csi', '-W=csi', '--write-index', '-W'].any { args.contains(it) }) {
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

- Warning: `modules/nf-core/gunzip/main.nf:43:9`: Variable was declared but not used

  ```nextflow
      def args = task.ext.args ?: ''
          ^^^^
  ```

- Warning: `subworkflows/local/mhc_binding_prediction/main.nf:92:49`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          .map { meta, file -> [meta.findAll { k, v -> k != 'alleles_supported' }, file] } // drop alleles_supported from meta
                                                  ^
  ```

- Warning: `subworkflows/local/mhc_binding_prediction/main.nf:115:45`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
      def invalid_tools = tool_list.findAll { it.trim() !in valid_tools }
                                              ^^
  ```

- Warning: `subworkflows/local/utils_nfcore_epitopeprediction_pipeline/main.nf:32:5`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
      monochrome_logs   // boolean: Do not use coloured log outputs
      ^^^^^^^^^^^^^^^
  ```

- Warning: `subworkflows/local/utils_nfcore_epitopeprediction_pipeline/main.nf:35:5`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
      input             //  string: Path to input samplesheet
      ^^^^^
  ```

- Warning: `subworkflows/local/utils_nfcore_epitopeprediction_pipeline/main.nf:101:9`: Variable was declared but not used

  ```nextflow
      def readAlleles = { allele_input ->
          ^^^^^^^^^^^
  ```

- Warning: `subworkflows/local/utils_nfcore_epitopeprediction_pipeline/main.nf:114:5`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      Channel
      ^^^^^^^
  ```

- Warning: `workflows/epitopeprediction.nf:119:79`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
      ch_multiqc_files = ch_multiqc_files.mix(BCFTOOLS_STATS.out.stats.collect{ meta, stats -> stats })
                                                                                ^^^^
  ```

- Warning: `workflows/epitopeprediction.nf:126:24`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
              meta_data, input_file ->
                         ^^^^^^^^^^
  ```

- Warning: `workflows/epitopeprediction.nf:155:19`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          .filter { meta, file -> file.size() > 0 }
                    ^^^^
  ```

- Warning: `workflows/epitopeprediction.nf:205:81`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
      ch_multiqc_files = ch_multiqc_files.mix(SUMMARIZE_RESULTS.out.json.collect{ it[1] })
                                                                                  ^^
  ```
