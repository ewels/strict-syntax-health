# Nextflow lint results

- Generated: 2026-01-16T06:42:18.180681922Z
- Nextflow version: 25.12.0-edge
- Summary: 55 errors, 48 warnings

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

- Error: `main.nf:21:16`: `WorkflowMain` is not defined

  ```nextflow
  params.fasta = WorkflowMain.getGenomeAttribute(params, 'fasta')
                 ^^^^^^^^^^^^
  ```

- Error: `main.nf:29:1`: Statements cannot be mixed with script declarations -- move statements into a process, workflow, or function

  ```nextflow
  WorkflowMain.initialise(workflow, params, log)
  ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  ```

- Error: `main.nf:29:1`: `WorkflowMain` is not defined

  ```nextflow
  WorkflowMain.initialise(workflow, params, log)
  ^^^^^^^^^^^^
  ```

- Error: `modules/local/MT_Step2_participant_data.nf:6:12`: `meta` is already declared

  ```nextflow
  	tuple val(meta), path(Sample_list)
             ^^^^
  ```

- Error: `modules/local/MT_Step3_metadata_sample.nf:11:12`: `meta` is already declared

  ```nextflow
  	tuple val(meta), path(haplocheck)
             ^^^^
  ```

- Error: `modules/local/deepvariant/main.nf:8:5`: Invalid process directive

  ```nextflow
      if (workflow.profile.tokenize(',').intersect(['conda', 'mamba']).size() >= 1) {
      ^
  ```

- Error: `modules/nf-core/bwa/index/main.nf:14:27`: `bwa` is not defined

  ```nextflow
      tuple val(meta), path(bwa) , emit: index
                            ^^^
  ```

- Error: `modules/nf-core/deepvariant/main.nf:8:5`: Invalid process directive

  ```nextflow
      if (workflow.profile.tokenize(',').intersect(['conda', 'mamba']).size() >= 1) {
      ^
  ```

- Error: `modules/nf-core/picard/collectwgsmetrics/main.nf:13:15`: `meta2` is already declared

  ```nextflow
      tuple val(meta2), path(fai)
                ^^^^^
  ```

- Error: `nextflow.config:65:5`: Unexpected input: 'includeConfig'

  ```nextflow
      includeConfig "${params.custom_config_base}/nfcore_custom.config"
      ^
  ```

- Error: `workflows/variantcatalogue.nf:7:1`: Statements cannot be mixed with script declarations -- move statements into a process, workflow, or function

  ```nextflow
  def summary_params = NfcoreSchema.paramsSummaryMap(workflow, params)
  ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  ```

- Error: `workflows/variantcatalogue.nf:7:22`: `NfcoreSchema` is not defined

  ```nextflow
  def summary_params = NfcoreSchema.paramsSummaryMap(workflow, params)
                       ^^^^^^^^^^^^
  ```

- Error: `workflows/variantcatalogue.nf:10:1`: Statements cannot be mixed with script declarations -- move statements into a process, workflow, or function

  ```nextflow
  WorkflowVariantcatalogue.initialise(params, log)
  ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  ```

- Error: `workflows/variantcatalogue.nf:10:1`: `WorkflowVariantcatalogue` is not defined

  ```nextflow
  WorkflowVariantcatalogue.initialise(params, log)
  ^^^^^^^^^^^^^^^^^^^^^^^^
  ```

- Error: `workflows/variantcatalogue.nf:13:1`: Statements cannot be mixed with script declarations -- move statements into a process, workflow, or function

  ```nextflow
  def checkPathParamList = [ params.input, params.multiqc_config, params.fasta ]
  ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  ```

- Error: `workflows/variantcatalogue.nf:14:1`: `for` loops are no longer supported

  ```nextflow
  for (param in checkPathParamList) { if (param) { file(param, checkIfExists: true) } }
  ^^^
  ```

- Error: `workflows/variantcatalogue.nf:14:1`: Statements cannot be mixed with script declarations -- move statements into a process, workflow, or function

  ```nextflow
  for (param in checkPathParamList) { if (param) { file(param, checkIfExists: true) } }
  ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  ```

- Error: `workflows/variantcatalogue.nf:14:6`: `param` is not defined

  ```nextflow
  for (param in checkPathParamList) { if (param) { file(param, checkIfExists: true) } }
       ^^^^^
  ```

- Error: `workflows/variantcatalogue.nf:14:40`: `param` is not defined

  ```nextflow
  for (param in checkPathParamList) { if (param) { file(param, checkIfExists: true) } }
                                         ^^^^^^^
  ```

- Error: `workflows/variantcatalogue.nf:14:55`: `param` is not defined

  ```nextflow
  for (param in checkPathParamList) { if (param) { file(param, checkIfExists: true) } }
                                                        ^^^^^
  ```

- Error: `workflows/variantcatalogue.nf:17:1`: Statements cannot be mixed with script declarations -- move statements into a process, workflow, or function

  ```nextflow
  if (params.input) { ch_input = file(params.input) } else { exit 1, 'Input samplesheet not specified!' }
  ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  ```

- Error: `workflows/variantcatalogue.nf:25:1`: Statements cannot be mixed with script declarations -- move statements into a process, workflow, or function

  ```nextflow
  ch_multiqc_config          = Channel.fromPath("$projectDir/assets/multiqc_config.yml", checkIfExists: true)
  ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  ```

- Error: `workflows/variantcatalogue.nf:26:1`: Statements cannot be mixed with script declarations -- move statements into a process, workflow, or function

  ```nextflow
  ch_multiqc_custom_config   = params.multiqc_config ? Channel.fromPath( params.multiqc_config, checkIfExists: true ) : Channel.empty()
  ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  ```

- Error: `workflows/variantcatalogue.nf:27:1`: Statements cannot be mixed with script declarations -- move statements into a process, workflow, or function

  ```nextflow
  ch_multiqc_logo            = params.multiqc_logo   ? Channel.fromPath( params.multiqc_logo, checkIfExists: true ) : Channel.empty()
  ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  ```

- Error: `workflows/variantcatalogue.nf:28:1`: Statements cannot be mixed with script declarations -- move statements into a process, workflow, or function

  ```nextflow
  ch_multiqc_custom_methods_description = params.multiqc_methods_description ? file(params.multiqc_methods_description, checkIfExists: true) : file("$projectDir/assets/methods_description_template.yml", checkIfExists: true)
  ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  ```

- Error: `workflows/variantcatalogue.nf:135:1`: Statements cannot be mixed with script declarations -- move statements into a process, workflow, or function

  ```nextflow
  def multiqc_report = []
  ^^^^^^^^^^^^^^^^^^^^^^^
  ```

- Error: `workflows/variantcatalogue.nf:145:9`: `ch_input` is not defined

  ```nextflow
          ch_input
          ^^^^^^^^
  ```

- Error: `workflows/variantcatalogue.nf:359:27`: `WorkflowVariantcatalogue` is not defined

  ```nextflow
      workflow_summary    = WorkflowVariantcatalogue.paramsSummaryMultiqc(workflow, summary_params)
                            ^^^^^^^^^^^^^^^^^^^^^^^^
  ```

- Error: `workflows/variantcatalogue.nf:359:83`: `summary_params` is not defined

  ```nextflow
      workflow_summary    = WorkflowVariantcatalogue.paramsSummaryMultiqc(workflow, summary_params)
                                                                                    ^^^^^^^^^^^^^^
  ```

- Error: `workflows/variantcatalogue.nf:362:30`: `WorkflowVariantcatalogue` is not defined

  ```nextflow
      methods_description    = WorkflowVariantcatalogue.methodsDescriptionText(workflow, ch_multiqc_custom_methods_description)
                               ^^^^^^^^^^^^^^^^^^^^^^^^
  ```

- Error: `workflows/variantcatalogue.nf:362:88`: `ch_multiqc_custom_methods_description` is not defined

  ```nextflow
      methods_description    = WorkflowVariantcatalogue.methodsDescriptionText(workflow, ch_multiqc_custom_methods_description)
                                                                                         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  ```

- Error: `workflows/variantcatalogue.nf:378:9`: `ch_multiqc_config` is not defined

  ```nextflow
          ch_multiqc_config.toList(),
          ^^^^^^^^^^^^^^^^^
  ```

- Error: `workflows/variantcatalogue.nf:379:9`: `ch_multiqc_custom_config` is not defined

  ```nextflow
          ch_multiqc_custom_config.toList(),
          ^^^^^^^^^^^^^^^^^^^^^^^^
  ```

- Error: `workflows/variantcatalogue.nf:380:9`: `ch_multiqc_logo` is not defined

  ```nextflow
          ch_multiqc_logo.toList()
          ^^^^^^^^^^^^^^^
  ```

- Error: `workflows/variantcatalogue.nf:391:1`: Statements cannot be mixed with script declarations -- move statements into a process, workflow, or function

  ```nextflow
  workflow.onComplete {
  ^
  ```

- Error: `workflows/variantcatalogue.nf:393:9`: `NfcoreTemplate` is not defined

  ```nextflow
          NfcoreTemplate.email(workflow, params, summary_params, projectDir, log, multiqc_report)
          ^^^^^^^^^^^^^^
  ```

- Error: `workflows/variantcatalogue.nf:395:5`: `NfcoreTemplate` is not defined

  ```nextflow
      NfcoreTemplate.summary(workflow, params, log)
      ^^^^^^^^^^^^^^
  ```

- Error: `workflows/variantcatalogue.nf:397:9`: `NfcoreTemplate` is not defined

  ```nextflow
          NfcoreTemplate.IM_notification(workflow, params, summary_params, projectDir, log)
          ^^^^^^^^^^^^^^
  ```

## :warning: Warnings

- Warning: `modules/local/Hail_sample_QC.nf:21:14`: The use of `projectDir` in a process is discouraged -- input files should be provided as process inputs

  ```nextflow
      python ${projectDir}/modules/local/Hail_sample_QC.py $SNV_vcf $params.tmp_dir $params.genome
               ^^^^^^^^^^
  ```

- Warning: `modules/local/Hail_variant_MT_QC.nf:32:11`: The use of `projectDir` in a process is discouraged -- input files should be provided as process inputs

  ```nextflow
  	python ${projectDir}/modules/local/Hail_variant_MT_QC.py $MT_Step1_input_tsv $MT_Step2_participant_data $MT_participants_to_subset $MT_Step3_participant_data $pon_prediction_table $artifact_prone_sites_bed $reference $reference_index $mitotip_predictions_table $params.tmp_dir
            ^^^^^^^^^^
  ```

- Warning: `modules/local/Hail_variant_QC.nf:24:14`: The use of `projectDir` in a process is discouraged -- input files should be provided as process inputs

  ```nextflow
      python ${projectDir}/modules/local/Hail_variant_QC.py $vcf_sample_filtered $sample_sex_file $params.tmp_dir $params.genome
               ^^^^^^^^^^
  ```

- Warning: `modules/local/MT_Step2_participant_data.nf:5:19`: Variable was declared but not used

  ```nextflow
          tuple val(meta), path(Sample_MT_Step2_participant_data)
                    ^^^^
  ```

- Warning: `modules/local/MT_Step3_metadata_sample.nf:10:12`: Variable was declared but not used

  ```nextflow
  	tuple val(meta), path(mosdepth)
             ^^^^
  ```

- Warning: `modules/local/MT_Step3_metadata_sample.nf:18:12`: The use of `projectDir` in a process is discouraged -- input files should be provided as process inputs

  ```nextflow
  	Rscript ${projectDir}/modules/local/MT_Step3_metadata_sample.R ${mosdepth} ${haplocheck}
             ^^^^^^^^^^
  ```

- Warning: `modules/local/filtermutectcalls/main.nf:26:9`: Variable was declared but not used

  ```nextflow
      def args = task.ext.args ?: ''
          ^^^^
  ```

- Warning: `modules/local/filtermutectcalls/main.nf:27:9`: Variable was declared but not used

  ```nextflow
      def prefix = task.ext.prefix ?: "${meta.id}"
          ^^^^^^
  ```

- Warning: `modules/local/gatk4/mergemutectstats/main.nf:24:9`: Variable was declared but not used

  ```nextflow
      def input_list = stats.collect{ "--stats ${it}"}.join(' ')
          ^^^^^^^^^^
  ```

- Warning: `modules/local/gatk4/mergemutectstats/main.nf:24:48`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
      def input_list = stats.collect{ "--stats ${it}"}.join(' ')
                                                 ^^
  ```

- Warning: `modules/local/haplocheck/main.nf:23:9`: Variable was declared but not used

  ```nextflow
      def args = task.ext.args ?: ''
          ^^^^
  ```

- Warning: `modules/local/shift_back.nf:19:12`: The use of `projectDir` in a process is discouraged -- input files should be provided as process inputs

  ```nextflow
  	Rscript ${projectDir}/modules/local/shift_back.R $MT_shifted_CollectMetrics $MT_CollectMetrics
             ^^^^^^^^^^
  ```

- Warning: `modules/nf-core/custom/dumpsoftwareversions/main.nf:22:9`: Variable was declared but not used

  ```nextflow
      def args = task.ext.args ?: ''
          ^^^^
  ```

- Warning: `modules/nf-core/fastqc/main.nf:27:48`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
      def renamed_files = old_new_pairs.collect{ old_name, new_name -> new_name }.join(' ')
                                                 ^^^^^^^^
  ```

- Warning: `modules/nf-core/gatk4/filtermutectcalls/main.nf:29:113`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
      def orientationbias_command = orientationbias ? orientationbias.collect{"--orientation-bias-artifact-priors $it"}.join(' ') : ''
                                                                                                                  ^^
  ```

- Warning: `modules/nf-core/gatk4/filtermutectcalls/main.nf:30:96`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
      def segmentation_command    = segmentation    ? segmentation.collect{"--tumor-segmentation $it"}.join(' ')                  : ''
                                                                                                 ^^
  ```

- Warning: `modules/nf-core/gatk4/markduplicates/main.nf:29:43`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
      def input_list = bam.collect{"--INPUT $it"}.join(' ')
                                            ^^
  ```

- Warning: `modules/nf-core/gatk4/mergemutectstats/main.nf:23:48`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
      def input_list = stats.collect{ "--stats ${it}"}.join(' ')
                                                 ^^
  ```

- Warning: `modules/nf-core/gatk4/mergevcfs/main.nf:25:44`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
      def input_list = vcf.collect{ "--INPUT $it"}.join(' ')
                                             ^^
  ```

- Warning: `modules/nf-core/gatk4/mutect2/main.nf:33:42`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
      def inputs = input.collect{ "--input $it"}.join(" ")
                                           ^^
  ```

- Warning: `modules/nf-core/glnexus/main.nf:25:33`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
      def input = gvcfs.collect { it.toString() }
                                  ^^
  ```

- Warning: `modules/nf-core/haplocheck/main.nf:22:9`: Variable was declared but not used

  ```nextflow
      def args = task.ext.args ?: ''
          ^^^^
  ```

- Warning: `modules/nf-core/picard/collectwgsmetrics/main.nf:12:15`: Variable was declared but not used

  ```nextflow
      tuple val(meta2), path(fasta)
                ^^^^^
  ```

- Warning: `modules/nf-core/tabix/tabix/main.nf:33:9`: Variable was declared but not used

  ```nextflow
      def prefix = task.ext.prefix ?: "${meta.id}"
          ^^^^^^
  ```

- Warning: `subworkflows/local/input_check.nf:15:37`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          .map { create_fastq_channel(it) }
                                      ^^
  ```

- Warning: `workflows/variantcatalogue.nf:17:21`: Variable was declared but not used

  ```nextflow
  if (params.input) { ch_input = file(params.input) } else { exit 1, 'Input samplesheet not specified!' }
                      ^^^^^^^^
  ```

- Warning: `workflows/variantcatalogue.nf:25:1`: Variable was declared but not used

  ```nextflow
  ch_multiqc_config          = Channel.fromPath("$projectDir/assets/multiqc_config.yml", checkIfExists: true)
  ^^^^^^^^^^^^^^^^^
  ```

- Warning: `workflows/variantcatalogue.nf:25:30`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
  ch_multiqc_config          = Channel.fromPath("$projectDir/assets/multiqc_config.yml", checkIfExists: true)
                               ^^^^^^^
  ```

- Warning: `workflows/variantcatalogue.nf:26:1`: Variable was declared but not used

  ```nextflow
  ch_multiqc_custom_config   = params.multiqc_config ? Channel.fromPath( params.multiqc_config, checkIfExists: true ) : Channel.empty()
  ^^^^^^^^^^^^^^^^^^^^^^^^
  ```

- Warning: `workflows/variantcatalogue.nf:26:54`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
  ch_multiqc_custom_config   = params.multiqc_config ? Channel.fromPath( params.multiqc_config, checkIfExists: true ) : Channel.empty()
                                                       ^^^^^^^
  ```

- Warning: `workflows/variantcatalogue.nf:26:119`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
  ch_multiqc_custom_config   = params.multiqc_config ? Channel.fromPath( params.multiqc_config, checkIfExists: true ) : Channel.empty()
                                                                                                                        ^^^^^^^
  ```

- Warning: `workflows/variantcatalogue.nf:27:1`: Variable was declared but not used

  ```nextflow
  ch_multiqc_logo            = params.multiqc_logo   ? Channel.fromPath( params.multiqc_logo, checkIfExists: true ) : Channel.empty()
  ^^^^^^^^^^^^^^^
  ```

- Warning: `workflows/variantcatalogue.nf:27:54`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
  ch_multiqc_logo            = params.multiqc_logo   ? Channel.fromPath( params.multiqc_logo, checkIfExists: true ) : Channel.empty()
                                                       ^^^^^^^
  ```

- Warning: `workflows/variantcatalogue.nf:27:117`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
  ch_multiqc_logo            = params.multiqc_logo   ? Channel.fromPath( params.multiqc_logo, checkIfExists: true ) : Channel.empty()
                                                                                                                      ^^^^^^^
  ```

- Warning: `workflows/variantcatalogue.nf:28:1`: Variable was declared but not used

  ```nextflow
  ch_multiqc_custom_methods_description = params.multiqc_methods_description ? file(params.multiqc_methods_description, checkIfExists: true) : file("$projectDir/assets/methods_description_template.yml", checkIfExists: true)
  ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  ```

- Warning: `workflows/variantcatalogue.nf:139:19`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_versions = Channel.empty()
                    ^^^^^^^
  ```

- Warning: `workflows/variantcatalogue.nf:216:20`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_case_info = Channel.from([id:'SNV'])
                     ^^^^^^^
  ```

- Warning: `workflows/variantcatalogue.nf:219:22`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
              .collect{it[1]}
                       ^^
  ```

- Warning: `workflows/variantcatalogue.nf:275:5`: Variable was declared but not used

  ```nextflow
      reference_MT_shifted_dict = [
      ^^^^^^^^^^^^^^^^^^^^^^^^^
  ```

- Warning: `workflows/variantcatalogue.nf:360:27`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_workflow_summary = Channel.value(workflow_summary)
                            ^^^^^^^
  ```

- Warning: `workflows/variantcatalogue.nf:363:30`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_methods_description = Channel.value(methods_description)
                               ^^^^^^^
  ```

- Warning: `workflows/variantcatalogue.nf:365:24`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_multiqc_files = Channel.empty()
                         ^^^^^^^
  ```

- Warning: `workflows/variantcatalogue.nf:369:68`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
      ch_multiqc_files = ch_multiqc_files.mix(FASTQC.out.zip.collect{it[1]}.ifEmpty([]))
                                                                     ^^
  ```

- Warning: `workflows/variantcatalogue.nf:370:77`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
      ch_multiqc_files = ch_multiqc_files.mix(MOSDEPTH.out.global_txt.collect{it[1]}.ifEmpty([]))
                                                                              ^^
  ```

- Warning: `workflows/variantcatalogue.nf:371:90`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
      ch_multiqc_files = ch_multiqc_files.mix(PICARD_COLLECTWGSMETRICS.out.metrics.collect{it[1]}.ifEmpty([]))
                                                                                           ^^
  ```

- Warning: `workflows/variantcatalogue.nf:372:102`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
      ch_multiqc_files = ch_multiqc_files.mix(Picard_CollectAlignmentSummaryMetrics.out.report.collect{it[1]}.ifEmpty([]))
                                                                                                       ^^
  ```

- Warning: `workflows/variantcatalogue.nf:373:96`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
      ch_multiqc_files = ch_multiqc_files.mix(Picard_QualityScoreDistribution.out.report.collect{it[1]}.ifEmpty([]))
                                                                                                 ^^
  ```

- Warning: `workflows/variantcatalogue.nf:382:5`: Variable was declared but not used

  ```nextflow
      multiqc_report = MULTIQC.out.report.toList()
      ^^^^^^^^^^^^^^
  ```
