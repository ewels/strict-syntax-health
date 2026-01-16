# Nextflow lint results

- Generated: 2026-01-16T02:02:17.523436+00:00
- Nextflow version: 25.12.0-edge
- Summary: 1 warning

## :warning: Warnings

- Warning: `modules/nf-core/ampcombi2/parsetables/main.nf:43:47`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          --path_list '${amp_input.collect { "${it}" }.join("' '")}' \\
                                                ^^^^^^^^^^
  ```
