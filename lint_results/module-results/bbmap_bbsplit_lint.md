# Nextflow lint results

- Generated: 2026-01-16T02:02:17.528483+00:00
- Nextflow version: 25.12.0-edge
- Summary: 2 errors, 1 warning

## :x: Errors

- Error: `modules/nf-core/bbmap/bbsplit/main.nf:41:43`: `index` is already declared

  ```nextflow
      other_ref_names.eachWithIndex { name, index ->
                                            ^^^^^^^^
  ```

- Error: `modules/nf-core/bbmap/bbsplit/main.nf:116:43`: `index` is already declared

  ```nextflow
      other_ref_names.eachWithIndex { name, index ->
                                            ^^^^^^^^
  ```

## :warning: Warnings

- Warning: `modules/nf-core/bbmap/bbsplit/main.nf:116:43`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
      other_ref_names.eachWithIndex { name, index ->
                                            ^^^^^^^^
  ```
