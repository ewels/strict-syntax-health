# Nextflow lint results

- Generated: 2026-01-16T10:21:06.179633042Z
- Nextflow version: 25.12.0-edge
- Summary: 6 errors, 115 warnings

## :x: Errors

- Error: `modules/nf-core/rgi/cardannotation/main.nf:14:9`: `RGI_VERSION` is not defined

  ```nextflow
      env RGI_VERSION, emit: tool_version
          ^^^^^^^^^^^
  ```

- Error: `modules/nf-core/rgi/cardannotation/main.nf:15:9`: `DB_VERSION` is not defined

  ```nextflow
      env DB_VERSION, emit: db_version
          ^^^^^^^^^^
  ```

- Error: `modules/nf-core/rgi/main/main.nf:19:9`: `RGI_VERSION` is not defined

  ```nextflow
      env RGI_VERSION, emit: tool_version
          ^^^^^^^^^^^
  ```

- Error: `modules/nf-core/rgi/main/main.nf:20:9`: `DB_VERSION` is not defined

  ```nextflow
      env DB_VERSION, emit: db_version
          ^^^^^^^^^^
  ```

- Error: `subworkflows/local/arg.nf:73:26`: `fastas` is already declared

  ```nextflow
              .map { meta, fastas, hmm_class ->
                           ^^^^^^
  ```

- Error: `workflows/funcscan.nf:206:65`: `_` is not allowed as an identifier because it is reserved for future use

  ```nextflow
          ch_interproscan_tsv = ch_prepped_input.faas.map { meta, _ ->
                                                                  ^
  ```

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

- Warning: `subworkflows/local/amp.nf:27:38`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_versions                    = Channel.empty()
                                       ^^^^^^^
  ```

- Warning: `subworkflows/local/amp.nf:28:38`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_ampresults_for_ampcombi     = Channel.empty()
                                       ^^^^^^^
  ```

- Warning: `subworkflows/local/amp.nf:29:38`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_macrel_faa                  = Channel.empty()
                                       ^^^^^^^
  ```

- Warning: `subworkflows/local/amp.nf:30:38`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_ampcombi_summaries          = Channel.empty()
                                       ^^^^^^^
  ```

- Warning: `subworkflows/local/amp.nf:72:66`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
          if ( params.amp_hmmsearch_models ) { ch_amp_hmm_models = Channel.fromPath( params.amp_hmmsearch_models, checkIfExists: true ) } else { error('[nf-core/funcscan] error: HMM model files not found for --amp_hmmsearch_models! Please check input.') }
                                                                   ^^^^^^^
  ```

- Warning: `subworkflows/local/amp.nf:110:22`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
              input: [ it[0], it[1] ]
                       ^^
  ```

- Warning: `subworkflows/local/amp.nf:110:29`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
              input: [ it[0], it[1] ]
                              ^^
  ```

- Warning: `subworkflows/local/amp.nf:111:18`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
              faa: it[2]
                   ^^
  ```

- Warning: `subworkflows/local/amp.nf:112:18`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
              gbk: it[3]
                   ^^
  ```

- Warning: `subworkflows/local/amp.nf:113:23`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
              interpro: it [4]
                        ^^
  ```

- Warning: `subworkflows/local/amp.nf:127:64`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
      ch_ampcombi_summaries = AMPCOMBI2_PARSETABLES.out.tsv.map{ it[1] }.collect()
                                                                 ^^
  ```

- Warning: `subworkflows/local/amp.nf:130:52`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
      ch_summary_count = ch_ampcombi_summaries.map { it.size() }.sum()
                                                     ^^
  ```

- Warning: `subworkflows/local/amp.nf:153:45`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          ch_mmseqs_taxonomy_list = tsvs.map{ it[1] }.collect()
                                              ^^
  ```

- Warning: `subworkflows/local/amp.nf:158:26`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
          ch_tabix_input = Channel.of( [ 'id':'ampcombi_complete_summary_taxonomy' ] )
                           ^^^^^^^
  ```

- Warning: `subworkflows/local/annotation.nf:22:19`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_versions = Channel.empty()
                    ^^^^^^^
  ```

- Warning: `subworkflows/local/annotation.nf:23:24`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_multiqc_files = Channel.empty()
                         ^^^^^^^
  ```

- Warning: `subworkflows/local/annotation.nf:65:53`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          ch_multiqc_files = PROKKA.out.txt.collect { it[1] }.ifEmpty([])
                                                      ^^
  ```

- Warning: `subworkflows/local/annotation.nf:74:27`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
              ch_bakta_db = Channel.fromPath(params.annotation_bakta_db, checkIfExists: true)
                            ^^^^^^^
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

- Warning: `subworkflows/local/arg.nf:33:19`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_versions = Channel.empty()
                    ^^^^^^^
  ```

- Warning: `subworkflows/local/arg.nf:36:43`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_input_to_hamronization_summarize = Channel.empty()
                                            ^^^^^^^
  ```

- Warning: `subworkflows/local/arg.nf:41:31`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
          ch_amrfinderplus_db = Channel
                                ^^^^^^^
  ```

- Warning: `subworkflows/local/arg.nf:61:94`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
              ch_input_to_argnorm_amrfinderplus = HAMRONIZATION_AMRFINDERPLUS.out.tsv.filter { meta, file -> !file.isEmpty() }
                                                                                               ^^^^
  ```

- Warning: `subworkflows/local/arg.nf:69:30`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
          ch_fargene_classes = Channel.fromList(params.arg_fargene_hmmmodel.tokenize(','))
                               ^^^^^^^
  ```

- Warning: `subworkflows/local/arg.nf:79:26`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
                  fastas: [it[0], it[1]]
                           ^^
  ```

- Warning: `subworkflows/local/arg.nf:79:33`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
                  fastas: [it[0], it[1]]
                                  ^^
  ```

- Warning: `subworkflows/local/arg.nf:80:27`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
                  hmmclass: it[2]
                            ^^
  ```

- Warning: `subworkflows/local/arg.nf:101:49`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
              rgi_db = UNTAR_CARD.out.untar.map { it[1] }
                                                  ^^
  ```

- Warning: `subworkflows/local/arg.nf:131:25`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
          ch_deeparg_db = Channel
                          ^^^^^^^
  ```

- Warning: `subworkflows/local/arg.nf:166:82`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
              ch_input_to_argnorm_deeparg = HAMRONIZATION_DEEPARG.out.tsv.filter { meta, file -> !file.isEmpty() }
                                                                                   ^^^^
  ```

- Warning: `subworkflows/local/arg.nf:183:84`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
              ch_input_to_argnorm_abricate = HAMRONIZATION_ABRICATE.out.tsv.filter { meta, file -> !file.isEmpty() }
                                                                                     ^^^^
  ```

- Warning: `subworkflows/local/arg.nf:191:13`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
              it[1]
              ^^
  ```

- Warning: `subworkflows/local/arg.nf:202:46`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          ch_mmseqs_taxonomy_list = tsvs.map { it[1] }.collect()
                                               ^^
  ```

- Warning: `subworkflows/local/arg.nf:206:26`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
          ch_tabix_input = Channel
                           ^^^^^^^
  ```

- Warning: `subworkflows/local/bgc.nf:25:19`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_versions = Channel.empty()
                    ^^^^^^^
  ```

- Warning: `subworkflows/local/bgc.nf:26:32`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_bgcresults_for_combgc = Channel.empty()
                                 ^^^^^^^
  ```

- Warning: `subworkflows/local/bgc.nf:42:38`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
              ch_antismash_databases = Channel.fromPath(params.bgc_antismash_db, checkIfExists: true).first()
                                       ^^^^^^^
  ```

- Warning: `subworkflows/local/bgc.nf:75:35`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
              ch_deepbgc_database = Channel
                                    ^^^^^^^
  ```

- Warning: `subworkflows/local/bgc.nf:95:26`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
                  fastas: [it[0], it[1], []]
                           ^^
  ```

- Warning: `subworkflows/local/bgc.nf:95:33`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
                  fastas: [it[0], it[1], []]
                                  ^^
  ```

- Warning: `subworkflows/local/bgc.nf:123:33`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
              ch_bgc_hmm_models = Channel.fromPath(params.bgc_hmmsearch_models, checkIfExists: true)
                                  ^^^^^^^
  ```

- Warning: `subworkflows/local/bgc.nf:165:52`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          ch_combgc_summaries = COMBGC.out.tsv.map { it[1] }.collectFile(name: 'combgc_complete_summary.tsv', storeDir: "${params.outdir}/reports/combgc", keepHeader: true)
                                                     ^^
  ```

- Warning: `subworkflows/local/bgc.nf:168:52`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          ch_combgc_summaries = COMBGC.out.tsv.map { it[1] }.collectFile(name: 'combgc_complete_summary.tsv', keepHeader: true)
                                                     ^^
  ```

- Warning: `subworkflows/local/bgc.nf:174:46`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          ch_mmseqs_taxonomy_list = tsvs.map { it[1] }.collect()
                                               ^^
  ```

- Warning: `subworkflows/local/bgc.nf:178:26`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
          ch_tabix_input = Channel
                           ^^^^^^^
  ```

- Warning: `subworkflows/local/protein_annotation.nf:13:36`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_versions                  = Channel.empty()
                                     ^^^^^^^
  ```

- Warning: `subworkflows/local/protein_annotation.nf:14:36`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_interproscan_tsv          = Channel.empty()
                                     ^^^^^^^
  ```

- Warning: `subworkflows/local/protein_annotation.nf:15:36`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_interproscan_db           = Channel.empty()
                                     ^^^^^^^
  ```

- Warning: `subworkflows/local/protein_annotation.nf:16:36`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_interproscan_tsv_modified = Channel.empty()
                                     ^^^^^^^
  ```

- Warning: `subworkflows/local/protein_annotation.nf:23:34`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
              ch_interproscan_db = Channel
                                   ^^^^^^^
  ```

- Warning: `subworkflows/local/taxa_class.nf:15:19`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_versions = Channel.empty()
                    ^^^^^^^
  ```

- Warning: `subworkflows/local/taxa_class.nf:16:20`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_mmseqs_db = Channel.empty()
                     ^^^^^^^
  ```

- Warning: `subworkflows/local/taxa_class.nf:17:5`: Variable was declared but not used

  ```nextflow
      ch_taxonomy_querydb = Channel.empty()
      ^^^^^^^^^^^^^^^^^^^
  ```

- Warning: `subworkflows/local/taxa_class.nf:17:27`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_taxonomy_querydb = Channel.empty()
                            ^^^^^^^
  ```

- Warning: `subworkflows/local/taxa_class.nf:18:33`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_taxonomy_querydb_taxdb = Channel.empty()
                                  ^^^^^^^
  ```

- Warning: `subworkflows/local/taxa_class.nf:19:23`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_taxonomy_tsv = Channel.empty()
                        ^^^^^^^
  ```

- Warning: `subworkflows/local/taxa_class.nf:26:28`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
              ch_mmseqs_db = Channel
                             ^^^^^^^
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

- Warning: `workflows/funcscan.nf:63:25`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_multiqc_config = Channel.fromPath("${projectDir}/assets/multiqc_config.yml", checkIfExists: true)
                          ^^^^^^^
  ```

- Warning: `workflows/funcscan.nf:64:56`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_multiqc_custom_config = params.multiqc_config ? Channel.fromPath(params.multiqc_config, checkIfExists: true) : Channel.empty()
                                                         ^^^^^^^
  ```

- Warning: `workflows/funcscan.nf:64:119`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_multiqc_custom_config = params.multiqc_config ? Channel.fromPath(params.multiqc_config, checkIfExists: true) : Channel.empty()
                                                                                                                        ^^^^^^^
  ```

- Warning: `workflows/funcscan.nf:65:45`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_multiqc_logo = params.multiqc_logo ? Channel.fromPath(params.multiqc_logo, checkIfExists: true) : Channel.empty()
                                              ^^^^^^^
  ```

- Warning: `workflows/funcscan.nf:65:106`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_multiqc_logo = params.multiqc_logo ? Channel.fromPath(params.multiqc_logo, checkIfExists: true) : Channel.empty()
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
          ch_mmseqs_db = Channel.empty()
          ^^^^^^^^^^^^
  ```

- Warning: `workflows/funcscan.nf:173:24`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
          ch_mmseqs_db = Channel.empty()
                         ^^^^^^^
  ```

- Warning: `workflows/funcscan.nf:174:9`: Variable was declared but not used

  ```nextflow
          ch_taxonomy_querydb = Channel.empty()
          ^^^^^^^^^^^^^^^^^^^
  ```

- Warning: `workflows/funcscan.nf:174:31`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
          ch_taxonomy_querydb = Channel.empty()
                                ^^^^^^^
  ```

- Warning: `workflows/funcscan.nf:175:9`: Variable was declared but not used

  ```nextflow
          ch_taxonomy_querydb_taxdb = Channel.empty()
          ^^^^^^^^^^^^^^^^^^^^^^^^^
  ```

- Warning: `workflows/funcscan.nf:175:37`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
          ch_taxonomy_querydb_taxdb = Channel.empty()
                                      ^^^^^^^
  ```

- Warning: `workflows/funcscan.nf:176:27`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
          ch_taxonomy_tsv = Channel.empty()
                            ^^^^^^^
  ```

- Warning: `workflows/funcscan.nf:363:26`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      def topic_versions = Channel.topic("versions")
                           ^^^^^^^
  ```

- Warning: `workflows/funcscan.nf:423:88`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          ch_multiqc_files = ch_multiqc_files.mix(ANNOTATION.out.multiqc_files.collect { it[1] })
                                                                                         ^^
  ```
