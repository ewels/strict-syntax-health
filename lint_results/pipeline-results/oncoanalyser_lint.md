# Nextflow lint results

- Generated: 2026-09-03T00:25:28.684320497Z
- Nextflow version: 26.08.0-edge
- Summary: 106 warnings

## :warning: Warnings

- Warning: `subworkflows/local/amber_profiling/main.nf:49:36`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          .branch { meta, tumor_aln, tumor_idx, normal_aln, normal_idx, donor_aln, donor_idx ->
                                     ^^^^^^^^^
  ```

- Warning: `subworkflows/local/amber_profiling/main.nf:49:59`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          .branch { meta, tumor_aln, tumor_idx, normal_aln, normal_idx, donor_aln, donor_idx ->
                                                            ^^^^^^^^^^
  ```

- Warning: `subworkflows/local/amber_profiling/main.nf:49:71`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          .branch { meta, tumor_aln, tumor_idx, normal_aln, normal_idx, donor_aln, donor_idx ->
                                                                        ^^^^^^^^^
  ```

- Warning: `subworkflows/local/amber_profiling/main.nf:49:82`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          .branch { meta, tumor_aln, tumor_idx, normal_aln, normal_idx, donor_aln, donor_idx ->
                                                                                   ^^^^^^^^^
  ```

- Warning: `subworkflows/local/bamtools_metrics/main.nf:35:30`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          .branch { meta, aln, idx ->
                               ^^^
  ```

- Warning: `subworkflows/local/bamtools_metrics/main.nf:52:30`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          .branch { meta, aln, idx ->
                               ^^^
  ```

- Warning: `subworkflows/local/bamtools_metrics/main.nf:91:34`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          .branch { meta_bamtools, bamtools_dir ->
                                   ^^^^^^^^^^^^
  ```

- Warning: `subworkflows/local/cider_calling/main.nf:10:5`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
      ch_inputs          // channel: [mandatory] [ meta ]
      ^^^^^^^^^
  ```

- Warning: `subworkflows/local/cider_calling/main.nf:34:30`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          .branch { meta, aln, idx ->
                               ^^^
  ```

- Warning: `subworkflows/local/cider_calling/main.nf:50:30`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          .branch { meta, aln, idx ->
                               ^^^
  ```

- Warning: `subworkflows/local/cobalt_profiling/main.nf:44:36`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          .branch { meta, tumor_aln, tumor_idx, normal_aln, normal_idx ->
                                     ^^^^^^^^^
  ```

- Warning: `subworkflows/local/cobalt_profiling/main.nf:44:59`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          .branch { meta, tumor_aln, tumor_idx, normal_aln, normal_idx ->
                                                            ^^^^^^^^^^
  ```

- Warning: `subworkflows/local/cuppa_prediction/main.nf:40:70`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          .branch { meta, isofox_dir, purple_dir, linx_annotation_dir, virusinterpreter_dir ->
                                                                       ^^^^^^^^^^^^^^^^^^^^
  ```

- Warning: `subworkflows/local/esvee_calling/main.nf:50:59`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          .branch { meta, tumor_aln, tumor_idx, normal_aln, normal_idx ->
                                                            ^^^^^^^^^^
  ```

- Warning: `subworkflows/local/isofox_quantification/main.nf:43:36`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          .branch { meta, tumor_aln, tumor_idx ->
                                     ^^^^^^^^^
  ```

- Warning: `subworkflows/local/lilac_calling/main.nf:56:41`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          .branch { meta, normal_dna_aln, normal_dna_idx, tumor_dna_aln, tumor_dna_idx, tumor_rna_aln, tumor_rna_idx, purple_dir ->
                                          ^^^^^^^^^^^^^^
  ```

- Warning: `subworkflows/local/lilac_calling/main.nf:56:72`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          .branch { meta, normal_dna_aln, normal_dna_idx, tumor_dna_aln, tumor_dna_idx, tumor_rna_aln, tumor_rna_idx, purple_dir ->
                                                                         ^^^^^^^^^^^^^
  ```

- Warning: `subworkflows/local/lilac_calling/main.nf:56:87`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          .branch { meta, normal_dna_aln, normal_dna_idx, tumor_dna_aln, tumor_dna_idx, tumor_rna_aln, tumor_rna_idx, purple_dir ->
                                                                                        ^^^^^^^^^^^^^
  ```

- Warning: `subworkflows/local/lilac_calling/main.nf:56:102`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          .branch { meta, normal_dna_aln, normal_dna_idx, tumor_dna_aln, tumor_dna_idx, tumor_rna_aln, tumor_rna_idx, purple_dir ->
                                                                                                       ^^^^^^^^^^^^^
  ```

- Warning: `subworkflows/local/linx_annotation/main.nf:93:25`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          .branch { meta, purple_dir ->
                          ^^^^^^^^^^
  ```

- Warning: `subworkflows/local/linx_plotting/main.nf:44:47`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          .branch { meta, linx_annotations_dir, amber_dir, cobalt_dir, purple_dir ->
                                                ^^^^^^^^^
  ```

- Warning: `subworkflows/local/linx_plotting/main.nf:44:58`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          .branch { meta, linx_annotations_dir, amber_dir, cobalt_dir, purple_dir ->
                                                           ^^^^^^^^^^
  ```

- Warning: `subworkflows/local/linx_plotting/main.nf:44:70`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          .branch { meta, linx_annotations_dir, amber_dir, cobalt_dir, purple_dir ->
                                                                       ^^^^^^^^^^
  ```

- Warning: `subworkflows/local/neo_prediction/main.nf:116:25`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          .branch { meta, neo_finder_dir, tumor_rna_aln, tumor_rna_idx ->
                          ^^^^^^^^^^^^^^
  ```

- Warning: `subworkflows/local/neo_prediction/main.nf:116:41`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          .branch { meta, neo_finder_dir, tumor_rna_aln, tumor_rna_idx ->
                                          ^^^^^^^^^^^^^
  ```

- Warning: `subworkflows/local/neo_prediction/main.nf:116:56`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          .branch { meta, neo_finder_dir, tumor_rna_aln, tumor_rna_idx ->
                                                         ^^^^^^^^^^^^^
  ```

- Warning: `subworkflows/local/neo_prediction/main.nf:194:25`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          .branch { meta, isofox_dir, purple_dir, sage_append_dir_somatic, lilac_dir, neo_finder_dir, annotated_fusions ->
                          ^^^^^^^^^^
  ```

- Warning: `subworkflows/local/neo_prediction/main.nf:194:49`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          .branch { meta, isofox_dir, purple_dir, sage_append_dir_somatic, lilac_dir, neo_finder_dir, annotated_fusions ->
                                                  ^^^^^^^^^^^^^^^^^^^^^^^
  ```

- Warning: `subworkflows/local/neo_prediction/main.nf:194:101`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          .branch { meta, isofox_dir, purple_dir, sage_append_dir_somatic, lilac_dir, neo_finder_dir, annotated_fusions ->
                                                                                                      ^^^^^^^^^^^^^^^^^
  ```

- Warning: `subworkflows/local/pave_annotation/main.nf:48:35`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          .branch { meta, sage_vcf, sage_tbi ->
                                    ^^^^^^^^
  ```

- Warning: `subworkflows/local/pave_annotation/main.nf:101:35`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          .branch { meta, sage_vcf, sage_tbi ->
                                    ^^^^^^^^
  ```

- Warning: `subworkflows/local/prepare_reference/main.nf:229:33`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
                  .filter { meta, dir -> meta.topic_key == params.ref_data_panel_data_path }
                                  ^^^
  ```

- Warning: `subworkflows/local/prepare_reference/main.nf:230:24`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
                  .map { meta, dir -> dir }
                         ^^^^
  ```

- Warning: `subworkflows/local/purple_calling/main.nf:58:48`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          .branch { meta, amber_dir, cobalt_dir, esvee_dir, pave_somatic_dir, pave_germline_dir, redux_tsvs_tumor ->
                                                 ^^^^^^^^^
  ```

- Warning: `subworkflows/local/purple_calling/main.nf:58:59`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          .branch { meta, amber_dir, cobalt_dir, esvee_dir, pave_somatic_dir, pave_germline_dir, redux_tsvs_tumor ->
                                                            ^^^^^^^^^^^^^^^^
  ```

- Warning: `subworkflows/local/purple_calling/main.nf:58:77`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          .branch { meta, amber_dir, cobalt_dir, esvee_dir, pave_somatic_dir, pave_germline_dir, redux_tsvs_tumor ->
                                                                              ^^^^^^^^^^^^^^^^^
  ```

- Warning: `subworkflows/local/purple_calling/main.nf:58:96`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          .branch { meta, amber_dir, cobalt_dir, esvee_dir, pave_somatic_dir, pave_germline_dir, redux_tsvs_tumor ->
                                                                                                 ^^^^^^^^^^^^^^^^
  ```

- Warning: `subworkflows/local/qsee_metrics/main.nf:60:25`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          .branch { meta, redux_tsvs_tumor, redux_tsvs_normal, bamtools_dir_tumor, bamtools_dir_normal, cobalt_dir, esvee_dir, purple_dir ->
                          ^^^^^^^^^^^^^^^^
  ```

- Warning: `subworkflows/local/qsee_metrics/main.nf:60:43`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          .branch { meta, redux_tsvs_tumor, redux_tsvs_normal, bamtools_dir_tumor, bamtools_dir_normal, cobalt_dir, esvee_dir, purple_dir ->
                                            ^^^^^^^^^^^^^^^^^
  ```

- Warning: `subworkflows/local/qsee_metrics/main.nf:60:82`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          .branch { meta, redux_tsvs_tumor, redux_tsvs_normal, bamtools_dir_tumor, bamtools_dir_normal, cobalt_dir, esvee_dir, purple_dir ->
                                                                                   ^^^^^^^^^^^^^^^^^^^
  ```

- Warning: `subworkflows/local/qsee_metrics/main.nf:60:103`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          .branch { meta, redux_tsvs_tumor, redux_tsvs_normal, bamtools_dir_tumor, bamtools_dir_normal, cobalt_dir, esvee_dir, purple_dir ->
                                                                                                        ^^^^^^^^^^
  ```

- Warning: `subworkflows/local/qsee_metrics/main.nf:60:115`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          .branch { meta, redux_tsvs_tumor, redux_tsvs_normal, bamtools_dir_tumor, bamtools_dir_normal, cobalt_dir, esvee_dir, purple_dir ->
                                                                                                                    ^^^^^^^^^
  ```

- Warning: `subworkflows/local/read_alignment_dna/main.nf:196:31`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          .branch { meta_group, alns, idxs ->
                                ^^^^
  ```

- Warning: `subworkflows/local/read_alignment_dna/main.nf:196:37`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          .branch { meta_group, alns, idxs ->
                                      ^^^^
  ```

- Warning: `subworkflows/local/read_alignment_rna/main.nf:26:25`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          .branch { meta, fastq_info, fastq_fwd, fastq_rev ->
                          ^^^^^^^^^^
  ```

- Warning: `subworkflows/local/read_alignment_rna/main.nf:78:18`: Variable was declared but not used

  ```nextflow
              def (meta_group, meta_fastq, fastq_fwd, fastq_rev) = inputs_tuple
                   ^^^^^^^^^^
  ```

- Warning: `subworkflows/local/read_umi_processing/main.nf:103:35`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
              .branch { meta_fastq, fastq_fwd, fastq_rev ->
                                    ^^^^^^^^^
  ```

- Warning: `subworkflows/local/read_umi_processing/main.nf:103:46`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
              .branch { meta_fastq, fastq_fwd, fastq_rev ->
                                               ^^^^^^^^^
  ```

- Warning: `subworkflows/local/read_umi_processing/main.nf:143:35`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
              .branch { meta_fastq, fastq_fwd, fastq_rev ->
                                    ^^^^^^^^^
  ```

- Warning: `subworkflows/local/read_umi_processing/main.nf:143:46`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
              .branch { meta_fastq, fastq_fwd, fastq_rev ->
                                               ^^^^^^^^^
  ```

- Warning: `subworkflows/local/read_umi_processing/main.nf:188:31`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          .branch { meta_fastq, fastq_info, fastq_fwd, fastq_rev ->
                                ^^^^^^^^^^
  ```

- Warning: `subworkflows/local/read_umi_processing/main.nf:188:43`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          .branch { meta_fastq, fastq_info, fastq_fwd, fastq_rev ->
                                            ^^^^^^^^^
  ```

- Warning: `subworkflows/local/read_umi_processing/main.nf:188:54`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          .branch { meta_fastq, fastq_info, fastq_fwd, fastq_rev ->
                                                       ^^^^^^^^^
  ```

- Warning: `subworkflows/local/redux_processing/main.nf:43:31`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          .branch { meta, alns, idxs ->
                                ^^^^
  ```

- Warning: `subworkflows/local/redux_processing/main.nf:58:31`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          .branch { meta, alns, idxs ->
                                ^^^^
  ```

- Warning: `subworkflows/local/redux_processing/main.nf:73:31`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          .branch { meta, alns, idxs ->
                                ^^^^
  ```

- Warning: `subworkflows/local/redux_processing/main.nf:124:31`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          .branch { meta_redux, redux_dir ->
                                ^^^^^^^^^
  ```

- Warning: `subworkflows/local/sage_append/main.nf:59:52`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          .branch { meta, purple_dir, tumor_dna_aln, tumor_dna_idx, redux_tsvs_tumor, tumor_rna_aln, tumor_rna_idx ->
                                                     ^^^^^^^^^^^^^
  ```

- Warning: `subworkflows/local/sage_append/main.nf:59:67`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          .branch { meta, purple_dir, tumor_dna_aln, tumor_dna_idx, redux_tsvs_tumor, tumor_rna_aln, tumor_rna_idx ->
                                                                    ^^^^^^^^^^^^^^^^
  ```

- Warning: `subworkflows/local/sage_append/main.nf:59:100`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          .branch { meta, purple_dir, tumor_dna_aln, tumor_dna_idx, redux_tsvs_tumor, tumor_rna_aln, tumor_rna_idx ->
                                                                                                     ^^^^^^^^^^^^^
  ```

- Warning: `subworkflows/local/sage_append/main.nf:73:37`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          .branch { meta, purple_dir, tumor_dna_aln, tumor_dna_idx, redux_tsvs_tumor, tumor_rna_aln, tumor_rna_idx ->
                                      ^^^^^^^^^^^^^
  ```

- Warning: `subworkflows/local/sage_append/main.nf:73:52`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          .branch { meta, purple_dir, tumor_dna_aln, tumor_dna_idx, redux_tsvs_tumor, tumor_rna_aln, tumor_rna_idx ->
                                                     ^^^^^^^^^^^^^
  ```

- Warning: `subworkflows/local/sage_append/main.nf:73:67`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          .branch { meta, purple_dir, tumor_dna_aln, tumor_dna_idx, redux_tsvs_tumor, tumor_rna_aln, tumor_rna_idx ->
                                                                    ^^^^^^^^^^^^^^^^
  ```

- Warning: `subworkflows/local/sage_append/main.nf:73:85`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          .branch { meta, purple_dir, tumor_dna_aln, tumor_dna_idx, redux_tsvs_tumor, tumor_rna_aln, tumor_rna_idx ->
                                                                                      ^^^^^^^^^^^^^
  ```

- Warning: `subworkflows/local/sage_append/main.nf:73:100`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          .branch { meta, purple_dir, tumor_dna_aln, tumor_dna_idx, redux_tsvs_tumor, tumor_rna_aln, tumor_rna_idx ->
                                                                                                     ^^^^^^^^^^^^^
  ```

- Warning: `subworkflows/local/sage_append/main.nf:138:37`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          .branch { meta, purple_dir, tumor_dna_aln, tumor_dna_idx, redux_tsvs_tumor, tumor_rna_aln, tumor_rna_idx ->
                                      ^^^^^^^^^^^^^
  ```

- Warning: `subworkflows/local/sage_append/main.nf:138:52`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          .branch { meta, purple_dir, tumor_dna_aln, tumor_dna_idx, redux_tsvs_tumor, tumor_rna_aln, tumor_rna_idx ->
                                                     ^^^^^^^^^^^^^
  ```

- Warning: `subworkflows/local/sage_append/main.nf:138:67`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          .branch { meta, purple_dir, tumor_dna_aln, tumor_dna_idx, redux_tsvs_tumor, tumor_rna_aln, tumor_rna_idx ->
                                                                    ^^^^^^^^^^^^^^^^
  ```

- Warning: `subworkflows/local/sage_append/main.nf:138:85`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          .branch { meta, purple_dir, tumor_dna_aln, tumor_dna_idx, redux_tsvs_tumor, tumor_rna_aln, tumor_rna_idx ->
                                                                                      ^^^^^^^^^^^^^
  ```

- Warning: `subworkflows/local/sage_append/main.nf:138:100`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          .branch { meta, purple_dir, tumor_dna_aln, tumor_dna_idx, redux_tsvs_tumor, tumor_rna_aln, tumor_rna_idx ->
                                                                                                     ^^^^^^^^^^^^^
  ```

- Warning: `subworkflows/local/sage_calling/main.nf:25:5`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
      segment_mappability          // channel: [mandatory] /path/to/segment_mappability
      ^^^^^^^^^^^^^^^^^^^
  ```

- Warning: `subworkflows/local/sage_calling/main.nf:63:36`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          .branch { meta, tumor_aln, tumor_idx, normal_aln, normal_idx, donor_aln, donor_idx, redux_tsvs ->
                                     ^^^^^^^^^
  ```

- Warning: `subworkflows/local/sage_calling/main.nf:63:47`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          .branch { meta, tumor_aln, tumor_idx, normal_aln, normal_idx, donor_aln, donor_idx, redux_tsvs ->
                                                ^^^^^^^^^^
  ```

- Warning: `subworkflows/local/sage_calling/main.nf:63:59`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          .branch { meta, tumor_aln, tumor_idx, normal_aln, normal_idx, donor_aln, donor_idx, redux_tsvs ->
                                                            ^^^^^^^^^^
  ```

- Warning: `subworkflows/local/sage_calling/main.nf:63:71`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          .branch { meta, tumor_aln, tumor_idx, normal_aln, normal_idx, donor_aln, donor_idx, redux_tsvs ->
                                                                        ^^^^^^^^^
  ```

- Warning: `subworkflows/local/sage_calling/main.nf:63:82`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          .branch { meta, tumor_aln, tumor_idx, normal_aln, normal_idx, donor_aln, donor_idx, redux_tsvs ->
                                                                                   ^^^^^^^^^
  ```

- Warning: `subworkflows/local/sage_calling/main.nf:63:93`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          .branch { meta, tumor_aln, tumor_idx, normal_aln, normal_idx, donor_aln, donor_idx, redux_tsvs ->
                                                                                              ^^^^^^^^^^
  ```

- Warning: `subworkflows/local/sage_calling/main.nf:76:36`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          .branch { meta, tumor_aln, tumor_idx, normal_aln, normal_idx, donor_aln, donor_idx, redux_tsvs ->
                                     ^^^^^^^^^
  ```

- Warning: `subworkflows/local/sage_calling/main.nf:76:59`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          .branch { meta, tumor_aln, tumor_idx, normal_aln, normal_idx, donor_aln, donor_idx, redux_tsvs ->
                                                            ^^^^^^^^^^
  ```

- Warning: `subworkflows/local/sage_calling/main.nf:76:71`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          .branch { meta, tumor_aln, tumor_idx, normal_aln, normal_idx, donor_aln, donor_idx, redux_tsvs ->
                                                                        ^^^^^^^^^
  ```

- Warning: `subworkflows/local/sage_calling/main.nf:76:82`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          .branch { meta, tumor_aln, tumor_idx, normal_aln, normal_idx, donor_aln, donor_idx, redux_tsvs ->
                                                                                   ^^^^^^^^^
  ```

- Warning: `subworkflows/local/sage_calling/main.nf:76:93`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          .branch { meta, tumor_aln, tumor_idx, normal_aln, normal_idx, donor_aln, donor_idx, redux_tsvs ->
                                                                                              ^^^^^^^^^^
  ```

- Warning: `subworkflows/local/sage_calling/main.nf:122:36`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          .branch { meta, tumor_aln, tumor_idx, normal_aln, normal_idx, donor_aln, donor_idx, redux_tsvs ->
                                     ^^^^^^^^^
  ```

- Warning: `subworkflows/local/sage_calling/main.nf:122:47`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          .branch { meta, tumor_aln, tumor_idx, normal_aln, normal_idx, donor_aln, donor_idx, redux_tsvs ->
                                                ^^^^^^^^^^
  ```

- Warning: `subworkflows/local/sage_calling/main.nf:122:59`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          .branch { meta, tumor_aln, tumor_idx, normal_aln, normal_idx, donor_aln, donor_idx, redux_tsvs ->
                                                            ^^^^^^^^^^
  ```

- Warning: `subworkflows/local/sage_calling/main.nf:122:71`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          .branch { meta, tumor_aln, tumor_idx, normal_aln, normal_idx, donor_aln, donor_idx, redux_tsvs ->
                                                                        ^^^^^^^^^
  ```

- Warning: `subworkflows/local/sage_calling/main.nf:122:82`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          .branch { meta, tumor_aln, tumor_idx, normal_aln, normal_idx, donor_aln, donor_idx, redux_tsvs ->
                                                                                   ^^^^^^^^^
  ```

- Warning: `subworkflows/local/sage_calling/main.nf:122:93`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          .branch { meta, tumor_aln, tumor_idx, normal_aln, normal_idx, donor_aln, donor_idx, redux_tsvs ->
                                                                                              ^^^^^^^^^^
  ```

- Warning: `subworkflows/local/sage_plotting/main.nf:67:36`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          .branch { meta, tumor_aln, tumor_idx, normal_aln, normal_idx, donor_aln, donor_idx, redux_tsvs, purple_dir ->
                                     ^^^^^^^^^
  ```

- Warning: `subworkflows/local/sage_plotting/main.nf:67:47`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          .branch { meta, tumor_aln, tumor_idx, normal_aln, normal_idx, donor_aln, donor_idx, redux_tsvs, purple_dir ->
                                                ^^^^^^^^^^
  ```

- Warning: `subworkflows/local/sage_plotting/main.nf:67:59`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          .branch { meta, tumor_aln, tumor_idx, normal_aln, normal_idx, donor_aln, donor_idx, redux_tsvs, purple_dir ->
                                                            ^^^^^^^^^^
  ```

- Warning: `subworkflows/local/sage_plotting/main.nf:67:71`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          .branch { meta, tumor_aln, tumor_idx, normal_aln, normal_idx, donor_aln, donor_idx, redux_tsvs, purple_dir ->
                                                                        ^^^^^^^^^
  ```

- Warning: `subworkflows/local/sage_plotting/main.nf:67:82`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          .branch { meta, tumor_aln, tumor_idx, normal_aln, normal_idx, donor_aln, donor_idx, redux_tsvs, purple_dir ->
                                                                                   ^^^^^^^^^
  ```

- Warning: `subworkflows/local/sage_plotting/main.nf:67:93`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          .branch { meta, tumor_aln, tumor_idx, normal_aln, normal_idx, donor_aln, donor_idx, redux_tsvs, purple_dir ->
                                                                                              ^^^^^^^^^^
  ```

- Warning: `subworkflows/local/teal_characterisation/main.nf:49:36`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          .branch { meta, tumor_aln, tumor_idx, normal_aln, normal_idx ->
                                     ^^^^^^^^^
  ```

- Warning: `subworkflows/local/teal_characterisation/main.nf:49:59`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          .branch { meta, tumor_aln, tumor_idx, normal_aln, normal_idx ->
                                                            ^^^^^^^^^^
  ```

- Warning: `subworkflows/local/teal_characterisation/main.nf:131:41`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          .branch { meta, teal_bam_tumor, teal_bai_tumor, teal_bam_normal, teal_bai_normal, bamtools_dir_tumor, bamtools_dir_normal, cobalt_dir, purple_dir ->
                                          ^^^^^^^^^^^^^^
  ```

- Warning: `subworkflows/local/teal_characterisation/main.nf:131:74`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          .branch { meta, teal_bam_tumor, teal_bai_tumor, teal_bam_normal, teal_bai_normal, bamtools_dir_tumor, bamtools_dir_normal, cobalt_dir, purple_dir ->
                                                                           ^^^^^^^^^^^^^^^
  ```

- Warning: `subworkflows/local/utils_nfcore_oncoanalyser_pipeline/main.nf:34:5`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
      input             //  string: Path to input samplesheet
      ^^^^^
  ```

- Warning: `subworkflows/local/virusbreakend_calling/main.nf:45:36`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          .branch { meta, tumor_aln, tumor_idx ->
                                     ^^^^^^^^^
  ```

- Warning: `subworkflows/local/wisp_analysis/main.nf:10:5`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
      ch_inputs                  // channel: [mandatory] [ meta ]
      ^^^^^^^^^
  ```

- Warning: `subworkflows/local/wisp_analysis/main.nf:54:45`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          .branch { meta, primary_purple_dir, primary_amber_dir, primary_normal_aln, longitudinal_redux_dir, longitudinal_amber_dir, longitudinal_cobalt_dir, longitudinal_sage_append_dir ->
                                              ^^^^^^^^^^^^^^^^^
  ```

- Warning: `subworkflows/local/wisp_analysis/main.nf:54:64`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          .branch { meta, primary_purple_dir, primary_amber_dir, primary_normal_aln, longitudinal_redux_dir, longitudinal_amber_dir, longitudinal_cobalt_dir, longitudinal_sage_append_dir ->
                                                                 ^^^^^^^^^^^^^^^^^^
  ```

- Warning: `subworkflows/local/wisp_analysis/main.nf:54:84`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          .branch { meta, primary_purple_dir, primary_amber_dir, primary_normal_aln, longitudinal_redux_dir, longitudinal_amber_dir, longitudinal_cobalt_dir, longitudinal_sage_append_dir ->
                                                                                     ^^^^^^^^^^^^^^^^^^^^^^
  ```

- Warning: `subworkflows/local/wisp_analysis/main.nf:54:108`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          .branch { meta, primary_purple_dir, primary_amber_dir, primary_normal_aln, longitudinal_redux_dir, longitudinal_amber_dir, longitudinal_cobalt_dir, longitudinal_sage_append_dir ->
                                                                                                             ^^^^^^^^^^^^^^^^^^^^^^
  ```

- Warning: `tests/nextflow.config:12:48`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
      def present = vars.findAll { System.getenv(it) }
                                                 ^^
  ```
