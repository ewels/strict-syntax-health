# Nextflow lint results

- Generated: 2026-01-16T06:34:36.681690832Z
- Nextflow version: 25.12.0-edge
- Summary: 52 errors, 123 warnings

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
          memory = { check_max( 84.GB * task.attempt, 'memory'  ) }
                     ^^^^^^^^^
  ```

- Error: `conf/base.config:45:20`: `check_max` is not defined

  ```nextflow
          time   = { check_max( 16.h  * task.attempt, 'time'    ) }
                     ^^^^^^^^^
  ```

- Error: `conf/base.config:48:20`: `check_max` is not defined

  ```nextflow
          cpus   = { check_max( 12    * task.attempt, 'cpus'    ) }
                     ^^^^^^^^^
  ```

- Error: `conf/base.config:49:20`: `check_max` is not defined

  ```nextflow
          memory = { check_max( 84.GB * task.attempt, 'memory'  ) }
                     ^^^^^^^^^
  ```

- Error: `conf/base.config:50:20`: `check_max` is not defined

  ```nextflow
          time   = { check_max( 20.h  * task.attempt, 'time'    ) }
                     ^^^^^^^^^
  ```

- Error: `conf/base.config:53:20`: `check_max` is not defined

  ```nextflow
          time   = { check_max( 20.h  * task.attempt, 'time'    ) }
                     ^^^^^^^^^
  ```

- Error: `conf/base.config:56:20`: `check_max` is not defined

  ```nextflow
          memory = { check_max( 200.GB * task.attempt, 'memory' ) }
                     ^^^^^^^^^
  ```

- Error: `conf/modules.config:139:32`: `$` is not defined

  ```nextflow
                  ext.prefix = { ${meta.id} }
                                 ^
  ```

- Error: `conf/modules.config:177:32`: `$` is not defined

  ```nextflow
                  ext.prefix = { ${meta.id} }
                                 ^
  ```

- Error: `conf/modules.config:316:31`: `$` is not defined

  ```nextflow
                  ext.prefix ={ ${meta.id} }
                                ^
  ```

- Error: `conf/modules.config:332:31`: `$` is not defined

  ```nextflow
                  ext.prefix ={ ${meta.id} }
                                ^
  ```

- Error: `conf/modules.config:351:39`: `$` is not defined

  ```nextflow
                          ext.prefix ={ ${meta.id} }
                                        ^
  ```

- Error: `main.nf:21:1`: Module could not be parsed: '/home/runner/work/strict-syntax-health/strict-syntax-health/pipelines/metaboigniter/subworkflows/local/utils_nfcore_metaboigniter_pipeline/main.nf'

  ```nextflow
  include { PIPELINE_INITIALISATION } from './subworkflows/local/utils_nfcore_metaboigniter_pipeline'
  ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  ```

- Error: `main.nf:22:1`: Module could not be parsed: '/home/runner/work/strict-syntax-health/strict-syntax-health/pipelines/metaboigniter/subworkflows/local/utils_nfcore_metaboigniter_pipeline/main.nf'

  ```nextflow
  include { PIPELINE_COMPLETION     } from './subworkflows/local/utils_nfcore_metaboigniter_pipeline'
  ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  ```

- Error: `main.nf:71:5`: `PIPELINE_INITIALISATION` is not defined

  ```nextflow
      PIPELINE_INITIALISATION (
      ^^^^^^^^^^^^^^^^^^^^^^^
  ```

- Error: `main.nf:85:9`: `PIPELINE_INITIALISATION` is not defined

  ```nextflow
          PIPELINE_INITIALISATION.out.samplesheet
          ^^^^^^^^^^^^^^^^^^^^^^^
  ```

- Error: `main.nf:91:5`: `PIPELINE_COMPLETION` is not defined

  ```nextflow
      PIPELINE_COMPLETION (
      ^^^^^^^^^^^^^^^^^^^
  ```

- Error: `modules/local/ms2query_modelfulltrain.nf:34:49`: `PWD` is not defined

  ```nextflow
      fulltrain_ms2query.py --input $mgf --output $PWD/output/  --polarity negative
                                                  ^^^^
  ```

- Error: `modules/local/pyopenms_extractmapping.nf:28:18`: `featurexmlcomplete` is not defined

  ```nextflow
          --inputc $featurexmlcomplete --inputr $featurexmlreq --output ${prefix}.csv $args
                   ^^^^^^^^^^^^^^^^^^^
  ```

- Error: `modules/local/pyopenms_extractmapping.nf:28:47`: `featurexmlreq` is not defined

  ```nextflow
          --inputc $featurexmlcomplete --inputr $featurexmlreq --output ${prefix}.csv $args
                                                ^^^^^^^^^^^^^^
  ```

- Error: `modules/nf-core/multiqc/main.nf:28:31`: Unexpected input: '/'

  ```nextflow
      def logo = multiqc_logo ? /--cl-config 'custom_logo: "${multiqc_logo}"'/ : ''
                                ^
  ```

- Error: `nextflow.config:304:5`: Unexpected input: 'includeConfig'

  ```nextflow
      includeConfig "${params.custom_config_base}/nfcore_custom.config"
      ^
  ```

- Error: `subworkflows/local/identification.nf:106:20`: Incomplete expression

  ```nextflow
  generated_params = OPENMS_FILEFILTER.out.consensusxml.map{it[0]}.combine(
                     ^^^^^^^^^^^^^^
  ```

- Error: `subworkflows/local/identification.nf:137:1`: Incomplete expression

  ```nextflow
  OPENMS_FILEFILTER.out.consensusxml.map{it[0]}.combine(
  ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  ```

- Error: `subworkflows/local/identification.nf:165:1`: Incomplete expression

  ```nextflow
  OPENMS_FILEFILTER.out.consensusxml.map{it[0]}.combine(
  ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  ```

- Error: `subworkflows/local/linker.nf:88:80`: `consensusxml` is already declared

  ```nextflow
          consensusxml=OPENMS_FEATURELINKERUNLABELEDKD.out.consensusxml.map{meta,consensusxml->[[id:consensusxml.baseName],consensusxml]}
                                                                                 ^^^^^^^^^^^^
  ```

- Error: `subworkflows/local/quantification.nf:32:5`: Variables in a closure should be declared with `def`

  ```nextflow
      idd=mzml.baseName
      ^^^
  ```

- Error: `subworkflows/local/utils_nfcore_metaboigniter_pipeline/main.nf:239:21`: Unexpected input: 'doi_ref'

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

- Error: `workflows/metaboigniter.nf:31:1`: Module could not be parsed: '/home/runner/work/strict-syntax-health/strict-syntax-health/pipelines/metaboigniter/modules/nf-core/multiqc/main.nf'

  ```nextflow
  include { MULTIQC                } from '../modules/nf-core/multiqc/main'
  ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  ```

- Error: `workflows/metaboigniter.nf:33:1`: Module could not be parsed: '/home/runner/work/strict-syntax-health/strict-syntax-health/pipelines/metaboigniter/subworkflows/nf-core/utils_nfcore_pipeline/main.nf'

  ```nextflow
  include { paramsSummaryMultiqc   } from '../subworkflows/nf-core/utils_nfcore_pipeline'
  ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  ```

- Error: `workflows/metaboigniter.nf:34:1`: Module could not be parsed: '/home/runner/work/strict-syntax-health/strict-syntax-health/pipelines/metaboigniter/subworkflows/nf-core/utils_nfcore_pipeline/main.nf'

  ```nextflow
  include { softwareVersionsToYAML } from '../subworkflows/nf-core/utils_nfcore_pipeline'
  ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  ```

- Error: `workflows/metaboigniter.nf:35:1`: Module could not be parsed: '/home/runner/work/strict-syntax-health/strict-syntax-health/pipelines/metaboigniter/subworkflows/local/utils_nfcore_metaboigniter_pipeline/main.nf'

  ```nextflow
  include { methodsDescriptionText } from '../subworkflows/local/utils_nfcore_metaboigniter_pipeline'
  ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  ```

- Error: `workflows/metaboigniter.nf:143:5`: `softwareVersionsToYAML` is not defined

  ```nextflow
      softwareVersionsToYAML(ch_versions)
      ^^^^^^^^^^^^^^^^^^^^^^
  ```

- Error: `workflows/metaboigniter.nf:165:41`: `paramsSummaryMultiqc` is not defined

  ```nextflow
      ch_workflow_summary = Channel.value(paramsSummaryMultiqc(summary_params))
                                          ^^^^^^^^^^^^^^^^^^^^
  ```

- Error: `workflows/metaboigniter.nf:171:9`: `methodsDescriptionText` is not defined

  ```nextflow
          methodsDescriptionText(ch_multiqc_custom_methods_description))
          ^^^^^^^^^^^^^^^^^^^^^^
  ```

- Error: `workflows/metaboigniter.nf:183:5`: `MULTIQC` is not defined

  ```nextflow
      MULTIQC (
      ^^^^^^^
  ```

- Error: `workflows/metaboigniter.nf:191:22`: `MULTIQC` is not defined

  ```nextflow
      multiqc_report = MULTIQC.out.report.toList() // channel: /path/to/multiqc_report.html
                       ^^^^^^^
  ```

## :warning: Warnings

- Warning: `modules/local/general_mergefile.nf:22:48`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
      def inputs        = input_target.collect { it }.join(' ')
                                                 ^^
  ```

- Warning: `modules/local/ms2query_checkmodelfiles.nf:31:51`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
      def model_files        = modelfiles.collect { it }.join(' ')
                                                    ^^
  ```

- Warning: `modules/local/ms2query_modelfulltrain.nf:29:9`: Variable was declared but not used

  ```nextflow
      def args = task.ext.args ?: ''
          ^^^^
  ```

- Warning: `modules/local/ms2query_modelfulltrain.nf:30:9`: Variable was declared but not used

  ```nextflow
      def prefix = task.ext.prefix ?: "${meta.id}"
          ^^^^^^
  ```

- Warning: `modules/local/ms2query_modeltrain.nf:30:9`: Variable was declared but not used

  ```nextflow
      def prefix = task.ext.prefix ?: "${meta.id}"
          ^^^^^^
  ```

- Warning: `modules/local/openms_featurelinkerunlabeledkd.nf:23:56`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
      def featurexml_input        = featurexml.collect { it }.join(' ')
                                                         ^^
  ```

- Warning: `modules/local/openms_filefilter.nf:55:9`: Variable was declared but not used

  ```nextflow
      def args = task.ext.args ?: ''
          ^^^^
  ```

- Warning: `modules/local/openms_gnpsexport.nf:28:9`: Variable was declared but not used

  ```nextflow
      def prefix = task.ext.prefix ?: meta.id
          ^^^^^^
  ```

- Warning: `modules/local/openms_gnpsexport.nf:29:44`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
      def mzml_input        = mzml.collect { it }.join(' ')
                                             ^^
  ```

- Warning: `modules/local/openms_idmapperconsensus.nf:21:9`: Variable was declared but not used

  ```nextflow
      def args = task.ext.args ?: ''
          ^^^^
  ```

- Warning: `modules/local/openms_mapalignerposeclustering.nf:16:56`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
      tuple val(meta), path({meta.id.collect { 'output/'+it+'.trafoXML' }}), emit: trafoxml
                                                         ^^
  ```

- Warning: `modules/local/openms_mapalignerposeclustering.nf:17:56`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
      tuple val(meta), path({meta.id.collect { 'output/'+it+'.featureXML' }}), emit: featurexml
                                                         ^^
  ```

- Warning: `modules/local/openms_mapalignerposeclustering.nf:27:56`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
      def featurexml_input        = featurexml.collect { it }.join(' ')
                                                         ^^
  ```

- Warning: `modules/local/openms_mapalignerposeclustering.nf:28:61`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
      def trafoxml_output        = prefix.collect { 'output/'+it+'.trafoXML' }.join(' ')
                                                              ^^
  ```

- Warning: `modules/local/openms_mapalignerposeclustering.nf:29:63`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
      def featurexml_output        = prefix.collect { 'output/'+it+'.featureXML' }.join(' ')
                                                                ^^
  ```

- Warning: `modules/local/openms_mapalignerposeclusteringmzml.nf:14:56`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
      tuple val(meta), path({meta.id.collect { 'output/'+it+'.trafoXML' }}), emit: trafoxml
                                                         ^^
  ```

- Warning: `modules/local/openms_mapalignerposeclusteringmzml.nf:15:56`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
      tuple val(meta), path({meta.id.collect { 'output/'+it+'.mzML' }}), emit: mzml
                                                         ^^
  ```

- Warning: `modules/local/openms_mapalignerposeclusteringmzml.nf:26:56`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
      def featurexml_input        = featurexml.collect { it }.join(' ')
                                                         ^^
  ```

- Warning: `modules/local/openms_mapalignerposeclusteringmzml.nf:27:61`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
      def trafoxml_output        = prefix.collect { 'output/'+it+'.trafoXML' }.join(' ')
                                                              ^^
  ```

- Warning: `modules/local/openms_mapalignerposeclusteringmzml.nf:28:57`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
      def mzml_output        = prefix.collect { 'output/'+it+'.mzML' }.join(' ')
                                                          ^^
  ```

- Warning: `modules/local/openms_siriusparams.nf:23:9`: Variable was declared but not used

  ```nextflow
      def prefix = task.ext.prefix ?: "${meta.id}"
          ^^^^^^
  ```

- Warning: `modules/local/openms_siriusparams.nf:24:44`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
      def mzml_input        = mzml.collect { it }.join(' ')
                                             ^^
  ```

- Warning: `modules/local/openms_siriusparams.nf:25:46`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
      def ms_output        = mzml.collect { "${it.baseName}.ms" }.join(' ')
                                               ^^
  ```

- Warning: `modules/local/openms_siriusparams.nf:26:43`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
      def ms1_input        = mzml.collect { it }.join(' ')
                                            ^^
  ```

- Warning: `modules/local/openms_siriusparams.nf:27:56`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
      def featurexml_input        = featurexml.collect { it }.join(' ')
                                                         ^^
  ```

- Warning: `modules/local/pyopenms_conctsv.nf:25:9`: Variable was declared but not used

  ```nextflow
      def args = task.ext.args ?: ''
          ^^^^
  ```

- Warning: `modules/local/pyopenms_filemerger.nf:26:54`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
      def inputs        = consensusxml_input.collect { it }.join(' ')
                                                       ^^
  ```

- Warning: `modules/local/pyopenms_generatesearchparams.nf:27:53`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
      def mzml_input        = input_spectra.collect { it }.join(' ')
                                                      ^^
  ```

- Warning: `modules/local/pyopenms_generatesearchparams.nf:28:63`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
      def csv_output        = input_spectra.collect { "output/${it.baseName}${map_index}.csv" }.join(' ')
                                                                ^^
  ```

- Warning: `modules/local/pyopenms_isomapping.nf:25:53`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
      def mzml_input        = input_spectra.collect { it }.join(' ')
                                                      ^^
  ```

- Warning: `modules/local/pyopenms_msmapping.nf:24:53`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
      def mzml_input        = input_spectra.collect { it }.join(' ')
                                                      ^^
  ```

- Warning: `modules/local/pyopenms_removedup.nf:24:9`: Variable was declared but not used

  ```nextflow
      def args = task.ext.args ?: ''
          ^^^^
  ```

- Warning: `modules/local/pyopenms_removedup.nf:25:9`: Variable was declared but not used

  ```nextflow
      def prefix = task.ext.prefix ?: meta.id
          ^^^^^^
  ```

- Warning: `modules/local/pyopenms_removedup.nf:26:44`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
      def mzml_input        = mzml.collect { it }.join(' ')
                                             ^^
  ```

- Warning: `modules/local/pyopenms_splitconsensus.nf:22:9`: Variable was declared but not used

  ```nextflow
      def prefix = task.ext.prefix ?: "${meta.id}"
          ^^^^^^
  ```

- Warning: `modules/local/pyopenms_splitfeaturexml.nf:23:9`: Variable was declared but not used

  ```nextflow
      def prefix = task.ext.prefix ?: "${meta.id}"
          ^^^^^^
  ```

- Warning: `modules/local/pyopenms_splitmgf.nf:26:9`: Variable was declared but not used

  ```nextflow
      def prefix = task.ext.prefix ?: "${meta.id}"
          ^^^^^^
  ```

- Warning: `modules/local/sirius_search.nf:24:9`: Variable was declared but not used

  ```nextflow
      def prefix = task.ext.prefix ?: "${meta.id}"
          ^^^^^^
  ```

- Warning: `modules/nf-core/fastqc/main.nf:27:48`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
      def renamed_files = old_new_pairs.collect{ old_name, new_name -> new_name }.join(' ')
                                                 ^^^^^^^^
  ```

- Warning: `subworkflows/local/annotation.nf:9:9`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          empty_id
          ^^^^^^^^
  ```

- Warning: `subworkflows/local/annotation.nf:10:9`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          separate
          ^^^^^^^^
  ```

- Warning: `subworkflows/local/annotation.nf:11:9`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          mzml_files
          ^^^^^^^^^^
  ```

- Warning: `subworkflows/local/annotation.nf:16:19`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_versions = Channel.empty()
                    ^^^^^^^
  ```

- Warning: `subworkflows/local/annotation.nf:20:73`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          OPENMS_METABOLITEADDUCTDECHARGER(quantification_information.map{it[0,1]})
                                                                          ^^
  ```

- Warning: `subworkflows/local/annotation.nf:21:9`: Variable was declared but not used

  ```nextflow
          quantified_features=OPENMS_METABOLITEADDUCTDECHARGER.out.featurexml
          ^^^^^^^^^^^^^^^^^^^
  ```

- Warning: `subworkflows/local/annotation.nf:23:46`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          .join(quantification_information.map{it[0,2]},by:[0])
                                               ^^
  ```

- Warning: `subworkflows/local/identification.nf:23:5`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
      quantification_information
      ^^^^^^^^^^^^^^^^^^^^^^^^^^
  ```

- Warning: `subworkflows/local/identification.nf:41:15`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
  ch_versions = Channel.empty()
                ^^^^^^^
  ```

- Warning: `subworkflows/local/identification.nf:46:50`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
  consensusxml_data.combine(mzml_files.filter{meta,file->meta.level == "MS2" | meta.level == "MS12"}.collect{it[1]}
                                                   ^^^^
  ```

- Warning: `subworkflows/local/identification.nf:46:108`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
  consensusxml_data.combine(mzml_files.filter{meta,file->meta.level == "MS2" | meta.level == "MS12"}.collect{it[1]}
                                                                                                             ^^
  ```

- Warning: `subworkflows/local/identification.nf:70:67`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
  filtered_consensus = PYOPENMS_SPLITCONSENSUS.out.consensusxml.map{it[1]}.flatten().map{ file ->
                                                                    ^^
  ```

- Warning: `subworkflows/local/identification.nf:83:26`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
  mzml_files.filter{ meta, file -> meta.level == "MS2" || meta.level == "MS12" }.map{tuple ->
                           ^^^^
  ```

- Warning: `subworkflows/local/identification.nf:90:44`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          def metas = sortedTuples.collect { it[0] }
                                             ^^
  ```

- Warning: `subworkflows/local/identification.nf:91:44`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          def files = sortedTuples.collect { it[1] }
                                             ^^
  ```

- Warning: `subworkflows/local/identification.nf:98:66`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
  csv_unmmaped_channel = PYOPENMS_GENERATESEARCHPARAMS.out.csv.map{it[1]}.flatten().map{file -> [[id:file.baseName],file]}
                                                                   ^^
  ```

- Warning: `subworkflows/local/identification.nf:99:62`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
  ms_mmaped_channel = PYOPENMS_GENERATESEARCHPARAMS.out.ms.map{it[1]}.flatten().map{file -> [[id:file.baseName],file]}
                                                               ^^
  ```

- Warning: `subworkflows/local/identification.nf:100:64`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
  mgf_mmaped_channel = PYOPENMS_GENERATESEARCHPARAMS.out.mgf.map{it[1]}.flatten().map{file -> [[id:file.baseName],file]}
                                                                 ^^
  ```

- Warning: `subworkflows/local/identification.nf:106:59`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
  generated_params = OPENMS_FILEFILTER.out.consensusxml.map{it[0]}.combine(
                                                            ^^
  ```

- Warning: `subworkflows/local/identification.nf:107:47`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
  PYOPENMS_GENERATESEARCHPARAMS.out.csv.collect{it[1]}
                                                ^^
  ```

- Warning: `subworkflows/local/identification.nf:123:17`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
  }.toList()).map{it[1]}.flatten().
                  ^^
  ```

- Warning: `subworkflows/local/identification.nf:137:40`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
  OPENMS_FILEFILTER.out.consensusxml.map{it[0]}.combine(
                                         ^^
  ```

- Warning: `subworkflows/local/identification.nf:138:46`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
  PYOPENMS_GENERATESEARCHPARAMS.out.ms.collect{it[1]}
                                               ^^
  ```

- Warning: `subworkflows/local/identification.nf:154:17`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
  }.toList()).map{it[1]}.flatten().
                  ^^
  ```

- Warning: `subworkflows/local/identification.nf:165:40`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
  OPENMS_FILEFILTER.out.consensusxml.map{it[0]}.combine(
                                         ^^
  ```

- Warning: `subworkflows/local/identification.nf:166:47`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
  PYOPENMS_GENERATESEARCHPARAMS.out.mgf.collect{it[1]}
                                                ^^
  ```

- Warning: `subworkflows/local/identification.nf:182:17`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
  }.toList()).map{it[1]}.flatten().
                  ^^
  ```

- Warning: `subworkflows/local/identification.nf:198:26`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
  mzml_files.filter{ meta, file -> meta.level == "MS2" || meta.level == "MS12" }
                           ^^^^
  ```

- Warning: `subworkflows/local/identification.nf:201:7`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
  ).map{it[1,2,3]} | PYOPENMS_GENERATESEARCHPARAMSUNMAPPED
        ^^
  ```

- Warning: `subworkflows/local/identification.nf:210:17`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
  output_sirius = Channel.empty()
                  ^^^^^^^
  ```

- Warning: `subworkflows/local/identification.nf:211:19`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
  output_fingerid = Channel.empty()
                    ^^^^^^^
  ```

- Warning: `subworkflows/local/identification.nf:226:12`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
  ms2query = Channel.empty()
             ^^^^^^^
  ```

- Warning: `subworkflows/local/linker.nf:19:23`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
          ch_versions = Channel.empty()
                        ^^^^^^^
  ```

- Warning: `subworkflows/local/linker.nf:25:36`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
      quantification_information.map{it[0,1]} | PYOPENMS_EXTRACTFEATUREMZ
                                     ^^
  ```

- Warning: `subworkflows/local/linker.nf:31:21`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
  PYOPENMS_CONCTSV_MZ(Channel.of([id:"merged_mz_range"]).combine(PYOPENMS_EXTRACTFEATUREMZ.out.tsv.collect{it[1]}.toList()),"tsv","tsv")
                      ^^^^^^^
  ```

- Warning: `subworkflows/local/linker.nf:31:106`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
  PYOPENMS_CONCTSV_MZ(Channel.of([id:"merged_mz_range"]).combine(PYOPENMS_EXTRACTFEATUREMZ.out.tsv.collect{it[1]}.toList()),"tsv","tsv")
                                                                                                           ^^
  ```

- Warning: `subworkflows/local/linker.nf:38:57`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
  PYOPENMS_SPLITFEATUREXML(quantification_information.map{it[0,1]},
                                                          ^^
  ```

- Warning: `subworkflows/local/linker.nf:39:45`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
      PYOPENMS_CALCULATEBOUNDRIES.out.tsv.map{it[1]}
                                              ^^
  ```

- Warning: `subworkflows/local/linker.nf:45:49`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
  PYOPENMS_SPLITFEATUREXML.out.featurexml.collect{it[1]}.flatten().map{file ->
                                                  ^^
  ```

- Warning: `subworkflows/local/linker.nf:55:16`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
  to_be_merged = Channel.of([id:"Linked_data"]).combine(
                 ^^^^^^^
  ```

- Warning: `subworkflows/local/linker.nf:56:59`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
  OPENMS_FEATURELINKERUNLABELEDKDPARTS.out.consensusxml.map{it[1]}.collect()
                                                            ^^
  ```

- Warning: `subworkflows/local/linker.nf:77:58`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
  consensusxml=   PYOPENMS_FILEMERGER.out.consensusxml.map{meta,consensusxml->[[id:consensusxml.baseName],consensusxml]}
                                                           ^^^^
  ```

- Warning: `subworkflows/local/linker.nf:81:1`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
  Channel.of([id:"Linked_data"]).combine(quantification_information.collect{it[1]}.map { files ->
  ^^^^^^^
  ```

- Warning: `subworkflows/local/linker.nf:81:75`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
  Channel.of([id:"Linked_data"]).combine(quantification_information.collect{it[1]}.map { files ->
                                                                            ^^
  ```

- Warning: `subworkflows/local/linker.nf:88:75`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          consensusxml=OPENMS_FEATURELINKERUNLABELEDKD.out.consensusxml.map{meta,consensusxml->[[id:consensusxml.baseName],consensusxml]}
                                                                            ^^^^
  ```

- Warning: `subworkflows/local/ms2query.nf:26:15`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
  ch_versions = Channel.empty()
                ^^^^^^^
  ```

- Warning: `subworkflows/local/ms2query.nf:40:1`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
  Channel
  ^^^^^^^
  ```

- Warning: `subworkflows/local/ms2query.nf:65:85`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
  mgf_channel = PYOPENMS_SPLITMGF.out.mgf.flatMap{id, values -> values.collect { [id, it]}}
                                                                                      ^^
  ```

- Warning: `subworkflows/local/ms2query.nf:73:5`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      Channel
      ^^^^^^^
  ```

- Warning: `subworkflows/local/ms2query_modeldownloader.nf:8:19`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_versions = Channel.empty()
                    ^^^^^^^
  ```

- Warning: `subworkflows/local/ms2query_modeldownloader.nf:12:5`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      Channel
      ^^^^^^^
  ```

- Warning: `subworkflows/local/ms2query_modeldownloader.nf:18:5`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      Channel
      ^^^^^^^
  ```

- Warning: `subworkflows/local/quantification.nf:17:19`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_versions = Channel.empty()
                    ^^^^^^^
  ```

- Warning: `subworkflows/local/quantification.nf:28:24`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
      mzml_files.collect{it[0]}.toList().combine(mzml_files.collect{it[1]}.toList()) | OPENMS_MAPALIGNERPOSECLUSTERINGMZML
                         ^^
  ```

- Warning: `subworkflows/local/quantification.nf:28:67`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
      mzml_files.collect{it[0]}.toList().combine(mzml_files.collect{it[1]}.toList()) | OPENMS_MAPALIGNERPOSECLUSTERINGMZML
                                                                    ^^
  ```

- Warning: `subworkflows/local/quantification.nf:33:85`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
      [[map_id:idd],meta,mzml]}.join(OPENMS_MAPALIGNERPOSECLUSTERINGMZML.out.mzml.map{it[1]}.flatten().map{mzml ->
                                                                                      ^^
  ```

- Warning: `subworkflows/local/quantification.nf:35:32`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
      [[map_id:idd], mzml]}).map{it[1,3]}
                                 ^^
  ```

- Warning: `subworkflows/local/quantification.nf:44:44`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
  quantificaiton_data=mzml_files.filter{meta,file->meta.level == "MS1" | meta.level == "MS12"}
                                             ^^^^
  ```

- Warning: `subworkflows/local/quantification.nf:53:33`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
      quantified_features.collect{it[0]}.toList().combine(quantified_features.collect{it[1]}.toList()) | OPENMS_MAPALIGNERPOSECLUSTERING
                                  ^^
  ```

- Warning: `subworkflows/local/quantification.nf:53:85`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
      quantified_features.collect{it[0]}.toList().combine(quantified_features.collect{it[1]}.toList()) | OPENMS_MAPALIGNERPOSECLUSTERING
                                                                                      ^^
  ```

- Warning: `subworkflows/local/quantification.nf:59:62`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
      .join(OPENMS_MAPALIGNERPOSECLUSTERING.out.featurexml.map{it[1]}.flatten().map{featurexml ->
                                                               ^^
  ```

- Warning: `subworkflows/local/quantification.nf:61:60`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
      .join(OPENMS_MAPALIGNERPOSECLUSTERING.out.trafoxml.map{it[1]}.flatten().map{trafoxml ->
                                                             ^^
  ```

- Warning: `subworkflows/local/quantification.nf:63:35`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
      .join(quantificaiton_data.map{meta,mzml->
                                    ^^^^
  ```

- Warning: `subworkflows/local/quantification.nf:64:34`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
  tuple(mzml.baseName, mzml)}).map{it[1..4]}
                                   ^^
  ```

- Warning: `subworkflows/local/quantification.nf:67:23`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
      combined_data.map{it[0,2,3]} | OPENMS_MAPRTTRANSFORMER
                        ^^
  ```

- Warning: `subworkflows/local/quantification.nf:72:43`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
      quantified_features=combined_data.map{it[0,1]}
                                            ^^
  ```

- Warning: `subworkflows/local/requantification.nf:14:19`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_versions = Channel.empty()
                    ^^^^^^^
  ```

- Warning: `subworkflows/local/requantification.nf:20:44`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
  quantified_features.combine(data_split.map{it[1]}) |  PYOPENMS_RELOADMAPS
                                             ^^
  ```

- Warning: `subworkflows/local/requantification.nf:26:16`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
  data_split.map{it[0,2]} | PYOPENMS_LIBBUILDER
                 ^^
  ```

- Warning: `subworkflows/local/requantification.nf:30:61`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
  quantificaiton_data.combine(PYOPENMS_LIBBUILDER.out.tsv.map{it[1]}) | OPENMS_FEATUREFINDERMETABOIDENT
                                                              ^^
  ```

- Warning: `subworkflows/local/sirius.nf:19:15`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
  ch_versions = Channel.empty()
                ^^^^^^^
  ```

- Warning: `subworkflows/local/sirius.nf:28:82`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
  ms_channel = PYOPENMS_SPLITMS.out.ms.flatMap{id, values -> values.collect { [id, it]}}
                                                                                   ^^
  ```

- Warning: `workflows/metaboigniter.nf:49:19`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_versions = Channel.empty()
                    ^^^^^^^
  ```

- Warning: `workflows/metaboigniter.nf:50:24`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_multiqc_files = Channel.empty()
                         ^^^^^^^
  ```

- Warning: `workflows/metaboigniter.nf:54:14`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      empty_id=Channel.fromPath("$projectDir/assets/emptyfile.idXML")
               ^^^^^^^
  ```

- Warning: `workflows/metaboigniter.nf:72:62`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
          ANNOTATION(quantification_information,empty_id,false,Channel.empty(),params.skip_adduct_detection,!params.identification)
                                                               ^^^^^^^
  ```

- Warning: `workflows/metaboigniter.nf:108:9`: Variable was declared but not used

  ```nextflow
          consensusxml_data_tsv = PYOPENMS_EXPORTQUANTIFICATION.out.tsv
          ^^^^^^^^^^^^^^^^^^^^^
  ```

- Warning: `workflows/metaboigniter.nf:154:32`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_multiqc_config        = Channel.fromPath(
                                 ^^^^^^^
  ```

- Warning: `workflows/metaboigniter.nf:157:9`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
          Channel.fromPath(params.multiqc_config, checkIfExists: true) :
          ^^^^^^^
  ```

- Warning: `workflows/metaboigniter.nf:158:9`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
          Channel.empty()
          ^^^^^^^
  ```

- Warning: `workflows/metaboigniter.nf:160:9`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
          Channel.fromPath(params.multiqc_logo, checkIfExists: true) :
          ^^^^^^^
  ```

- Warning: `workflows/metaboigniter.nf:161:9`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
          Channel.empty()
          ^^^^^^^
  ```

- Warning: `workflows/metaboigniter.nf:165:27`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_workflow_summary = Channel.value(paramsSummaryMultiqc(summary_params))
                            ^^^^^^^
  ```

- Warning: `workflows/metaboigniter.nf:170:45`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_methods_description                = Channel.value(
                                              ^^^^^^^
  ```
