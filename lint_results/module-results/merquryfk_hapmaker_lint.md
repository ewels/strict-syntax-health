# Nextflow lint results

- Generated: 2026-01-16T02:02:17.599754+00:00
- Nextflow version: 25.12.0-edge
- Summary: 6 warnings

## :warning: Warnings

- Warning: `modules/nf-core/merquryfk/hapmaker/main.nf:27:52`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
      input_mat       = matktab   ? "${matktab.find{ it.toString().endsWith(".ktab") }.toString() - ~/\.ktab/}"   : ''
                                                     ^^^^^^^^^^
  ```

- Warning: `modules/nf-core/merquryfk/hapmaker/main.nf:28:52`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
      input_pat       = patktab   ? "${patktab.find{ it.toString().endsWith(".ktab") }.toString() - ~/\.ktab/}"   : ''
                                                     ^^^^^^^^^^
  ```

- Warning: `modules/nf-core/merquryfk/hapmaker/main.nf:29:54`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
      def input_child = childktab ? "${childktab.find{ it.toString().endsWith(".ktab") }.toString() - ~/\.ktab/}" : ''
                                                       ^^^^^^^^^^
  ```

- Warning: `modules/nf-core/merquryfk/hapmaker/main.nf:51:9`: Variable was declared but not used

  ```nextflow
      def args  = task.ext.args ?: ''
          ^^^^^^^^^^
  ```

- Warning: `modules/nf-core/merquryfk/hapmaker/main.nf:52:44`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
      input_mat = matktab ? "${matktab.find{ it.toString().endsWith(".ktab") }.toString() - ~/\.ktab/}" : ''
                                             ^^^^^^^^^^
  ```

- Warning: `modules/nf-core/merquryfk/hapmaker/main.nf:53:44`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
      input_pat = patktab ? "${patktab.find{ it.toString().endsWith(".ktab") }.toString() - ~/\.ktab/}" : ''
                                             ^^^^^^^^^^
  ```
