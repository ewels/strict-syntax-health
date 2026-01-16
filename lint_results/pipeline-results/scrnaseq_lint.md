# Nextflow lint results

- Generated: 2026-01-16T06:40:41.598739552Z
- Nextflow version: 25.12.0-edge
- Summary: 22 errors, 111 warnings

## :x: Errors

- Error: `modules/local/parse_cellrangermulti_samplesheet.nf:8:5`: Invalid process directive

  ```nextflow
      publishDir = [ enabled: false ]
      ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  ```

- Error: `modules/nf-core/cellranger/count/main.nf:32:9`: `prefix` is already declared

  ```nextflow
      def prefix = task.ext.prefix ?: "${meta.id}"
          ^^^^^^
  ```

- Error: `modules/nf-core/cellranger/multi/main.nf:126:46`: `meta_fb` is not defined

  ```nextflow
      fb_options_r1_length = fb_options_use && meta_fb.options.containsKey("r1-length") ? "r1-length,${meta_fb.options["r1-length"]}" : ''
                                               ^^^^^^^
  ```

- Error: `modules/nf-core/cellranger/multi/main.nf:126:102`: `meta_fb` is not defined

  ```nextflow
      fb_options_r1_length = fb_options_use && meta_fb.options.containsKey("r1-length") ? "r1-length,${meta_fb.options["r1-length"]}" : ''
                                                                                                       ^^^^^^^
  ```

- Error: `modules/nf-core/cellranger/multi/main.nf:127:46`: `meta_fb` is not defined

  ```nextflow
      fb_options_r2_length = fb_options_use && meta_fb.options.containsKey("r2-length") ? "r2-length,${meta_fb.options["r2-length"]}" : ''
                                               ^^^^^^^
  ```

- Error: `modules/nf-core/cellranger/multi/main.nf:127:102`: `meta_fb` is not defined

  ```nextflow
      fb_options_r2_length = fb_options_use && meta_fb.options.containsKey("r2-length") ? "r2-length,${meta_fb.options["r2-length"]}" : ''
                                                                                                       ^^^^^^^
  ```

- Error: `modules/nf-core/cellrangerarc/count/main.nf:8:5`: Invalid process directive

  ```nextflow
      if (workflow.profile.tokenize(',').intersect(['conda', 'mamba']).size() >= 1) {
      ^
  ```

- Error: `modules/nf-core/cellrangerarc/mkgtf/main.nf:8:5`: Invalid process directive

  ```nextflow
      if (workflow.profile.tokenize(',').intersect(['conda', 'mamba']).size() >= 1) {
      ^
  ```

- Error: `modules/nf-core/cellrangerarc/mkref/main.nf:8:5`: Invalid process directive

  ```nextflow
      if (workflow.profile.tokenize(',').intersect(['conda', 'mamba']).size() >= 1) {
      ^
  ```

- Error: `modules/nf-core/cellrangerarc/mkref/main.nf:31:9`: `reference_config` is already declared

  ```nextflow
      def reference_config = reference_config.name
          ^^^^^^^^^^^^^^^^
  ```

- Error: `nextflow.config:231:28`: Invalid include source: '/home/runner/work/strict-syntax-health/strict-syntax-health/pipelines/scrnaseq/conf/test_multiome.config'

  ```nextflow
      test_multiome        { includeConfig 'conf/test_multiome.config'         }
                             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  ```

- Error: `subworkflows/local/align_cellrangermulti.nf:150:34`: Unexpected input: '='

  ```nextflow
                      while ((line = reader.readLine()) != null) {
                                   ^
  ```

- Error: `subworkflows/local/kallisto_bustools.nf:8:1`: Statements cannot be mixed with script declarations -- move statements into a process, workflow, or function

  ```nextflow
  def multiqc_report    = []
  ^^^^^^^^^^^^^^^^^^^^^^^^^^
  ```

- Error: `subworkflows/local/utils_nfcore_scrnaseq_pipeline/main.nf:238:5`: `cellranger_multi_barcodes` was assigned but not declared

  ```nextflow
      cellranger_multi_barcodes = file(params.cellranger_multi_barcodes).splitCsv(header: true)
      ^^^^^^^^^^^^^^^^^^^^^^^^^
  ```

- Error: `subworkflows/local/utils_nfcore_scrnaseq_pipeline/main.nf:248:5`: `cellranger_multi_barcodes` is not defined

  ```nextflow
      cellranger_multi_barcodes.eachWithIndex { row, idx ->
      ^^^^^^^^^^^^^^^^^^^^^^^^^
  ```

- Error: `workflows/scrnaseq.nf:17:1`: Module could not be parsed: '/home/runner/work/strict-syntax-health/strict-syntax-health/pipelines/scrnaseq/subworkflows/local/align_cellrangermulti.nf'

  ```nextflow
  include { CELLRANGER_MULTI_ALIGN                            } from "../subworkflows/local/align_cellrangermulti"
  ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  ```

- Error: `workflows/scrnaseq.nf:37:23`: `Utils` is not defined

  ```nextflow
      protocol_config = Utils.getProtocol(workflow, log, params.aligner, params.protocol)
                        ^^^^^
  ```

- Error: `workflows/scrnaseq.nf:264:9`: `CELLRANGER_MULTI_ALIGN` is not defined

  ```nextflow
          CELLRANGER_MULTI_ALIGN(
          ^^^^^^^^^^^^^^^^^^^^^^
  ```

- Error: `workflows/scrnaseq.nf:272:39`: `CELLRANGER_MULTI_ALIGN` is not defined

  ```nextflow
          ch_versions = ch_versions.mix(CELLRANGER_MULTI_ALIGN.out.ch_versions)
                                        ^^^^^^^^^^^^^^^^^^^^^^
  ```

- Error: `workflows/scrnaseq.nf:273:50`: `CELLRANGER_MULTI_ALIGN` is not defined

  ```nextflow
          ch_multiqc_files = ch_multiqc_files.mix( CELLRANGER_MULTI_ALIGN.out.cellrangermulti_out.map{
                                                   ^^^^^^^^^^^^^^^^^^^^^^
  ```

- Error: `workflows/scrnaseq.nf:276:48`: `CELLRANGER_MULTI_ALIGN` is not defined

  ```nextflow
          ch_mtx_matrices = ch_mtx_matrices.mix( CELLRANGER_MULTI_ALIGN.out.cellrangermulti_mtx_raw, CELLRANGER_MULTI_ALIGN.out.cellrangermulti_mtx_filtered )
                                                 ^^^^^^^^^^^^^^^^^^^^^^
  ```

- Error: `workflows/scrnaseq.nf:276:100`: `CELLRANGER_MULTI_ALIGN` is not defined

  ```nextflow
          ch_mtx_matrices = ch_mtx_matrices.mix( CELLRANGER_MULTI_ALIGN.out.cellrangermulti_mtx_raw, CELLRANGER_MULTI_ALIGN.out.cellrangermulti_mtx_filtered )
                                                                                                     ^^^^^^^^^^^^^^^^^^^^^^
  ```

## :warning: Warnings

- Warning: `conf/modules.config:160:25`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
              saveAs: { (!it.endsWith('.bam') || params.save_align_intermeds) ? it : null }
                          ^^
  ```

- Warning: `conf/modules.config:160:79`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
              saveAs: { (!it.endsWith('.bam') || params.save_align_intermeds) ? it : null }
                                                                                ^^
  ```

- Warning: `modules/nf-core/cellranger/count/main.nf:23:5`: Variable was declared but not used

  ```nextflow
      args = task.ext.args ?: ''
      ^^^^
  ```

- Warning: `modules/nf-core/cellranger/count/main.nf:24:5`: Variable was declared but not used

  ```nextflow
      prefix = task.ext.prefix ?: "${meta.id}"
      ^^^^^^
  ```

- Warning: `modules/nf-core/cellranger/mkgtf/main.nf:42:9`: Variable was declared but not used

  ```nextflow
      def args = task.ext.args ?: ''
          ^^^^
  ```

- Warning: `modules/nf-core/cellranger/mkref/main.nf:50:9`: Variable was declared but not used

  ```nextflow
      def args = task.ext.args ?: ''
          ^^^^
  ```

- Warning: `modules/nf-core/cellranger/multi/main.nf:44:63`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
      if ([ocm_barcodes, cmo_barcodes, frna_sampleinfo].count { it } >= 2) {
                                                                ^^
  ```

- Warning: `modules/nf-core/cellranger/multi/main.nf:47:5`: Variable was declared but not used

  ```nextflow
      args   = task.ext.args   ?: ''
      ^^^^
  ```

- Warning: `modules/nf-core/cellranger/multi/main.nf:71:5`: Variable was declared but not used

  ```nextflow
      gex_reference_path = include_gex ? "reference,./${gex_reference_name}" : ''
      ^^^^^^^^^^^^^^^^^^
  ```

- Warning: `modules/nf-core/cellranger/multi/main.nf:72:5`: Variable was declared but not used

  ```nextflow
      fb_reference_path  = include_fb  ? "reference,./${fb_reference_name}"  : ''
      ^^^^^^^^^^^^^^^^^
  ```

- Warning: `modules/nf-core/cellranger/multi/main.nf:73:5`: Variable was declared but not used

  ```nextflow
      vdj_reference_path = include_vdj ? "reference,./${vdj_reference_name}" : ''
      ^^^^^^^^^^^^^^^^^^
  ```

- Warning: `modules/nf-core/cellranger/multi/main.nf:76:5`: Variable was declared but not used

  ```nextflow
      target_panel = gex_targetpanel_name != '' ? "target-panel,./$gex_targetpanel_name" : ''
      ^^^^^^^^^^^^
  ```

- Warning: `modules/nf-core/cellranger/multi/main.nf:79:5`: Variable was declared but not used

  ```nextflow
      frna_probeset = include_frna && gex_frna_probeset_name != '' ? "probe-set,./$gex_frna_probeset_name" : ''
      ^^^^^^^^^^^^^
  ```

- Warning: `modules/nf-core/cellranger/multi/main.nf:82:5`: Variable was declared but not used

  ```nextflow
      primer_index = vdj_primer_index ? "inner-enrichment-primers,./references/primers/${vdj_primer_index.getName()}" : ''
      ^^^^^^^^^^^^
  ```

- Warning: `modules/nf-core/cellranger/multi/main.nf:85:5`: Variable was declared but not used

  ```nextflow
      beam_antigen_csv = include_beam && beam_antigen_panel_name != '' ? "reference,./$beam_antigen_panel_name" : ''
      ^^^^^^^^^^^^^^^^
  ```

- Warning: `modules/nf-core/cellranger/multi/main.nf:89:5`: Variable was declared but not used

  ```nextflow
      beam_csv_text  = include_beam && beam_control_panel.size() > 0 ? beam_control_panel : ''
      ^^^^^^^^^^^^^
  ```

- Warning: `modules/nf-core/cellranger/multi/main.nf:90:5`: Variable was declared but not used

  ```nextflow
      cmo_csv_text   = include_cmo  && cmo_barcodes.size() > 0       ? cmo_barcodes       : ''
      ^^^^^^^^^^^^
  ```

- Warning: `modules/nf-core/cellranger/multi/main.nf:91:5`: Variable was declared but not used

  ```nextflow
      ocm_csv_text   = include_ocm  && ocm_barcodes.size() > 0       ? ocm_barcodes       : ''
      ^^^^^^^^^^^^
  ```

- Warning: `modules/nf-core/cellranger/multi/main.nf:92:5`: Variable was declared but not used

  ```nextflow
      frna_csv_text  = include_frna && frna_sampleinfo.size() > 0    ? frna_sampleinfo    : ''
      ^^^^^^^^^^^^^
  ```

- Warning: `modules/nf-core/cellranger/multi/main.nf:102:5`: Variable was declared but not used

  ```nextflow
      beam_options_use   = include_beam && meta_beam?.options ? 'true' : null
      ^^^^^^^^^^^^^^^^
  ```

- Warning: `modules/nf-core/cellranger/multi/main.nf:107:5`: Variable was declared but not used

  ```nextflow
      gex_options_filter_probes = gex_options_use && meta_gex.options.containsKey("filter-probes") ? "filter-probes,${meta_gex.options["filter-probes"]}" : ''
      ^^^^^^^^^^^^^^^^^^^^^^^^^
  ```

- Warning: `modules/nf-core/cellranger/multi/main.nf:108:5`: Variable was declared but not used

  ```nextflow
      gex_options_r1_length     = gex_options_use && meta_gex.options.containsKey("r1-length")     ? "r1-length,${meta_gex.options["r1-length"]}"         : ''
      ^^^^^^^^^^^^^^^^^^^^^
  ```

- Warning: `modules/nf-core/cellranger/multi/main.nf:109:5`: Variable was declared but not used

  ```nextflow
      gex_options_r2_length     = gex_options_use && meta_gex.options.containsKey("r2-length")     ? "r2-length,${meta_gex.options["r2-length"]}"         : ''
      ^^^^^^^^^^^^^^^^^^^^^
  ```

- Warning: `modules/nf-core/cellranger/multi/main.nf:110:5`: Variable was declared but not used

  ```nextflow
      gex_options_chemistry     = gex_options_use && meta_gex.options.containsKey("chemistry")     ? "chemistry,${meta_gex.options["chemistry"]}"         : ''
      ^^^^^^^^^^^^^^^^^^^^^
  ```

- Warning: `modules/nf-core/cellranger/multi/main.nf:111:5`: Variable was declared but not used

  ```nextflow
      gex_options_expect_cells  = gex_options_use && meta_gex.options.containsKey("expect-cells")  ? "expect-cells,${meta_gex.options["expect-cells"]}"   : ''
      ^^^^^^^^^^^^^^^^^^^^^^^^
  ```

- Warning: `modules/nf-core/cellranger/multi/main.nf:112:5`: Variable was declared but not used

  ```nextflow
      gex_options_force_cells   = gex_options_use && meta_gex.options.containsKey("force-cells")   ? "force-cells,${meta_gex.options["force-cells"]}"     : ''
      ^^^^^^^^^^^^^^^^^^^^^^^
  ```

- Warning: `modules/nf-core/cellranger/multi/main.nf:113:5`: Variable was declared but not used

  ```nextflow
      gex_options_no_secondary  = gex_options_use && meta_gex.options.containsKey("no-secondary")  ? "no-secondary,${meta_gex.options["no-secondary"]}"   : ''
      ^^^^^^^^^^^^^^^^^^^^^^^^
  ```

- Warning: `modules/nf-core/cellranger/multi/main.nf:114:5`: Variable was declared but not used

  ```nextflow
      gex_options_no_bam        = gex_options_use && meta_gex.options.containsKey("create-bam")    ? "create-bam,${meta_gex.options["create-bam"]}"           : ''
      ^^^^^^^^^^^^^^^^^^
  ```

- Warning: `modules/nf-core/cellranger/multi/main.nf:115:5`: Variable was declared but not used

  ```nextflow
      gex_options_no_target_umi_filter = gex_options_use && meta_gex.options.containsKey("no-target-umi-filter") ? "no-target-umi-filter,${meta_gex.options["no-target-umi-filter"]}" : ''
      ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  ```

- Warning: `modules/nf-core/cellranger/multi/main.nf:116:5`: Variable was declared but not used

  ```nextflow
      gex_options_include_introns      = gex_options_use && meta_gex.options.containsKey("include-introns")      ? "include-introns,${meta_gex.options["include-introns"]}"           : ''
      ^^^^^^^^^^^^^^^^^^^^^^^^^^^
  ```

- Warning: `modules/nf-core/cellranger/multi/main.nf:117:5`: Variable was declared but not used

  ```nextflow
      gex_options_check_library_compatibility = gex_options_use && meta_gex.options.containsKey("check-library-compatibility") ? "check-library-compatibility,${meta_gex.options["check-library-compatibility"]}" : ''
      ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  ```

- Warning: `modules/nf-core/cellranger/multi/main.nf:119:5`: Variable was declared but not used

  ```nextflow
      cmo_reference_path = cmo_options_use && cmo_reference_name    ? "cmo-set,./${cmo_reference_name}"                      : ''
      ^^^^^^^^^^^^^^^^^^
  ```

- Warning: `modules/nf-core/cellranger/multi/main.nf:120:5`: Variable was declared but not used

  ```nextflow
      cmo_barcode_path   = cmo_options_use && cmo_sample_assignment ? "barcode-sample-assignment,./${cmo_sample_assignment}" : ''
      ^^^^^^^^^^^^^^^^
  ```

- Warning: `modules/nf-core/cellranger/multi/main.nf:121:5`: Variable was declared but not used

  ```nextflow
      cmo_options_min_assignment_confidence = cmo_options_use && meta_cmo.options.containsKey("min-assignment-confidence") ? "min-assignment-confidence,${meta_cmo.options["min-assignment-confidence"]}" : ''
      ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  ```

- Warning: `modules/nf-core/cellranger/multi/main.nf:123:5`: Variable was declared but not used

  ```nextflow
      vdj_options_r1_length = vdj_options_use && meta_vdj.options.containsKey("r1-length") ? "r1-length,${meta_vdj.options["r1-length"]}" : ''
      ^^^^^^^^^^^^^^^^^^^^^
  ```

- Warning: `modules/nf-core/cellranger/multi/main.nf:124:5`: Variable was declared but not used

  ```nextflow
      vdj_options_r2_length = vdj_options_use && meta_vdj.options.containsKey("r2-length") ? "r2-length,${meta_vdj.options["r2-length"]}" : ''
      ^^^^^^^^^^^^^^^^^^^^^
  ```

- Warning: `modules/nf-core/cellranger/multi/main.nf:126:5`: Variable was declared but not used

  ```nextflow
      fb_options_r1_length = fb_options_use && meta_fb.options.containsKey("r1-length") ? "r1-length,${meta_fb.options["r1-length"]}" : ''
      ^^^^^^^^^^^^^^^^^^^^
  ```

- Warning: `modules/nf-core/cellranger/multi/main.nf:127:5`: Variable was declared but not used

  ```nextflow
      fb_options_r2_length = fb_options_use && meta_fb.options.containsKey("r2-length") ? "r2-length,${meta_fb.options["r2-length"]}" : ''
      ^^^^^^^^^^^^^^^^^^^^
  ```

- Warning: `modules/nf-core/cellranger/multi/main.nf:131:5`: Variable was declared but not used

  ```nextflow
      fastq_gex      = include_gex                      ? "${meta_gex.id},./fastq_all/gex,,Gene Expression"            : ''
      ^^^^^^^^^
  ```

- Warning: `modules/nf-core/cellranger/multi/main.nf:132:5`: Variable was declared but not used

  ```nextflow
      fastq_vdj      = include_vdj                      ? "${meta_vdj.id},./fastq_all/vdj,,VDJ"                        : ''
      ^^^^^^^^^
  ```

- Warning: `modules/nf-core/cellranger/multi/main.nf:133:5`: Variable was declared but not used

  ```nextflow
      fastq_antibody = include_fb && ab_options_use     ? "${meta_ab.id},./fastq_all/ab,,Antibody Capture"             : ''
      ^^^^^^^^^^^^^^
  ```

- Warning: `modules/nf-core/cellranger/multi/main.nf:134:5`: Variable was declared but not used

  ```nextflow
      fastq_beam     = include_beam                     ? "${meta_beam.id},./fastq_all/beam,,Antigen Capture"         : ''
      ^^^^^^^^^^
  ```

- Warning: `modules/nf-core/cellranger/multi/main.nf:135:5`: Variable was declared but not used

  ```nextflow
      fastq_crispr   = include_fb && crispr_options_use ? "${meta_crispr.id},./fastq_all/crispr,,CRISPR Guide Capture" : ''
      ^^^^^^^^^^^^
  ```

- Warning: `modules/nf-core/cellranger/multi/main.nf:136:5`: Variable was declared but not used

  ```nextflow
      fastq_cmo      = include_cmo                      ? "${meta_cmo.id},./fastq_all/cmo,,Multiplexing Capture"       : ''
      ^^^^^^^^^
  ```

- Warning: `modules/nf-core/cellranger/multi/main.nf:139:5`: Variable was declared but not used

  ```nextflow
      config = "cellranger_multi_config.csv"
      ^^^^^^
  ```

- Warning: `modules/nf-core/gunzip/main.nf:43:9`: Variable was declared but not used

  ```nextflow
      def args        = task.ext.args ?: ''
          ^^^^
  ```

- Warning: `modules/nf-core/kallistobustools/ref/main.nf:28:9`: Variable was declared but not used

  ```nextflow
      def args = task.ext.args ?: ''
          ^^^^
  ```

- Warning: `modules/nf-core/unzip/main.nf:38:9`: Variable was declared but not used

  ```nextflow
      def args = task.ext.args ?: ''
          ^^^^
  ```

- Warning: `subworkflows/local/align_cellranger.nf:19:23`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
          ch_versions = Channel.empty()
                        ^^^^^^^
  ```

- Warning: `subworkflows/local/align_cellranger.nf:50:22`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
                  if ( it.toString().contains("raw_feature_bc_matrix") ) { desired_files.add( it ) }
                       ^^
  ```

- Warning: `subworkflows/local/align_cellranger.nf:50:93`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
                  if ( it.toString().contains("raw_feature_bc_matrix") ) { desired_files.add( it ) }
                                                                                              ^^
  ```

- Warning: `subworkflows/local/align_cellranger.nf:59:22`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
                  if ( it.toString().contains("filtered_feature_bc_matrix") ) { desired_files.add( it ) }
                       ^^
  ```

- Warning: `subworkflows/local/align_cellranger.nf:59:98`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
                  if ( it.toString().contains("filtered_feature_bc_matrix") ) { desired_files.add( it ) }
                                                                                                   ^^
  ```

- Warning: `subworkflows/local/align_cellrangerarc.nf:20:23`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
          ch_versions = Channel.empty()
                        ^^^^^^^
  ```

- Warning: `subworkflows/local/align_cellrangerarc.nf:73:30`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          mtx_files.each{ if ( it.toString().contains("${pattern}") ) { desired_files.add( it ) } }
                               ^^
  ```

- Warning: `subworkflows/local/align_cellrangerarc.nf:73:90`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          mtx_files.each{ if ( it.toString().contains("${pattern}") ) { desired_files.add( it ) } }
                                                                                           ^^
  ```

- Warning: `subworkflows/local/fastqc.nf:29:22`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      fastqc_multiqc = Channel.empty()
                       ^^^^^^^
  ```

- Warning: `subworkflows/local/h5ad_conversion.nf:13:19`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_versions = Channel.empty()
                    ^^^^^^^
  ```

- Warning: `subworkflows/local/kallisto_bustools.nf:8:5`: Variable was declared but not used

  ```nextflow
  def multiqc_report    = []
      ^^^^^^^^^^^^^^
  ```

- Warning: `subworkflows/local/kallisto_bustools.nf:23:19`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_versions = Channel.empty()
                    ^^^^^^^
  ```

- Warning: `subworkflows/local/simpleaf.nf:21:19`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_versions = Channel.empty()
                    ^^^^^^^
  ```

- Warning: `subworkflows/local/simpleaf.nf:61:28`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
                  txp2gene = Channel.of( txp2gene )
                             ^^^^^^^
  ```

- Warning: `subworkflows/local/simpleaf.nf:65:30`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
              simpleaf_index = Channel.of( [ [:], [] ] )
                               ^^^^^^^
  ```

- Warning: `subworkflows/local/simpleaf.nf:70:26`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
          simpleaf_index = Channel.of( [ [ id: simpleaf_index.getName() ], simpleaf_index ] )
                           ^^^^^^^
  ```

- Warning: `subworkflows/local/simpleaf.nf:74:24`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
              txp2gene = Channel.of( txp2gene )
                         ^^^^^^^
  ```

- Warning: `subworkflows/local/starsolo.nf:22:19`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_versions = Channel.empty()
                    ^^^^^^^
  ```

- Warning: `subworkflows/local/starsolo.nf:76:53`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
      for_multiqc     = STAR_ALIGN.out.log_final.map{ meta, it -> it }
                                                      ^^^^
  ```

- Warning: `subworkflows/local/utils_nfcore_scrnaseq_pipeline/main.nf:32:5`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
      monochrome_logs   // boolean: Do not use coloured log outputs
      ^^^^^^^^^^^^^^^
  ```

- Warning: `subworkflows/local/utils_nfcore_scrnaseq_pipeline/main.nf:35:5`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
      input             //  string: Path to input samplesheet
      ^^^^^
  ```

- Warning: `subworkflows/local/utils_nfcore_scrnaseq_pipeline/main.nf:42:19`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_versions = Channel.empty()
                    ^^^^^^^
  ```

- Warning: `subworkflows/local/utils_nfcore_scrnaseq_pipeline/main.nf:67:144`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
      after_text = """${workflow.manifest.doi ? "\n* The pipeline\n" : ""}${workflow.manifest.doi.tokenize(",").collect { "    https://doi.org/${it.trim().replace('https://doi.org/','')}"}.join("\n")}${workflow.manifest.doi ? "\n" : ""}
                                                                                                                                                 ^^
  ```

- Warning: `subworkflows/local/utils_nfcore_scrnaseq_pipeline/main.nf:104:9`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
          Channel
          ^^^^^^^
  ```

- Warning: `subworkflows/local/utils_nfcore_scrnaseq_pipeline/main.nf:115:23`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
              .map{ id, type, meta, reads -> [ id, meta, reads ] }
                        ^^^^
  ```

- Warning: `subworkflows/local/utils_nfcore_scrnaseq_pipeline/main.nf:117:42`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
                  validateInputSamplesheet(it)
                                           ^^
  ```

- Warning: `subworkflows/local/utils_nfcore_scrnaseq_pipeline/main.nf:125:9`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
          Channel
          ^^^^^^^
  ```

- Warning: `subworkflows/local/utils_nfcore_scrnaseq_pipeline/main.nf:139:40`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
                  cellrangerarcStructure(it)
                                         ^^
  ```

- Warning: `subworkflows/local/utils_nfcore_scrnaseq_pipeline/main.nf:143:9`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
          Channel
          ^^^^^^^
  ```

- Warning: `subworkflows/local/utils_nfcore_scrnaseq_pipeline/main.nf:155:42`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
                  validateInputSamplesheet(it)
                                           ^^
  ```

- Warning: `subworkflows/local/utils_nfcore_scrnaseq_pipeline/main.nf:241:76`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
      def inputSamples = file(params.input).splitCsv(header: true).collect { it.sample }.toSet()
                                                                             ^^
  ```

- Warning: `subworkflows/local/utils_nfcore_scrnaseq_pipeline/main.nf:268:65`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          def errorDetails = rowsWithoutBarcodes.collect { "row ${it.row} (${it.multiplexed_sample_id})" }.join(', ')
                                                                  ^^
  ```

- Warning: `subworkflows/local/utils_nfcore_scrnaseq_pipeline/main.nf:268:76`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          def errorDetails = rowsWithoutBarcodes.collect { "row ${it.row} (${it.multiplexed_sample_id})" }.join(', ')
                                                                             ^^
  ```

- Warning: `subworkflows/local/utils_nfcore_scrnaseq_pipeline/main.nf:275:65`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
      def samplesWithMixedBarcodes = sampleBarcodeTypes.findAll { multiplexed_sample_id, info -> info.types.size() > 1 }
                                                                  ^^^^^^^^^^^^^^^^^^^^^
  ```

- Warning: `subworkflows/local/utils_nfcore_scrnaseq_pipeline/main.nf:321:86`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
      def sample_type_ok = metas.collect { meta -> meta.sample_type }.unique().every { it in valid_sample_types }
                                                                                       ^^
  ```

- Warning: `subworkflows/nf-core/h5ad_removebackground_barcodes_cellbender_anndata/main.nf:13:19`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_versions = Channel.empty()
                    ^^^^^^^
  ```

- Warning: `subworkflows/nf-core/utils_nfcore_pipeline/main.nf:101:98`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      return ch_versions.unique().map { version -> processVersionsFromYAML(version) }.unique().mix(Channel.of(workflowVersionToYAML()))
                                                                                                   ^^^^^^^
  ```

- Warning: `workflows/scrnaseq.nf:33:24`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_multiqc_files = Channel.empty()
                         ^^^^^^^
  ```

- Warning: `workflows/scrnaseq.nf:34:24`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_versions      = Channel.empty()
                         ^^^^^^^
  ```

- Warning: `workflows/scrnaseq.nf:35:24`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_mtx_matrices  = Channel.empty()
                         ^^^^^^^
  ```

- Warning: `workflows/scrnaseq.nf:71:38`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_star_index     = star_index ? Channel.value( [[id: star_index.baseName], star_index] ) : []
                                       ^^^^^^^
  ```

- Warning: `workflows/scrnaseq.nf:96:89`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
              ch_genome_fasta    = GUNZIP_FASTA ( [ [:], ch_genome_fasta ] ).gunzip.map { it[1] }
                                                                                          ^^
  ```

- Warning: `workflows/scrnaseq.nf:99:31`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
              ch_genome_fasta = Channel.value( ch_genome_fasta )
                                ^^^^^^^
  ```

- Warning: `workflows/scrnaseq.nf:108:71`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
              ch_gtf      = GUNZIP_GTF ( [ [:], ch_gtf ] ).gunzip.map { it[1] }
                                                                        ^^
  ```

- Warning: `workflows/scrnaseq.nf:111:22`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
              ch_gtf = Channel.value( ch_gtf )
                       ^^^^^^^
  ```

- Warning: `workflows/scrnaseq.nf:193:13`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
              meta, outs -> outs.findAll{ it -> it.name == "web_summary.html"}
              ^^^^
  ```

- Warning: `workflows/scrnaseq.nf:251:44`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
              if (!map_collection_clone.any{ it.feature_type == 'gex' })    { map_collection_clone.add( [id: sample_id, feature_type: 'gex'   , gex:    empty_file, options:[:] ] ) }
                                             ^^
  ```

- Warning: `workflows/scrnaseq.nf:252:44`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
              if (!map_collection_clone.any{ it.feature_type == 'vdj' })    { map_collection_clone.add( [id: sample_id, feature_type: 'vdj'   , vdj:    empty_file, options:[:] ] ) }
                                             ^^
  ```

- Warning: `workflows/scrnaseq.nf:253:44`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
              if (!map_collection_clone.any{ it.feature_type == 'ab' })     { map_collection_clone.add( [id: sample_id, feature_type: 'ab'    , ab:     empty_file, options:[:] ] ) }
                                             ^^
  ```

- Warning: `workflows/scrnaseq.nf:254:44`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
              if (!map_collection_clone.any{ it.feature_type == 'beam' })   { map_collection_clone.add( [id: sample_id, feature_type: 'beam'  , beam:   empty_file, options:[:] ] ) } // currently not implemented, the input samplesheet checking will not allow it.
                                             ^^
  ```

- Warning: `workflows/scrnaseq.nf:255:44`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
              if (!map_collection_clone.any{ it.feature_type == 'crispr' }) { map_collection_clone.add( [id: sample_id, feature_type: 'crispr', crispr: empty_file, options:[:] ] ) }
                                             ^^
  ```

- Warning: `workflows/scrnaseq.nf:256:44`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
              if (!map_collection_clone.any{ it.feature_type == 'cmo' })    { map_collection_clone.add( [id: sample_id, feature_type: 'cmo'   , cmo:    empty_file, options:[:] ] ) }
                                             ^^
  ```

- Warning: `workflows/scrnaseq.nf:274:13`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
              meta, outs -> outs.findAll{ it -> it.name == "web_summary.html" }
              ^^^^
  ```

- Warning: `workflows/scrnaseq.nf:286:40`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          star_index ? ch_star_index.map{it[1]} : [],
                                         ^^
  ```

- Warning: `workflows/scrnaseq.nf:299:33`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
                  .filter { meta, mtx_files -> meta.input_type == 'raw' }
                                  ^^^^^^^^^
  ```

- Warning: `workflows/scrnaseq.nf:330:36`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
          ch_multiqc_config        = Channel.fromPath(
                                     ^^^^^^^
  ```

- Warning: `workflows/scrnaseq.nf:333:13`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
              Channel.fromPath(params.multiqc_config, checkIfExists: true) :
              ^^^^^^^
  ```

- Warning: `workflows/scrnaseq.nf:334:13`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
              Channel.empty()
              ^^^^^^^
  ```

- Warning: `workflows/scrnaseq.nf:336:13`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
              Channel.fromPath(params.multiqc_logo, checkIfExists: true) :
              ^^^^^^^
  ```

- Warning: `workflows/scrnaseq.nf:337:13`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
              Channel.empty()
              ^^^^^^^
  ```

- Warning: `workflows/scrnaseq.nf:341:31`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
          ch_workflow_summary = Channel.value(paramsSummaryMultiqc(summary_params))
                                ^^^^^^^
  ```

- Warning: `workflows/scrnaseq.nf:347:49`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
          ch_methods_description                = Channel.value(
                                                  ^^^^^^^
  ```

- Warning: `workflows/scrnaseq.nf:368:29`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
          ch_multiqc_report = Channel.empty()
                              ^^^^^^^
  ```
