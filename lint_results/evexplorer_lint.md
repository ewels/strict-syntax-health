# Nextflow lint results

- Generated: 2026-01-14T09:17:36.741743939Z
- Nextflow version: 25.12.0-edge
- Summary: 75 errors, 53 warnings

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

- Error: `main.nf:23:1`: Module could not be parsed: '/home/runner/work/strict-syntax-health/strict-syntax-health/pipelines/evexplorer/subworkflows/local/utils_nfcore_evexplorer_pipeline/main.nf'

  ```nextflow
  include { PIPELINE_INITIALISATION } from './subworkflows/local/utils_nfcore_evexplorer_pipeline'
  ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  ```

- Error: `main.nf:24:1`: Module could not be parsed: '/home/runner/work/strict-syntax-health/strict-syntax-health/pipelines/evexplorer/subworkflows/local/utils_nfcore_evexplorer_pipeline/main.nf'

  ```nextflow
  include { PIPELINE_COMPLETION     } from './subworkflows/local/utils_nfcore_evexplorer_pipeline'
  ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  ```

- Error: `main.nf:25:1`: Module could not be parsed: '/home/runner/work/strict-syntax-health/strict-syntax-health/pipelines/evexplorer/subworkflows/local/utils_nfcore_evexplorer_pipeline/main.nf'

  ```nextflow
  include { getGenomeAttribute      } from './subworkflows/local/utils_nfcore_evexplorer_pipeline'
  ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  ```

- Error: `main.nf:35:16`: `getGenomeAttribute` is not defined

  ```nextflow
  params.fasta = getGenomeAttribute('fasta')
                 ^^^^^^^^^^^^^^^^^^
  ```

- Error: `main.nf:41:1`: Statements cannot be mixed with script declarations -- move statements into a process or workflow

  ```nextflow
  ch_gtf_1     = Channel.fromPath(params.gtf_1)
  ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  ```

- Error: `main.nf:42:1`: Statements cannot be mixed with script declarations -- move statements into a process or workflow

  ```nextflow
  ch_gtf_2     = Channel.fromPath(params.gtf_2)
  ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  ```

- Error: `main.nf:43:1`: Statements cannot be mixed with script declarations -- move statements into a process or workflow

  ```nextflow
  ch_chr_names = Channel.fromPath(params.chr_names)
  ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  ```

- Error: `main.nf:44:1`: Statements cannot be mixed with script declarations -- move statements into a process or workflow

  ```nextflow
  ch_fasta     = Channel.fromPath(params.fasta, checkIfExists: true)
  ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  ```

- Error: `main.nf:71:9`: `ch_fasta` is not defined

  ```nextflow
          ch_fasta,
          ^^^^^^^^
  ```

- Error: `main.nf:72:9`: `ch_gtf_1` is not defined

  ```nextflow
          ch_gtf_1,
          ^^^^^^^^
  ```

- Error: `main.nf:73:9`: `ch_gtf_2` is not defined

  ```nextflow
          ch_gtf_2,
          ^^^^^^^^
  ```

- Error: `main.nf:74:9`: `ch_chr_names` is not defined

  ```nextflow
          ch_chr_names
          ^^^^^^^^^^^^
  ```

- Error: `main.nf:80:9`: `ch_fasta` is not defined

  ```nextflow
          ch_fasta,
          ^^^^^^^^
  ```

- Error: `main.nf:81:9`: `ch_gtf_1` is not defined

  ```nextflow
          ch_gtf_1,
          ^^^^^^^^
  ```

- Error: `main.nf:82:9`: `ch_gtf_2` is not defined

  ```nextflow
          ch_gtf_2,
          ^^^^^^^^
  ```

- Error: `main.nf:83:9`: `ch_chr_names` is not defined

  ```nextflow
          ch_chr_names
          ^^^^^^^^^^^^
  ```

- Error: `main.nf:107:5`: `PIPELINE_INITIALISATION` is not defined

  ```nextflow
      PIPELINE_INITIALISATION (
      ^^^^^^^^^^^^^^^^^^^^^^^
  ```

- Error: `main.nf:120:9`: `PIPELINE_INITIALISATION` is not defined

  ```nextflow
          PIPELINE_INITIALISATION.out.samplesheet,
          ^^^^^^^^^^^^^^^^^^^^^^^
  ```

- Error: `main.nf:123:6`: `PIPELINE_COMPLETION` is not defined

  ```nextflow
  	    PIPELINE_COMPLETION (
       ^^^^^^^^^^^^^^^^^^^
  ```

- Error: `modules/local/derfinder/main.nf:12:15`: `meta` is already declared

  ```nextflow
      tuple val(meta), path(path_bai)
                ^^^^
  ```

- Error: `modules/nf-core/multiqc/main.nf:28:31`: Unexpected input: '/'

  ```nextflow
      def logo = multiqc_logo ? /--cl-config 'custom_logo: "${multiqc_logo}"'/ : ''
                                ^
  ```

- Error: `nextflow.config:67:5`: Unexpected input: 'includeConfig'

  ```nextflow
      includeConfig "${params.custom_config_base}/nfcore_custom.config"
      ^
  ```

- Error: `subworkflows/local/utils_nfcore_evexplorer_pipeline/main.nf:248:21`: Unexpected input: 'doi_ref'

  ```nextflow
          for (String doi_ref: manifest_doi) temp_doi_ref += "(doi: <a href=\'https://doi.org/${doi_ref.replace("https://doi.org/", "").replace(" ", "")}\'>${doi_ref.replace("https://doi.org/", "").replace(" ", "")}</a>), "
                      ^
  ```

- Error: `subworkflows/nf-core/utils_nextflow_pipeline/main.nf:111:14`: Unexpected input: 'i'

  ```nextflow
      for (int i = 0; i < n - 1; i++) {
               ^
  ```

- Error: `subworkflows/nf-core/utils_nfcore_pipeline/main.nf:73:17`: Unexpected input: 'doi_ref'

  ```nextflow
      for (String doi_ref: manifest_doi) temp_doi_ref += "  https://doi.org/${doi_ref.replace('https://doi.org/', '').replace(' ', '')}\n"
                  ^
  ```

- Error: `workflows/evexplorer.nf:9:1`: Module could not be parsed: '/home/runner/work/strict-syntax-health/strict-syntax-health/pipelines/evexplorer/modules/nf-core/multiqc/main.nf'

  ```nextflow
  include { MULTIQC                   } from '../modules/nf-core/multiqc/main'
  ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  ```

- Error: `workflows/evexplorer.nf:19:1`: Module could not be parsed: '/home/runner/work/strict-syntax-health/strict-syntax-health/pipelines/evexplorer/subworkflows/nf-core/utils_nfcore_pipeline/main.nf'

  ```nextflow
  include { paramsSummaryMultiqc      } from '../subworkflows/nf-core/utils_nfcore_pipeline'
  ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  ```

- Error: `workflows/evexplorer.nf:20:1`: Module could not be parsed: '/home/runner/work/strict-syntax-health/strict-syntax-health/pipelines/evexplorer/subworkflows/nf-core/utils_nfcore_pipeline/main.nf'

  ```nextflow
  include { softwareVersionsToYAML    } from '../subworkflows/nf-core/utils_nfcore_pipeline'
  ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  ```

- Error: `workflows/evexplorer.nf:21:1`: Module could not be parsed: '/home/runner/work/strict-syntax-health/strict-syntax-health/pipelines/evexplorer/subworkflows/local/utils_nfcore_evexplorer_pipeline/main.nf'

  ```nextflow
  include { methodsDescriptionText    } from '../subworkflows/local/utils_nfcore_evexplorer_pipeline'
  ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  ```

- Error: `workflows/evexplorer.nf:138:18`: `_` is not allowed as an identifier because it is reserved for future use

  ```nextflow
      .map { meta, _ -> tuple(meta.id, meta.sample_batch) }
                   ^
  ```

- Error: `workflows/evexplorer.nf:150:18`: `_` is not allowed as an identifier because it is reserved for future use

  ```nextflow
      .map { meta, _ -> tuple(meta.id, meta.sample_batch, meta.sample_cond ) }
                   ^
  ```

- Error: `workflows/evexplorer.nf:163:5`: `softwareVersionsToYAML` is not defined

  ```nextflow
      softwareVersionsToYAML(ch_versions)
      ^^^^^^^^^^^^^^^^^^^^^^
  ```

- Error: `workflows/evexplorer.nf:186:41`: `paramsSummaryMultiqc` is not defined

  ```nextflow
      ch_workflow_summary = Channel.value(paramsSummaryMultiqc(summary_params))
                                          ^^^^^^^^^^^^^^^^^^^^
  ```

- Error: `workflows/evexplorer.nf:193:9`: `methodsDescriptionText` is not defined

  ```nextflow
          methodsDescriptionText(ch_multiqc_custom_methods_description))
          ^^^^^^^^^^^^^^^^^^^^^^
  ```

- Error: `workflows/evexplorer.nf:203:5`: `MULTIQC` is not defined

  ```nextflow
      MULTIQC (
      ^^^^^^^
  ```

- Error: `workflows/evexplorer.nf:212:27`: `MULTIQC` is not defined

  ```nextflow
      emit:multiqc_report = MULTIQC.out.report.toList() // channel: /path/to/multiqc_report.html
                            ^^^^^^^
  ```

- Error: `workflows/long_reads.nf:11:1`: Module could not be parsed: '/home/runner/work/strict-syntax-health/strict-syntax-health/pipelines/evexplorer/modules/nf-core/multiqc/main.nf'

  ```nextflow
  include { MULTIQC                   } from '../modules/nf-core/multiqc/main'
  ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  ```

- Error: `workflows/long_reads.nf:20:1`: Module could not be parsed: '/home/runner/work/strict-syntax-health/strict-syntax-health/pipelines/evexplorer/subworkflows/nf-core/utils_nfcore_pipeline/main.nf'

  ```nextflow
  include { paramsSummaryMultiqc      } from '../subworkflows/nf-core/utils_nfcore_pipeline'
  ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  ```

- Error: `workflows/long_reads.nf:21:1`: Module could not be parsed: '/home/runner/work/strict-syntax-health/strict-syntax-health/pipelines/evexplorer/subworkflows/nf-core/utils_nfcore_pipeline/main.nf'

  ```nextflow
  include { softwareVersionsToYAML    } from '../subworkflows/nf-core/utils_nfcore_pipeline'
  ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  ```

- Error: `workflows/long_reads.nf:22:1`: Module could not be parsed: '/home/runner/work/strict-syntax-health/strict-syntax-health/pipelines/evexplorer/subworkflows/local/utils_nfcore_evexplorer_pipeline/main.nf'

  ```nextflow
  include { methodsDescriptionText    } from '../subworkflows/local/utils_nfcore_evexplorer_pipeline'
  ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  ```

- Error: `workflows/long_reads.nf:116:18`: `_` is not allowed as an identifier because it is reserved for future use

  ```nextflow
      .map { meta, _ -> tuple(meta.id, meta.sample_batch) }
                   ^
  ```

- Error: `workflows/long_reads.nf:128:18`: `_` is not allowed as an identifier because it is reserved for future use

  ```nextflow
      .map { meta, _ -> tuple(meta.id, meta.sample_batch, meta.sample_cond ) }
                   ^
  ```

- Error: `workflows/long_reads.nf:142:5`: `softwareVersionsToYAML` is not defined

  ```nextflow
      softwareVersionsToYAML(ch_versions)
      ^^^^^^^^^^^^^^^^^^^^^^
  ```

- Error: `workflows/long_reads.nf:165:41`: `paramsSummaryMultiqc` is not defined

  ```nextflow
      ch_workflow_summary = Channel.value(paramsSummaryMultiqc(summary_params))
                                          ^^^^^^^^^^^^^^^^^^^^
  ```

- Error: `workflows/long_reads.nf:172:9`: `methodsDescriptionText` is not defined

  ```nextflow
          methodsDescriptionText(ch_multiqc_custom_methods_description))
          ^^^^^^^^^^^^^^^^^^^^^^
  ```

- Error: `workflows/long_reads.nf:182:5`: `MULTIQC` is not defined

  ```nextflow
      MULTIQC (
      ^^^^^^^
  ```

- Error: `workflows/long_reads.nf:191:27`: `MULTIQC` is not defined

  ```nextflow
      emit:multiqc_report = MULTIQC.out.report.toList() // channel: /path/to/multiqc_report.html
                            ^^^^^^^
  ```

- Error: `workflows/small_reads.nf:9:1`: Module could not be parsed: '/home/runner/work/strict-syntax-health/strict-syntax-health/pipelines/evexplorer/modules/nf-core/multiqc/main.nf'

  ```nextflow
  include { MULTIQC                   } from '../modules/nf-core/multiqc/main'
  ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  ```

- Error: `workflows/small_reads.nf:19:1`: Module could not be parsed: '/home/runner/work/strict-syntax-health/strict-syntax-health/pipelines/evexplorer/subworkflows/nf-core/utils_nfcore_pipeline/main.nf'

  ```nextflow
  include { paramsSummaryMultiqc      } from '../subworkflows/nf-core/utils_nfcore_pipeline'
  ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  ```

- Error: `workflows/small_reads.nf:20:1`: Module could not be parsed: '/home/runner/work/strict-syntax-health/strict-syntax-health/pipelines/evexplorer/subworkflows/nf-core/utils_nfcore_pipeline/main.nf'

  ```nextflow
  include { softwareVersionsToYAML    } from '../subworkflows/nf-core/utils_nfcore_pipeline'
  ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  ```

- Error: `workflows/small_reads.nf:21:1`: Module could not be parsed: '/home/runner/work/strict-syntax-health/strict-syntax-health/pipelines/evexplorer/subworkflows/local/utils_nfcore_evexplorer_pipeline/main.nf'

  ```nextflow
  include { methodsDescriptionText    } from '../subworkflows/local/utils_nfcore_evexplorer_pipeline'
  ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  ```

- Error: `workflows/small_reads.nf:138:18`: `_` is not allowed as an identifier because it is reserved for future use

  ```nextflow
      .map { meta, _ -> tuple(meta.id, meta.sample_batch) }
                   ^
  ```

- Error: `workflows/small_reads.nf:150:18`: `_` is not allowed as an identifier because it is reserved for future use

  ```nextflow
      .map { meta, _ -> tuple(meta.id, meta.sample_batch, meta.sample_cond ) }
                   ^
  ```

- Error: `workflows/small_reads.nf:163:5`: `softwareVersionsToYAML` is not defined

  ```nextflow
      softwareVersionsToYAML(ch_versions)
      ^^^^^^^^^^^^^^^^^^^^^^
  ```

- Error: `workflows/small_reads.nf:186:41`: `paramsSummaryMultiqc` is not defined

  ```nextflow
      ch_workflow_summary = Channel.value(paramsSummaryMultiqc(summary_params))
                                          ^^^^^^^^^^^^^^^^^^^^
  ```

- Error: `workflows/small_reads.nf:193:9`: `methodsDescriptionText` is not defined

  ```nextflow
          methodsDescriptionText(ch_multiqc_custom_methods_description))
          ^^^^^^^^^^^^^^^^^^^^^^
  ```

- Error: `workflows/small_reads.nf:203:5`: `MULTIQC` is not defined

  ```nextflow
      MULTIQC (
      ^^^^^^^
  ```

- Error: `workflows/small_reads.nf:212:27`: `MULTIQC` is not defined

  ```nextflow
      emit:multiqc_report = MULTIQC.out.report.toList() // channel: /path/to/multiqc_report.html
                            ^^^^^^^
  ```

## :warning: Warnings

- Warning: `main.nf:41:1`: Variable was declared but not used

  ```nextflow
  ch_gtf_1     = Channel.fromPath(params.gtf_1)
  ^^^^^^^^
  ```

- Warning: `main.nf:41:16`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
  ch_gtf_1     = Channel.fromPath(params.gtf_1)
                 ^^^^^^^
  ```

- Warning: `main.nf:42:1`: Variable was declared but not used

  ```nextflow
  ch_gtf_2     = Channel.fromPath(params.gtf_2)
  ^^^^^^^^
  ```

- Warning: `main.nf:42:16`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
  ch_gtf_2     = Channel.fromPath(params.gtf_2)
                 ^^^^^^^
  ```

- Warning: `main.nf:43:1`: Variable was declared but not used

  ```nextflow
  ch_chr_names = Channel.fromPath(params.chr_names)
  ^^^^^^^^^^^^
  ```

- Warning: `main.nf:43:16`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
  ch_chr_names = Channel.fromPath(params.chr_names)
                 ^^^^^^^
  ```

- Warning: `main.nf:44:1`: Variable was declared but not used

  ```nextflow
  ch_fasta     = Channel.fromPath(params.fasta, checkIfExists: true)
  ^^^^^^^^
  ```

- Warning: `main.nf:44:16`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
  ch_fasta     = Channel.fromPath(params.fasta, checkIfExists: true)
                 ^^^^^^^
  ```

- Warning: `modules/local/derfinder/main.nf:11:15`: Variable was declared but not used

  ```nextflow
      tuple val(meta), path(path_bam)
                ^^^^
  ```

- Warning: `modules/nf-core/fastqc/main.nf:27:48`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
      def renamed_files = old_new_pairs.collect{ old_name, new_name -> new_name }.join(' ')
                                                 ^^^^^^^^
  ```

- Warning: `modules/nf-core/gunzip/main.nf:43:9`: Variable was declared but not used

  ```nextflow
      def args = task.ext.args ?: ''
          ^^^^
  ```

- Warning: `modules/nf-core/minimap2/align/main.nf:67:9`: Variable was declared but not used

  ```nextflow
      def target = reference ?: (bam_input ? error("BAM input requires reference") : reads)
          ^^^^^^
  ```

- Warning: `modules/nf-core/pychopper/main.nf:41:9`: Variable was declared but not used

  ```nextflow
      def args = task.ext.args ?: ''
          ^^^^
  ```

- Warning: `modules/nf-core/star/align/main.nf:46:56`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
      meta.single_end ? [reads].flatten().each{reads1 << it} : reads.eachWithIndex{ v, ix -> ( ix & 1 ? reads2 : reads1) << v }
                                                         ^^
  ```

- Warning: `workflows/evexplorer.nf:40:19`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_versions = Channel.empty()
                    ^^^^^^^
  ```

- Warning: `workflows/evexplorer.nf:41:24`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_multiqc_files = Channel.empty()
                         ^^^^^^^
  ```

- Warning: `workflows/evexplorer.nf:63:77`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
      ch_multiqc_files = ch_multiqc_files.mix(FASTQC_PRE_TRIM.out.zip.collect{it[1]})
                                                                              ^^
  ```

- Warning: `workflows/evexplorer.nf:81:78`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
      ch_multiqc_files = ch_multiqc_files.mix(FASTQC_POST_TRIM.out.zip.collect{it[1]})
                                                                               ^^
  ```

- Warning: `workflows/evexplorer.nf:118:12`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
      .map { meta, bam -> tuple([id: 'sample1', single_end: true], bam) }
             ^^^^
  ```

- Warning: `workflows/evexplorer.nf:122:12`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
      .map { meta, index -> tuple([id: 'sample1', single_end: true], index) }
             ^^^^
  ```

- Warning: `workflows/evexplorer.nf:175:32`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_multiqc_config        = Channel.fromPath(
                                 ^^^^^^^
  ```

- Warning: `workflows/evexplorer.nf:178:9`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
          Channel.fromPath(params.multiqc_config, checkIfExists: true) :
          ^^^^^^^
  ```

- Warning: `workflows/evexplorer.nf:179:9`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
          Channel.empty()
          ^^^^^^^
  ```

- Warning: `workflows/evexplorer.nf:181:9`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
          Channel.fromPath(params.multiqc_logo, checkIfExists: true) :
          ^^^^^^^
  ```

- Warning: `workflows/evexplorer.nf:182:9`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
          Channel.empty()
          ^^^^^^^
  ```

- Warning: `workflows/evexplorer.nf:186:27`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_workflow_summary = Channel.value(paramsSummaryMultiqc(summary_params))
                            ^^^^^^^
  ```

- Warning: `workflows/evexplorer.nf:192:45`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_methods_description                = Channel.value(
                                              ^^^^^^^
  ```

- Warning: `workflows/long_reads.nf:41:19`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_versions = Channel.empty()
                    ^^^^^^^
  ```

- Warning: `workflows/long_reads.nf:42:24`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_multiqc_files = Channel.empty()
                         ^^^^^^^
  ```

- Warning: `workflows/long_reads.nf:61:77`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
      ch_multiqc_files = ch_multiqc_files.mix(FASTQC_PRE_TRIM.out.zip.collect{it[1]})
                                                                              ^^
  ```

- Warning: `workflows/long_reads.nf:79:78`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
      ch_multiqc_files = ch_multiqc_files.mix(FASTQC_POST_TRIM.out.zip.collect{it[1]})
                                                                               ^^
  ```

- Warning: `workflows/long_reads.nf:98:12`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
      .map { meta, bam -> tuple([id: 'sample1', single_end: true], bam) }
             ^^^^
  ```

- Warning: `workflows/long_reads.nf:102:12`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
      .map { meta, index -> tuple([id: 'sample1', single_end: true], index) }
             ^^^^
  ```

- Warning: `workflows/long_reads.nf:154:32`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_multiqc_config        = Channel.fromPath(
                                 ^^^^^^^
  ```

- Warning: `workflows/long_reads.nf:157:9`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
          Channel.fromPath(params.multiqc_config, checkIfExists: true) :
          ^^^^^^^
  ```

- Warning: `workflows/long_reads.nf:158:9`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
          Channel.empty()
          ^^^^^^^
  ```

- Warning: `workflows/long_reads.nf:160:9`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
          Channel.fromPath(params.multiqc_logo, checkIfExists: true) :
          ^^^^^^^
  ```

- Warning: `workflows/long_reads.nf:161:9`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
          Channel.empty()
          ^^^^^^^
  ```

- Warning: `workflows/long_reads.nf:165:27`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_workflow_summary = Channel.value(paramsSummaryMultiqc(summary_params))
                            ^^^^^^^
  ```

- Warning: `workflows/long_reads.nf:171:45`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_methods_description                = Channel.value(
                                              ^^^^^^^
  ```

- Warning: `workflows/small_reads.nf:40:19`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_versions = Channel.empty()
                    ^^^^^^^
  ```

- Warning: `workflows/small_reads.nf:41:24`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_multiqc_files = Channel.empty()
                         ^^^^^^^
  ```

- Warning: `workflows/small_reads.nf:63:77`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
      ch_multiqc_files = ch_multiqc_files.mix(FASTQC_PRE_TRIM.out.zip.collect{it[1]})
                                                                              ^^
  ```

- Warning: `workflows/small_reads.nf:81:78`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
      ch_multiqc_files = ch_multiqc_files.mix(FASTQC_POST_TRIM.out.zip.collect{it[1]})
                                                                               ^^
  ```

- Warning: `workflows/small_reads.nf:118:12`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
      .map { meta, bam -> tuple([id: 'sample1', single_end: true], bam) }
             ^^^^
  ```

- Warning: `workflows/small_reads.nf:122:12`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
      .map { meta, index -> tuple([id: 'sample1', single_end: true], index) }
             ^^^^
  ```

- Warning: `workflows/small_reads.nf:175:32`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_multiqc_config        = Channel.fromPath(
                                 ^^^^^^^
  ```

- Warning: `workflows/small_reads.nf:178:9`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
          Channel.fromPath(params.multiqc_config, checkIfExists: true) :
          ^^^^^^^
  ```

- Warning: `workflows/small_reads.nf:179:9`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
          Channel.empty()
          ^^^^^^^
  ```

- Warning: `workflows/small_reads.nf:181:9`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
          Channel.fromPath(params.multiqc_logo, checkIfExists: true) :
          ^^^^^^^
  ```

- Warning: `workflows/small_reads.nf:182:9`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
          Channel.empty()
          ^^^^^^^
  ```

- Warning: `workflows/small_reads.nf:186:27`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_workflow_summary = Channel.value(paramsSummaryMultiqc(summary_params))
                            ^^^^^^^
  ```

- Warning: `workflows/small_reads.nf:192:45`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_methods_description                = Channel.value(
                                              ^^^^^^^
  ```
