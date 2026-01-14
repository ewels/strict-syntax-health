# Nextflow lint results

- Generated: 2026-01-14T09:21:39.809092515Z
- Nextflow version: 25.12.0-edge
- Summary: 305 errors, 102 warnings

## :x: Errors

- Error: `conf/modules.config:314:128`: Unexpected input: '='

  ```nextflow
              saveAs: { filename -> get_saveas_path(meta, task, filename, "panel_resources/${filename}", panel_resource_creation = true) },
                                                                                                                                 ^
  ```

- Error: `main.nf:84:20`: Unexpected input: '='

  ```nextflow
      if (run_mode === Constants.RunMode.PREPARE_REFERENCE)  {
                     ^
  ```

- Error: `modules/local/lilac/main.nf:82:9`: `Sys` is not defined

  ```nextflow
          Sys.exit(1)
          ^^^
  ```

- Error: `modules/local/orange/main.nf:60:39`: Unexpected input: '='

  ```nextflow
      def experiment_type = (run_mode === Constants.RunMode.WGTS) ? 'WGS' : 'PANEL'
                                        ^
  ```

- Error: `modules/local/wisp/main.nf:34:32`: `Utils` is not defined

  ```nextflow
      def purity_estimate_mode = Utils.getEnumFromString(params.purity_estimate_mode, Constants.RunMode)
                                 ^^^^^
  ```

- Error: `modules/local/wisp/main.nf:34:85`: `Constants` is not defined

  ```nextflow
      def purity_estimate_mode = Utils.getEnumFromString(params.purity_estimate_mode, Constants.RunMode)
                                                                                      ^^^^^^^^^
  ```

- Error: `modules/local/wisp/main.nf:60:21`: `primary_amber_dir` is not defined

  ```nextflow
          for fp in ${primary_amber_dir}/*.amber.*; do ln -sf ../\$fp amber_dir__prepared/; done
                      ^^^^^^^^^^^^^^^^^
  ```

- Error: `modules/local/wisp/main.nf:61:21`: `sample_amber_dir` is not defined

  ```nextflow
          for fp in ${sample_amber_dir}/*.amber.*;  do ln -sf ../\$fp amber_dir__prepared/; done
                      ^^^^^^^^^^^^^^^^
  ```

- Error: `modules/nf-core/bwa/index/main.nf:15:10`: `bwa_index` is not defined

  ```nextflow
      path bwa_index     , emit: index
           ^^^^^^^^^
  ```

- Error: `subworkflows/local/amber_profiling/main.nf:5:1`: Groovy `import` declarations are not supported -- use fully-qualified name inline instead

  ```nextflow
  import Constants
  ^^^^^^^^^^^^^^^^
  ```

- Error: `subworkflows/local/amber_profiling/main.nf:6:1`: Groovy `import` declarations are not supported -- use fully-qualified name inline instead

  ```nextflow
  import Utils
  ^^^^^^^^^^^^
  ```

- Error: `subworkflows/local/amber_profiling/main.nf:32:24`: `WorkflowOncoanalyser` is not defined

  ```nextflow
      ch_inputs_sorted = WorkflowOncoanalyser.groupByMeta(
                         ^^^^^^^^^^^^^^^^^^^^
  ```

- Error: `subworkflows/local/amber_profiling/main.nf:40:17`: `Utils` is not defined

  ```nextflow
                  Utils.selectCurrentOrExisting(tumor_bam, meta, Constants.INPUT.BAM_REDUX_DNA_TUMOR),
                  ^^^^^
  ```

- Error: `subworkflows/local/amber_profiling/main.nf:40:64`: `Constants` is not defined

  ```nextflow
                  Utils.selectCurrentOrExisting(tumor_bam, meta, Constants.INPUT.BAM_REDUX_DNA_TUMOR),
                                                                 ^^^^^^^^^
  ```

- Error: `subworkflows/local/amber_profiling/main.nf:41:30`: `Utils` is not defined

  ```nextflow
                  tumor_bai ?: Utils.getInput(meta, Constants.INPUT.BAI_DNA_TUMOR),
                               ^^^^^
  ```

- Error: `subworkflows/local/amber_profiling/main.nf:41:51`: `Constants` is not defined

  ```nextflow
                  tumor_bai ?: Utils.getInput(meta, Constants.INPUT.BAI_DNA_TUMOR),
                                                    ^^^^^^^^^
  ```

- Error: `subworkflows/local/amber_profiling/main.nf:43:17`: `Utils` is not defined

  ```nextflow
                  Utils.selectCurrentOrExisting(normal_bam, meta, Constants.INPUT.BAM_REDUX_DNA_NORMAL),
                  ^^^^^
  ```

- Error: `subworkflows/local/amber_profiling/main.nf:43:65`: `Constants` is not defined

  ```nextflow
                  Utils.selectCurrentOrExisting(normal_bam, meta, Constants.INPUT.BAM_REDUX_DNA_NORMAL),
                                                                  ^^^^^^^^^
  ```

- Error: `subworkflows/local/amber_profiling/main.nf:44:31`: `Utils` is not defined

  ```nextflow
                  normal_bai ?: Utils.getInput(meta, Constants.INPUT.BAI_DNA_NORMAL),
                                ^^^^^
  ```

- Error: `subworkflows/local/amber_profiling/main.nf:44:52`: `Constants` is not defined

  ```nextflow
                  normal_bai ?: Utils.getInput(meta, Constants.INPUT.BAI_DNA_NORMAL),
                                                     ^^^^^^^^^
  ```

- Error: `subworkflows/local/amber_profiling/main.nf:46:17`: `Utils` is not defined

  ```nextflow
                  Utils.selectCurrentOrExisting(donor_bam, meta, Constants.INPUT.BAM_REDUX_DNA_DONOR),
                  ^^^^^
  ```

- Error: `subworkflows/local/amber_profiling/main.nf:46:64`: `Constants` is not defined

  ```nextflow
                  Utils.selectCurrentOrExisting(donor_bam, meta, Constants.INPUT.BAM_REDUX_DNA_DONOR),
                                                                 ^^^^^^^^^
  ```

- Error: `subworkflows/local/amber_profiling/main.nf:47:30`: `Utils` is not defined

  ```nextflow
                  donor_bai ?: Utils.getInput(meta, Constants.INPUT.BAI_DNA_DONOR),
                               ^^^^^
  ```

- Error: `subworkflows/local/amber_profiling/main.nf:47:51`: `Constants` is not defined

  ```nextflow
                  donor_bai ?: Utils.getInput(meta, Constants.INPUT.BAI_DNA_DONOR),
                                                    ^^^^^^^^^
  ```

- Error: `subworkflows/local/amber_profiling/main.nf:51:32`: `Utils` is not defined

  ```nextflow
              def has_existing = Utils.hasExistingInput(meta, Constants.INPUT.AMBER_DIR)
                                 ^^^^^
  ```

- Error: `subworkflows/local/amber_profiling/main.nf:51:61`: `Constants` is not defined

  ```nextflow
              def has_existing = Utils.hasExistingInput(meta, Constants.INPUT.AMBER_DIR)
                                                              ^^^^^^^^^
  ```

- Error: `subworkflows/local/amber_profiling/main.nf:55:39`: `Utils` is not defined

  ```nextflow
              def longitudinal_sample = Utils.getTumorDnaSample(meta).containsKey('longitudinal_sample_id')
                                        ^^^^^
  ```

- Error: `subworkflows/local/amber_profiling/main.nf:72:27`: `Utils` is not defined

  ```nextflow
                  tumor_id: Utils.getTumorDnaSampleName(meta),
                            ^^^^^
  ```

- Error: `subworkflows/local/amber_profiling/main.nf:76:40`: `Utils` is not defined

  ```nextflow
                  meta_amber.normal_id = Utils.getNormalDnaSampleName(meta)
                                         ^^^^^
  ```

- Error: `subworkflows/local/amber_profiling/main.nf:80:39`: `Utils` is not defined

  ```nextflow
                  meta_amber.donor_id = Utils.getDonorDnaSampleName(meta)
                                        ^^^^^
  ```

- Error: `subworkflows/local/amber_profiling/main.nf:101:13`: `WorkflowOncoanalyser` is not defined

  ```nextflow
              WorkflowOncoanalyser.restoreMeta(AMBER.out.amber_dir, ch_inputs),
              ^^^^^^^^^^^^^^^^^^^^
  ```

- Error: `subworkflows/local/bamtools_metrics/main.nf:5:1`: Groovy `import` declarations are not supported -- use fully-qualified name inline instead

  ```nextflow
  import Constants
  ^^^^^^^^^^^^^^^^
  ```

- Error: `subworkflows/local/bamtools_metrics/main.nf:6:1`: Groovy `import` declarations are not supported -- use fully-qualified name inline instead

  ```nextflow
  import Utils
  ^^^^^^^^^^^^
  ```

- Error: `subworkflows/local/bamtools_metrics/main.nf:36:17`: `Utils` is not defined

  ```nextflow
                  Utils.selectCurrentOrExisting(bam, meta, Constants.INPUT.BAM_REDUX_DNA_TUMOR),
                  ^^^^^
  ```

- Error: `subworkflows/local/bamtools_metrics/main.nf:36:58`: `Constants` is not defined

  ```nextflow
                  Utils.selectCurrentOrExisting(bam, meta, Constants.INPUT.BAM_REDUX_DNA_TUMOR),
                                                           ^^^^^^^^^
  ```

- Error: `subworkflows/local/bamtools_metrics/main.nf:37:24`: `Utils` is not defined

  ```nextflow
                  bai ?: Utils.getInput(meta, Constants.INPUT.BAI_DNA_TUMOR),
                         ^^^^^
  ```

- Error: `subworkflows/local/bamtools_metrics/main.nf:37:45`: `Constants` is not defined

  ```nextflow
                  bai ?: Utils.getInput(meta, Constants.INPUT.BAI_DNA_TUMOR),
                                              ^^^^^^^^^
  ```

- Error: `subworkflows/local/bamtools_metrics/main.nf:41:32`: `Utils` is not defined

  ```nextflow
              def has_existing = Utils.hasExistingInput(meta, Constants.INPUT.BAMTOOLS_DIR_TUMOR)
                                 ^^^^^
  ```

- Error: `subworkflows/local/bamtools_metrics/main.nf:41:61`: `Constants` is not defined

  ```nextflow
              def has_existing = Utils.hasExistingInput(meta, Constants.INPUT.BAMTOOLS_DIR_TUMOR)
                                                              ^^^^^^^^^
  ```

- Error: `subworkflows/local/bamtools_metrics/main.nf:53:17`: `Utils` is not defined

  ```nextflow
                  Utils.selectCurrentOrExisting(bam, meta, Constants.INPUT.BAM_REDUX_DNA_NORMAL),
                  ^^^^^
  ```

- Error: `subworkflows/local/bamtools_metrics/main.nf:53:58`: `Constants` is not defined

  ```nextflow
                  Utils.selectCurrentOrExisting(bam, meta, Constants.INPUT.BAM_REDUX_DNA_NORMAL),
                                                           ^^^^^^^^^
  ```

- Error: `subworkflows/local/bamtools_metrics/main.nf:54:24`: `Utils` is not defined

  ```nextflow
                  bai ?: Utils.getInput(meta, Constants.INPUT.BAI_DNA_NORMAL),
                         ^^^^^
  ```

- Error: `subworkflows/local/bamtools_metrics/main.nf:54:45`: `Constants` is not defined

  ```nextflow
                  bai ?: Utils.getInput(meta, Constants.INPUT.BAI_DNA_NORMAL),
                                              ^^^^^^^^^
  ```

- Error: `subworkflows/local/bamtools_metrics/main.nf:58:32`: `Utils` is not defined

  ```nextflow
              def has_existing = Utils.hasExistingInput(meta, Constants.INPUT.BAMTOOLS_DIR_NORMAL)
                                 ^^^^^
  ```

- Error: `subworkflows/local/bamtools_metrics/main.nf:58:61`: `Constants` is not defined

  ```nextflow
              def has_existing = Utils.hasExistingInput(meta, Constants.INPUT.BAMTOOLS_DIR_NORMAL)
                                                              ^^^^^^^^^
  ```

- Error: `subworkflows/local/bamtools_metrics/main.nf:68:76`: `Utils` is not defined

  ```nextflow
              ch_inputs_tumor_sorted.runnable.map { meta, bam, bai -> [meta, Utils.getTumorDnaSample(meta), 'tumor', bam, bai] },
                                                                             ^^^^^
  ```

- Error: `subworkflows/local/bamtools_metrics/main.nf:69:77`: `Utils` is not defined

  ```nextflow
              ch_inputs_normal_sorted.runnable.map { meta, bam, bai -> [meta, Utils.getNormalDnaSample(meta), 'normal', bam, bai] },
                                                                              ^^^^^
  ```

- Error: `subworkflows/local/bamtools_metrics/main.nf:108:13`: `WorkflowOncoanalyser` is not defined

  ```nextflow
              WorkflowOncoanalyser.restoreMeta(ch_bamtools_out.tumor, ch_inputs),
              ^^^^^^^^^^^^^^^^^^^^
  ```

- Error: `subworkflows/local/bamtools_metrics/main.nf:114:13`: `WorkflowOncoanalyser` is not defined

  ```nextflow
              WorkflowOncoanalyser.restoreMeta(ch_bamtools_out.normal, ch_inputs),
              ^^^^^^^^^^^^^^^^^^^^
  ```

- Error: `subworkflows/local/chord_prediction/main.nf:5:1`: Groovy `import` declarations are not supported -- use fully-qualified name inline instead

  ```nextflow
  import Constants
  ^^^^^^^^^^^^^^^^
  ```

- Error: `subworkflows/local/chord_prediction/main.nf:6:1`: Groovy `import` declarations are not supported -- use fully-qualified name inline instead

  ```nextflow
  import Utils
  ^^^^^^^^^^^^
  ```

- Error: `subworkflows/local/chord_prediction/main.nf:28:27`: `Utils` is not defined

  ```nextflow
              return [meta, Utils.selectCurrentOrExisting(purple_dir, meta, Constants.INPUT.PURPLE_DIR)]
                            ^^^^^
  ```

- Error: `subworkflows/local/chord_prediction/main.nf:28:75`: `Constants` is not defined

  ```nextflow
              return [meta, Utils.selectCurrentOrExisting(purple_dir, meta, Constants.INPUT.PURPLE_DIR)]
                                                                            ^^^^^^^^^
  ```

- Error: `subworkflows/local/chord_prediction/main.nf:37:27`: `Utils` is not defined

  ```nextflow
              def has_dna = Utils.hasTumorDna(meta)
                            ^^^^^
  ```

- Error: `subworkflows/local/chord_prediction/main.nf:44:28`: `Utils` is not defined

  ```nextflow
                  tumor_id = Utils.getTumorDnaSampleName(meta)
                             ^^^^^
  ```

- Error: `subworkflows/local/chord_prediction/main.nf:49:32`: `Utils` is not defined

  ```nextflow
              def has_existing = Utils.hasExistingInput(meta, Constants.INPUT.CHORD_DIR)
                                 ^^^^^
  ```

- Error: `subworkflows/local/chord_prediction/main.nf:49:61`: `Constants` is not defined

  ```nextflow
              def has_existing = Utils.hasExistingInput(meta, Constants.INPUT.CHORD_DIR)
                                                              ^^^^^^^^^
  ```

- Error: `subworkflows/local/chord_prediction/main.nf:61:28`: `Utils` is not defined

  ```nextflow
              def tumor_id = Utils.getTumorDnaSampleName(meta)
                             ^^^^^
  ```

- Error: `subworkflows/local/chord_prediction/main.nf:89:13`: `WorkflowOncoanalyser` is not defined

  ```nextflow
              WorkflowOncoanalyser.restoreMeta(CHORD.out.chord_dir, ch_inputs),
              ^^^^^^^^^^^^^^^^^^^^
  ```

- Error: `subworkflows/local/cider_calling/main.nf:5:1`: Groovy `import` declarations are not supported -- use fully-qualified name inline instead

  ```nextflow
  import Constants
  ^^^^^^^^^^^^^^^^
  ```

- Error: `subworkflows/local/cider_calling/main.nf:6:1`: Groovy `import` declarations are not supported -- use fully-qualified name inline instead

  ```nextflow
  import Utils
  ^^^^^^^^^^^^
  ```

- Error: `subworkflows/local/cider_calling/main.nf:35:17`: `Utils` is not defined

  ```nextflow
                  Utils.selectCurrentOrExisting(bam, meta, Constants.INPUT.BAM_REDUX_DNA_TUMOR),
                  ^^^^^
  ```

- Error: `subworkflows/local/cider_calling/main.nf:35:58`: `Constants` is not defined

  ```nextflow
                  Utils.selectCurrentOrExisting(bam, meta, Constants.INPUT.BAM_REDUX_DNA_TUMOR),
                                                           ^^^^^^^^^
  ```

- Error: `subworkflows/local/cider_calling/main.nf:36:24`: `Utils` is not defined

  ```nextflow
                  bai ?: Utils.getInput(meta, Constants.INPUT.BAI_DNA_TUMOR),
                         ^^^^^
  ```

- Error: `subworkflows/local/cider_calling/main.nf:36:45`: `Constants` is not defined

  ```nextflow
                  bai ?: Utils.getInput(meta, Constants.INPUT.BAI_DNA_TUMOR),
                                              ^^^^^^^^^
  ```

- Error: `subworkflows/local/cider_calling/main.nf:51:17`: `Utils` is not defined

  ```nextflow
                  Utils.selectCurrentOrExisting(bam, meta, Constants.INPUT.BAM_RNA_TUMOR),
                  ^^^^^
  ```

- Error: `subworkflows/local/cider_calling/main.nf:51:58`: `Constants` is not defined

  ```nextflow
                  Utils.selectCurrentOrExisting(bam, meta, Constants.INPUT.BAM_RNA_TUMOR),
                                                           ^^^^^^^^^
  ```

- Error: `subworkflows/local/cider_calling/main.nf:52:24`: `Utils` is not defined

  ```nextflow
                  bai ?: Utils.getInput(meta, Constants.INPUT.BAI_RNA_TUMOR),
                         ^^^^^
  ```

- Error: `subworkflows/local/cider_calling/main.nf:52:45`: `Constants` is not defined

  ```nextflow
                  bai ?: Utils.getInput(meta, Constants.INPUT.BAI_RNA_TUMOR),
                                              ^^^^^^^^^
  ```

- Error: `subworkflows/local/cider_calling/main.nf:65:80`: `Utils` is not defined

  ```nextflow
              ch_inputs_tumor_dna_sorted.runnable.map { meta, bam, bai -> [meta, Utils.getTumorDnaSample(meta), bam, bai] },
                                                                                 ^^^^^
  ```

- Error: `subworkflows/local/cider_calling/main.nf:66:80`: `Utils` is not defined

  ```nextflow
              ch_inputs_tumor_rna_sorted.runnable.map { meta, bam, bai -> [meta, Utils.getTumorRnaSample(meta), bam, bai] },
                                                                                 ^^^^^
  ```

- Error: `subworkflows/local/cobalt_normalisation/main.nf:5:1`: Groovy `import` declarations are not supported -- use fully-qualified name inline instead

  ```nextflow
  import Constants
  ^^^^^^^^^^^^^^^^
  ```

- Error: `subworkflows/local/cobalt_normalisation/main.nf:6:1`: Groovy `import` declarations are not supported -- use fully-qualified name inline instead

  ```nextflow
  import Utils
  ^^^^^^^^^^^^
  ```

- Error: `subworkflows/local/cobalt_normalisation/main.nf:28:24`: `WorkflowOncoanalyser` is not defined

  ```nextflow
      ch_cobalt_inputs = WorkflowOncoanalyser.groupByMeta(
                         ^^^^^^^^^^^^^^^^^^^^
  ```

- Error: `subworkflows/local/cobalt_normalisation/main.nf:34:17`: `Utils` is not defined

  ```nextflow
                  Utils.selectCurrentOrExisting(amber_dir, meta, Constants.INPUT.AMBER_DIR),
                  ^^^^^
  ```

- Error: `subworkflows/local/cobalt_normalisation/main.nf:34:64`: `Constants` is not defined

  ```nextflow
                  Utils.selectCurrentOrExisting(amber_dir, meta, Constants.INPUT.AMBER_DIR),
                                                                 ^^^^^^^^^
  ```

- Error: `subworkflows/local/cobalt_normalisation/main.nf:35:17`: `Utils` is not defined

  ```nextflow
                  Utils.selectCurrentOrExisting(cobalt_dir, meta, Constants.INPUT.COBALT_DIR),
                  ^^^^^
  ```

- Error: `subworkflows/local/cobalt_normalisation/main.nf:35:65`: `Constants` is not defined

  ```nextflow
                  Utils.selectCurrentOrExisting(cobalt_dir, meta, Constants.INPUT.COBALT_DIR),
                                                                  ^^^^^^^^^
  ```

- Error: `subworkflows/local/cobalt_profiling/main.nf:59:49`: Unexpected input: '\*'

  ```nextflow
              ch_inputs_sorted.runnable_tn.map { [*it, []] },
                                                  ^
  ```

- Error: `subworkflows/local/cuppa_prediction/main.nf:46:27`: Unexpected input: '\*'

  ```nextflow
              return [meta, *inputs]
                            ^
  ```

- Error: `subworkflows/local/esvee_calling/main.nf:62:49`: Unexpected input: '\*'

  ```nextflow
              ch_inputs_sorted.runnable_to.map { [*it, [], []] },
                                                  ^
  ```

- Error: `subworkflows/local/isofox_normalisation/main.nf:5:1`: Groovy `import` declarations are not supported -- use fully-qualified name inline instead

  ```nextflow
  import Constants
  ^^^^^^^^^^^^^^^^
  ```

- Error: `subworkflows/local/isofox_normalisation/main.nf:6:1`: Groovy `import` declarations are not supported -- use fully-qualified name inline instead

  ```nextflow
  import Utils
  ^^^^^^^^^^^^
  ```

- Error: `subworkflows/local/isofox_normalisation/main.nf:29:20`: `Utils` is not defined

  ```nextflow
              return Utils.selectCurrentOrExisting(isofox_dir, meta, Constants.INPUT.ISOFOX_DIR)
                     ^^^^^
  ```

- Error: `subworkflows/local/isofox_normalisation/main.nf:29:68`: `Constants` is not defined

  ```nextflow
              return Utils.selectCurrentOrExisting(isofox_dir, meta, Constants.INPUT.ISOFOX_DIR)
                                                                     ^^^^^^^^^
  ```

- Error: `subworkflows/local/isofox_quantification/main.nf:5:1`: Groovy `import` declarations are not supported -- use fully-qualified name inline instead

  ```nextflow
  import Constants
  ^^^^^^^^^^^^^^^^
  ```

- Error: `subworkflows/local/isofox_quantification/main.nf:6:1`: Groovy `import` declarations are not supported -- use fully-qualified name inline instead

  ```nextflow
  import Utils
  ^^^^^^^^^^^^
  ```

- Error: `subworkflows/local/isofox_quantification/main.nf:43:17`: `Utils` is not defined

  ```nextflow
                  Utils.selectCurrentOrExisting(tumor_bam, meta, Constants.INPUT.BAM_RNA_TUMOR),
                  ^^^^^
  ```

- Error: `subworkflows/local/isofox_quantification/main.nf:43:64`: `Constants` is not defined

  ```nextflow
                  Utils.selectCurrentOrExisting(tumor_bam, meta, Constants.INPUT.BAM_RNA_TUMOR),
                                                                 ^^^^^^^^^
  ```

- Error: `subworkflows/local/isofox_quantification/main.nf:44:17`: `Utils` is not defined

  ```nextflow
                  Utils.selectCurrentOrExisting(tumor_bai, meta, Constants.INPUT.BAI_RNA_TUMOR),
                  ^^^^^
  ```

- Error: `subworkflows/local/isofox_quantification/main.nf:44:64`: `Constants` is not defined

  ```nextflow
                  Utils.selectCurrentOrExisting(tumor_bai, meta, Constants.INPUT.BAI_RNA_TUMOR),
                                                                 ^^^^^^^^^
  ```

- Error: `subworkflows/local/isofox_quantification/main.nf:48:32`: `Utils` is not defined

  ```nextflow
              def has_existing = Utils.hasExistingInput(meta, Constants.INPUT.ISOFOX_DIR)
                                 ^^^^^
  ```

- Error: `subworkflows/local/isofox_quantification/main.nf:48:61`: `Constants` is not defined

  ```nextflow
              def has_existing = Utils.hasExistingInput(meta, Constants.INPUT.ISOFOX_DIR)
                                                              ^^^^^^^^^
  ```

- Error: `subworkflows/local/isofox_quantification/main.nf:62:28`: `Utils` is not defined

  ```nextflow
                  sample_id: Utils.getTumorRnaSampleName(meta),
                             ^^^^^
  ```

- Error: `subworkflows/local/isofox_quantification/main.nf:90:13`: `WorkflowOncoanalyser` is not defined

  ```nextflow
              WorkflowOncoanalyser.restoreMeta(ISOFOX.out.isofox_dir, ch_inputs),
              ^^^^^^^^^^^^^^^^^^^^
  ```

- Error: `subworkflows/local/lilac_calling/main.nf:5:1`: Groovy `import` declarations are not supported -- use fully-qualified name inline instead

  ```nextflow
  import Constants
  ^^^^^^^^^^^^^^^^
  ```

- Error: `subworkflows/local/lilac_calling/main.nf:6:1`: Groovy `import` declarations are not supported -- use fully-qualified name inline instead

  ```nextflow
  import Utils
  ^^^^^^^^^^^^
  ```

- Error: `subworkflows/local/lilac_calling/main.nf:34:28`: `WorkflowOncoanalyser` is not defined

  ```nextflow
      ch_dna_inputs_sorted = WorkflowOncoanalyser.groupByMeta(
                             ^^^^^^^^^^^^^^^^^^^^
  ```

- Error: `subworkflows/local/lilac_calling/main.nf:41:17`: `Utils` is not defined

  ```nextflow
                  Utils.selectCurrentOrExisting(tumor_bam, meta, Constants.INPUT.BAM_REDUX_DNA_TUMOR),
                  ^^^^^
  ```

- Error: `subworkflows/local/lilac_calling/main.nf:41:64`: `Constants` is not defined

  ```nextflow
                  Utils.selectCurrentOrExisting(tumor_bam, meta, Constants.INPUT.BAM_REDUX_DNA_TUMOR),
                                                                 ^^^^^^^^^
  ```

- Error: `subworkflows/local/lilac_calling/main.nf:42:30`: `Utils` is not defined

  ```nextflow
                  tumor_bai ?: Utils.getInput(meta, Constants.INPUT.BAI_DNA_TUMOR),
                               ^^^^^
  ```

- Error: `subworkflows/local/lilac_calling/main.nf:42:51`: `Constants` is not defined

  ```nextflow
                  tumor_bai ?: Utils.getInput(meta, Constants.INPUT.BAI_DNA_TUMOR),
                                                    ^^^^^^^^^
  ```

- Error: `subworkflows/local/lilac_calling/main.nf:43:17`: `Utils` is not defined

  ```nextflow
                  Utils.selectCurrentOrExisting(normal_bam, meta, Constants.INPUT.BAM_REDUX_DNA_NORMAL),
                  ^^^^^
  ```

- Error: `subworkflows/local/lilac_calling/main.nf:43:65`: `Constants` is not defined

  ```nextflow
                  Utils.selectCurrentOrExisting(normal_bam, meta, Constants.INPUT.BAM_REDUX_DNA_NORMAL),
                                                                  ^^^^^^^^^
  ```

- Error: `subworkflows/local/lilac_calling/main.nf:44:31`: `Utils` is not defined

  ```nextflow
                  normal_bai ?: Utils.getInput(meta, Constants.INPUT.BAI_DNA_NORMAL),
                                ^^^^^
  ```

- Error: `subworkflows/local/lilac_calling/main.nf:44:52`: `Constants` is not defined

  ```nextflow
                  normal_bai ?: Utils.getInput(meta, Constants.INPUT.BAI_DNA_NORMAL),
                                                     ^^^^^^^^^
  ```

- Error: `subworkflows/local/lilac_calling/main.nf:49:32`: `Utils` is not defined

  ```nextflow
              def has_existing = Utils.hasExistingInput(meta, Constants.INPUT.LILAC_DIR)
                                 ^^^^^
  ```

- Error: `subworkflows/local/lilac_calling/main.nf:49:61`: `Constants` is not defined

  ```nextflow
              def has_existing = Utils.hasExistingInput(meta, Constants.INPUT.LILAC_DIR)
                                                              ^^^^^^^^^
  ```

- Error: `subworkflows/local/lilac_calling/main.nf:61:23`: `WorkflowOncoanalyser` is not defined

  ```nextflow
      ch_lilac_inputs = WorkflowOncoanalyser.groupByMeta(
                        ^^^^^^^^^^^^^^^^^^^^
  ```

- Error: `subworkflows/local/lilac_calling/main.nf:73:17`: `Utils` is not defined

  ```nextflow
              if (Utils.hasTumorDna(meta)) {
                  ^^^^^
  ```

- Error: `subworkflows/local/lilac_calling/main.nf:74:39`: `Utils` is not defined

  ```nextflow
                  meta_lilac.tumor_id = Utils.getTumorDnaSampleName(meta)
                                        ^^^^^
  ```

- Error: `subworkflows/local/lilac_calling/main.nf:77:17`: `Utils` is not defined

  ```nextflow
              if (Utils.hasNormalDna(meta)) {
                  ^^^^^
  ```

- Error: `subworkflows/local/lilac_calling/main.nf:78:40`: `Utils` is not defined

  ```nextflow
                  meta_lilac.normal_id = Utils.getNormalDnaSampleName(meta)
                                         ^^^^^
  ```

- Error: `subworkflows/local/lilac_calling/main.nf:87:17`: `Utils` is not defined

  ```nextflow
                  Utils.selectCurrentOrExisting(tbam_rna, meta, Constants.INPUT.BAM_RNA_TUMOR),
                  ^^^^^
  ```

- Error: `subworkflows/local/lilac_calling/main.nf:87:63`: `Constants` is not defined

  ```nextflow
                  Utils.selectCurrentOrExisting(tbam_rna, meta, Constants.INPUT.BAM_RNA_TUMOR),
                                                                ^^^^^^^^^
  ```

- Error: `subworkflows/local/lilac_calling/main.nf:88:17`: `Utils` is not defined

  ```nextflow
                  Utils.selectCurrentOrExisting(tbai_rna, meta, Constants.INPUT.BAI_RNA_TUMOR),
                  ^^^^^
  ```

- Error: `subworkflows/local/lilac_calling/main.nf:88:63`: `Constants` is not defined

  ```nextflow
                  Utils.selectCurrentOrExisting(tbai_rna, meta, Constants.INPUT.BAI_RNA_TUMOR),
                                                                ^^^^^^^^^
  ```

- Error: `subworkflows/local/lilac_calling/main.nf:89:17`: `Utils` is not defined

  ```nextflow
                  Utils.selectCurrentOrExisting(purple_dir, meta, Constants.INPUT.PURPLE_DIR),
                  ^^^^^
  ```

- Error: `subworkflows/local/lilac_calling/main.nf:89:65`: `Constants` is not defined

  ```nextflow
                  Utils.selectCurrentOrExisting(purple_dir, meta, Constants.INPUT.PURPLE_DIR),
                                                                  ^^^^^^^^^
  ```

- Error: `subworkflows/local/lilac_calling/main.nf:109:13`: `WorkflowOncoanalyser` is not defined

  ```nextflow
              WorkflowOncoanalyser.restoreMeta(LILAC.out.lilac_dir, ch_inputs),
              ^^^^^^^^^^^^^^^^^^^^
  ```

- Error: `subworkflows/local/linx_annotation/main.nf:5:1`: Groovy `import` declarations are not supported -- use fully-qualified name inline instead

  ```nextflow
  import Constants
  ^^^^^^^^^^^^^^^^
  ```

- Error: `subworkflows/local/linx_annotation/main.nf:6:1`: Groovy `import` declarations are not supported -- use fully-qualified name inline instead

  ```nextflow
  import Utils
  ^^^^^^^^^^^^
  ```

- Error: `subworkflows/local/linx_annotation/main.nf:35:17`: `Utils` is not defined

  ```nextflow
                  Utils.selectCurrentOrExisting(purple_dir, meta, Constants.INPUT.PURPLE_DIR),
                  ^^^^^
  ```

- Error: `subworkflows/local/linx_annotation/main.nf:35:65`: `Constants` is not defined

  ```nextflow
                  Utils.selectCurrentOrExisting(purple_dir, meta, Constants.INPUT.PURPLE_DIR),
                                                                  ^^^^^^^^^
  ```

- Error: `subworkflows/local/linx_annotation/main.nf:53:28`: `Utils` is not defined

  ```nextflow
              def tumor_id = Utils.getTumorDnaSampleName(meta)
                             ^^^^^
  ```

- Error: `subworkflows/local/linx_annotation/main.nf:55:36`: `Utils` is not defined

  ```nextflow
              def has_tumor_normal = Utils.hasTumorDna(meta) && Utils.hasNormalDna(meta)
                                     ^^^^^
  ```

- Error: `subworkflows/local/linx_annotation/main.nf:55:63`: `Utils` is not defined

  ```nextflow
              def has_tumor_normal = Utils.hasTumorDna(meta) && Utils.hasNormalDna(meta)
                                                                ^^^^^
  ```

- Error: `subworkflows/local/linx_annotation/main.nf:57:32`: `Utils` is not defined

  ```nextflow
              def has_existing = Utils.hasExistingInput(meta, Constants.INPUT.LINX_ANNO_DIR_NORMAL)
                                 ^^^^^
  ```

- Error: `subworkflows/local/linx_annotation/main.nf:57:61`: `Constants` is not defined

  ```nextflow
              def has_existing = Utils.hasExistingInput(meta, Constants.INPUT.LINX_ANNO_DIR_NORMAL)
                                                              ^^^^^^^^^
  ```

- Error: `subworkflows/local/linx_annotation/main.nf:69:28`: `Utils` is not defined

  ```nextflow
              def tumor_id = Utils.getTumorDnaSampleName(meta)
                             ^^^^^
  ```

- Error: `subworkflows/local/linx_annotation/main.nf:101:29`: `Utils` is not defined

  ```nextflow
              def has_tumor = Utils.hasTumorDna(meta)
                              ^^^^^
  ```

- Error: `subworkflows/local/linx_annotation/main.nf:102:32`: `Utils` is not defined

  ```nextflow
              def has_existing = Utils.hasExistingInput(meta, Constants.INPUT.LINX_ANNO_DIR_TUMOR)
                                 ^^^^^
  ```

- Error: `subworkflows/local/linx_annotation/main.nf:102:61`: `Constants` is not defined

  ```nextflow
              def has_existing = Utils.hasExistingInput(meta, Constants.INPUT.LINX_ANNO_DIR_TUMOR)
                                                              ^^^^^^^^^
  ```

- Error: `subworkflows/local/linx_annotation/main.nf:117:28`: `Utils` is not defined

  ```nextflow
                  sample_id: Utils.getTumorDnaSampleName(meta),
                             ^^^^^
  ```

- Error: `subworkflows/local/linx_annotation/main.nf:139:13`: `WorkflowOncoanalyser` is not defined

  ```nextflow
              WorkflowOncoanalyser.restoreMeta(LINX_SOMATIC.out.annotation_dir, ch_inputs),
              ^^^^^^^^^^^^^^^^^^^^
  ```

- Error: `subworkflows/local/linx_annotation/main.nf:146:13`: `WorkflowOncoanalyser` is not defined

  ```nextflow
              WorkflowOncoanalyser.restoreMeta(LINX_GERMLINE.out.annotation_dir, ch_inputs),
              ^^^^^^^^^^^^^^^^^^^^
  ```

- Error: `subworkflows/local/linx_plotting/main.nf:5:1`: Groovy `import` declarations are not supported -- use fully-qualified name inline instead

  ```nextflow
  import Constants
  ^^^^^^^^^^^^^^^^
  ```

- Error: `subworkflows/local/linx_plotting/main.nf:6:1`: Groovy `import` declarations are not supported -- use fully-qualified name inline instead

  ```nextflow
  import Utils
  ^^^^^^^^^^^^
  ```

- Error: `subworkflows/local/linx_plotting/main.nf:35:24`: `WorkflowOncoanalyser` is not defined

  ```nextflow
      ch_inputs_sorted = WorkflowOncoanalyser.groupByMeta(
                         ^^^^^^^^^^^^^^^^^^^^
  ```

- Error: `subworkflows/local/linx_plotting/main.nf:45:17`: `Utils` is not defined

  ```nextflow
                  Utils.selectCurrentOrExisting(annotation_dir, meta, Constants.INPUT.LINX_ANNO_DIR_TUMOR),
                  ^^^^^
  ```

- Error: `subworkflows/local/linx_plotting/main.nf:45:69`: `Constants` is not defined

  ```nextflow
                  Utils.selectCurrentOrExisting(annotation_dir, meta, Constants.INPUT.LINX_ANNO_DIR_TUMOR),
                                                                      ^^^^^^^^^
  ```

- Error: `subworkflows/local/linx_plotting/main.nf:46:17`: `Utils` is not defined

  ```nextflow
                  Utils.selectCurrentOrExisting(amber_dir, meta, Constants.INPUT.AMBER_DIR),
                  ^^^^^
  ```

- Error: `subworkflows/local/linx_plotting/main.nf:46:64`: `Constants` is not defined

  ```nextflow
                  Utils.selectCurrentOrExisting(amber_dir, meta, Constants.INPUT.AMBER_DIR),
                                                                 ^^^^^^^^^
  ```

- Error: `subworkflows/local/linx_plotting/main.nf:47:17`: `Utils` is not defined

  ```nextflow
                  Utils.selectCurrentOrExisting(cobalt_dir, meta, Constants.INPUT.COBALT_DIR),
                  ^^^^^
  ```

- Error: `subworkflows/local/linx_plotting/main.nf:47:65`: `Constants` is not defined

  ```nextflow
                  Utils.selectCurrentOrExisting(cobalt_dir, meta, Constants.INPUT.COBALT_DIR),
                                                                  ^^^^^^^^^
  ```

- Error: `subworkflows/local/linx_plotting/main.nf:48:17`: `Utils` is not defined

  ```nextflow
                  Utils.selectCurrentOrExisting(purple_dir, meta, Constants.INPUT.PURPLE_DIR),
                  ^^^^^
  ```

- Error: `subworkflows/local/linx_plotting/main.nf:48:65`: `Constants` is not defined

  ```nextflow
                  Utils.selectCurrentOrExisting(purple_dir, meta, Constants.INPUT.PURPLE_DIR),
                                                                  ^^^^^^^^^
  ```

- Error: `subworkflows/local/linx_plotting/main.nf:53:32`: `Utils` is not defined

  ```nextflow
              def has_existing = Utils.hasExistingInput(meta, Constants.INPUT.LINX_PLOT_DIR_TUMOR)
                                 ^^^^^
  ```

- Error: `subworkflows/local/linx_plotting/main.nf:53:61`: `Constants` is not defined

  ```nextflow
              def has_existing = Utils.hasExistingInput(meta, Constants.INPUT.LINX_PLOT_DIR_TUMOR)
                                                              ^^^^^^^^^
  ```

- Error: `subworkflows/local/linx_plotting/main.nf:71:28`: `Utils` is not defined

  ```nextflow
                  sample_id: Utils.getTumorDnaSampleName(meta),
                             ^^^^^
  ```

- Error: `subworkflows/local/linx_plotting/main.nf:91:27`: `WorkflowOncoanalyser` is not defined

  ```nextflow
      ch_gpgr_linx_inputs = WorkflowOncoanalyser.groupByMeta(
                            ^^^^^^^^^^^^^^^^^^^^
  ```

- Error: `subworkflows/local/linx_plotting/main.nf:93:9`: `WorkflowOncoanalyser` is not defined

  ```nextflow
          WorkflowOncoanalyser.restoreMeta(LINX_VISUALISER.out.plots, ch_inputs),
          ^^^^^^^^^^^^^^^^^^^^
  ```

- Error: `subworkflows/local/linx_plotting/main.nf:100:28`: `Utils` is not defined

  ```nextflow
                  sample_id: Utils.getTumorDnaSampleName(meta),
                             ^^^^^
  ```

- Error: `subworkflows/local/linx_plotting/main.nf:117:13`: `WorkflowOncoanalyser` is not defined

  ```nextflow
              WorkflowOncoanalyser.restoreMeta(LINX_VISUALISER.out.plots, ch_inputs),
              ^^^^^^^^^^^^^^^^^^^^
  ```

- Error: `subworkflows/local/neo_prediction/main.nf:55:27`: Unexpected input: '\*'

  ```nextflow
              return [meta, *inputs]
                            ^
  ```

- Error: `subworkflows/local/orange_reporting/main.nf:125:27`: Unexpected input: '\*'

  ```nextflow
              return [meta, *inputs_selected]
                            ^
  ```

- Error: `subworkflows/local/pave_annotation/main.nf:5:1`: Groovy `import` declarations are not supported -- use fully-qualified name inline instead

  ```nextflow
  import Constants
  ^^^^^^^^^^^^^^^^
  ```

- Error: `subworkflows/local/pave_annotation/main.nf:6:1`: Groovy `import` declarations are not supported -- use fully-qualified name inline instead

  ```nextflow
  import Utils
  ^^^^^^^^^^^^
  ```

- Error: `subworkflows/local/pave_annotation/main.nf:46:17`: `Utils` is not defined

  ```nextflow
                  Utils.selectCurrentOrExisting(sage_vcf, meta, Constants.INPUT.SAGE_VCF_NORMAL),
                  ^^^^^
  ```

- Error: `subworkflows/local/pave_annotation/main.nf:46:63`: `Constants` is not defined

  ```nextflow
                  Utils.selectCurrentOrExisting(sage_vcf, meta, Constants.INPUT.SAGE_VCF_NORMAL),
                                                                ^^^^^^^^^
  ```

- Error: `subworkflows/local/pave_annotation/main.nf:47:17`: `Utils` is not defined

  ```nextflow
                  Utils.selectCurrentOrExisting(sage_tbi, meta, Constants.INPUT.SAGE_VCF_TBI_NORMAL),
                  ^^^^^
  ```

- Error: `subworkflows/local/pave_annotation/main.nf:47:63`: `Constants` is not defined

  ```nextflow
                  Utils.selectCurrentOrExisting(sage_tbi, meta, Constants.INPUT.SAGE_VCF_TBI_NORMAL),
                                                                ^^^^^^^^^
  ```

- Error: `subworkflows/local/pave_annotation/main.nf:52:32`: `Utils` is not defined

  ```nextflow
              def has_existing = Utils.hasExistingInput(meta, Constants.INPUT.PAVE_VCF_NORMAL)
                                 ^^^^^
  ```

- Error: `subworkflows/local/pave_annotation/main.nf:52:61`: `Constants` is not defined

  ```nextflow
              def has_existing = Utils.hasExistingInput(meta, Constants.INPUT.PAVE_VCF_NORMAL)
                                                              ^^^^^^^^^
  ```

- Error: `subworkflows/local/pave_annotation/main.nf:54:23`: `Utils` is not defined

  ```nextflow
              runnable: Utils.hasTumorDna(meta) && Utils.hasNormalDna(meta) && sage_vcf && !has_existing
                        ^^^^^
  ```

- Error: `subworkflows/local/pave_annotation/main.nf:54:50`: `Utils` is not defined

  ```nextflow
              runnable: Utils.hasTumorDna(meta) && Utils.hasNormalDna(meta) && sage_vcf && !has_existing
                                                   ^^^^^
  ```

- Error: `subworkflows/local/pave_annotation/main.nf:67:28`: `Utils` is not defined

  ```nextflow
                  sample_id: Utils.getTumorDnaSampleName(meta),
                             ^^^^^
  ```

- Error: `subworkflows/local/pave_annotation/main.nf:99:17`: `Utils` is not defined

  ```nextflow
                  Utils.selectCurrentOrExisting(sage_vcf, meta, Constants.INPUT.SAGE_VCF_TUMOR),
                  ^^^^^
  ```

- Error: `subworkflows/local/pave_annotation/main.nf:99:63`: `Constants` is not defined

  ```nextflow
                  Utils.selectCurrentOrExisting(sage_vcf, meta, Constants.INPUT.SAGE_VCF_TUMOR),
                                                                ^^^^^^^^^
  ```

- Error: `subworkflows/local/pave_annotation/main.nf:100:17`: `Utils` is not defined

  ```nextflow
                  Utils.selectCurrentOrExisting(sage_tbi, meta, Constants.INPUT.SAGE_VCF_TBI_TUMOR),
                  ^^^^^
  ```

- Error: `subworkflows/local/pave_annotation/main.nf:100:63`: `Constants` is not defined

  ```nextflow
                  Utils.selectCurrentOrExisting(sage_tbi, meta, Constants.INPUT.SAGE_VCF_TBI_TUMOR),
                                                                ^^^^^^^^^
  ```

- Error: `subworkflows/local/pave_annotation/main.nf:105:32`: `Utils` is not defined

  ```nextflow
              def has_existing = Utils.hasExistingInput(meta, Constants.INPUT.PAVE_VCF_TUMOR)
                                 ^^^^^
  ```

- Error: `subworkflows/local/pave_annotation/main.nf:105:61`: `Constants` is not defined

  ```nextflow
              def has_existing = Utils.hasExistingInput(meta, Constants.INPUT.PAVE_VCF_TUMOR)
                                                              ^^^^^^^^^
  ```

- Error: `subworkflows/local/pave_annotation/main.nf:107:23`: `Utils` is not defined

  ```nextflow
              runnable: Utils.hasTumorDna(meta) && sage_vcf && !has_existing
                        ^^^^^
  ```

- Error: `subworkflows/local/pave_annotation/main.nf:120:28`: `Utils` is not defined

  ```nextflow
                  sample_id: Utils.getTumorDnaSampleName(meta),
                             ^^^^^
  ```

- Error: `subworkflows/local/pave_annotation/main.nf:147:13`: `WorkflowOncoanalyser` is not defined

  ```nextflow
              WorkflowOncoanalyser.restoreMeta(PAVE_SOMATIC.out.vcf, ch_inputs),
              ^^^^^^^^^^^^^^^^^^^^
  ```

- Error: `subworkflows/local/pave_annotation/main.nf:153:13`: `WorkflowOncoanalyser` is not defined

  ```nextflow
              WorkflowOncoanalyser.restoreMeta(PAVE_GERMLINE.out.vcf, ch_inputs),
              ^^^^^^^^^^^^^^^^^^^^
  ```

- Error: `subworkflows/local/pave_pon_creation/main.nf:5:1`: Groovy `import` declarations are not supported -- use fully-qualified name inline instead

  ```nextflow
  import Constants
  ^^^^^^^^^^^^^^^^
  ```

- Error: `subworkflows/local/pave_pon_creation/main.nf:6:1`: Groovy `import` declarations are not supported -- use fully-qualified name inline instead

  ```nextflow
  import Utils
  ^^^^^^^^^^^^
  ```

- Error: `subworkflows/local/pave_pon_creation/main.nf:29:17`: `Utils` is not defined

  ```nextflow
                  Utils.selectCurrentOrExisting(sage_vcf, meta, Constants.INPUT.SAGE_VCF_TUMOR),
                  ^^^^^
  ```

- Error: `subworkflows/local/pave_pon_creation/main.nf:29:63`: `Constants` is not defined

  ```nextflow
                  Utils.selectCurrentOrExisting(sage_vcf, meta, Constants.INPUT.SAGE_VCF_TUMOR),
                                                                ^^^^^^^^^
  ```

- Error: `subworkflows/local/pave_pon_creation/main.nf:30:17`: `Utils` is not defined

  ```nextflow
                  Utils.selectCurrentOrExisting(sage_tbi, meta, Constants.INPUT.SAGE_VCF_TBI_TUMOR),
                  ^^^^^
  ```

- Error: `subworkflows/local/pave_pon_creation/main.nf:30:63`: `Constants` is not defined

  ```nextflow
                  Utils.selectCurrentOrExisting(sage_tbi, meta, Constants.INPUT.SAGE_VCF_TBI_TUMOR),
                                                                ^^^^^^^^^
  ```

- Error: `subworkflows/local/peach_calling/main.nf:5:1`: Groovy `import` declarations are not supported -- use fully-qualified name inline instead

  ```nextflow
  import Constants
  ^^^^^^^^^^^^^^^^
  ```

- Error: `subworkflows/local/peach_calling/main.nf:6:1`: Groovy `import` declarations are not supported -- use fully-qualified name inline instead

  ```nextflow
  import Utils
  ^^^^^^^^^^^^
  ```

- Error: `subworkflows/local/peach_calling/main.nf:33:17`: `Utils` is not defined

  ```nextflow
                  Utils.selectCurrentOrExisting(purple_dir, meta, Constants.INPUT.PURPLE_DIR),
                  ^^^^^
  ```

- Error: `subworkflows/local/peach_calling/main.nf:33:65`: `Constants` is not defined

  ```nextflow
                  Utils.selectCurrentOrExisting(purple_dir, meta, Constants.INPUT.PURPLE_DIR),
                                                                  ^^^^^^^^^
  ```

- Error: `subworkflows/local/peach_calling/main.nf:38:30`: `Utils` is not defined

  ```nextflow
              def has_normal = Utils.hasNormalDna(meta)
                               ^^^^^
  ```

- Error: `subworkflows/local/peach_calling/main.nf:39:32`: `Utils` is not defined

  ```nextflow
              def has_existing = Utils.hasExistingInput(meta, Constants.INPUT.PEACH_DIR)
                                 ^^^^^
  ```

- Error: `subworkflows/local/peach_calling/main.nf:39:61`: `Constants` is not defined

  ```nextflow
              def has_existing = Utils.hasExistingInput(meta, Constants.INPUT.PEACH_DIR)
                                                              ^^^^^^^^^
  ```

- Error: `subworkflows/local/peach_calling/main.nf:54:28`: `Utils` is not defined

  ```nextflow
                  sample_id: Utils.getNormalDnaSampleName(meta),
                             ^^^^^
  ```

- Error: `subworkflows/local/peach_calling/main.nf:57:72`: `Utils` is not defined

  ```nextflow
              def purple_germline_smlv_vcf = file(purple_dir).resolve("${Utils.getTumorDnaSampleName(meta)}.purple.germline.vcf.gz")
                                                                         ^^^^^
  ```

- Error: `subworkflows/local/peach_calling/main.nf:76:13`: `WorkflowOncoanalyser` is not defined

  ```nextflow
              WorkflowOncoanalyser.restoreMeta(PEACH.out.peach_dir, ch_inputs),
              ^^^^^^^^^^^^^^^^^^^^
  ```

- Error: `subworkflows/local/prepare_inputs/main.nf:11:1`: Groovy `import` declarations are not supported -- use fully-qualified name inline instead

  ```nextflow
  import Utils
  ^^^^^^^^^^^^
  ```

- Error: `subworkflows/local/prepare_inputs/main.nf:19:9`: `Utils` is not defined

  ```nextflow
          Utils.parseInput(input_fp_str, workflow.stubRun, log)
          ^^^^^
  ```

- Error: `subworkflows/local/prepare_reference/main.nf:215:28`: Unexpected input: '='

  ```nextflow
              if (run_mode !== Constants.RunMode.PANEL_RESOURCE_CREATION) {
                             ^
  ```

- Error: `subworkflows/local/purple_calling/main.nf:68:27`: Unexpected input: '\*'

  ```nextflow
              return [meta, *inputs]
                            ^
  ```

- Error: `subworkflows/local/read_alignment_dna/main.nf:122:29`: Unexpected input: '\*'

  ```nextflow
                              *:meta_fastq,
                              ^
  ```

- Error: `subworkflows/local/read_alignment_rna/main.nf:65:17`: Unexpected input: '\*'

  ```nextflow
                  *:meta_fastq,
                  ^
  ```

- Error: `subworkflows/local/redux_processing/main.nf:5:1`: Groovy `import` declarations are not supported -- use fully-qualified name inline instead

  ```nextflow
  import Constants
  ^^^^^^^^^^^^^^^^
  ```

- Error: `subworkflows/local/redux_processing/main.nf:6:1`: Groovy `import` declarations are not supported -- use fully-qualified name inline instead

  ```nextflow
  import Utils
  ^^^^^^^^^^^^
  ```

- Error: `subworkflows/local/redux_processing/main.nf:42:17`: `Utils` is not defined

  ```nextflow
                  Utils.hasExistingInput(meta, Constants.INPUT.BAM_DNA_TUMOR) ? [Utils.getInput(meta, Constants.INPUT.BAM_DNA_TUMOR)] : bams,
                  ^^^^^
  ```

- Error: `subworkflows/local/redux_processing/main.nf:42:46`: `Constants` is not defined

  ```nextflow
                  Utils.hasExistingInput(meta, Constants.INPUT.BAM_DNA_TUMOR) ? [Utils.getInput(meta, Constants.INPUT.BAM_DNA_TUMOR)] : bams,
                                               ^^^^^^^^^
  ```

- Error: `subworkflows/local/redux_processing/main.nf:42:80`: `Utils` is not defined

  ```nextflow
                  Utils.hasExistingInput(meta, Constants.INPUT.BAM_DNA_TUMOR) ? [Utils.getInput(meta, Constants.INPUT.BAM_DNA_TUMOR)] : bams,
                                                                                 ^^^^^
  ```

- Error: `subworkflows/local/redux_processing/main.nf:42:101`: `Constants` is not defined

  ```nextflow
                  Utils.hasExistingInput(meta, Constants.INPUT.BAM_DNA_TUMOR) ? [Utils.getInput(meta, Constants.INPUT.BAM_DNA_TUMOR)] : bams,
                                                                                                      ^^^^^^^^^
  ```

- Error: `subworkflows/local/redux_processing/main.nf:43:17`: `Utils` is not defined

  ```nextflow
                  Utils.hasExistingInput(meta, Constants.INPUT.BAI_DNA_TUMOR) ? [Utils.getInput(meta, Constants.INPUT.BAI_DNA_TUMOR)] : bais,
                  ^^^^^
  ```

- Error: `subworkflows/local/redux_processing/main.nf:43:46`: `Constants` is not defined

  ```nextflow
                  Utils.hasExistingInput(meta, Constants.INPUT.BAI_DNA_TUMOR) ? [Utils.getInput(meta, Constants.INPUT.BAI_DNA_TUMOR)] : bais,
                                               ^^^^^^^^^
  ```

- Error: `subworkflows/local/redux_processing/main.nf:43:80`: `Utils` is not defined

  ```nextflow
                  Utils.hasExistingInput(meta, Constants.INPUT.BAI_DNA_TUMOR) ? [Utils.getInput(meta, Constants.INPUT.BAI_DNA_TUMOR)] : bais,
                                                                                 ^^^^^
  ```

- Error: `subworkflows/local/redux_processing/main.nf:43:101`: `Constants` is not defined

  ```nextflow
                  Utils.hasExistingInput(meta, Constants.INPUT.BAI_DNA_TUMOR) ? [Utils.getInput(meta, Constants.INPUT.BAI_DNA_TUMOR)] : bais,
                                                                                                      ^^^^^^^^^
  ```

- Error: `subworkflows/local/redux_processing/main.nf:47:32`: `Utils` is not defined

  ```nextflow
              def has_existing = Utils.hasExistingInput(meta, Constants.INPUT.BAM_REDUX_DNA_TUMOR)
                                 ^^^^^
  ```

- Error: `subworkflows/local/redux_processing/main.nf:47:61`: `Constants` is not defined

  ```nextflow
              def has_existing = Utils.hasExistingInput(meta, Constants.INPUT.BAM_REDUX_DNA_TUMOR)
                                                              ^^^^^^^^^
  ```

- Error: `subworkflows/local/redux_processing/main.nf:57:17`: `Utils` is not defined

  ```nextflow
                  Utils.hasExistingInput(meta, Constants.INPUT.BAM_DNA_NORMAL) ? [Utils.getInput(meta, Constants.INPUT.BAM_DNA_NORMAL)] : bams,
                  ^^^^^
  ```

- Error: `subworkflows/local/redux_processing/main.nf:57:46`: `Constants` is not defined

  ```nextflow
                  Utils.hasExistingInput(meta, Constants.INPUT.BAM_DNA_NORMAL) ? [Utils.getInput(meta, Constants.INPUT.BAM_DNA_NORMAL)] : bams,
                                               ^^^^^^^^^
  ```

- Error: `subworkflows/local/redux_processing/main.nf:57:81`: `Utils` is not defined

  ```nextflow
                  Utils.hasExistingInput(meta, Constants.INPUT.BAM_DNA_NORMAL) ? [Utils.getInput(meta, Constants.INPUT.BAM_DNA_NORMAL)] : bams,
                                                                                  ^^^^^
  ```

- Error: `subworkflows/local/redux_processing/main.nf:57:102`: `Constants` is not defined

  ```nextflow
                  Utils.hasExistingInput(meta, Constants.INPUT.BAM_DNA_NORMAL) ? [Utils.getInput(meta, Constants.INPUT.BAM_DNA_NORMAL)] : bams,
                                                                                                       ^^^^^^^^^
  ```

- Error: `subworkflows/local/redux_processing/main.nf:58:17`: `Utils` is not defined

  ```nextflow
                  Utils.hasExistingInput(meta, Constants.INPUT.BAI_DNA_NORMAL) ? [Utils.getInput(meta, Constants.INPUT.BAI_DNA_NORMAL)] : bais,
                  ^^^^^
  ```

- Error: `subworkflows/local/redux_processing/main.nf:58:46`: `Constants` is not defined

  ```nextflow
                  Utils.hasExistingInput(meta, Constants.INPUT.BAI_DNA_NORMAL) ? [Utils.getInput(meta, Constants.INPUT.BAI_DNA_NORMAL)] : bais,
                                               ^^^^^^^^^
  ```

- Error: `subworkflows/local/redux_processing/main.nf:58:81`: `Utils` is not defined

  ```nextflow
                  Utils.hasExistingInput(meta, Constants.INPUT.BAI_DNA_NORMAL) ? [Utils.getInput(meta, Constants.INPUT.BAI_DNA_NORMAL)] : bais,
                                                                                  ^^^^^
  ```

- Error: `subworkflows/local/redux_processing/main.nf:58:102`: `Constants` is not defined

  ```nextflow
                  Utils.hasExistingInput(meta, Constants.INPUT.BAI_DNA_NORMAL) ? [Utils.getInput(meta, Constants.INPUT.BAI_DNA_NORMAL)] : bais,
                                                                                                       ^^^^^^^^^
  ```

- Error: `subworkflows/local/redux_processing/main.nf:62:32`: `Utils` is not defined

  ```nextflow
              def has_existing = Utils.hasExistingInput(meta, Constants.INPUT.BAM_REDUX_DNA_NORMAL)
                                 ^^^^^
  ```

- Error: `subworkflows/local/redux_processing/main.nf:62:61`: `Constants` is not defined

  ```nextflow
              def has_existing = Utils.hasExistingInput(meta, Constants.INPUT.BAM_REDUX_DNA_NORMAL)
                                                              ^^^^^^^^^
  ```

- Error: `subworkflows/local/redux_processing/main.nf:72:17`: `Utils` is not defined

  ```nextflow
                  Utils.hasExistingInput(meta, Constants.INPUT.BAM_DNA_DONOR) ? [Utils.getInput(meta, Constants.INPUT.BAM_DNA_DONOR)] : bams,
                  ^^^^^
  ```

- Error: `subworkflows/local/redux_processing/main.nf:72:46`: `Constants` is not defined

  ```nextflow
                  Utils.hasExistingInput(meta, Constants.INPUT.BAM_DNA_DONOR) ? [Utils.getInput(meta, Constants.INPUT.BAM_DNA_DONOR)] : bams,
                                               ^^^^^^^^^
  ```

- Error: `subworkflows/local/redux_processing/main.nf:72:80`: `Utils` is not defined

  ```nextflow
                  Utils.hasExistingInput(meta, Constants.INPUT.BAM_DNA_DONOR) ? [Utils.getInput(meta, Constants.INPUT.BAM_DNA_DONOR)] : bams,
                                                                                 ^^^^^
  ```

- Error: `subworkflows/local/redux_processing/main.nf:72:101`: `Constants` is not defined

  ```nextflow
                  Utils.hasExistingInput(meta, Constants.INPUT.BAM_DNA_DONOR) ? [Utils.getInput(meta, Constants.INPUT.BAM_DNA_DONOR)] : bams,
                                                                                                      ^^^^^^^^^
  ```

- Error: `subworkflows/local/redux_processing/main.nf:73:17`: `Utils` is not defined

  ```nextflow
                  Utils.hasExistingInput(meta, Constants.INPUT.BAI_DNA_DONOR) ? [Utils.getInput(meta, Constants.INPUT.BAI_DNA_DONOR)] : bais,
                  ^^^^^
  ```

- Error: `subworkflows/local/redux_processing/main.nf:73:46`: `Constants` is not defined

  ```nextflow
                  Utils.hasExistingInput(meta, Constants.INPUT.BAI_DNA_DONOR) ? [Utils.getInput(meta, Constants.INPUT.BAI_DNA_DONOR)] : bais,
                                               ^^^^^^^^^
  ```

- Error: `subworkflows/local/redux_processing/main.nf:73:80`: `Utils` is not defined

  ```nextflow
                  Utils.hasExistingInput(meta, Constants.INPUT.BAI_DNA_DONOR) ? [Utils.getInput(meta, Constants.INPUT.BAI_DNA_DONOR)] : bais,
                                                                                 ^^^^^
  ```

- Error: `subworkflows/local/redux_processing/main.nf:73:101`: `Constants` is not defined

  ```nextflow
                  Utils.hasExistingInput(meta, Constants.INPUT.BAI_DNA_DONOR) ? [Utils.getInput(meta, Constants.INPUT.BAI_DNA_DONOR)] : bais,
                                                                                                      ^^^^^^^^^
  ```

- Error: `subworkflows/local/redux_processing/main.nf:77:32`: `Utils` is not defined

  ```nextflow
              def has_existing = Utils.hasExistingInput(meta, Constants.INPUT.BAM_REDUX_DNA_DONOR)
                                 ^^^^^
  ```

- Error: `subworkflows/local/redux_processing/main.nf:77:61`: `Constants` is not defined

  ```nextflow
              def has_existing = Utils.hasExistingInput(meta, Constants.INPUT.BAM_REDUX_DNA_DONOR)
                                                              ^^^^^^^^^
  ```

- Error: `subworkflows/local/redux_processing/main.nf:87:78`: `Utils` is not defined

  ```nextflow
              ch_inputs_tumor_sorted.runnable.map { meta, bams, bais -> [meta, Utils.getTumorDnaSample(meta), 'tumor', bams, bais] },
                                                                               ^^^^^
  ```

- Error: `subworkflows/local/redux_processing/main.nf:88:79`: `Utils` is not defined

  ```nextflow
              ch_inputs_normal_sorted.runnable.map { meta, bams, bais -> [meta, Utils.getNormalDnaSample(meta), 'normal', bams, bais] },
                                                                                ^^^^^
  ```

- Error: `subworkflows/local/redux_processing/main.nf:89:78`: `Utils` is not defined

  ```nextflow
              ch_inputs_donor_sorted.runnable.map { meta, bams, bais -> [meta, Utils.getDonorDnaSample(meta), 'donor', bams, bais] },
                                                                               ^^^^^
  ```

- Error: `subworkflows/local/redux_processing/main.nf:122:20`: `WorkflowOncoanalyser` is not defined

  ```nextflow
      ch_redux_out = WorkflowOncoanalyser.groupByMeta(
                     ^^^^^^^^^^^^^^^^^^^^
  ```

- Error: `subworkflows/local/redux_processing/main.nf:144:13`: `WorkflowOncoanalyser` is not defined

  ```nextflow
              WorkflowOncoanalyser.restoreMeta(ch_redux_out_sorted.tumor, ch_inputs),
              ^^^^^^^^^^^^^^^^^^^^
  ```

- Error: `subworkflows/local/redux_processing/main.nf:154:13`: `WorkflowOncoanalyser` is not defined

  ```nextflow
              WorkflowOncoanalyser.restoreMeta(ch_redux_out_sorted.normal, ch_inputs),
              ^^^^^^^^^^^^^^^^^^^^
  ```

- Error: `subworkflows/local/redux_processing/main.nf:164:13`: `WorkflowOncoanalyser` is not defined

  ```nextflow
              WorkflowOncoanalyser.restoreMeta(ch_redux_out_sorted.donor, ch_inputs),
              ^^^^^^^^^^^^^^^^^^^^
  ```

- Error: `subworkflows/local/sage_append/main.nf:36:43`: Unexpected input: '='

  ```nextflow
      def purity_estimate_mode = run_mode === Constants.RunMode.PURITY_ESTIMATE
                                            ^
  ```

- Error: `subworkflows/local/sage_calling/main.nf:5:1`: Groovy `import` declarations are not supported -- use fully-qualified name inline instead

  ```nextflow
  import Constants
  ^^^^^^^^^^^^^^^^
  ```

- Error: `subworkflows/local/sage_calling/main.nf:6:1`: Groovy `import` declarations are not supported -- use fully-qualified name inline instead

  ```nextflow
  import Utils
  ^^^^^^^^^^^^
  ```

- Error: `subworkflows/local/sage_calling/main.nf:8:1`: Groovy `import` declarations are not supported -- use fully-qualified name inline instead

  ```nextflow
  import java.nio.channels.Channel
  ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  ```

- Error: `subworkflows/local/sage_calling/main.nf:48:24`: `WorkflowOncoanalyser` is not defined

  ```nextflow
      ch_inputs_sorted = WorkflowOncoanalyser.groupByMeta(
                         ^^^^^^^^^^^^^^^^^^^^
  ```

- Error: `subworkflows/local/sage_calling/main.nf:66:37`: `Utils` is not defined

  ```nextflow
                  tumor_jitter_tsv ?: Utils.getInput(meta, Constants.INPUT.REDUX_JITTER_TSV_TUMOR),
                                      ^^^^^
  ```

- Error: `subworkflows/local/sage_calling/main.nf:66:58`: `Constants` is not defined

  ```nextflow
                  tumor_jitter_tsv ?: Utils.getInput(meta, Constants.INPUT.REDUX_JITTER_TSV_TUMOR),
                                                           ^^^^^^^^^
  ```

- Error: `subworkflows/local/sage_calling/main.nf:67:33`: `Utils` is not defined

  ```nextflow
                  tumor_ms_tsv ?: Utils.getInput(meta, Constants.INPUT.REDUX_MS_TSV_TUMOR),
                                  ^^^^^
  ```

- Error: `subworkflows/local/sage_calling/main.nf:67:54`: `Constants` is not defined

  ```nextflow
                  tumor_ms_tsv ?: Utils.getInput(meta, Constants.INPUT.REDUX_MS_TSV_TUMOR),
                                                       ^^^^^^^^^
  ```

- Error: `subworkflows/local/sage_calling/main.nf:69:38`: `Utils` is not defined

  ```nextflow
                  normal_jitter_tsv ?: Utils.getInput(meta, Constants.INPUT.REDUX_JITTER_TSV_NORMAL),
                                       ^^^^^
  ```

- Error: `subworkflows/local/sage_calling/main.nf:69:59`: `Constants` is not defined

  ```nextflow
                  normal_jitter_tsv ?: Utils.getInput(meta, Constants.INPUT.REDUX_JITTER_TSV_NORMAL),
                                                            ^^^^^^^^^
  ```

- Error: `subworkflows/local/sage_calling/main.nf:70:34`: `Utils` is not defined

  ```nextflow
                  normal_ms_tsv ?: Utils.getInput(meta, Constants.INPUT.REDUX_MS_TSV_NORMAL),
                                   ^^^^^
  ```

- Error: `subworkflows/local/sage_calling/main.nf:70:55`: `Constants` is not defined

  ```nextflow
                  normal_ms_tsv ?: Utils.getInput(meta, Constants.INPUT.REDUX_MS_TSV_NORMAL),
                                                        ^^^^^^^^^
  ```

- Error: `subworkflows/local/sage_calling/main.nf:72:37`: `Utils` is not defined

  ```nextflow
                  donor_jitter_tsv ?: Utils.getInput(meta, Constants.INPUT.REDUX_JITTER_TSV_DONOR),
                                      ^^^^^
  ```

- Error: `subworkflows/local/sage_calling/main.nf:72:58`: `Constants` is not defined

  ```nextflow
                  donor_jitter_tsv ?: Utils.getInput(meta, Constants.INPUT.REDUX_JITTER_TSV_DONOR),
                                                           ^^^^^^^^^
  ```

- Error: `subworkflows/local/sage_calling/main.nf:73:33`: `Utils` is not defined

  ```nextflow
                  donor_ms_tsv ?: Utils.getInput(meta, Constants.INPUT.REDUX_MS_TSV_DONOR),
                                  ^^^^^
  ```

- Error: `subworkflows/local/sage_calling/main.nf:73:54`: `Constants` is not defined

  ```nextflow
                  donor_ms_tsv ?: Utils.getInput(meta, Constants.INPUT.REDUX_MS_TSV_DONOR),
                                                       ^^^^^^^^^
  ```

- Error: `subworkflows/local/sage_calling/main.nf:81:17`: `Utils` is not defined

  ```nextflow
                  Utils.selectCurrentOrExisting(tumor_bam, meta, Constants.INPUT.BAM_REDUX_DNA_TUMOR),
                  ^^^^^
  ```

- Error: `subworkflows/local/sage_calling/main.nf:81:64`: `Constants` is not defined

  ```nextflow
                  Utils.selectCurrentOrExisting(tumor_bam, meta, Constants.INPUT.BAM_REDUX_DNA_TUMOR),
                                                                 ^^^^^^^^^
  ```

- Error: `subworkflows/local/sage_calling/main.nf:82:30`: `Utils` is not defined

  ```nextflow
                  tumor_bai ?: Utils.getInput(meta, Constants.INPUT.BAI_DNA_TUMOR),
                               ^^^^^
  ```

- Error: `subworkflows/local/sage_calling/main.nf:82:51`: `Constants` is not defined

  ```nextflow
                  tumor_bai ?: Utils.getInput(meta, Constants.INPUT.BAI_DNA_TUMOR),
                                                    ^^^^^^^^^
  ```

- Error: `subworkflows/local/sage_calling/main.nf:84:17`: `Utils` is not defined

  ```nextflow
                  Utils.selectCurrentOrExisting(normal_bam, meta, Constants.INPUT.BAM_REDUX_DNA_NORMAL),
                  ^^^^^
  ```

- Error: `subworkflows/local/sage_calling/main.nf:84:65`: `Constants` is not defined

  ```nextflow
                  Utils.selectCurrentOrExisting(normal_bam, meta, Constants.INPUT.BAM_REDUX_DNA_NORMAL),
                                                                  ^^^^^^^^^
  ```

- Error: `subworkflows/local/sage_calling/main.nf:85:31`: `Utils` is not defined

  ```nextflow
                  normal_bai ?: Utils.getInput(meta, Constants.INPUT.BAI_DNA_NORMAL),
                                ^^^^^
  ```

- Error: `subworkflows/local/sage_calling/main.nf:85:52`: `Constants` is not defined

  ```nextflow
                  normal_bai ?: Utils.getInput(meta, Constants.INPUT.BAI_DNA_NORMAL),
                                                     ^^^^^^^^^
  ```

- Error: `subworkflows/local/sage_calling/main.nf:87:17`: `Utils` is not defined

  ```nextflow
                  Utils.selectCurrentOrExisting(donor_bam, meta, Constants.INPUT.BAM_REDUX_DNA_DONOR),
                  ^^^^^
  ```

- Error: `subworkflows/local/sage_calling/main.nf:87:64`: `Constants` is not defined

  ```nextflow
                  Utils.selectCurrentOrExisting(donor_bam, meta, Constants.INPUT.BAM_REDUX_DNA_DONOR),
                                                                 ^^^^^^^^^
  ```

- Error: `subworkflows/local/sage_calling/main.nf:88:30`: `Utils` is not defined

  ```nextflow
                  donor_bai ?: Utils.getInput(meta, Constants.INPUT.BAI_DNA_DONOR),
                               ^^^^^
  ```

- Error: `subworkflows/local/sage_calling/main.nf:88:51`: `Constants` is not defined

  ```nextflow
                  donor_bai ?: Utils.getInput(meta, Constants.INPUT.BAI_DNA_DONOR),
                                                    ^^^^^^^^^
  ```

- Error: `subworkflows/local/sage_calling/main.nf:108:32`: `Utils` is not defined

  ```nextflow
              def has_existing = Utils.hasExistingInput(meta, Constants.INPUT.SAGE_VCF_NORMAL)
                                 ^^^^^
  ```

- Error: `subworkflows/local/sage_calling/main.nf:108:61`: `Constants` is not defined

  ```nextflow
              def has_existing = Utils.hasExistingInput(meta, Constants.INPUT.SAGE_VCF_NORMAL)
                                                              ^^^^^^^^^
  ```

- Error: `subworkflows/local/sage_calling/main.nf:123:27`: `Utils` is not defined

  ```nextflow
                  tumor_id: Utils.getTumorDnaSampleName(meta),
                            ^^^^^
  ```

- Error: `subworkflows/local/sage_calling/main.nf:124:28`: `Utils` is not defined

  ```nextflow
                  normal_id: Utils.getNormalDnaSampleName(meta),
                             ^^^^^
  ```

- Error: `subworkflows/local/sage_calling/main.nf:155:32`: `Utils` is not defined

  ```nextflow
              def has_existing = Utils.hasExistingInput(meta, Constants.INPUT.SAGE_VCF_TUMOR)
                                 ^^^^^
  ```

- Error: `subworkflows/local/sage_calling/main.nf:155:61`: `Constants` is not defined

  ```nextflow
              def has_existing = Utils.hasExistingInput(meta, Constants.INPUT.SAGE_VCF_TUMOR)
                                                              ^^^^^^^^^
  ```

- Error: `subworkflows/local/sage_calling/main.nf:171:27`: `Utils` is not defined

  ```nextflow
                  tumor_id: Utils.getTumorDnaSampleName(meta),
                            ^^^^^
  ```

- Error: `subworkflows/local/sage_calling/main.nf:172:27`: `Utils` is not defined

  ```nextflow
                  donor_id: Utils.getDonorDnaSampleName(meta),
                            ^^^^^
  ```

- Error: `subworkflows/local/sage_calling/main.nf:176:39`: `Utils` is not defined

  ```nextflow
                  meta_sage.normal_id = Utils.getNormalDnaSampleName(meta)
                                        ^^^^^
  ```

- Error: `subworkflows/local/sage_calling/main.nf:180:38`: `Utils` is not defined

  ```nextflow
                  meta_sage.donor_id = Utils.getDonorDnaSampleName(meta)
                                       ^^^^^
  ```

- Error: `subworkflows/local/sage_calling/main.nf:208:13`: `WorkflowOncoanalyser` is not defined

  ```nextflow
              WorkflowOncoanalyser.restoreMeta(SAGE_SOMATIC.out.vcf, ch_inputs),
              ^^^^^^^^^^^^^^^^^^^^
  ```

- Error: `subworkflows/local/sage_calling/main.nf:216:13`: `WorkflowOncoanalyser` is not defined

  ```nextflow
              WorkflowOncoanalyser.restoreMeta(SAGE_GERMLINE.out.vcf, ch_inputs),
              ^^^^^^^^^^^^^^^^^^^^
  ```

- Error: `subworkflows/local/sage_calling/main.nf:224:13`: `WorkflowOncoanalyser` is not defined

  ```nextflow
              WorkflowOncoanalyser.restoreMeta(SAGE_SOMATIC.out.sage_dir, ch_inputs),
              ^^^^^^^^^^^^^^^^^^^^
  ```

- Error: `subworkflows/local/sage_calling/main.nf:232:13`: `WorkflowOncoanalyser` is not defined

  ```nextflow
              WorkflowOncoanalyser.restoreMeta(SAGE_GERMLINE.out.sage_dir, ch_inputs),
              ^^^^^^^^^^^^^^^^^^^^
  ```

- Error: `subworkflows/local/sigs_fitting/main.nf:5:1`: Groovy `import` declarations are not supported -- use fully-qualified name inline instead

  ```nextflow
  import Constants
  ^^^^^^^^^^^^^^^^
  ```

- Error: `subworkflows/local/sigs_fitting/main.nf:6:1`: Groovy `import` declarations are not supported -- use fully-qualified name inline instead

  ```nextflow
  import Utils
  ^^^^^^^^^^^^
  ```

- Error: `subworkflows/local/sigs_fitting/main.nf:28:27`: `Utils` is not defined

  ```nextflow
              return [meta, Utils.selectCurrentOrExisting(purple_dir, meta, Constants.INPUT.PURPLE_DIR)]
                            ^^^^^
  ```

- Error: `subworkflows/local/sigs_fitting/main.nf:28:75`: `Constants` is not defined

  ```nextflow
              return [meta, Utils.selectCurrentOrExisting(purple_dir, meta, Constants.INPUT.PURPLE_DIR)]
                                                                            ^^^^^^^^^
  ```

- Error: `subworkflows/local/sigs_fitting/main.nf:37:27`: `Utils` is not defined

  ```nextflow
              def has_dna = Utils.hasTumorDna(meta)
                            ^^^^^
  ```

- Error: `subworkflows/local/sigs_fitting/main.nf:42:28`: `Utils` is not defined

  ```nextflow
                  tumor_id = Utils.getTumorDnaSampleName(meta)
                             ^^^^^
  ```

- Error: `subworkflows/local/sigs_fitting/main.nf:46:32`: `Utils` is not defined

  ```nextflow
              def has_existing = Utils.hasExistingInput(meta, Constants.INPUT.SIGS_DIR)
                                 ^^^^^
  ```

- Error: `subworkflows/local/sigs_fitting/main.nf:46:61`: `Constants` is not defined

  ```nextflow
              def has_existing = Utils.hasExistingInput(meta, Constants.INPUT.SIGS_DIR)
                                                              ^^^^^^^^^
  ```

- Error: `subworkflows/local/sigs_fitting/main.nf:58:28`: `Utils` is not defined

  ```nextflow
              def tumor_id = Utils.getTumorDnaSampleName(meta)
                             ^^^^^
  ```

- Error: `subworkflows/local/sigs_fitting/main.nf:83:13`: `WorkflowOncoanalyser` is not defined

  ```nextflow
              WorkflowOncoanalyser.restoreMeta(SIGS.out.sigs_dir, ch_inputs),
              ^^^^^^^^^^^^^^^^^^^^
  ```

- Error: `subworkflows/local/teal_characterisation/main.nf:86:40`: Unexpected input: '\*'

  ```nextflow
          .map { meta, bam_bai -> [meta, *bam_bai] }
                                         ^
  ```

- Error: `subworkflows/local/virusbreakend_calling/main.nf:103:27`: Unexpected input: '\*'

  ```nextflow
              return [meta, *inputs]
                            ^
  ```

- Error: `subworkflows/local/wisp_analysis/main.nf:46:40`: Unexpected input: '='

  ```nextflow
              if (purity_estimate_mode === Constants.RunMode.WGTS) {
                                         ^
  ```

- Error: `workflows/panel_resource_creation.nf:136:54`: Unexpected input: '='

  ```nextflow
      isofox_read_length = params.isofox_read_length !== null ? params.isofox_read_length : Constants.DEFAULT_ISOFOX_READ_LENGTH_TARGETED
                                                       ^
  ```

- Error: `workflows/prepare_reference.nf:1:1`: Groovy `import` declarations are not supported -- use fully-qualified name inline instead

  ```nextflow
  import Constants
  ^^^^^^^^^^^^^^^^
  ```

- Error: `workflows/prepare_reference.nf:2:1`: Groovy `import` declarations are not supported -- use fully-qualified name inline instead

  ```nextflow
  import Processes
  ^^^^^^^^^^^^^^^^
  ```

- Error: `workflows/prepare_reference.nf:3:1`: Groovy `import` declarations are not supported -- use fully-qualified name inline instead

  ```nextflow
  import Utils
  ^^^^^^^^^^^^
  ```

- Error: `workflows/prepare_reference.nf:11:1`: Module could not be parsed: '/home/runner/work/strict-syntax-health/strict-syntax-health/pipelines/oncoanalyser/subworkflows/local/prepare_reference/main.nf'

  ```nextflow
  include { PREPARE_REFERENCE as STAGE_REFERENCE } from '../subworkflows/local/prepare_reference'
  ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  ```

- Error: `workflows/prepare_reference.nf:27:19`: `WorkflowMain` is not defined

  ```nextflow
      prep_config = WorkflowMain.getPrepConfigFromCli(params, log)
                    ^^^^^^^^^^^^
  ```

- Error: `workflows/prepare_reference.nf:28:5`: `STAGE_REFERENCE` is not defined

  ```nextflow
      STAGE_REFERENCE(
      ^^^^^^^^^^^^^^^
  ```

- Error: `workflows/prepare_reference.nf:33:35`: `STAGE_REFERENCE` is not defined

  ```nextflow
      ch_versions = ch_versions.mix(STAGE_REFERENCE.out.versions)
                                    ^^^^^^^^^^^^^^^
  ```

- Error: `workflows/purity_estimate.nf:147:63`: Unexpected input: '='

  ```nextflow
      if (run_config.stages.amber && purity_estimate_run_mode === Constants.RunMode.WGTS) {
                                                                ^
  ```

- Error: `workflows/targeted.nf:182:54`: Unexpected input: '='

  ```nextflow
      isofox_read_length = params.isofox_read_length !== null ? params.isofox_read_length : Constants.DEFAULT_ISOFOX_READ_LENGTH_TARGETED
                                                       ^
  ```

- Error: `workflows/wgts.nf:79:44`: Unexpected input: '='

  ```nextflow
      gridss_config = params.gridss_config !== null ? file(params.gridss_config) : hmf_data.gridss_config
                                             ^
  ```

## :warning: Warnings

- Warning: `modules/local/wisp/main.nf:34:9`: Variable was declared but not used

  ```nextflow
      def purity_estimate_mode = Utils.getEnumFromString(params.purity_estimate_mode, Constants.RunMode)
          ^^^^^^^^^^^^^^^^^^^^
  ```

- Warning: `modules/nf-core/gatk4/markduplicates/main.nf:30:43`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
      def input_list = bam.collect{"--INPUT $it"}.join(' ')
                                            ^^
  ```

- Warning: `modules/nf-core/star/genomegenerate/main.nf:23:9`: Variable was declared but not used

  ```nextflow
      def args_list   = args.tokenize()
          ^^^^^^^^^
  ```

- Warning: `subworkflows/local/amber_profiling/main.nf:27:19`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_versions = Channel.empty()
                    ^^^^^^^
  ```

- Warning: `subworkflows/local/amber_profiling/main.nf:50:36`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          .branch { meta, tumor_bam, tumor_bai, normal_bam, normal_bai, donor_bam, donor_bai ->
                                     ^^^^^^^^^
  ```

- Warning: `subworkflows/local/amber_profiling/main.nf:50:47`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          .branch { meta, tumor_bam, tumor_bai, normal_bam, normal_bai, donor_bam, donor_bai ->
                                                ^^^^^^^^^^
  ```

- Warning: `subworkflows/local/amber_profiling/main.nf:50:59`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          .branch { meta, tumor_bam, tumor_bai, normal_bam, normal_bai, donor_bam, donor_bai ->
                                                            ^^^^^^^^^^
  ```

- Warning: `subworkflows/local/amber_profiling/main.nf:50:71`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          .branch { meta, tumor_bam, tumor_bai, normal_bam, normal_bai, donor_bam, donor_bai ->
                                                                        ^^^^^^^^^
  ```

- Warning: `subworkflows/local/amber_profiling/main.nf:50:82`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          .branch { meta, tumor_bam, tumor_bai, normal_bam, normal_bai, donor_bam, donor_bai ->
                                                                                   ^^^^^^^^^
  ```

- Warning: `subworkflows/local/amber_profiling/main.nf:99:18`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_outputs = Channel.empty()
                   ^^^^^^^
  ```

- Warning: `subworkflows/local/bamtools_metrics/main.nf:27:19`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_versions = Channel.empty()
                    ^^^^^^^
  ```

- Warning: `subworkflows/local/bamtools_metrics/main.nf:40:30`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          .branch { meta, bam, bai ->
                               ^^^
  ```

- Warning: `subworkflows/local/bamtools_metrics/main.nf:57:30`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          .branch { meta, bam, bai ->
                               ^^^
  ```

- Warning: `subworkflows/local/bamtools_metrics/main.nf:66:26`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_bamtools_inputs = Channel.empty()
                           ^^^^^^^
  ```

- Warning: `subworkflows/local/bamtools_metrics/main.nf:97:34`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          .branch { meta_bamtools, metrics_dir ->
                                   ^^^^^^^^^^^
  ```

- Warning: `subworkflows/local/bamtools_metrics/main.nf:106:30`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_somatic_metrics_dir = Channel.empty()
                               ^^^^^^^
  ```

- Warning: `subworkflows/local/bamtools_metrics/main.nf:112:31`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_germline_metrics_dir = Channel.empty()
                                ^^^^^^^
  ```

- Warning: `subworkflows/local/chord_prediction/main.nf:22:19`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_versions = Channel.empty()
                    ^^^^^^^
  ```

- Warning: `subworkflows/local/chord_prediction/main.nf:87:18`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_outputs = Channel.empty()
                   ^^^^^^^
  ```

- Warning: `subworkflows/local/cider_calling/main.nf:13:5`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
      ch_inputs        // channel: [mandatory] [ meta ]
      ^^^^^^^^^
  ```

- Warning: `subworkflows/local/cider_calling/main.nf:26:19`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_versions = Channel.empty()
                    ^^^^^^^
  ```

- Warning: `subworkflows/local/cider_calling/main.nf:39:30`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          .branch { meta, bam, bai ->
                               ^^^
  ```

- Warning: `subworkflows/local/cider_calling/main.nf:55:30`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          .branch { meta, bam, bai ->
                               ^^^
  ```

- Warning: `subworkflows/local/cider_calling/main.nf:63:23`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_cider_inputs = Channel.empty()
                        ^^^^^^^
  ```

- Warning: `subworkflows/local/cobalt_normalisation/main.nf:24:19`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_versions = Channel.empty()
                    ^^^^^^^
  ```

- Warning: `subworkflows/local/isofox_normalisation/main.nf:23:19`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_versions = Channel.empty()
                    ^^^^^^^
  ```

- Warning: `subworkflows/local/isofox_quantification/main.nf:34:19`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_versions = Channel.empty()
                    ^^^^^^^
  ```

- Warning: `subworkflows/local/isofox_quantification/main.nf:47:36`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          .branch { meta, tumor_bam, tumor_bai ->
                                     ^^^^^^^^^
  ```

- Warning: `subworkflows/local/isofox_quantification/main.nf:88:18`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_outputs = Channel.empty()
                   ^^^^^^^
  ```

- Warning: `subworkflows/local/lilac_calling/main.nf:29:19`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_versions = Channel.empty()
                    ^^^^^^^
  ```

- Warning: `subworkflows/local/lilac_calling/main.nf:47:36`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          .branch { meta, tumor_bam, tumor_bai, normal_bam, normal_bai ->
                                     ^^^^^^^^^
  ```

- Warning: `subworkflows/local/lilac_calling/main.nf:47:59`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          .branch { meta, tumor_bam, tumor_bai, normal_bam, normal_bai ->
                                                            ^^^^^^^^^^
  ```

- Warning: `subworkflows/local/lilac_calling/main.nf:107:18`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_outputs = Channel.empty()
                   ^^^^^^^
  ```

- Warning: `subworkflows/local/linx_annotation/main.nf:26:19`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_versions = Channel.empty()
                    ^^^^^^^
  ```

- Warning: `subworkflows/local/linx_annotation/main.nf:99:25`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          .branch { meta, purple_dir ->
                          ^^^^^^^^^^
  ```

- Warning: `subworkflows/local/linx_annotation/main.nf:137:22`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_somatic_out = Channel.empty()
                       ^^^^^^^
  ```

- Warning: `subworkflows/local/linx_annotation/main.nf:144:23`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_germline_out = Channel.empty()
                        ^^^^^^^
  ```

- Warning: `subworkflows/local/linx_plotting/main.nf:29:19`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_versions = Channel.empty()
                    ^^^^^^^
  ```

- Warning: `subworkflows/local/linx_plotting/main.nf:51:41`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          .branch { meta, annotation_dir, amber_dir, cobalt_dir, purple_dir ->
                                          ^^^^^^^^^
  ```

- Warning: `subworkflows/local/linx_plotting/main.nf:51:52`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          .branch { meta, annotation_dir, amber_dir, cobalt_dir, purple_dir ->
                                                     ^^^^^^^^^^
  ```

- Warning: `subworkflows/local/linx_plotting/main.nf:51:64`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          .branch { meta, annotation_dir, amber_dir, cobalt_dir, purple_dir ->
                                                                 ^^^^^^^^^^
  ```

- Warning: `subworkflows/local/linx_plotting/main.nf:95:38`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          .map { meta, annotation_dir, amber_dir, cobalt_dir, purple_dir, visualiser_dir ->
                                       ^^^^^^^^^
  ```

- Warning: `subworkflows/local/linx_plotting/main.nf:95:49`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          .map { meta, annotation_dir, amber_dir, cobalt_dir, purple_dir, visualiser_dir ->
                                                  ^^^^^^^^^^
  ```

- Warning: `subworkflows/local/linx_plotting/main.nf:95:61`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          .map { meta, annotation_dir, amber_dir, cobalt_dir, purple_dir, visualiser_dir ->
                                                              ^^^^^^^^^^
  ```

- Warning: `subworkflows/local/linx_plotting/main.nf:115:29`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_visualiser_dir_out = Channel.empty()
                              ^^^^^^^
  ```

- Warning: `subworkflows/local/pave_annotation/main.nf:34:19`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_versions = Channel.empty()
                    ^^^^^^^
  ```

- Warning: `subworkflows/local/pave_annotation/main.nf:50:35`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          .branch { meta, sage_vcf, sage_tbi ->
                                    ^^^^^^^^
  ```

- Warning: `subworkflows/local/pave_annotation/main.nf:103:35`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          .branch { meta, sage_vcf, sage_tbi ->
                                    ^^^^^^^^
  ```

- Warning: `subworkflows/local/pave_annotation/main.nf:145:22`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_somatic_out = Channel.empty()
                       ^^^^^^^
  ```

- Warning: `subworkflows/local/pave_annotation/main.nf:151:23`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_germline_out = Channel.empty()
                        ^^^^^^^
  ```

- Warning: `subworkflows/local/pave_pon_creation/main.nf:22:19`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_versions = Channel.empty()
                    ^^^^^^^
  ```

- Warning: `subworkflows/local/peach_calling/main.nf:24:19`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_versions = Channel.empty()
                    ^^^^^^^
  ```

- Warning: `subworkflows/local/peach_calling/main.nf:74:18`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_outputs = Channel.empty()
                   ^^^^^^^
  ```

- Warning: `subworkflows/local/prepare_inputs/main.nf:18:17`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_inputs = Channel.fromList(
                  ^^^^^^^
  ```

- Warning: `subworkflows/local/redux_processing/main.nf:33:19`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_versions = Channel.empty()
                    ^^^^^^^
  ```

- Warning: `subworkflows/local/redux_processing/main.nf:46:31`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          .branch { meta, bams, bais ->
                                ^^^^
  ```

- Warning: `subworkflows/local/redux_processing/main.nf:61:31`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          .branch { meta, bams, bais ->
                                ^^^^
  ```

- Warning: `subworkflows/local/redux_processing/main.nf:76:31`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          .branch { meta, bams, bais ->
                                ^^^^
  ```

- Warning: `subworkflows/local/redux_processing/main.nf:85:23`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_redux_inputs = Channel.empty()
                        ^^^^^^^
  ```

- Warning: `subworkflows/local/redux_processing/main.nf:132:31`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          .branch { meta_redux, bam, bai, dup_freq_tsv, jitter_tsv, ms_tsv ->
                                ^^^
  ```

- Warning: `subworkflows/local/redux_processing/main.nf:132:36`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          .branch { meta_redux, bam, bai, dup_freq_tsv, jitter_tsv, ms_tsv ->
                                     ^^^
  ```

- Warning: `subworkflows/local/redux_processing/main.nf:132:41`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          .branch { meta_redux, bam, bai, dup_freq_tsv, jitter_tsv, ms_tsv ->
                                          ^^^^^^^^^^^^
  ```

- Warning: `subworkflows/local/redux_processing/main.nf:132:55`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          .branch { meta_redux, bam, bai, dup_freq_tsv, jitter_tsv, ms_tsv ->
                                                        ^^^^^^^^^^
  ```

- Warning: `subworkflows/local/redux_processing/main.nf:132:67`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          .branch { meta_redux, bam, bai, dup_freq_tsv, jitter_tsv, ms_tsv ->
                                                                    ^^^^^^
  ```

- Warning: `subworkflows/local/redux_processing/main.nf:142:26`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_redux_tumor_out = Channel.empty()
                           ^^^^^^^
  ```

- Warning: `subworkflows/local/redux_processing/main.nf:152:27`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_redux_normal_out = Channel.empty()
                            ^^^^^^^
  ```

- Warning: `subworkflows/local/redux_processing/main.nf:162:26`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_redux_donor_out = Channel.empty()
                           ^^^^^^^
  ```

- Warning: `subworkflows/local/sage_calling/main.nf:33:5`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
      segment_mappability          // channel: [mandatory] /path/to/segment_mappability
      ^^^^^^^^^^^^^^^^^^^
  ```

- Warning: `subworkflows/local/sage_calling/main.nf:43:19`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_versions = Channel.empty()
                    ^^^^^^^
  ```

- Warning: `subworkflows/local/sage_calling/main.nf:61:13`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
              tumor_dup_freq_tsv,  tumor_jitter_tsv,  tumor_ms_tsv,
              ^^^^^^^^^^^^^^^^^^
  ```

- Warning: `subworkflows/local/sage_calling/main.nf:62:13`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
              normal_dup_freq_tsv, normal_jitter_tsv, normal_ms_tsv,
              ^^^^^^^^^^^^^^^^^^^
  ```

- Warning: `subworkflows/local/sage_calling/main.nf:63:13`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
              donor_dup_freq_tsv,  donor_jitter_tsv,  donor_ms_tsv ->
              ^^^^^^^^^^^^^^^^^^
  ```

- Warning: `subworkflows/local/sage_calling/main.nf:76:54`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
              redux_tsv_list = redux_tsv_list.findAll{ it != [] }
                                                       ^^
  ```

- Warning: `subworkflows/local/sage_calling/main.nf:93:36`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          .branch { meta, tumor_bam, tumor_bai, normal_bam, normal_bai, donor_bam, donor_bai, redux_tsvs ->
                                     ^^^^^^^^^
  ```

- Warning: `subworkflows/local/sage_calling/main.nf:93:47`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          .branch { meta, tumor_bam, tumor_bai, normal_bam, normal_bai, donor_bam, donor_bai, redux_tsvs ->
                                                ^^^^^^^^^^
  ```

- Warning: `subworkflows/local/sage_calling/main.nf:93:59`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          .branch { meta, tumor_bam, tumor_bai, normal_bam, normal_bai, donor_bam, donor_bai, redux_tsvs ->
                                                            ^^^^^^^^^^
  ```

- Warning: `subworkflows/local/sage_calling/main.nf:93:71`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          .branch { meta, tumor_bam, tumor_bai, normal_bam, normal_bai, donor_bam, donor_bai, redux_tsvs ->
                                                                        ^^^^^^^^^
  ```

- Warning: `subworkflows/local/sage_calling/main.nf:93:82`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          .branch { meta, tumor_bam, tumor_bai, normal_bam, normal_bai, donor_bam, donor_bai, redux_tsvs ->
                                                                                   ^^^^^^^^^
  ```

- Warning: `subworkflows/local/sage_calling/main.nf:93:93`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          .branch { meta, tumor_bam, tumor_bai, normal_bam, normal_bai, donor_bam, donor_bai, redux_tsvs ->
                                                                                              ^^^^^^^^^^
  ```

- Warning: `subworkflows/local/sage_calling/main.nf:106:36`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          .branch { meta, tumor_bam, tumor_bai, normal_bam, normal_bai, donor_bam, donor_bai, redux_tsvs ->
                                     ^^^^^^^^^
  ```

- Warning: `subworkflows/local/sage_calling/main.nf:106:59`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          .branch { meta, tumor_bam, tumor_bai, normal_bam, normal_bai, donor_bam, donor_bai, redux_tsvs ->
                                                            ^^^^^^^^^^
  ```

- Warning: `subworkflows/local/sage_calling/main.nf:106:71`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          .branch { meta, tumor_bam, tumor_bai, normal_bam, normal_bai, donor_bam, donor_bai, redux_tsvs ->
                                                                        ^^^^^^^^^
  ```

- Warning: `subworkflows/local/sage_calling/main.nf:106:82`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          .branch { meta, tumor_bam, tumor_bai, normal_bam, normal_bai, donor_bam, donor_bai, redux_tsvs ->
                                                                                   ^^^^^^^^^
  ```

- Warning: `subworkflows/local/sage_calling/main.nf:106:93`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          .branch { meta, tumor_bam, tumor_bai, normal_bam, normal_bai, donor_bam, donor_bai, redux_tsvs ->
                                                                                              ^^^^^^^^^^
  ```

- Warning: `subworkflows/local/sage_calling/main.nf:118:68`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          .map { meta, tumor_bam, tumor_bai, normal_bam, normal_bai, donor_bam, donor_bai, redux_tsvs ->
                                                                     ^^^^^^^^^
  ```

- Warning: `subworkflows/local/sage_calling/main.nf:118:79`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          .map { meta, tumor_bam, tumor_bai, normal_bam, normal_bai, donor_bam, donor_bai, redux_tsvs ->
                                                                                ^^^^^^^^^
  ```

- Warning: `subworkflows/local/sage_calling/main.nf:153:36`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          .branch { meta, tumor_bam, tumor_bai, normal_bam, normal_bai, donor_bam, donor_bai, redux_tsvs ->
                                     ^^^^^^^^^
  ```

- Warning: `subworkflows/local/sage_calling/main.nf:153:47`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          .branch { meta, tumor_bam, tumor_bai, normal_bam, normal_bai, donor_bam, donor_bai, redux_tsvs ->
                                                ^^^^^^^^^^
  ```

- Warning: `subworkflows/local/sage_calling/main.nf:153:59`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          .branch { meta, tumor_bam, tumor_bai, normal_bam, normal_bai, donor_bam, donor_bai, redux_tsvs ->
                                                            ^^^^^^^^^^
  ```

- Warning: `subworkflows/local/sage_calling/main.nf:153:71`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          .branch { meta, tumor_bam, tumor_bai, normal_bam, normal_bai, donor_bam, donor_bai, redux_tsvs ->
                                                                        ^^^^^^^^^
  ```

- Warning: `subworkflows/local/sage_calling/main.nf:153:82`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          .branch { meta, tumor_bam, tumor_bai, normal_bam, normal_bai, donor_bam, donor_bai, redux_tsvs ->
                                                                                   ^^^^^^^^^
  ```

- Warning: `subworkflows/local/sage_calling/main.nf:153:93`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          .branch { meta, tumor_bam, tumor_bai, normal_bam, normal_bai, donor_bam, donor_bai, redux_tsvs ->
                                                                                              ^^^^^^^^^^
  ```

- Warning: `subworkflows/local/sage_calling/main.nf:206:26`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_somatic_vcf_out = Channel.empty()
                           ^^^^^^^
  ```

- Warning: `subworkflows/local/sage_calling/main.nf:214:27`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_germline_vcf_out = Channel.empty()
                            ^^^^^^^
  ```

- Warning: `subworkflows/local/sage_calling/main.nf:222:22`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_somatic_dir = Channel.empty()
                       ^^^^^^^
  ```

- Warning: `subworkflows/local/sage_calling/main.nf:230:23`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_germline_dir = Channel.empty()
                        ^^^^^^^
  ```

- Warning: `subworkflows/local/sigs_fitting/main.nf:22:19`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_versions = Channel.empty()
                    ^^^^^^^
  ```

- Warning: `subworkflows/local/sigs_fitting/main.nf:81:18`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_outputs = Channel.empty()
                   ^^^^^^^
  ```

- Warning: `subworkflows/local/utils_nfcore_oncoanalyser_pipeline/main.nf:32:5`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
      monochrome_logs   // boolean: Do not use coloured log outputs
      ^^^^^^^^^^^^^^^
  ```

- Warning: `subworkflows/local/utils_nfcore_oncoanalyser_pipeline/main.nf:35:5`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
      input             //  string: Path to input samplesheet
      ^^^^^
  ```

- Warning: `workflows/prepare_reference.nf:24:19`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_versions = Channel.empty()
                    ^^^^^^^
  ```

- Warning: `workflows/prepare_reference.nf:38:26`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      def topic_versions = Channel.topic("versions")
                           ^^^^^^^
  ```
