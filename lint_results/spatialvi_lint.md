# Nextflow lint results

- Generated: 2026-01-14T09:26:27.196871477Z
- Nextflow version: 25.12.0-edge
- Summary: 14 errors, 20 warnings

## :x: Errors

- Error: `modules/nf-core/quartonotebook/main.nf:45:5`: `yamlBuilder` is not defined

  ```nextflow
      yamlBuilder(notebook_parameters)
      ^^^^^^^^^^^
  ```

- Error: `modules/nf-core/spaceranger/count/main.nf:27:9`: `probeset` is already declared

  ```nextflow
      def probeset = probeset ? "--probe-set=\"${probeset}\"" : ""
          ^^^^^^^^
  ```

- Error: `modules/nf-core/spaceranger/count/main.nf:28:9`: `alignment` is already declared

  ```nextflow
      def alignment = alignment ? "--loupe-alignment=\"${alignment}\"" : ""
          ^^^^^^^^^
  ```

- Error: `modules/nf-core/spaceranger/count/main.nf:29:9`: `slidefile` is already declared

  ```nextflow
      def slidefile = slidefile ? "--slidefile=\"${slidefile}\"" : ""
          ^^^^^^^^^
  ```

- Error: `modules/nf-core/spaceranger/count/main.nf:30:9`: `image` is already declared

  ```nextflow
      def image = image ? "--image=\"${image}\"" : ""
          ^^^^^
  ```

- Error: `modules/nf-core/spaceranger/count/main.nf:31:9`: `cytaimage` is already declared

  ```nextflow
      def cytaimage = cytaimage ? "--cytaimage=\"${cytaimage}\"" : ""
          ^^^^^^^^^
  ```

- Error: `modules/nf-core/spaceranger/count/main.nf:32:9`: `darkimage` is already declared

  ```nextflow
      def darkimage = darkimage ? "--darkimage=\"${darkimage}\"" : ""
          ^^^^^^^^^
  ```

- Error: `modules/nf-core/spaceranger/count/main.nf:33:9`: `colorizedimage` is already declared

  ```nextflow
      def colorizedimage = colorizedimage ? "--colorizedimage=\"${colorizedimage}\"" : ""
          ^^^^^^^^^^^^^^
  ```

- Error: `subworkflows/local/input_check/main.nf:135:28`: `get_file_from_meta` is not defined

  ```nextflow
      def manual_alignment = get_file_from_meta("manual_alignment")
                             ^^^^^^^^^^^^^^^^^^
  ```

- Error: `subworkflows/local/input_check/main.nf:136:21`: `get_file_from_meta` is not defined

  ```nextflow
      def slidefile = get_file_from_meta("slidefile")
                      ^^^^^^^^^^^^^^^^^^
  ```

- Error: `subworkflows/local/input_check/main.nf:137:17`: `get_file_from_meta` is not defined

  ```nextflow
      def image = get_file_from_meta("image")
                  ^^^^^^^^^^^^^^^^^^
  ```

- Error: `subworkflows/local/input_check/main.nf:138:21`: `get_file_from_meta` is not defined

  ```nextflow
      def cytaimage = get_file_from_meta("cytaimage")
                      ^^^^^^^^^^^^^^^^^^
  ```

- Error: `subworkflows/local/input_check/main.nf:139:26`: `get_file_from_meta` is not defined

  ```nextflow
      def colorizedimage = get_file_from_meta("colorizedimage")
                           ^^^^^^^^^^^^^^^^^^
  ```

- Error: `subworkflows/local/input_check/main.nf:140:21`: `get_file_from_meta` is not defined

  ```nextflow
      def darkimage = get_file_from_meta("darkimage")
                      ^^^^^^^^^^^^^^^^^^
  ```

## :warning: Warnings

- Warning: `subworkflows/local/aggregation/main.nf:19:19`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_versions = Channel.empty()
                    ^^^^^^^
  ```

- Warning: `subworkflows/local/aggregation/main.nf:23:18`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      extensions = Channel.fromPath("${projectDir}/assets/_extensions").collect()
                   ^^^^^^^
  ```

- Warning: `subworkflows/local/aggregation/main.nf:35:23`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_merged_sdata = Channel.empty()
                        ^^^^^^^
  ```

- Warning: `subworkflows/local/aggregation/main.nf:47:27`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_integrated_sdata = Channel.empty()
                            ^^^^^^^
  ```

- Warning: `subworkflows/local/aggregation/main.nf:48:27`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_integrated_adata = Channel.empty()
                            ^^^^^^^
  ```

- Warning: `subworkflows/local/downstream/main.nf:26:19`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_versions = Channel.empty()
                    ^^^^^^^
  ```

- Warning: `subworkflows/local/downstream/main.nf:34:18`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      extensions = Channel.fromPath("${projectDir}/assets/_extensions").collect()
                   ^^^^^^^
  ```

- Warning: `subworkflows/local/input_check/main.nf:16:19`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_versions = Channel.empty()
                    ^^^^^^^
  ```

- Warning: `subworkflows/local/input_check/main.nf:18:13`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_st = Channel.fromPath(samplesheet)
              ^^^^^^^
  ```

- Warning: `subworkflows/local/input_check/main.nf:131:9`: Variable was declared but not used

  ```nextflow
      def get_file_from_meta = { k ->
          ^^^^^^^^^^^^^^^^^^
  ```

- Warning: `subworkflows/local/spaceranger/main.nf:17:19`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_versions = Channel.empty()
                    ^^^^^^^
  ```

- Warning: `subworkflows/local/spaceranger/main.nf:22:20`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_reference = Channel.empty()
                     ^^^^^^^
  ```

- Warning: `subworkflows/local/spaceranger/main.nf:38:19`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_probeset = Channel.empty()
                    ^^^^^^^
  ```

- Warning: `subworkflows/local/utils_nfcore_spatialvi_pipeline/main.nf:32:5`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
      monochrome_logs   // boolean: Do not use coloured log outputs
      ^^^^^^^^^^^^^^^
  ```

- Warning: `subworkflows/local/utils_nfcore_spatialvi_pipeline/main.nf:35:5`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
      input             //  string: Path to input samplesheet
      ^^^^^
  ```

- Warning: `workflows/spatialvi.nf:131:26`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      def topic_versions = Channel.topic("versions")
                           ^^^^^^^
  ```

- Warning: `workflows/spatialvi.nf:163:9`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
          Channel.fromPath(multiqc_config, checkIfExists: true) :
          ^^^^^^^
  ```

- Warning: `workflows/spatialvi.nf:164:9`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
          Channel.empty()
          ^^^^^^^
  ```

- Warning: `workflows/spatialvi.nf:166:9`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
          Channel.fromPath(multiqc_logo, checkIfExists: true) :
          ^^^^^^^
  ```

- Warning: `workflows/spatialvi.nf:167:9`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
          Channel.empty()
          ^^^^^^^
  ```
