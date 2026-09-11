# Nextflow lint results

- Generated: 2026-09-11T00:23:18.588334+00:00
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
