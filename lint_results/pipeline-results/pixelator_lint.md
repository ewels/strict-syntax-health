# Nextflow lint results

- Generated: 2026-08-25T00:11:42.983268334Z
- Nextflow version: 26.08.0-edge
- Summary: 16 warnings

## :warning: Warnings

- Warning: `conf/modules.pna.config:172:89`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
                  saveAs: { params.save_pna_sample_calling_pixelfile || params.save_all ? it : null },
                                                                                          ^^
  ```

- Warning: `conf/modules.pna.config:183:65`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
                  saveAs: { params.save_json || params.save_all ? it : null },
                                                                  ^^
  ```

- Warning: `modules/local/experiment_summary/main.nf:30:51`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
      def stageArray = result_stages.collect { "\"${it}\"" }.join(' ')
                                                    ^^
  ```

- Warning: `subworkflows/local/pna/v1/main.nf:94:5`: Variable was declared but not used

  ```nextflow
      ch_cat_panel_files = ch_cat_fastq
      ^^^^^^^^^^^^^^^^^^
  ```

- Warning: `subworkflows/local/pna/v1/main.nf:205:24`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
              .flatMap { it }
                         ^^
  ```

- Warning: `subworkflows/local/pna/v1/main.nf:209:55`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
                  def stages = stageFilePairs.collect { it[0] }
                                                        ^^
  ```

- Warning: `subworkflows/local/pna/v1/main.nf:210:54`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
                  def files = stageFilePairs.collect { it[1] }
                                                       ^^
  ```

- Warning: `subworkflows/local/pna/v2/main.nf:115:5`: Variable was declared but not used

  ```nextflow
      ch_cat_panel_files = ch_cat_fastq
      ^^^^^^^^^^^^^^^^^^
  ```

- Warning: `subworkflows/local/pna/v2/main.nf:118:16`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          .map { id, meta, panel_files -> [meta, panel_files] }
                 ^^
  ```

- Warning: `subworkflows/local/pna/v2/main.nf:170:42`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
              def parquet = data.collect { it[1] }.flatten()
                                           ^^
  ```

- Warning: `subworkflows/local/pna/v2/main.nf:171:42`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
              def reports = data.collect { it[2] }.flatten()
                                           ^^
  ```

- Warning: `subworkflows/local/pna/v2/main.nf:176:17`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          single: it[1].size() == 1
                  ^^
  ```

- Warning: `subworkflows/local/pna/v2/main.nf:177:16`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          multi: it[1].size() > 1
                 ^^
  ```

- Warning: `subworkflows/local/pna/v2/main.nf:248:24`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
              .flatMap { it }
                         ^^
  ```

- Warning: `subworkflows/local/pna/v2/main.nf:252:55`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
                  def stages = stageFilePairs.collect { it[0] }
                                                        ^^
  ```

- Warning: `subworkflows/local/pna/v2/main.nf:253:54`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
                  def files = stageFilePairs.collect { it[1] }
                                                       ^^
  ```
