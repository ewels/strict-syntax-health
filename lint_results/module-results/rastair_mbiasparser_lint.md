# Nextflow lint results

- Generated: 2026-01-16T02:02:17.629481+00:00
- Nextflow version: 25.12.0-edge
- Summary: 2 errors

## :x: Errors

- Error: `modules/nf-core/rastair/mbiasparser/main.nf:15:26`: `trim_OT` is not defined

  ```nextflow
      tuple val(meta), env(trim_OT), env(trim_OB),                    emit: mbias_processed_str
                           ^^^^^^^^^^
  ```

- Error: `modules/nf-core/rastair/mbiasparser/main.nf:15:40`: `trim_OB` is not defined

  ```nextflow
      tuple val(meta), env(trim_OT), env(trim_OB),                    emit: mbias_processed_str
                                         ^^^^^^^^^^
  ```
