# Nextflow lint results

- Generated: 2026-01-21T13:35:22.850380+00:00
- Nextflow version: 25.12.0-edge
- Summary: 1 warning

## :warning: Warnings

- Warning: `modules/nf-core/sentieon/tnhaplotyper2/main.nf:44:40`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
      def inputs = input.collect { "-i ${it}" }.join(" ")
                                         ^^^^^^^^^^
  ```
