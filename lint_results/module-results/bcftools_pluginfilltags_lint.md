# Nextflow lint results

- Generated: 2026-01-16T02:02:17.530566+00:00
- Nextflow version: 25.12.0-edge
- Summary: 1 warning

## :warning: Warnings

- Warning: `modules/nf-core/bcftools/pluginfilltags/main.nf:39:16`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          assert it.name != "${prefix}.${extension}" : "Input and output names are the same, set prefix in module configuration to disambiguate!"
                 ^^^^^^^^^^
  ```
