# Nextflow lint results

- Generated: 2026-01-16T02:02:17.639291+00:00
- Nextflow version: 25.12.0-edge
- Summary: 2 errors

## :x: Errors

- Error: `modules/nf-core/sentieon/applyvarcal/tests/nextflow.config:10:25`: `SENTIEON_LICSRVR_IP` is not defined (hint: use `env('...')` to access environment variable)

  ```nextflow
      SENTIEON_LICENSE = "$SENTIEON_LICSRVR_IP"
                          ^^^^^^^^^^
  ```

- Error: `modules/nf-core/sentieon/applyvarcal/tests/nextflow.config:12:27`: `SENTIEON_AUTH_MECH` is not defined (hint: use `env('...')` to access environment variable)

  ```nextflow
      SENTIEON_AUTH_MECH = "$SENTIEON_AUTH_MECH"
                            ^^^^^^^^^^
  ```
