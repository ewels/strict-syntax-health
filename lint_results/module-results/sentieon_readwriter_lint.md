# Nextflow lint results

- Generated: 2026-01-16T02:02:17.642163+00:00
- Nextflow version: 25.12.0-edge
- Summary: 4 errors, 2 warnings

## :x: Errors

- Error: `modules/nf-core/sentieon/readwriter/tests/nextflow.config:3:25`: `SENTIEON_LICSRVR_IP` is not defined (hint: use `env('...')` to access environment variable)

  ```nextflow
      SENTIEON_LICENSE = "$SENTIEON_LICSRVR_IP"
                          ^^^^^^^^^^
  ```

- Error: `modules/nf-core/sentieon/readwriter/tests/nextflow.config:5:27`: `SENTIEON_AUTH_MECH` is not defined (hint: use `env('...')` to access environment variable)

  ```nextflow
      SENTIEON_AUTH_MECH = "$SENTIEON_AUTH_MECH"
                            ^^^^^^^^^^
  ```

- Error: `modules/nf-core/sentieon/readwriter/tests/nextflow_outputcram.config:3:25`: `SENTIEON_LICSRVR_IP` is not defined (hint: use `env('...')` to access environment variable)

  ```nextflow
      SENTIEON_LICENSE = "$SENTIEON_LICSRVR_IP"
                          ^^^^^^^^^^
  ```

- Error: `modules/nf-core/sentieon/readwriter/tests/nextflow_outputcram.config:5:27`: `SENTIEON_AUTH_MECH` is not defined (hint: use `env('...')` to access environment variable)

  ```nextflow
      SENTIEON_AUTH_MECH = "$SENTIEON_AUTH_MECH"
                            ^^^^^^^^^^
  ```

## :warning: Warnings

- Warning: `modules/nf-core/sentieon/readwriter/main.nf:30:34`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
      def input_str = input.sort { it.getName() }.collect { "-i ${it}" }.join(' ')
                                   ^^^^^^^^^^
  ```

- Warning: `modules/nf-core/sentieon/readwriter/main.nf:30:65`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
      def input_str = input.sort { it.getName() }.collect { "-i ${it}" }.join(' ')
                                                                  ^^^^^^^^^^
  ```
