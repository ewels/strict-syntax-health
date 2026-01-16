# Nextflow lint results

- Generated: 2026-01-16T10:26:27.047655018Z
- Nextflow version: 25.12.0-edge
- Summary: 25 warnings

## :warning: Warnings

- Warning: `conf/modules_boltz.config:37:21`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          ].findAll { it }.join(' ').trim()
                      ^^
  ```

- Warning: `modules/local/combine_uniprot/main.nf:21:9`: Variable was declared but not used

  ```nextflow
      def args = task.ext.args ?: ''
          ^^^^
  ```

- Warning: `modules/local/download_pdbmmcif/main.nf:25:9`: Variable was declared but not used

  ```nextflow
      def args = task.ext.args ?: ''
          ^^^^
  ```

- Warning: `modules/local/download_pdbmmcif_af3/main.nf:25:9`: Variable was declared but not used

  ```nextflow
      def args = task.ext.args ?: ''
          ^^^^
  ```

- Warning: `modules/local/download_rna_rf2na/main.nf:27:9`: Variable was declared but not used

  ```nextflow
      def args = task.ext.args ?: ''
          ^^^^
  ```

- Warning: `modules/local/fasta2yaml/main.nf:22:9`: Variable was declared but not used

  ```nextflow
      def args = task.ext.args ?: ''
          ^^^^
  ```

- Warning: `modules/local/run_rosettafold2na/main.nf:35:9`: Variable was declared but not used

  ```nextflow
      def args = task.ext.args ?: ''
          ^^^^
  ```

- Warning: `modules/local/run_rosettafold2na/main.nf:36:9`: Variable was declared but not used

  ```nextflow
      def VERSION = 'dev' // WARN: Version information not provided by tool on CLI. Please update this string when bumping container versions.
          ^^^^^^^
  ```

- Warning: `modules/local/split_msa/main.nf:20:9`: Variable was declared but not used

  ```nextflow
      def args = task.ext.args ?: ''
          ^^^^
  ```

- Warning: `modules/nf-core/foldseek/easysearch/main.nf:46:9`: Variable was declared but not used

  ```nextflow
      def args = task.ext.args ?: ''
          ^^^^
  ```

- Warning: `modules/nf-core/mmseqs/createindex/main.nf:24:9`: Variable was declared but not used

  ```nextflow
      def prefix = task.ext.prefix ?: "${meta.id}"
          ^^^^^^
  ```

- Warning: `modules/nf-core/unzip/main.nf:38:9`: Variable was declared but not used

  ```nextflow
      def args = task.ext.args ?: ''
          ^^^^
  ```

- Warning: `subworkflows/local/aria2_uncompress.nf:37:28`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
                      .map { meta, dir ->
                             ^^^^
  ```

- Warning: `subworkflows/local/post_processing.nf:23:5`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
      requested_modes
      ^^^^^^^^^^^^^^^
  ```

- Warning: `subworkflows/local/prepare_colabfold_dbs.nf:67:44`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
                                      .map { meta, dir ->
                                             ^^^^
  ```

- Warning: `subworkflows/local/prepare_colabfold_dbs.nf:97:40`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
                                  .map { meta, dir ->
                                         ^^^^
  ```

- Warning: `subworkflows/local/utils_nfcore_proteinfold_pipeline/main.nf:32:5`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
      monochrome_logs   // boolean: Do not use coloured log outputs
      ^^^^^^^^^^^^^^^
  ```

- Warning: `subworkflows/local/utils_nfcore_proteinfold_pipeline/main.nf:35:5`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
      input             //  string: Path to input samplesheet
      ^^^^^
  ```

- Warning: `subworkflows/local/utils_nfcore_proteinfold_pipeline/main.nf:98:22`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_samplesheet = Channel.fromList(samplesheetToList(params.input, "assets/schema_input.json"))
                       ^^^^^^^
  ```

- Warning: `subworkflows/local/utils_nfcore_proteinfold_pipeline/main.nf:111:30`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          ch_samplesheet.map { meta, fasta ->
                               ^^^^
  ```

- Warning: `subworkflows/local/utils_nfcore_proteinfold_pipeline/main.nf:117:20`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
              .map { meta,fasta -> fasta }
                     ^^^^
  ```

- Warning: `subworkflows/local/utils_nfcore_proteinfold_pipeline/main.nf:303:35`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
      def headers = fasta.findAll { it.startsWith('>') }
                                    ^^
  ```

- Warning: `workflows/rosettafold2na.nf:31:5`: Variable was declared but not used

  ```nextflow
      ch_multiqc_files  = channel.empty()
      ^^^^^^^^^^^^^^^^
  ```

- Warning: `workflows/rosettafold2na.nf:32:5`: Variable was declared but not used

  ```nextflow
      ch_top_ranked_pdb = channel.empty()
      ^^^^^^^^^^^^^^^^^
  ```

- Warning: `workflows/rosettafold2na.nf:33:5`: Variable was declared but not used

  ```nextflow
      ch_pdb_msa        = channel.empty()
      ^^^^^^^^^^
  ```
