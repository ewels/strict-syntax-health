# Nextflow lint results

- Generated: 2026-09-01T00:25:56.429198+00:00
- Nextflow version: 26.08.0-edge
- Summary: 2 warnings

## :warning: Warnings

- Warning: `subworkflows/nf-core/fasta_clean_faidx/main.nf:82:40`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          SEQKIT_DOTS.out.fastx.filter { meta, file -> val_get_dict }
                                         ^^^^^^^^^^
  ```

- Warning: `subworkflows/nf-core/fasta_clean_faidx/main.nf:82:46`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          SEQKIT_DOTS.out.fastx.filter { meta, file -> val_get_dict }
                                               ^^^^^^^^^^
  ```
