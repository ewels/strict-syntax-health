# Nextflow lint results

- Generated: 2026-01-21T13:35:22.765900+00:00
- Nextflow version: 25.12.0-edge
- Summary: 1 warning

## :warning: Warnings

- Warning: `modules/nf-core/gatk4/baserecalibrator/main.nf:29:64`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
      def sites_command = known_sites.collect { "--known-sites ${it}" }.join(' ')
                                                                 ^^^^^^^^^^
  ```
