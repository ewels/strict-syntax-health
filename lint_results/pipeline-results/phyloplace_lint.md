# Nextflow lint results

- Generated: 2026-01-16T06:37:05.991619748Z
- Nextflow version: 25.12.0-edge
- Summary: 17 errors, 106 warnings

## :x: Errors

- Error: `modules/local/hmmer/hmmextract/main.nf:25:30`: `keyfile` is not defined

  ```nextflow
      def outfile = ! key && ! keyfile ? '' : "> ${prefix}.hmm"
                               ^^^^^^^
  ```

- Error: `modules/nf-core/mafft/align/main.nf:29:9`: `add` is already declared

  ```nextflow
      def add          = add             ? "--add <(unpigz -cdf ${add})"                   : ''
          ^^^
  ```

- Error: `modules/nf-core/mafft/align/main.nf:30:9`: `addfragments` is already declared

  ```nextflow
      def addfragments = addfragments    ? "--addfragments <(unpigz -cdf ${addfragments})" : ''
          ^^^^^^^^^^^^
  ```

- Error: `modules/nf-core/mafft/align/main.nf:31:9`: `addfull` is already declared

  ```nextflow
      def addfull      = addfull         ? "--addfull <(unpigz -cdf ${addfull})"           : ''
          ^^^^^^^
  ```

- Error: `modules/nf-core/mafft/align/main.nf:32:9`: `addprofile` is already declared

  ```nextflow
      def addprofile   = addprofile      ? "--addprofile <(unpigz -cdf ${addprofile})"     : ''
          ^^^^^^^^^^
  ```

- Error: `modules/nf-core/mafft/align/main.nf:33:9`: `addlong` is already declared

  ```nextflow
      def addlong      = addlong         ? "--addlong <(unpigz -cdf ${addlong})"           : ''
          ^^^^^^^
  ```

- Error: `modules/nf-core/mafft/align/main.nf:59:9`: `add` is already declared

  ```nextflow
      def add          = add             ? "--add ${add}"                   : ''
          ^^^
  ```

- Error: `modules/nf-core/mafft/align/main.nf:60:9`: `addfragments` is already declared

  ```nextflow
      def addfragments = addfragments    ? "--addfragments ${addfragments}" : ''
          ^^^^^^^^^^^^
  ```

- Error: `modules/nf-core/mafft/align/main.nf:61:9`: `addfull` is already declared

  ```nextflow
      def addfull      = addfull         ? "--addfull ${addfull}"           : ''
          ^^^^^^^
  ```

- Error: `modules/nf-core/mafft/align/main.nf:62:9`: `addprofile` is already declared

  ```nextflow
      def addprofile   = addprofile      ? "--addprofile ${addprofile}"     : ''
          ^^^^^^^^^^
  ```

- Error: `modules/nf-core/mafft/align/main.nf:63:9`: `addlong` is already declared

  ```nextflow
      def addlong      = addlong         ? "--addlong ${addlong}"           : ''
          ^^^^^^^
  ```

- Error: `nextflow.config:289:34`: `manifest` is not defined

  ```nextflow
  \033[0;35m  nf-core/phyloplace ${manifest.version}\033[0m
                                   ^^^^^^^^
  ```

- Error: `nextflow.config:292:26`: `manifest` is not defined

  ```nextflow
          afterText = """${manifest.doi ? "\n* The pipeline\n" : ""}${manifest.doi.tokenize(",").collect { "    https://doi.org/${it.trim().replace('https://doi.org/','')}"}.join("\n")}${manifest.doi ? "\n" : ""}
                           ^^^^^^^^
  ```

- Error: `nextflow.config:292:69`: `manifest` is not defined

  ```nextflow
          afterText = """${manifest.doi ? "\n* The pipeline\n" : ""}${manifest.doi.tokenize(",").collect { "    https://doi.org/${it.trim().replace('https://doi.org/','')}"}.join("\n")}${manifest.doi ? "\n" : ""}
                                                                      ^^^^^^^^
  ```

- Error: `nextflow.config:292:186`: `manifest` is not defined

  ```nextflow
          afterText = """${manifest.doi ? "\n* The pipeline\n" : ""}${manifest.doi.tokenize(",").collect { "    https://doi.org/${it.trim().replace('https://doi.org/','')}"}.join("\n")}${manifest.doi ? "\n" : ""}
                                                                                                                                                                                           ^^^^^^^^
  ```

- Error: `nextflow.config:301:22`: `validation` is not defined

  ```nextflow
          beforeText = validation.help.beforeText
                       ^^^^^^^^^^
  ```

- Error: `nextflow.config:302:21`: `validation` is not defined

  ```nextflow
          afterText = validation.help.afterText
                      ^^^^^^^^^^
  ```

## :warning: Warnings

- Warning: `modules/local/hmmer/hmmextract/main.nf:50:9`: Variable was declared but not used

  ```nextflow
      def args = task.ext.args ?: ''
          ^^^^
  ```

- Warning: `modules/nf-core/clustalo/align/main.nf:60:9`: Variable was declared but not used

  ```nextflow
      def args = task.ext.args ?: ''
          ^^^^
  ```

- Warning: `modules/nf-core/epang/place/main.nf:56:9`: Variable was declared but not used

  ```nextflow
      def args       = task.ext.args   ?: ''
          ^^^^
  ```

- Warning: `modules/nf-core/epang/place/main.nf:58:9`: Variable was declared but not used

  ```nextflow
      def queryarg   = queryaln        ? "--query $queryaln"       : ""
          ^^^^^^^^
  ```

- Warning: `modules/nf-core/epang/place/main.nf:59:9`: Variable was declared but not used

  ```nextflow
      def refalnarg  = referencealn    ? "--ref-msa $referencealn" : ""
          ^^^^^^^^^
  ```

- Warning: `modules/nf-core/epang/place/main.nf:60:9`: Variable was declared but not used

  ```nextflow
      def reftreearg = referencetree   ? "--tree $referencetree"   : ""
          ^^^^^^^^^^
  ```

- Warning: `modules/nf-core/epang/place/main.nf:61:9`: Variable was declared but not used

  ```nextflow
      def bfastarg   = bfastfile       ? "--bfast $bfastfile"      : ""
          ^^^^^^^^
  ```

- Warning: `modules/nf-core/epang/place/main.nf:62:9`: Variable was declared but not used

  ```nextflow
      def binaryarg  = binaryfile      ? "--binary $binaryfile"    : ""
          ^^^^^^^^^
  ```

- Warning: `modules/nf-core/gappa/examineassign/main.nf:44:9`: Variable was declared but not used

  ```nextflow
      def args = task.ext.args ?: ''
          ^^^^
  ```

- Warning: `modules/nf-core/gappa/examineheattree/main.nf:47:9`: Variable was declared but not used

  ```nextflow
      def args = task.ext.args ?: ''
          ^^^^
  ```

- Warning: `modules/nf-core/hmmer/hmmrank/main.nf:21:9`: Variable was declared but not used

  ```nextflow
      def args   = task.ext.args ?: ''
          ^^^^
  ```

- Warning: `modules/nf-core/hmmer/hmmrank/main.nf:59:9`: Variable was declared but not used

  ```nextflow
      def args = task.ext.args ?: ''
          ^^^^
  ```

- Warning: `modules/nf-core/mafft/align/main.nf:57:9`: Variable was declared but not used

  ```nextflow
      def args         = task.ext.args   ?: ''
          ^^^^
  ```

- Warning: `modules/nf-core/mafft/align/main.nf:59:9`: Variable was declared but not used

  ```nextflow
      def add          = add             ? "--add ${add}"                   : ''
          ^^^
  ```

- Warning: `modules/nf-core/mafft/align/main.nf:60:9`: Variable was declared but not used

  ```nextflow
      def addfragments = addfragments    ? "--addfragments ${addfragments}" : ''
          ^^^^^^^^^^^^
  ```

- Warning: `modules/nf-core/mafft/align/main.nf:61:9`: Variable was declared but not used

  ```nextflow
      def addfull      = addfull         ? "--addfull ${addfull}"           : ''
          ^^^^^^^
  ```

- Warning: `modules/nf-core/mafft/align/main.nf:62:9`: Variable was declared but not used

  ```nextflow
      def addprofile   = addprofile      ? "--addprofile ${addprofile}"     : ''
          ^^^^^^^^^^
  ```

- Warning: `modules/nf-core/mafft/align/main.nf:63:9`: Variable was declared but not used

  ```nextflow
      def addlong      = addlong         ? "--addlong ${addlong}"           : ''
          ^^^^^^^
  ```

- Warning: `nextflow.config:292:129`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          afterText = """${manifest.doi ? "\n* The pipeline\n" : ""}${manifest.doi.tokenize(",").collect { "    https://doi.org/${it.trim().replace('https://doi.org/','')}"}.join("\n")}${manifest.doi ? "\n" : ""}
                                                                                                                                  ^^
  ```

- Warning: `subworkflows/local/utils_nfcore_phyloplace_pipeline/main.nf:31:5`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
      monochrome_logs   // boolean: Do not use coloured log outputs
      ^^^^^^^^^^^^^^^
  ```

- Warning: `subworkflows/local/utils_nfcore_phyloplace_pipeline/main.nf:34:5`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
      phyloplace_input  //  string: Path to phyloplace input samplesheet
      ^^^^^^^^^^^^^^^^
  ```

- Warning: `subworkflows/local/utils_nfcore_phyloplace_pipeline/main.nf:35:5`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
      phylosearch_input //  string: Path to phylosearch input samplesheet
      ^^^^^^^^^^^^^^^^^
  ```

- Warning: `subworkflows/local/utils_nfcore_phyloplace_pipeline/main.nf:39:19`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_versions = Channel.empty()
                    ^^^^^^^
  ```

- Warning: `subworkflows/local/utils_nfcore_phyloplace_pipeline/main.nf:77:27`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_phylosearch_data = Channel.empty()
                            ^^^^^^^
  ```

- Warning: `subworkflows/local/utils_nfcore_phyloplace_pipeline/main.nf:78:27`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_sequence_fasta   = Channel.empty()
                            ^^^^^^^
  ```

- Warning: `subworkflows/local/utils_nfcore_phyloplace_pipeline/main.nf:79:27`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_phyloplace_data  = Channel.empty()
                            ^^^^^^^
  ```

- Warning: `subworkflows/local/utils_nfcore_phyloplace_pipeline/main.nf:82:31`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
          ch_phylosearch_data = Channel.fromPath(params.phylosearch_input)
                                ^^^^^^^
  ```

- Warning: `subworkflows/local/utils_nfcore_phyloplace_pipeline/main.nf:87:29`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
                          id: it.target,
                              ^^
  ```

- Warning: `subworkflows/local/utils_nfcore_phyloplace_pipeline/main.nf:88:39`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
                          min_bitscore: it.min_bitscore
                                        ^^
  ```

- Warning: `subworkflows/local/utils_nfcore_phyloplace_pipeline/main.nf:91:41`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
                          alignmethod:    it.alignmethod  ? it.alignmethod                             : 'hmmer',
                                          ^^
  ```

- Warning: `subworkflows/local/utils_nfcore_phyloplace_pipeline/main.nf:91:59`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
                          alignmethod:    it.alignmethod  ? it.alignmethod                             : 'hmmer',
                                                            ^^
  ```

- Warning: `subworkflows/local/utils_nfcore_phyloplace_pipeline/main.nf:92:46`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
                          hmm:            file(it.hmm,  checkIfExists: true),
                                               ^^
  ```

- Warning: `subworkflows/local/utils_nfcore_phyloplace_pipeline/main.nf:93:41`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
                          extract_hmm:    it.extract_hmm,
                                          ^^
  ```

- Warning: `subworkflows/local/utils_nfcore_phyloplace_pipeline/main.nf:94:41`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
                          refseqfile:     it.refseqfile   ? file(it.refseqfile,   checkIfExists: true) : [],
                                          ^^
  ```

- Warning: `subworkflows/local/utils_nfcore_phyloplace_pipeline/main.nf:94:64`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
                          refseqfile:     it.refseqfile   ? file(it.refseqfile,   checkIfExists: true) : [],
                                                                 ^^
  ```

- Warning: `subworkflows/local/utils_nfcore_phyloplace_pipeline/main.nf:95:41`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
                          refphylogeny:   it.refphylogeny ? file(it.refphylogeny, checkIfExists: true) : [],
                                          ^^
  ```

- Warning: `subworkflows/local/utils_nfcore_phyloplace_pipeline/main.nf:95:64`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
                          refphylogeny:   it.refphylogeny ? file(it.refphylogeny, checkIfExists: true) : [],
                                                                 ^^
  ```

- Warning: `subworkflows/local/utils_nfcore_phyloplace_pipeline/main.nf:96:41`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
                          model:          it.model,
                                          ^^
  ```

- Warning: `subworkflows/local/utils_nfcore_phyloplace_pipeline/main.nf:97:41`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
                          taxonomy:       it.taxonomy     ? file(it.taxonomy,     checkIfExists: true) : []
                                          ^^
  ```

- Warning: `subworkflows/local/utils_nfcore_phyloplace_pipeline/main.nf:97:64`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
                          taxonomy:       it.taxonomy     ? file(it.taxonomy,     checkIfExists: true) : []
                                                                 ^^
  ```

- Warning: `subworkflows/local/utils_nfcore_phyloplace_pipeline/main.nf:101:9`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
          Channel.fromPath(params.search_fasta)
          ^^^^^^^
  ```

- Warning: `subworkflows/local/utils_nfcore_phyloplace_pipeline/main.nf:104:30`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
          ch_phyloplace_data = Channel.fromPath(params.phyloplace_input)
                               ^^^^^^^
  ```

- Warning: `subworkflows/local/utils_nfcore_phyloplace_pipeline/main.nf:108:33`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
                      meta: [ id: it.sample ],
                                  ^^
  ```

- Warning: `subworkflows/local/utils_nfcore_phyloplace_pipeline/main.nf:110:39`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
                          alignmethod:  it.alignmethod ? it.alignmethod    : 'hmmer',
                                        ^^
  ```

- Warning: `subworkflows/local/utils_nfcore_phyloplace_pipeline/main.nf:110:56`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
                          alignmethod:  it.alignmethod ? it.alignmethod    : 'hmmer',
                                                         ^^
  ```

- Warning: `subworkflows/local/utils_nfcore_phyloplace_pipeline/main.nf:111:44`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
                          queryseqfile: file(it.queryseqfile),
                                             ^^
  ```

- Warning: `subworkflows/local/utils_nfcore_phyloplace_pipeline/main.nf:112:44`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
                          refseqfile:   file(it.refseqfile),
                                             ^^
  ```

- Warning: `subworkflows/local/utils_nfcore_phyloplace_pipeline/main.nf:113:39`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
                          hmmfile:      it.hmmfile     ? file(it.hmmfile,  checkIfExists: true) : [],
                                        ^^
  ```

- Warning: `subworkflows/local/utils_nfcore_phyloplace_pipeline/main.nf:113:61`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
                          hmmfile:      it.hmmfile     ? file(it.hmmfile,  checkIfExists: true) : [],
                                                              ^^
  ```

- Warning: `subworkflows/local/utils_nfcore_phyloplace_pipeline/main.nf:114:44`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
                          refphylogeny: file(it.refphylogeny),
                                             ^^
  ```

- Warning: `subworkflows/local/utils_nfcore_phyloplace_pipeline/main.nf:115:39`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
                          model:        it.model,
                                        ^^
  ```

- Warning: `subworkflows/local/utils_nfcore_phyloplace_pipeline/main.nf:116:39`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
                          taxonomy:     it.taxonomy    ? file(it.taxonomy, checkIfExists: true) : []
                                        ^^
  ```

- Warning: `subworkflows/local/utils_nfcore_phyloplace_pipeline/main.nf:116:61`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
                          taxonomy:     it.taxonomy    ? file(it.taxonomy, checkIfExists: true) : []
                                                              ^^
  ```

- Warning: `subworkflows/local/utils_nfcore_phyloplace_pipeline/main.nf:121:9`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
          Channel.of([
          ^^^^^^^
  ```

- Warning: `subworkflows/nf-core/fasta_hmmsearch_rank_fastas/main.nf:13:19`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_versions = Channel.empty()
                    ^^^^^^^
  ```

- Warning: `subworkflows/nf-core/fasta_hmmsearch_rank_fastas/main.nf:17:18`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          .map { [ it[0], it[1], it[2], false, true, false ] }
                   ^^
  ```

- Warning: `subworkflows/nf-core/fasta_hmmsearch_rank_fastas/main.nf:17:25`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          .map { [ it[0], it[1], it[2], false, true, false ] }
                          ^^
  ```

- Warning: `subworkflows/nf-core/fasta_hmmsearch_rank_fastas/main.nf:17:32`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          .map { [ it[0], it[1], it[2], false, true, false ] }
                                 ^^
  ```

- Warning: `subworkflows/nf-core/fasta_hmmsearch_rank_fastas/main.nf:24:20`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          .collect { it[1] }
                     ^^
  ```

- Warning: `subworkflows/nf-core/fasta_hmmsearch_rank_fastas/main.nf:25:34`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          .map { [ [ id: 'rank' ], it ] }
                                   ^^
  ```

- Warning: `subworkflows/nf-core/fasta_hmmsearch_rank_fastas/main.nf:32:16`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          .map { it[1] }
                 ^^
  ```

- Warning: `subworkflows/nf-core/fasta_hmmsearch_rank_fastas/main.nf:34:19`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          .filter { it.rank == '1' }
                    ^^
  ```

- Warning: `subworkflows/nf-core/fasta_hmmsearch_rank_fastas/main.nf:35:29`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          .collectFile { [ "${it.profile}.txt", "${it.accno}\n" ] }
                              ^^
  ```

- Warning: `subworkflows/nf-core/fasta_hmmsearch_rank_fastas/main.nf:35:50`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          .collectFile { [ "${it.profile}.txt", "${it.accno}\n" ] }
                                                   ^^
  ```

- Warning: `subworkflows/nf-core/fasta_hmmsearch_rank_fastas/main.nf:36:24`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          .map { [ [ id: it.baseName ], it ] }
                         ^^
  ```

- Warning: `subworkflows/nf-core/fasta_hmmsearch_rank_fastas/main.nf:36:39`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          .map { [ [ id: it.baseName ], it ] }
                                        ^^
  ```

- Warning: `subworkflows/nf-core/fasta_hmmsearch_rank_fastas/main.nf:42:18`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          .map { [ it[0], it[2] ] }
                   ^^
  ```

- Warning: `subworkflows/nf-core/fasta_hmmsearch_rank_fastas/main.nf:42:25`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          .map { [ it[0], it[2] ] }
                          ^^
  ```

- Warning: `subworkflows/nf-core/fasta_hmmsearch_rank_fastas/main.nf:46:60`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
      SEQTK_SUBSEQ ( ch_subseq_fasta, ch_subseq_filter.map { it[1] } )
                                                             ^^
  ```

- Warning: `subworkflows/nf-core/fasta_newick_epang_gappa/main.nf:24:19`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_versions = Channel.empty()
                    ^^^^^^^
  ```

- Warning: `subworkflows/nf-core/fasta_newick_epang_gappa/main.nf:39:14`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_hmm = Channel.empty()
               ^^^^^^^
  ```

- Warning: `subworkflows/nf-core/fasta_newick_epang_gappa/main.nf:55:26`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_hmmer_unaligned = Channel.empty()
                           ^^^^^^^
  ```

- Warning: `subworkflows/nf-core/fasta_newick_epang_gappa/main.nf:68:41`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          .groupTuple(size: 2, sort: { a, b -> a =~ /\.hmm/ ? 1 : -1 })
                                          ^
  ```

- Warning: `subworkflows/nf-core/fasta_newick_epang_gappa/main.nf:76:27`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_hmmer_alignquery = Channel.empty()
                            ^^^^^^^
  ```

- Warning: `subworkflows/nf-core/fasta_newick_epang_gappa/main.nf:79:41`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          .groupTuple(size: 2, sort: { a, b -> a =~ /\.hmm/ ? 1 : -1 })
                                          ^
  ```

- Warning: `subworkflows/nf-core/utils_nfcore_pipeline/main.nf:101:98`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      return ch_versions.unique().map { version -> processVersionsFromYAML(version) }.unique().mix(Channel.of(workflowVersionToYAML()))
                                                                                                   ^^^^^^^
  ```

- Warning: `workflows/phyloplace.nf:31:19`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_versions = Channel.empty()
                    ^^^^^^^
  ```

- Warning: `workflows/phyloplace.nf:32:24`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_multiqc_files = Channel.empty()
                         ^^^^^^^
  ```

- Warning: `workflows/phyloplace.nf:38:19`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          .filter { it.data.extract_hmm }
                    ^^
  ```

- Warning: `workflows/phyloplace.nf:39:18`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          .map { [ it.meta, it.data.hmm, it.data.extract_hmm ] }
                   ^^
  ```

- Warning: `workflows/phyloplace.nf:39:27`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          .map { [ it.meta, it.data.hmm, it.data.extract_hmm ] }
                            ^^
  ```

- Warning: `workflows/phyloplace.nf:39:40`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          .map { [ it.meta, it.data.hmm, it.data.extract_hmm ] }
                                         ^^
  ```

- Warning: `workflows/phyloplace.nf:49:29`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
                  .filter { ! it.data.extract_hmm }
                              ^^
  ```

- Warning: `workflows/phyloplace.nf:50:26`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
                  .map { [ it.meta, it.data.hmm ] }
                           ^^
  ```

- Warning: `workflows/phyloplace.nf:50:35`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
                  .map { [ it.meta, it.data.hmm ] }
                                    ^^
  ```

- Warning: `workflows/phyloplace.nf:60:27`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
                  .filter { it.data.alignmethod && it.data.refseqfile && it.data.refphylogeny }
                            ^^
  ```

- Warning: `workflows/phyloplace.nf:60:50`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
                  .filter { it.data.alignmethod && it.data.refseqfile && it.data.refphylogeny }
                                                   ^^
  ```

- Warning: `workflows/phyloplace.nf:60:72`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
                  .filter { it.data.alignmethod && it.data.refseqfile && it.data.refphylogeny }
                                                                         ^^
  ```

- Warning: `workflows/phyloplace.nf:61:32`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
                  .map { [ [ id: it.meta.id ], it ] }
                                 ^^
  ```

- Warning: `workflows/phyloplace.nf:61:46`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
                  .map { [ [ id: it.meta.id ], it ] }
                                               ^^
  ```

- Warning: `workflows/phyloplace.nf:64:19`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
              meta: it[2].meta,
                    ^^
  ```

- Warning: `workflows/phyloplace.nf:66:30`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
                  alignmethod: it[2].data.alignmethod,
                               ^^
  ```

- Warning: `workflows/phyloplace.nf:67:31`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
                  queryseqfile: it[1],
                                ^^
  ```

- Warning: `workflows/phyloplace.nf:68:29`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
                  refseqfile: it[2].data.refseqfile,
                              ^^
  ```

- Warning: `workflows/phyloplace.nf:69:31`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
                  refphylogeny: it[2].data.refphylogeny,
                                ^^
  ```

- Warning: `workflows/phyloplace.nf:70:24`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
                  model: it[2].data.model,
                         ^^
  ```

- Warning: `workflows/phyloplace.nf:71:27`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
                  taxonomy: it[2].data.taxonomy
                            ^^
  ```

- Warning: `workflows/phyloplace.nf:94:45`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_multiqc_config                     = Channel.fromPath("$projectDir/assets/multiqc_config.yml", checkIfExists: true)
                                              ^^^^^^^
  ```

- Warning: `workflows/phyloplace.nf:95:69`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_multiqc_custom_config              = params.multiqc_config ? Channel.fromPath(params.multiqc_config, checkIfExists: true) : Channel.empty()
                                                                      ^^^^^^^
  ```

- Warning: `workflows/phyloplace.nf:95:132`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_multiqc_custom_config              = params.multiqc_config ? Channel.fromPath(params.multiqc_config, checkIfExists: true) : Channel.empty()
                                                                                                                                     ^^^^^^^
  ```

- Warning: `workflows/phyloplace.nf:96:67`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_multiqc_logo                       = params.multiqc_logo ? Channel.fromPath(params.multiqc_logo, checkIfExists: true) : Channel.empty()
                                                                    ^^^^^^^
  ```

- Warning: `workflows/phyloplace.nf:96:128`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_multiqc_logo                       = params.multiqc_logo ? Channel.fromPath(params.multiqc_logo, checkIfExists: true) : Channel.empty()
                                                                                                                                 ^^^^^^^
  ```

- Warning: `workflows/phyloplace.nf:98:45`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_workflow_summary                   = Channel.value(paramsSummaryMultiqc(summary_params))
                                              ^^^^^^^
  ```

- Warning: `workflows/phyloplace.nf:100:45`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_methods_description                = Channel.value(methodsDescriptionText(ch_multiqc_custom_methods_description))
                                              ^^^^^^^
  ```

- Warning: `workflows/phyloplace.nf:107:27`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_workflow_summary = Channel.value(paramsSummaryMultiqc(summary_params))
                            ^^^^^^^
  ```

- Warning: `workflows/phyloplace.nf:113:45`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_methods_description                = Channel.value(
                                              ^^^^^^^
  ```
