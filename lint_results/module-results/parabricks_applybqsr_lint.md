# Nextflow lint results

- Generated: 2026-01-21T13:35:22.820159+00:00
- Nextflow version: 25.12.0-edge
- Summary: 1 warning

## :warning: Warnings

- Warning: `modules/nf-core/parabricks/applybqsr/main.nf:32:86`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
      def interval_command = intervals        ? intervals.collect { "--interval-file ${it}" }.join(' ') : ""
                                                                                       ^^^^^^^^^^
  ```
