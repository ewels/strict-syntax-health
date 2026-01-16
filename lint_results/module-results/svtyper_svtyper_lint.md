# Nextflow lint results

- Generated: 2026-01-16T02:02:17.655185+00:00
- Nextflow version: 25.12.0-edge
- Summary: 2 errors, 1 warning

## :x: Errors

- Error: `modules/nf-core/svtyper/svtyper/main.nf:13:15`: `meta2` is already declared

  ```nextflow
      tuple val(meta2), path(fai)
                ^^^^^^^^^^
  ```

- Error: `modules/nf-core/svtyper/svtyper/main.nf:27:9`: `vcf` is already declared

  ```nextflow
      def vcf  = vcf ? "--input_vcf ${vcf}" : ""
          ^^^^^^^^^^
  ```

## :warning: Warnings

- Warning: `modules/nf-core/svtyper/svtyper/main.nf:12:15`: Variable was declared but not used

  ```nextflow
      tuple val(meta2), path(fasta)
                ^^^^^^^^^^
  ```
