# Nextflow lint results

- Generated: 2026-01-16T06:41:25.035649464Z
- Nextflow version: 25.12.0-edge
- Summary: 50 errors, 9 warnings

## :x: Errors

- Error: `conf/base.config:14:16`: `check_max` is not defined

  ```nextflow
      cpus   = { check_max( 1    * task.attempt, 'cpus'   ) }
                 ^^^^^^^^^
  ```

- Error: `conf/base.config:15:16`: `check_max` is not defined

  ```nextflow
      memory = { check_max( 6.GB * task.attempt, 'memory' ) }
                 ^^^^^^^^^
  ```

- Error: `conf/base.config:16:16`: `check_max` is not defined

  ```nextflow
      time   = { check_max( 4.h  * task.attempt, 'time'   ) }
                 ^^^^^^^^^
  ```

- Error: `conf/base.config:30:20`: `check_max` is not defined

  ```nextflow
          cpus   = { check_max( 1                  , 'cpus'    ) }
                     ^^^^^^^^^
  ```

- Error: `conf/base.config:31:20`: `check_max` is not defined

  ```nextflow
          memory = { check_max( 6.GB * task.attempt, 'memory'  ) }
                     ^^^^^^^^^
  ```

- Error: `conf/base.config:32:20`: `check_max` is not defined

  ```nextflow
          time   = { check_max( 4.h  * task.attempt, 'time'    ) }
                     ^^^^^^^^^
  ```

- Error: `conf/base.config:35:20`: `check_max` is not defined

  ```nextflow
          cpus   = { check_max( 2     * task.attempt, 'cpus'    ) }
                     ^^^^^^^^^
  ```

- Error: `conf/base.config:36:20`: `check_max` is not defined

  ```nextflow
          memory = { check_max( 12.GB * task.attempt, 'memory'  ) }
                     ^^^^^^^^^
  ```

- Error: `conf/base.config:37:20`: `check_max` is not defined

  ```nextflow
          time   = { check_max( 4.h   * task.attempt, 'time'    ) }
                     ^^^^^^^^^
  ```

- Error: `conf/base.config:40:20`: `check_max` is not defined

  ```nextflow
          cpus   = { check_max( 6     * task.attempt, 'cpus'    ) }
                     ^^^^^^^^^
  ```

- Error: `conf/base.config:41:20`: `check_max` is not defined

  ```nextflow
          memory = { check_max( 36.GB * task.attempt, 'memory'  ) }
                     ^^^^^^^^^
  ```

- Error: `conf/base.config:42:20`: `check_max` is not defined

  ```nextflow
          time   = { check_max( 8.h   * task.attempt, 'time'    ) }
                     ^^^^^^^^^
  ```

- Error: `conf/base.config:45:20`: `check_max` is not defined

  ```nextflow
          cpus   = { check_max( 12    * task.attempt, 'cpus'    ) }
                     ^^^^^^^^^
  ```

- Error: `conf/base.config:46:20`: `check_max` is not defined

  ```nextflow
          memory = { check_max( 72.GB * task.attempt, 'memory'  ) }
                     ^^^^^^^^^
  ```

- Error: `conf/base.config:47:20`: `check_max` is not defined

  ```nextflow
          time   = { check_max( 16.h  * task.attempt, 'time'    ) }
                     ^^^^^^^^^
  ```

- Error: `conf/base.config:50:20`: `check_max` is not defined

  ```nextflow
          time   = { check_max( 20.h  * task.attempt, 'time'    ) }
                     ^^^^^^^^^
  ```

- Error: `conf/base.config:53:20`: `check_max` is not defined

  ```nextflow
          memory = { check_max( 200.GB * task.attempt, 'memory' ) }
                     ^^^^^^^^^
  ```

- Error: `main.nf:20:1`: Module could not be parsed: '/home/runner/work/strict-syntax-health/strict-syntax-health/pipelines/spinningjenny/workflows/spinningjenny/main.nf'

  ```nextflow
  include { SPINNINGJENNY  } from './workflows/spinningjenny'
  ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  ```

- Error: `main.nf:50:5`: `SPINNINGJENNY` is not defined

  ```nextflow
      SPINNINGJENNY (
      ^^^^^^^^^^^^^
  ```

- Error: `modules/local/rplot.nf:5:5`: Invalid process directive

  ```nextflow
      errorStrategy = 'ignore'
      ^^^^^^^^^^^^^^^^^^^^^^^^
  ```

- Error: `nextflow.config:77:5`: Unexpected input: 'includeConfig'

  ```nextflow
      includeConfig "${params.custom_config_base}/nfcore_custom.config"
      ^
  ```

- Error: `subworkflows/local/utils_nfcore_spinningjenny_pipeline/main.nf:14:1`: Module could not be parsed: '/home/runner/work/strict-syntax-health/strict-syntax-health/pipelines/spinningjenny/subworkflows/nf-core/utils_nextflow_pipeline/main.nf'

  ```nextflow
  include { UTILS_NEXTFLOW_PIPELINE   } from '../../nf-core/utils_nextflow_pipeline'
  ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  ```

- Error: `subworkflows/local/utils_nfcore_spinningjenny_pipeline/main.nf:47:5`: `UTILS_NEXTFLOW_PIPELINE` is not defined

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

- Error: `workflows/spinningjenny/main.nf:92:16`: Unexpected input: '='

  ```nextflow
          for (i = fin; i > start; i-=step) {
                 ^
  ```

## :warning: Warnings

- Warning: `subworkflows/local/utils_nfcore_spinningjenny_pipeline/main.nf:38:5`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
      input             //  string: Path to input samplesheet
      ^^^^^
  ```

- Warning: `subworkflows/local/utils_nfcore_spinningjenny_pipeline/main.nf:42:19`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_versions = Channel.empty()
                    ^^^^^^^
  ```

- Warning: `subworkflows/local/utils_nfcore_spinningjenny_pipeline/main.nf:83:5`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      Channel
      ^^^^^^^
  ```

- Warning: `subworkflows/local/utils_nfcore_spinningjenny_pipeline/main.nf:95:38`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
              validateInputSamplesheet(it)
                                       ^^
  ```

- Warning: `subworkflows/local/utils_nfcore_spinningjenny_pipeline/main.nf:164:39`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
      def endedness_ok = metas.collect{ it.single_end }.unique().size == 1
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
