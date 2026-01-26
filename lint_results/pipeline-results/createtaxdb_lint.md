# Nextflow lint results

- Generated: 2026-01-26T00:16:57.714905848Z
- Nextflow version: 25.12.0-edge
- Summary: 33 warnings

## :warning: Warnings

- Warning: `modules/nf-core/ganon/buildcustom/main.nf:46:9`: Variable was declared but not used

  ```nextflow
      def args = task.ext.args ?: ''
          ^^^^
  ```

- Warning: `modules/nf-core/ganon/buildcustom/main.nf:48:9`: Variable was declared but not used

  ```nextflow
      def taxonomy_args = taxonomy_files ? "--taxonomy-files ${taxonomy_files}" : ""
          ^^^^^^^^^^^^^
  ```

- Warning: `modules/nf-core/ganon/buildcustom/main.nf:49:9`: Variable was declared but not used

  ```nextflow
      def genome_size_args = genome_size_files ? "--genome-size-files ${genome_size_files}" : ""
          ^^^^^^^^^^^^^^^^
  ```

- Warning: `modules/nf-core/kaiju/mkfmi/main.nf:44:9`: Variable was declared but not used

  ```nextflow
      def args = task.ext.args ?: ''
          ^^^^
  ```

- Warning: `modules/nf-core/kmcp/compute/main.nf:40:9`: Variable was declared but not used

  ```nextflow
      def args = task.ext.args ?: ''
          ^^^^
  ```

- Warning: `modules/nf-core/kmcp/index/main.nf:39:9`: Variable was declared but not used

  ```nextflow
      def args = task.ext.args ?: ''
          ^^^^
  ```

- Warning: `modules/nf-core/malt/build/main.nf:44:9`: Variable was declared but not used

  ```nextflow
      def args = task.ext.args ?: ''
          ^^^^
  ```

- Warning: `modules/nf-core/pigz/compress/main.nf:35:9`: Variable was declared but not used

  ```nextflow
      def args = task.ext.args ?: ''
          ^^^^
  ```

- Warning: `modules/nf-core/unzip/main.nf:38:9`: Variable was declared but not used

  ```nextflow
      def args = task.ext.args ?: ''
          ^^^^
  ```

- Warning: `subworkflows/local/kmcp_create/main.nf:11:19`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_versions = Channel.empty()
                    ^^^^^^^
  ```

- Warning: `subworkflows/local/preprocessing/main.nf:15:19`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_versions = Channel.empty()
                    ^^^^^^^
  ```

- Warning: `subworkflows/local/preprocessing/main.nf:16:24`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_multiqc_files = Channel.empty()
                         ^^^^^^^
  ```

- Warning: `subworkflows/local/preprocessing/main.nf:19:28`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_singleref_for_dna = Channel.empty()
                             ^^^^^^^
  ```

- Warning: `subworkflows/local/preprocessing/main.nf:20:27`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_singleref_for_aa = Channel.empty()
                            ^^^^^^^
  ```

- Warning: `subworkflows/local/preprocessing/main.nf:21:29`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_prepped_dna_fastas = Channel.empty()
                              ^^^^^^^
  ```

- Warning: `subworkflows/local/preprocessing/main.nf:22:28`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_prepped_aa_fastas = Channel.empty()
                             ^^^^^^^
  ```

- Warning: `subworkflows/local/preprocessing/main.nf:23:39`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_prepped_dna_fastas_ungrouped = Channel.empty()
                                        ^^^^^^^
  ```

- Warning: `subworkflows/local/preprocessing/main.nf:24:38`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_prepped_aa_fastas_ungrouped = Channel.empty()
                                       ^^^^^^^
  ```

- Warning: `subworkflows/local/preprocessing/main.nf:25:34`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_prepped_aa_fastas_kaiju = Channel.empty()
                                   ^^^^^^^
  ```

- Warning: `subworkflows/local/utils_nfcore_createtaxdb_pipeline/main.nf:31:5`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
      monochrome_logs // boolean: Do not use coloured log outputs
      ^^^^^^^^^^^^^^^
  ```

- Warning: `subworkflows/local/utils_nfcore_createtaxdb_pipeline/main.nf:34:5`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
      input //  string: Path to input samplesheet
      ^^^^^
  ```

- Warning: `subworkflows/local/utils_nfcore_createtaxdb_pipeline/main.nf:106:22`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_samplesheet = Channel.fromList(samplesheetToList(params.input, "assets/schema_input.json"))
                       ^^^^^^^
  ```

- Warning: `subworkflows/local/utils_nfcore_createtaxdb_pipeline/main.nf:118:58`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
                  def not_unique_dna = fasta_dna.countBy { it }.grep { it.value > 1 }.collect { it.key }
                                                           ^^
  ```

- Warning: `subworkflows/local/utils_nfcore_createtaxdb_pipeline/main.nf:118:70`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
                  def not_unique_dna = fasta_dna.countBy { it }.grep { it.value > 1 }.collect { it.key }
                                                                       ^^
  ```

- Warning: `subworkflows/local/utils_nfcore_createtaxdb_pipeline/main.nf:118:95`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
                  def not_unique_dna = fasta_dna.countBy { it }.grep { it.value > 1 }.collect { it.key }
                                                                                                ^^
  ```

- Warning: `subworkflows/local/utils_nfcore_createtaxdb_pipeline/main.nf:133:56`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
                  def not_unique_aa = fasta_aa.countBy { it }.grep { it.value > 1 }.collect { it.key }
                                                         ^^
  ```

- Warning: `subworkflows/local/utils_nfcore_createtaxdb_pipeline/main.nf:133:68`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
                  def not_unique_aa = fasta_aa.countBy { it }.grep { it.value > 1 }.collect { it.key }
                                                                     ^^
  ```

- Warning: `subworkflows/local/utils_nfcore_createtaxdb_pipeline/main.nf:133:93`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
                  def not_unique_aa = fasta_aa.countBy { it }.grep { it.value > 1 }.collect { it.key }
                                                                                              ^^
  ```

- Warning: `workflows/createtaxdb.nf:124:20`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
              .map { it.join("\t") }
                     ^^
  ```

- Warning: `workflows/createtaxdb.nf:130:39`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
                  [[id: params.dbname], it]
                                        ^^
  ```

- Warning: `workflows/createtaxdb.nf:171:41`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
          ch_taxdmpfiles_for_krakenuniq = Channel
                                          ^^^^^^^
  ```

- Warning: `workflows/createtaxdb.nf:174:21`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
              .map { [it] }
                      ^^
  ```

- Warning: `workflows/createtaxdb.nf:312:26`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      def topic_versions = Channel
                           ^^^^^^^
  ```
