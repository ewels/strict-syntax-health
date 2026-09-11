# Nextflow lint results

- Generated: 2026-09-11T00:23:18.592205+00:00
- Nextflow version: 26.08.0-edge
- Summary: 2 warnings

## :warning: Warnings

- Warning: `subworkflows/nf-core/orftable_fasta_gtf_buildorfcatalogue/main.nf:49:19`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          .filter { it.size() > 0 }
                    ^^^^^^^^^^
  ```

- Warning: `subworkflows/nf-core/orftable_fasta_gtf_buildorfcatalogue/main.nf:55:19`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          .filter { it.size() > 0 }
                    ^^^^^^^^^^
  ```
