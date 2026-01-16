# Nextflow lint results

- Generated: 2026-01-16T10:19:14.049777445Z
- Nextflow version: 25.12.0-edge
- Summary: 10 errors, 49 warnings

## :x: Errors

- Error: `conf/modules.config:100:9`: If statements cannot be mixed with config statements

  ```nextflow
          if (params.container_dev) {
          ^
  ```

- Error: `conf/modules.config:111:9`: If statements cannot be mixed with config statements

  ```nextflow
          if (params.container_dev) {
          ^
  ```

- Error: `conf/modules.config:125:9`: If statements cannot be mixed with config statements

  ```nextflow
          if (params.container_dev) {
          ^
  ```

- Error: `conf/modules.config:136:9`: If statements cannot be mixed with config statements

  ```nextflow
          if (params.container_dev) {
          ^
  ```

- Error: `conf/modules.config:152:9`: If statements cannot be mixed with config statements

  ```nextflow
          if (params.container_dev) {
          ^
  ```

- Error: `conf/modules.config:160:9`: If statements cannot be mixed with config statements

  ```nextflow
          if (params.container_dev) {
          ^
  ```

- Error: `conf/modules.config:167:9`: If statements cannot be mixed with config statements

  ```nextflow
          if (params.container_dev) {
          ^
  ```

- Error: `modules/local/bedtools/random/main.nf:15:27`: Unexpected input: '"\*.bed"'

  ```nextflow
      tuple val(meta), path "*.bed", emit: bed
                            ^
  ```

- Error: `modules/local/stimulus/check_model/main.nf:3:12`: `meta` is not defined

  ```nextflow
      tag "${meta.id}"
             ^^^^
  ```

- Error: `nextflow.config:214:5`: Unexpected input: 'includeConfig'

  ```nextflow
      includeConfig 'conf/igenomes.config'
      ^
  ```

## :warning: Warnings

- Warning: `modules/local/stimulus/tune/main.nf:22:9`: Variable was declared but not used

  ```nextflow
      def use_initial_weights = initial_weights != [] ? "-w ${initial_weights}" : ""
          ^^^^^^^^^^^^^^^^^^^
  ```

- Warning: `modules/nf-core/custom/getchromsizes/main.nf:23:9`: Variable was declared but not used

  ```nextflow
      def args = task.ext.args ?: ''
          ^^^^
  ```

- Warning: `modules/nf-core/gawk/main.nf:25:51`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
      suffix = task.ext.suffix ?: "${input.collect{ it.getExtension()}.get(0)}" // use the first extension of the input files
                                                    ^^
  ```

- Warning: `modules/nf-core/gawk/main.nf:28:32`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
      lst_gz    = input.collect{ it.getExtension().endsWith("gz") }
                                 ^^
  ```

- Warning: `modules/nf-core/gawk/main.nf:34:16`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          assert it.name != "${prefix}.${suffix}" : "Input and output names are the same, set prefix in module configuration to disambiguate!"
                 ^^
  ```

- Warning: `subworkflows/local/check_model/main.nf:26:5`: Variable was declared but not used

  ```nextflow
      ch_versions = Channel.empty()
      ^^^^^^^^^^^
  ```

- Warning: `subworkflows/local/check_model/main.nf:26:19`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_versions = Channel.empty()
                    ^^^^^^^
  ```

- Warning: `subworkflows/local/evaluation/main.nf:25:19`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_versions = Channel.empty()
                    ^^^^^^^
  ```

- Warning: `subworkflows/local/evaluation/main.nf:75:20`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          .flatMap { it }
                     ^^
  ```

- Warning: `subworkflows/local/evaluation/main.nf:85:9`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          meta, csv -> csv
          ^^^^
  ```

- Warning: `subworkflows/local/preprocess_ibis_bedfile_to_stimulus/main.nf:51:19`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_versions = Channel.empty()
                    ^^^^^^^
  ```

- Warning: `subworkflows/local/preprocess_ibis_bedfile_to_stimulus/main.nf:61:38`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          .combine(ch_genome_sizes.map{it[1]})
                                       ^^
  ```

- Warning: `subworkflows/local/preprocess_ibis_bedfile_to_stimulus/main.nf:65:22`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_awk_program = Channel.fromPath('./bin/center_around_peak.sh')
                       ^^^^^^^
  ```

- Warning: `subworkflows/local/preprocess_ibis_bedfile_to_stimulus/main.nf:102:19`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          .filter { it.background_type == 'aliens' }
                    ^^
  ```

- Warning: `subworkflows/local/preprocess_ibis_bedfile_to_stimulus/main.nf:126:20`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
              shade: it[0].background_type == 'shade'
                     ^^
  ```

- Warning: `subworkflows/local/preprocess_ibis_bedfile_to_stimulus/main.nf:127:22`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
              shuffle: it[0].background_type == 'shuffle'
                       ^^
  ```

- Warning: `subworkflows/local/preprocess_ibis_bedfile_to_stimulus/main.nf:185:23`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          ch_genome.map{it[1]}.collect()
                        ^^
  ```

- Warning: `subworkflows/local/preprocess_ibis_bedfile_to_stimulus/main.nf:191:23`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          ch_genome.map{it[1]}.collect()
                        ^^
  ```

- Warning: `subworkflows/local/preprocess_ibis_bedfile_to_stimulus/main.nf:210:22`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_awk_program = Channel.fromPath('./bin/background_foreground_to_stimulus_csv.sh')
                       ^^^^^^^
  ```

- Warning: `subworkflows/local/split_csv/main.nf:23:19`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_versions = Channel.empty()
                    ^^^^^^^
  ```

- Warning: `subworkflows/local/split_data_config_unified/main.nf:21:19`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_versions = Channel.empty()
                    ^^^^^^^
  ```

- Warning: `subworkflows/local/transform_csv/main.nf:25:19`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_versions = Channel.empty()
                    ^^^^^^^
  ```

- Warning: `subworkflows/local/tune/main.nf:28:19`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_versions = Channel.empty()
                    ^^^^^^^
  ```

- Warning: `subworkflows/local/tune/main.nf:56:31`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          .combine(ch_model.map{it[1]})
                                ^^
  ```

- Warning: `subworkflows/local/tune/main.nf:60:73`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          .multiMap { meta, data, model, meta_model_config, model_config, meta_weights, initial_weights, n_replicate ->
                                                                          ^^^^^^^^^^^^
  ```

- Warning: `subworkflows/local/utils_nfcore_deepmodeloptim_pipeline/main.nf:31:5`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
      monochrome_logs   // boolean: Do not use coloured log outputs
      ^^^^^^^^^^^^^^^
  ```

- Warning: `subworkflows/local/utils_nfcore_deepmodeloptim_pipeline/main.nf:39:5`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
      preprocessing_config
      ^^^^^^^^^^^^^^^^^^^^
  ```

- Warning: `subworkflows/local/utils_nfcore_deepmodeloptim_pipeline/main.nf:43:19`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_versions = Channel.empty()
                    ^^^^^^^
  ```

- Warning: `subworkflows/local/utils_nfcore_deepmodeloptim_pipeline/main.nf:74:26`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_data            = Channel.fromPath(data, checkIfExists: true).map { it -> [[id:it.baseName], it]}
                           ^^^^^^^
  ```

- Warning: `subworkflows/local/utils_nfcore_deepmodeloptim_pipeline/main.nf:75:26`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_data_config     = Channel.fromPath(data_config, checkIfExists: true).map { it -> [[id:it.baseName], it]}
                           ^^^^^^^
  ```

- Warning: `subworkflows/local/utils_nfcore_deepmodeloptim_pipeline/main.nf:76:26`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_model           = Channel.fromPath(model, checkIfExists: true).map { it -> [[id:it.baseName], it]}
                           ^^^^^^^
  ```

- Warning: `subworkflows/local/utils_nfcore_deepmodeloptim_pipeline/main.nf:77:26`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_model_config    = Channel.fromPath(model_config, checkIfExists: true).map { it -> [[id:it.baseName], it]}
                           ^^^^^^^
  ```

- Warning: `subworkflows/local/utils_nfcore_deepmodeloptim_pipeline/main.nf:83:9`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
          Channel.of([[],[]]) :
          ^^^^^^^
  ```

- Warning: `subworkflows/local/utils_nfcore_deepmodeloptim_pipeline/main.nf:84:9`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
          Channel.fromPath(initial_weights, checkIfExists: true)
          ^^^^^^^
  ```

- Warning: `subworkflows/local/utils_nfcore_deepmodeloptim_pipeline/main.nf:92:9`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
          Channel.empty() :
          ^^^^^^^
  ```

- Warning: `subworkflows/local/utils_nfcore_deepmodeloptim_pipeline/main.nf:93:9`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
          Channel.fromList(samplesheetToList(params.preprocessing_config, "assets/schema_preprocessing.json")).map{it[0]}
          ^^^^^^^
  ```

- Warning: `subworkflows/local/utils_nfcore_deepmodeloptim_pipeline/main.nf:93:114`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          Channel.fromList(samplesheetToList(params.preprocessing_config, "assets/schema_preprocessing.json")).map{it[0]}
                                                                                                                   ^^
  ```

- Warning: `subworkflows/local/utils_nfcore_deepmodeloptim_pipeline/main.nf:99:9`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
          Channel.of([[],[]]) :
          ^^^^^^^
  ```

- Warning: `subworkflows/local/utils_nfcore_deepmodeloptim_pipeline/main.nf:102:13`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
              Channel.fromPath(params.genomes[params.genome]['fasta'], checkIfExists: true) :
              ^^^^^^^
  ```

- Warning: `subworkflows/local/utils_nfcore_deepmodeloptim_pipeline/main.nf:103:13`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
              Channel.fromPath(params.genome, checkIfExists: true)
              ^^^^^^^
  ```

- Warning: `subworkflows/local/utils_nfcore_deepmodeloptim_pipeline/main.nf:114:33`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
          val_tune_trials_range = Channel.from(range)
                                  ^^^^^^^
  ```

- Warning: `subworkflows/local/utils_nfcore_deepmodeloptim_pipeline/main.nf:126:26`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_tune_replicates = Channel.from(1..params.tune_replicates)
                           ^^^^^^^
  ```

- Warning: `subworkflows/local/utils_nfcore_deepmodeloptim_pipeline/main.nf:132:13`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
              Channel.empty() :
              ^^^^^^^
  ```

- Warning: `subworkflows/local/utils_nfcore_deepmodeloptim_pipeline/main.nf:133:13`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
              Channel.fromPath(params.prediction_data, checkIfExists: true)
              ^^^^^^^
  ```

- Warning: `subworkflows/nf-core/utils_nfcore_pipeline/main.nf:101:98`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      return ch_versions.unique().map { version -> processVersionsFromYAML(version) }.unique().mix(Channel.of(workflowVersionToYAML()))
                                                                                                   ^^^^^^^
  ```

- Warning: `workflows/deepmodeloptim.nf:48:19`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_versions = Channel.empty()
                    ^^^^^^^
  ```

- Warning: `workflows/deepmodeloptim.nf:65:44`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
              ch_preprocessing_config.filter{it.protocol == 'ibis'},
                                             ^^
  ```

- Warning: `workflows/deepmodeloptim.nf:127:17`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          .filter{it}   // remove the empty element from the check model
                  ^^
  ```

- Warning: `workflows/deepmodeloptim.nf:160:17`: Variable was declared but not used

  ```nextflow
          ).set { ch_collated_versions }
                  ^^^^^^^^^^^^^^^^^^^^
  ```
