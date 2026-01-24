# Nextflow lint results

- Generated: 2026-01-24T00:20:36.573820+00:00
- Nextflow version: 25.12.0-edge
- Summary: 26 warnings

## :warning: Warnings

- Warning: `subworkflows/nf-core/differential_functional_enrichment/main.nf:36:19`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_versions = Channel.empty()
                    ^^^^^^^^^^
  ```

- Warning: `subworkflows/nf-core/differential_functional_enrichment/main.nf:58:62`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
      def criteria = multiMapCriteria { meta, input, genesets, background, method, samplesheet, featuresheet, features_id, features_symbol, meta_contrast, variable, reference, target, formula, comparison ->
                                                               ^^^^^^^^^^
  ```

- Warning: `subworkflows/nf-core/differential_functional_enrichment/main.nf:58:154`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
      def criteria = multiMapCriteria { meta, input, genesets, background, method, samplesheet, featuresheet, features_id, features_symbol, meta_contrast, variable, reference, target, formula, comparison ->
                                                                                                                                                           ^^^^^^^^^^
  ```

- Warning: `subworkflows/nf-core/differential_functional_enrichment/main.nf:58:164`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
      def criteria = multiMapCriteria { meta, input, genesets, background, method, samplesheet, featuresheet, features_id, features_symbol, meta_contrast, variable, reference, target, formula, comparison ->
                                                                                                                                                                     ^^^^^^^^^^
  ```

- Warning: `subworkflows/nf-core/differential_functional_enrichment/main.nf:58:175`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
      def criteria = multiMapCriteria { meta, input, genesets, background, method, samplesheet, featuresheet, features_id, features_symbol, meta_contrast, variable, reference, target, formula, comparison ->
                                                                                                                                                                                ^^^^^^^^^^
  ```

- Warning: `subworkflows/nf-core/differential_functional_enrichment/main.nf:58:183`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
      def criteria = multiMapCriteria { meta, input, genesets, background, method, samplesheet, featuresheet, features_id, features_symbol, meta_contrast, variable, reference, target, formula, comparison ->
                                                                                                                                                                                        ^^^^^^^^^^
  ```

- Warning: `subworkflows/nf-core/differential_functional_enrichment/main.nf:58:192`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
      def criteria = multiMapCriteria { meta, input, genesets, background, method, samplesheet, featuresheet, features_id, features_symbol, meta_contrast, variable, reference, target, formula, comparison ->
                                                                                                                                                                                                 ^^^^^^^^^^
  ```

- Warning: `subworkflows/nf-core/differential_functional_enrichment/main.nf:75:19`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          .filter { meta, contrastMap, variable, reference, target, formula, comparison ->
                    ^^^^^^^^^^
  ```

- Warning: `subworkflows/nf-core/differential_functional_enrichment/main.nf:75:25`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          .filter { meta, contrastMap, variable, reference, target, formula, comparison ->
                          ^^^^^^^^^^
  ```

- Warning: `subworkflows/nf-core/differential_functional_enrichment/main.nf:75:48`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          .filter { meta, contrastMap, variable, reference, target, formula, comparison ->
                                                 ^^^^^^^^^^
  ```

- Warning: `subworkflows/nf-core/differential_functional_enrichment/main.nf:75:59`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          .filter { meta, contrastMap, variable, reference, target, formula, comparison ->
                                                            ^^^^^^^^^^
  ```

- Warning: `subworkflows/nf-core/differential_functional_enrichment/main.nf:75:67`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          .filter { meta, contrastMap, variable, reference, target, formula, comparison ->
                                                                    ^^^^^^^^^^
  ```

- Warning: `subworkflows/nf-core/differential_functional_enrichment/main.nf:75:76`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          .filter { meta, contrastMap, variable, reference, target, formula, comparison ->
                                                                             ^^^^^^^^^^
  ```

- Warning: `subworkflows/nf-core/differential_functional_enrichment/main.nf:80:18`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          .filter{ it[4] == 'gsea' }
                   ^^^^^^^^^^
  ```

- Warning: `subworkflows/nf-core/differential_functional_enrichment/main.nf:91:42`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          ch_input_for_other.input.filter{ it[0].functional_method == 'gprofiler2' },
                                           ^^^^^^^^^^
  ```

- Warning: `subworkflows/nf-core/differential_functional_enrichment/main.nf:92:45`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          ch_input_for_other.genesets.filter{ it[0].functional_method == 'gprofiler2'},
                                              ^^^^^^^^^^
  ```

- Warning: `subworkflows/nf-core/differential_functional_enrichment/main.nf:93:47`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          ch_input_for_other.background.filter{ it[0].functional_method == 'gprofiler2'}
                                                ^^^^^^^^^^
  ```

- Warning: `subworkflows/nf-core/differential_functional_enrichment/main.nf:119:38`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          ch_input_for_gsea.map{ tuple(it[0].reference, it[0].target) },
                                       ^^^^^^^^^^
  ```

- Warning: `subworkflows/nf-core/differential_functional_enrichment/main.nf:119:55`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          ch_input_for_gsea.map{ tuple(it[0].reference, it[0].target) },
                                                        ^^^^^^^^^^
  ```

- Warning: `subworkflows/nf-core/differential_functional_enrichment/main.nf:127:42`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          ch_input_for_other.input.filter{ it[0].functional_method == 'decoupler' },
                                           ^^^^^^^^^^
  ```

- Warning: `subworkflows/nf-core/differential_functional_enrichment/main.nf:128:45`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          ch_input_for_other.genesets.filter{ it[0].functional_method == 'decoupler'},
                                              ^^^^^^^^^^
  ```

- Warning: `subworkflows/nf-core/differential_functional_enrichment/main.nf:129:45`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          ch_input_for_other.features.filter{ it[0].functional_method == 'decoupler'}
                                              ^^^^^^^^^^
  ```

- Warning: `subworkflows/nf-core/differential_functional_enrichment/main.nf:130:41`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
              .map{ meta, features_sheet, features_id, features_symbol -> [meta, features_sheet] }
                                          ^^^^^^^^^^
  ```

- Warning: `subworkflows/nf-core/differential_functional_enrichment/main.nf:130:54`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
              .map{ meta, features_sheet, features_id, features_symbol -> [meta, features_sheet] }
                                                       ^^^^^^^^^^
  ```

- Warning: `subworkflows/nf-core/differential_functional_enrichment/main.nf:138:42`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          ch_input_for_other.input.filter{ it[0].functional_method == 'grea' },
                                           ^^^^^^^^^^
  ```

- Warning: `subworkflows/nf-core/differential_functional_enrichment/main.nf:139:45`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          ch_input_for_other.genesets.filter{ it[0].functional_method == 'grea' }
                                              ^^^^^^^^^^
  ```
