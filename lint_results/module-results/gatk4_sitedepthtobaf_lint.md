# Nextflow lint results

- Generated: 2026-01-16T02:02:17.573096+00:00
- Nextflow version: 25.12.0-edge
- Summary: 1 warning

## :warning: Warnings

- Warning: `modules/nf-core/gatk4/sitedepthtobaf/main.nf:29:66`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
      def site_depth_input = site_depths.collect { "--site-depth ${it}" }.join(" ")
                                                                   ^^^^^^^^^^
  ```
