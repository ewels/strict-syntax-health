# Nextflow lint results

- Generated: 2026-01-16T02:02:17.641867+00:00
- Nextflow version: 25.12.0-edge
- Summary: 2 errors, 2 warnings

## :x: Errors

- Error: `modules/nf-core/sentieon/qualcal/tests/nextflow.config:3:25`: `SENTIEON_LICSRVR_IP` is not defined (hint: use `env('...')` to access environment variable)

  ```nextflow
      SENTIEON_LICENSE = "$SENTIEON_LICSRVR_IP"
                          ^^^^^^^^^^
  ```

- Error: `modules/nf-core/sentieon/qualcal/tests/nextflow.config:5:27`: `SENTIEON_AUTH_MECH` is not defined (hint: use `env('...')` to access environment variable)

  ```nextflow
      SENTIEON_AUTH_MECH = "$SENTIEON_AUTH_MECH"
                            ^^^^^^^^^^
  ```

## :warning: Warnings

- Warning: `modules/nf-core/sentieon/qualcal/main.nf:33:44`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
      def input_list = input.collect { "-i ${it}" }.join(' ')
                                             ^^^^^^^^^^
  ```

- Warning: `modules/nf-core/sentieon/qualcal/main.nf:34:64`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
      def knownSites = known_sites ? known_sites.collect { "-k ${it}" }.join(' ') : ""
                                                                 ^^^^^^^^^^
  ```
