# Nextflow lint results

- Generated: 2026-01-16T02:02:17.600447+00:00
- Nextflow version: 25.12.0-edge
- Summary: 3 warnings

## :warning: Warnings

- Warning: `modules/nf-core/merquryfk/merquryfk/main.nf:45:52`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
      fk_ktab     = fastk_ktab ? "${fastk_ktab.find{ it.toString().endsWith(".ktab") }}" : ''
                                                     ^^^^^^^^^^
  ```

- Warning: `modules/nf-core/merquryfk/merquryfk/main.nf:46:51`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
      mat_hapktab = mathaptab  ? "${mathaptab.find{ it.toString().endsWith(".ktab") }}"  : ''
                                                    ^^^^^^^^^^
  ```

- Warning: `modules/nf-core/merquryfk/merquryfk/main.nf:47:51`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
      pat_hapktab = pathaptab  ? "${pathaptab.find{ it.toString().endsWith(".ktab") }}"  : ''
                                                    ^^^^^^^^^^
  ```
