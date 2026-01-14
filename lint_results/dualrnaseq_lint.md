# Nextflow lint results

- Generated: 2026-01-14T09:17:15.899842013Z
- Nextflow version: 25.12.0-edge
- Summary: 2 errors, 48 warnings

## :x: Errors

- Error: `conf/modules.config:83:17`: Unexpected input: ':'

  ```nextflow
          withName: 'NFCORE_DUALRNASEQ:DUALRNASEQ:SALMON_SELECTIVE_ALIGNMENT:SALMON_INDEX' {
                  ^
  ```

- Error: `nextflow.config:462:14`: Unexpected input: '('

  ```nextflow
  def check_max(obj, type) {
               ^
  ```

## :warning: Warnings

- Warning: `modules/local/combine_files/main.nf:14:9`: Variable was declared but not used

  ```nextflow
      def args = task.ext.args ?: ''
          ^^^^
  ```

- Warning: `modules/local/combine_quantification_results_salmon/main.nf:15:9`: Variable was declared but not used

  ```nextflow
      def args = task.ext.args ?: ''
          ^^^^
  ```

- Warning: `modules/local/salmon_split_table/main.nf:18:9`: Variable was declared but not used

  ```nextflow
      def args = task.ext.args ?: ''
          ^^^^
  ```

- Warning: `modules/local/tximport/main.nf:21:9`: Variable was declared but not used

  ```nextflow
      def args = task.ext.args ?: ''
          ^^^^
  ```

- Warning: `modules/local/tximport/main.nf:22:5`: Variable was declared but not used

  ```nextflow
      prefix = task.ext.prefix ?: "${meta.id}"
      ^^^^^^
  ```

- Warning: `modules/nf-core/custom/dumpsoftwareversions/main.nf:22:9`: Variable was declared but not used

  ```nextflow
      def args = task.ext.args ?: ''
          ^^^^
  ```

- Warning: `subworkflows/local/prepare_pathogen_transcriptome/main.nf:12:18`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      parameters = Channel.value(
                   ^^^^^^^
  ```

- Warning: `subworkflows/local/prepare_reference_files/main.nf:58:43`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_combined_pathogen_host_gff_htseq = Channel.empty()
                                            ^^^^^^^
  ```

- Warning: `subworkflows/local/prepare_reference_files/main.nf:59:43`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_extracted_annotations_host_htseq = Channel.empty()
                                            ^^^^^^^
  ```

- Warning: `subworkflows/local/prepare_reference_files/main.nf:60:45`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_extract_annotations_pathogen_htseq = Channel.empty()
                                              ^^^^^^^
  ```

- Warning: `subworkflows/local/prepare_reference_files/main.nf:61:37`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_combined_fasta_transcripts = Channel.empty()
                                      ^^^^^^^
  ```

- Warning: `subworkflows/local/prepare_reference_files/main.nf:62:42`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_host_fasta_transcripts_unzipped = Channel.empty()
                                           ^^^^^^^
  ```

- Warning: `subworkflows/local/prepare_reference_files/main.nf:63:46`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_pathogen_fasta_transcripts_unzipped = Channel.empty()
                                               ^^^^^^^
  ```

- Warning: `subworkflows/local/prepare_reference_files/main.nf:77:32`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_gene_feature_pathogen = Channel.value(pathogenFeaturesList)
                                 ^^^^^^^
  ```

- Warning: `subworkflows/local/prepare_reference_files/main.nf:83:28`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_gene_feature_host = Channel.value(hostFeaturesList)
                             ^^^^^^^
  ```

- Warning: `subworkflows/local/prepare_reference_files/main.nf:93:28`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_host_fasta_genome = Channel.value(file(host_fasta_genome, checkIfExists: true))
                             ^^^^^^^
  ```

- Warning: `subworkflows/local/prepare_reference_files/main.nf:94:19`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_host_gff = Channel.value(file(host_gff, checkIfExists: true))
                    ^^^^^^^
  ```

- Warning: `subworkflows/local/prepare_reference_files/main.nf:95:23`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_pathogen_gff = Channel.value(file(pathogen_gff, checkIfExists: true))
                        ^^^^^^^
  ```

- Warning: `subworkflows/local/prepare_reference_files/main.nf:96:32`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_pathogen_fasta_genome = Channel.value(file(pathogen_fasta_genome, checkIfExists: true))
                                 ^^^^^^^
  ```

- Warning: `subworkflows/local/prepare_reference_files/main.nf:157:73`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
              ch_host_fasta_transcripts = params.host_fasta_transcripts ? Channel.value(file(params.host_fasta_transcripts, checkIfExists: true)) : Channel.empty()
                                                                          ^^^^^^^
  ```

- Warning: `subworkflows/local/prepare_reference_files/main.nf:157:147`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
              ch_host_fasta_transcripts = params.host_fasta_transcripts ? Channel.value(file(params.host_fasta_transcripts, checkIfExists: true)) : Channel.empty()
                                                                                                                                                    ^^^^^^^
  ```

- Warning: `subworkflows/local/prepare_reference_files/main.nf:181:81`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
              ch_pathogen_fasta_transcripts = params.pathogen_fasta_transcripts ? Channel.value(file(params.pathogen_fasta_transcripts, checkIfExists: true)) : Channel.empty()
                                                                                  ^^^^^^^
  ```

- Warning: `subworkflows/local/prepare_reference_files/main.nf:181:159`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
              ch_pathogen_fasta_transcripts = params.pathogen_fasta_transcripts ? Channel.value(file(params.pathogen_fasta_transcripts, checkIfExists: true)) : Channel.empty()
                                                                                                                                                                ^^^^^^^
  ```

- Warning: `subworkflows/local/prepare_reference_files/main.nf:383:116`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      host_pathogen_transcripts_gff   = params.salmon_sa || params.salmon_ab ? COMBINE_FILES_PATHOGEN_HOST_GFF.out : Channel.empty() // 'host_pathogen_transcripts.gff'
                                                                                                                     ^^^^^^^
  ```

- Warning: `subworkflows/local/prepare_reference_files/main.nf:384:128`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      annotations_host_salmon         = params.salmon_sa || params.salmon_ab ? EXTRACT_ANNOTATIONS_HOST_SALMON.out.annotations : Channel.empty() // extracted_annotations_host_salmon.tsv
                                                                                                                                 ^^^^^^^
  ```

- Warning: `subworkflows/local/prepare_reference_files/main.nf:385:132`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      annotations_pathogen_salmon     = params.salmon_sa || params.salmon_ab ? EXTRACT_ANNOTATIONS_PATHOGEN_SALMON.out.annotations : Channel.empty() // extracted_annotations_pathogen_salmon.tsv
                                                                                                                                     ^^^^^^^
  ```

- Warning: `subworkflows/local/salmon_alignment_based/main.nf:24:19`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_versions = Channel.empty()
                    ^^^^^^^
  ```

- Warning: `subworkflows/local/salmon_alignment_based/main.nf:82:50`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
      input_files = SALMON_QUANT.out.results.map { it[1] }.collect()
                                                   ^^
  ```

- Warning: `subworkflows/local/salmon_alignment_based/main.nf:87:9`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
          Channel.value("both"),
          ^^^^^^^
  ```

- Warning: `subworkflows/local/salmon_alignment_based/main.nf:96:36`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          .map { [[id: "combined"], [it]] }
                                     ^^
  ```

- Warning: `subworkflows/local/salmon_selective_alignment/main.nf:21:19`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_versions = Channel.empty()
                    ^^^^^^^
  ```

- Warning: `subworkflows/local/salmon_selective_alignment/main.nf:64:50`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
      input_files = SALMON_QUANT.out.results.map { it[1] }.collect()
                                                   ^^
  ```

- Warning: `subworkflows/local/salmon_selective_alignment/main.nf:69:9`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
          Channel.value("both"),
          ^^^^^^^
  ```

- Warning: `subworkflows/local/salmon_selective_alignment/main.nf:78:36`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          .map { [[id: "combined"], [it]] }
                                     ^^
  ```

- Warning: `subworkflows/local/star_htseq/main.nf:13:19`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_versions = Channel.empty()
                    ^^^^^^^
  ```

- Warning: `subworkflows/local/utils_nfcore_dualrnaseq_pipeline/main.nf:30:5`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
      monochrome_logs   // boolean: Do not use coloured log outputs
      ^^^^^^^^^^^^^^^
  ```

- Warning: `subworkflows/local/utils_nfcore_dualrnaseq_pipeline/main.nf:33:5`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
      input             //  string: Path to input samplesheet
      ^^^^^
  ```

- Warning: `subworkflows/local/utils_nfcore_dualrnaseq_pipeline/main.nf:37:19`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_versions = Channel.empty()
                    ^^^^^^^
  ```

- Warning: `subworkflows/local/utils_nfcore_dualrnaseq_pipeline/main.nf:74:5`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      Channel.fromList(samplesheetToList(params.input, "${projectDir}/assets/schema_input.json"))
      ^^^^^^^
  ```

- Warning: `subworkflows/nf-core/utils_nfcore_pipeline/main.nf:101:98`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      return ch_versions.unique().map { version -> processVersionsFromYAML(version) }.unique().mix(Channel.of(workflowVersionToYAML()))
                                                                                                   ^^^^^^^
  ```

- Warning: `workflows/dualrnaseq.nf:44:19`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_versions = Channel.empty()
                    ^^^^^^^
  ```

- Warning: `workflows/dualrnaseq.nf:45:24`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_multiqc_files = Channel.empty()
                         ^^^^^^^
  ```

- Warning: `workflows/dualrnaseq.nf:50:25`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_multiqc_config = Channel.fromPath("${projectDir}/assets/multiqc_config.yml", checkIfExists: true)
                          ^^^^^^^
  ```

- Warning: `workflows/dualrnaseq.nf:51:56`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_multiqc_custom_config = params.multiqc_config ? Channel.fromPath(params.multiqc_config) : Channel.empty()
                                                         ^^^^^^^
  ```

- Warning: `workflows/dualrnaseq.nf:51:98`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_multiqc_custom_config = params.multiqc_config ? Channel.fromPath(params.multiqc_config) : Channel.empty()
                                                                                                   ^^^^^^^
  ```

- Warning: `workflows/dualrnaseq.nf:52:45`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_multiqc_logo = params.multiqc_logo ? Channel.fromPath(params.multiqc_logo) : Channel.empty()
                                              ^^^^^^^
  ```

- Warning: `workflows/dualrnaseq.nf:52:85`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_multiqc_logo = params.multiqc_logo ? Channel.fromPath(params.multiqc_logo) : Channel.empty()
                                                                                      ^^^^^^^
  ```

- Warning: `workflows/dualrnaseq.nf:61:74`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          ch_multiqc_files = ch_multiqc_files.mix(FASTQC.out.zip.collect { it[1] })
                                                                           ^^
  ```
