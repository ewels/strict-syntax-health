# Nextflow lint results

- Generated: 2026-01-16T02:02:17.654336+00:00
- Nextflow version: 25.12.0-edge
- Summary: 5 warnings

## :warning: Warnings

- Warning: `modules/nf-core/svdb/merge/main.nf:38:53`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
              def pairs = vcfs.indices.collect { [vcfs[it], input_priority[it]] }
                                                      ^^^^^^^^^^
  ```

- Warning: `modules/nf-core/svdb/merge/main.nf:38:73`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
              def pairs = vcfs.indices.collect { [vcfs[it], input_priority[it]] }
                                                                          ^^^^^^^
  ```

- Warning: `modules/nf-core/svdb/merge/main.nf:40:36`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
              vcfs = pairs.collect { it[0] }
                                     ^^^^^^^
  ```

- Warning: `modules/nf-core/svdb/merge/main.nf:41:40`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
              priority = pairs.collect { it[1] }
                                         ^^^^^^^
  ```

- Warning: `modules/nf-core/svdb/merge/main.nf:55:74`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          input = (vcfs.collect().size() > 1 && sort_inputs) ? vcfs.sort { it.name } : vcfs
                                                                           ^^^^^^^^^^
  ```
