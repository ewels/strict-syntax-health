# Nextflow lint results

- Generated: 2026-01-16T02:02:17.641491+00:00
- Nextflow version: 25.12.0-edge
- Summary: 2 errors, 1 warning

## :x: Errors

- Error: `modules/nf-core/sentieon/haplotyper/tests/nextflow.config:3:25`: `SENTIEON_LICSRVR_IP` is not defined (hint: use `env('...')` to access environment variable)

  ```nextflow
      SENTIEON_LICENSE = "$SENTIEON_LICSRVR_IP"
                          ^^^^^^^^^^
  ```

- Error: `modules/nf-core/sentieon/haplotyper/tests/nextflow.config:5:27`: `SENTIEON_AUTH_MECH` is not defined (hint: use `env('...')` to access environment variable)

  ```nextflow
      SENTIEON_AUTH_MECH = "$SENTIEON_AUTH_MECH"
                            ^^^^^^^^^^
  ```

## :warning: Warnings

- Warning: `modules/nf-core/sentieon/haplotyper/main.nf:37:68`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
      def input_list = input instanceof List ? input.collect { "-i ${it}" }.join(' ') : "-i ${input}"
                                                                     ^^^^^^^^^^
  ```
