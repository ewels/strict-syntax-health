# Nextflow lint results

- Generated: 2026-01-16T02:02:17.642501+00:00
- Nextflow version: 25.12.0-edge
- Summary: 2 errors, 1 warning

## :x: Errors

- Error: `modules/nf-core/sentieon/rsemcalculateexpression/tests/nextflow.config:17:25`: `SENTIEON_LICSRVR_IP` is not defined (hint: use `env('...')` to access environment variable)

  ```nextflow
      SENTIEON_LICENSE = "$SENTIEON_LICSRVR_IP"
                          ^^^^^^^^^^
  ```

- Error: `modules/nf-core/sentieon/rsemcalculateexpression/tests/nextflow.config:19:27`: `SENTIEON_AUTH_MECH` is not defined (hint: use `env('...')` to access environment variable)

  ```nextflow
      SENTIEON_AUTH_MECH = "$SENTIEON_AUTH_MECH"
                            ^^^^^^^^^^
  ```

## :warning: Warnings

- Warning: `modules/nf-core/sentieon/rsemcalculateexpression/main.nf:47:9`: Variable was declared but not used

  ```nextflow
      def sentieonLicense = secrets.SENTIEON_LICENSE_BASE64
          ^^^^^^^^^^
  ```
