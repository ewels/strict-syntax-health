# Nextflow lint results

- Generated: 2026-01-16T06:33:12.603876715Z
- Nextflow version: 25.12.0-edge
- Summary: 17 errors, 16 warnings

## :x: Errors

- Error: `main.nf:19:1`: Module could not be parsed: '/home/runner/work/strict-syntax-health/strict-syntax-health/pipelines/hlatyping/subworkflows/local/utils_nfcore_hlatyping_pipeline/main.nf'

  ```nextflow
  include { PIPELINE_INITIALISATION } from './subworkflows/local/utils_nfcore_hlatyping_pipeline'
  ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  ```

- Error: `main.nf:20:1`: Module could not be parsed: '/home/runner/work/strict-syntax-health/strict-syntax-health/pipelines/hlatyping/subworkflows/local/utils_nfcore_hlatyping_pipeline/main.nf'

  ```nextflow
  include { PIPELINE_COMPLETION     } from './subworkflows/local/utils_nfcore_hlatyping_pipeline'
  ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  ```

- Error: `main.nf:21:1`: Module could not be parsed: '/home/runner/work/strict-syntax-health/strict-syntax-health/pipelines/hlatyping/subworkflows/local/utils_nfcore_hlatyping_pipeline/main.nf'

  ```nextflow
  include { getGenomeAttribute      } from './subworkflows/local/utils_nfcore_hlatyping_pipeline'
  ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  ```

- Error: `main.nf:66:5`: `PIPELINE_INITIALISATION` is not defined

  ```nextflow
      PIPELINE_INITIALISATION (
      ^^^^^^^^^^^^^^^^^^^^^^^
  ```

- Error: `main.nf:82:9`: `PIPELINE_INITIALISATION` is not defined

  ```nextflow
          PIPELINE_INITIALISATION.out.samplesheet
          ^^^^^^^^^^^^^^^^^^^^^^^
  ```

- Error: `main.nf:87:5`: `PIPELINE_COMPLETION` is not defined

  ```nextflow
      PIPELINE_COMPLETION (
      ^^^^^^^^^^^^^^^^^^^
  ```

- Error: `subworkflows/local/utils_nfcore_hlatyping_pipeline/main.nf:210:13`: Unexpected input: '+'

  ```nextflow
              + "sample must have the same sequence type: ${metas[0].id}"
              ^
  ```

- Error: `workflows/hlatyping.nf:23:1`: Module could not be parsed: '/home/runner/work/strict-syntax-health/strict-syntax-health/pipelines/hlatyping/subworkflows/local/utils_nfcore_hlatyping_pipeline/main.nf'

  ```nextflow
  include { methodsDescriptionText      } from '../subworkflows/local/utils_nfcore_hlatyping_pipeline'
  ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  ```

- Error: `workflows/hlatyping.nf:260:9`: `methodsDescriptionText` is not defined

  ```nextflow
          methodsDescriptionText(ch_multiqc_custom_methods_description))
          ^^^^^^^^^^^^^^^^^^^^^^
  ```

- Error: `workflows/hlatyping.nf:291:5`: `valid_tools` was assigned but not declared

  ```nextflow
      valid_tools = [ 'optitype', 'hlahd' ]
      ^^^^^^^^^^^
  ```

- Error: `workflows/hlatyping.nf:292:5`: `tool_list` was assigned but not declared

  ```nextflow
      tool_list = tools.tokenize(',')
      ^^^^^^^^^
  ```

- Error: `workflows/hlatyping.nf:294:25`: `tool_list` is not defined

  ```nextflow
      def invalid_tools = tool_list.findAll { it.trim() !in valid_tools }
                          ^^^^^^^^^
  ```

- Error: `workflows/hlatyping.nf:294:59`: `valid_tools` is not defined

  ```nextflow
      def invalid_tools = tool_list.findAll { it.trim() !in valid_tools }
                                                            ^^^^^^^^^^^
  ```

- Error: `workflows/hlatyping.nf:296:110`: `valid_tools` is not defined

  ```nextflow
          throw new IllegalArgumentException("Invalid tools found: ${invalid_tools.join(',')}.\nValid tools: ${valid_tools.join(',')}")
                                                                                                               ^^^^^^^^^^^
  ```

- Error: `workflows/hlatyping.nf:308:5`: `ch_hlahd_exe` was assigned but not declared

  ```nextflow
      ch_hlahd_exe = Channel.empty()
      ^^^^^^^^^^^^
  ```

- Error: `workflows/hlatyping.nf:309:5`: `ch_hlahd_exe` is not defined

  ```nextflow
      ch_hlahd_exe.bind([
      ^^^^^^^^^^^^
  ```

- Error: `workflows/hlatyping.nf:316:12`: `ch_hlahd_exe` is not defined

  ```nextflow
      return ch_hlahd_exe
             ^^^^^^^^^^^^
  ```

## :warning: Warnings

- Warning: `modules/nf-core/cat/fastq/main.nf:22:60`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
      def readList = reads instanceof List ? reads.collect { it.toString() } : [reads.toString()]
                                                             ^^
  ```

- Warning: `modules/nf-core/cat/fastq/main.nf:58:60`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
      def readList = reads instanceof List ? reads.collect { it.toString() } : [reads.toString()]
                                                             ^^
  ```

- Warning: `modules/nf-core/gunzip/main.nf:43:9`: Variable was declared but not used

  ```nextflow
      def args = task.ext.args ?: ''
          ^^^^
  ```

- Warning: `modules/nf-core/yara/index/main.nf:21:9`: Variable was declared but not used

  ```nextflow
      def args   = task.ext.args   ?: ''
          ^^^^
  ```

- Warning: `modules/nf-core/yara/index/main.nf:35:9`: Variable was declared but not used

  ```nextflow
      def args   = task.ext.args   ?: ''
          ^^^^
  ```

- Warning: `modules/nf-core/yara/mapper/main.nf:68:9`: Variable was declared but not used

  ```nextflow
      def args = task.ext.args ?: ''
          ^^^^
  ```

- Warning: `modules/nf-core/yara/mapper/main.nf:70:9`: Variable was declared but not used

  ```nextflow
      def index_prefix = index[0].baseName.substring(0,index[0].baseName.lastIndexOf('.'))
          ^^^^^^^^^^^^
  ```

- Warning: `workflows/hlatyping.nf:65:19`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_versions = Channel.empty()
                    ^^^^^^^
  ```

- Warning: `workflows/hlatyping.nf:66:24`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_multiqc_files = Channel.empty()
                         ^^^^^^^
  ```

- Warning: `workflows/hlatyping.nf:126:68`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
      ch_multiqc_files = ch_multiqc_files.mix(FASTQC.out.zip.collect{it[1]})
                                                                     ^^
  ```

- Warning: `workflows/hlatyping.nf:136:26`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
              .map { meta, reads ->
                           ^^^^^
  ```

- Warning: `workflows/hlatyping.nf:184:79`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          ch_multiqc_files = ch_multiqc_files.mix(OPTITYPE.out.hla_type.collect{it[1]})
                                                                                ^^
  ```

- Warning: `workflows/hlatyping.nf:185:84`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          ch_multiqc_files = ch_multiqc_files.mix(OPTITYPE.out.coverage_plot.collect{it[1]})
                                                                                     ^^
  ```

- Warning: `workflows/hlatyping.nf:212:26`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      def topic_versions = Channel.topic("versions")
                           ^^^^^^^
  ```

- Warning: `workflows/hlatyping.nf:294:45`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
      def invalid_tools = tool_list.findAll { it.trim() !in valid_tools }
                                              ^^
  ```

- Warning: `workflows/hlatyping.nf:308:20`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_hlahd_exe = Channel.empty()
                     ^^^^^^^
  ```
