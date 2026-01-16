# Nextflow lint results

- Generated: 2026-01-16T10:29:43.196462028Z
- Nextflow version: 25.12.0-edge
- Summary: 1 error, 14 warnings

## :x: Errors

- Error: `conf/modules.config:123:45`: Unexpected input: '\n'

  ```nextflow
                          case 'versions.yml':
                                              ^
  ```

## :warning: Warnings

- Warning: `modules/nf-core/fastqscreen/buildfromindex/main.nf:22:32`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
      folder = indexes.collect { it.toString() }
                                 ^^
  ```

- Warning: `modules/nf-core/fastqscreen/buildfromindex/main.nf:24:46`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
      copy_indexes = folder.collect { "cp -r ${it} $dir/${it}"}.join(" && ")
                                               ^^
  ```

- Warning: `modules/nf-core/fastqscreen/buildfromindex/main.nf:24:57`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
      copy_indexes = folder.collect { "cp -r ${it} $dir/${it}"}.join(" && ")
                                                          ^^
  ```

- Warning: `modules/nf-core/fastqscreen/buildfromindex/main.nf:28:34`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          .collect { "########## ${it[0]} \nDATABASE ${it[0]} $dir/${it[1]}/${it[1] + '_to_be_replaced'}" }
                                   ^^
  ```

- Warning: `modules/nf-core/fastqscreen/buildfromindex/main.nf:28:54`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          .collect { "########## ${it[0]} \nDATABASE ${it[0]} $dir/${it[1]}/${it[1] + '_to_be_replaced'}" }
                                                       ^^
  ```

- Warning: `modules/nf-core/fastqscreen/buildfromindex/main.nf:28:68`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          .collect { "########## ${it[0]} \nDATABASE ${it[0]} $dir/${it[1]}/${it[1] + '_to_be_replaced'}" }
                                                                     ^^
  ```

- Warning: `modules/nf-core/fastqscreen/buildfromindex/main.nf:28:77`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          .collect { "########## ${it[0]} \nDATABASE ${it[0]} $dir/${it[1]}/${it[1] + '_to_be_replaced'}" }
                                                                              ^^
  ```

- Warning: `subworkflows/local/utils_nfcore_seqinspector_pipeline/main.nf:32:5`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
      monochrome_logs   // boolean: Do not use coloured log outputs
      ^^^^^^^^^^^^^^^
  ```

- Warning: `subworkflows/local/utils_nfcore_seqinspector_pipeline/main.nf:35:5`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
      input             //  string: Path to input samplesheet
      ^^^^^
  ```

- Warning: `subworkflows/local/utils_nfcore_seqinspector_pipeline/main.nf:103:18`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      nr_samples = Channel.fromList(samplesheetToList(params.input, "${projectDir}/assets/schema_input.json"))
                   ^^^^^^^
  ```

- Warning: `subworkflows/local/utils_nfcore_seqinspector_pipeline/main.nf:109:20`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          .flatMap { it.withIndex().collect {  entry, idx -> entry + "${idx+1}" } }
                     ^^
  ```

- Warning: `subworkflows/local/utils_nfcore_seqinspector_pipeline/main.nf:132:38`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
              validateInputSamplesheet(it) // Applies additional group validation checks that schema_input.json cannot do.
                                       ^^
  ```

- Warning: `subworkflows/local/utils_nfcore_seqinspector_pipeline/main.nf:143:19`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
              meta, fastqs -> meta.tags
                    ^^^^^^
  ```

- Warning: `subworkflows/local/utils_nfcore_seqinspector_pipeline/main.nf:150:13`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
              tag_lowercase, tags ->
              ^^^^^^^^^^^^^
  ```
