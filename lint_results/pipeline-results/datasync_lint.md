# Nextflow lint results

- Generated: 2026-09-10T00:18:26.833651836Z
- Nextflow version: 26.08.0-edge
- Summary: 4 warnings

## :warning: Warnings

- Warning: `subworkflows/local/utils_nfcore_datasync_pipeline/main.nf:177:43`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
      def requires_download = samples.any { meta, input_path, output_path, md5, sha ->
                                            ^^^^
  ```

- Warning: `subworkflows/local/utils_nfcore_datasync_pipeline/main.nf:177:61`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
      def requires_download = samples.any { meta, input_path, output_path, md5, sha ->
                                                              ^^^^^^^^^^^
  ```

- Warning: `subworkflows/local/utils_nfcore_datasync_pipeline/main.nf:177:74`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
      def requires_download = samples.any { meta, input_path, output_path, md5, sha ->
                                                                           ^^^
  ```

- Warning: `workflows/datasync.nf:119:23`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
              .filter { it != null }
                        ^^
  ```
