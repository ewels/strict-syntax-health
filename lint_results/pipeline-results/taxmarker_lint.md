# Nextflow lint results

- Generated: 2026-09-10T00:21:58.690458109Z
- Nextflow version: 26.08.0-edge
- Summary: 9 warnings

## :warning: Warnings

- Warning: `subworkflows/local/ensure_aligned/main.nf:54:65`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
      CHECKALIGNED(ch_sequences.map { [ [ id: 'user-alignment' ], it ] })
                                                                  ^^
  ```

- Warning: `subworkflows/local/ensure_aligned/main.nf:75:37`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
              .map { [ [ id: 'hmm' ], it ] }
                                      ^^
  ```

- Warning: `subworkflows/local/raxtax_prefilter/main.nf:35:77`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
      def ch_meta_taxonomy   = ch_taxonomy.map  { [ [ id: 'user-alignment' ], it ] }
                                                                              ^^
  ```

- Warning: `subworkflows/local/raxtax_prefilter/main.nf:36:77`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
      def ch_alignment_fasta = ch_alignment.map { [ [ id: 'user-alignment' ], it ] }
                                                                              ^^
  ```

- Warning: `subworkflows/local/sativa/main.nf:63:5`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
      ch_ref_tree   // channel: [ val(meta), path(tree.nwk) ]
      ^^^^^^^^^^^
  ```

- Warning: `subworkflows/local/sativa/main.nf:66:5`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
      ch_ref_model  // channel: [ val(meta), path(model.txt) ]
      ^^^^^^^^^^^^
  ```

- Warning: `subworkflows/local/sativa/main.nf:74:76`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
      def ch_alignment_meta = ch_alignment.map { [ [ id: 'user-alignment' ], it ] }
                                                                             ^^
  ```

- Warning: `subworkflows/local/sativa/main.nf:184:61`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          .join(ch_taxonomy.map { [ [ id: 'user-alignment' ], it ] })
                                                              ^^
  ```

- Warning: `workflows/taxmarker.nf:120:74`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
      EMBOSS_SEQRET(ch_sequences_checked.map { [ [ id: 'user-alignment' ], it ] }, 'fasta')
                                                                           ^^
  ```
