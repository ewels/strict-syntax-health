# Nextflow lint results

- Generated: 2026-01-21T13:35:35.511719+00:00
- Nextflow version: 25.12.0-edge
- Summary: 15 warnings

## :warning: Warnings

- Warning: `subworkflows/nf-core/fasta_hmmsearch_rank_fastas/main.nf:13:19`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_versions = Channel.empty()
                    ^^^^^^^^^^
  ```

- Warning: `subworkflows/nf-core/fasta_hmmsearch_rank_fastas/main.nf:17:18`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          .map { [ it[0], it[1], it[2], false, true, false ] }
                   ^^^^^^^^^^
  ```

- Warning: `subworkflows/nf-core/fasta_hmmsearch_rank_fastas/main.nf:17:25`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          .map { [ it[0], it[1], it[2], false, true, false ] }
                          ^^^^^^^^^^
  ```

- Warning: `subworkflows/nf-core/fasta_hmmsearch_rank_fastas/main.nf:17:32`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          .map { [ it[0], it[1], it[2], false, true, false ] }
                                 ^^^^^^^^^^
  ```

- Warning: `subworkflows/nf-core/fasta_hmmsearch_rank_fastas/main.nf:24:20`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          .collect { it[1] }
                     ^^^^^^^
  ```

- Warning: `subworkflows/nf-core/fasta_hmmsearch_rank_fastas/main.nf:25:34`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          .map { [ [ id: 'rank' ], it ] }
                                   ^^^^^^
  ```

- Warning: `subworkflows/nf-core/fasta_hmmsearch_rank_fastas/main.nf:32:16`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          .map { it[1] }
                 ^^^^^^^
  ```

- Warning: `subworkflows/nf-core/fasta_hmmsearch_rank_fastas/main.nf:34:19`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          .filter { it.rank == '1' }
                    ^^^^^^^^^^
  ```

- Warning: `subworkflows/nf-core/fasta_hmmsearch_rank_fastas/main.nf:35:29`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          .collectFile { [ "${it.profile}.txt", "${it.accno}\n" ] }
                              ^^^^^^^^^^
  ```

- Warning: `subworkflows/nf-core/fasta_hmmsearch_rank_fastas/main.nf:35:50`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          .collectFile { [ "${it.profile}.txt", "${it.accno}\n" ] }
                                                   ^^^^^^^^^^
  ```

- Warning: `subworkflows/nf-core/fasta_hmmsearch_rank_fastas/main.nf:36:24`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          .map { [ [ id: it.baseName ], it ] }
                         ^^^^^^^^^^
  ```

- Warning: `subworkflows/nf-core/fasta_hmmsearch_rank_fastas/main.nf:36:39`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          .map { [ [ id: it.baseName ], it ] }
                                        ^^^^^^
  ```

- Warning: `subworkflows/nf-core/fasta_hmmsearch_rank_fastas/main.nf:42:18`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          .map { [ it[0], it[2] ] }
                   ^^^^^^^^^^
  ```

- Warning: `subworkflows/nf-core/fasta_hmmsearch_rank_fastas/main.nf:42:25`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          .map { [ it[0], it[2] ] }
                          ^^^^^^^^^
  ```

- Warning: `subworkflows/nf-core/fasta_hmmsearch_rank_fastas/main.nf:46:60`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
      SEQTK_SUBSEQ ( ch_subseq_fasta, ch_subseq_filter.map { it[1] } )
                                                             ^^^^^^^^^
  ```
