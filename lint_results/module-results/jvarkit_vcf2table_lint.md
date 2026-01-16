# Nextflow lint results

- Generated: 2026-01-16T02:02:17.588127+00:00
- Nextflow version: 25.12.0-edge
- Summary: 1 error

## :x: Errors

- Error: `modules/nf-core/jvarkit/vcf2table/main.nf:25:9`: `regions_file` is already declared

  ```nextflow
      def regions_file = regions_file? (tbi ? " --regions-file" : " --targets-file")+" \"${regions_file}\" ":""
          ^^^^^^^^^^
  ```
