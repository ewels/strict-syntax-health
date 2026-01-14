# Nextflow lint results

- Generated: 2026-01-14T09:23:14.134393210Z
- Nextflow version: 25.12.0-edge
- Summary: 21 errors, 43 warnings

## :x: Errors

- Error: `modules/local/force-higher_level/main.nf:53:5`: Unexpected input: 'def'

  ```nextflow
      def outputOptions      = task.ext.args?["FILE_OUTPUT_OPTIONS"]   ? "FILE_OUTPUT_OPTIONS = ${task.ext.args["FILE_OUTPUT_OPTIONS"]}"     : "FILE_OUTPUT_OPTIONS = NULL"
      ^
  ```

- Error: `modules/local/force-preprocess/main.nf:59:5`: Unexpected input: 'def'

  ```nextflow
      def doReproj      = task.ext.args?["DO_REPROJ"]              ? "DO_REPROJ = ${task.ext.args["DO_REPROJ"]}"                         : "DO_REPROJ = TRUE"
      ^
  ```

- Error: `subworkflows/local/higher_level/main.nf:1:1`: Module could not be parsed: '/home/runner/work/strict-syntax-health/strict-syntax-health/pipelines/rangeland/modules/local/force-higher_level/main.nf'

  ```nextflow
  include { FORCE_HIGHER_LEVEL }  from '../../../modules/local/force-higher_level/main'
  ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  ```

- Error: `subworkflows/local/higher_level/main.nf:24:9`: `FORCE_HIGHER_LEVEL` is not defined

  ```nextflow
          FORCE_HIGHER_LEVEL(
          ^^^^^^^^^^^^^^^^^^
  ```

- Error: `subworkflows/local/higher_level/main.nf:35:39`: `FORCE_HIGHER_LEVEL` is not defined

  ```nextflow
          ch_versions = ch_versions.mix(FORCE_HIGHER_LEVEL.out.versions.first())
                                        ^^^^^^^^^^^^^^^^^^
  ```

- Error: `subworkflows/local/higher_level/main.nf:38:31`: `FORCE_HIGHER_LEVEL` is not defined

  ```nextflow
          trend_files_pyramid = FORCE_HIGHER_LEVEL.out.trend_files
                                ^^^^^^^^^^^^^^^^^^
  ```

- Error: `subworkflows/local/higher_level/main.nf:51:30`: `FORCE_HIGHER_LEVEL` is not defined

  ```nextflow
          trend_files_mosaic = FORCE_HIGHER_LEVEL.out.trend_files
                               ^^^^^^^^^^^^^^^^^^
  ```

- Error: `subworkflows/local/higher_level/main.nf:78:20`: `FORCE_HIGHER_LEVEL` is not defined

  ```nextflow
          trends   = FORCE_HIGHER_LEVEL.out.trend_files
                     ^^^^^^^^^^^^^^^^^^
  ```

- Error: `subworkflows/local/preprocessing/main.nf:3:1`: Module could not be parsed: '/home/runner/work/strict-syntax-health/strict-syntax-health/pipelines/rangeland/modules/local/force-preprocess/main.nf'

  ```nextflow
  include { FORCE_PREPROCESS }                       from '../../../modules/local/force-preprocess/main'
  ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  ```

- Error: `subworkflows/local/preprocessing/main.nf:28:29`: `extractDirectory` is not defined

  ```nextflow
                  def id = "${extractDirectory(path)}_${path.simpleName}"
                              ^^^^^^^^^^^^^^^^
  ```

- Error: `subworkflows/local/preprocessing/main.nf:52:82`: `extractDirectory` is not defined

  ```nextflow
          masks = FORCE_GENERATE_ANALYSIS_MASK.out.masks.flatten().map{ x -> [ [id:extractDirectory(x)], x ] }
                                                                                   ^^^^^^^^^^^^^^^^
  ```

- Error: `subworkflows/local/preprocessing/main.nf:55:9`: `FORCE_PREPROCESS` is not defined

  ```nextflow
          FORCE_PREPROCESS( data, cube_file, FORCE_GENERATE_TILE_ALLOW_LIST.out.tile_allow, dem, wvdb, aoi_file, aod, coreg )
          ^^^^^^^^^^^^^^^^
  ```

- Error: `subworkflows/local/preprocessing/main.nf:56:39`: `FORCE_PREPROCESS` is not defined

  ```nextflow
          ch_versions = ch_versions.mix(FORCE_PREPROCESS.out.versions.first())
                                        ^^^^^^^^^^^^^^^^
  ```

- Error: `subworkflows/local/preprocessing/main.nf:59:21`: `extractTile` is not defined

  ```nextflow
          boa_tiles = extractTile(FORCE_PREPROCESS.out.boa_tiles)
                      ^^^^^^^^^^^
  ```

- Error: `subworkflows/local/preprocessing/main.nf:59:33`: `FORCE_PREPROCESS` is not defined

  ```nextflow
          boa_tiles = extractTile(FORCE_PREPROCESS.out.boa_tiles)
                                  ^^^^^^^^^^^^^^^^
  ```

- Error: `subworkflows/local/preprocessing/main.nf:60:21`: `extractTile` is not defined

  ```nextflow
          qai_tiles = extractTile(FORCE_PREPROCESS.out.qai_tiles)
                      ^^^^^^^^^^^
  ```

- Error: `subworkflows/local/preprocessing/main.nf:60:33`: `FORCE_PREPROCESS` is not defined

  ```nextflow
          qai_tiles = extractTile(FORCE_PREPROCESS.out.qai_tiles)
                                  ^^^^^^^^^^^^^^^^
  ```

- Error: `subworkflows/local/preprocessing/main.nf:67:30`: `groupForMerge` is not defined

  ```nextflow
          boa_tiles_to_merge = groupForMerge(boa_tiles)
                               ^^^^^^^^^^^^^
  ```

- Error: `subworkflows/local/preprocessing/main.nf:68:30`: `groupForMerge` is not defined

  ```nextflow
          qai_tiles_to_merge = groupForMerge(qai_tiles)
                               ^^^^^^^^^^^^^
  ```

- Error: `workflows/rangeland.nf:114:23`: `initMetaMap` is not defined

  ```nextflow
      .map{ it -> tuple(initMetaMap(it), it) }
                        ^^^^^^^^^^^
  ```

- Error: `workflows/rangeland.nf:115:27`: `inRegion` is not defined

  ```nextflow
      .filter{ meta, _it -> inRegion(meta) }
                            ^^^^^^^^
  ```

## :warning: Warnings

- Warning: `conf/modules.config:52:46`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
                  saveAs:  { params.save_ard ? it : null },
                                               ^^
  ```

- Warning: `conf/modules.config:70:61`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
                  saveAs:  { params.save_tsa ? "trend_files/${it.tokenize('/')[-1]}" : null },
                                                              ^^
  ```

- Warning: `conf/modules.config:87:59`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
              saveAs:  { "${meta.product}/trend/${task.tag}/$it" },
                                                            ^^
  ```

- Warning: `subworkflows/local/preprocessing/main.nf:22:13`: Variable was declared but not used

  ```nextflow
          def extractDirectory = { it.parent.toString().substring(it.parent.toString().lastIndexOf('/') + 1 ) }
              ^^^^^^^^^^^^^^^^
  ```

- Warning: `subworkflows/local/preprocessing/main.nf:22:34`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          def extractDirectory = { it.parent.toString().substring(it.parent.toString().lastIndexOf('/') + 1 ) }
                                   ^^
  ```

- Warning: `subworkflows/local/preprocessing/main.nf:22:65`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          def extractDirectory = { it.parent.toString().substring(it.parent.toString().lastIndexOf('/') + 1 ) }
                                                                  ^^
  ```

- Warning: `subworkflows/local/preprocessing/main.nf:25:13`: Variable was declared but not used

  ```nextflow
          def extractTile = { ch ->
              ^^^^^^^^^^^
  ```

- Warning: `subworkflows/local/preprocessing/main.nf:26:26`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
              ch.flatMap { it[1] } // strip meta map for now, will be reintroduced after merging
                           ^^
  ```

- Warning: `subworkflows/local/preprocessing/main.nf:34:13`: Variable was declared but not used

  ```nextflow
          def groupForMerge = { ch ->
              ^^^^^^^^^^^^^
  ```

- Warning: `subworkflows/local/preprocessing/main.nf:36:25`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
                  .map{ [ it[0].substring( 0, 11 ), it[1] ] }
                          ^^
  ```

- Warning: `subworkflows/local/preprocessing/main.nf:36:51`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
                  .map{ [ it[0].substring( 0, 11 ), it[1] ] }
                                                    ^^
  ```

- Warning: `subworkflows/local/preprocessing/main.nf:39:26`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
                  .flatMap{it}
                           ^^
  ```

- Warning: `subworkflows/local/preprocessing/main.nf:40:75`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
                  .groupTuple( remainder : true, size : group_size ).map{ [ it[0], it[1].flatten() ] }
                                                                            ^^
  ```

- Warning: `subworkflows/local/preprocessing/main.nf:40:82`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
                  .groupTuple( remainder : true, size : group_size ).map{ [ it[0], it[1].flatten() ] }
                                                                                   ^^
  ```

- Warning: `subworkflows/local/preprocessing/main.nf:83:37`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
                          .map { [[id:it[0]], it[1].flatten() ] }
                                      ^^
  ```

- Warning: `subworkflows/local/preprocessing/main.nf:83:45`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
                          .map { [[id:it[0]], it[1].flatten() ] }
                                              ^^
  ```

- Warning: `subworkflows/local/preprocessing/main.nf:86:37`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
                          .map { [[id:it[0]], it[1].flatten() ] }
                                      ^^
  ```

- Warning: `subworkflows/local/preprocessing/main.nf:86:45`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
                          .map { [[id:it[0]], it[1].flatten() ] }
                                              ^^
  ```

- Warning: `subworkflows/local/utils_nfcore_rangeland_pipeline/main.nf:32:5`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
      monochrome_logs   // boolean: Do not use coloured log outputs
      ^^^^^^^^^^^^^^^
  ```

- Warning: `subworkflows/local/utils_nfcore_rangeland_pipeline/main.nf:35:5`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
      input             //  string: Path to input samplesheet
      ^^^^^
  ```

- Warning: `workflows/rangeland.nf:47:9`: Variable was declared but not used

  ```nextflow
      def inRegion = { meta ->
          ^^^^^^^^
  ```

- Warning: `workflows/rangeland.nf:60:9`: Variable was declared but not used

  ```nextflow
      def initMetaMap = {
          ^^^^^^^^^^^
  ```

- Warning: `workflows/rangeland.nf:61:30`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          String id          = it.simpleName
                               ^^
  ```

- Warning: `workflows/rangeland.nf:95:23`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
      ch_input.branch { it
                        ^^
  ```

- Warning: `workflows/rangeland.nf:96:20`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          archives : it.name.endsWith('tar') || it.name.endsWith('tar.gz')
                     ^^
  ```

- Warning: `workflows/rangeland.nf:96:47`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          archives : it.name.endsWith('tar') || it.name.endsWith('tar.gz')
                                                ^^
  ```

- Warning: `workflows/rangeland.nf:97:31`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
              return tuple([:], it)
                                ^^
  ```

- Warning: `workflows/rangeland.nf:99:20`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
              return it
                     ^^
  ```

- Warning: `workflows/rangeland.nf:104:52`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
      ch_untared_inputs = UNTAR_INPUT.out.untar.map{ it[1] }
                                                     ^^
  ```

- Warning: `workflows/rangeland.nf:123:21`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
      ch_dem.branch { it
                      ^^
  ```

- Warning: `workflows/rangeland.nf:124:20`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          archives : it.name.endsWith('tar') || it.name.endsWith('tar.gz')
                     ^^
  ```

- Warning: `workflows/rangeland.nf:124:47`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          archives : it.name.endsWith('tar') || it.name.endsWith('tar.gz')
                                                ^^
  ```

- Warning: `workflows/rangeland.nf:125:31`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
              return tuple([:], it)
                                ^^
  ```

- Warning: `workflows/rangeland.nf:127:25`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
              return file(it)
                          ^^
  ```

- Warning: `workflows/rangeland.nf:132:47`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
      ch_untared_dem = UNTAR_DEM.out.untar.map{ it[1] }
                                                ^^
  ```

- Warning: `workflows/rangeland.nf:139:22`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
      ch_wvdb.branch { it
                       ^^
  ```

- Warning: `workflows/rangeland.nf:140:20`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          archives : it.name.endsWith('tar') || it.name.endsWith('tar.gz')
                     ^^
  ```

- Warning: `workflows/rangeland.nf:140:47`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          archives : it.name.endsWith('tar') || it.name.endsWith('tar.gz')
                                                ^^
  ```

- Warning: `workflows/rangeland.nf:141:31`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
              return tuple([:], it)
                                ^^
  ```

- Warning: `workflows/rangeland.nf:143:25`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
              return file(it)
                          ^^
  ```

- Warning: `workflows/rangeland.nf:148:49`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
      ch_untared_wvdb = UNTAR_WVDB.out.untar.map{ it[1] }
                                                  ^^
  ```

- Warning: `workflows/rangeland.nf:188:5`: Variable was declared but not used

  ```nextflow
      grouped_trend_data = HIGHER_LEVEL.out.mosaic.map{ it[1] }.flatten().buffer( size: Integer.MAX_VALUE, remainder: true )
      ^^^^^^^^^^^^^^^^^^
  ```

- Warning: `workflows/rangeland.nf:188:55`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
      grouped_trend_data = HIGHER_LEVEL.out.mosaic.map{ it[1] }.flatten().buffer( size: Integer.MAX_VALUE, remainder: true )
                                                        ^^
  ```
