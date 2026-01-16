# Nextflow lint results

- Generated: 2026-01-16T02:02:17.529675+00:00
- Nextflow version: 25.12.0-edge
- Summary: 1 warning

## :warning: Warnings

- Warning: `modules/nf-core/bcftools/convert/main.nf:87:39`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          hap = args_split.findIndexOf{ it == '--haplegendsample'}
                                        ^^^^^^^^^^
  ```
