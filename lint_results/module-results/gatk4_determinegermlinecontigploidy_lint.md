# Nextflow lint results

- Generated: 2026-01-16T02:02:17.569538+00:00
- Nextflow version: 25.12.0-edge
- Summary: 2 warnings

## :warning: Warnings

- Warning: `modules/nf-core/gatk4/determinegermlinecontigploidy/main.nf:27:80`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
      def exclude = exclude_beds ? exclude_beds.collect { "--exclude-intervals ${it}" }.join(" ") : ""
                                                                                 ^^^^^^^^^^
  ```

- Warning: `modules/nf-core/gatk4/determinegermlinecontigploidy/main.nf:30:50`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
      def input_list = counts.collect { "--input ${it}" }.join(" ")
                                                   ^^^^^^^^^^
  ```
