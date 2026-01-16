# Nextflow lint results

- Generated: 2026-01-16T10:30:17.623636368Z
- Nextflow version: 25.12.0-edge
- Summary: 98 warnings

## :warning: Warnings

- Warning: `modules/local/ficture/model/main.nf:20:9`: Variable was declared but not used

  ```nextflow
      def args = task.ext.args ?: ''
          ^^^^
  ```

- Warning: `modules/local/ficture/model/main.nf:21:9`: Variable was declared but not used

  ```nextflow
      def prefix = task.ext.prefix ?: "${meta.id}"
          ^^^^^^
  ```

- Warning: `modules/local/ficture/model/main.nf:43:9`: Variable was declared but not used

  ```nextflow
      def args = task.ext.args ?: ''
          ^^^^
  ```

- Warning: `modules/local/ficture/model/main.nf:44:9`: Variable was declared but not used

  ```nextflow
      def prefix = task.ext.prefix ?: "${meta.id}"
          ^^^^^^
  ```

- Warning: `modules/local/ficture/preprocess/main.nf:21:9`: Variable was declared but not used

  ```nextflow
      def args = task.ext.args ?: ''
          ^^^^
  ```

- Warning: `modules/local/utility/split_transcripts/main.nf:24:9`: Variable was declared but not used

  ```nextflow
      def prefix = task.ext.prefix ?: "${meta.id}"
          ^^^^^^
  ```

- Warning: `subworkflows/local/baysor_generate_preview/main.nf:17:27`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_versions         = Channel.empty()
                            ^^^^^^^
  ```

- Warning: `subworkflows/local/baysor_generate_preview/main.nf:18:27`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_preview_mqc_html = Channel.empty()
                            ^^^^^^^
  ```

- Warning: `subworkflows/local/baysor_generate_preview/main.nf:19:27`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_preview_mqc_png  = Channel.empty()
                            ^^^^^^^
  ```

- Warning: `subworkflows/local/baysor_generate_segfree/main.nf:15:19`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_versions = Channel.empty()
                    ^^^^^^^
  ```

- Warning: `subworkflows/local/baysor_run_prior_segmentation_mask/main.nf:19:19`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_versions = Channel.empty()
                    ^^^^^^^
  ```

- Warning: `subworkflows/local/baysor_run_prior_segmentation_mask/main.nf:21:22`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_transcripts = Channel.empty()
                       ^^^^^^^
  ```

- Warning: `subworkflows/local/baysor_run_prior_segmentation_mask/main.nf:23:27`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_redefined_bundle = Channel.empty()
                            ^^^^^^^
  ```

- Warning: `subworkflows/local/baysor_run_prior_segmentation_mask/main.nf:24:27`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_coordinate_space = Channel.value("pixels")
                            ^^^^^^^
  ```

- Warning: `subworkflows/local/baysor_run_transcripts_parquet/main.nf:19:19`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_versions = Channel.empty()
                    ^^^^^^^
  ```

- Warning: `subworkflows/local/baysor_run_transcripts_parquet/main.nf:21:22`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_transcripts = Channel.empty()
                       ^^^^^^^
  ```

- Warning: `subworkflows/local/baysor_run_transcripts_parquet/main.nf:24:27`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_redefined_bundle = Channel.empty()
                            ^^^^^^^
  ```

- Warning: `subworkflows/local/baysor_run_transcripts_parquet/main.nf:25:27`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_coordinate_space = Channel.value("microns")
                            ^^^^^^^
  ```

- Warning: `subworkflows/local/cellpose_baysor_import_segmentation/main.nf:24:19`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_versions = Channel.empty()
                    ^^^^^^^
  ```

- Warning: `subworkflows/local/cellpose_baysor_import_segmentation/main.nf:25:22`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_transcripts = Channel.empty()
                       ^^^^^^^
  ```

- Warning: `subworkflows/local/cellpose_baysor_import_segmentation/main.nf:26:25`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_imp_seg_inputs = Channel.empty()
                          ^^^^^^^
  ```

- Warning: `subworkflows/local/cellpose_baysor_import_segmentation/main.nf:27:31`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_filtered_transcripts = Channel.empty()
                                ^^^^^^^
  ```

- Warning: `subworkflows/local/cellpose_baysor_import_segmentation/main.nf:28:27`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_coordinate_space = Channel.value("microns")
                            ^^^^^^^
  ```

- Warning: `subworkflows/local/cellpose_baysor_import_segmentation/main.nf:31:47`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      cellpose_model = params.cellpose_model ? (Channel.fromPath(params.cellpose_model, checkIfExists: true)) : []
                                                ^^^^^^^
  ```

- Warning: `subworkflows/local/cellpose_resolift_morphology_ome_tif/main.nf:17:19`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_versions = Channel.empty()
                    ^^^^^^^
  ```

- Warning: `subworkflows/local/cellpose_resolift_morphology_ome_tif/main.nf:18:25`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_imp_seg_inputs = Channel.empty()
                          ^^^^^^^
  ```

- Warning: `subworkflows/local/cellpose_resolift_morphology_ome_tif/main.nf:19:27`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_coordinate_space = Channel.value("pixels")
                            ^^^^^^^
  ```

- Warning: `subworkflows/local/cellpose_resolift_morphology_ome_tif/main.nf:21:47`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      cellpose_model = params.cellpose_model ? (Channel.fromPath(params.cellpose_model, checkIfExists: true)) : []
                                                ^^^^^^^
  ```

- Warning: `subworkflows/local/ficture_preprocess_model/main.nf:18:19`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_versions = Channel.empty()
                    ^^^^^^^
  ```

- Warning: `subworkflows/local/ficture_preprocess_model/main.nf:31:25`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_features_clean = Channel.empty()
                          ^^^^^^^
  ```

- Warning: `subworkflows/local/opt_flip_track_stat/main.nf:14:19`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_versions = Channel.empty()
                    ^^^^^^^
  ```

- Warning: `subworkflows/local/opt_flip_track_stat/main.nf:15:18`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_summary = Channel.empty()
                   ^^^^^^^
  ```

- Warning: `subworkflows/local/proseg_preset_proseg2baysor/main.nf:16:19`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_versions = Channel.empty()
                    ^^^^^^^
  ```

- Warning: `subworkflows/local/proseg_preset_proseg2baysor/main.nf:17:27`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_coordinate_space = Channel.value("microns")
                            ^^^^^^^
  ```

- Warning: `subworkflows/local/segger_create_train_predict/main.nf:18:19`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_versions = Channel.empty()
                    ^^^^^^^
  ```

- Warning: `subworkflows/local/segger_create_train_predict/main.nf:20:25`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_updated_bundle = Channel.empty()
                          ^^^^^^^
  ```

- Warning: `subworkflows/local/segger_create_train_predict/main.nf:21:27`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_redefined_bundle = Channel.empty()
                            ^^^^^^^
  ```

- Warning: `subworkflows/local/segger_create_train_predict/main.nf:22:27`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_coordinate_space = Channel.value("pixels")
                            ^^^^^^^
  ```

- Warning: `subworkflows/local/spatialdata_write_meta_merge/main.nf:18:19`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_versions = Channel.empty()
                    ^^^^^^^
  ```

- Warning: `subworkflows/local/spatialdata_write_meta_merge/main.nf:19:27`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_segmented_object = Channel.empty()
                            ^^^^^^^
  ```

- Warning: `subworkflows/local/spatialdata_write_meta_merge/main.nf:25:35`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
              ch_segmented_object = Channel.value('cells_and_nuclei')
                                    ^^^^^^^
  ```

- Warning: `subworkflows/local/spatialdata_write_meta_merge/main.nf:28:35`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
              ch_segmented_object = Channel.value('nuclei')
                                    ^^^^^^^
  ```

- Warning: `subworkflows/local/spatialdata_write_meta_merge/main.nf:31:35`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
              ch_segmented_object = Channel.value('cells')
                                    ^^^^^^^
  ```

- Warning: `subworkflows/local/spatialdata_write_meta_merge/main.nf:34:35`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
              ch_segmented_object = Channel.value([])
                                    ^^^^^^^
  ```

- Warning: `subworkflows/local/spatialdata_write_meta_merge/main.nf:40:31`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
          ch_segmented_object = Channel.value([])
                                ^^^^^^^
  ```

- Warning: `subworkflows/local/utils_nfcore_spatialxe_pipeline/main.nf:30:5`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
      monochrome_logs   // boolean: Do not use coloured log outputs
      ^^^^^^^^^^^^^^^
  ```

- Warning: `subworkflows/local/utils_nfcore_spatialxe_pipeline/main.nf:40:19`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_versions = Channel.empty()
                    ^^^^^^^
  ```

- Warning: `subworkflows/local/utils_nfcore_spatialxe_pipeline/main.nf:65:144`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
      after_text = """${workflow.manifest.doi ? "\n* The pipeline\n" : ""}${workflow.manifest.doi.tokenize(",").collect { "    https://doi.org/${it.trim().replace('https://doi.org/', '')}" }.join("\n")}${workflow.manifest.doi ? "\n" : ""}
                                                                                                                                                 ^^
  ```

- Warning: `subworkflows/local/utils_nfcore_spatialxe_pipeline/main.nf:104:9`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
          Channel.fromList(samplesheetToList(input, "${projectDir}/assets/schema_input.json"))
          ^^^^^^^
  ```

- Warning: `subworkflows/local/utils_nfcore_spatialxe_pipeline/main.nf:291:31`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
      if (!ch_bundle_path.map { it.exists() }) {
                                ^^
  ```

- Warning: `subworkflows/local/utils_nfcore_spatialxe_pipeline/main.nf:297:30`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
      if (ch_bundle_path.map { it.exists() }) {
                               ^^
  ```

- Warning: `subworkflows/local/xeniumranger_import_segmentation_redefine_bundle/main.nf:16:19`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_versions = Channel.empty()
                    ^^^^^^^
  ```

- Warning: `subworkflows/local/xeniumranger_import_segmentation_redefine_bundle/main.nf:17:27`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_redefined_bundle = Channel.empty()
                            ^^^^^^^
  ```

- Warning: `subworkflows/local/xeniumranger_import_segmentation_redefine_bundle/main.nf:18:27`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_coordinate_space = Channel.empty()
                            ^^^^^^^
  ```

- Warning: `subworkflows/local/xeniumranger_relabel_resegment/main.nf:15:19`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_versions = Channel.empty()
                    ^^^^^^^
  ```

- Warning: `subworkflows/local/xeniumranger_resegment_morphology_ome_tif/main.nf:14:19`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_versions = Channel.empty()
                    ^^^^^^^
  ```

- Warning: `subworkflows/local/xeniumranger_resegment_morphology_ome_tif/main.nf:15:27`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_redefined_bundle = Channel.empty()
                            ^^^^^^^
  ```

- Warning: `subworkflows/local/xeniumranger_resegment_morphology_ome_tif/main.nf:16:27`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_coordinate_space = Channel.value("pixels")
                            ^^^^^^^
  ```

- Warning: `subworkflows/nf-core/utils_nfcore_pipeline/main.nf:101:98`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      return ch_versions.unique().map { version -> processVersionsFromYAML(version) }.unique().mix(Channel.of(workflowVersionToYAML()))
                                                                                                   ^^^^^^^
  ```

- Warning: `workflows/spatialxe.nf:65:19`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_versions = Channel.empty()
                    ^^^^^^^
  ```

- Warning: `workflows/spatialxe.nf:67:16`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_input = Channel.empty()
                 ^^^^^^^
  ```

- Warning: `workflows/spatialxe.nf:68:17`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_bundle = Channel.empty()
                  ^^^^^^^
  ```

- Warning: `workflows/spatialxe.nf:69:17`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_config = Channel.empty()
                  ^^^^^^^
  ```

- Warning: `workflows/spatialxe.nf:70:19`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_features = Channel.empty()
                    ^^^^^^^
  ```

- Warning: `workflows/spatialxe.nf:71:21`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_raw_bundle = Channel.empty()
                      ^^^^^^^
  ```

- Warning: `workflows/spatialxe.nf:72:21`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_gene_panel = Channel.empty()
                      ^^^^^^^
  ```

- Warning: `workflows/spatialxe.nf:73:21`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_qc_reports = Channel.empty()
                      ^^^^^^^
  ```

- Warning: `workflows/spatialxe.nf:74:22`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_bundle_path = Channel.empty()
                       ^^^^^^^
  ```

- Warning: `workflows/spatialxe.nf:75:23`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_preview_html = Channel.empty()
                        ^^^^^^^
  ```

- Warning: `workflows/spatialxe.nf:76:23`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_exp_metadata = Channel.empty()
                        ^^^^^^^
  ```

- Warning: `workflows/spatialxe.nf:77:24`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_gene_synonyms = Channel.empty()
                         ^^^^^^^
  ```

- Warning: `workflows/spatialxe.nf:78:24`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_multiqc_files = Channel.empty()
                         ^^^^^^^
  ```

- Warning: `workflows/spatialxe.nf:79:25`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_multiqc_report = Channel.empty()
                          ^^^^^^^
  ```

- Warning: `workflows/spatialxe.nf:80:26`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_qupath_polygons = Channel.empty()
                           ^^^^^^^
  ```

- Warning: `workflows/spatialxe.nf:81:27`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_morphology_image = Channel.empty()
                            ^^^^^^^
  ```

- Warning: `workflows/spatialxe.nf:82:27`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_redefined_bundle = Channel.empty()
                            ^^^^^^^
  ```

- Warning: `workflows/spatialxe.nf:83:27`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_coordinate_space = Channel.empty()
                            ^^^^^^^
  ```

- Warning: `workflows/spatialxe.nf:84:29`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_panel_probes_fasta = Channel.empty()
                              ^^^^^^^
  ```

- Warning: `workflows/spatialxe.nf:85:30`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_transcripts_parquet = Channel.empty()
                               ^^^^^^^
  ```

- Warning: `workflows/spatialxe.nf:86:32`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_reference_annotations = Channel.empty()
                                 ^^^^^^^
  ```

- Warning: `workflows/spatialxe.nf:87:32`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_multiqc_pre_xr_report = Channel.empty()
                                 ^^^^^^^
  ```

- Warning: `workflows/spatialxe.nf:88:33`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_multiqc_post_xr_report = Channel.empty()
                                  ^^^^^^^
  ```

- Warning: `workflows/spatialxe.nf:176:17`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_config = Channel.fromPath(
                  ^^^^^^^
  ```

- Warning: `workflows/spatialxe.nf:184:32`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
          ch_segmentation_mask = Channel.fromPath(
                                 ^^^^^^^
  ```

- Warning: `workflows/spatialxe.nf:193:23`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
          ch_features = Channel.fromPath(
                        ^^^^^^^
  ```

- Warning: `workflows/spatialxe.nf:202:23`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
          ch_features = Channel.fromPath(
                        ^^^^^^^
  ```

- Warning: `workflows/spatialxe.nf:211:33`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
          ch_panel_probes_fasta = Channel.fromPath(
                                  ^^^^^^^
  ```

- Warning: `workflows/spatialxe.nf:220:36`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
          ch_reference_annotations = Channel.fromPath(
                                     ^^^^^^^
  ```

- Warning: `workflows/spatialxe.nf:229:28`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
          ch_gene_synonyms = Channel.fromPath(
                             ^^^^^^^
  ```

- Warning: `workflows/spatialxe.nf:238:30`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
          ch_qupath_polygons = Channel.fromPath(
                               ^^^^^^^
  ```

- Warning: `workflows/spatialxe.nf:249:25`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
          ch_gene_panel = Channel.fromPath(
                          ^^^^^^^
  ```

- Warning: `workflows/spatialxe.nf:503:25`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_multiqc_config = Channel.fromPath(
                          ^^^^^^^
  ```

- Warning: `workflows/spatialxe.nf:509:11`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
          ? Channel.fromPath(params.multiqc_config, checkIfExists: true)
            ^^^^^^^
  ```

- Warning: `workflows/spatialxe.nf:510:11`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
          : Channel.empty()
            ^^^^^^^
  ```

- Warning: `workflows/spatialxe.nf:513:11`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
          ? Channel.fromPath(params.multiqc_logo, checkIfExists: true)
            ^^^^^^^
  ```

- Warning: `workflows/spatialxe.nf:514:11`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
          : Channel.empty()
            ^^^^^^^
  ```

- Warning: `workflows/spatialxe.nf:521:27`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_workflow_summary = Channel.value(paramsSummaryMultiqc(summary_params))
                            ^^^^^^^
  ```

- Warning: `workflows/spatialxe.nf:531:30`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_methods_description = Channel.value(
                               ^^^^^^^
  ```
