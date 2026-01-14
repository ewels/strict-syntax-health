# Nextflow lint results

- Generated: 2026-01-14T09:21:20.703754064Z
- Nextflow version: 25.12.0-edge
- Summary: 4 errors, 23 warnings

## :x: Errors

- Error: `workflows/nanostring.nf:7:1`: Statements cannot be mixed with script declarations -- move statements into a process or workflow

  ```nextflow
  ch_gene_score_yaml         = params.gene_score_yaml   ? Channel.fromPath( params.gene_score_yaml, checkIfExists: true ) : Channel.empty()
  ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  ```

- Error: `workflows/nanostring.nf:8:1`: Statements cannot be mixed with script declarations -- move statements into a process or workflow

  ```nextflow
  ch_heatmap_genes_to_filter   = params.heatmap_genes_to_filter  ? Channel.fromPath( params.heatmap_genes_to_filter, checkIfExists: true ) : Channel.empty()
  ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  ```

- Error: `workflows/nanostring.nf:112:9`: `ch_gene_score_yaml` is not defined

  ```nextflow
          ch_gene_score_yaml,
          ^^^^^^^^^^^^^^^^^^
  ```

- Error: `workflows/nanostring.nf:113:9`: `ch_heatmap_genes_to_filter` is not defined

  ```nextflow
          ch_heatmap_genes_to_filter,
          ^^^^^^^^^^^^^^^^^^^^^^^^^^
  ```

## :warning: Warnings

- Warning: `main.nf:50:9`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
          Channel.from(file(params.input)).map{ tuple( [id: file(params.input).getName()], it) } // Add meta component to channel
          ^^^^^^^
  ```

- Warning: `main.nf:50:90`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          Channel.from(file(params.input)).map{ tuple( [id: file(params.input).getName()], it) } // Add meta component to channel
                                                                                           ^^
  ```

- Warning: `modules/local/create_annotated_tables/main.nf:22:9`: Variable was declared but not used

  ```nextflow
      def args = task.ext.args ?: ''
          ^^^^
  ```

- Warning: `modules/local/create_annotated_tables/main.nf:36:9`: Variable was declared but not used

  ```nextflow
      def args = task.ext.args ?: ''
          ^^^^
  ```

- Warning: `modules/nf-core/nacho/normalize/main.nf:44:9`: Variable was declared but not used

  ```nextflow
      def args = task.ext.args ?: ''
          ^^^^
  ```

- Warning: `modules/nf-core/nacho/qc/main.nf:24:9`: Variable was declared but not used

  ```nextflow
      def args = task.ext.args ?: ''
          ^^^^
  ```

- Warning: `subworkflows/local/compute_gene_scores_heatmap/main.nf:21:19`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_versions = Channel.empty()
                    ^^^^^^^
  ```

- Warning: `subworkflows/local/compute_gene_scores_heatmap/main.nf:22:24`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_multiqc_files = Channel.empty()
                         ^^^^^^^
  ```

- Warning: `subworkflows/local/compute_gene_scores_heatmap/main.nf:32:89`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
      ch_multiqc_files = ch_multiqc_files.mix(COMPUTE_GENE_SCORES.out.scores_for_mqc.map{ meta, file -> file }.collect())
                                                                                          ^^^^
  ```

- Warning: `subworkflows/local/compute_gene_scores_heatmap/main.nf:44:92`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          ch_multiqc_files  = ch_multiqc_files.mix(CREATE_GENE_HEATMAP.out.gene_heatmap.map{ meta, file -> file }.collect())
                                                                                             ^^^^
  ```

- Warning: `subworkflows/local/utils_nfcore_nanostring_pipeline/main.nf:32:5`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
      monochrome_logs   // boolean: Do not use coloured log outputs
      ^^^^^^^^^^^^^^^
  ```

- Warning: `subworkflows/local/utils_nfcore_nanostring_pipeline/main.nf:35:5`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
      input             //  string: Path to input samplesheet
      ^^^^^
  ```

- Warning: `workflows/nanostring.nf:7:1`: Variable was declared but not used

  ```nextflow
  ch_gene_score_yaml         = params.gene_score_yaml   ? Channel.fromPath( params.gene_score_yaml, checkIfExists: true ) : Channel.empty()
  ^^^^^^^^^^^^^^^^^^
  ```

- Warning: `workflows/nanostring.nf:7:57`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
  ch_gene_score_yaml         = params.gene_score_yaml   ? Channel.fromPath( params.gene_score_yaml, checkIfExists: true ) : Channel.empty()
                                                          ^^^^^^^
  ```

- Warning: `workflows/nanostring.nf:7:123`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
  ch_gene_score_yaml         = params.gene_score_yaml   ? Channel.fromPath( params.gene_score_yaml, checkIfExists: true ) : Channel.empty()
                                                                                                                            ^^^^^^^
  ```

- Warning: `workflows/nanostring.nf:8:1`: Variable was declared but not used

  ```nextflow
  ch_heatmap_genes_to_filter   = params.heatmap_genes_to_filter  ? Channel.fromPath( params.heatmap_genes_to_filter, checkIfExists: true ) : Channel.empty()
  ^^^^^^^^^^^^^^^^^^^^^^^^^^
  ```

- Warning: `workflows/nanostring.nf:8:66`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
  ch_heatmap_genes_to_filter   = params.heatmap_genes_to_filter  ? Channel.fromPath( params.heatmap_genes_to_filter, checkIfExists: true ) : Channel.empty()
                                                                   ^^^^^^^
  ```

- Warning: `workflows/nanostring.nf:8:140`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
  ch_heatmap_genes_to_filter   = params.heatmap_genes_to_filter  ? Channel.fromPath( params.heatmap_genes_to_filter, checkIfExists: true ) : Channel.empty()
                                                                                                                                             ^^^^^^^
  ```

- Warning: `workflows/nanostring.nf:66:16`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          .map { meta, rcc_path -> rcc_path}
                 ^^^^
  ```

- Warning: `workflows/nanostring.nf:81:65`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
      ch_nacho_qc_multiqc_metrics = NACHO_QC.out.nacho_qc_png.map{it[1]}.mix(NACHO_QC.out.nacho_qc_txt.map{it[1]})
                                                                  ^^
  ```

- Warning: `workflows/nanostring.nf:81:106`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
      ch_nacho_qc_multiqc_metrics = NACHO_QC.out.nacho_qc_png.map{it[1]}.mix(NACHO_QC.out.nacho_qc_txt.map{it[1]})
                                                                                                           ^^
  ```

- Warning: `workflows/nanostring.nf:104:102`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
      ch_multiqc_files       = ch_multiqc_files.mix(CREATE_ANNOTATED_TABLES.out.annotated_data_mqc.map{it[1]}.collect())
                                                                                                       ^^
  ```

- Warning: `workflows/nanostring.nf:122:26`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      def topic_versions = Channel.topic("versions")
                           ^^^^^^^
  ```
