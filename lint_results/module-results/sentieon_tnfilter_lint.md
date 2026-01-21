# Nextflow lint results

- Generated: 2026-01-21T13:35:22.850181+00:00
- Nextflow version: 25.12.0-edge
- Summary: 2 warnings

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
