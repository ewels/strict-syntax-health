# Nextflow lint results

- Generated: 2026-01-16T02:02:17.537124+00:00
- Nextflow version: 25.12.0-edge
- Summary: 2 errors

## :x: Errors

- Error: `modules/nf-core/blobtk/plot/main.nf:9:5`: Invalid process directive

  ```nextflow
      errorStrategy = 'ignore'
      ^^^^^^^^^^
  ```

- Error: `modules/nf-core/blobtk/plot/main.nf:55:9`: `prefix` is already declared

  ```nextflow
      def prefix  = task.ext.prefix ?: "${meta.id}"
          ^^^^^^^^^^
  ```
