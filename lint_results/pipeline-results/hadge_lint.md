# Nextflow lint results

- Generated: 2026-08-24T00:09:59.548076560Z
- Nextflow version: 26.08.0-edge
- Summary: 27 warnings

## :warning: Warnings

- Warning: `modules/local/hash_summary/main.nf:34:5`: Variable was declared but not used

  ```nextflow
      hash_list      = "${meta.hto_names}".split(",")
      ^^^^^^^^^
  ```

- Warning: `modules/local/htodemux_visualization/main.nf:27:5`: Variable was declared but not used

  ```nextflow
      ridgePlot      = task.ext.ridgePlot      ?: true         // Generate ridge plot
      ^^^^^^^^^
  ```

- Warning: `modules/local/htodemux_visualization/main.nf:28:5`: Variable was declared but not used

  ```nextflow
      ridgeNCol      = task.ext.ridgeNCol      ?: 2            // Number of columns for ridge plot
      ^^^^^^^^^
  ```

- Warning: `modules/local/htodemux_visualization/main.nf:31:5`: Variable was declared but not used

  ```nextflow
      featureScatter = task.ext.featureScatter ?: true         // Generate feature scatter plot
      ^^^^^^^^^^^^^^
  ```

- Warning: `modules/local/htodemux_visualization/main.nf:32:5`: Variable was declared but not used

  ```nextflow
      scatterFeat1   = task.ext.scatterFeat1   ?: null         // Feature 1 for scatter plot
      ^^^^^^^^^^^^
  ```

- Warning: `modules/local/htodemux_visualization/main.nf:33:5`: Variable was declared but not used

  ```nextflow
      scatterFeat2   = task.ext.scatterFeat2   ?: null         // Feature 2 for scatter plot
      ^^^^^^^^^^^^
  ```

- Warning: `modules/local/htodemux_visualization/main.nf:36:5`: Variable was declared but not used

  ```nextflow
      vlnPlot        = task.ext.vlnPlot        ?: true         // Generate violin plot
      ^^^^^^^
  ```

- Warning: `modules/local/htodemux_visualization/main.nf:37:5`: Variable was declared but not used

  ```nextflow
      vlnFeatures    = task.ext.vlnFeatures    ?: "nCount_RNA" // Features to plot (gene expression, metrics, PC scores, anything that can be retreived by FetchData)
      ^^^^^^^^^^^
  ```

- Warning: `modules/local/htodemux_visualization/main.nf:38:5`: Variable was declared but not used

  ```nextflow
      vlnLog         = task.ext.vlnLog         ?: true         // Plot the feature axis on log scale
      ^^^^^^
  ```

- Warning: `modules/local/htodemux_visualization/main.nf:41:5`: Variable was declared but not used

  ```nextflow
      tSNE           = task.ext.tSNE           ?: true         // Generate a two dimensional tSNE embedding for HTOs
      ^^^^
  ```

- Warning: `modules/local/htodemux_visualization/main.nf:42:5`: Variable was declared but not used

  ```nextflow
      tSNEIdents     = task.ext.tSNEIdents     ?: "Negative"   // What should we remove from the object (we have Singlet,Doublet and Negative)
      ^^^^^^^^^^
  ```

- Warning: `modules/local/htodemux_visualization/main.nf:43:5`: Variable was declared but not used

  ```nextflow
      tSNEInvert     = task.ext.tSNEInvert     ?: true         // Invert tSNE selection
      ^^^^^^^^^^
  ```

- Warning: `modules/local/htodemux_visualization/main.nf:44:5`: Variable was declared but not used

  ```nextflow
      tSNEVerbose    = task.ext.tSNEVerbose    ?: false        // Verbose tSNE
      ^^^^^^^^^^^
  ```

- Warning: `modules/local/htodemux_visualization/main.nf:45:5`: Variable was declared but not used

  ```nextflow
      tSNEApprox     = task.ext.tSNEApprox     ?: false        // Approximate tSNE
      ^^^^^^^^^^
  ```

- Warning: `modules/local/htodemux_visualization/main.nf:46:5`: Variable was declared but not used

  ```nextflow
      tSNEDimMax     = task.ext.tSNEDimMax     ?: 2            // Max number of donors
      ^^^^^^^^^^
  ```

- Warning: `modules/local/htodemux_visualization/main.nf:47:5`: Variable was declared but not used

  ```nextflow
      tSNEPerplexity = task.ext.tSNEPerplexity ?: 100          // Value for perplexity
      ^^^^^^^^^^^^^^
  ```

- Warning: `modules/local/htodemux_visualization/main.nf:50:5`: Variable was declared but not used

  ```nextflow
      heatMap        = task.ext.heatMap        ?: true         // Generate heatmap
      ^^^^^^^
  ```

- Warning: `modules/local/htodemux_visualization/main.nf:51:5`: Variable was declared but not used

  ```nextflow
      heatMapNcells  = task.ext.heatMapNcells  ?: 500          // Number of cells for heatmap
      ^^^^^^^^^^^^^
  ```

- Warning: `modules/local/preprocessing_for_htodemux_multiseq/main.nf:24:5`: Variable was declared but not used

  ```nextflow
      sel_method  = task.ext.sel_method  ?: "mean.var.plot" // Selection method
      ^^^^^^^^^^
  ```

- Warning: `modules/local/preprocessing_for_htodemux_multiseq/main.nf:25:5`: Variable was declared but not used

  ```nextflow
      ndelim      = task.ext.ndelim      ?: "_"             // For the initial identity class for each cell, delimiter for the cell's column name
      ^^^^^^
  ```

- Warning: `modules/local/preprocessing_for_htodemux_multiseq/main.nf:26:5`: Variable was declared but not used

  ```nextflow
      n_features  = task.ext.n_features  ?: 2000            // Number of features to be used when finding variable features
      ^^^^^^^^^^
  ```

- Warning: `modules/local/preprocessing_for_htodemux_multiseq/main.nf:27:5`: Variable was declared but not used

  ```nextflow
      assay       = task.ext.assay       ?: "HTO"           // Assay name for hashing modality
      ^^^^^
  ```

- Warning: `modules/local/preprocessing_for_htodemux_multiseq/main.nf:28:5`: Variable was declared but not used

  ```nextflow
      margin      = task.ext.margin      ?: 2               // Margin for normalisation
      ^^^^^^
  ```

- Warning: `modules/local/preprocessing_for_htodemux_multiseq/main.nf:29:5`: Variable was declared but not used

  ```nextflow
      norm_method = task.ext.norm_method ?: "CLR"           // Normalisation method
      ^^^^^^^^^^^
  ```

- Warning: `modules/local/preprocessing_for_htodemux_multiseq/main.nf:30:5`: Variable was declared but not used

  ```nextflow
      gene_col    = task.ext.gene_col    ?: 2               // Specify which column of genes.tsv or features.tsv to use for gene names
      ^^^^^^^^
  ```

- Warning: `modules/nf-core/gmmdemux/main.nf:62:9`: Variable was declared but not used

  ```nextflow
      def prefix = task.ext.prefix ?: "${meta.id}"
          ^^^^^^
  ```

- Warning: `subworkflows/local/utils_nfcore_hadge_pipeline/main.nf:40:5`: Variable was declared but not used

  ```nextflow
      ch_versions = channel.empty()
      ^^^^^^^^^^^
  ```
