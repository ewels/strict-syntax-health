# Nextflow lint results

- Generated: 2026-08-26T00:11:43.963459126Z
- Nextflow version: 26.08.0-edge
- Summary: 9 warnings

## :warning: Warnings

- Warning: `modules/local/gstama/filelist/main.nf:20:9`: Variable was declared but not used

  ```nextflow
      def args = task.ext.args ?: ''
          ^^^^
  ```

- Warning: `subworkflows/local/set_value_channel/main.nf:15:20`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
              .map { it[1] }
                     ^^
  ```

- Warning: `subworkflows/local/utils_nfcore_isoseq_pipeline/main.nf:34:5`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
      input             //  string: Path to input samplesheet
      ^^^^^
  ```

- Warning: `workflows/isoseq.nf:215:39`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
      GSTAMA_MERGE(ch_tmerge_in.map { [ it[0], it[1] ] }, ch_tmerge_in.map { it[2] }) // Merge all bed files from one sample into a uniq bed file
                                        ^^
  ```

- Warning: `workflows/isoseq.nf:215:46`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
      GSTAMA_MERGE(ch_tmerge_in.map { [ it[0], it[1] ] }, ch_tmerge_in.map { it[2] }) // Merge all bed files from one sample into a uniq bed file
                                               ^^
  ```

- Warning: `workflows/isoseq.nf:215:76`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
      GSTAMA_MERGE(ch_tmerge_in.map { [ it[0], it[1] ] }, ch_tmerge_in.map { it[2] }) // Merge all bed files from one sample into a uniq bed file
                                                                             ^^
  ```

- Warning: `workflows/isoseq.nf:285:75`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
      ch_multiqc_files = ch_multiqc_files.mix(PBCCS.out.report_json.collect{it[1]}.ifEmpty([]))
                                                                            ^^
  ```

- Warning: `workflows/isoseq.nf:286:70`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
      ch_multiqc_files = ch_multiqc_files.mix(LIMA.out.summary.collect{it[1]}.ifEmpty([]))
                                                                       ^^
  ```

- Warning: `workflows/isoseq.nf:287:69`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
      ch_multiqc_files = ch_multiqc_files.mix(LIMA.out.counts.collect{it[1]}.ifEmpty([]))
                                                                      ^^
  ```
