# Nextflow lint results

- Generated: 2026-08-29T00:21:12.285939+00:00
- Nextflow version: 26.08.0-edge
- Summary: 2 warnings

## :warning: Warnings

- Warning: `modules/nf-core/trtools/mergestr/main.nf:24:23`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
      if ( vcfs.any{ "${it}" == "${prefix}.vcf" || "${it}" == "${prefix}.vcf.gz" } ) {
                        ^^^^^^^^^^
  ```

- Warning: `modules/nf-core/trtools/mergestr/main.nf:24:53`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
      if ( vcfs.any{ "${it}" == "${prefix}.vcf" || "${it}" == "${prefix}.vcf.gz" } ) {
                                                      ^^^^^^^^^^
  ```
