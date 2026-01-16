# Nextflow lint results

- Generated: 2026-01-16T10:27:12.824567503Z
- Nextflow version: 25.12.0-edge
- Summary: 53 errors, 49 warnings

## :x: Errors

- Error: `conf/base.config:13:16`: `check_max` is not defined

  ```nextflow
      cpus   = { check_max( 1    * task.attempt, 'cpus'   ) }
                 ^^^^^^^^^
  ```

- Error: `conf/base.config:14:16`: `check_max` is not defined

  ```nextflow
      memory = { check_max( 6.GB * task.attempt, 'memory' ) }
                 ^^^^^^^^^
  ```

- Error: `conf/base.config:15:16`: `check_max` is not defined

  ```nextflow
      time   = { check_max( 4.h  * task.attempt, 'time'   ) }
                 ^^^^^^^^^
  ```

- Error: `conf/base.config:28:20`: `check_max` is not defined

  ```nextflow
          cpus   = { check_max( 1                  , 'cpus'    ) }
                     ^^^^^^^^^
  ```

- Error: `conf/base.config:29:20`: `check_max` is not defined

  ```nextflow
          memory = { check_max( 6.GB * task.attempt, 'memory'  ) }
                     ^^^^^^^^^
  ```

- Error: `conf/base.config:30:20`: `check_max` is not defined

  ```nextflow
          time   = { check_max( 4.h  * task.attempt, 'time'    ) }
                     ^^^^^^^^^
  ```

- Error: `conf/base.config:33:20`: `check_max` is not defined

  ```nextflow
          cpus   = { check_max( 2     * task.attempt, 'cpus'    ) }
                     ^^^^^^^^^
  ```

- Error: `conf/base.config:34:20`: `check_max` is not defined

  ```nextflow
          memory = { check_max( 12.GB * task.attempt, 'memory'  ) }
                     ^^^^^^^^^
  ```

- Error: `conf/base.config:35:20`: `check_max` is not defined

  ```nextflow
          time   = { check_max( 4.h   * task.attempt, 'time'    ) }
                     ^^^^^^^^^
  ```

- Error: `conf/base.config:38:20`: `check_max` is not defined

  ```nextflow
          cpus   = { check_max( 6     * task.attempt, 'cpus'    ) }
                     ^^^^^^^^^
  ```

- Error: `conf/base.config:39:20`: `check_max` is not defined

  ```nextflow
          memory = { check_max( 36.GB * task.attempt, 'memory'  ) }
                     ^^^^^^^^^
  ```

- Error: `conf/base.config:40:20`: `check_max` is not defined

  ```nextflow
          time   = { check_max( 8.h   * task.attempt, 'time'    ) }
                     ^^^^^^^^^
  ```

- Error: `conf/base.config:43:20`: `check_max` is not defined

  ```nextflow
          cpus   = { check_max( 12    * task.attempt, 'cpus'    ) }
                     ^^^^^^^^^
  ```

- Error: `conf/base.config:44:20`: `check_max` is not defined

  ```nextflow
          memory = { check_max( 72.GB * task.attempt, 'memory'  ) }
                     ^^^^^^^^^
  ```

- Error: `conf/base.config:45:20`: `check_max` is not defined

  ```nextflow
          time   = { check_max( 16.h  * task.attempt, 'time'    ) }
                     ^^^^^^^^^
  ```

- Error: `conf/base.config:48:20`: `check_max` is not defined

  ```nextflow
          time   = { check_max( 20.h  * task.attempt, 'time'    ) }
                     ^^^^^^^^^
  ```

- Error: `conf/base.config:51:20`: `check_max` is not defined

  ```nextflow
          memory = { check_max( 200.GB * task.attempt, 'memory' ) }
                     ^^^^^^^^^
  ```

- Error: `main.nf:34:1`: Statements cannot be mixed with script declarations -- move statements into a process, workflow, or function

  ```nextflow
  if (!params.fasta) {
  ^
  ```

- Error: `modules/local/insilicoseq/generate/main.nf:26:9`: `input_format` is already declared

  ```nextflow
      def input_format  = input_format == "genomes" ? "--genomes": "--draft"
          ^^^^^^^^^^^^
  ```

- Error: `modules/local/uncompress_fasta/main.nf:2:10`: `file` is not defined

  ```nextflow
      tag "$file"
           ^^^^^
  ```

- Error: `modules/nf-core/multiqc/main.nf:28:31`: Unexpected input: '/'

  ```nextflow
      def logo = multiqc_logo ? /--cl-config 'custom_logo: "${multiqc_logo}"'/ : ''
                                ^
  ```

- Error: `nextflow.config:123:5`: Unexpected input: 'includeConfig'

  ```nextflow
      includeConfig "${params.custom_config_base}/nfcore_custom.config"
      ^
  ```

- Error: `subworkflows/local/utils_nfcore_readsimulator_pipeline/main.nf:14:1`: Module could not be parsed: '/home/runner/work/strict-syntax-health/strict-syntax-health/pipelines/readsimulator/subworkflows/nf-core/utils_nextflow_pipeline/main.nf'

  ```nextflow
  include { UTILS_NEXTFLOW_PIPELINE   } from '../../nf-core/utils_nextflow_pipeline'
  ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  ```

- Error: `subworkflows/local/utils_nfcore_readsimulator_pipeline/main.nf:47:5`: `UTILS_NEXTFLOW_PIPELINE` is not defined

  ```nextflow
      UTILS_NEXTFLOW_PIPELINE (
      ^^^^^^^^^^^^^^^^^^^^^^^
  ```

- Error: `subworkflows/nf-core/utils_nextflow_pipeline/main.nf:111:14`: Unexpected input: 'i'

  ```nextflow
      for (int i = 0; i < n - 1; i++) {
               ^
  ```

- Error: `subworkflows/nf-core/utils_nfcore_pipeline/main.nf:5:1`: Groovy `import` declarations are not supported -- use fully-qualified name inline instead

  ```nextflow
  import org.yaml.snakeyaml.Yaml
  ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  ```

- Error: `subworkflows/nf-core/utils_nfcore_pipeline/main.nf:6:1`: Groovy `import` declarations are not supported -- use fully-qualified name inline instead

  ```nextflow
  import nextflow.extension.FilesEx
  ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  ```

- Error: `subworkflows/nf-core/utils_nfcore_pipeline/main.nf:37:5`: `valid_config` was assigned but not declared

  ```nextflow
      valid_config = true
      ^^^^^^^^^^^^
  ```

- Error: `subworkflows/nf-core/utils_nfcore_pipeline/main.nf:45:9`: `valid_config` was assigned but not declared

  ```nextflow
          valid_config = false
          ^^^^^^^^^^^^
  ```

- Error: `subworkflows/nf-core/utils_nfcore_pipeline/main.nf:47:12`: `valid_config` is not defined

  ```nextflow
      return valid_config
             ^^^^^^^^^^^^
  ```

- Error: `subworkflows/nf-core/utils_nfcore_pipeline/main.nf:99:17`: `Yaml` is not defined

  ```nextflow
      Yaml yaml = new Yaml()
                  ^^^^^^^^^^
  ```

- Error: `subworkflows/nf-core/utils_nfcore_pipeline/main.nf:100:5`: `versions` was assigned but not declared

  ```nextflow
      versions = yaml.load(yaml_file).collectEntries { k, v -> [ k.tokenize(':')[-1], v ] }
      ^^^^^^^^
  ```

- Error: `subworkflows/nf-core/utils_nfcore_pipeline/main.nf:101:27`: `versions` is not defined

  ```nextflow
      return yaml.dumpAsMap(versions).trim()
                            ^^^^^^^^
  ```

- Error: `subworkflows/nf-core/utils_nfcore_pipeline/main.nf:131:5`: `for` loops are no longer supported

  ```nextflow
      for (group in summary_params.keySet()) {
      ^^^
  ```

- Error: `subworkflows/nf-core/utils_nfcore_pipeline/main.nf:131:10`: `group` is not defined

  ```nextflow
      for (group in summary_params.keySet()) {
           ^^^^^
  ```

- Error: `subworkflows/nf-core/utils_nfcore_pipeline/main.nf:132:47`: `group` is not defined

  ```nextflow
          def group_params = summary_params.get(group)  // This gets the parameters of that particular group
                                                ^^^^^
  ```

- Error: `subworkflows/nf-core/utils_nfcore_pipeline/main.nf:134:68`: `group` is not defined

  ```nextflow
              summary_section += "    <p style=\"font-size:110%\"><b>$group</b></p>\n"
                                                                     ^^^^^^
  ```

- Error: `subworkflows/nf-core/utils_nfcore_pipeline/main.nf:136:13`: `for` loops are no longer supported

  ```nextflow
              for (param in group_params.keySet()) {
              ^^^
  ```

- Error: `subworkflows/nf-core/utils_nfcore_pipeline/main.nf:136:18`: `param` is not defined

  ```nextflow
              for (param in group_params.keySet()) {
                   ^^^^^
  ```

- Error: `subworkflows/nf-core/utils_nfcore_pipeline/main.nf:137:49`: `param` is not defined

  ```nextflow
                  summary_section += "        <dt>$param</dt><dd><samp>${group_params.get(param) ?: '<span style=\"color:#999999;\">N/A</a>'}</samp></dd>\n"
                                                  ^^^^^^
  ```

- Error: `subworkflows/nf-core/utils_nfcore_pipeline/main.nf:137:89`: `param` is not defined

  ```nextflow
                  summary_section += "        <dt>$param</dt><dd><samp>${group_params.get(param) ?: '<span style=\"color:#999999;\">N/A</a>'}</samp></dd>\n"
                                                                                          ^^^^^
  ```

- Error: `subworkflows/nf-core/utils_nfcore_pipeline/main.nf:284:5`: `for` loops are no longer supported

  ```nextflow
      for (group in summary_params.keySet()) {
      ^^^
  ```

- Error: `subworkflows/nf-core/utils_nfcore_pipeline/main.nf:284:10`: `group` is not defined

  ```nextflow
      for (group in summary_params.keySet()) {
           ^^^^^
  ```

- Error: `subworkflows/nf-core/utils_nfcore_pipeline/main.nf:285:34`: `group` is not defined

  ```nextflow
          summary << summary_params[group]
                                   ^^^^^^^
  ```

- Error: `subworkflows/nf-core/utils_nfcore_pipeline/main.nf:344:42`: `GroovyException` is not defined

  ```nextflow
              if (plaintext_email) { throw GroovyException('Send plaintext e-mail, not HTML') }
                                           ^^^^^^^^^^^^^^^
  ```

- Error: `subworkflows/nf-core/utils_nfcore_pipeline/main.nf:361:5`: `FilesEx` is not defined

  ```nextflow
      FilesEx.copyTo(output_hf.toPath(), "${outdir}/pipeline_info/pipeline_report.html");
      ^^^^^^^
  ```

- Error: `subworkflows/nf-core/utils_nfcore_pipeline/main.nf:367:5`: `FilesEx` is not defined

  ```nextflow
      FilesEx.copyTo(output_tf.toPath(), "${outdir}/pipeline_info/pipeline_report.txt");
      ^^^^^^^
  ```

- Error: `subworkflows/nf-core/utils_nfcore_pipeline/main.nf:392:5`: `for` loops are no longer supported

  ```nextflow
      for (group in summary_params.keySet()) {
      ^^^
  ```

- Error: `subworkflows/nf-core/utils_nfcore_pipeline/main.nf:392:10`: `group` is not defined

  ```nextflow
      for (group in summary_params.keySet()) {
           ^^^^^
  ```

- Error: `subworkflows/nf-core/utils_nfcore_pipeline/main.nf:393:34`: `group` is not defined

  ```nextflow
          summary << summary_params[group]
                                   ^^^^^^^
  ```

- Error: `workflows/readsimulator/main.nf:8:1`: Module could not be parsed: '/home/runner/work/strict-syntax-health/strict-syntax-health/pipelines/readsimulator/modules/nf-core/multiqc/main.nf'

  ```nextflow
  include { MULTIQC                     } from '../../modules/nf-core/multiqc/main'
  ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  ```

- Error: `workflows/readsimulator/main.nf:197:5`: `MULTIQC` is not defined

  ```nextflow
      MULTIQC (
      ^^^^^^^
  ```

- Error: `workflows/readsimulator/main.nf:207:23`: `MULTIQC` is not defined

  ```nextflow
      multiqc_report  = MULTIQC.out.report.toList() // channel: /path/to/multiqc_report.html
                        ^^^^^^^
  ```

## :warning: Warnings

- Warning: `main.nf:35:5`: Params should be declared at the top-level (i.e. outside the workflow)

  ```nextflow
      params.fasta = getGenomeAttribute('fasta')
      ^^^^^^
  ```

- Warning: `modules/local/custom/create_samplesheet/main.nf:26:57`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
      samplesheet  = pipeline_map.keySet().collect{ '"' + it + '"'}.join(",") + '\n'
                                                          ^^
  ```

- Warning: `modules/local/custom/create_samplesheet/main.nf:27:57`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
      samplesheet += pipeline_map.values().collect{ '"' + it + '"'}.join(",")
                                                          ^^
  ```

- Warning: `modules/local/custom/merge_samplesheets/main.nf:20:9`: Variable was declared but not used

  ```nextflow
      def args    = task.ext.args ?: ''
          ^^^^
  ```

- Warning: `modules/nf-core/fastqc/main.nf:27:48`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
      def renamed_files = old_new_pairs.collect{ old_name, new_name -> new_name }.join(' ')
                                                 ^^^^^^^^
  ```

- Warning: `modules/nf-core/ncbigenomedownload/main.nf:37:9`: Variable was declared but not used

  ```nextflow
      def prefix         = task.ext.prefix ?: "${meta.id}"
          ^^^^^^
  ```

- Warning: `subworkflows/local/amplicon_workflow.nf:16:20`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_ref_fasta = Channel.empty()
                     ^^^^^^^
  ```

- Warning: `subworkflows/local/amplicon_workflow.nf:17:19`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_versions = Channel.empty()
                    ^^^^^^^
  ```

- Warning: `subworkflows/local/amplicon_workflow.nf:47:13`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
              it = [ it[2], it[1] ]
              ^^
  ```

- Warning: `subworkflows/local/amplicon_workflow.nf:47:20`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
              it = [ it[2], it[1] ]
                     ^^
  ```

- Warning: `subworkflows/local/amplicon_workflow.nf:47:27`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
              it = [ it[2], it[1] ]
                            ^^
  ```

- Warning: `subworkflows/local/target_capture_workflow.nf:20:19`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_versions = Channel.empty()
                    ^^^^^^^
  ```

- Warning: `subworkflows/local/target_capture_workflow.nf:26:23`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
          ch_zip_file = Channel.fromPath(params.probe_ref_db[params.probe_ref_name]["url"])
                        ^^^^^^^
  ```

- Warning: `subworkflows/local/target_capture_workflow.nf:93:43`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
      ch_capsim_input = ch_meta_fasta.map { it = it[1] }
                                            ^^
  ```

- Warning: `subworkflows/local/target_capture_workflow.nf:93:48`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
      ch_capsim_input = ch_meta_fasta.map { it = it[1] }
                                                 ^^
  ```

- Warning: `subworkflows/local/target_capture_workflow.nf:94:52`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          .combine ( BOWTIE2_ALIGN.out.aligned.map { it = it[1] } )
                                                     ^^
  ```

- Warning: `subworkflows/local/target_capture_workflow.nf:94:57`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          .combine ( BOWTIE2_ALIGN.out.aligned.map { it = it[1] } )
                                                          ^^
  ```

- Warning: `subworkflows/local/target_capture_workflow.nf:95:49`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          .combine ( SAMTOOLS_INDEX.out.bai.map { it = it[1] } )
                                                  ^^
  ```

- Warning: `subworkflows/local/target_capture_workflow.nf:95:54`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          .combine ( SAMTOOLS_INDEX.out.bai.map { it = it[1] } )
                                                       ^^
  ```

- Warning: `subworkflows/local/target_capture_workflow.nf:104:16`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_reads = Channel.empty()
                 ^^^^^^^
  ```

- Warning: `subworkflows/local/utils_nfcore_readsimulator_pipeline/main.nf:38:5`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
      input             //  string: Path to input samplesheet
      ^^^^^
  ```

- Warning: `subworkflows/local/utils_nfcore_readsimulator_pipeline/main.nf:42:19`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_versions = Channel.empty()
                    ^^^^^^^
  ```

- Warning: `subworkflows/local/utils_nfcore_readsimulator_pipeline/main.nf:83:5`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      Channel
      ^^^^^^^
  ```

- Warning: `subworkflows/local/utils_nfcore_readsimulator_pipeline/main.nf:87:38`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
              validateInputSamplesheet(it)
                                       ^^
  ```

- Warning: `subworkflows/nf-core/utils_nfcore_pipeline/main.nf:121:48`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
                  .map { processVersionsFromYAML(it) }
                                                 ^^
  ```

- Warning: `subworkflows/nf-core/utils_nfcore_pipeline/main.nf:123:22`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
                  .mix(Channel.of(workflowVersionToYAML()))
                       ^^^^^^^
  ```

- Warning: `subworkflows/nf-core/utils_nfcore_pipeline/main.nf:264:14`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
      } catch (all) {
               ^^^
  ```

- Warning: `subworkflows/nf-core/utils_nfcore_pipeline/main.nf:350:18`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          } catch (all) {
                   ^^^
  ```

- Warning: `workflows/readsimulator/main.nf:35:26`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_versions        = Channel.empty()
                           ^^^^^^^
  ```

- Warning: `workflows/readsimulator/main.nf:36:26`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_multiqc_files   = Channel.empty()
                           ^^^^^^^
  ```

- Warning: `workflows/readsimulator/main.nf:37:26`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_simulated_reads = Channel.empty()
                           ^^^^^^^
  ```

- Warning: `workflows/readsimulator/main.nf:38:26`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_taxids          = Channel.empty()
                           ^^^^^^^
  ```

- Warning: `workflows/readsimulator/main.nf:39:26`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_accessions      = Channel.empty()
                           ^^^^^^^
  ```

- Warning: `workflows/readsimulator/main.nf:40:26`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_fasta           = Channel.empty()
                           ^^^^^^^
  ```

- Warning: `workflows/readsimulator/main.nf:43:20`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
          ch_fasta = Channel.fromPath(params.fasta)
                     ^^^^^^^
  ```

- Warning: `workflows/readsimulator/main.nf:46:29`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
              ch_accessions = Channel.fromPath(params.ncbidownload_accessions)
                              ^^^^^^^
  ```

- Warning: `workflows/readsimulator/main.nf:48:25`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
              ch_taxids = Channel.fromPath(params.ncbidownload_taxids)
                          ^^^^^^^
  ```

- Warning: `workflows/readsimulator/main.nf:70:17`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
                  meta, fasta ->
                  ^^^^
  ```

- Warning: `workflows/readsimulator/main.nf:76:21`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
          ch_probes = Channel.fromPath(params.probe_file)
                      ^^^^^^^
  ```

- Warning: `workflows/readsimulator/main.nf:78:21`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
          ch_probes = Channel.empty()
                      ^^^^^^^
  ```

- Warning: `workflows/readsimulator/main.nf:156:23`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
              datatype, old_meta, samplesheet ->
                        ^^^^^^^^
  ```

- Warning: `workflows/readsimulator/main.nf:173:68`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
      ch_multiqc_files = ch_multiqc_files.mix(FASTQC.out.zip.collect{it[1]})
                                                                     ^^
  ```

- Warning: `workflows/readsimulator/main.nf:186:45`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_multiqc_config                     = Channel.fromPath("$projectDir/assets/multiqc_config.yml", checkIfExists: true)
                                              ^^^^^^^
  ```

- Warning: `workflows/readsimulator/main.nf:187:69`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_multiqc_custom_config              = params.multiqc_config ? Channel.fromPath(params.multiqc_config, checkIfExists: true) : Channel.empty()
                                                                      ^^^^^^^
  ```

- Warning: `workflows/readsimulator/main.nf:187:132`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_multiqc_custom_config              = params.multiqc_config ? Channel.fromPath(params.multiqc_config, checkIfExists: true) : Channel.empty()
                                                                                                                                     ^^^^^^^
  ```

- Warning: `workflows/readsimulator/main.nf:188:67`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_multiqc_logo                       = params.multiqc_logo ? Channel.fromPath(params.multiqc_logo, checkIfExists: true) : Channel.empty()
                                                                    ^^^^^^^
  ```

- Warning: `workflows/readsimulator/main.nf:188:128`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_multiqc_logo                       = params.multiqc_logo ? Channel.fromPath(params.multiqc_logo, checkIfExists: true) : Channel.empty()
                                                                                                                                 ^^^^^^^
  ```

- Warning: `workflows/readsimulator/main.nf:190:45`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_workflow_summary                   = Channel.value(paramsSummaryMultiqc(summary_params))
                                              ^^^^^^^
  ```

- Warning: `workflows/readsimulator/main.nf:192:45`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_methods_description                = Channel.value(methodsDescriptionText(ch_multiqc_custom_methods_description))
                                              ^^^^^^^
  ```
