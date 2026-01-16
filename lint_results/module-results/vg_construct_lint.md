# Nextflow lint results

- Generated: 2026-01-16T02:02:17.663479+00:00
- Nextflow version: 25.12.0-edge
- Summary: 1 warning

## :warning: Warnings

- Warning: `modules/nf-core/vg/construct/main.nf:28:60`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
      input_files = mode == 'vcf' ? input.collect { "--vcf ${it}" }.join(" ") : "--msa ${input}"
                                                             ^^^^^^^^^^
  ```
