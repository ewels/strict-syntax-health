# Nextflow lint results

- Generated: 2026-01-16T02:02:17.534033+00:00
- Nextflow version: 25.12.0-edge
- Summary: 2 errors

## :x: Errors

- Error: `modules/nf-core/biobambam/bamsormadup/main.nf:28:47`: `reference` is not defined

  ```nextflow
      if (args.contains("outputformat=cram") && reference == null) error "Reference required for CRAM output."
                                                ^^^^^^^^^^
  ```

- Error: `modules/nf-core/biobambam/bamsormadup/main.nf:56:47`: `reference` is not defined

  ```nextflow
      if (args.contains("outputformat=cram") && reference == null) error "Reference required for CRAM output."
                                                ^^^^^^^^^^
  ```
