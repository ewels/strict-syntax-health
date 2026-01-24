# Nextflow lint results

- Generated: 2026-01-24T00:20:36.576318+00:00
- Nextflow version: 25.12.0-edge
- Summary: 6 warnings

## :warning: Warnings

- Warning: `subworkflows/nf-core/fasta_newick_epang_gappa/main.nf:24:19`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_versions = Channel.empty()
                    ^^^^^^^^^^
  ```

- Warning: `subworkflows/nf-core/fasta_newick_epang_gappa/main.nf:39:14`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_hmm = Channel.empty()
               ^^^^^^^^^^
  ```

- Warning: `subworkflows/nf-core/fasta_newick_epang_gappa/main.nf:55:26`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_hmmer_unaligned = Channel.empty()
                           ^^^^^^^^^^
  ```

- Warning: `subworkflows/nf-core/fasta_newick_epang_gappa/main.nf:68:41`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          .groupTuple(size: 2, sort: { a, b -> a =~ /\.hmm/ ? 1 : -1 })
                                          ^^^^^^^^^^
  ```

- Warning: `subworkflows/nf-core/fasta_newick_epang_gappa/main.nf:76:27`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_hmmer_alignquery = Channel.empty()
                            ^^^^^^^^^^
  ```

- Warning: `subworkflows/nf-core/fasta_newick_epang_gappa/main.nf:79:41`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          .groupTuple(size: 2, sort: { a, b -> a =~ /\.hmm/ ? 1 : -1 })
                                          ^^^^^^^^^^
  ```
