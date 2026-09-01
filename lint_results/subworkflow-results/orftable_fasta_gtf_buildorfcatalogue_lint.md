# Nextflow lint results

- Generated: 2026-09-01T00:25:56.434936+00:00
- Nextflow version: 26.08.0-edge
- Summary: 2 warnings

## :warning: Warnings

- Warning: `subworkflows/nf-core/orftable_fasta_gtf_buildorfcatalogue/main.nf:51:19`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          .filter { it.size() > 0 }
                    ^^^^^^^^^^
  ```

- Warning: `subworkflows/nf-core/orftable_fasta_gtf_buildorfcatalogue/main.nf:57:19`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          .filter { it.size() > 0 }
                    ^^^^^^^^^^
  ```
