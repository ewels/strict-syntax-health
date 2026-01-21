# Nextflow lint results

- Generated: 2026-01-21T13:35:22.712112+00:00
- Nextflow version: 25.12.0-edge
- Summary: 1 warning

## :warning: Warnings

- Warning: `modules/nf-core/bamtools/split/main.nf:23:39`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
      def input_list = bam.collect{"-in $it"}.join(' ')
                                        ^^^^^^^^^^
  ```
