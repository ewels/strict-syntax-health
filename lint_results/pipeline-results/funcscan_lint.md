# Nextflow lint results

- Generated: 2026-01-21T13:33:49.012516154Z
- Nextflow version: 25.12.0-edge
- Summary: 73 warnings

## :warning: Warnings

- Warning: `conf/modules.config:592:65`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
              saveAs: { params.run_taxa_classification == false ? it : null },
                                                                  ^^
  ```

- Warning: `modules/nf-core/ampcombi2/cluster/main.nf:37:9`: Variable was declared but not used

  ```nextflow
      def args = task.ext.args ?: ''
          ^^^^
  ```

- Warning: `modules/nf-core/ampcombi2/complete/main.nf:25:49`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          --summaries_files '${summaries.collect{"$it"}.join("' '")}' \\
                                                  ^^
  ```

- Warning: `modules/nf-core/ampcombi2/complete/main.nf:35:9`: Variable was declared but not used

  ```nextflow
      def args = task.ext.args ?: ''
          ^^^^
  ```

- Warning: `modules/nf-core/ampcombi2/parsetables/main.nf:43:47`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          --path_list '${amp_input.collect { "${it}" }.join("' '")}' \\
                                                ^^
  ```

- Warning: `modules/nf-core/ampcombi2/parsetables/main.nf:60:9`: Variable was declared but not used

  ```nextflow
      def args = task.ext.args ?: ''
          ^^^^
  ```

- Warning: `modules/nf-core/ampcombi2/parsetables/main.nf:62:9`: Variable was declared but not used

  ```nextflow
      def db_dir = opt_amp_db_dir ? "--amp_database_dir ${opt_amp_db_dir}" : ""
          ^^^^^^
  ```

- Warning: `modules/nf-core/ampcombi2/parsetables/main.nf:63:9`: Variable was declared but not used

  ```nextflow
      def interpro = opt_interproscan ? "--interproscan_output ${opt_interproscan}" : ""
          ^^^^^^^^
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

- Warning: `modules/nf-core/gecco/convert/main.nf:27:9`: Variable was declared but not used

  ```nextflow
      def prefix = task.ext.prefix ?: "${meta.id}" // IMPORTANT: -o ${prefix} does not work in 0.10.0
          ^^^^^^
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

- Warning: `subworkflows/local/amp.nf:111:21`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
              input: [it[0], it[1]]
                      ^^
  ```

- Warning: `subworkflows/local/amp.nf:111:28`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
              input: [it[0], it[1]]
                             ^^
  ```

- Warning: `subworkflows/local/amp.nf:112:18`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
              faa: it[2]
                   ^^
  ```

- Warning: `subworkflows/local/amp.nf:113:18`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
              gbk: it[3]
                   ^^
  ```

- Warning: `subworkflows/local/amp.nf:114:23`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
              interpro: it[4]
                        ^^
  ```

- Warning: `subworkflows/local/amp.nf:129:65`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
      ch_ampcombi_summaries = AMPCOMBI2_PARSETABLES.out.tsv.map { it[1] }.collect()
                                                                  ^^
  ```

- Warning: `subworkflows/local/amp.nf:132:52`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
      ch_summary_count = ch_ampcombi_summaries.map { it.size() }.sum()
                                                     ^^
  ```

- Warning: `subworkflows/local/amp.nf:157:46`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          ch_mmseqs_taxonomy_list = tsvs.map { it[1] }.collect()
                                               ^^
  ```

- Warning: `subworkflows/local/annotation.nf:65:53`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          ch_multiqc_files = PROKKA.out.txt.collect { it[1] }.ifEmpty([])
                                                      ^^
  ```

- Warning: `subworkflows/local/annotation.nf:85:28`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
              ch_bakta_hmm = Channel.fromPath(params.annotation_bakta_hmms, checkIfExists: true).first()
                             ^^^^^^^
  ```

- Warning: `subworkflows/local/annotation.nf:100:58`: Implicit closure parameter is deprecated, declare an explicit parameter instead

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

- Warning: `subworkflows/local/bgc.nf:94:26`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
                  fastas: [it[0], it[1], []]
                           ^^
  ```

- Warning: `subworkflows/local/bgc.nf:94:33`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
                  fastas: [it[0], it[1], []]
                                  ^^
  ```

- Warning: `subworkflows/local/bgc.nf:164:52`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          ch_combgc_summaries = COMBGC.out.tsv.map { it[1] }.collectFile(name: 'combgc_complete_summary.tsv', storeDir: "${params.outdir}/reports/combgc", keepHeader: true)
                                                     ^^
  ```

- Warning: `subworkflows/local/bgc.nf:167:52`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          ch_combgc_summaries = COMBGC.out.tsv.map { it[1] }.collectFile(name: 'combgc_complete_summary.tsv', keepHeader: true)
                                                     ^^
  ```

- Warning: `subworkflows/local/bgc.nf:173:46`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          ch_mmseqs_taxonomy_list = tsvs.map { it[1] }.collect()
                                               ^^
  ```

- Warning: `subworkflows/local/taxa_class.nf:17:5`: Variable was declared but not used

  ```nextflow
      ch_taxonomy_querydb = channel.empty()
      ^^^^^^^^^^^^^^^^^^^
  ```

- Warning: `subworkflows/local/utils_nfcore_funcscan_pipeline/main.nf:31:5`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
      monochrome_logs // boolean: Do not use coloured log outputs
      ^^^^^^^^^^^^^^^
  ```

- Warning: `subworkflows/local/utils_nfcore_funcscan_pipeline/main.nf:102:5`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      Channel
      ^^^^^^^
  ```

- Warning: `workflows/funcscan.nf:74:25`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
              compressed: it[1].toString().endsWith('.gz')
                          ^^
  ```

- Warning: `workflows/funcscan.nf:75:27`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
              uncompressed: it[1]
                            ^^
  ```

- Warning: `workflows/funcscan.nf:87:44`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
              def fasta_found = files.find { it.toString().tokenize('.').last().matches('fasta|fas|fna|fa') }
                                             ^^
  ```

- Warning: `workflows/funcscan.nf:88:42`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
              def faa_found = files.find { it.toString().endsWith('.faa') }
                                           ^^
  ```

- Warning: `workflows/funcscan.nf:89:42`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
              def gbk_found = files.find { it.toString().tokenize('.').last().matches('gbk|gbff') }
                                           ^^
  ```

- Warning: `workflows/funcscan.nf:96:19`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          .branch { meta, fasta, faa, gbk ->
                    ^^^^
  ```

- Warning: `workflows/funcscan.nf:96:25`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          .branch { meta, fasta, faa, gbk ->
                          ^^^^^
  ```

- Warning: `workflows/funcscan.nf:96:32`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          .branch { meta, fasta, faa, gbk ->
                                 ^^^
  ```

- Warning: `workflows/funcscan.nf:104:75`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          SEQKIT_SEQ_LENGTH(ch_intermediate_input.fastas.map { meta, fasta, faa, gbk -> [meta, fasta] })
                                                                            ^^^
  ```

- Warning: `workflows/funcscan.nf:104:80`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          SEQKIT_SEQ_LENGTH(ch_intermediate_input.fastas.map { meta, fasta, faa, gbk -> [meta, fasta] })
                                                                                 ^^^
  ```

- Warning: `workflows/funcscan.nf:106:33`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
              .map { meta, fasta, protein, gbk -> [meta, fasta] }
                                  ^^^^^^^
  ```

- Warning: `workflows/funcscan.nf:106:42`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
              .map { meta, fasta, protein, gbk -> [meta, fasta] }
                                           ^^^
  ```

- Warning: `workflows/funcscan.nf:117:83`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          ch_input_for_annotation = ch_intermediate_input.fastas.map { meta, fasta, protein, gbk -> [meta, fasta] }
                                                                                    ^^^^^^^
  ```

- Warning: `workflows/funcscan.nf:117:92`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          ch_input_for_annotation = ch_intermediate_input.fastas.map { meta, fasta, protein, gbk -> [meta, fasta] }
                                                                                             ^^^
  ```

- Warning: `workflows/funcscan.nf:139:25`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          .filter { meta, fasta, faa, gbk -> meta.category != 'long' }
                          ^^^^^
  ```

- Warning: `workflows/funcscan.nf:139:32`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          .filter { meta, fasta, faa, gbk -> meta.category != 'long' }
                                 ^^^
  ```

- Warning: `workflows/funcscan.nf:139:37`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          .filter { meta, fasta, faa, gbk -> meta.category != 'long' }
                                      ^^^
  ```

- Warning: `workflows/funcscan.nf:150:29`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
              .filter { meta, fasta, faa, gbk -> meta.category == 'long' }
                              ^^^^^
  ```

- Warning: `workflows/funcscan.nf:150:36`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
              .filter { meta, fasta, faa, gbk -> meta.category == 'long' }
                                     ^^^
  ```

- Warning: `workflows/funcscan.nf:150:41`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
              .filter { meta, fasta, faa, gbk -> meta.category == 'long' }
                                          ^^^
  ```

- Warning: `workflows/funcscan.nf:173:9`: Variable was declared but not used

  ```nextflow
          ch_mmseqs_db = channel.empty()
          ^^^^^^^^^^^^
  ```

- Warning: `workflows/funcscan.nf:174:9`: Variable was declared but not used

  ```nextflow
          ch_taxonomy_querydb = channel.empty()
          ^^^^^^^^^^^^^^^^^^^
  ```

- Warning: `workflows/funcscan.nf:175:9`: Variable was declared but not used

  ```nextflow
          ch_taxonomy_querydb_taxdb = channel.empty()
          ^^^^^^^^^^^^^^^^^^^^^^^^^
  ```

- Warning: `workflows/funcscan.nf:431:88`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          ch_multiqc_files = ch_multiqc_files.mix(ANNOTATION.out.multiqc_files.collect { it[1] })
                                                                                         ^^
  ```
