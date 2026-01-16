# Nextflow lint results

- Generated: 2026-01-16T02:02:17.643686+00:00
- Nextflow version: 25.12.0-edge
- Summary: 2 errors, 1 warning

## :x: Errors

- Error: `modules/nf-core/sentieon/tnhaplotyper2/tests/nextflow.config:24:25`: `SENTIEON_LICSRVR_IP` is not defined (hint: use `env('...')` to access environment variable)

  ```nextflow
      SENTIEON_LICENSE = "$SENTIEON_LICSRVR_IP"
                          ^^^^^^^^^^
  ```

- Error: `modules/nf-core/sentieon/tnhaplotyper2/tests/nextflow.config:26:27`: `SENTIEON_AUTH_MECH` is not defined (hint: use `env('...')` to access environment variable)

  ```nextflow
      SENTIEON_AUTH_MECH = "$SENTIEON_AUTH_MECH"
                            ^^^^^^^^^^
  ```

## :warning: Warnings

- Warning: `modules/nf-core/sentieon/tnhaplotyper2/main.nf:44:40`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
      def inputs = input.collect { "-i ${it}" }.join(" ")
                                         ^^^^^^^^^^
  ```
