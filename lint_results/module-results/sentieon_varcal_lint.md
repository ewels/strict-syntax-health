# Nextflow lint results

- Generated: 2026-01-16T02:02:17.644142+00:00
- Nextflow version: 25.12.0-edge
- Summary: 2 errors

## :x: Errors

- Error: `modules/nf-core/sentieon/varcal/tests/nextflow.config:9:25`: `SENTIEON_LICSRVR_IP` is not defined (hint: use `env('...')` to access environment variable)

  ```nextflow
      SENTIEON_LICENSE = "$SENTIEON_LICSRVR_IP"
                          ^^^^^^^^^^
  ```

- Error: `modules/nf-core/sentieon/varcal/tests/nextflow.config:11:27`: `SENTIEON_AUTH_MECH` is not defined (hint: use `env('...')` to access environment variable)

  ```nextflow
      SENTIEON_AUTH_MECH = "$SENTIEON_AUTH_MECH"
                            ^^^^^^^^^^
  ```
