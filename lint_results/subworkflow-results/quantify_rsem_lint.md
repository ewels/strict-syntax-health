# Nextflow lint results

- Generated: 2026-08-25T00:14:12.649145+00:00
- Nextflow version: 26.08.0-edge
- Summary: 2 warnings

## :warning: Warnings

- Warning: `subworkflows/nf-core/quantify_rsem/main.nf:62:76`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
                  .map { sorted -> [ ['id': 'all_samples'], sorted.collect { it[1] } ] },
                                                                             ^^^^^^^^^^
  ```

- Warning: `subworkflows/nf-core/quantify_rsem/main.nf:66:51`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
                  .map { sorted -> sorted.collect { it[1] } }
                                                    ^^^^^^^^^
  ```
