# Nextflow lint results

- Generated: 2026-01-16T06:42:27.754154747Z
- Nextflow version: 25.12.0-edge
- Summary: 66 errors, 13 warnings

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

- Error: `main.nf:21:1`: Module could not be parsed: '/home/runner/work/strict-syntax-health/strict-syntax-health/pipelines/viralintegration/subworkflows/local/utils_nfcore_viralintegration_pipeline/main.nf'

  ```nextflow
  include { PIPELINE_INITIALISATION } from './subworkflows/local/utils_nfcore_viralintegration_pipeline'
  ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  ```

- Error: `main.nf:22:1`: Module could not be parsed: '/home/runner/work/strict-syntax-health/strict-syntax-health/pipelines/viralintegration/subworkflows/local/utils_nfcore_viralintegration_pipeline/main.nf'

  ```nextflow
  include { PIPELINE_COMPLETION     } from './subworkflows/local/utils_nfcore_viralintegration_pipeline'
  ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  ```

- Error: `main.nf:23:1`: Module could not be parsed: '/home/runner/work/strict-syntax-health/strict-syntax-health/pipelines/viralintegration/subworkflows/local/utils_nfcore_viralintegration_pipeline/main.nf'

  ```nextflow
  include { getGenomeAttribute      } from './subworkflows/local/utils_nfcore_viralintegration_pipeline'
  ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  ```

- Error: `main.nf:34:16`: `getGenomeAttribute` is not defined

  ```nextflow
  params.fasta = getGenomeAttribute('fasta')
                 ^^^^^^^^^^^^^^^^^^
  ```

- Error: `main.nf:35:14`: `getGenomeAttribute` is not defined

  ```nextflow
  params.gtf = getGenomeAttribute('gtf')
               ^^^^^^^^^^^^^^^^^^
  ```

- Error: `main.nf:77:5`: `PIPELINE_INITIALISATION` is not defined

  ```nextflow
      PIPELINE_INITIALISATION (
      ^^^^^^^^^^^^^^^^^^^^^^^
  ```

- Error: `main.nf:91:9`: `PIPELINE_INITIALISATION` is not defined

  ```nextflow
          PIPELINE_INITIALISATION.out.samplesheet
          ^^^^^^^^^^^^^^^^^^^^^^^
  ```

- Error: `main.nf:97:5`: `PIPELINE_COMPLETION` is not defined

  ```nextflow
      PIPELINE_COMPLETION (
      ^^^^^^^^^^^^^^^^^^^
  ```

- Error: `modules/local/abridged_tsv.nf:7:5`: Invalid process directive

  ```nextflow
      if (workflow.profile.tokenize(',').intersect(['conda', 'mamba']).size() >= 1) {
      ^
  ```

- Error: `modules/local/chimeric_contig_evidence_analyzer.nf:1:1`: Invalid process definition -- check for missing or out-of-order section labels

  ```nextflow
  process CHIMERIC_CONTIG_EVIDENCE_ANALYZER {
  ^
  ```

- Error: `modules/local/extract_chimeric_genomic_targets.nf:7:5`: Invalid process directive

  ```nextflow
      if (workflow.profile.tokenize(',').intersect(['conda', 'mamba']).size() >= 1) {
      ^
  ```

- Error: `modules/local/insertion_site_candidates.nf:7:5`: Invalid process directive

  ```nextflow
      if (workflow.profile.tokenize(',').intersect(['conda', 'mamba']).size() >= 1) {
      ^
  ```

- Error: `modules/local/polyA_stripper.nf:7:5`: Invalid process directive

  ```nextflow
      if (workflow.profile.tokenize(',').intersect(['conda', 'mamba']).size() >= 1) {
      ^
  ```

- Error: `modules/local/remove_duplicates.nf:7:5`: Invalid process directive

  ```nextflow
      if (workflow.profile.tokenize(',').intersect(['conda', 'mamba']).size() >= 1) {
      ^
  ```

- Error: `modules/local/star_align_validate.nf:1:1`: Invalid process definition -- check for missing or out-of-order section labels

  ```nextflow
  process STAR_ALIGN_VALIDATE {
  ^
  ```

- Error: `modules/local/summary_report.nf:1:1`: Invalid process definition -- check for missing or out-of-order section labels

  ```nextflow
  process SUMMARY_REPORT {
  ^
  ```

- Error: `modules/local/virus_report.nf:7:5`: Invalid process directive

  ```nextflow
      if (workflow.profile.tokenize(',').intersect(['conda', 'mamba']).size() >= 1) {
      ^
  ```

- Error: `modules/nf-core/multiqc/main.nf:28:31`: Unexpected input: '/'

  ```nextflow
      def logo = multiqc_logo ? /--cl-config 'custom_logo: "${multiqc_logo}"'/ : ''
                                ^
  ```

- Error: `modules/nf-core/star/align/main.nf:41:9`: `seq_platform` is already declared

  ```nextflow
      def seq_platform    = seq_platform ? "'PL:$seq_platform'" : ""
          ^^^^^^^^^^^^
  ```

- Error: `modules/nf-core/star/align/main.nf:42:9`: `seq_center` is already declared

  ```nextflow
      def seq_center      = seq_center ? "--outSAMattrRGline ID:$prefix 'CN:$seq_center' 'SM:$prefix' $seq_platform " : "--outSAMattrRGline ID:$prefix 'SM:$prefix' $seq_platform "
          ^^^^^^^^^^
  ```

- Error: `nextflow.config:79:5`: Unexpected input: 'includeConfig'

  ```nextflow
      includeConfig "${params.custom_config_base}/nfcore_custom.config"
      ^
  ```

- Error: `subworkflows/local/utils_nfcore_viralintegration_pipeline/main.nf:243:21`: Unexpected input: 'doi_ref'

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

- Error: `workflows/viralintegration.nf:7:1`: Module could not be parsed: '/home/runner/work/strict-syntax-health/strict-syntax-health/pipelines/viralintegration/subworkflows/nf-core/utils_nfcore_pipeline/main.nf'

  ```nextflow
  include { paramsSummaryMultiqc   } from '../subworkflows/nf-core/utils_nfcore_pipeline'
  ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  ```

- Error: `workflows/viralintegration.nf:8:1`: Module could not be parsed: '/home/runner/work/strict-syntax-health/strict-syntax-health/pipelines/viralintegration/subworkflows/nf-core/utils_nfcore_pipeline/main.nf'

  ```nextflow
  include { softwareVersionsToYAML } from '../subworkflows/nf-core/utils_nfcore_pipeline'
  ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  ```

- Error: `workflows/viralintegration.nf:9:1`: Module could not be parsed: '/home/runner/work/strict-syntax-health/strict-syntax-health/pipelines/viralintegration/subworkflows/local/utils_nfcore_viralintegration_pipeline/main.nf'

  ```nextflow
  include { methodsDescriptionText } from '../subworkflows/local/utils_nfcore_viralintegration_pipeline'
  ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  ```

- Error: `workflows/viralintegration.nf:23:1`: Module could not be parsed: '/home/runner/work/strict-syntax-health/strict-syntax-health/pipelines/viralintegration/modules/nf-core/multiqc/main.nf'

  ```nextflow
  include { MULTIQC                     } from '../modules/nf-core/multiqc/main'
  ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  ```

- Error: `workflows/viralintegration.nf:24:1`: Statements cannot be mixed with script declarations -- move statements into a process, workflow, or function

  ```nextflow
  ch_igvjs_VIF             = file("$projectDir/assets/igvjs_VIF.html", checkIfExists: true)
  ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  ```

- Error: `workflows/viralintegration.nf:38:1`: Included name 'STAR_ALIGN_VALIDATE' is not defined in module '/home/runner/work/strict-syntax-health/strict-syntax-health/pipelines/viralintegration/modules/local/star_align_validate.nf'

  ```nextflow
  include { STAR_ALIGN_VALIDATE } from '../modules/local/star_align_validate'
  ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  ```

- Error: `workflows/viralintegration.nf:39:1`: Included name 'CHIMERIC_CONTIG_EVIDENCE_ANALYZER' is not defined in module '/home/runner/work/strict-syntax-health/strict-syntax-health/pipelines/viralintegration/modules/local/chimeric_contig_evidence_analyzer.nf'

  ```nextflow
  include { CHIMERIC_CONTIG_EVIDENCE_ANALYZER } from '../modules/local/chimeric_contig_evidence_analyzer'
  ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  ```

- Error: `workflows/viralintegration.nf:40:1`: Included name 'SUMMARY_REPORT' is not defined in module '/home/runner/work/strict-syntax-health/strict-syntax-health/pipelines/viralintegration/modules/local/summary_report.nf'

  ```nextflow
  include { SUMMARY_REPORT } from '../modules/local/summary_report'
  ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  ```

- Error: `workflows/viralintegration.nf:152:9`: `ch_igvjs_VIF` is not defined

  ```nextflow
          ch_igvjs_VIF
          ^^^^^^^^^^^^
  ```

- Error: `workflows/viralintegration.nf:169:5`: `STAR_ALIGN_VALIDATE` is not defined

  ```nextflow
      STAR_ALIGN_VALIDATE (
      ^^^^^^^^^^^^^^^^^^^
  ```

- Error: `workflows/viralintegration.nf:175:35`: `STAR_ALIGN_VALIDATE` is not defined

  ```nextflow
      ch_versions = ch_versions.mix(STAR_ALIGN_VALIDATE.out.versions.first())
                                    ^^^^^^^^^^^^^^^^^^^
  ```

- Error: `workflows/viralintegration.nf:178:9`: `STAR_ALIGN_VALIDATE` is not defined

  ```nextflow
          STAR_ALIGN_VALIDATE.out.bam
          ^^^^^^^^^^^^^^^^^^^
  ```

- Error: `workflows/viralintegration.nf:202:5`: `CHIMERIC_CONTIG_EVIDENCE_ANALYZER` is not defined

  ```nextflow
      CHIMERIC_CONTIG_EVIDENCE_ANALYZER (
      ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  ```

- Error: `workflows/viralintegration.nf:205:35`: `CHIMERIC_CONTIG_EVIDENCE_ANALYZER` is not defined

  ```nextflow
      ch_versions = ch_versions.mix(CHIMERIC_CONTIG_EVIDENCE_ANALYZER.out.versions.first())
                                    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  ```

- Error: `workflows/viralintegration.nf:207:5`: `CHIMERIC_CONTIG_EVIDENCE_ANALYZER` is not defined

  ```nextflow
      CHIMERIC_CONTIG_EVIDENCE_ANALYZER.out.evidence_bam
      ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  ```

- Error: `workflows/viralintegration.nf:208:15`: `CHIMERIC_CONTIG_EVIDENCE_ANALYZER` is not defined

  ```nextflow
          .join(CHIMERIC_CONTIG_EVIDENCE_ANALYZER.out.evidence_bai, by: [0])
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  ```

- Error: `workflows/viralintegration.nf:210:15`: `CHIMERIC_CONTIG_EVIDENCE_ANALYZER` is not defined

  ```nextflow
          .join(CHIMERIC_CONTIG_EVIDENCE_ANALYZER.out.evidence_counts, by: [0])
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  ```

- Error: `workflows/viralintegration.nf:218:5`: `SUMMARY_REPORT` is not defined

  ```nextflow
      SUMMARY_REPORT(
      ^^^^^^^^^^^^^^
  ```

- Error: `workflows/viralintegration.nf:221:9`: `ch_igvjs_VIF` is not defined

  ```nextflow
          ch_igvjs_VIF
          ^^^^^^^^^^^^
  ```

- Error: `workflows/viralintegration.nf:223:35`: `SUMMARY_REPORT` is not defined

  ```nextflow
      ch_versions = ch_versions.mix(SUMMARY_REPORT.out.versions.first())
                                    ^^^^^^^^^^^^^^
  ```

- Error: `workflows/viralintegration.nf:228:5`: `softwareVersionsToYAML` is not defined

  ```nextflow
      softwareVersionsToYAML(ch_versions)
      ^^^^^^^^^^^^^^^^^^^^^^
  ```

- Error: `workflows/viralintegration.nf:250:41`: `paramsSummaryMultiqc` is not defined

  ```nextflow
      ch_workflow_summary = Channel.value(paramsSummaryMultiqc(summary_params))
                                          ^^^^^^^^^^^^^^^^^^^^
  ```

- Error: `workflows/viralintegration.nf:256:9`: `methodsDescriptionText` is not defined

  ```nextflow
          methodsDescriptionText(ch_multiqc_custom_methods_description))
          ^^^^^^^^^^^^^^^^^^^^^^
  ```

- Error: `workflows/viralintegration.nf:268:5`: `MULTIQC` is not defined

  ```nextflow
      MULTIQC (
      ^^^^^^^
  ```

- Error: `workflows/viralintegration.nf:276:22`: `MULTIQC` is not defined

  ```nextflow
      multiqc_report = MULTIQC.out.report.toList() // channel: /path/to/multiqc_report.html
                       ^^^^^^^
  ```

## :warning: Warnings

- Warning: `modules/nf-core/fastqc/main.nf:27:48`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
      def renamed_files = old_new_pairs.collect{ old_name, new_name -> new_name }.join(' ')
                                                 ^^^^^^^^
  ```

- Warning: `workflows/viralintegration.nf:24:1`: Variable was declared but not used

  ```nextflow
  ch_igvjs_VIF             = file("$projectDir/assets/igvjs_VIF.html", checkIfExists: true)
  ^^^^^^^^^^^^
  ```

- Warning: `workflows/viralintegration.nf:56:19`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_versions = Channel.empty()
                    ^^^^^^^
  ```

- Warning: `workflows/viralintegration.nf:57:24`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_multiqc_files = Channel.empty()
                         ^^^^^^^
  ```

- Warning: `workflows/viralintegration.nf:65:68`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
      ch_multiqc_files = ch_multiqc_files.mix(FASTQC.out.zip.collect{it[1]})
                                                                     ^^
  ```

- Warning: `workflows/viralintegration.nf:188:25`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_to_dupe_or_not = Channel.empty()
                          ^^^^^^^
  ```

- Warning: `workflows/viralintegration.nf:239:32`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_multiqc_config        = Channel.fromPath(
                                 ^^^^^^^
  ```

- Warning: `workflows/viralintegration.nf:242:9`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
          Channel.fromPath(params.multiqc_config, checkIfExists: true) :
          ^^^^^^^
  ```

- Warning: `workflows/viralintegration.nf:243:9`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
          Channel.empty()
          ^^^^^^^
  ```

- Warning: `workflows/viralintegration.nf:245:9`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
          Channel.fromPath(params.multiqc_logo, checkIfExists: true) :
          ^^^^^^^
  ```

- Warning: `workflows/viralintegration.nf:246:9`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
          Channel.empty()
          ^^^^^^^
  ```

- Warning: `workflows/viralintegration.nf:250:27`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_workflow_summary = Channel.value(paramsSummaryMultiqc(summary_params))
                            ^^^^^^^
  ```

- Warning: `workflows/viralintegration.nf:255:45`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_methods_description                = Channel.value(
                                              ^^^^^^^
  ```
