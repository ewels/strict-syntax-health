# Nextflow lint results

- Generated: 2026-01-16T06:33:21.318282904Z
- Nextflow version: 25.12.0-edge
- Summary: 31 warnings

## :warning: Warnings

- Warning: `modules/local/gstama/filelist/main.nf:20:9`: Variable was declared but not used

  ```nextflow
      def args = task.ext.args ?: ''
          ^^^^
  ```

- Warning: `modules/nf-core/gunzip/main.nf:43:9`: Variable was declared but not used

  ```nextflow
      def args = task.ext.args ?: ''
          ^^^^
  ```

- Warning: `modules/nf-core/isoseq/refine/main.nf:44:9`: Variable was declared but not used

  ```nextflow
      def args = task.ext.args ?: ''
          ^^^^
  ```

- Warning: `modules/nf-core/isoseq/refine/main.nf:45:9`: Variable was declared but not used

  ```nextflow
      def prefix = task.ext.prefix ?: "${meta.id}"
          ^^^^^^
  ```

- Warning: `modules/nf-core/minimap2/align/main.nf:67:9`: Variable was declared but not used

  ```nextflow
      def target = reference ?: (bam_input ? error("BAM input requires reference") : reads)
          ^^^^^^
  ```

- Warning: `modules/nf-core/pbccs/main.nf:47:9`: Variable was declared but not used

  ```nextflow
      def args = task.ext.args ?: ''
          ^^^^
  ```

- Warning: `modules/nf-core/pbccs/main.nf:48:9`: Variable was declared but not used

  ```nextflow
      def prefix = task.ext.prefix ?: "${meta.id}"
          ^^^^^^
  ```

- Warning: `subworkflows/local/set_value_channel.nf:15:20`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
              .map { it[1] }
                     ^^
  ```

- Warning: `subworkflows/local/utils_nfcore_isoseq_pipeline/main.nf:32:5`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
      monochrome_logs   // boolean: Do not use coloured log outputs
      ^^^^^^^^^^^^^^^
  ```

- Warning: `subworkflows/local/utils_nfcore_isoseq_pipeline/main.nf:35:5`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
      input             //  string: Path to input samplesheet
      ^^^^^
  ```

- Warning: `subworkflows/local/utils_nfcore_isoseq_pipeline/main.nf:42:19`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_versions = Channel.empty()
                    ^^^^^^^
  ```

- Warning: `subworkflows/local/utils_nfcore_isoseq_pipeline/main.nf:67:144`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
      after_text = """${workflow.manifest.doi ? "\n* The pipeline\n" : ""}${workflow.manifest.doi.tokenize(",").collect { "    https://doi.org/${it.trim().replace('https://doi.org/','')}"}.join("\n")}${workflow.manifest.doi ? "\n" : ""}
                                                                                                                                                 ^^
  ```

- Warning: `subworkflows/local/utils_nfcore_isoseq_pipeline/main.nf:104:9`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
          Channel
          ^^^^^^^
  ```

- Warning: `subworkflows/local/utils_nfcore_isoseq_pipeline/main.nf:106:45`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
              .flatMap { create_pbccs_channel(it, params.chunk) }
                                              ^^
  ```

- Warning: `subworkflows/local/utils_nfcore_isoseq_pipeline/main.nf:111:9`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
          Channel
          ^^^^^^^
  ```

- Warning: `subworkflows/local/utils_nfcore_isoseq_pipeline/main.nf:113:45`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
              .flatMap { create_reads_channel(it) }
                                              ^^
  ```

- Warning: `subworkflows/local/utils_nfcore_isoseq_pipeline/main.nf:121:28`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
                  def chk = (it[1] =~ /(chunk\.\d+)\.gz/)[ 0 ][ 1 ]
                             ^^
  ```

- Warning: `subworkflows/local/utils_nfcore_isoseq_pipeline/main.nf:122:33`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
                  def id_former = it[0].id
                                  ^^
  ```

- Warning: `subworkflows/local/utils_nfcore_isoseq_pipeline/main.nf:123:33`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
                  def id_new    = it[0].id + "." + chk
                                  ^^
  ```

- Warning: `subworkflows/local/utils_nfcore_isoseq_pipeline/main.nf:124:56`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
                  [ [ id:id_new, id_former:id_former ] , it[1] ]
                                                         ^^
  ```

- Warning: `subworkflows/nf-core/utils_nfcore_pipeline/main.nf:101:98`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      return ch_versions.unique().map { version -> processVersionsFromYAML(version) }.unique().mix(Channel.of(workflowVersionToYAML()))
                                                                                                   ^^^^^^^
  ```

- Warning: `workflows/isoseq.nf:142:39`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
              .map { meta1, pickle, db, meta2, reads -> [meta1, pickle, db] }
                                        ^^^^^
  ```

- Warning: `workflows/isoseq.nf:142:46`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
              .map { meta1, pickle, db, meta2, reads -> [meta1, pickle, db] }
                                               ^^^^^
  ```

- Warning: `workflows/isoseq.nf:162:22`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          .map { [ [id:it[0].id_former], it[1] ] }
                       ^^
  ```

- Warning: `workflows/isoseq.nf:162:40`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          .map { [ [id:it[0].id_former], it[1] ] }
                                         ^^
  ```

- Warning: `workflows/isoseq.nf:177:39`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
      GSTAMA_MERGE(ch_tmerge_in.map { [ it[0], it[1] ] }, ch_tmerge_in.map { it[2] }) // Merge all bed files from one sample into a uniq bed file
                                        ^^
  ```

- Warning: `workflows/isoseq.nf:177:46`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
      GSTAMA_MERGE(ch_tmerge_in.map { [ it[0], it[1] ] }, ch_tmerge_in.map { it[2] }) // Merge all bed files from one sample into a uniq bed file
                                               ^^
  ```

- Warning: `workflows/isoseq.nf:177:76`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
      GSTAMA_MERGE(ch_tmerge_in.map { [ it[0], it[1] ] }, ch_tmerge_in.map { it[2] }) // Merge all bed files from one sample into a uniq bed file
                                                                             ^^
  ```

- Warning: `workflows/isoseq.nf:258:79`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          ch_multiqc_files = ch_multiqc_files.mix(PBCCS.out.report_json.collect{it[1]}.ifEmpty([]))
                                                                                ^^
  ```

- Warning: `workflows/isoseq.nf:259:74`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          ch_multiqc_files = ch_multiqc_files.mix(LIMA.out.summary.collect{it[1]}.ifEmpty([]))
                                                                           ^^
  ```

- Warning: `workflows/isoseq.nf:260:73`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          ch_multiqc_files = ch_multiqc_files.mix(LIMA.out.counts.collect{it[1]}.ifEmpty([]))
                                                                          ^^
  ```
