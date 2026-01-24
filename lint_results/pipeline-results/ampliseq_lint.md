# Nextflow lint results

- Generated: 2026-01-24T00:17:22.102554517Z
- Nextflow version: 25.12.0-edge
- Summary: 66 warnings

## :warning: Warnings

- Warning: `modules/nf-core/kraken2/kraken2/main.nf:59:9`: Variable was declared but not used

  ```nextflow
      def args = task.ext.args ?: ''
          ^^^^
  ```

- Warning: `modules/nf-core/kraken2/kraken2/main.nf:61:9`: Variable was declared but not used

  ```nextflow
      def paired       = meta.single_end ? "" : "--paired"
          ^^^^^^
  ```

- Warning: `modules/nf-core/kraken2/kraken2/main.nf:64:9`: Variable was declared but not used

  ```nextflow
      def readclassification_option = save_reads_assignment ? "--output ${prefix}.kraken2.classifiedreads.txt" : "--output /dev/null"
          ^^^^^^^^^^^^^^^^^^^^^^^^^
  ```

- Warning: `modules/nf-core/kraken2/kraken2/main.nf:65:9`: Variable was declared but not used

  ```nextflow
      def compress_reads_command = save_output_fastqs ? "pigz -p $task.cpus *.fastq" : ""
          ^^^^^^^^^^^^^^^^^^^^^^
  ```

- Warning: `modules/nf-core/pigz/uncompress/main.nf:39:9`: Variable was declared but not used

  ```nextflow
      def args = task.ext.args ?: ''
          ^^^^
  ```

- Warning: `modules/nf-core/vsearch/cluster/main.nf:78:9`: Variable was declared but not used

  ```nextflow
      def args = task.ext.args ?: ''
          ^^^^
  ```

- Warning: `subworkflows/nf-core/fasta_newick_epang_gappa/main.nf:22:19`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_versions = Channel.empty()
                    ^^^^^^^
  ```

- Warning: `subworkflows/nf-core/fasta_newick_epang_gappa/main.nf:25:41`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
      ch_hmmer_data = ch_pp_data.filter { it.data.alignmethod == 'hmmer' }
                                          ^^
  ```

- Warning: `subworkflows/nf-core/fasta_newick_epang_gappa/main.nf:26:41`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
      ch_mafft_data = ch_pp_data.filter { it.data.alignmethod == 'mafft' }
                                          ^^
  ```

- Warning: `subworkflows/nf-core/fasta_newick_epang_gappa/main.nf:31:25`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
              .filter { ! it.data.hmmfile }
                          ^^
  ```

- Warning: `subworkflows/nf-core/fasta_newick_epang_gappa/main.nf:32:22`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
              .map { [ it.meta, it.data.refseqfile ] },
                       ^^
  ```

- Warning: `subworkflows/nf-core/fasta_newick_epang_gappa/main.nf:32:31`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
              .map { [ it.meta, it.data.refseqfile ] },
                                ^^
  ```

- Warning: `subworkflows/nf-core/fasta_newick_epang_gappa/main.nf:36:14`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_hmm = Channel.empty()
               ^^^^^^^
  ```

- Warning: `subworkflows/nf-core/fasta_newick_epang_gappa/main.nf:37:45`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          .mix(HMMER_HMMBUILD.out.hmm.map { [ it[0], it[1] ] })
                                              ^^
  ```

- Warning: `subworkflows/nf-core/fasta_newick_epang_gappa/main.nf:37:52`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          .mix(HMMER_HMMBUILD.out.hmm.map { [ it[0], it[1] ] })
                                                     ^^
  ```

- Warning: `subworkflows/nf-core/fasta_newick_epang_gappa/main.nf:40:27`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
                  .filter { it.data.hmmfile }
                            ^^
  ```

- Warning: `subworkflows/nf-core/fasta_newick_epang_gappa/main.nf:41:26`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
                  .map { [ it.meta, it.data.hmmfile ] }
                           ^^
  ```

- Warning: `subworkflows/nf-core/fasta_newick_epang_gappa/main.nf:41:35`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
                  .map { [ it.meta, it.data.hmmfile ] }
                                    ^^
  ```

- Warning: `subworkflows/nf-core/fasta_newick_epang_gappa/main.nf:49:25`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
              .filter { ! it.data.hmmfile }
                          ^^
  ```

- Warning: `subworkflows/nf-core/fasta_newick_epang_gappa/main.nf:50:22`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
              .map { [ it.meta, it.data.refseqfile ] }
                       ^^
  ```

- Warning: `subworkflows/nf-core/fasta_newick_epang_gappa/main.nf:50:31`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
              .map { [ it.meta, it.data.refseqfile ] }
                                ^^
  ```

- Warning: `subworkflows/nf-core/fasta_newick_epang_gappa/main.nf:52:26`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_hmmer_unaligned = Channel.empty()
                           ^^^^^^^
  ```

- Warning: `subworkflows/nf-core/fasta_newick_epang_gappa/main.nf:53:57`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          .mix(HMMER_UNALIGNREF.out.seqreformated.map { [ it[0], it[1] ] })
                                                          ^^
  ```

- Warning: `subworkflows/nf-core/fasta_newick_epang_gappa/main.nf:53:64`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          .mix(HMMER_UNALIGNREF.out.seqreformated.map { [ it[0], it[1] ] })
                                                                 ^^
  ```

- Warning: `subworkflows/nf-core/fasta_newick_epang_gappa/main.nf:56:27`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
                  .filter { it.data.hmmfile }
                            ^^
  ```

- Warning: `subworkflows/nf-core/fasta_newick_epang_gappa/main.nf:57:26`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
                  .map { [ it.meta, it.data.refseqfile ] }
                           ^^
  ```

- Warning: `subworkflows/nf-core/fasta_newick_epang_gappa/main.nf:57:35`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
                  .map { [ it.meta, it.data.refseqfile ] }
                                    ^^
  ```

- Warning: `subworkflows/nf-core/fasta_newick_epang_gappa/main.nf:65:41`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          .groupTuple(size: 2, sort: { a, b -> a =~ /\.hmm/ ? 1 : -1 })
                                          ^
  ```

- Warning: `subworkflows/nf-core/fasta_newick_epang_gappa/main.nf:68:35`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          ch_hmmer_alignref.map { [ it[0], it[1][0] ] },
                                    ^^
  ```

- Warning: `subworkflows/nf-core/fasta_newick_epang_gappa/main.nf:68:42`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          ch_hmmer_alignref.map { [ it[0], it[1][0] ] },
                                           ^^
  ```

- Warning: `subworkflows/nf-core/fasta_newick_epang_gappa/main.nf:69:33`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          ch_hmmer_alignref.map { it[1][1] }
                                  ^^
  ```

- Warning: `subworkflows/nf-core/fasta_newick_epang_gappa/main.nf:73:27`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_hmmer_alignquery = Channel.empty()
                            ^^^^^^^
  ```

- Warning: `subworkflows/nf-core/fasta_newick_epang_gappa/main.nf:74:36`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          .mix(ch_hmmer_data.map { [ it.meta, it.data.queryseqfile ] })
                                     ^^
  ```

- Warning: `subworkflows/nf-core/fasta_newick_epang_gappa/main.nf:74:45`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          .mix(ch_hmmer_data.map { [ it.meta, it.data.queryseqfile ] })
                                              ^^
  ```

- Warning: `subworkflows/nf-core/fasta_newick_epang_gappa/main.nf:76:41`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          .groupTuple(size: 2, sort: { a, b -> a =~ /\.hmm/ ? 1 : -1 })
                                          ^
  ```

- Warning: `subworkflows/nf-core/fasta_newick_epang_gappa/main.nf:79:37`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          ch_hmmer_alignquery.map { [ it[0], it[1][0] ] },
                                      ^^
  ```

- Warning: `subworkflows/nf-core/fasta_newick_epang_gappa/main.nf:79:44`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          ch_hmmer_alignquery.map { [ it[0], it[1][0] ] },
                                             ^^
  ```

- Warning: `subworkflows/nf-core/fasta_newick_epang_gappa/main.nf:80:35`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          ch_hmmer_alignquery.map { it[1][1] }
                                    ^^
  ```

- Warning: `subworkflows/nf-core/fasta_newick_epang_gappa/main.nf:85:57`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
      HMMER_MASKREF ( HMMER_HMMALIGNREF.out.sthlm.map { [ it[0], it[1], [], [], [], [], [], [] ] }, [] )
                                                          ^^
  ```

- Warning: `subworkflows/nf-core/fasta_newick_epang_gappa/main.nf:85:64`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
      HMMER_MASKREF ( HMMER_HMMALIGNREF.out.sthlm.map { [ it[0], it[1], [], [], [], [], [], [] ] }, [] )
                                                                 ^^
  ```

- Warning: `subworkflows/nf-core/fasta_newick_epang_gappa/main.nf:88:61`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
      HMMER_MASKQUERY ( HMMER_HMMALIGNQUERY.out.sthlm.map { [ it[0], it[1], [], [], [], [], [], [] ] }, [] )
                                                              ^^
  ```

- Warning: `subworkflows/nf-core/fasta_newick_epang_gappa/main.nf:88:68`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
      HMMER_MASKQUERY ( HMMER_HMMALIGNQUERY.out.sthlm.map { [ it[0], it[1], [], [], [], [], [], [] ] }, [] )
                                                                     ^^
  ```

- Warning: `subworkflows/nf-core/fasta_newick_epang_gappa/main.nf:100:31`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          ch_mafft_data.map { [ it.meta, it.data.refseqfile ] },
                                ^^
  ```

- Warning: `subworkflows/nf-core/fasta_newick_epang_gappa/main.nf:100:40`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          ch_mafft_data.map { [ it.meta, it.data.refseqfile ] },
                                         ^^
  ```

- Warning: `subworkflows/nf-core/fasta_newick_epang_gappa/main.nf:101:31`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          ch_mafft_data.map { [ it.data.queryseqfile ] }
                                ^^
  ```

- Warning: `subworkflows/nf-core/fasta_newick_epang_gappa/main.nf:107:31`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          ch_mafft_data.map { [ it.meta, it.data.refseqfile ] }
                                ^^
  ```

- Warning: `subworkflows/nf-core/fasta_newick_epang_gappa/main.nf:107:40`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          ch_mafft_data.map { [ it.meta, it.data.refseqfile ] }
                                         ^^
  ```

- Warning: `subworkflows/nf-core/fasta_newick_epang_gappa/main.nf:113:41`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
      ch_epang_query = ch_pp_data.map { [ it.meta, it.data.model, it.data.refphylogeny ] }
                                          ^^
  ```

- Warning: `subworkflows/nf-core/fasta_newick_epang_gappa/main.nf:113:50`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
      ch_epang_query = ch_pp_data.map { [ it.meta, it.data.model, it.data.refphylogeny ] }
                                                   ^^
  ```

- Warning: `subworkflows/nf-core/fasta_newick_epang_gappa/main.nf:113:65`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
      ch_epang_query = ch_pp_data.map { [ it.meta, it.data.model, it.data.refphylogeny ] }
                                                                  ^^
  ```

- Warning: `subworkflows/nf-core/fasta_newick_epang_gappa/main.nf:117:32`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
              ch_pp_data.map { [ it.meta, it.data.model, it.data.refphylogeny ] }
                                 ^^
  ```

- Warning: `subworkflows/nf-core/fasta_newick_epang_gappa/main.nf:117:41`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
              ch_pp_data.map { [ it.meta, it.data.model, it.data.refphylogeny ] }
                                          ^^
  ```

- Warning: `subworkflows/nf-core/fasta_newick_epang_gappa/main.nf:117:56`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
              ch_pp_data.map { [ it.meta, it.data.model, it.data.refphylogeny ] }
                                                         ^^
  ```

- Warning: `subworkflows/nf-core/fasta_newick_epang_gappa/main.nf:118:53`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
                  .join(EPANG_SPLIT.out.query.map { [ it[0], it[1] ] } )
                                                      ^^
  ```

- Warning: `subworkflows/nf-core/fasta_newick_epang_gappa/main.nf:118:60`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
                  .join(EPANG_SPLIT.out.query.map { [ it[0], it[1] ] } )
                                                             ^^
  ```

- Warning: `subworkflows/nf-core/fasta_newick_epang_gappa/main.nf:119:57`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
                  .join(EPANG_SPLIT.out.reference.map { [ it[0], it[1] ] } )
                                                          ^^
  ```

- Warning: `subworkflows/nf-core/fasta_newick_epang_gappa/main.nf:119:64`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
                  .join(EPANG_SPLIT.out.reference.map { [ it[0], it[1] ] } )
                                                                 ^^
  ```

- Warning: `subworkflows/nf-core/fasta_newick_epang_gappa/main.nf:121:23`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          .map { [ [ id:it[0].id, model:it[1] ], it[3], it[4], it[2] ] }
                        ^^
  ```

- Warning: `subworkflows/nf-core/fasta_newick_epang_gappa/main.nf:121:39`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          .map { [ [ id:it[0].id, model:it[1] ], it[3], it[4], it[2] ] }
                                        ^^
  ```

- Warning: `subworkflows/nf-core/fasta_newick_epang_gappa/main.nf:121:48`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          .map { [ [ id:it[0].id, model:it[1] ], it[3], it[4], it[2] ] }
                                                 ^^
  ```

- Warning: `subworkflows/nf-core/fasta_newick_epang_gappa/main.nf:121:55`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          .map { [ [ id:it[0].id, model:it[1] ], it[3], it[4], it[2] ] }
                                                        ^^
  ```

- Warning: `subworkflows/nf-core/fasta_newick_epang_gappa/main.nf:121:62`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          .map { [ [ id:it[0].id, model:it[1] ], it[3], it[4], it[2] ] }
                                                               ^^
  ```

- Warning: `subworkflows/nf-core/fasta_newick_epang_gappa/main.nf:136:27`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
              .map { [ [ id:it[0].id ], it[1] ] }
                            ^^
  ```

- Warning: `subworkflows/nf-core/fasta_newick_epang_gappa/main.nf:136:39`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
              .map { [ [ id:it[0].id ], it[1] ] }
                                        ^^
  ```

- Warning: `subworkflows/nf-core/fasta_newick_epang_gappa/main.nf:137:39`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
              .join( ch_pp_data.map { [ it.meta, it.data.taxonomy ] } )
                                        ^^
  ```

- Warning: `subworkflows/nf-core/fasta_newick_epang_gappa/main.nf:137:48`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
              .join( ch_pp_data.map { [ it.meta, it.data.taxonomy ] } )
                                                 ^^
  ```
