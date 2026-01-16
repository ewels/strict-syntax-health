# Nextflow lint results

- Generated: 2026-01-16T02:02:17.629728+00:00
- Nextflow version: 25.12.0-edge
- Summary: 2 warnings

## :warning: Warnings

- Warning: `modules/nf-core/rbt/vcfsplit/main.nf:22:9`: Variable was declared but not used

  ```nextflow
      def args   = task.ext.args ?: ''
          ^^^^^^^^^^
  ```

- Warning: `modules/nf-core/rbt/vcfsplit/main.nf:39:56`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
      def bcf_files = (0..chunks).collect { "${prefix}.${it}.bcf" }.join(' ')
                                                         ^^^^^^^^^^
  ```
