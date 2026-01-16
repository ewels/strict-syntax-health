# Nextflow lint results

- Generated: 2026-01-16T06:31:26.599163297Z
- Nextflow version: 25.12.0-edge
- Summary: 7 errors, 29 warnings

## :x: Errors

- Error: `modules/nf-core/custom/dumpsoftwareversions/main.nf:1:1`: Statements cannot be mixed with script declarations -- move statements into a process, workflow, or function

  ```nextflow
  def deprecation_message = """
  ^^^
  ```

- Error: `modules/nf-core/custom/dumpsoftwareversions/main.nf:30:18`: `deprecation_message` is not defined

  ```nextflow
      assert true: deprecation_message
                   ^^^^^^^^^^^^^^^^^^^
  ```

- Error: `workflows/drugresponseeval.nf:24:1`: Statements cannot be mixed with script declarations -- move statements into a process, workflow, or function

  ```nextflow
  def test_modes = params.test_mode.split(",")
  ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  ```

- Error: `workflows/drugresponseeval.nf:25:1`: Statements cannot be mixed with script declarations -- move statements into a process, workflow, or function

  ```nextflow
  def randomizations = params.randomization_mode.split(",")
  ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  ```

- Error: `workflows/drugresponseeval.nf:48:9`: `test_modes` is not defined

  ```nextflow
          test_modes,
          ^^^^^^^^^^
  ```

- Error: `workflows/drugresponseeval.nf:59:9`: `randomizations` is not defined

  ```nextflow
          randomizations,
          ^^^^^^^^^^^^^^
  ```

- Error: `workflows/drugresponseeval.nf:64:9`: `test_modes` is not defined

  ```nextflow
          test_modes,
          ^^^^^^^^^^
  ```

## :warning: Warnings

- Warning: `conf/modules.config:65:23`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
              saveAs: { filename -> null }
                        ^^^^^^^^
  ```

- Warning: `conf/modules.config:73:23`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
              saveAs: { filename -> null }
                        ^^^^^^^^
  ```

- Warning: `conf/modules.config:81:23`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
              saveAs: { filename -> null }
                        ^^^^^^^^
  ```

- Warning: `conf/modules.config:89:23`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
              saveAs: { filename -> null }
                        ^^^^^^^^
  ```

- Warning: `conf/modules.config:97:23`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
              saveAs: { filename -> null }
                        ^^^^^^^^
  ```

- Warning: `conf/modules.config:105:23`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
              saveAs: { filename -> null }
                        ^^^^^^^^
  ```

- Warning: `conf/modules.config:114:23`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
              saveAs: { filename -> null }
                        ^^^^^^^^
  ```

- Warning: `conf/modules.config:133:23`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
              saveAs: { filename -> null }
                        ^^^^^^^^
  ```

- Warning: `conf/modules.config:159:23`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
              saveAs: { filename -> null }
                        ^^^^^^^^
  ```

- Warning: `conf/modules.config:205:23`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
              saveAs: { filename -> null }
                        ^^^^^^^^
  ```

- Warning: `conf/modules.config:213:23`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
              saveAs: { filename -> null }
                        ^^^^^^^^
  ```

- Warning: `conf/modules.config:239:23`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
              saveAs: { filename -> null }
                        ^^^^^^^^
  ```

- Warning: `modules/nf-core/custom/dumpsoftwareversions/main.nf:1:5`: Variable was declared but not used

  ```nextflow
  def deprecation_message = """
      ^^^^^^^^^^^^^^^^^^^
  ```

- Warning: `modules/nf-core/custom/dumpsoftwareversions/main.nf:31:9`: Variable was declared but not used

  ```nextflow
      def args = task.ext.args ?: ''
          ^^^^
  ```

- Warning: `modules/nf-core/unzip/main.nf:38:9`: Variable was declared but not used

  ```nextflow
      def args = task.ext.args ?: ''
          ^^^^
  ```

- Warning: `subworkflows/local/model_testing/main.nf:63:31`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
                          .map{ model_class, model_name, rand_file -> [model_name, rand_file] }
                                ^^^^^^^^^^^
  ```

- Warning: `subworkflows/local/model_testing/main.nf:125:36`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
                              .map { model_class, model_name, train_ds, val_ds, es_ds ->
                                     ^^^^^^^^^^^
  ```

- Warning: `subworkflows/local/model_testing/main.nf:145:47`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
                              .map{ model_name, final_constant, test_mode, best_hpam_combi ->
                                                ^^^^^^^^^^^^^^
  ```

- Warning: `subworkflows/local/model_testing/main.nf:158:49`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
                          .map{ test_mode, model, pred_file -> [test_mode, model.split("\\.")[0]] }
                                                  ^^^^^^^^^
  ```

- Warning: `subworkflows/local/run_cv/main.nf:54:43`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
                                  .filter { dataset_name, dataset_path ->
                                            ^^^^^^^^^^^^
  ```

- Warning: `subworkflows/local/run_cv/main.nf:57:40`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
                                  .map { dataset_name, dataset_path ->
                                         ^^^^^^^^^^^^
  ```

- Warning: `subworkflows/local/run_cv/main.nf:62:43`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
                                  .filter { dataset_name, dataset_path ->
                                            ^^^^^^^^^^^^
  ```

- Warning: `subworkflows/local/run_cv/main.nf:131:16`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          .map { model_class, model_name, hpam_combis -> [model_name, hpam_combis] }
                 ^^^^^^^^^^^
  ```

- Warning: `subworkflows/local/run_cv/main.nf:139:16`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          .map { model_class, model_name, test_mode, split -> [model_name, test_mode, split] }
                 ^^^^^^^^^^^
  ```

- Warning: `subworkflows/local/utils_nfcore_drugresponseeval_pipeline/main.nf:32:5`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
      monochrome_logs         // boolean: Do not use coloured log outputs
      ^^^^^^^^^^^^^^^
  ```

- Warning: `subworkflows/local/utils_nfcore_drugresponseeval_pipeline/main.nf:129:58`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
      ch_models = channel.from(models.split(',').collect { it.trim() })
                                                           ^^
  ```

- Warning: `workflows/drugresponseeval.nf:24:5`: Variable was declared but not used

  ```nextflow
  def test_modes = params.test_mode.split(",")
      ^^^^^^^^^^
  ```

- Warning: `workflows/drugresponseeval.nf:25:5`: Variable was declared but not used

  ```nextflow
  def randomizations = params.randomization_mode.split(",")
      ^^^^^^^^^^^^^^
  ```

- Warning: `workflows/drugresponseeval.nf:96:17`: Variable was declared but not used

  ```nextflow
          ).set { ch_collated_versions }
                  ^^^^^^^^^^^^^^^^^^^^
  ```
