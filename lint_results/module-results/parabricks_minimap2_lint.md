# Nextflow lint results

- Generated: 2026-01-16T02:02:17.616271+00:00
- Nextflow version: 25.12.0-edge
- Summary: 2 warnings

## :warning: Warnings

- Warning: `modules/nf-core/parabricks/minimap2/main.nf:52:117`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
      def known_sites_command    = known_sites ? (known_sites instanceof List ? known_sites.collect { "--knownSites ${it}" }.join(' ') : "--knownSites ${known_sites}") : ""
                                                                                                                      ^^^^^^^^^^
  ```

- Warning: `modules/nf-core/parabricks/minimap2/main.nf:54:126`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
      def interval_file_command  = interval_file ? (interval_file instanceof List ? interval_file.collect { "--interval-file ${it}" }.join(' ') : "--interval-file ${interval_file}") : ""
                                                                                                                               ^^^^^^^^^^
  ```
