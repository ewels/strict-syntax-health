# Nextflow lint results

- Generated: 2026-01-16T02:02:17.541549+00:00
- Nextflow version: 25.12.0-edge
- Summary: 4 errors, 39 warnings

## :x: Errors

- Error: `modules/nf-core/cellranger/multi/main.nf:126:46`: `meta_fb` is not defined

  ```nextflow
      fb_options_r1_length = fb_options_use && meta_fb.options.containsKey("r1-length") ? "r1-length,${meta_fb.options["r1-length"]}" : ''
                                               ^^^^^^^^^^
  ```

- Error: `modules/nf-core/cellranger/multi/main.nf:126:102`: `meta_fb` is not defined

  ```nextflow
      fb_options_r1_length = fb_options_use && meta_fb.options.containsKey("r1-length") ? "r1-length,${meta_fb.options["r1-length"]}" : ''
                                                                                                       ^^^^^^^^^^
  ```

- Error: `modules/nf-core/cellranger/multi/main.nf:127:46`: `meta_fb` is not defined

  ```nextflow
      fb_options_r2_length = fb_options_use && meta_fb.options.containsKey("r2-length") ? "r2-length,${meta_fb.options["r2-length"]}" : ''
                                               ^^^^^^^^^^
  ```

- Error: `modules/nf-core/cellranger/multi/main.nf:127:102`: `meta_fb` is not defined

  ```nextflow
      fb_options_r2_length = fb_options_use && meta_fb.options.containsKey("r2-length") ? "r2-length,${meta_fb.options["r2-length"]}" : ''
                                                                                                       ^^^^^^^^^^
  ```

## :warning: Warnings

- Warning: `modules/nf-core/cellranger/multi/main.nf:44:63`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
      if ([ocm_barcodes, cmo_barcodes, frna_sampleinfo].count { it } >= 2) {
                                                                ^^^^^^^^^^
  ```

- Warning: `modules/nf-core/cellranger/multi/main.nf:47:5`: Variable was declared but not used

  ```nextflow
      args   = task.ext.args   ?: ''
      ^^^^^^^^^^
  ```

- Warning: `modules/nf-core/cellranger/multi/main.nf:71:5`: Variable was declared but not used

  ```nextflow
      gex_reference_path = include_gex ? "reference,./${gex_reference_name}" : ''
      ^^^^^^^^^^
  ```

- Warning: `modules/nf-core/cellranger/multi/main.nf:72:5`: Variable was declared but not used

  ```nextflow
      fb_reference_path  = include_fb  ? "reference,./${fb_reference_name}"  : ''
      ^^^^^^^^^^
  ```

- Warning: `modules/nf-core/cellranger/multi/main.nf:73:5`: Variable was declared but not used

  ```nextflow
      vdj_reference_path = include_vdj ? "reference,./${vdj_reference_name}" : ''
      ^^^^^^^^^^
  ```

- Warning: `modules/nf-core/cellranger/multi/main.nf:76:5`: Variable was declared but not used

  ```nextflow
      target_panel = gex_targetpanel_name != '' ? "target-panel,./$gex_targetpanel_name" : ''
      ^^^^^^^^^^
  ```

- Warning: `modules/nf-core/cellranger/multi/main.nf:79:5`: Variable was declared but not used

  ```nextflow
      frna_probeset = include_frna && gex_frna_probeset_name != '' ? "probe-set,./$gex_frna_probeset_name" : ''
      ^^^^^^^^^^
  ```

- Warning: `modules/nf-core/cellranger/multi/main.nf:82:5`: Variable was declared but not used

  ```nextflow
      primer_index = vdj_primer_index ? "inner-enrichment-primers,./references/primers/${vdj_primer_index.getName()}" : ''
      ^^^^^^^^^^
  ```

- Warning: `modules/nf-core/cellranger/multi/main.nf:85:5`: Variable was declared but not used

  ```nextflow
      beam_antigen_csv = include_beam && beam_antigen_panel_name != '' ? "reference,./$beam_antigen_panel_name" : ''
      ^^^^^^^^^^
  ```

- Warning: `modules/nf-core/cellranger/multi/main.nf:89:5`: Variable was declared but not used

  ```nextflow
      beam_csv_text  = include_beam && beam_control_panel.size() > 0 ? beam_control_panel : ''
      ^^^^^^^^^^
  ```

- Warning: `modules/nf-core/cellranger/multi/main.nf:90:5`: Variable was declared but not used

  ```nextflow
      cmo_csv_text   = include_cmo  && cmo_barcodes.size() > 0       ? cmo_barcodes       : ''
      ^^^^^^^^^^
  ```

- Warning: `modules/nf-core/cellranger/multi/main.nf:91:5`: Variable was declared but not used

  ```nextflow
      ocm_csv_text   = include_ocm  && ocm_barcodes.size() > 0       ? ocm_barcodes       : ''
      ^^^^^^^^^^
  ```

- Warning: `modules/nf-core/cellranger/multi/main.nf:92:5`: Variable was declared but not used

  ```nextflow
      frna_csv_text  = include_frna && frna_sampleinfo.size() > 0    ? frna_sampleinfo    : ''
      ^^^^^^^^^^
  ```

- Warning: `modules/nf-core/cellranger/multi/main.nf:102:5`: Variable was declared but not used

  ```nextflow
      beam_options_use   = include_beam && meta_beam?.options ? 'true' : null
      ^^^^^^^^^^
  ```

- Warning: `modules/nf-core/cellranger/multi/main.nf:107:5`: Variable was declared but not used

  ```nextflow
      gex_options_filter_probes = gex_options_use && meta_gex.options.containsKey("filter-probes") ? "filter-probes,${meta_gex.options["filter-probes"]}" : ''
      ^^^^^^^^^^
  ```

- Warning: `modules/nf-core/cellranger/multi/main.nf:108:5`: Variable was declared but not used

  ```nextflow
      gex_options_r1_length     = gex_options_use && meta_gex.options.containsKey("r1-length")     ? "r1-length,${meta_gex.options["r1-length"]}"         : ''
      ^^^^^^^^^^
  ```

- Warning: `modules/nf-core/cellranger/multi/main.nf:109:5`: Variable was declared but not used

  ```nextflow
      gex_options_r2_length     = gex_options_use && meta_gex.options.containsKey("r2-length")     ? "r2-length,${meta_gex.options["r2-length"]}"         : ''
      ^^^^^^^^^^
  ```

- Warning: `modules/nf-core/cellranger/multi/main.nf:110:5`: Variable was declared but not used

  ```nextflow
      gex_options_chemistry     = gex_options_use && meta_gex.options.containsKey("chemistry")     ? "chemistry,${meta_gex.options["chemistry"]}"         : ''
      ^^^^^^^^^^
  ```

- Warning: `modules/nf-core/cellranger/multi/main.nf:111:5`: Variable was declared but not used

  ```nextflow
      gex_options_expect_cells  = gex_options_use && meta_gex.options.containsKey("expect-cells")  ? "expect-cells,${meta_gex.options["expect-cells"]}"   : ''
      ^^^^^^^^^^
  ```

- Warning: `modules/nf-core/cellranger/multi/main.nf:112:5`: Variable was declared but not used

  ```nextflow
      gex_options_force_cells   = gex_options_use && meta_gex.options.containsKey("force-cells")   ? "force-cells,${meta_gex.options["force-cells"]}"     : ''
      ^^^^^^^^^^
  ```

- Warning: `modules/nf-core/cellranger/multi/main.nf:113:5`: Variable was declared but not used

  ```nextflow
      gex_options_no_secondary  = gex_options_use && meta_gex.options.containsKey("no-secondary")  ? "no-secondary,${meta_gex.options["no-secondary"]}"   : ''
      ^^^^^^^^^^
  ```

- Warning: `modules/nf-core/cellranger/multi/main.nf:114:5`: Variable was declared but not used

  ```nextflow
      gex_options_no_bam        = gex_options_use && meta_gex.options.containsKey("create-bam")    ? "create-bam,${meta_gex.options["create-bam"]}"           : ''
      ^^^^^^^^^^
  ```

- Warning: `modules/nf-core/cellranger/multi/main.nf:115:5`: Variable was declared but not used

  ```nextflow
      gex_options_no_target_umi_filter = gex_options_use && meta_gex.options.containsKey("no-target-umi-filter") ? "no-target-umi-filter,${meta_gex.options["no-target-umi-filter"]}" : ''
      ^^^^^^^^^^
  ```

- Warning: `modules/nf-core/cellranger/multi/main.nf:116:5`: Variable was declared but not used

  ```nextflow
      gex_options_include_introns      = gex_options_use && meta_gex.options.containsKey("include-introns")      ? "include-introns,${meta_gex.options["include-introns"]}"           : ''
      ^^^^^^^^^^
  ```

- Warning: `modules/nf-core/cellranger/multi/main.nf:117:5`: Variable was declared but not used

  ```nextflow
      gex_options_check_library_compatibility = gex_options_use && meta_gex.options.containsKey("check-library-compatibility") ? "check-library-compatibility,${meta_gex.options["check-library-compatibility"]}" : ''
      ^^^^^^^^^^
  ```

- Warning: `modules/nf-core/cellranger/multi/main.nf:119:5`: Variable was declared but not used

  ```nextflow
      cmo_reference_path = cmo_options_use && cmo_reference_name    ? "cmo-set,./${cmo_reference_name}"                      : ''
      ^^^^^^^^^^
  ```

- Warning: `modules/nf-core/cellranger/multi/main.nf:120:5`: Variable was declared but not used

  ```nextflow
      cmo_barcode_path   = cmo_options_use && cmo_sample_assignment ? "barcode-sample-assignment,./${cmo_sample_assignment}" : ''
      ^^^^^^^^^^
  ```

- Warning: `modules/nf-core/cellranger/multi/main.nf:121:5`: Variable was declared but not used

  ```nextflow
      cmo_options_min_assignment_confidence = cmo_options_use && meta_cmo.options.containsKey("min-assignment-confidence") ? "min-assignment-confidence,${meta_cmo.options["min-assignment-confidence"]}" : ''
      ^^^^^^^^^^
  ```

- Warning: `modules/nf-core/cellranger/multi/main.nf:123:5`: Variable was declared but not used

  ```nextflow
      vdj_options_r1_length = vdj_options_use && meta_vdj.options.containsKey("r1-length") ? "r1-length,${meta_vdj.options["r1-length"]}" : ''
      ^^^^^^^^^^
  ```

- Warning: `modules/nf-core/cellranger/multi/main.nf:124:5`: Variable was declared but not used

  ```nextflow
      vdj_options_r2_length = vdj_options_use && meta_vdj.options.containsKey("r2-length") ? "r2-length,${meta_vdj.options["r2-length"]}" : ''
      ^^^^^^^^^^
  ```

- Warning: `modules/nf-core/cellranger/multi/main.nf:126:5`: Variable was declared but not used

  ```nextflow
      fb_options_r1_length = fb_options_use && meta_fb.options.containsKey("r1-length") ? "r1-length,${meta_fb.options["r1-length"]}" : ''
      ^^^^^^^^^^
  ```

- Warning: `modules/nf-core/cellranger/multi/main.nf:127:5`: Variable was declared but not used

  ```nextflow
      fb_options_r2_length = fb_options_use && meta_fb.options.containsKey("r2-length") ? "r2-length,${meta_fb.options["r2-length"]}" : ''
      ^^^^^^^^^^
  ```

- Warning: `modules/nf-core/cellranger/multi/main.nf:131:5`: Variable was declared but not used

  ```nextflow
      fastq_gex      = include_gex                      ? "${meta_gex.id},./fastq_all/gex,,Gene Expression"            : ''
      ^^^^^^^^^^
  ```

- Warning: `modules/nf-core/cellranger/multi/main.nf:132:5`: Variable was declared but not used

  ```nextflow
      fastq_vdj      = include_vdj                      ? "${meta_vdj.id},./fastq_all/vdj,,VDJ"                        : ''
      ^^^^^^^^^^
  ```

- Warning: `modules/nf-core/cellranger/multi/main.nf:133:5`: Variable was declared but not used

  ```nextflow
      fastq_antibody = include_fb && ab_options_use     ? "${meta_ab.id},./fastq_all/ab,,Antibody Capture"             : ''
      ^^^^^^^^^^
  ```

- Warning: `modules/nf-core/cellranger/multi/main.nf:134:5`: Variable was declared but not used

  ```nextflow
      fastq_beam     = include_beam                     ? "${meta_beam.id},./fastq_all/beam,,Antigen Capture"         : ''
      ^^^^^^^^^^
  ```

- Warning: `modules/nf-core/cellranger/multi/main.nf:135:5`: Variable was declared but not used

  ```nextflow
      fastq_crispr   = include_fb && crispr_options_use ? "${meta_crispr.id},./fastq_all/crispr,,CRISPR Guide Capture" : ''
      ^^^^^^^^^^
  ```

- Warning: `modules/nf-core/cellranger/multi/main.nf:136:5`: Variable was declared but not used

  ```nextflow
      fastq_cmo      = include_cmo                      ? "${meta_cmo.id},./fastq_all/cmo,,Multiplexing Capture"       : ''
      ^^^^^^^^^^
  ```

- Warning: `modules/nf-core/cellranger/multi/main.nf:139:5`: Variable was declared but not used

  ```nextflow
      config = "cellranger_multi_config.csv"
      ^^^^^^^^^^
  ```
