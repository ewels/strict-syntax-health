# Nextflow lint results

- Generated: 2026-01-16T06:36:48.706092082Z
- Nextflow version: 25.12.0-edge
- Summary: 59 errors, 98 warnings

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

- Error: `conf/test_full.config:26:1`: Invalid include source: '/home/runner/work/strict-syntax-health/strict-syntax-health/pipelines/phageannotator/conf/test_data.config'

  ```nextflow
  includeConfig 'test_data.config'
  ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  ```

- Error: `main.nf:28:1`: Module could not be parsed: '/home/runner/work/strict-syntax-health/strict-syntax-health/pipelines/phageannotator/modules/nf-core/multiqc/main.nf'

  ```nextflow
  include { MULTIQC                               } from './modules/nf-core/multiqc/main'
  ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  ```

- Error: `main.nf:43:1`: Module could not be parsed: '/home/runner/work/strict-syntax-health/strict-syntax-health/pipelines/phageannotator/workflows/phageannotator/main.nf'

  ```nextflow
  include { PHAGEANNOTATOR            } from './workflows/phageannotator/main'
  ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  ```

- Error: `main.nf:67:5`: `PHAGEANNOTATOR` is not defined

  ```nextflow
      PHAGEANNOTATOR (
      ^^^^^^^^^^^^^^
  ```

- Error: `main.nf:73:16`: `PHAGEANNOTATOR` is not defined

  ```nextflow
      versions = PHAGEANNOTATOR.out.versions
                 ^^^^^^^^^^^^^^
  ```

- Error: `main.nf:138:5`: `MULTIQC` is not defined

  ```nextflow
      MULTIQC (
      ^^^^^^^
  ```

- Error: `main.nf:145:26`: `MULTIQC` is not defined

  ```nextflow
      ch_multiqc_report  = MULTIQC.out.report.toList() // channel: /path/to/multiqc_report.html
                           ^^^^^^^
  ```

- Error: `modules/nf-core/multiqc/main.nf:28:31`: Unexpected input: '/'

  ```nextflow
      def logo = multiqc_logo ? /--cl-config 'custom_logo: "${multiqc_logo}"'/ : ''
                                ^
  ```

- Error: `nextflow.config:151:5`: Unexpected input: 'includeConfig'

  ```nextflow
      includeConfig "${params.custom_config_base}/nfcore_custom.config"
      ^
  ```

- Error: `subworkflows/local/fasta_all_v_all_blast/main.nf:25:31`: Unexpected input: '='

  ```nextflow
      ch_versions = ch_versions = ch_versions.mix( BLAST_MAKEBLASTDB.out.versions )
                                ^
  ```

- Error: `subworkflows/local/fastq_fasta_contig_extension_cobra/main.nf:49:28`: Unexpected input: '='

  ```nextflow
                  while( line=source.readLine() ) {
                             ^
  ```

- Error: `subworkflows/local/utils_nfcore_phageannotator_pipeline/main.nf:14:1`: Module could not be parsed: '/home/runner/work/strict-syntax-health/strict-syntax-health/pipelines/phageannotator/subworkflows/nf-core/utils_nextflow_pipeline/main.nf'

  ```nextflow
  include { UTILS_NEXTFLOW_PIPELINE   } from '../../nf-core/utils_nextflow_pipeline'
  ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  ```

- Error: `subworkflows/local/utils_nfcore_phageannotator_pipeline/main.nf:47:5`: `UTILS_NEXTFLOW_PIPELINE` is not defined

  ```nextflow
      UTILS_NEXTFLOW_PIPELINE (
      ^^^^^^^^^^^^^^^^^^^^^^^
  ```

- Error: `subworkflows/nf-core/initialise/main.nf:70:13`: `Nextflow` is not defined

  ```nextflow
              Nextflow.error "Profile cannot end with a trailing comma. Please remove the comma from the end of the profile string.\nHint: A common mistake is to provide multiple values to `-profile` separated by spaces. Please use commas to separate profiles instead,e.g., `-profile docker,test`."
              ^^^^^^^^
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

- Error: `tests/nextflow.config:55:1`: Invalid include source: '/home/runner/work/strict-syntax-health/strict-syntax-health/pipelines/phageannotator/tests/https:/github.com/nf-core/modules/raw/master/tests/config/test_data.config'

  ```nextflow
  includeConfig 'https://github.com/nf-core/modules/raw/master/tests/config/test_data.config'
  ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  ```

- Error: `workflows/phageannotator/main.nf:411:32`: Unexpected input: '='

  ```nextflow
                      while( line=source.readLine() ) {
                                 ^
  ```

## :warning: Warnings

- Warning: `main.nf:61:50`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
      ch_fastq_gz = samplesheet.map { meta, fastq, fasta -> return [ meta, fastq ] }
                                                   ^^^^^
  ```

- Warning: `main.nf:62:43`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
      ch_fasta_gz = samplesheet.map { meta, fastq, fasta -> return [ meta, fasta ] }
                                            ^^^^^
  ```

- Warning: `main.nf:85:27`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_versions         = Channel.empty()
                            ^^^^^^^
  ```

- Warning: `main.nf:86:27`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_multiqc_files    = Channel.empty()
                            ^^^^^^^
  ```

- Warning: `main.nf:105:68`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          PIPELINE_INITIALISATION.out.samplesheet.map { meta, fastq, fasta -> return [ meta, fastq ] }
                                                                     ^^^^^
  ```

- Warning: `main.nf:107:68`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
      ch_multiqc_files = ch_multiqc_files.mix(FASTQC.out.zip.collect{it[1]})
                                                                     ^^
  ```

- Warning: `main.nf:127:45`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_multiqc_config                     = Channel.fromPath("$projectDir/assets/multiqc_config.yml", checkIfExists: true)
                                              ^^^^^^^
  ```

- Warning: `main.nf:128:69`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_multiqc_custom_config              = params.multiqc_config ? Channel.fromPath(params.multiqc_config, checkIfExists: true) : Channel.empty()
                                                                      ^^^^^^^
  ```

- Warning: `main.nf:128:132`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_multiqc_custom_config              = params.multiqc_config ? Channel.fromPath(params.multiqc_config, checkIfExists: true) : Channel.empty()
                                                                                                                                     ^^^^^^^
  ```

- Warning: `main.nf:129:67`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_multiqc_logo                       = params.multiqc_logo ? Channel.fromPath(params.multiqc_logo, checkIfExists: true) : Channel.empty()
                                                                    ^^^^^^^
  ```

- Warning: `main.nf:129:128`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_multiqc_logo                       = params.multiqc_logo ? Channel.fromPath(params.multiqc_logo, checkIfExists: true) : Channel.empty()
                                                                                                                                 ^^^^^^^
  ```

- Warning: `main.nf:131:45`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_workflow_summary                   = Channel.value(paramsSummaryMultiqc(summary_params))
                                              ^^^^^^^
  ```

- Warning: `main.nf:133:45`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_methods_description                = Channel.value(methodsDescriptionText(ch_multiqc_custom_methods_description))
                                              ^^^^^^^
  ```

- Warning: `modules/local/anicluster/anicalc/main.nf:21:9`: Variable was declared but not used

  ```nextflow
      def args = task.ext.args ?: ''
          ^^^^
  ```

- Warning: `modules/local/anicluster/anicalc/main.nf:37:9`: Variable was declared but not used

  ```nextflow
      def args = task.ext.args ?: ''
          ^^^^
  ```

- Warning: `modules/local/anicluster/aniclust/main.nf:37:9`: Variable was declared but not used

  ```nextflow
      def args = task.ext.args ?: ''
          ^^^^
  ```

- Warning: `modules/local/anicluster/extractreps/main.nf:21:9`: Variable was declared but not used

  ```nextflow
      def args = task.ext.args ?: ''
          ^^^^
  ```

- Warning: `modules/local/anicluster/extractreps/main.nf:39:9`: Variable was declared but not used

  ```nextflow
      def args = task.ext.args ?: ''
          ^^^^
  ```

- Warning: `modules/local/appendscreenhits/main.nf:22:9`: Variable was declared but not used

  ```nextflow
      def args = task.ext.args ?: ''
          ^^^^
  ```

- Warning: `modules/local/appendscreenhits/main.nf:43:9`: Variable was declared but not used

  ```nextflow
      def args = task.ext.args ?: ''
          ^^^^
  ```

- Warning: `modules/local/coverm/contig/main.nf:38:9`: Variable was declared but not used

  ```nextflow
      def args = task.ext.args ?: ''
          ^^^^
  ```

- Warning: `modules/local/extractviralassemblies/main.nf:21:9`: Variable was declared but not used

  ```nextflow
      def args = task.ext.args ?: ''
          ^^^^
  ```

- Warning: `modules/local/extractviralassemblies/main.nf:37:9`: Variable was declared but not used

  ```nextflow
      def args = task.ext.args ?: ''
          ^^^^
  ```

- Warning: `modules/local/instrain/stb/main.nf:21:9`: Variable was declared but not used

  ```nextflow
      def args = task.ext.args ?: ''
          ^^^^
  ```

- Warning: `modules/local/instrain/stb/main.nf:37:9`: Variable was declared but not used

  ```nextflow
      def args = task.ext.args ?: ''
          ^^^^
  ```

- Warning: `modules/local/mash/paste/main.nf:39:9`: Variable was declared but not used

  ```nextflow
      def args = task.ext.args ?: ''
          ^^^^
  ```

- Warning: `modules/local/qualityfilterviruses/main.nf:42:9`: Variable was declared but not used

  ```nextflow
      def args = task.ext.args ?: ''
          ^^^^
  ```

- Warning: `modules/local/seqkit/seq/main.nf:43:9`: Variable was declared but not used

  ```nextflow
      def args = task.ext.args ?: ''
          ^^^^
  ```

- Warning: `modules/local/seqkit/seq/main.nf:49:9`: Variable was declared but not used

  ```nextflow
      def endswith = task.ext.suffix ?: "${extension}.gz"
          ^^^^^^^^
  ```

- Warning: `modules/local/viromeqc/install/main.nf:32:9`: Variable was declared but not used

  ```nextflow
      def args = task.ext.args ?: ''
          ^^^^
  ```

- Warning: `modules/local/viromeqc/viromeqc/main.nf:41:9`: Variable was declared but not used

  ```nextflow
      def args = task.ext.args ?: ''
          ^^^^
  ```

- Warning: `modules/nf-core/bacphlip/main.nf:23:9`: Variable was declared but not used

  ```nextflow
      def prefix = task.ext.prefix ?: "${meta.id}"
          ^^^^^^
  ```

- Warning: `modules/nf-core/bacphlip/main.nf:37:9`: Variable was declared but not used

  ```nextflow
      def args = task.ext.args ?: ''
          ^^^^
  ```

- Warning: `modules/nf-core/bacphlip/main.nf:38:9`: Variable was declared but not used

  ```nextflow
      def prefix = task.ext.prefix ?: "${meta.id}"
          ^^^^^^
  ```

- Warning: `modules/nf-core/blast/blastn/main.nf:52:9`: Variable was declared but not used

  ```nextflow
      def args = task.ext.args ?: ''
          ^^^^
  ```

- Warning: `modules/nf-core/blast/makeblastdb/main.nf:43:9`: Variable was declared but not used

  ```nextflow
      def args = task.ext.args ?: ''
          ^^^^
  ```

- Warning: `modules/nf-core/bowtie2/align/main.nf:93:9`: Variable was declared but not used

  ```nextflow
      def reference = fasta && extension=="cram"  ? "--reference ${fasta}" : ""
          ^^^^^^^^^
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

- Warning: `modules/nf-core/checkv/downloaddatabase/main.nf:32:9`: Variable was declared but not used

  ```nextflow
      def args = task.ext.args ?: ''
          ^^^^
  ```

- Warning: `modules/nf-core/checkv/endtoend/main.nf:48:9`: Variable was declared but not used

  ```nextflow
      def args = task.ext.args ?: ''
          ^^^^
  ```

- Warning: `modules/nf-core/cobrameta/main.nf:66:9`: Variable was declared but not used

  ```nextflow
      def args = task.ext.args ?: ''
          ^^^^
  ```

- Warning: `modules/nf-core/fastqc/main.nf:27:48`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
      def renamed_files = old_new_pairs.collect{ old_name, new_name -> new_name }.join(' ')
                                                 ^^^^^^^^
  ```

- Warning: `modules/nf-core/genomad/download/main.nf:17:9`: Variable was declared but not used

  ```nextflow
      def args = task.ext.args ?: ''
          ^^^^
  ```

- Warning: `modules/nf-core/genomad/endtoend/main.nf:35:9`: Variable was declared but not used

  ```nextflow
      def prefix = task.ext.prefix ?: "${meta.id}"
          ^^^^^^
  ```

- Warning: `modules/nf-core/genomad/endtoend/main.nf:55:9`: Variable was declared but not used

  ```nextflow
      def args = task.ext.args ?: ''
          ^^^^
  ```

- Warning: `modules/nf-core/genomad/endtoend/main.nf:56:9`: Variable was declared but not used

  ```nextflow
      def prefix = task.ext.prefix ?: "${meta.id}"
          ^^^^^^
  ```

- Warning: `modules/nf-core/instrain/compare/main.nf:28:9`: Variable was declared but not used

  ```nextflow
      def stb_args = stb_file ? "-s ${stb_file}": ''
          ^^^^^^^^
  ```

- Warning: `modules/nf-core/instrain/compare/main.nf:45:9`: Variable was declared but not used

  ```nextflow
      def args = task.ext.args ?: ''
          ^^^^
  ```

- Warning: `modules/nf-core/instrain/compare/main.nf:47:9`: Variable was declared but not used

  ```nextflow
      def stb_args = stb_file ? "-s ${stb_file}": ''
          ^^^^^^^^
  ```

- Warning: `modules/nf-core/instrain/profile/main.nf:52:9`: Variable was declared but not used

  ```nextflow
      def args = task.ext.args ?: ''
          ^^^^
  ```

- Warning: `modules/nf-core/instrain/profile/main.nf:54:9`: Variable was declared but not used

  ```nextflow
      def genes_args = genes_fasta ? "-g ${genes_fasta}": ''
          ^^^^^^^^^^
  ```

- Warning: `modules/nf-core/instrain/profile/main.nf:55:9`: Variable was declared but not used

  ```nextflow
      def stb_args = stb_file ? "-s ${stb_file}": ''
          ^^^^^^^^
  ```

- Warning: `modules/nf-core/iphop/download/main.nf:45:9`: Variable was declared but not used

  ```nextflow
      def args = task.ext.args ?: ''
          ^^^^
  ```

- Warning: `modules/nf-core/iphop/predict/main.nf:26:9`: Variable was declared but not used

  ```nextflow
      def prefix = task.ext.prefix ?: "${meta.id}"
          ^^^^^^
  ```

- Warning: `modules/nf-core/iphop/predict/main.nf:52:9`: Variable was declared but not used

  ```nextflow
      def prefix = task.ext.prefix ?: "${meta.id}"
          ^^^^^^
  ```

- Warning: `modules/nf-core/mash/screen/main.nf:40:9`: Variable was declared but not used

  ```nextflow
      def args = task.ext.args ?: ''
          ^^^^
  ```

- Warning: `modules/nf-core/mash/sketch/main.nf:39:9`: Variable was declared but not used

  ```nextflow
      def args = task.ext.args ?: ''
          ^^^^
  ```

- Warning: `modules/nf-core/pharokka/installdatabases/main.nf:31:9`: Variable was declared but not used

  ```nextflow
      def args = task.ext.args ?: ''
          ^^^^
  ```

- Warning: `modules/nf-core/pharokka/pharokka/main.nf:50:9`: Variable was declared but not used

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

- Warning: `subworkflows/local/fasta_microdiversity_instrain/main.nf:17:19`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_versions = Channel.empty()
                    ^^^^^^^
  ```

- Warning: `subworkflows/local/fasta_microdiversity_instrain/main.nf:20:49`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
      ch_genome_fasta_nometa = genome_fasta.map { it[1] }.first()
                                                  ^^
  ```

- Warning: `subworkflows/local/fasta_microdiversity_instrain/main.nf:22:53`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          ch_proteins_fna_nometa = proteins_fna.map { it[1] }.first()
                                                      ^^
  ```

- Warning: `subworkflows/local/fasta_microdiversity_instrain/main.nf:27:53`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          ch_stb_file_tsv_nometa = instrain_stb.map { it[1] }.first()
                                                      ^^
  ```

- Warning: `subworkflows/local/fasta_microdiversity_instrain/main.nf:41:88`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
      ch_instrain_compare_input = ch_bam_profiles_combined.map { [ [ id:'all_samples' ], it[1], it[2] ] }.groupTuple( sort: 'deep' )
                                                                                         ^^
  ```

- Warning: `subworkflows/local/fasta_microdiversity_instrain/main.nf:41:95`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
      ch_instrain_compare_input = ch_bam_profiles_combined.map { [ [ id:'all_samples' ], it[1], it[2] ] }.groupTuple( sort: 'deep' )
                                                                                                ^^
  ```

- Warning: `subworkflows/local/fasta_microdiversity_instrain/main.nf:46:5`: Variable was declared but not used

  ```nextflow
      ch_instrain_compare = INSTRAIN_COMPARE ( ch_instrain_compare_input, ch_stb_file_tsv_nometa ).compare
      ^^^^^^^^^^^^^^^^^^^
  ```

- Warning: `subworkflows/local/fasta_microdiversity_instrain/main.nf:47:5`: Variable was declared but not used

  ```nextflow
      ch_instrain_comparisons_tsv = INSTRAIN_COMPARE.out.comparisons_table
      ^^^^^^^^^^^^^^^^^^^^^^^^^^^
  ```

- Warning: `subworkflows/local/fasta_microdiversity_instrain/main.nf:48:5`: Variable was declared but not used

  ```nextflow
      ch_instrain_pooled_snvs_tsv = INSTRAIN_COMPARE.out.pooled_snv
      ^^^^^^^^^^^^^^^^^^^^^^^^^^^
  ```

- Warning: `subworkflows/local/fasta_phage_function_pharokka/main.nf:14:19`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_versions = Channel.empty()
                    ^^^^^^^
  ```

- Warning: `subworkflows/local/fasta_phage_host_iphop/main.nf:16:19`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_versions = Channel.empty()
                    ^^^^^^^
  ```

- Warning: `subworkflows/local/fasta_phage_host_iphop/main.nf:33:217`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
              ch_iphop_db = UNTAR ( [ [ id:'iphop_minimal_db' ], file("https://github.com/nf-core/test-datasets/raw/phageannotator/modules/nfcore/iphop/download/Test_db_rw.tar.gz", checkIfExists: true) ] ).untar.map { it[1] }
                                                                                                                                                                                                                          ^^
  ```

- Warning: `subworkflows/local/fasta_phage_host_iphop/main.nf:44:227`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          ch_iphop_partial_input = UNTAR2 ( [ [ id:'iphop_partial_input' ], file("https://github.com/nf-core/test-datasets/raw/phageannotator/modules/nfcore/iphop/predict/iPHoP_data.tar.gz", checkIfExists: true) ] ).untar.map { it[1] }
                                                                                                                                                                                                                                    ^^
  ```

- Warning: `subworkflows/local/fasta_virus_classification_genomad/main.nf:14:19`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_versions = Channel.empty()
                    ^^^^^^^
  ```

- Warning: `subworkflows/local/fasta_virus_quality_checkv/main.nf:15:19`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_versions = Channel.empty()
                    ^^^^^^^
  ```

- Warning: `subworkflows/local/fasta_virus_quality_checkv/main.nf:32:224`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
              ch_checkv_db = UNTAR ( [ [ id:'checkv_minimal_db' ], file("https://github.com/nf-core/test-datasets/raw/phageannotator/modules/nfcore/checkv/endtoend/checkv_minimal_db.tar", checkIfExists: true) ] ).untar.map { it[1] }
                                                                                                                                                                                                                                 ^^
  ```

- Warning: `subworkflows/local/fastq_fasta_reference_containment_mash/main.nf:18:19`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_versions = Channel.empty()
                    ^^^^^^^
  ```

- Warning: `subworkflows/local/fastq_fasta_reference_containment_mash/main.nf:49:69`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
      ch_mash_screen_tsv = MASH_SCREEN ( ch_mash_screen_input.map { [ it[0], it[1] ] }, ch_mash_screen_input.map { [ it[0], it[2] ] } ).screen
                                                                      ^^
  ```

- Warning: `subworkflows/local/fastq_fasta_reference_containment_mash/main.nf:49:76`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
      ch_mash_screen_tsv = MASH_SCREEN ( ch_mash_screen_input.map { [ it[0], it[1] ] }, ch_mash_screen_input.map { [ it[0], it[2] ] } ).screen
                                                                             ^^
  ```

- Warning: `subworkflows/local/fastq_fasta_reference_containment_mash/main.nf:49:116`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
      ch_mash_screen_tsv = MASH_SCREEN ( ch_mash_screen_input.map { [ it[0], it[1] ] }, ch_mash_screen_input.map { [ it[0], it[2] ] } ).screen
                                                                                                                     ^^
  ```

- Warning: `subworkflows/local/fastq_fasta_reference_containment_mash/main.nf:49:123`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
      ch_mash_screen_tsv = MASH_SCREEN ( ch_mash_screen_input.map { [ it[0], it[1] ] }, ch_mash_screen_input.map { [ it[0], it[2] ] } ).screen
                                                                                                                            ^^
  ```

- Warning: `subworkflows/local/fastq_virus_enrichment_viromeqc/main.nf:13:19`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_versions = Channel.empty()
                    ^^^^^^^
  ```

- Warning: `subworkflows/local/utils_nfcore_phageannotator_pipeline/main.nf:38:5`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
      input             //  string: Path to input samplesheet
      ^^^^^
  ```

- Warning: `subworkflows/local/utils_nfcore_phageannotator_pipeline/main.nf:42:19`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_versions = Channel.empty()
                    ^^^^^^^
  ```

- Warning: `subworkflows/local/utils_nfcore_phageannotator_pipeline/main.nf:83:5`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      Channel
      ^^^^^^^
  ```

- Warning: `subworkflows/local/utils_nfcore_phageannotator_pipeline/main.nf:95:38`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
              validateInputSamplesheet(it)
                                       ^^
  ```

- Warning: `subworkflows/local/utils_nfcore_phageannotator_pipeline/main.nf:164:39`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
      def endedness_ok = metas.collect{ it.single_end }.unique().size == 1
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

- Warning: `subworkflows/nf-core/fastq_align_bowtie2/main.nf:18:19`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_versions = Channel.empty()
                    ^^^^^^^
  ```

- Warning: `subworkflows/nf-core/initialise/main.nf:164:10`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
  def logo(workflow, monochrome_logs) {
           ^^^^^^^^
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
