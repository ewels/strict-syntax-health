# Nextflow lint results

- Generated: 2026-01-16T02:02:17.661672+00:00
- Nextflow version: 25.12.0-edge
- Summary: 2 warnings

## :warning: Warnings

- Warning: `modules/nf-core/varlociraptor/callvariants/main.nf:26:120`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
      def scenario_samples = vcfs instanceof List && vcfs.size() > 1 ? [scenario_aliases, vcfs].transpose().collect { "${it[0]}=${it[1]}" }.join(' ') : "${scenario_aliases}=${vcfs}"
                                                                                                                         ^^^^^^^^^^
  ```

- Warning: `modules/nf-core/varlociraptor/callvariants/main.nf:26:129`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
      def scenario_samples = vcfs instanceof List && vcfs.size() > 1 ? [scenario_aliases, vcfs].transpose().collect { "${it[0]}=${it[1]}" }.join(' ') : "${scenario_aliases}=${vcfs}"
                                                                                                                                  ^^^^^^^^^^
  ```
