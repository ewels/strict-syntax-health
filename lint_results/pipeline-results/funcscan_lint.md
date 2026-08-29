# Nextflow lint results

- Generated: 2026-08-29T00:17:29.607478585Z
- Nextflow version: 26.08.0-edge
- Summary: 64 warnings

## :warning: Warnings

- Warning: `conf/modules.config:616:65`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
              saveAs: { params.run_taxa_classification == false ? it : null },
                                                                  ^^
  ```

- Warning: `modules/nf-core/ampir/main.nf:25:9`: Variable was declared but not used

  ```nextflow
      def args = task.ext.args ?: ''
          ^^^^
  ```

- Warning: `modules/nf-core/ampir/main.nf:49:9`: Variable was declared but not used

  ```nextflow
      def args = task.ext.args ?: ''
          ^^^^
  ```

- Warning: `modules/nf-core/argnorm/main.nf:49:9`: Variable was declared but not used

  ```nextflow
      def args = task.ext.args ?: ''
          ^^^^
  ```

- Warning: `modules/nf-core/deeparg/predict/main.nf:65:9`: Variable was declared but not used

  ```nextflow
      def args = task.ext.args ?: ''
          ^^^^
  ```

- Warning: `modules/nf-core/deepbgc/download/main.nf:17:9`: Variable was declared but not used

  ```nextflow
      def args = task.ext.args ?: ''
          ^^^^
  ```

- Warning: `modules/nf-core/fargene/main.nf:56:9`: Variable was declared but not used

  ```nextflow
      def args = task.ext.args   ?: ''
          ^^^^
  ```

- Warning: `modules/nf-core/gunzip/main.nf:43:9`: Variable was declared but not used

  ```nextflow
      def args = task.ext.args ?: ''
          ^^^^
  ```

- Warning: `modules/nf-core/mmseqs/createdb/main.nf:45:9`: Variable was declared but not used

  ```nextflow
      def args = task.ext.args ?: ''
          ^^^^
  ```

- Warning: `modules/nf-core/mmseqs/createtsv/main.nf:52:9`: Variable was declared but not used

  ```nextflow
      def args = task.ext.args ?: ''
          ^^^^
  ```

- Warning: `modules/nf-core/mmseqs/taxonomy/main.nf:50:9`: Variable was declared but not used

  ```nextflow
      def args = task.ext.args ?: ''
          ^^^^
  ```

- Warning: `modules/nf-core/prodigal/main.nf:49:9`: Variable was declared but not used

  ```nextflow
      def args = task.ext.args   ?: ''
          ^^^^
  ```

- Warning: `modules/nf-core/pyrodigal/main.nf:48:9`: Variable was declared but not used

  ```nextflow
      def args = task.ext.args ?: ''
          ^^^^
  ```

- Warning: `subworkflows/local/annotation.nf:78:53`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          ch_multiqc_files = PROKKA.out.txt.collect { it[1] }.ifEmpty([])
                                                      ^^
  ```

- Warning: `subworkflows/local/annotation.nf:98:28`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
              ch_bakta_hmm = Channel.fromPath(params.annotation_bakta_hmms, checkIfExists: true).first()
                             ^^^^^^^
  ```

- Warning: `subworkflows/local/annotation.nf:112:58`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          ch_multiqc_files = BAKTA_BAKTA.out.txt.collect { it[1] }.ifEmpty([])
                                                           ^^
  ```

- Warning: `subworkflows/local/arg.nf:60:94`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
              ch_input_to_argnorm_amrfinderplus = HAMRONIZATION_AMRFINDERPLUS.out.tsv.filter { meta, file -> !file.isEmpty() }
                                                                                               ^^^^
  ```

- Warning: `subworkflows/local/arg.nf:78:26`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
                  fastas: [it[0], it[1]]
                           ^^
  ```

- Warning: `subworkflows/local/arg.nf:78:33`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
                  fastas: [it[0], it[1]]
                                  ^^
  ```

- Warning: `subworkflows/local/arg.nf:79:27`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
                  hmmclass: it[2]
                            ^^
  ```

- Warning: `subworkflows/local/arg.nf:100:49`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
              rgi_db = UNTAR_CARD.out.untar.map { it[1] }
                                                  ^^
  ```

- Warning: `subworkflows/local/arg.nf:164:82`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
              ch_input_to_argnorm_deeparg = HAMRONIZATION_DEEPARG.out.tsv.filter { meta, file -> !file.isEmpty() }
                                                                                   ^^^^
  ```

- Warning: `subworkflows/local/arg.nf:181:84`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
              ch_input_to_argnorm_abricate = HAMRONIZATION_ABRICATE.out.tsv.filter { meta, file -> !file.isEmpty() }
                                                                                     ^^^^
  ```

- Warning: `subworkflows/local/arg.nf:189:13`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
              it[1]
              ^^
  ```

- Warning: `subworkflows/local/arg.nf:200:46`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          ch_mmseqs_taxonomy_list = tsvs.map { it[1] }.collect()
                                               ^^
  ```

- Warning: `subworkflows/local/bgc.nf:96:26`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
                  fastas: [it[0], it[1], []]
                           ^^
  ```

- Warning: `subworkflows/local/bgc.nf:96:33`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
                  fastas: [it[0], it[1], []]
                                  ^^
  ```

- Warning: `subworkflows/local/bgc.nf:196:52`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          ch_combgc_summaries = COMBGC.out.tsv.map { it[1] }.collectFile(name: 'combgc_complete_summary.tsv', storeDir: "${params.outdir}/reports/combgc", keepHeader: true)
                                                     ^^
  ```

- Warning: `subworkflows/local/bgc.nf:199:52`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          ch_combgc_summaries = COMBGC.out.tsv.map { it[1] }.collectFile(name: 'combgc_complete_summary.tsv', keepHeader: true)
                                                     ^^
  ```

- Warning: `subworkflows/local/bgc.nf:205:46`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          ch_mmseqs_taxonomy_list = tsvs.map { it[1] }.collect()
                                               ^^
  ```

- Warning: `subworkflows/local/cazyme.nf:25:23`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
          ch_dbcan_db = Channel
                        ^^^^^^^
  ```

- Warning: `subworkflows/local/cazyme.nf:43:33`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
                  .filter { meta, faa, gff ->
                                  ^^^
  ```

- Warning: `subworkflows/local/taxa_class.nf:17:5`: Variable was declared but not used

  ```nextflow
      ch_taxonomy_querydb = channel.empty()
      ^^^^^^^^^^^^^^^^^^^
  ```

- Warning: `subworkflows/local/utils_nfcore_funcscan_pipeline/main.nf:114:5`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      Channel
      ^^^^^^^
  ```

- Warning: `workflows/funcscan.nf:73:25`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
              compressed: it[1].toString().endsWith('.gz')
                          ^^
  ```

- Warning: `workflows/funcscan.nf:74:27`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
              uncompressed: it[1]
                            ^^
  ```

- Warning: `workflows/funcscan.nf:86:44`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
              def fasta_found = files.find { it.toString().tokenize('.').last().matches('fasta|fas|fna|fa') }
                                             ^^
  ```

- Warning: `workflows/funcscan.nf:87:42`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
              def faa_found = files.find { it.toString().endsWith('.faa') }
                                           ^^
  ```

- Warning: `workflows/funcscan.nf:88:42`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
              def gff_found = files.find { it.toString().tokenize('.').last().matches('gff|gff3') }
                                           ^^
  ```

- Warning: `workflows/funcscan.nf:89:42`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
              def gbk_found = files.find { it.toString().tokenize('.').last().matches('gbk|gbff') }
                                           ^^
  ```

- Warning: `workflows/funcscan.nf:97:19`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          .branch { meta, fasta, faa, gff, gbk ->
                    ^^^^
  ```

- Warning: `workflows/funcscan.nf:97:25`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          .branch { meta, fasta, faa, gff, gbk ->
                          ^^^^^
  ```

- Warning: `workflows/funcscan.nf:97:32`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          .branch { meta, fasta, faa, gff, gbk ->
                                 ^^^
  ```

- Warning: `workflows/funcscan.nf:105:75`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          SEQKIT_SEQ_LENGTH(ch_intermediate_input.fastas.map { meta, fasta, faa, gff, gbk -> [meta, fasta] })
                                                                            ^^^
  ```

- Warning: `workflows/funcscan.nf:105:80`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          SEQKIT_SEQ_LENGTH(ch_intermediate_input.fastas.map { meta, fasta, faa, gff, gbk -> [meta, fasta] })
                                                                                 ^^^
  ```

- Warning: `workflows/funcscan.nf:105:85`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          SEQKIT_SEQ_LENGTH(ch_intermediate_input.fastas.map { meta, fasta, faa, gff, gbk -> [meta, fasta] })
                                                                                      ^^^
  ```

- Warning: `workflows/funcscan.nf:107:33`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
              .map { meta, fasta, protein, gff, gbk -> [meta, fasta] }
                                  ^^^^^^^
  ```

- Warning: `workflows/funcscan.nf:107:42`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
              .map { meta, fasta, protein, gff, gbk -> [meta, fasta] }
                                           ^^^
  ```

- Warning: `workflows/funcscan.nf:107:47`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
              .map { meta, fasta, protein, gff, gbk -> [meta, fasta] }
                                                ^^^
  ```

- Warning: `workflows/funcscan.nf:118:83`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          ch_input_for_annotation = ch_intermediate_input.fastas.map { meta, fasta, protein, gff, gbk -> [meta, fasta] }
                                                                                    ^^^^^^^
  ```

- Warning: `workflows/funcscan.nf:118:92`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          ch_input_for_annotation = ch_intermediate_input.fastas.map { meta, fasta, protein, gff, gbk -> [meta, fasta] }
                                                                                             ^^^
  ```

- Warning: `workflows/funcscan.nf:118:97`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          ch_input_for_annotation = ch_intermediate_input.fastas.map { meta, fasta, protein, gff, gbk -> [meta, fasta] }
                                                                                                  ^^^
  ```

- Warning: `workflows/funcscan.nf:140:64`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
      ch_new_annotation_short = ch_new_annotation.filter { meta, fasta, faa, gff, gbk -> meta.category != 'long' }
                                                                 ^^^^^
  ```

- Warning: `workflows/funcscan.nf:140:71`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
      ch_new_annotation_short = ch_new_annotation.filter { meta, fasta, faa, gff, gbk -> meta.category != 'long' }
                                                                        ^^^
  ```

- Warning: `workflows/funcscan.nf:140:76`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
      ch_new_annotation_short = ch_new_annotation.filter { meta, fasta, faa, gff, gbk -> meta.category != 'long' }
                                                                             ^^^
  ```

- Warning: `workflows/funcscan.nf:140:81`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
      ch_new_annotation_short = ch_new_annotation.filter { meta, fasta, faa, gff, gbk -> meta.category != 'long' }
                                                                                  ^^^
  ```

- Warning: `workflows/funcscan.nf:166:29`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
              .filter { meta, fasta, faa, gff, gbk -> meta.category == 'long' }
                              ^^^^^
  ```

- Warning: `workflows/funcscan.nf:166:36`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
              .filter { meta, fasta, faa, gff, gbk -> meta.category == 'long' }
                                     ^^^
  ```

- Warning: `workflows/funcscan.nf:166:41`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
              .filter { meta, fasta, faa, gff, gbk -> meta.category == 'long' }
                                          ^^^
  ```

- Warning: `workflows/funcscan.nf:166:46`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
              .filter { meta, fasta, faa, gff, gbk -> meta.category == 'long' }
                                               ^^^
  ```

- Warning: `workflows/funcscan.nf:190:9`: Variable was declared but not used

  ```nextflow
          ch_mmseqs_db = channel.empty()
          ^^^^^^^^^^^^
  ```

- Warning: `workflows/funcscan.nf:191:9`: Variable was declared but not used

  ```nextflow
          ch_taxonomy_querydb = channel.empty()
          ^^^^^^^^^^^^^^^^^^^
  ```

- Warning: `workflows/funcscan.nf:192:9`: Variable was declared but not used

  ```nextflow
          ch_taxonomy_querydb_taxdb = channel.empty()
          ^^^^^^^^^^^^^^^^^^^^^^^^^
  ```

- Warning: `workflows/funcscan.nf:437:88`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          ch_multiqc_files = ch_multiqc_files.mix(ANNOTATION.out.multiqc_files.collect { it[1] })
                                                                                         ^^
  ```
