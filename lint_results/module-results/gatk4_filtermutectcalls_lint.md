# Nextflow lint results

- Generated: 2026-01-16T02:02:17.570064+00:00
- Nextflow version: 25.12.0-edge
- Summary: 3 warnings

## :warning: Warnings

- Warning: `modules/nf-core/gatk4/filtermutectcalls/main.nf:29:117`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
      def orientationbias_command = orientationbias ? orientationbias.collect { "--orientation-bias-artifact-priors ${it}" }.join(' ') : ''
                                                                                                                      ^^^^^^^^^^
  ```

- Warning: `modules/nf-core/gatk4/filtermutectcalls/main.nf:30:94`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
      def segmentation_command = segmentation ? segmentation.collect { "--tumor-segmentation ${it}" }.join(' ') : ''
                                                                                               ^^^^^^^^^^
  ```

- Warning: `modules/nf-core/gatk4/filtermutectcalls/main.nf:32:74`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
      def table_command = table ? table.collect { "--contamination-table ${it}" }.join(' ') : ''
                                                                           ^^^^^^^^^^
  ```
