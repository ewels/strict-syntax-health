# Nextflow lint results

- Generated: 2026-01-16T02:02:17.569917+00:00
- Nextflow version: 25.12.0-edge
- Summary: 1 warning

## :warning: Warnings

- Warning: `modules/nf-core/gatk4/filterintervals/main.nf:26:78`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
      def read_counts_command = read_counts ? read_counts.collect { "--input ${it}" }.join(" ") : ""
                                                                               ^^^^^^^^^^
  ```
