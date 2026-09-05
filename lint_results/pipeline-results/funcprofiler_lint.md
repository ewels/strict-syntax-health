# Nextflow lint results

- Generated: 2026-09-05T00:18:45.339977139Z
- Nextflow version: 26.08.0-edge
- Summary: 12 warnings

## :warning: Warnings

- Warning: `modules/local/humann4/regroup/main.nf:45:9`: Variable was declared but not used

  ```nextflow
      def args = task.ext.args ?: ''
          ^^^^
  ```

- Warning: `modules/local/humann4/renorm/main.nf:39:9`: Variable was declared but not used

  ```nextflow
      def args = task.ext.args ?: ''
          ^^^^
  ```

- Warning: `modules/nf-core/humann3/renorm/main.nf:42:9`: Variable was declared but not used

  ```nextflow
      def args = task.ext.args ?: ''
          ^^^^
  ```

- Warning: `subworkflows/local/dbprep/main.nf:18:43`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
      ch_dbs_for_untar = databases.branch { db_meta, db_path ->
                                            ^^^^^^^
  ```

- Warning: `subworkflows/local/dbprep/main.nf:25:28`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          .filter { db_meta, db_path ->
                             ^^^^^^^
  ```

- Warning: `subworkflows/local/profile/main.nf:207:28`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          .filter { meta_db, file ->
                             ^^^^
  ```

- Warning: `subworkflows/local/utils_nfcore_funcprofiler_pipeline/main.nf:30:5`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
      monochrome_logs // boolean: Do not use coloured log outputs
      ^^^^^^^^^^^^^^^
  ```

- Warning: `subworkflows/local/utils_nfcore_funcprofiler_pipeline/main.nf:33:5`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
      input //  string: Path to input samplesheet
      ^^^^^
  ```

- Warning: `subworkflows/local/utils_nfcore_funcprofiler_pipeline/main.nf:34:5`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
      databases //  string: Path to databases
      ^^^^^^^^^
  ```

- Warning: `subworkflows/local/utils_nfcore_funcprofiler_pipeline/main.nf:139:5`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
      hook_url //  string: hook URL for notifications
      ^^^^^^^^
  ```

- Warning: `workflows/funcprofiler.nf:32:19`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_versions = Channel.empty()
                    ^^^^^^^
  ```

- Warning: `workflows/funcprofiler.nf:33:24`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_multiqc_files = Channel.empty()
                         ^^^^^^^
  ```
