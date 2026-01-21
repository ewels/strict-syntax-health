# Nextflow lint results

- Generated: 2026-01-21T13:35:35.519465+00:00
- Nextflow version: 25.12.0-edge
- Summary: 3 warnings

## :warning: Warnings

- Warning: `subworkflows/nf-core/tiff_segmentation_vpt/main.nf:19:19`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_versions = Channel.empty()
                    ^^^^^^^^^^
  ```

- Warning: `subworkflows/nf-core/tiff_segmentation_vpt/main.nf:36:19`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          .filter { it.key == 'num_tiles' }
                    ^^^^^^^^^^
  ```

- Warning: `subworkflows/nf-core/tiff_segmentation_vpt/main.nf:37:16`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          .map { it.value.toInteger() }
                 ^^^^^^^^^^
  ```
