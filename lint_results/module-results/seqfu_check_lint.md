# Nextflow lint results

- Generated: 2026-01-16T02:02:17.644639+00:00
- Nextflow version: 25.12.0-edge
- Summary: 1 warning

## :warning: Warnings

- Warning: `modules/nf-core/seqfu/check/main.nf:24:58`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
      def dirFlag = (reads instanceof List ? reads.every { it.isDirectory() } : reads.isDirectory()) ? "--dir" : ""
                                                           ^^^^^^^^^^
  ```
