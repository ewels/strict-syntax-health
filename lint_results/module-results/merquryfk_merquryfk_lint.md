# Nextflow lint results

- Generated: 2026-01-21T13:35:22.802833+00:00
- Nextflow version: 25.12.0-edge
- Summary: 3 warnings

## :warning: Warnings

- Warning: `modules/nf-core/merquryfk/merquryfk/main.nf:40:56`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
      def fk_ktab     = fastk_ktab ? "${fastk_ktab.find{ it.toString().endsWith(".ktab") }}" : ''
                                                         ^^^^^^^^^^
  ```

- Warning: `modules/nf-core/merquryfk/merquryfk/main.nf:41:55`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
      def mat_hapktab = mathaptab  ? "${mathaptab.find{ it.toString().endsWith(".ktab") }}"  : ''
                                                        ^^^^^^^^^^
  ```

- Warning: `modules/nf-core/merquryfk/merquryfk/main.nf:42:55`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
      def pat_hapktab = pathaptab  ? "${pathaptab.find{ it.toString().endsWith(".ktab") }}"  : ''
                                                        ^^^^^^^^^^
  ```
