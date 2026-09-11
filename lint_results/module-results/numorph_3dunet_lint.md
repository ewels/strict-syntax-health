# Nextflow lint results

- Generated: 2026-09-11T00:23:06.324221+00:00
- Nextflow version: 26.08.0-edge
- Summary: 1 warning

## :warning: Warnings

- Warning: `modules/nf-core/numorph/3dunet/main.nf:41:9`: Variable was declared but not used

  ```nextflow
      def args = task.ext.args ?: ''
          ^^^^^^^^^^
  ```
