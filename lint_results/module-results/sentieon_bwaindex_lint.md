# Nextflow lint results

- Generated: 2026-01-16T02:02:17.639462+00:00
- Nextflow version: 25.12.0-edge
- Summary: 2 errors

## :x: Errors

- Error: `modules/nf-core/sentieon/bwaindex/tests/nextflow.config:3:24`: `$SENTIEON_LICSRVR_IP` is not defined

  ```nextflow
      SENTIEON_LICENSE = $SENTIEON_LICSRVR_IP
                         ^^^^^^^^^^
  ```

- Error: `modules/nf-core/sentieon/bwaindex/tests/nextflow.config:5:26`: `$SENTIEON_AUTH_MECH` is not defined

  ```nextflow
      SENTIEON_AUTH_MECH = $SENTIEON_AUTH_MECH
                           ^^^^^^^^^^
  ```
