# Nextflow lint results

- Generated: 2026-01-21T13:35:35.502071+00:00
- Nextflow version: 25.12.0-edge
- Summary: 18 warnings

## :warning: Warnings

- Warning: `subworkflows/nf-core/abundance_differential_filter/main.nf:34:19`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_versions = Channel.empty()
                    ^^^^^^^^^^
  ```

- Warning: `subworkflows/nf-core/abundance_differential_filter/main.nf:93:60`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          norm_inputs.contrasts_for_norm_with_formula.filter{it[0].differential_method == 'limma'},
                                                             ^^^^^^^^^^
  ```

- Warning: `subworkflows/nf-core/abundance_differential_filter/main.nf:94:47`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          norm_inputs.samples_and_matrix.filter{it[0].differential_method == 'limma'}
                                                ^^^^^^^^^^
  ```

- Warning: `subworkflows/nf-core/abundance_differential_filter/main.nf:100:56`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          inputs.contrasts_for_diff_with_formula.filter{ it[0].differential_method == 'limma' },
                                                         ^^^^^^^^^^
  ```

- Warning: `subworkflows/nf-core/abundance_differential_filter/main.nf:101:43`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          inputs.samples_and_matrix.filter{ it[0].differential_method == 'limma' }
                                            ^^^^^^^^^^
  ```

- Warning: `subworkflows/nf-core/abundance_differential_filter/main.nf:118:60`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          norm_inputs.contrasts_for_norm_with_formula.filter{it[0].differential_method == 'deseq2'},
                                                             ^^^^^^^^^^
  ```

- Warning: `subworkflows/nf-core/abundance_differential_filter/main.nf:119:47`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          norm_inputs.samples_and_matrix.filter{it[0].differential_method == 'deseq2'},
                                                ^^^^^^^^^^
  ```

- Warning: `subworkflows/nf-core/abundance_differential_filter/main.nf:120:45`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          norm_inputs.control_features.filter{it[0].differential_method == 'deseq2'},
                                              ^^^^^^^^^^
  ```

- Warning: `subworkflows/nf-core/abundance_differential_filter/main.nf:121:46`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          norm_inputs.transcript_length.filter{it[0].differential_method == 'deseq2'}
                                               ^^^^^^^^^^
  ```

- Warning: `subworkflows/nf-core/abundance_differential_filter/main.nf:127:55`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          inputs.contrasts_for_diff_with_formula.filter{it[0].differential_method == 'deseq2'},
                                                        ^^^^^^^^^^
  ```

- Warning: `subworkflows/nf-core/abundance_differential_filter/main.nf:128:42`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          inputs.samples_and_matrix.filter{it[0].differential_method == 'deseq2'},
                                           ^^^^^^^^^^
  ```

- Warning: `subworkflows/nf-core/abundance_differential_filter/main.nf:129:40`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          inputs.control_features.filter{it[0].differential_method == 'deseq2'},
                                         ^^^^^^^^^^
  ```

- Warning: `subworkflows/nf-core/abundance_differential_filter/main.nf:130:41`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          inputs.transcript_length.filter{it[0].differential_method == 'deseq2'}
                                          ^^^^^^^^^^
  ```

- Warning: `subworkflows/nf-core/abundance_differential_filter/main.nf:143:42`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          inputs.contrasts_for_diff.filter{it[0].differential_method == 'propd'},
                                           ^^^^^^^^^^
  ```

- Warning: `subworkflows/nf-core/abundance_differential_filter/main.nf:144:44`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          inputs.samples_and_matrix.filter { it[0].differential_method == 'propd' }
                                             ^^^^^^^^^^
  ```

- Warning: `subworkflows/nf-core/abundance_differential_filter/main.nf:166:60`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          norm_inputs.contrasts_for_norm_with_formula.filter{it[0].differential_method == 'dream'},
                                                             ^^^^^^^^^^
  ```

- Warning: `subworkflows/nf-core/abundance_differential_filter/main.nf:167:47`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          norm_inputs.samples_and_matrix.filter{it[0].differential_method == 'dream'}
                                                ^^^^^^^^^^
  ```

- Warning: `subworkflows/nf-core/abundance_differential_filter/main.nf:172:43`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          inputs.samples_and_matrix.filter{ it[0].differential_method == 'dream' }
                                            ^^^^^^^^^^
  ```
