# Nextflow lint results

- Generated: 2026-01-16T02:02:17.570552+00:00
- Nextflow version: 25.12.0-edge
- Summary: 1 warning

## :warning: Warnings

- Warning: `modules/nf-core/gatk4/gatherpileupsummaries/main.nf:24:46`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
      def input_list = pileup.collect { "--I ${it}" }.join(' ')
                                               ^^^^^^^^^^
  ```
