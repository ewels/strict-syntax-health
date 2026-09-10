# Nextflow lint results

- Generated: 2026-09-10T00:22:54.314789+00:00
- Nextflow version: 26.08.0-edge
- Summary: 2 warnings

## :warning: Warnings

- Warning: `subworkflows/nf-core/fasta_clean_faidx/main.nf:91:32`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          renamed_fasta.filter { meta, file -> val_get_dict }
                                 ^^^^^^^^^^
  ```

- Warning: `subworkflows/nf-core/fasta_clean_faidx/main.nf:91:38`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          renamed_fasta.filter { meta, file -> val_get_dict }
                                       ^^^^^^^^^^
  ```
