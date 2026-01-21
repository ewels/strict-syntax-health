# Nextflow lint results

- Generated: 2026-01-21T13:35:22.769672+00:00
- Nextflow version: 25.12.0-edge
- Summary: 1 warning

## :warning: Warnings

- Warning: `modules/nf-core/gatk4/learnreadorientationmodel/main.nf:23:48`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
      def input_list = f1r2.collect { "--input ${it}" }.join(' ')
                                                 ^^^^^^^^^^
  ```
