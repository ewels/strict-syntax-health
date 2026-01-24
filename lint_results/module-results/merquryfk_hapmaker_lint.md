# Nextflow lint results

- Generated: 2026-01-24T00:20:24.623821+00:00
- Nextflow version: 25.12.0-edge
- Summary: 6 warnings

## :warning: Warnings

- Warning: `modules/nf-core/merquryfk/hapmaker/main.nf:30:52`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
      input_mat       = matktab   ? "${matktab.find{ it.toString().endsWith(".ktab") }.toString() - ~/\.ktab/}"   : ''
                                                     ^^^^^^^^^^
  ```

- Warning: `modules/nf-core/merquryfk/hapmaker/main.nf:31:52`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
      input_pat       = patktab   ? "${patktab.find{ it.toString().endsWith(".ktab") }.toString() - ~/\.ktab/}"   : ''
                                                     ^^^^^^^^^^
  ```

- Warning: `modules/nf-core/merquryfk/hapmaker/main.nf:32:54`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
      def input_child = childktab ? "${childktab.find{ it.toString().endsWith(".ktab") }.toString() - ~/\.ktab/}" : ''
                                                       ^^^^^^^^^^
  ```

- Warning: `modules/nf-core/merquryfk/hapmaker/main.nf:43:9`: Variable was declared but not used

  ```nextflow
      def args  = task.ext.args ?: ''
          ^^^^^^^^^^
  ```

- Warning: `modules/nf-core/merquryfk/hapmaker/main.nf:44:44`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
      input_mat = matktab ? "${matktab.find{ it.toString().endsWith(".ktab") }.toString() - ~/\.ktab/}" : ''
                                             ^^^^^^^^^^
  ```

- Warning: `modules/nf-core/merquryfk/hapmaker/main.nf:45:44`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
      input_pat = patktab ? "${patktab.find{ it.toString().endsWith(".ktab") }.toString() - ~/\.ktab/}" : ''
                                             ^^^^^^^^^^
  ```
