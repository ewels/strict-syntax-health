# Nextflow lint results

- Generated: 2026-01-16T02:02:17.631869+00:00
- Nextflow version: 25.12.0-edge
- Summary: 1 warning

## :warning: Warnings

- Warning: `modules/nf-core/rsem/preparereference/main.nf:27:30`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          args_list.removeIf { it.contains('--star') }
                               ^^^^^^^^^^
  ```
