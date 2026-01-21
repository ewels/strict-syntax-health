# Nextflow lint results

- Generated: 2026-01-21T13:35:22.849692+00:00
- Nextflow version: 25.12.0-edge
- Summary: 2 warnings

## :warning: Warnings

- Warning: `modules/nf-core/sentieon/readwriter/main.nf:30:34`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
      def input_str = input.sort { it.getName() }.collect { "-i ${it}" }.join(' ')
                                   ^^^^^^^^^^
  ```

- Warning: `modules/nf-core/sentieon/readwriter/main.nf:30:65`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
      def input_str = input.sort { it.getName() }.collect { "-i ${it}" }.join(' ')
                                                                  ^^^^^^^^^^
  ```
