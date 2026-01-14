# Nextflow lint results

- Generated: 2026-01-14T09:26:57.841527305Z
- Nextflow version: 25.12.0-edge
- Summary: 14 errors, 47 warnings

## :x: Errors

- Error: `modules/local/mtbseq/tbamend/main.nf:15:13`: `USER` is not defined

  ```nextflow
          env(USER)
              ^^^^
  ```

- Error: `modules/local/mtbseq/tbbwa/main.nf:16:13`: `USER` is not defined

  ```nextflow
          env(USER)
              ^^^^
  ```

- Error: `modules/local/mtbseq/tbfull/main.nf:18:13`: `USER` is not defined

  ```nextflow
          env(USER)
              ^^^^
  ```

- Error: `modules/local/mtbseq/tbgroups/main.nf:15:13`: `USER` is not defined

  ```nextflow
          env(USER)
              ^^^^
  ```

- Error: `modules/local/mtbseq/tbjoin/main.nf:18:13`: `USER` is not defined

  ```nextflow
          env(USER)
              ^^^^
  ```

- Error: `modules/local/mtbseq/tblist/main.nf:14:13`: `USER` is not defined

  ```nextflow
          env(USER)
              ^^^^
  ```

- Error: `modules/local/mtbseq/tbpile/main.nf:16:13`: `USER` is not defined

  ```nextflow
          env(USER)
              ^^^^
  ```

- Error: `modules/local/mtbseq/tbrefine/main.nf:14:13`: `USER` is not defined

  ```nextflow
          env(USER)
              ^^^^
  ```

- Error: `modules/local/mtbseq/tbstats/main.nf:16:13`: `USER` is not defined

  ```nextflow
          env(USER)
              ^^^^
  ```

- Error: `modules/local/mtbseq/tbstrains/main.nf:14:13`: `USER` is not defined

  ```nextflow
          env(USER)
              ^^^^
  ```

- Error: `modules/local/mtbseq/tbvariants/main.nf:14:13`: `USER` is not defined

  ```nextflow
          env(USER)
              ^^^^
  ```

- Error: `modules/nf-core/bcftools/view/main.nf:60:9`: `index` is already declared

  ```nextflow
      def index = args.contains("--write-index=tbi") || args.contains("-W=tbi") ? "tbi" :
          ^^^^^
  ```

- Error: `modules/nf-core/snpsites/main.nf:16:11`: `CONSTANT_SITES` is not defined

  ```nextflow
      env   CONSTANT_SITES, emit: constant_sites_string
            ^^^^^^^^^^^^^^
  ```

- Error: `nextflow.config:62:5`: Unexpected input: 'includeConfig'

  ```nextflow
      includeConfig 'conf/mtbseq_base.config'
      ^
  ```

## :warning: Warnings

- Warning: `modules/magma/modules/local/gatk4.nf:77:9`: Variable was declared but not used

  ```nextflow
      def args = task.ext.args ?: ''
          ^^^^
  ```

- Warning: `modules/nf-core/bcftools/merge/main.nf:28:58`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
      def input = (vcfs.collect().size() > 1) ? vcfs.sort{ it.name } : vcfs
                                                           ^^
  ```

- Warning: `modules/nf-core/bwamem2/mem/main.nf:59:9`: Variable was declared but not used

  ```nextflow
      def args = task.ext.args ?: ''
          ^^^^
  ```

- Warning: `modules/nf-core/bwamem2/mem/main.nf:62:9`: Variable was declared but not used

  ```nextflow
      def samtools_command = sort_bam ? 'sort' : 'view'
          ^^^^^^^^^^^^^^^^
  ```

- Warning: `modules/nf-core/bwamem2/mem/main.nf:66:9`: Variable was declared but not used

  ```nextflow
      def reference = fasta && extension=="cram"  ? "--reference ${fasta}" : ""
          ^^^^^^^^^
  ```

- Warning: `modules/nf-core/fastqc/main.nf:27:48`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
      def renamed_files = old_new_pairs.collect{ old_name, new_name -> new_name }.join(' ')
                                                 ^^^^^^^^
  ```

- Warning: `modules/nf-core/gatk4/markduplicates/main.nf:33:43`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
      def input_list = bam.collect{"--INPUT $it"}.join(' ')
                                            ^^
  ```

- Warning: `modules/nf-core/gatk4/variantstotable/main.nf:27:9`: Variable was declared but not used

  ```nextflow
      def include_intervals_arg = include_intervals ? "-L ${include_intervals}" : ""
          ^^^^^^^^^^^^^^^^^^^^^
  ```

- Warning: `modules/nf-core/gatk4/variantstotable/main.nf:28:9`: Variable was declared but not used

  ```nextflow
      def exclude_intervals_arg = exclude_intervals ? "-XL ${exclude_intervals}" : ""
          ^^^^^^^^^^^^^^^^^^^^^
  ```

- Warning: `modules/nf-core/iqtree/main.nf:68:9`: Variable was declared but not used

  ```nextflow
      def trees_rf_arg                = trees_rf                ? "-rf $trees_rf"                 : ''
          ^^^^^^^^^^^^
  ```

- Warning: `modules/nf-core/ismapper/main.nf:22:9`: Variable was declared but not used

  ```nextflow
      def prefix = task.ext.prefix ?: "${meta.id}"
          ^^^^^^
  ```

- Warning: `modules/nf-core/lofreq/indelqual/main.nf:38:9`: Variable was declared but not used

  ```nextflow
      def args = task.ext.args ?: ''
          ^^^^
  ```

- Warning: `modules/nf-core/samtools/stats/main.nf:22:9`: Variable was declared but not used

  ```nextflow
      def args = task.ext.args ?: ''
          ^^^^
  ```

- Warning: `subworkflows/local/mtbseq/parallel_mode.nf:22:23`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
          ch_versions = Channel.empty()
                        ^^^^^^^
  ```

- Warning: `subworkflows/local/mtbseq/parallel_mode.nf:23:28`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
          ch_multiqc_files = Channel.empty()
                             ^^^^^^^
  ```

- Warning: `subworkflows/local/mtbseq/quality_check.nf:12:28`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
          samples_tsv_file = Channel.empty()
                             ^^^^^^^
  ```

- Warning: `subworkflows/local/mtbseq/quality_check.nf:27:32`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
              samples_tsv_file = Channel.fromPath( params.mtbseq_cohort_tsv )
                                 ^^^^^^^
  ```

- Warning: `subworkflows/local/mtbseq/quality_check.nf:34:53`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
      multiqc_files          = FASTQC.out.zip.collect{it[1]}
                                                      ^^
  ```

- Warning: `subworkflows/local/utils_nfcore_tbanalyzer_pipeline/main.nf:31:5`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
      monochrome_logs   // boolean: Do not use coloured log outputs
      ^^^^^^^^^^^^^^^
  ```

- Warning: `subworkflows/local/utils_nfcore_tbanalyzer_pipeline/main.nf:34:5`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
      input             //  string: Path to input samplesheet
      ^^^^^
  ```

- Warning: `subworkflows/local/utils_nfcore_tbanalyzer_pipeline/main.nf:38:19`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_versions = Channel.empty()
                    ^^^^^^^
  ```

- Warning: `subworkflows/local/utils_nfcore_tbanalyzer_pipeline/main.nf:75:5`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      Channel
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

- Warning: `workflows/mtbseqnf.nf:37:19`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_versions = Channel.empty()
                    ^^^^^^^
  ```

- Warning: `workflows/mtbseqnf.nf:38:24`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_multiqc_files = Channel.empty()
                         ^^^^^^^
  ```

- Warning: `workflows/mtbseqnf.nf:40:26`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_reference_files = Channel.value([params.mtbseq_resilist,
                           ^^^^^^^
  ```

- Warning: `workflows/mtbseqnf.nf:123:32`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_multiqc_config        = Channel.fromPath(
                                 ^^^^^^^
  ```

- Warning: `workflows/mtbseqnf.nf:126:9`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
          Channel.fromPath(params.multiqc_config, checkIfExists: true) :
          ^^^^^^^
  ```

- Warning: `workflows/mtbseqnf.nf:127:9`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
          Channel.empty()
          ^^^^^^^
  ```

- Warning: `workflows/mtbseqnf.nf:129:9`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
          Channel.fromPath(params.multiqc_logo, checkIfExists: true) :
          ^^^^^^^
  ```

- Warning: `workflows/mtbseqnf.nf:130:9`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
          Channel.empty()
          ^^^^^^^
  ```

- Warning: `workflows/mtbseqnf.nf:134:27`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_workflow_summary = Channel.value(paramsSummaryMultiqc(summary_params))
                            ^^^^^^^
  ```

- Warning: `workflows/mtbseqnf.nf:140:45`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_methods_description                = Channel.value(
                                              ^^^^^^^
  ```

- Warning: `workflows/tbanalyzer.nf:25:19`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_versions = Channel.empty()
                    ^^^^^^^
  ```

- Warning: `workflows/tbanalyzer.nf:26:24`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_multiqc_files = Channel.empty()
                         ^^^^^^^
  ```

- Warning: `workflows/tbanalyzer.nf:33:68`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
      ch_multiqc_files = ch_multiqc_files.mix(FASTQC.out.zip.collect{it[1]})
                                                                     ^^
  ```

- Warning: `workflows/tbanalyzer.nf:51:32`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_multiqc_config        = Channel.fromPath(
                                 ^^^^^^^
  ```

- Warning: `workflows/tbanalyzer.nf:54:9`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
          Channel.fromPath(params.multiqc_config, checkIfExists: true) :
          ^^^^^^^
  ```

- Warning: `workflows/tbanalyzer.nf:55:9`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
          Channel.empty()
          ^^^^^^^
  ```

- Warning: `workflows/tbanalyzer.nf:57:9`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
          Channel.fromPath(params.multiqc_logo, checkIfExists: true) :
          ^^^^^^^
  ```

- Warning: `workflows/tbanalyzer.nf:58:9`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
          Channel.empty()
          ^^^^^^^
  ```

- Warning: `workflows/tbanalyzer.nf:62:27`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_workflow_summary = Channel.value(paramsSummaryMultiqc(summary_params))
                            ^^^^^^^
  ```

- Warning: `workflows/tbanalyzer.nf:68:45`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_methods_description                = Channel.value(
                                              ^^^^^^^
  ```
