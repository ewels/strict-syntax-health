# Nextflow lint results

- Generated: 2026-01-16T02:02:17.616453+00:00
- Nextflow version: 25.12.0-edge
- Summary: 1 warning

## :warning: Warnings

- Warning: `modules/nf-core/parabricks/mutectcaller/main.nf:34:92`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
      def interval_file_command = interval_file ? interval_file.collect { "--interval-file ${it}" }.join(' ') : ""
                                                                                             ^^^^^^^^^^
  ```
