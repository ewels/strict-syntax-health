# Nextflow lint results

- Generated: 2026-01-16T02:02:17.638993+00:00
- Nextflow version: 25.12.0-edge
- Summary: 1 error

## :x: Errors

- Error: `modules/nf-core/segemehl/align/main.nf:28:9`: `reads` is already declared

  ```nextflow
      def reads = meta.single_end ? "-q ${reads}" : "-q ${reads[0]} -p ${reads[1]}"
          ^^^^^^^^^^
  ```
