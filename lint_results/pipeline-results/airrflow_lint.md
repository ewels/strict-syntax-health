# Nextflow lint results

- Generated: 2026-01-16T10:16:52.499138121Z
- Nextflow version: 25.12.0-edge
- Summary: 151 errors, 141 warnings

## :x: Errors

- Error: `conf/base.config:66:9`: If statements cannot be mixed with config statements

  ```nextflow
          if (params.use_gpu){
          ^
  ```

- Error: `conf/test.config:26:13`: `pipelines_testdata_base_path` is not defined

  ```nextflow
      input = pipelines_testdata_base_path + 'testdata-bcr/Metadata_small_test_airr.tsv'
              ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  ```

- Error: `conf/test.config:27:16`: `pipelines_testdata_base_path` is not defined

  ```nextflow
      cprimers = pipelines_testdata_base_path + 'testdata-bcr/C_primers.fasta'
                 ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  ```

- Error: `conf/test.config:28:16`: `pipelines_testdata_base_path` is not defined

  ```nextflow
      vprimers = pipelines_testdata_base_path + 'testdata-bcr/V_primers.fasta'
                 ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  ```

- Error: `conf/test.config:29:23`: `pipelines_testdata_base_path` is not defined

  ```nextflow
      reference_fasta = pipelines_testdata_base_path + 'database-cache/imgtdb_base.zip'
                        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  ```

- Error: `conf/test.config:30:25`: `pipelines_testdata_base_path` is not defined

  ```nextflow
      reference_igblast = pipelines_testdata_base_path + 'database-cache/igblast_base.zip'
                          ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  ```

- Error: `conf/test_10x_sc.config:29:13`: `pipelines_testdata_base_path` is not defined

  ```nextflow
      input = pipelines_testdata_base_path + 'testdata-sc/10x_sc_raw.tsv'
              ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  ```

- Error: `conf/test_10x_sc.config:30:21`: `pipelines_testdata_base_path` is not defined

  ```nextflow
      reference_10x = pipelines_testdata_base_path + 'testdata-sc/refdata-cellranger-vdj-GRCh38-alts-ensembl-5.0.0.tar.gz'
                      ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  ```

- Error: `conf/test_assembled_hs.config:24:13`: `pipelines_testdata_base_path` is not defined

  ```nextflow
      input = pipelines_testdata_base_path + 'testdata-reveal/test_assembled_metadata_hs.tsv'
              ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  ```

- Error: `conf/test_assembled_hs.config:25:23`: `pipelines_testdata_base_path` is not defined

  ```nextflow
      reference_fasta = pipelines_testdata_base_path + 'database-cache/imgtdb_base.zip'
                        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  ```

- Error: `conf/test_assembled_hs.config:26:25`: `pipelines_testdata_base_path` is not defined

  ```nextflow
      reference_igblast = pipelines_testdata_base_path + 'database-cache/igblast_base.zip'
                          ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  ```

- Error: `conf/test_assembled_immcantation_devel_hs.config:24:13`: `pipelines_testdata_base_path` is not defined

  ```nextflow
      input = pipelines_testdata_base_path + 'testdata-reveal/test_assembled_metadata_hs.tsv'
              ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  ```

- Error: `conf/test_assembled_immcantation_devel_hs.config:25:23`: `pipelines_testdata_base_path` is not defined

  ```nextflow
      reference_fasta = pipelines_testdata_base_path + 'database-cache/imgtdb_base.zip'
                        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  ```

- Error: `conf/test_assembled_immcantation_devel_hs.config:26:25`: `pipelines_testdata_base_path` is not defined

  ```nextflow
      reference_igblast = pipelines_testdata_base_path + 'database-cache/igblast_base.zip'
                          ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  ```

- Error: `conf/test_assembled_immcantation_devel_mm.config:24:13`: `pipelines_testdata_base_path` is not defined

  ```nextflow
      input = pipelines_testdata_base_path + 'testdata-reveal/test_assembled_metadata_mm.tsv'
              ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  ```

- Error: `conf/test_assembled_immcantation_devel_mm.config:25:23`: `pipelines_testdata_base_path` is not defined

  ```nextflow
      reference_fasta = pipelines_testdata_base_path + 'database-cache/imgtdb_base.zip'
                        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  ```

- Error: `conf/test_assembled_immcantation_devel_mm.config:26:25`: `pipelines_testdata_base_path` is not defined

  ```nextflow
      reference_igblast = pipelines_testdata_base_path + 'database-cache/igblast_base.zip'
                          ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  ```

- Error: `conf/test_assembled_mm.config:24:13`: `pipelines_testdata_base_path` is not defined

  ```nextflow
      input = pipelines_testdata_base_path + 'testdata-reveal/test_assembled_metadata_mm.tsv'
              ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  ```

- Error: `conf/test_assembled_mm.config:25:23`: `pipelines_testdata_base_path` is not defined

  ```nextflow
      reference_fasta = pipelines_testdata_base_path + 'database-cache/imgtdb_base.zip'
                        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  ```

- Error: `conf/test_assembled_mm.config:26:25`: `pipelines_testdata_base_path` is not defined

  ```nextflow
      reference_igblast = pipelines_testdata_base_path + 'database-cache/igblast_base.zip'
                          ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  ```

- Error: `conf/test_embeddings_H.config:27:13`: `pipelines_testdata_base_path` is not defined

  ```nextflow
      input = pipelines_testdata_base_path + 'testdata-reveal/test_assembled_metadata_tiny.tsv'
              ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  ```

- Error: `conf/test_embeddings_H.config:28:23`: `pipelines_testdata_base_path` is not defined

  ```nextflow
      reference_fasta = pipelines_testdata_base_path + 'database-cache/imgtdb_base.zip'
                        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  ```

- Error: `conf/test_embeddings_H.config:29:25`: `pipelines_testdata_base_path` is not defined

  ```nextflow
      reference_igblast = pipelines_testdata_base_path + 'database-cache/igblast_base.zip'
                          ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  ```

- Error: `conf/test_embeddings_HL.config:27:13`: `pipelines_testdata_base_path` is not defined

  ```nextflow
      input = pipelines_testdata_base_path + 'testdata-reveal/test_assembled_metadata_tiny.tsv'
              ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  ```

- Error: `conf/test_embeddings_HL.config:28:23`: `pipelines_testdata_base_path` is not defined

  ```nextflow
      reference_fasta = pipelines_testdata_base_path + 'database-cache/imgtdb_base.zip'
                        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  ```

- Error: `conf/test_embeddings_HL.config:29:25`: `pipelines_testdata_base_path` is not defined

  ```nextflow
      reference_igblast = pipelines_testdata_base_path + 'database-cache/igblast_base.zip'
                          ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  ```

- Error: `conf/test_fetchimgt.config:26:13`: `pipelines_testdata_base_path` is not defined

  ```nextflow
      input = pipelines_testdata_base_path + 'testdata-reveal/test_assembled_metadata_hs.tsv'
              ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  ```

- Error: `conf/test_full.config:25:13`: `pipelines_testdata_base_path` is not defined

  ```nextflow
      input = pipelines_testdata_base_path + 'testdata-bcr/metadata_pcr_umi_airr_300.tsv'
              ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  ```

- Error: `conf/test_full.config:28:23`: `pipelines_testdata_base_path` is not defined

  ```nextflow
      reference_fasta = pipelines_testdata_base_path + 'database-cache/imgtdb_base.zip'
                        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  ```

- Error: `conf/test_full.config:29:25`: `pipelines_testdata_base_path` is not defined

  ```nextflow
      reference_igblast = pipelines_testdata_base_path + 'database-cache/igblast_base.zip'
                          ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  ```

- Error: `conf/test_maskprimers_align.config:25:13`: `pipelines_testdata_base_path` is not defined

  ```nextflow
      input = pipelines_testdata_base_path + 'testdata-bcr/Metadata_small_test_airr.tsv'
              ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  ```

- Error: `conf/test_maskprimers_align.config:26:16`: `pipelines_testdata_base_path` is not defined

  ```nextflow
      cprimers = pipelines_testdata_base_path + 'testdata-bcr/C_primers.fasta'
                 ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  ```

- Error: `conf/test_maskprimers_align.config:27:16`: `pipelines_testdata_base_path` is not defined

  ```nextflow
      vprimers = pipelines_testdata_base_path + 'testdata-bcr/V_primers.fasta'
                 ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  ```

- Error: `conf/test_maskprimers_align.config:28:23`: `pipelines_testdata_base_path` is not defined

  ```nextflow
      reference_fasta = pipelines_testdata_base_path + 'database-cache/imgtdb_base.zip'
                        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  ```

- Error: `conf/test_maskprimers_align.config:29:25`: `pipelines_testdata_base_path` is not defined

  ```nextflow
      reference_igblast = pipelines_testdata_base_path + 'database-cache/igblast_base.zip'
                          ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  ```

- Error: `conf/test_maskprimers_extract.config:25:13`: `pipelines_testdata_base_path` is not defined

  ```nextflow
      input = pipelines_testdata_base_path + 'testdata-bcr/Metadata_small_test_airr.tsv'
              ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  ```

- Error: `conf/test_maskprimers_extract.config:26:23`: `pipelines_testdata_base_path` is not defined

  ```nextflow
      reference_fasta = pipelines_testdata_base_path + 'database-cache/imgtdb_base.zip'
                        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  ```

- Error: `conf/test_maskprimers_extract.config:27:25`: `pipelines_testdata_base_path` is not defined

  ```nextflow
      reference_igblast = pipelines_testdata_base_path + 'database-cache/igblast_base.zip'
                          ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  ```

- Error: `conf/test_nebnext_umi.config:28:13`: `pipelines_testdata_base_path` is not defined

  ```nextflow
      input = pipelines_testdata_base_path + 'testdata-neb/samplesheet.tsv'
              ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  ```

- Error: `conf/test_nebnext_umi.config:30:23`: `pipelines_testdata_base_path` is not defined

  ```nextflow
      reference_fasta = pipelines_testdata_base_path + 'database-cache/imgtdb_base.zip'
                        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  ```

- Error: `conf/test_nebnext_umi.config:31:25`: `pipelines_testdata_base_path` is not defined

  ```nextflow
      reference_igblast = pipelines_testdata_base_path + 'database-cache/igblast_base.zip'
                          ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  ```

- Error: `conf/test_no_umi.config:31:13`: `pipelines_testdata_base_path` is not defined

  ```nextflow
      input = pipelines_testdata_base_path + 'testdata-no-umi/Metadata_test-no-umi_airr.tsv'
              ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  ```

- Error: `conf/test_no_umi.config:32:16`: `pipelines_testdata_base_path` is not defined

  ```nextflow
      cprimers = pipelines_testdata_base_path + 'testdata-no-umi/Greiff2014_CPrimers.fasta'
                 ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  ```

- Error: `conf/test_no_umi.config:33:16`: `pipelines_testdata_base_path` is not defined

  ```nextflow
      vprimers = pipelines_testdata_base_path + 'testdata-no-umi/Greiff2014_VPrimers.fasta'
                 ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  ```

- Error: `conf/test_no_umi.config:34:23`: `pipelines_testdata_base_path` is not defined

  ```nextflow
      reference_fasta = pipelines_testdata_base_path + 'database-cache/imgtdb_base.zip'
                        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  ```

- Error: `conf/test_no_umi.config:35:25`: `pipelines_testdata_base_path` is not defined

  ```nextflow
      reference_igblast = pipelines_testdata_base_path + 'database-cache/igblast_base.zip'
                          ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  ```

- Error: `conf/test_nocluster.config:25:13`: `pipelines_testdata_base_path` is not defined

  ```nextflow
      input = pipelines_testdata_base_path + 'testdata-bcr/Metadata_small_test_airr.tsv'
              ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  ```

- Error: `conf/test_nocluster.config:26:16`: `pipelines_testdata_base_path` is not defined

  ```nextflow
      cprimers = pipelines_testdata_base_path + 'testdata-bcr/C_primers.fasta'
                 ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  ```

- Error: `conf/test_nocluster.config:27:16`: `pipelines_testdata_base_path` is not defined

  ```nextflow
      vprimers = pipelines_testdata_base_path + 'testdata-bcr/V_primers.fasta'
                 ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  ```

- Error: `conf/test_nocluster.config:28:23`: `pipelines_testdata_base_path` is not defined

  ```nextflow
      reference_fasta = pipelines_testdata_base_path + 'database-cache/imgtdb_base.zip'
                        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  ```

- Error: `conf/test_nocluster.config:29:25`: `pipelines_testdata_base_path` is not defined

  ```nextflow
      reference_igblast = pipelines_testdata_base_path + 'database-cache/igblast_base.zip'
                          ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  ```

- Error: `conf/test_raw_immcantation_devel.config:25:13`: `pipelines_testdata_base_path` is not defined

  ```nextflow
      input = pipelines_testdata_base_path + 'testdata-bcr/Metadata_small_test_airr.tsv'
              ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  ```

- Error: `conf/test_raw_immcantation_devel.config:26:16`: `pipelines_testdata_base_path` is not defined

  ```nextflow
      cprimers = pipelines_testdata_base_path + 'testdata-bcr/C_primers.fasta'
                 ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  ```

- Error: `conf/test_raw_immcantation_devel.config:27:16`: `pipelines_testdata_base_path` is not defined

  ```nextflow
      vprimers = pipelines_testdata_base_path + 'testdata-bcr/V_primers.fasta'
                 ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  ```

- Error: `conf/test_raw_immcantation_devel.config:29:23`: `pipelines_testdata_base_path` is not defined

  ```nextflow
      reference_fasta = pipelines_testdata_base_path + 'database-cache/imgtdb_base.zip'
                        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  ```

- Error: `conf/test_raw_immcantation_devel.config:30:25`: `pipelines_testdata_base_path` is not defined

  ```nextflow
      reference_igblast = pipelines_testdata_base_path + 'database-cache/igblast_base.zip'
                          ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  ```

- Error: `conf/test_reassign_false.config:24:13`: `pipelines_testdata_base_path` is not defined

  ```nextflow
      input = pipelines_testdata_base_path + 'testdata-reveal/test_assembled_metadata_assigned.tsv'
              ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  ```

- Error: `conf/test_reassign_false.config:25:23`: `pipelines_testdata_base_path` is not defined

  ```nextflow
      reference_fasta = pipelines_testdata_base_path + 'database-cache/imgtdb_base.zip'
                        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  ```

- Error: `conf/test_reassign_false.config:26:25`: `pipelines_testdata_base_path` is not defined

  ```nextflow
      reference_igblast = pipelines_testdata_base_path + 'database-cache/igblast_base.zip'
                          ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  ```

- Error: `conf/test_takara_smartseq_umi_bcr.config:27:13`: `pipelines_testdata_base_path` is not defined

  ```nextflow
      input = pipelines_testdata_base_path +'testdata-clontech/samplesheet.tsv'
              ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  ```

- Error: `conf/test_takara_smartseq_umi_bcr.config:29:23`: `pipelines_testdata_base_path` is not defined

  ```nextflow
      reference_fasta = pipelines_testdata_base_path + 'database-cache/imgtdb_base.zip'
                        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  ```

- Error: `conf/test_takara_smartseq_umi_bcr.config:30:25`: `pipelines_testdata_base_path` is not defined

  ```nextflow
      reference_igblast = pipelines_testdata_base_path + 'database-cache/igblast_base.zip'
                          ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  ```

- Error: `conf/test_tcr.config:34:13`: `pipelines_testdata_base_path` is not defined

  ```nextflow
      input = pipelines_testdata_base_path + 'testdata-tcr/TCR_metadata_airr.tsv'
              ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  ```

- Error: `conf/test_tcr.config:35:16`: `pipelines_testdata_base_path` is not defined

  ```nextflow
      cprimers = pipelines_testdata_base_path + 'testdata-tcr/cprimers.fasta'
                 ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  ```

- Error: `conf/test_tcr.config:36:19`: `pipelines_testdata_base_path` is not defined

  ```nextflow
      race_linker = pipelines_testdata_base_path + 'testdata-tcr/linker.fasta'
                    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  ```

- Error: `conf/test_tcr.config:37:23`: `pipelines_testdata_base_path` is not defined

  ```nextflow
      reference_fasta = pipelines_testdata_base_path + 'database-cache/imgtdb_base.zip'
                        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  ```

- Error: `conf/test_tcr.config:38:25`: `pipelines_testdata_base_path` is not defined

  ```nextflow
      reference_igblast = pipelines_testdata_base_path + 'database-cache/igblast_base.zip'
                          ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  ```

- Error: `modules/local/airrflow_report/airrflow_report.nf:6:5`: Invalid process directive

  ```nextflow
      if (workflow.profile.tokenize(',').intersect(['conda', 'mamba']).size() >= 1) {
      ^
  ```

- Error: `modules/local/enchantr/clonal_assignment.nf:6:13`: `for` loops are no longer supported

  ```nextflow
              for (param in args.keySet().sort()){
              ^^^
  ```

- Error: `modules/local/enchantr/clonal_assignment.nf:6:18`: `param` is not defined

  ```nextflow
              for (param in args.keySet().sort()){
                   ^^^^^
  ```

- Error: `modules/local/enchantr/clonal_assignment.nf:7:29`: `param` is not defined

  ```nextflow
                  value = args[param].toString()
                              ^^^^^^^
  ```

- Error: `modules/local/enchantr/clonal_assignment.nf:11:30`: `param` is not defined

  ```nextflow
                  s = s + ",'"+param+"'="+value
                               ^^^^^
  ```

- Error: `modules/local/enchantr/clonal_assignment.nf:25:5`: Invalid process directive

  ```nextflow
      if (workflow.profile.tokenize(',').intersect(['conda', 'mamba']).size() >= 1) {
      ^
  ```

- Error: `modules/local/enchantr/collapse_duplicates.nf:8:5`: Invalid process directive

  ```nextflow
      if (workflow.profile.tokenize(',').intersect(['conda', 'mamba']).size() >= 1) {
      ^
  ```

- Error: `modules/local/enchantr/detect_contamination.nf:8:5`: Invalid process directive

  ```nextflow
      if (workflow.profile.tokenize(',').intersect(['conda', 'mamba']).size() >= 1) {
      ^
  ```

- Error: `modules/local/enchantr/dowser_lineages.nf:6:13`: `for` loops are no longer supported

  ```nextflow
              for (param in args.keySet().sort()){
              ^^^
  ```

- Error: `modules/local/enchantr/dowser_lineages.nf:6:18`: `param` is not defined

  ```nextflow
              for (param in args.keySet().sort()){
                   ^^^^^
  ```

- Error: `modules/local/enchantr/dowser_lineages.nf:7:29`: `param` is not defined

  ```nextflow
                  value = args[param].toString()
                              ^^^^^^^
  ```

- Error: `modules/local/enchantr/dowser_lineages.nf:11:30`: `param` is not defined

  ```nextflow
                  s = s + ",'"+param+"'="+value
                               ^^^^^
  ```

- Error: `modules/local/enchantr/dowser_lineages.nf:25:5`: Invalid process directive

  ```nextflow
      if (workflow.profile.tokenize(',').intersect(['conda', 'mamba']).size() >= 1) {
      ^
  ```

- Error: `modules/local/enchantr/find_threshold.nf:6:13`: `for` loops are no longer supported

  ```nextflow
              for (param in args.keySet().sort()){
              ^^^
  ```

- Error: `modules/local/enchantr/find_threshold.nf:6:18`: `param` is not defined

  ```nextflow
              for (param in args.keySet().sort()){
                   ^^^^^
  ```

- Error: `modules/local/enchantr/find_threshold.nf:7:29`: `param` is not defined

  ```nextflow
                  value = args[param].toString()
                              ^^^^^^^
  ```

- Error: `modules/local/enchantr/find_threshold.nf:11:30`: `param` is not defined

  ```nextflow
                  s = s + ",'"+param+"'="+value
                               ^^^^^
  ```

- Error: `modules/local/enchantr/find_threshold.nf:25:5`: Invalid process directive

  ```nextflow
      if (workflow.profile.tokenize(',').intersect(['conda', 'mamba']).size() >= 1) {
      ^
  ```

- Error: `modules/local/enchantr/remove_chimeric.nf:9:5`: Invalid process directive

  ```nextflow
      if (workflow.profile.tokenize(',').intersect(['conda', 'mamba']).size() >= 1) {
      ^
  ```

- Error: `modules/local/enchantr/report_file_size.nf:10:5`: Invalid process directive

  ```nextflow
      if (workflow.profile.tokenize(',').intersect(['conda', 'mamba']).size() >= 1) {
      ^
  ```

- Error: `modules/local/enchantr/single_cell_qc.nf:6:13`: `for` loops are no longer supported

  ```nextflow
              for (param in args.keySet().sort()){
              ^^^
  ```

- Error: `modules/local/enchantr/single_cell_qc.nf:6:18`: `param` is not defined

  ```nextflow
              for (param in args.keySet().sort()){
                   ^^^^^
  ```

- Error: `modules/local/enchantr/single_cell_qc.nf:7:29`: `param` is not defined

  ```nextflow
                  value = args[param].toString()
                              ^^^^^^^
  ```

- Error: `modules/local/enchantr/single_cell_qc.nf:11:30`: `param` is not defined

  ```nextflow
                  s = s + ",'"+param+"'="+value
                               ^^^^^
  ```

- Error: `modules/local/enchantr/single_cell_qc.nf:24:5`: Invalid process directive

  ```nextflow
      if (workflow.profile.tokenize(',').intersect(['conda', 'mamba']).size() >= 1) {
      ^
  ```

- Error: `modules/local/enchantr/validate_input.nf:10:5`: Invalid process directive

  ```nextflow
      if (workflow.profile.tokenize(',').intersect(['conda', 'mamba']).size() >= 1) {
      ^
  ```

- Error: `modules/local/presto/presto_maskprimers_align.nf:28:9`: `barcode` is already declared

  ```nextflow
      def barcode = barcode ? '--barcode' : ''
          ^^^^^^^
  ```

- Error: `modules/local/presto/presto_maskprimers_extract.nf:28:9`: `barcode` is already declared

  ```nextflow
      def barcode = barcode ? '--barcode' : ''
          ^^^^^^^
  ```

- Error: `modules/local/presto/presto_maskprimers_score.nf:32:9`: `barcode` is already declared

  ```nextflow
      def barcode = barcode ? '--barcode' : ''
          ^^^^^^^
  ```

- Error: `modules/local/reveal/add_meta_to_tab.nf:7:5`: Invalid process directive

  ```nextflow
      if (workflow.profile.tokenize(',').intersect(['conda', 'mamba']).size() >= 1) {
      ^
  ```

- Error: `modules/local/reveal/filter_junction_mod3.nf:7:5`: Invalid process directive

  ```nextflow
      if (workflow.profile.tokenize(',').intersect(['conda', 'mamba']).size() >= 1) {
      ^
  ```

- Error: `modules/local/reveal/filter_quality.nf:7:5`: Invalid process directive

  ```nextflow
      if (workflow.profile.tokenize(',').intersect(['conda', 'mamba']).size() >= 1) {
      ^
  ```

- Error: `nextflow.config:88:25`: `pipelines_testdata_base_path` is not defined

  ```nextflow
      reference_igblast = pipelines_testdata_base_path + 'database-cache/igblast_base.zip'
                          ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  ```

- Error: `nextflow.config:89:23`: `pipelines_testdata_base_path` is not defined

  ```nextflow
      reference_fasta = pipelines_testdata_base_path + 'database-cache/imgtdb_base.zip'
                        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  ```

- Error: `subworkflows/local/clonal_analysis.nf:86:38`: Unexpected input: '"'

  ```nextflow
      ch_repertoire.map{ it -> [ it[0]."${params.cloneby}",
                                       ^
  ```

- Error: `subworkflows/local/databases.nf:5:1`: Invalid workflow definition -- check for missing or out-of-order section labels

  ```nextflow
  workflow DATABASES {
  ^
  ```

- Error: `subworkflows/local/fastq_input_check.nf:67:35`: Unexpected input: '"'

  ```nextflow
      meta.collapseby_group   = col."${params.collapseby}"
                                    ^
  ```

- Error: `subworkflows/local/presto_sans_umi.nf:67:13`: Incorrect number of call arguments, expected 8 but received 6

  ```nextflow
              PRESTO_MASKPRIMERS_ALIGN_SANSUMI_FWD(
              ^
  ```

- Error: `subworkflows/local/presto_sans_umi.nf:75:13`: Incorrect number of call arguments, expected 8 but received 6

  ```nextflow
              PRESTO_MASKPRIMERS_ALIGN_SANSUMI_REV(
              ^
  ```

- Error: `subworkflows/local/presto_sans_umi.nf:84:13`: Incorrect number of call arguments, expected 8 but received 6

  ```nextflow
              PRESTO_MASKPRIMERS_ALIGN_SANSUMI_FWD(
              ^
  ```

- Error: `subworkflows/local/presto_sans_umi.nf:92:13`: Incorrect number of call arguments, expected 8 but received 6

  ```nextflow
              PRESTO_MASKPRIMERS_ALIGN_SANSUMI_REV(
              ^
  ```

- Error: `subworkflows/local/rnaseq_input.nf:3:1`: Module could not be parsed: '/home/runner/work/strict-syntax-health/strict-syntax-health/pipelines/airrflow/subworkflows/local/fastq_input_check.nf'

  ```nextflow
  include { FASTQ_INPUT_CHECK                                             } from '../../subworkflows/local/fastq_input_check'
  ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  ```

- Error: `subworkflows/local/rnaseq_input.nf:25:5`: `FASTQ_INPUT_CHECK` is not defined

  ```nextflow
      FASTQ_INPUT_CHECK(
      ^^^^^^^^^^^^^^^^^
  ```

- Error: `subworkflows/local/rnaseq_input.nf:28:35`: `FASTQ_INPUT_CHECK` is not defined

  ```nextflow
      ch_versions = ch_versions.mix(FASTQ_INPUT_CHECK.out.versions)
                                    ^^^^^^^^^^^^^^^^^
  ```

- Error: `subworkflows/local/rnaseq_input.nf:30:16`: `FASTQ_INPUT_CHECK` is not defined

  ```nextflow
      ch_reads = FASTQ_INPUT_CHECK.out.reads
                 ^^^^^^^^^^^^^^^^^
  ```

- Error: `subworkflows/local/rnaseq_input.nf:128:19`: `FASTQ_INPUT_CHECK` is not defined

  ```nextflow
      samplesheet = FASTQ_INPUT_CHECK.out.samplesheet
                    ^^^^^^^^^^^^^^^^^
  ```

- Error: `subworkflows/local/sc_raw_input.nf:5:1`: Module could not be parsed: '/home/runner/work/strict-syntax-health/strict-syntax-health/pipelines/airrflow/subworkflows/local/fastq_input_check.nf'

  ```nextflow
  include { FASTQ_INPUT_CHECK                                             } from '../../subworkflows/local/fastq_input_check'
  ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  ```

- Error: `subworkflows/local/sc_raw_input.nf:21:5`: `FASTQ_INPUT_CHECK` is not defined

  ```nextflow
      FASTQ_INPUT_CHECK(
      ^^^^^^^^^^^^^^^^^
  ```

- Error: `subworkflows/local/sc_raw_input.nf:24:35`: `FASTQ_INPUT_CHECK` is not defined

  ```nextflow
      ch_versions = ch_versions.mix(FASTQ_INPUT_CHECK.out.versions)
                                    ^^^^^^^^^^^^^^^^^
  ```

- Error: `subworkflows/local/sc_raw_input.nf:26:16`: `FASTQ_INPUT_CHECK` is not defined

  ```nextflow
      ch_reads = FASTQ_INPUT_CHECK.out.reads
                 ^^^^^^^^^^^^^^^^^
  ```

- Error: `subworkflows/local/sc_raw_input.nf:99:19`: `FASTQ_INPUT_CHECK` is not defined

  ```nextflow
      samplesheet = FASTQ_INPUT_CHECK.out.samplesheet
                    ^^^^^^^^^^^^^^^^^
  ```

- Error: `subworkflows/local/sequence_assembly.nf:11:1`: Statements cannot be mixed with script declarations -- move statements into a process, workflow, or function

  ```nextflow
  ch_report_rmd = Channel.fromPath(params.report_rmd, checkIfExists: true)
  ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  ```

- Error: `subworkflows/local/sequence_assembly.nf:12:1`: Statements cannot be mixed with script declarations -- move statements into a process, workflow, or function

  ```nextflow
  ch_report_css = Channel.fromPath(params.report_css, checkIfExists: true)
  ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  ```

- Error: `subworkflows/local/sequence_assembly.nf:28:1`: Module could not be parsed: '/home/runner/work/strict-syntax-health/strict-syntax-health/pipelines/airrflow/subworkflows/local/fastq_input_check.nf'

  ```nextflow
  include { FASTQ_INPUT_CHECK           } from '../../subworkflows/local/fastq_input_check'
  ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  ```

- Error: `subworkflows/local/sequence_assembly.nf:178:5`: `FASTQ_INPUT_CHECK` is not defined

  ```nextflow
      FASTQ_INPUT_CHECK(ch_input)
      ^^^^^^^^^^^^^^^^^
  ```

- Error: `subworkflows/local/sequence_assembly.nf:179:35`: `FASTQ_INPUT_CHECK` is not defined

  ```nextflow
      ch_versions = ch_versions.mix(FASTQ_INPUT_CHECK.out.versions)
                                    ^^^^^^^^^^^^^^^^^
  ```

- Error: `subworkflows/local/sequence_assembly.nf:181:16`: `FASTQ_INPUT_CHECK` is not defined

  ```nextflow
      ch_reads = FASTQ_INPUT_CHECK.out.reads
                 ^^^^^^^^^^^^^^^^^
  ```

- Error: `subworkflows/local/sequence_assembly.nf:243:19`: `FASTQ_INPUT_CHECK` is not defined

  ```nextflow
      samplesheet = FASTQ_INPUT_CHECK.out.samplesheet
                    ^^^^^^^^^^^^^^^^^
  ```

- Error: `workflows/airrflow.nf:14:1`: Statements cannot be mixed with script declarations -- move statements into a process, workflow, or function

  ```nextflow
  ch_multiqc_config        = Channel.fromPath("$projectDir/assets/multiqc_config.yml", checkIfExists: true)
  ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  ```

- Error: `workflows/airrflow.nf:15:1`: Statements cannot be mixed with script declarations -- move statements into a process, workflow, or function

  ```nextflow
  ch_multiqc_custom_config = params.multiqc_config ? Channel.fromPath( params.multiqc_config, checkIfExists: true ) : Channel.empty()
  ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  ```

- Error: `workflows/airrflow.nf:16:1`: Statements cannot be mixed with script declarations -- move statements into a process, workflow, or function

  ```nextflow
  ch_multiqc_logo          = params.multiqc_logo   ? Channel.fromPath( params.multiqc_logo, checkIfExists: true ) : Channel.empty()
  ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  ```

- Error: `workflows/airrflow.nf:17:1`: Statements cannot be mixed with script declarations -- move statements into a process, workflow, or function

  ```nextflow
  ch_multiqc_custom_methods_description = params.multiqc_methods_description ? file(params.multiqc_methods_description, checkIfExists: true) : file("$projectDir/assets/methods_description_template.yml", checkIfExists: true)
  ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  ```

- Error: `workflows/airrflow.nf:20:1`: Statements cannot be mixed with script declarations -- move statements into a process, workflow, or function

  ```nextflow
  ch_report_rmd       = Channel.fromPath(params.report_rmd, checkIfExists: true)
  ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  ```

- Error: `workflows/airrflow.nf:21:1`: Statements cannot be mixed with script declarations -- move statements into a process, workflow, or function

  ```nextflow
  ch_report_css       = Channel.fromPath(params.report_css, checkIfExists: true)
  ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  ```

- Error: `workflows/airrflow.nf:22:1`: Statements cannot be mixed with script declarations -- move statements into a process, workflow, or function

  ```nextflow
  ch_report_logo      = Channel.fromPath(params.report_logo, checkIfExists: true)
  ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  ```

- Error: `workflows/airrflow.nf:23:1`: Statements cannot be mixed with script declarations -- move statements into a process, workflow, or function

  ```nextflow
  ch_report_logo_img  = Channel.fromPath(params.report_logo_img, checkIfExists: true)
  ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  ```

- Error: `workflows/airrflow.nf:36:1`: Included name 'DATABASES' is not defined in module '/home/runner/work/strict-syntax-health/strict-syntax-health/pipelines/airrflow/subworkflows/local/databases.nf'

  ```nextflow
  include { DATABASES                     } from '../subworkflows/local/databases'
  ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  ```

- Error: `workflows/airrflow.nf:42:1`: Module could not be parsed: '/home/runner/work/strict-syntax-health/strict-syntax-health/pipelines/airrflow/subworkflows/local/clonal_analysis.nf'

  ```nextflow
  include { CLONAL_ANALYSIS               } from '../subworkflows/local/clonal_analysis'
  ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  ```

- Error: `workflows/airrflow.nf:45:1`: Module could not be parsed: '/home/runner/work/strict-syntax-health/strict-syntax-health/pipelines/airrflow/subworkflows/local/fastq_input_check.nf'

  ```nextflow
  include { FASTQ_INPUT_CHECK             } from '../subworkflows/local/fastq_input_check'
  ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  ```

- Error: `workflows/airrflow.nf:82:9`: `DATABASES` is not defined

  ```nextflow
          DATABASES()
          ^^^^^^^^^
  ```

- Error: `workflows/airrflow.nf:119:21`: `DATABASES` is not defined

  ```nextflow
                      DATABASES.out.igblast.collect()
                      ^^^^^^^^^
  ```

- Error: `workflows/airrflow.nf:144:21`: `DATABASES` is not defined

  ```nextflow
                      DATABASES.out.igblast.collect()
                      ^^^^^^^^^
  ```

- Error: `workflows/airrflow.nf:214:13`: `DATABASES` is not defined

  ```nextflow
              DATABASES.out.igblast.collect(),
              ^^^^^^^^^
  ```

- Error: `workflows/airrflow.nf:215:13`: `DATABASES` is not defined

  ```nextflow
              DATABASES.out.reference_fasta.collect()
              ^^^^^^^^^
  ```

- Error: `workflows/airrflow.nf:254:13`: `CLONAL_ANALYSIS` is not defined

  ```nextflow
              CLONAL_ANALYSIS(
              ^^^^^^^^^^^^^^^
  ```

- Error: `workflows/airrflow.nf:257:17`: `ch_report_logo_img` is not defined

  ```nextflow
                  ch_report_logo_img.collect().ifEmpty([])
                  ^^^^^^^^^^^^^^^^^^
  ```

- Error: `workflows/airrflow.nf:259:44`: `CLONAL_ANALYSIS` is not defined

  ```nextflow
              ch_versions = ch_versions.mix( CLONAL_ANALYSIS.out.versions)
                                             ^^^^^^^^^^^^^^^
  ```

- Error: `workflows/airrflow.nf:266:17`: `DATABASES` is not defined

  ```nextflow
                  DATABASES.out.igblast.collect()
                  ^^^^^^^^^
  ```

- Error: `workflows/airrflow.nf:295:17`: `ch_report_rmd` is not defined

  ```nextflow
                  ch_report_rmd.collect(),
                  ^^^^^^^^^^^^^
  ```

- Error: `workflows/airrflow.nf:296:17`: `ch_report_css` is not defined

  ```nextflow
                  ch_report_css.collect(),
                  ^^^^^^^^^^^^^
  ```

- Error: `workflows/airrflow.nf:297:17`: `ch_report_logo` is not defined

  ```nextflow
                  ch_report_logo.collect(),
                  ^^^^^^^^^^^^^^
  ```

- Error: `workflows/airrflow.nf:352:17`: `ch_multiqc_config` is not defined

  ```nextflow
                  ch_multiqc_config.toList(),
                  ^^^^^^^^^^^^^^^^^
  ```

- Error: `workflows/airrflow.nf:353:17`: `ch_multiqc_custom_config` is not defined

  ```nextflow
                  ch_multiqc_custom_config.toList(),
                  ^^^^^^^^^^^^^^^^^^^^^^^^
  ```

- Error: `workflows/airrflow.nf:354:17`: `ch_report_logo` is not defined

  ```nextflow
                  ch_report_logo.toList(),
                  ^^^^^^^^^^^^^^
  ```

## :warning: Warnings

- Warning: `modules/local/presto/presto_maskprimers_align.nf:29:9`: Variable was declared but not used

  ```nextflow
      def revpr = reverse_primers ? '--revpr' : ''
          ^^^^^
  ```

- Warning: `modules/nf-core/amulety/antiberta2/main.nf:41:9`: Variable was declared but not used

  ```nextflow
      def args = task.ext.args ?: ''
          ^^^^
  ```

- Warning: `modules/nf-core/amulety/antiberty/main.nf:40:9`: Variable was declared but not used

  ```nextflow
      def args = task.ext.args ?: ''
          ^^^^
  ```

- Warning: `modules/nf-core/amulety/balmpaired/main.nf:40:9`: Variable was declared but not used

  ```nextflow
      def args = task.ext.args ?: ''
          ^^^^
  ```

- Warning: `modules/nf-core/amulety/esm2/main.nf:40:9`: Variable was declared but not used

  ```nextflow
      def args = task.ext.args ?: ''
          ^^^^
  ```

- Warning: `modules/nf-core/amulety/translate/main.nf:22:9`: Variable was declared but not used

  ```nextflow
      def args = task.ext.args ?: ''
          ^^^^
  ```

- Warning: `modules/nf-core/amulety/translate/main.nf:38:9`: Variable was declared but not used

  ```nextflow
      def args = task.ext.args ?: ''
          ^^^^
  ```

- Warning: `modules/nf-core/cat/fastq/main.nf:21:9`: Variable was declared but not used

  ```nextflow
      def args = task.ext.args ?: ''
          ^^^^
  ```

- Warning: `modules/nf-core/cat/fastq/main.nf:23:59`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
      def readList = reads instanceof List ? reads.collect{ it.toString() } : [reads.toString()]
                                                            ^^
  ```

- Warning: `modules/nf-core/cat/fastq/main.nf:54:59`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
      def readList = reads instanceof List ? reads.collect{ it.toString() } : [reads.toString()]
                                                            ^^
  ```

- Warning: `modules/nf-core/cellranger/vdj/main.nf:47:9`: Variable was declared but not used

  ```nextflow
      def prefix = task.ext.prefix ?: "${meta.id}"
          ^^^^^^
  ```

- Warning: `modules/nf-core/trust4/main.nf:91:9`: Variable was declared but not used

  ```nextflow
      def args = task.ext.args ?: ''
          ^^^^
  ```

- Warning: `subworkflows/local/assembled_input_check.nf:18:15`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_logs = Channel.empty()
                ^^^^^^^
  ```

- Warning: `subworkflows/local/assembled_input_check.nf:25:25`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          .map { get_meta(it) }
                          ^^
  ```

- Warning: `subworkflows/local/bulk_qc_and_filter.nf:14:19`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_versions = Channel.empty()
                    ^^^^^^^
  ```

- Warning: `subworkflows/local/bulk_qc_and_filter.nf:15:15`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_logs = Channel.empty()
                ^^^^^^^
  ```

- Warning: `subworkflows/local/presto_sans_umi.nf:29:19`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_versions = Channel.empty()
                    ^^^^^^^
  ```

- Warning: `subworkflows/local/presto_sans_umi.nf:207:48`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
      fastp_reads_json = FASTP.out.json.collect{ meta,json -> json }
                                                 ^^^^
  ```

- Warning: `subworkflows/local/presto_sans_umi.nf:208:48`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
      fastp_reads_html = FASTP.out.html.collect{ meta,html -> html }
                                                 ^^^^
  ```

- Warning: `subworkflows/local/presto_umi.nf:54:19`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_versions = Channel.empty()
                    ^^^^^^^
  ```

- Warning: `subworkflows/local/presto_umi.nf:84:51`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
                                              .map{ id, meta1, R1, R2, meta2, index -> [ meta1, R1, R2, index ] }
                                                    ^^
  ```

- Warning: `subworkflows/local/presto_umi.nf:84:70`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
                                              .map{ id, meta1, R1, R2, meta2, index -> [ meta1, R1, R2, index ] }
                                                                       ^^^^^
  ```

- Warning: `subworkflows/local/presto_umi.nf:433:31`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
          ch_clustersets_logs = Channel.empty()
                                ^^^^^^^
  ```

- Warning: `subworkflows/local/presto_umi.nf:586:48`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
      fastp_reads_json = FASTP.out.json.collect{ meta,json -> json }
                                                 ^^^^
  ```

- Warning: `subworkflows/local/presto_umi.nf:587:48`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
      fastp_reads_html = FASTP.out.html.collect{ meta,html -> html }
                                                 ^^^^
  ```

- Warning: `subworkflows/local/repertoire_analysis_reporting.nf:31:19`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_versions = Channel.empty()
                    ^^^^^^^
  ```

- Warning: `subworkflows/local/repertoire_analysis_reporting.nf:51:26`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
          ch_parsed_logs = Channel.empty()
                           ^^^^^^^
  ```

- Warning: `subworkflows/local/rnaseq_input.nf:19:19`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_versions = Channel.empty()
                    ^^^^^^^
  ```

- Warning: `subworkflows/local/rnaseq_input.nf:20:5`: Variable was declared but not used

  ```nextflow
      ch_logs = Channel.empty()
      ^^^^^^^
  ```

- Warning: `subworkflows/local/rnaseq_input.nf:20:15`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_logs = Channel.empty()
                ^^^^^^^
  ```

- Warning: `subworkflows/local/rnaseq_input.nf:95:53`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
                      return [ meta, out_files.find { it.endsWith("${meta.id}_airr.tsv") } ]
                                                      ^^
  ```

- Warning: `subworkflows/local/rnaseq_input.nf:97:53`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
                      return [ meta, out_files.find { it.endsWith("${meta.id}_barcode_airr.tsv") } ]
                                                      ^^
  ```

- Warning: `subworkflows/local/rnaseq_input.nf:120:48`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
      fastp_reads_json = FASTP.out.json.collect{ meta,json -> json }
                                                 ^^^^
  ```

- Warning: `subworkflows/local/rnaseq_input.nf:121:48`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
      fastp_reads_html = FASTP.out.html.collect{ meta,html -> html }
                                                 ^^^^
  ```

- Warning: `subworkflows/local/sc_raw_input.nf:15:19`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_versions = Channel.empty()
                    ^^^^^^^
  ```

- Warning: `subworkflows/local/sc_raw_input.nf:16:5`: Variable was declared but not used

  ```nextflow
      ch_logs = Channel.empty()
      ^^^^^^^
  ```

- Warning: `subworkflows/local/sc_raw_input.nf:16:15`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_logs = Channel.empty()
                ^^^^^^^
  ```

- Warning: `subworkflows/local/sc_raw_input.nf:49:31`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
              ch_sc_reference = Channel.fromPath(params.reference_10x, checkIfExists: true)
                                ^^^^^^^
  ```

- Warning: `subworkflows/local/sc_raw_input.nf:66:42`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
                  [ meta, out_files.find { it.endsWith("airr_rearrangement.tsv") } ]
                                           ^^
  ```

- Warning: `subworkflows/local/sc_raw_input.nf:77:16`: Variable was declared but not used

  ```nextflow
          .set { ch_renamed_tsv }
                 ^^^^^^^^^^^^^^
  ```

- Warning: `subworkflows/local/sequence_assembly.nf:11:1`: Variable was declared but not used

  ```nextflow
  ch_report_rmd = Channel.fromPath(params.report_rmd, checkIfExists: true)
  ^^^^^^^^^^^^^
  ```

- Warning: `subworkflows/local/sequence_assembly.nf:11:17`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
  ch_report_rmd = Channel.fromPath(params.report_rmd, checkIfExists: true)
                  ^^^^^^^
  ```

- Warning: `subworkflows/local/sequence_assembly.nf:12:1`: Variable was declared but not used

  ```nextflow
  ch_report_css = Channel.fromPath(params.report_css, checkIfExists: true)
  ^^^^^^^^^^^^^
  ```

- Warning: `subworkflows/local/sequence_assembly.nf:12:17`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
  ch_report_css = Channel.fromPath(params.report_css, checkIfExists: true)
                  ^^^^^^^
  ```

- Warning: `subworkflows/local/sequence_assembly.nf:62:28`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
          ch_adapter_fasta = Channel.fromPath(params.adapter_fasta, checkIfExists: true)
                             ^^^^^^^
  ```

- Warning: `subworkflows/local/sequence_assembly.nf:72:37`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
                  ch_vprimers_fasta = Channel.fromPath(params.vprimers, checkIfExists: true)
                                      ^^^^^^^
  ```

- Warning: `subworkflows/local/sequence_assembly.nf:77:37`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
                  ch_cprimers_fasta = Channel.fromPath(params.cprimers, checkIfExists: true)
                                      ^^^^^^^
  ```

- Warning: `subworkflows/local/sequence_assembly.nf:85:33`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
              ch_vprimers_fasta = Channel.of([])
                                  ^^^^^^^
  ```

- Warning: `subworkflows/local/sequence_assembly.nf:86:33`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
              ch_cprimers_fasta = Channel.of([])
                                  ^^^^^^^
  ```

- Warning: `subworkflows/local/sequence_assembly.nf:92:35`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
              ch_internal_cregion = Channel.fromPath(params.internal_cregion_sequences, checkIfExists: true)
                                    ^^^^^^^
  ```

- Warning: `subworkflows/local/sequence_assembly.nf:94:35`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
              ch_internal_cregion = Channel.of([])
                                    ^^^^^^^
  ```

- Warning: `subworkflows/local/sequence_assembly.nf:98:33`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
              ch_vprimers_fasta = Channel.fromPath(params.vprimers, checkIfExists: true)
                                  ^^^^^^^
  ```

- Warning: `subworkflows/local/sequence_assembly.nf:103:33`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
              ch_cprimers_fasta = Channel.fromPath(params.cprimers, checkIfExists: true)
                                  ^^^^^^^
  ```

- Warning: `subworkflows/local/sequence_assembly.nf:122:33`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
              ch_vprimers_fasta = Channel.fromPath(params.race_linker, checkIfExists: true)
                                  ^^^^^^^
  ```

- Warning: `subworkflows/local/sequence_assembly.nf:124:33`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
              ch_vprimers_fasta = Channel.of([])
                                  ^^^^^^^
  ```

- Warning: `subworkflows/local/sequence_assembly.nf:129:33`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
              ch_cprimers_fasta = Channel.fromPath(params.cprimers, checkIfExists: true)
                                  ^^^^^^^
  ```

- Warning: `subworkflows/local/sequence_assembly.nf:137:35`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
              ch_internal_cregion = Channel.fromPath(params.internal_cregion_sequences, checkIfExists: true)
                                    ^^^^^^^
  ```

- Warning: `subworkflows/local/sequence_assembly.nf:139:35`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
              ch_internal_cregion = Channel.of([])
                                    ^^^^^^^
  ```

- Warning: `subworkflows/local/sequence_assembly.nf:145:33`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
              ch_vprimers_fasta = Channel.fromPath(params.race_linker, checkIfExists: true)
                                  ^^^^^^^
  ```

- Warning: `subworkflows/local/sequence_assembly.nf:147:33`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
              ch_vprimers_fasta = Channel.of([])
                                  ^^^^^^^
  ```

- Warning: `subworkflows/local/sequence_assembly.nf:152:33`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
              ch_cprimers_fasta = Channel.fromPath(params.cprimers, checkIfExists: true)
                                  ^^^^^^^
  ```

- Warning: `subworkflows/local/sequence_assembly.nf:176:19`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_versions = Channel.empty()
                    ^^^^^^^
  ```

- Warning: `subworkflows/local/sequence_assembly.nf:203:34`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
          ch_presto_pairseq_logs = Channel.empty()
                                   ^^^^^^^
  ```

- Warning: `subworkflows/local/sequence_assembly.nf:204:38`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
          ch_presto_clustersets_logs = Channel.empty()
                                       ^^^^^^^
  ```

- Warning: `subworkflows/local/sequence_assembly.nf:205:41`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
          ch_presto_buildconsensus_logs = Channel.empty()
                                          ^^^^^^^
  ```

- Warning: `subworkflows/local/sequence_assembly.nf:206:48`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
          ch_presto_postconsensus_pairseq_logs = Channel.empty()
                                                 ^^^^^^^
  ```

- Warning: `subworkflows/local/single_cell_qc_and_filtering.nf:8:19`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_versions = Channel.empty()
                    ^^^^^^^
  ```

- Warning: `subworkflows/local/single_cell_qc_and_filtering.nf:9:15`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_logs = Channel.empty()
                ^^^^^^^
  ```

- Warning: `subworkflows/local/translate_embed.nf:13:19`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_versions = Channel.empty()
                    ^^^^^^^
  ```

- Warning: `subworkflows/local/utils_nfcore_airrflow_pipeline/main.nf:32:5`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
      monochrome_logs   // boolean: Do not use coloured log outputs
      ^^^^^^^^^^^^^^^
  ```

- Warning: `subworkflows/local/utils_nfcore_airrflow_pipeline/main.nf:103:5`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      Channel.fromList(samplesheetToList(input, "${projectDir}/assets/schema_input.json"))
      ^^^^^^^
  ```

- Warning: `subworkflows/local/utils_nfcore_airrflow_pipeline/main.nf:105:5`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      Channel.fromPath(input).set{ch_samplesheet}
      ^^^^^^^
  ```

- Warning: `subworkflows/local/vdj_annotation.nf:20:19`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_versions = Channel.empty()
                    ^^^^^^^
  ```

- Warning: `subworkflows/local/vdj_annotation.nf:21:15`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_logs = Channel.empty()
                ^^^^^^^
  ```

- Warning: `workflows/airrflow.nf:14:1`: Variable was declared but not used

  ```nextflow
  ch_multiqc_config        = Channel.fromPath("$projectDir/assets/multiqc_config.yml", checkIfExists: true)
  ^^^^^^^^^^^^^^^^^
  ```

- Warning: `workflows/airrflow.nf:14:28`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
  ch_multiqc_config        = Channel.fromPath("$projectDir/assets/multiqc_config.yml", checkIfExists: true)
                             ^^^^^^^
  ```

- Warning: `workflows/airrflow.nf:15:1`: Variable was declared but not used

  ```nextflow
  ch_multiqc_custom_config = params.multiqc_config ? Channel.fromPath( params.multiqc_config, checkIfExists: true ) : Channel.empty()
  ^^^^^^^^^^^^^^^^^^^^^^^^
  ```

- Warning: `workflows/airrflow.nf:15:52`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
  ch_multiqc_custom_config = params.multiqc_config ? Channel.fromPath( params.multiqc_config, checkIfExists: true ) : Channel.empty()
                                                     ^^^^^^^
  ```

- Warning: `workflows/airrflow.nf:15:117`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
  ch_multiqc_custom_config = params.multiqc_config ? Channel.fromPath( params.multiqc_config, checkIfExists: true ) : Channel.empty()
                                                                                                                      ^^^^^^^
  ```

- Warning: `workflows/airrflow.nf:16:1`: Variable was declared but not used

  ```nextflow
  ch_multiqc_logo          = params.multiqc_logo   ? Channel.fromPath( params.multiqc_logo, checkIfExists: true ) : Channel.empty()
  ^^^^^^^^^^^^^^^
  ```

- Warning: `workflows/airrflow.nf:16:52`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
  ch_multiqc_logo          = params.multiqc_logo   ? Channel.fromPath( params.multiqc_logo, checkIfExists: true ) : Channel.empty()
                                                     ^^^^^^^
  ```

- Warning: `workflows/airrflow.nf:16:115`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
  ch_multiqc_logo          = params.multiqc_logo   ? Channel.fromPath( params.multiqc_logo, checkIfExists: true ) : Channel.empty()
                                                                                                                    ^^^^^^^
  ```

- Warning: `workflows/airrflow.nf:17:1`: Variable was declared but not used

  ```nextflow
  ch_multiqc_custom_methods_description = params.multiqc_methods_description ? file(params.multiqc_methods_description, checkIfExists: true) : file("$projectDir/assets/methods_description_template.yml", checkIfExists: true)
  ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  ```

- Warning: `workflows/airrflow.nf:20:1`: Variable was declared but not used

  ```nextflow
  ch_report_rmd       = Channel.fromPath(params.report_rmd, checkIfExists: true)
  ^^^^^^^^^^^^^
  ```

- Warning: `workflows/airrflow.nf:20:23`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
  ch_report_rmd       = Channel.fromPath(params.report_rmd, checkIfExists: true)
                        ^^^^^^^
  ```

- Warning: `workflows/airrflow.nf:21:1`: Variable was declared but not used

  ```nextflow
  ch_report_css       = Channel.fromPath(params.report_css, checkIfExists: true)
  ^^^^^^^^^^^^^
  ```

- Warning: `workflows/airrflow.nf:21:23`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
  ch_report_css       = Channel.fromPath(params.report_css, checkIfExists: true)
                        ^^^^^^^
  ```

- Warning: `workflows/airrflow.nf:22:1`: Variable was declared but not used

  ```nextflow
  ch_report_logo      = Channel.fromPath(params.report_logo, checkIfExists: true)
  ^^^^^^^^^^^^^^
  ```

- Warning: `workflows/airrflow.nf:22:23`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
  ch_report_logo      = Channel.fromPath(params.report_logo, checkIfExists: true)
                        ^^^^^^^
  ```

- Warning: `workflows/airrflow.nf:23:1`: Variable was declared but not used

  ```nextflow
  ch_report_logo_img  = Channel.fromPath(params.report_logo_img, checkIfExists: true)
  ^^^^^^^^^^^^^^^^^^
  ```

- Warning: `workflows/airrflow.nf:23:23`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
  ch_report_logo_img  = Channel.fromPath(params.report_logo_img, checkIfExists: true)
                        ^^^^^^^
  ```

- Warning: `workflows/airrflow.nf:77:23`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
          ch_versions = Channel.empty()
                        ^^^^^^^
  ```

- Warning: `workflows/airrflow.nf:78:28`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
          ch_reassign_logs = Channel.empty()
                             ^^^^^^^
  ```

- Warning: `workflows/airrflow.nf:79:31`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
          ch_input_check_logs = Channel.empty()
                                ^^^^^^^
  ```

- Warning: `workflows/airrflow.nf:95:17`: Variable was declared but not used

  ```nextflow
                  ch_cellranger_airr                      = SC_RAW_INPUT.out.airr
                  ^^^^^^^^^^^^^^^^^^
  ```

- Warning: `workflows/airrflow.nf:96:17`: Variable was declared but not used

  ```nextflow
                  ch_cellranger_out                       = SC_RAW_INPUT.out.outs
                  ^^^^^^^^^^^^^^^^^
  ```

- Warning: `workflows/airrflow.nf:100:59`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
                  ch_presto_filterseq_logs                = Channel.empty()
                                                            ^^^^^^^
  ```

- Warning: `workflows/airrflow.nf:101:59`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
                  ch_presto_maskprimers_logs              = Channel.empty()
                                                            ^^^^^^^
  ```

- Warning: `workflows/airrflow.nf:102:59`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
                  ch_presto_pairseq_logs                  = Channel.empty()
                                                            ^^^^^^^
  ```

- Warning: `workflows/airrflow.nf:103:59`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
                  ch_presto_clustersets_logs              = Channel.empty()
                                                            ^^^^^^^
  ```

- Warning: `workflows/airrflow.nf:104:59`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
                  ch_presto_buildconsensus_logs           = Channel.empty()
                                                            ^^^^^^^
  ```

- Warning: `workflows/airrflow.nf:105:59`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
                  ch_presto_postconsensus_pairseq_logs    = Channel.empty()
                                                            ^^^^^^^
  ```

- Warning: `workflows/airrflow.nf:106:59`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
                  ch_presto_assemblepairs_logs            = Channel.empty()
                                                            ^^^^^^^
  ```

- Warning: `workflows/airrflow.nf:107:59`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
                  ch_presto_collapseseq_logs              = Channel.empty()
                                                            ^^^^^^^
  ```

- Warning: `workflows/airrflow.nf:108:59`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
                  ch_presto_splitseq_logs                 = Channel.empty()
                                                            ^^^^^^^
  ```

- Warning: `workflows/airrflow.nf:109:59`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
                  ch_fastp_html                           = Channel.empty()
                                                            ^^^^^^^
  ```

- Warning: `workflows/airrflow.nf:110:59`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
                  ch_fastp_json                           = Channel.empty()
                                                            ^^^^^^^
  ```

- Warning: `workflows/airrflow.nf:111:59`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
                  ch_fastqc_postassembly_mqc              = Channel.empty()
                                                            ^^^^^^^
  ```

- Warning: `workflows/airrflow.nf:112:59`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
                  ch_tsv_files                            = Channel.empty()
                                                            ^^^^^^^
  ```

- Warning: `workflows/airrflow.nf:127:59`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
                  ch_presto_filterseq_logs                = Channel.empty()
                                                            ^^^^^^^
  ```

- Warning: `workflows/airrflow.nf:128:59`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
                  ch_presto_maskprimers_logs              = Channel.empty()
                                                            ^^^^^^^
  ```

- Warning: `workflows/airrflow.nf:129:59`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
                  ch_presto_pairseq_logs                  = Channel.empty()
                                                            ^^^^^^^
  ```

- Warning: `workflows/airrflow.nf:130:59`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
                  ch_presto_clustersets_logs              = Channel.empty()
                                                            ^^^^^^^
  ```

- Warning: `workflows/airrflow.nf:131:59`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
                  ch_presto_buildconsensus_logs           = Channel.empty()
                                                            ^^^^^^^
  ```

- Warning: `workflows/airrflow.nf:132:59`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
                  ch_presto_postconsensus_pairseq_logs    = Channel.empty()
                                                            ^^^^^^^
  ```

- Warning: `workflows/airrflow.nf:133:59`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
                  ch_presto_assemblepairs_logs            = Channel.empty()
                                                            ^^^^^^^
  ```

- Warning: `workflows/airrflow.nf:134:59`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
                  ch_presto_collapseseq_logs              = Channel.empty()
                                                            ^^^^^^^
  ```

- Warning: `workflows/airrflow.nf:135:59`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
                  ch_presto_splitseq_logs                 = Channel.empty()
                                                            ^^^^^^^
  ```

- Warning: `workflows/airrflow.nf:138:59`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
                  ch_fastqc_postassembly_mqc              = Channel.empty()
                                                            ^^^^^^^
  ```

- Warning: `workflows/airrflow.nf:139:59`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
                  ch_tsv_files                            = Channel.empty()
                                                            ^^^^^^^
  ```

- Warning: `workflows/airrflow.nf:162:59`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
                  ch_tsv_files                            = Channel.empty()
                                                            ^^^^^^^
  ```

- Warning: `workflows/airrflow.nf:183:32`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
                  ch_tsv_files = Channel.empty()
                                 ^^^^^^^
  ```

- Warning: `workflows/airrflow.nf:185:37`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
                  ch_fasta_from_tsv = Channel.empty()
                                      ^^^^^^^
  ```

- Warning: `workflows/airrflow.nf:192:52`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
              ch_presto_filterseq_logs             = Channel.empty()
                                                     ^^^^^^^
  ```

- Warning: `workflows/airrflow.nf:193:52`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
              ch_presto_maskprimers_logs           = Channel.empty()
                                                     ^^^^^^^
  ```

- Warning: `workflows/airrflow.nf:194:52`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
              ch_presto_pairseq_logs               = Channel.empty()
                                                     ^^^^^^^
  ```

- Warning: `workflows/airrflow.nf:195:52`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
              ch_presto_clustersets_logs           = Channel.empty()
                                                     ^^^^^^^
  ```

- Warning: `workflows/airrflow.nf:196:52`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
              ch_presto_buildconsensus_logs        = Channel.empty()
                                                     ^^^^^^^
  ```

- Warning: `workflows/airrflow.nf:197:52`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
              ch_presto_postconsensus_pairseq_logs = Channel.empty()
                                                     ^^^^^^^
  ```

- Warning: `workflows/airrflow.nf:198:52`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
              ch_presto_assemblepairs_logs         = Channel.empty()
                                                     ^^^^^^^
  ```

- Warning: `workflows/airrflow.nf:199:52`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
              ch_presto_collapseseq_logs           = Channel.empty()
                                                     ^^^^^^^
  ```

- Warning: `workflows/airrflow.nf:200:52`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
              ch_presto_splitseq_logs              = Channel.empty()
                                                     ^^^^^^^
  ```

- Warning: `workflows/airrflow.nf:201:52`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
              ch_fastp_html                        = Channel.empty()
                                                     ^^^^^^^
  ```

- Warning: `workflows/airrflow.nf:202:52`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
              ch_fastp_json                        = Channel.empty()
                                                     ^^^^^^^
  ```

- Warning: `workflows/airrflow.nf:203:52`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
              ch_fastqc_postassembly_mqc           = Channel.empty()
                                                     ^^^^^^^
  ```

- Warning: `workflows/airrflow.nf:306:26`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      def topic_versions = Channel.topic("versions")
                           ^^^^^^^
  ```

- Warning: `workflows/airrflow.nf:337:35`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
              ch_workflow_summary = Channel.value(paramsSummaryMultiqc(summary_params))
                                    ^^^^^^^
  ```

- Warning: `workflows/airrflow.nf:340:39`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
              ch_methods_description  = Channel.value(methodsDescriptionText(ch_multiqc_custom_methods_description))
                                        ^^^^^^^
  ```

- Warning: `workflows/airrflow.nf:342:32`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
              ch_multiqc_files = Channel.empty()
                                 ^^^^^^^
  ```

- Warning: `workflows/airrflow.nf:348:88`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
              ch_multiqc_files = ch_multiqc_files.mix(ch_fastqc_postassembly_mqc.collect{it[1]}.ifEmpty([]))
                                                                                         ^^
  ```

- Warning: `workflows/airrflow.nf:360:30`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
              multiqc_report = Channel.empty()
                               ^^^^^^^
  ```
