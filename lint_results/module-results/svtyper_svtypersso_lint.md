# Nextflow lint results

- Generated: 2026-01-16T02:02:17.655411+00:00
- Nextflow version: 25.12.0-edge
- Summary: 2 errors, 1 warning

## :x: Errors

- Error: `modules/nf-core/svtyper/svtypersso/main.nf:25:9`: `vcf` is already declared

  ```nextflow
      def vcf    = vcf ? "--input_vcf ${vcf}" : ""
          ^^^^^^^^^^
  ```

- Error: `modules/nf-core/svtyper/svtypersso/main.nf:26:9`: `fasta` is already declared

  ```nextflow
      def fasta  = fasta ? "--ref_fasta ${fasta}" : ""
          ^^^^^^^^^^
  ```

## :warning: Warnings

- Warning: `modules/nf-core/svtyper/svtypersso/main.nf:46:9`: Variable was declared but not used

  ```nextflow
      def args   = task.ext.args ?: ''
          ^^^^^^^^^^
  ```
