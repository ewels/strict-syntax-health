# Nextflow lint results

- Generated: 2026-01-16T02:02:17.643424+00:00
- Nextflow version: 25.12.0-edge
- Summary: 2 errors, 2 warnings

## :x: Errors

- Error: `modules/nf-core/sentieon/tnfilter/tests/nextflow.config:3:25`: `SENTIEON_LICSRVR_IP` is not defined (hint: use `env('...')` to access environment variable)

  ```nextflow
      SENTIEON_LICENSE = "$SENTIEON_LICSRVR_IP"
                          ^^^^^^^^^^
  ```

- Error: `modules/nf-core/sentieon/tnfilter/tests/nextflow.config:5:27`: `SENTIEON_AUTH_MECH` is not defined (hint: use `env('...')` to access environment variable)

  ```nextflow
      SENTIEON_AUTH_MECH = "$SENTIEON_AUTH_MECH"
                            ^^^^^^^^^^
  ```

## :warning: Warnings

- Warning: `modules/nf-core/sentieon/tnfilter/main.nf:30:78`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
      def segments_command = segments ? segments.collect { "--tumor_segments ${it}" }.join(' ') : ''
                                                                               ^^^^^^^^^^
  ```

- Warning: `modules/nf-core/sentieon/tnfilter/main.nf:31:112`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
      def orientation_priors_command = orientation_priors ? orientation_priors.collect { "--orientation_priors ${it}" }.join(' ') : ''
                                                                                                                 ^^^^^^^^^^
  ```
