# Nextflow lint results

- Generated: 2026-01-24T00:20:36.573409+00:00
- Nextflow version: 25.12.0-edge
- Summary: 1 error, 7 warnings

## :x: Errors

- Error: `subworkflows/nf-core/dia_proteomics_analysis/main.nf:110:21`: Unexpected input: ','

  ```nextflow
      def mass_acc_ms1, mass_acc_ms2, scan_window
                      ^^^^^^^^^^
  ```

## :warning: Warnings

- Warning: `subworkflows/nf-core/dia_proteomics_analysis/nextflow.config:45:21`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          ].findAll { it != '' }.join(' ').trim()}
                      ^^^^^^^^^^
  ```

- Warning: `subworkflows/nf-core/dia_proteomics_analysis/nextflow.config:62:21`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          ].findAll { it != '' }.join(' ').trim()
                      ^^^^^^^^^^
  ```

- Warning: `subworkflows/nf-core/dia_proteomics_analysis/nextflow.config:80:21`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          ].findAll { it != '' }.join(' ').trim()
                      ^^^^^^^^^^
  ```

- Warning: `subworkflows/nf-core/dia_proteomics_analysis/nextflow.config:101:25`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
              ].findAll { it != '' }.join(' ').trim()
                          ^^^^^^^^^^
  ```

- Warning: `subworkflows/nf-core/dia_proteomics_analysis/nextflow.config:124:21`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          ].findAll { it != '' }.join(' ').trim()
                      ^^^^^^^^^^
  ```

- Warning: `subworkflows/nf-core/dia_proteomics_analysis/nextflow.config:135:25`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
              ].findAll { it != '' }.join(' ').trim()
                          ^^^^^^^^^^
  ```

- Warning: `subworkflows/nf-core/dia_proteomics_analysis/tests/nextflow.config:52:21`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          ].findAll { it != '' }.join(' ').trim()
                      ^^^^^^^^^^
  ```
