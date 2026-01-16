# Nextflow lint results

- Generated: 2026-01-16T02:02:17.576885+00:00
- Nextflow version: 25.12.0-edge
- Summary: 3 warnings

## :warning: Warnings

- Warning: `modules/nf-core/glimpse2/phase/main.nf:45:9`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          it.toString().endsWithAny("cram", "bam")          ? "bam" :
          ^^^^^^^^^^
  ```

- Warning: `modules/nf-core/glimpse2/phase/main.nf:46:9`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          it.toString().endsWithAny("vcf", "bcf", "vcf.gz") ? "gl"  :
          ^^^^^^^^^^
  ```

- Warning: `modules/nf-core/glimpse2/phase/main.nf:47:9`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          it.getExtension()
          ^^^^^^^^^^
  ```
