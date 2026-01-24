# Nextflow lint results

- Generated: 2026-01-24T00:20:24.624085+00:00
- Nextflow version: 25.12.0-edge
- Summary: 2 warnings

## :warning: Warnings

- Warning: `modules/nf-core/merquryfk/katcomp/main.nf:28:39`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
      def input_fk1 = fastk1_ktab.find{ it.toString().endsWith(".ktab") }.getBaseName()
                                        ^^^^^^^^^^
  ```

- Warning: `modules/nf-core/merquryfk/katcomp/main.nf:29:39`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
      def input_fk2 = fastk2_ktab.find{ it.toString().endsWith(".ktab") }.getBaseName()
                                        ^^^^^^^^^^
  ```
