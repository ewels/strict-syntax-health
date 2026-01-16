# Nextflow lint results

- Generated: 2026-01-16T02:02:17.561746+00:00
- Nextflow version: 25.12.0-edge
- Summary: 7 warnings

## :warning: Warnings

- Warning: `modules/nf-core/fastqscreen/buildfromindex/main.nf:22:32`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
      folder = indexes.collect { it.toString() }
                                 ^^^^^^^^^^
  ```

- Warning: `modules/nf-core/fastqscreen/buildfromindex/main.nf:24:46`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
      copy_indexes = folder.collect { "cp -r ${it} $dir/${it}"}.join(" && ")
                                               ^^^^^^^^^^
  ```

- Warning: `modules/nf-core/fastqscreen/buildfromindex/main.nf:24:57`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
      copy_indexes = folder.collect { "cp -r ${it} $dir/${it}"}.join(" && ")
                                                          ^^^^^^^^^^
  ```

- Warning: `modules/nf-core/fastqscreen/buildfromindex/main.nf:28:34`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          .collect { "########## ${it[0]} \nDATABASE ${it[0]} $dir/${it[1]}/${it[1] + '_to_be_replaced'}" }
                                   ^^^^^^^^^^
  ```

- Warning: `modules/nf-core/fastqscreen/buildfromindex/main.nf:28:54`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          .collect { "########## ${it[0]} \nDATABASE ${it[0]} $dir/${it[1]}/${it[1] + '_to_be_replaced'}" }
                                                       ^^^^^^^^^^
  ```

- Warning: `modules/nf-core/fastqscreen/buildfromindex/main.nf:28:68`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          .collect { "########## ${it[0]} \nDATABASE ${it[0]} $dir/${it[1]}/${it[1] + '_to_be_replaced'}" }
                                                                     ^^^^^^^^^^
  ```

- Warning: `modules/nf-core/fastqscreen/buildfromindex/main.nf:28:77`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          .collect { "########## ${it[0]} \nDATABASE ${it[0]} $dir/${it[1]}/${it[1] + '_to_be_replaced'}" }
                                                                              ^^^^^^^^^^
  ```
