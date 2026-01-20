# Nextflow lint results

- Generated: 2026-01-20T00:18:22.623390680Z
- Nextflow version: 25.12.0-edge
- Summary: 2 errors, 24 warnings

## :x: Errors

- Error: `conf/modules.config:130:22`: `publishDir` is not defined

  ```nextflow
          publishDir = publishDir + [
                       ^^^^^^^^^^
  ```

- Error: `modules/local/multiqc_assemblyscan_plot_data/main.nf:65:40`: `meta` is not defined

  ```nextflow
      def prefix = task.ext.prefix ?: "${meta.id}"
                                         ^^^^
  ```

## :warning: Warnings

- Warning: `modules/local/multiqc_assemblyscan_plot_data/main.nf:64:9`: Variable was declared but not used

  ```nextflow
      def args = task.ext.args ?: ''
          ^^^^
  ```

- Warning: `modules/local/multiqc_assemblyscan_plot_data/main.nf:65:9`: Variable was declared but not used

  ```nextflow
      def prefix = task.ext.prefix ?: "${meta.id}"
          ^^^^^^
  ```

- Warning: `modules/nf-core/last/dotplot/main.nf:51:9`: Variable was declared but not used

  ```nextflow
      def args = task.ext.args ?: ''
          ^^^^
  ```

- Warning: `modules/nf-core/last/lastal/main.nf:67:9`: Variable was declared but not used

  ```nextflow
      def args = task.ext.args ?: ''
          ^^^^
  ```

- Warning: `modules/nf-core/last/lastal/main.nf:69:9`: Variable was declared but not used

  ```nextflow
      def trained_params = param_file ? "-p ${param_file}"  : ''
          ^^^^^^^^^^^^^^
  ```

- Warning: `modules/nf-core/last/lastdb/main.nf:38:9`: Variable was declared but not used

  ```nextflow
      def args = task.ext.args ?: ''
          ^^^^
  ```

- Warning: `modules/nf-core/last/mafconvert/main.nf:82:9`: Variable was declared but not used

  ```nextflow
      def args = task.ext.args ?: ''
          ^^^^
  ```

- Warning: `modules/nf-core/last/split/main.nf:61:9`: Variable was declared but not used

  ```nextflow
      def args = task.ext.args ?: ''
          ^^^^
  ```

- Warning: `modules/nf-core/last/train/main.nf:52:9`: Variable was declared but not used

  ```nextflow
      def args = task.ext.args ?: ''
          ^^^^
  ```

- Warning: `subworkflows/local/fasta_bgzip_index_dict_samtools/main.nf:12:19`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_versions = Channel.empty()
                    ^^^^^^^
  ```

- Warning: `subworkflows/local/pairalign_m2m/main.nf:38:19`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_versions = Channel.empty()
                    ^^^^^^^
  ```

- Warning: `subworkflows/local/pairalign_m2m/main.nf:59:77`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          training_results_for_multiqc = ALIGNMENT_TRAIN.out.multiqc.collect{ it[1] }
                                                                              ^^
  ```

- Warning: `subworkflows/local/pairalign_m2m/main.nf:168:15`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      multiqc = Channel.empty()
                ^^^^^^^
  ```

- Warning: `subworkflows/local/pairalign_m2m/main.nf:170:55`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          .mix(ALIGNMENT_SPLIT_O2O.out.multiqc.collect{ it[1]} )
                                                        ^^
  ```

- Warning: `subworkflows/local/pairalign_m2o/main.nf:32:19`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_versions = Channel.empty()
                    ^^^^^^^
  ```

- Warning: `subworkflows/local/pairalign_m2o/main.nf:53:77`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          training_results_for_multiqc = ALIGNMENT_TRAIN.out.multiqc.collect{ it[1] }
                                                                              ^^
  ```

- Warning: `subworkflows/local/pairalign_m2o/main.nf:115:15`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      multiqc = Channel.empty()
                ^^^^^^^
  ```

- Warning: `subworkflows/local/pairalign_m2o/main.nf:117:55`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          .mix(ALIGNMENT_SPLIT_O2O.out.multiqc.collect{ it[1]} )
                                                        ^^
  ```

- Warning: `subworkflows/local/utils_nfcore_pairgenomealign_pipeline/main.nf:32:5`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
      monochrome_logs   // boolean: Do not use coloured log outputs
      ^^^^^^^^^^^^^^^
  ```

- Warning: `subworkflows/local/utils_nfcore_pairgenomealign_pipeline/main.nf:35:5`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
      input             //  string: Path to input samplesheet
      ^^^^^
  ```

- Warning: `workflows/pairgenomealign.nf:41:31`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          ch_targetgenome.map { meta, file -> [ [id:'targetGenome'] , file ] }
                                ^^^^
  ```

- Warning: `workflows/pairgenomealign.nf:54:55`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
            .map { sorted_list -> sorted_list.collect { it[1] } }
                                                        ^^
  ```

- Warning: `workflows/pairgenomealign.nf:109:39`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
              pairalign_out.o2o.combine(Channel.fromList(export_formats)),
                                        ^^^^^^^
  ```

- Warning: `workflows/pairgenomealign.nf:123:26`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      def topic_versions = Channel.topic("versions")
                           ^^^^^^^
  ```
