# Nextflow lint results

- Generated: 2026-09-03T00:23:48.553381712Z
- Nextflow version: 26.08.0-edge
- Summary: 13 warnings

## :warning: Warnings

- Warning: `subworkflows/local/sourmash/main.nf:144:44`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
                              .splitText() { it.trim() }
                                             ^^
  ```

- Warning: `subworkflows/local/sourmash/main.nf:145:39`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
                              .filter { it }
                                        ^^
  ```

- Warning: `subworkflows/local/sourmash/main.nf:154:44`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
                              .splitText() { it.trim() }
                                             ^^
  ```

- Warning: `subworkflows/local/sourmash/main.nf:155:39`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
                              .filter { it }
                                        ^^
  ```

- Warning: `subworkflows/local/utils_nfcore_magmap_pipeline/main.nf:55:5`: Variable was declared but not used

  ```nextflow
      ch_versions = channel.empty()
      ^^^^^^^^^^^
  ```

- Warning: `workflows/magmap.nf:251:28`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
              .splitText() { it.trim() }
                             ^^
  ```

- Warning: `workflows/magmap.nf:252:23`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
              .filter { it }
                        ^^
  ```

- Warning: `workflows/magmap.nf:265:36`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
                      .splitText() { it.trim() }
                                     ^^
  ```

- Warning: `workflows/magmap.nf:266:31`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
                      .filter { it }
                                ^^
  ```

- Warning: `workflows/magmap.nf:274:36`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
                      .splitText() { it.trim() }
                                     ^^
  ```

- Warning: `workflows/magmap.nf:275:31`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
                      .filter { it }
                                ^^
  ```

- Warning: `workflows/magmap.nf:333:66`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
                  .map { pairs -> [ [ id: 'all' ], pairs.collect { it[0] }, pairs.collect { it[1] } ] }
                                                                   ^^
  ```

- Warning: `workflows/magmap.nf:333:91`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
                  .map { pairs -> [ [ id: 'all' ], pairs.collect { it[0] }, pairs.collect { it[1] } ] }
                                                                                            ^^
  ```
