# Nextflow lint results

- Generated: 2026-01-16T02:02:17.595950+00:00
- Nextflow version: 25.12.0-edge
- Summary: 2 warnings

## :warning: Warnings

- Warning: `modules/nf-core/macs2/callpeak/main.nf:33:40`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          def id = args_list.findIndexOf{it=='--format'}
                                         ^^^^^^^^^^
  ```

- Warning: `modules/nf-core/macs2/callpeak/main.nf:55:9`: Variable was declared but not used

  ```nextflow
      def args = task.ext.args ?: ''
          ^^^^^^^^^^
  ```
