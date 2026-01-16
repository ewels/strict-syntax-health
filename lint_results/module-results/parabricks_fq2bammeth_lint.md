# Nextflow lint results

- Generated: 2026-01-16T02:02:17.615717+00:00
- Nextflow version: 25.12.0-edge
- Summary: 1 warning

## :warning: Warnings

- Warning: `modules/nf-core/parabricks/fq2bammeth/main.nf:35:83`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
      def known_sites_command = known_sites ? known_sites.collect { "--knownSites ${it}" }.join(' ') : ""
                                                                                    ^^^^^^^^^^
  ```
