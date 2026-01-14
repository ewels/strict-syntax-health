# Nextflow lint results

- Generated: 2026-01-14T09:25:40.123292721Z
- Nextflow version: 25.12.0-edge
- Summary: 2 errors, 30 warnings

## :x: Errors

- Error: `modules/local/liana/rankaggregate/main.nf:7:9`: `https` is not defined

  ```nextflow
          https://community-cr-prod.seqera.io/docker/registry/v2/blobs/sha256/e8/e83ce3d883af5a7be7f05e740fffaf0fff63b5f13e9bf175af9465e91c8cfda2/data':
          ^^^^^
  ```

- Error: `nextflow.config:237:9`: Invalid include source: '/home/runner/work/strict-syntax-health/strict-syntax-health/pipelines/scdownstream/conf/test_offline.config'

  ```nextflow
          includeConfig 'conf/test_offline.config'
          ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  ```

## :warning: Warnings

- Warning: `modules/local/adata/extend/main.nf:22:5`: Variable was declared but not used

  ```nextflow
      prefix = task.ext.prefix ?: "${meta.id}"
      ^^^^^^
  ```

- Warning: `modules/local/adata/merge/main.nf:27:5`: Variable was declared but not used

  ```nextflow
      force_obs_cols = task.ext.force_obs_cols ?: params.force_obs_cols ?: ""
      ^^^^^^^^^^^^^^
  ```

- Warning: `modules/local/adata/mygene/main.nf:22:5`: Variable was declared but not used

  ```nextflow
      input_col = task.ext.input_col ?: "index"
      ^^^^^^^^^
  ```

- Warning: `modules/local/adata/mygene/main.nf:23:5`: Variable was declared but not used

  ```nextflow
      output_col = task.ext.output_col ?: "symbols"
      ^^^^^^^^^^
  ```

- Warning: `modules/local/adata/prepcellxgene/main.nf:21:5`: Variable was declared but not used

  ```nextflow
      prefix = task.ext.prefix ?: "${meta.id}"
      ^^^^^^
  ```

- Warning: `modules/local/adata/splitembeddings/main.nf:22:5`: Variable was declared but not used

  ```nextflow
      prefix = task.ext.prefix ?: "${meta.id}"
      ^^^^^^
  ```

- Warning: `modules/local/adata/tords/main.nf:21:5`: Variable was declared but not used

  ```nextflow
      counts_layer = task.ext.counts_layer ?: 'X'
      ^^^^^^^^^^^^
  ```

- Warning: `modules/local/liana/rankaggregate/main.nf:22:5`: Variable was declared but not used

  ```nextflow
      obs_key = meta.obs_key ?: "leiden"
      ^^^^^^^
  ```

- Warning: `modules/local/liana/rankaggregate/main.nf:23:5`: Variable was declared but not used

  ```nextflow
      prefix = task.ext.prefix ?: "${meta.id}"
      ^^^^^^
  ```

- Warning: `modules/local/scanpy/hvgs/main.nf:25:5`: Variable was declared but not used

  ```nextflow
      batch_key = task.ext.batch_key ?: ""
      ^^^^^^^^^
  ```

- Warning: `modules/local/scanpy/paga/main.nf:25:5`: Variable was declared but not used

  ```nextflow
      obs_key = meta.obs_key ?: "leiden"
      ^^^^^^^
  ```

- Warning: `modules/local/scanpy/paga/main.nf:26:5`: Variable was declared but not used

  ```nextflow
      prefix = task.ext.prefix ?: "${meta.id}"
      ^^^^^^
  ```

- Warning: `modules/local/scanpy/rankgenesgroups/main.nf:24:5`: Variable was declared but not used

  ```nextflow
      obs_key = meta.obs_key ?: "leiden"
      ^^^^^^^
  ```

- Warning: `modules/local/scanpy/rankgenesgroups/main.nf:25:5`: Variable was declared but not used

  ```nextflow
      prefix = task.ext.prefix ?: "${meta.id}"
      ^^^^^^
  ```

- Warning: `modules/local/scvitools/scanvi/main.nf:33:5`: Variable was declared but not used

  ```nextflow
      n_hidden = task.ext.n_hidden ?: 128
      ^^^^^^^^
  ```

- Warning: `modules/local/scvitools/scanvi/main.nf:34:5`: Variable was declared but not used

  ```nextflow
      n_layers = task.ext.n_layers ?: 2
      ^^^^^^^^
  ```

- Warning: `modules/local/scvitools/scanvi/main.nf:35:5`: Variable was declared but not used

  ```nextflow
      n_latent = task.ext.n_latent ?: 30
      ^^^^^^^^
  ```

- Warning: `modules/local/scvitools/scanvi/main.nf:36:5`: Variable was declared but not used

  ```nextflow
      dispersion = task.ext.dispersion ?: 'gene'
      ^^^^^^^^^^
  ```

- Warning: `modules/local/scvitools/scanvi/main.nf:37:5`: Variable was declared but not used

  ```nextflow
      gene_likelihood = task.ext.gene_likelihood ?: 'zinb'
      ^^^^^^^^^^^^^^^
  ```

- Warning: `modules/local/scvitools/scanvi/main.nf:38:5`: Variable was declared but not used

  ```nextflow
      max_epochs = task.ext.max_epochs ?: null
      ^^^^^^^^^^
  ```

- Warning: `modules/local/scvitools/scvi/main.nf:31:5`: Variable was declared but not used

  ```nextflow
      n_hidden = task.ext.n_hidden ?: 128
      ^^^^^^^^
  ```

- Warning: `modules/local/scvitools/scvi/main.nf:32:5`: Variable was declared but not used

  ```nextflow
      n_layers = task.ext.n_layers ?: 2
      ^^^^^^^^
  ```

- Warning: `modules/local/scvitools/scvi/main.nf:33:5`: Variable was declared but not used

  ```nextflow
      n_latent = task.ext.n_latent ?: 30
      ^^^^^^^^
  ```

- Warning: `modules/local/scvitools/scvi/main.nf:34:5`: Variable was declared but not used

  ```nextflow
      dispersion = task.ext.dispersion ?: 'gene'
      ^^^^^^^^^^
  ```

- Warning: `modules/local/scvitools/scvi/main.nf:35:5`: Variable was declared but not used

  ```nextflow
      gene_likelihood = task.ext.gene_likelihood ?: 'zinb'
      ^^^^^^^^^^^^^^^
  ```

- Warning: `modules/local/scvitools/scvi/main.nf:36:5`: Variable was declared but not used

  ```nextflow
      max_epochs = task.ext.max_epochs ?: null
      ^^^^^^^^^^
  ```

- Warning: `subworkflows/local/utils_nfcore_scdownstream_pipeline/main.nf:31:5`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
      monochrome_logs   // boolean: Do not use coloured log outputs
      ^^^^^^^^^^^^^^^
  ```

- Warning: `subworkflows/local/utils_nfcore_scdownstream_pipeline/main.nf:34:5`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
      input             //  string: Path to input samplesheet
      ^^^^^
  ```

- Warning: `subworkflows/local/utils_nfcore_scdownstream_pipeline/main.nf:172:79`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
      def integration_methods = params.integration_methods.split(',').collect { it.trim().toLowerCase() }
                                                                                ^^
  ```

- Warning: `subworkflows/nf-core/h5ad_removebackground_barcodes_cellbender_anndata/main.nf:13:19`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_versions = Channel.empty()
                    ^^^^^^^
  ```
