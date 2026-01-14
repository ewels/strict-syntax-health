# Nextflow lint results

- Generated: 2026-01-14T09:20:03.815766382Z
- Nextflow version: 25.12.0-edge
- Summary: 44 errors, 84 warnings

## :x: Errors

- Error: `conf/base.config:14:16`: `check_max` is not defined

  ```nextflow
      cpus   = { check_max( 1    * task.attempt, 'cpus'   ) }
                 ^^^^^^^^^
  ```

- Error: `conf/base.config:15:16`: `check_max` is not defined

  ```nextflow
      memory = { check_max( 6.GB * task.attempt, 'memory' ) }
                 ^^^^^^^^^
  ```

- Error: `conf/base.config:16:16`: `check_max` is not defined

  ```nextflow
      time   = { check_max( 4.h  * task.attempt, 'time'   ) }
                 ^^^^^^^^^
  ```

- Error: `conf/base.config:30:20`: `check_max` is not defined

  ```nextflow
          cpus   = { check_max( 1                  , 'cpus'    ) }
                     ^^^^^^^^^
  ```

- Error: `conf/base.config:31:20`: `check_max` is not defined

  ```nextflow
          memory = { check_max( 6.GB * task.attempt, 'memory'  ) }
                     ^^^^^^^^^
  ```

- Error: `conf/base.config:32:20`: `check_max` is not defined

  ```nextflow
          time   = { check_max( 4.h  * task.attempt, 'time'    ) }
                     ^^^^^^^^^
  ```

- Error: `conf/base.config:35:20`: `check_max` is not defined

  ```nextflow
          cpus   = { check_max( 1                  , 'cpus'    ) }
                     ^^^^^^^^^
  ```

- Error: `conf/base.config:36:20`: `check_max` is not defined

  ```nextflow
          memory = { check_max( 6.GB * task.attempt, 'memory'  ) }
                     ^^^^^^^^^
  ```

- Error: `conf/base.config:37:20`: `check_max` is not defined

  ```nextflow
          time   = { check_max( 4.h  * task.attempt, 'time'    ) }
                     ^^^^^^^^^
  ```

- Error: `conf/base.config:40:20`: `check_max` is not defined

  ```nextflow
          cpus   = { check_max( 2     * task.attempt, 'cpus'    ) }
                     ^^^^^^^^^
  ```

- Error: `conf/base.config:41:20`: `check_max` is not defined

  ```nextflow
          memory = { check_max( 12.GB * task.attempt, 'memory'  ) }
                     ^^^^^^^^^
  ```

- Error: `conf/base.config:42:20`: `check_max` is not defined

  ```nextflow
          time   = { check_max( 4.h   * task.attempt, 'time'    ) }
                     ^^^^^^^^^
  ```

- Error: `conf/base.config:45:20`: `check_max` is not defined

  ```nextflow
          cpus   = { check_max( 6     * task.attempt, 'cpus'    ) }
                     ^^^^^^^^^
  ```

- Error: `conf/base.config:46:20`: `check_max` is not defined

  ```nextflow
          memory = { check_max( 36.GB * task.attempt, 'memory'  ) }
                     ^^^^^^^^^
  ```

- Error: `conf/base.config:47:20`: `check_max` is not defined

  ```nextflow
          time   = { check_max( 8.h   * task.attempt, 'time'    ) }
                     ^^^^^^^^^
  ```

- Error: `conf/base.config:50:20`: `check_max` is not defined

  ```nextflow
          cpus   = { check_max( 12    * task.attempt, 'cpus'    ) }
                     ^^^^^^^^^
  ```

- Error: `conf/base.config:51:20`: `check_max` is not defined

  ```nextflow
          memory = { check_max( 72.GB * task.attempt, 'memory'  ) }
                     ^^^^^^^^^
  ```

- Error: `conf/base.config:52:20`: `check_max` is not defined

  ```nextflow
          time   = { check_max( 16.h  * task.attempt, 'time'    ) }
                     ^^^^^^^^^
  ```

- Error: `conf/base.config:55:20`: `check_max` is not defined

  ```nextflow
          time   = { check_max( 20.h  * task.attempt, 'time'    ) }
                     ^^^^^^^^^
  ```

- Error: `conf/base.config:58:20`: `check_max` is not defined

  ```nextflow
          memory = { check_max( 200.GB * task.attempt, 'memory' ) }
                     ^^^^^^^^^
  ```

- Error: `modules/local/grab_all_pairs.nf:66:40`: `meta` is not defined

  ```nextflow
      def prefix = task.ext.prefix ?: "${meta.id}"
                                         ^^^^
  ```

- Error: `modules/local/psradd_calibrate_clean.nf:22:167`: `SNR` is not defined

  ```nextflow
      tuple val(meta), path(ephemeris), path(template), path("${meta.pulsar}_${meta.utc}_raw*.ar", includeInputs: true), path("${meta.pulsar}_${meta.utc}_zap.ar"), env(SNR), env(FLUX)
                                                                                                                                                                        ^^^
  ```

- Error: `modules/local/psradd_calibrate_clean.nf:22:177`: `FLUX` is not defined

  ```nextflow
      tuple val(meta), path(ephemeris), path(template), path("${meta.pulsar}_${meta.utc}_raw*.ar", includeInputs: true), path("${meta.pulsar}_${meta.utc}_zap.ar"), env(SNR), env(FLUX)
                                                                                                                                                                                  ^^^^
  ```

- Error: `nextflow.config:111:5`: Unexpected input: 'includeConfig'

  ```nextflow
      includeConfig "${params.custom_config_base}/nfcore_custom.config"
      ^
  ```

- Error: `subworkflows/local/utils_nfcore_meerpipe_pipeline/main.nf:14:1`: Module could not be parsed: '/home/runner/work/strict-syntax-health/strict-syntax-health/pipelines/meerpipe/subworkflows/nf-core/utils_nextflow_pipeline/main.nf'

  ```nextflow
  include { UTILS_NEXTFLOW_PIPELINE   } from '../../nf-core/utils_nextflow_pipeline'
  ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  ```

- Error: `subworkflows/local/utils_nfcore_meerpipe_pipeline/main.nf:15:1`: Module could not be parsed: '/home/runner/work/strict-syntax-health/strict-syntax-health/pipelines/meerpipe/subworkflows/nf-core/utils_nfcore_pipeline/main.nf'

  ```nextflow
  include { completionEmail           } from '../../nf-core/utils_nfcore_pipeline'
  ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  ```

- Error: `subworkflows/local/utils_nfcore_meerpipe_pipeline/main.nf:16:1`: Module could not be parsed: '/home/runner/work/strict-syntax-health/strict-syntax-health/pipelines/meerpipe/subworkflows/nf-core/utils_nfcore_pipeline/main.nf'

  ```nextflow
  include { completionSummary         } from '../../nf-core/utils_nfcore_pipeline'
  ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  ```

- Error: `subworkflows/local/utils_nfcore_meerpipe_pipeline/main.nf:17:1`: Module could not be parsed: '/home/runner/work/strict-syntax-health/strict-syntax-health/pipelines/meerpipe/subworkflows/nf-core/utils_nfcore_pipeline/main.nf'

  ```nextflow
  include { dashedLine                } from '../../nf-core/utils_nfcore_pipeline'
  ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  ```

- Error: `subworkflows/local/utils_nfcore_meerpipe_pipeline/main.nf:18:1`: Module could not be parsed: '/home/runner/work/strict-syntax-health/strict-syntax-health/pipelines/meerpipe/subworkflows/nf-core/utils_nfcore_pipeline/main.nf'

  ```nextflow
  include { nfCoreLogo                } from '../../nf-core/utils_nfcore_pipeline'
  ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  ```

- Error: `subworkflows/local/utils_nfcore_meerpipe_pipeline/main.nf:19:1`: Module could not be parsed: '/home/runner/work/strict-syntax-health/strict-syntax-health/pipelines/meerpipe/subworkflows/nf-core/utils_nfcore_pipeline/main.nf'

  ```nextflow
  include { imNotification            } from '../../nf-core/utils_nfcore_pipeline'
  ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  ```

- Error: `subworkflows/local/utils_nfcore_meerpipe_pipeline/main.nf:20:1`: Module could not be parsed: '/home/runner/work/strict-syntax-health/strict-syntax-health/pipelines/meerpipe/subworkflows/nf-core/utils_nfcore_pipeline/main.nf'

  ```nextflow
  include { UTILS_NFCORE_PIPELINE     } from '../../nf-core/utils_nfcore_pipeline'
  ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  ```

- Error: `subworkflows/local/utils_nfcore_meerpipe_pipeline/main.nf:21:1`: Module could not be parsed: '/home/runner/work/strict-syntax-health/strict-syntax-health/pipelines/meerpipe/subworkflows/nf-core/utils_nfcore_pipeline/main.nf'

  ```nextflow
  include { workflowCitation          } from '../../nf-core/utils_nfcore_pipeline'
  ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  ```

- Error: `subworkflows/local/utils_nfcore_meerpipe_pipeline/main.nf:47:5`: `UTILS_NEXTFLOW_PIPELINE` is not defined

  ```nextflow
      UTILS_NEXTFLOW_PIPELINE (
      ^^^^^^^^^^^^^^^^^^^^^^^
  ```

- Error: `subworkflows/local/utils_nfcore_meerpipe_pipeline/main.nf:57:21`: `nfCoreLogo` is not defined

  ```nextflow
      pre_help_text = nfCoreLogo(monochrome_logs)
                      ^^^^^^^^^^
  ```

- Error: `subworkflows/local/utils_nfcore_meerpipe_pipeline/main.nf:58:29`: `workflowCitation` is not defined

  ```nextflow
      post_help_text = '\n' + workflowCitation() + '\n' + dashedLine(monochrome_logs)
                              ^^^^^^^^^^^^^^^^
  ```

- Error: `subworkflows/local/utils_nfcore_meerpipe_pipeline/main.nf:58:57`: `dashedLine` is not defined

  ```nextflow
      post_help_text = '\n' + workflowCitation() + '\n' + dashedLine(monochrome_logs)
                                                          ^^^^^^^^^^
  ```

- Error: `subworkflows/local/utils_nfcore_meerpipe_pipeline/main.nf:72:5`: `UTILS_NFCORE_PIPELINE` is not defined

  ```nextflow
      UTILS_NFCORE_PIPELINE (
      ^^^^^^^^^^^^^^^^^^^^^
  ```

- Error: `subworkflows/local/utils_nfcore_meerpipe_pipeline/main.nf:133:13`: `completionEmail` is not defined

  ```nextflow
              completionEmail(summary_params, email, email_on_fail, plaintext_email, outdir, monochrome_logs)
              ^^^^^^^^^^^^^^^
  ```

- Error: `subworkflows/local/utils_nfcore_meerpipe_pipeline/main.nf:136:9`: `completionSummary` is not defined

  ```nextflow
          completionSummary(monochrome_logs)
          ^^^^^^^^^^^^^^^^^
  ```

- Error: `subworkflows/local/utils_nfcore_meerpipe_pipeline/main.nf:139:13`: `imNotification` is not defined

  ```nextflow
              imNotification(summary_params, hook_url)
              ^^^^^^^^^^^^^^
  ```

- Error: `subworkflows/nf-core/utils_nextflow_pipeline/main.nf:111:14`: Unexpected input: 'i'

  ```nextflow
      for (int i = 0; i < n - 1; i++) {
               ^
  ```

- Error: `subworkflows/nf-core/utils_nfcore_pipeline/main.nf:73:17`: Unexpected input: 'doi_ref'

  ```nextflow
      for (String doi_ref: manifest_doi) temp_doi_ref += "  https://doi.org/${doi_ref.replace('https://doi.org/', '').replace(' ', '')}\n"
                  ^
  ```

- Error: `tests/nextflow.config:9:20`: `PSRDB_URL` is not defined

  ```nextflow
      psrdb_url   = "$PSRDB_URL"
                     ^^^^^^^^^^
  ```

- Error: `tests/nextflow.config:10:20`: `PSRDB_TOKEN` is not defined

  ```nextflow
      psrdb_token = "$PSRDB_TOKEN"
                     ^^^^^^^^^^^^
  ```

## :warning: Warnings

- Warning: `modules/local/decimate.nf:28:9`: Variable was declared but not used

  ```nextflow
      def args = task.ext.args ?: ''
          ^^^^
  ```

- Warning: `modules/local/decimate.nf:29:9`: Variable was declared but not used

  ```nextflow
      def prefix = task.ext.prefix ?: "${meta.id}"
          ^^^^^^
  ```

- Warning: `modules/local/decimate.nf:89:9`: Variable was declared but not used

  ```nextflow
      def args = task.ext.args ?: ''
          ^^^^
  ```

- Warning: `modules/local/decimate.nf:90:9`: Variable was declared but not used

  ```nextflow
      def prefix = task.ext.prefix ?: "${meta.id}"
          ^^^^^^
  ```

- Warning: `modules/local/dm_rm_calc.nf:24:9`: Variable was declared but not used

  ```nextflow
      def args = task.ext.args ?: ''
          ^^^^
  ```

- Warning: `modules/local/dm_rm_calc.nf:25:9`: Variable was declared but not used

  ```nextflow
      def prefix = task.ext.prefix ?: "${meta.id}"
          ^^^^^^
  ```

- Warning: `modules/local/dm_rm_calc.nf:171:9`: Variable was declared but not used

  ```nextflow
      def args = task.ext.args ?: ''
          ^^^^
  ```

- Warning: `modules/local/dm_rm_calc.nf:172:9`: Variable was declared but not used

  ```nextflow
      def prefix = task.ext.prefix ?: "${meta.id}"
          ^^^^^^
  ```

- Warning: `modules/local/generate_image_results.nf:29:9`: Variable was declared but not used

  ```nextflow
      def args = task.ext.args ?: ''
          ^^^^
  ```

- Warning: `modules/local/generate_image_results.nf:30:9`: Variable was declared but not used

  ```nextflow
      def prefix = task.ext.prefix ?: "${meta.id}"
          ^^^^^^
  ```

- Warning: `modules/local/generate_image_results.nf:105:9`: Variable was declared but not used

  ```nextflow
      def args = task.ext.args ?: ''
          ^^^^
  ```

- Warning: `modules/local/generate_residuals.nf:21:9`: Variable was declared but not used

  ```nextflow
      def args = task.ext.args ?: ''
          ^^^^
  ```

- Warning: `modules/local/generate_residuals.nf:22:9`: Variable was declared but not used

  ```nextflow
      def prefix = task.ext.prefix ?: "${meta.id}"
          ^^^^^^
  ```

- Warning: `modules/local/generate_residuals.nf:51:9`: Variable was declared but not used

  ```nextflow
      def args = task.ext.args ?: ''
          ^^^^
  ```

- Warning: `modules/local/generate_residuals.nf:52:9`: Variable was declared but not used

  ```nextflow
      def prefix = task.ext.prefix ?: "${meta.id}"
          ^^^^^^
  ```

- Warning: `modules/local/generate_toas.nf:27:9`: Variable was declared but not used

  ```nextflow
      def args = task.ext.args ?: ''
          ^^^^
  ```

- Warning: `modules/local/generate_toas.nf:28:9`: Variable was declared but not used

  ```nextflow
      def prefix = task.ext.prefix ?: "${meta.id}"
          ^^^^^^
  ```

- Warning: `modules/local/generate_toas.nf:64:9`: Variable was declared but not used

  ```nextflow
      def args = task.ext.args ?: ''
          ^^^^
  ```

- Warning: `modules/local/generate_toas.nf:65:9`: Variable was declared but not used

  ```nextflow
      def prefix = task.ext.prefix ?: "${meta.id}"
          ^^^^^^
  ```

- Warning: `modules/local/grab_all_pairs.nf:24:9`: Variable was declared but not used

  ```nextflow
      def args = task.ext.args ?: ''
          ^^^^
  ```

- Warning: `modules/local/grab_all_pairs.nf:25:9`: Variable was declared but not used

  ```nextflow
      def prefix = task.ext.prefix ?: "${pulsar}"
          ^^^^^^
  ```

- Warning: `modules/local/grab_all_pairs.nf:65:9`: Variable was declared but not used

  ```nextflow
      def args = task.ext.args ?: ''
          ^^^^
  ```

- Warning: `modules/local/grab_all_pairs.nf:66:9`: Variable was declared but not used

  ```nextflow
      def prefix = task.ext.prefix ?: "${meta.id}"
          ^^^^^^
  ```

- Warning: `modules/local/psradd_calibrate_clean.nf:28:9`: Variable was declared but not used

  ```nextflow
      def args = task.ext.args ?: ''
          ^^^^
  ```

- Warning: `modules/local/psradd_calibrate_clean.nf:29:9`: Variable was declared but not used

  ```nextflow
      def prefix = task.ext.prefix ?: "${meta.id}"
          ^^^^^^
  ```

- Warning: `modules/local/psradd_calibrate_clean.nf:186:9`: Variable was declared but not used

  ```nextflow
      def args = task.ext.args ?: ''
          ^^^^
  ```

- Warning: `modules/local/psradd_calibrate_clean.nf:187:9`: Variable was declared but not used

  ```nextflow
      def prefix = task.ext.prefix ?: "${meta.id}"
          ^^^^^^
  ```

- Warning: `modules/local/upload_dm_rm_results.nf:21:9`: Variable was declared but not used

  ```nextflow
      def args = task.ext.args ?: ''
          ^^^^
  ```

- Warning: `modules/local/upload_dm_rm_results.nf:22:9`: Variable was declared but not used

  ```nextflow
      def prefix = task.ext.prefix ?: "${meta.id}"
          ^^^^^^
  ```

- Warning: `modules/local/upload_dm_rm_results.nf:103:9`: Variable was declared but not used

  ```nextflow
      def args = task.ext.args ?: ''
          ^^^^
  ```

- Warning: `modules/local/upload_dm_rm_results.nf:104:9`: Variable was declared but not used

  ```nextflow
      def prefix = task.ext.prefix ?: "${meta.id}"
          ^^^^^^
  ```

- Warning: `modules/local/upload_results.nf:21:9`: Variable was declared but not used

  ```nextflow
      def args = task.ext.args ?: ''
          ^^^^
  ```

- Warning: `modules/local/upload_results.nf:22:9`: Variable was declared but not used

  ```nextflow
      def prefix = task.ext.prefix ?: "${meta.id}"
          ^^^^^^
  ```

- Warning: `modules/local/upload_results.nf:116:9`: Variable was declared but not used

  ```nextflow
      def args = task.ext.args ?: ''
          ^^^^
  ```

- Warning: `modules/local/upload_results.nf:117:9`: Variable was declared but not used

  ```nextflow
      def prefix = task.ext.prefix ?: "${meta.id}"
          ^^^^^^
  ```

- Warning: `modules/local/upload_toas.nf:24:9`: Variable was declared but not used

  ```nextflow
      def args = task.ext.args ?: ''
          ^^^^
  ```

- Warning: `modules/local/upload_toas.nf:25:9`: Variable was declared but not used

  ```nextflow
      def prefix = task.ext.prefix ?: "${meta.id}"
          ^^^^^^
  ```

- Warning: `modules/local/upload_toas.nf:110:9`: Variable was declared but not used

  ```nextflow
      def args = task.ext.args ?: ''
          ^^^^
  ```

- Warning: `modules/local/upload_toas.nf:111:9`: Variable was declared but not used

  ```nextflow
      def prefix = task.ext.prefix ?: "${meta.id}"
          ^^^^^^
  ```

- Warning: `subworkflows/local/utils_nfcore_meerpipe_pipeline/main.nf:38:5`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
      input             //  string: Path to input samplesheet
      ^^^^^
  ```

- Warning: `subworkflows/local/utils_nfcore_meerpipe_pipeline/main.nf:42:19`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_versions = Channel.empty()
                    ^^^^^^^
  ```

- Warning: `subworkflows/local/utils_nfcore_meerpipe_pipeline/main.nf:83:5`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      Channel
      ^^^^^^^
  ```

- Warning: `subworkflows/local/utils_nfcore_meerpipe_pipeline/main.nf:95:38`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
              validateInputSamplesheet(it)
                                       ^^
  ```

- Warning: `subworkflows/local/utils_nfcore_meerpipe_pipeline/main.nf:163:39`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
      def endedness_ok = metas.collect{ it.single_end }.unique().size == 1
                                        ^^
  ```

- Warning: `workflows/meerpipe.nf:40:19`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
          obs_csv = Channel.fromPath("none_given")
                    ^^^^^^^
  ```

- Warning: `workflows/meerpipe.nf:42:19`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
          obs_csv = Channel.fromPath(params.obs_csv)
                    ^^^^^^^
  ```

- Warning: `workflows/meerpipe.nf:74:89`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
              pulsar, utc, project_short, beam, band, dur, mode_dur, obs_nchan, obs_nbin, cal_loc, pipe_id, ephemeris, template, n_obs, snr, flux, percent_rfi_zapped, raw_archive, cleaned_archive ->
                                                                                          ^^^^^^^
  ```

- Warning: `workflows/meerpipe.nf:88:64`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
                      nchans: params.nchans.split(',').collect { it.toInteger() },
                                                                 ^^
  ```

- Warning: `workflows/meerpipe.nf:89:62`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
                      npols:params.npols.split(',').collect  { it.toInteger() },
                                                               ^^
  ```

- Warning: `workflows/meerpipe.nf:119:64`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
                      nchans: params.nchans.split(',').collect { it.toInteger() },
                                                                 ^^
  ```

- Warning: `workflows/meerpipe.nf:120:62`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
                      npols:params.npols.split(',').collect  { it.toInteger() },
                                                               ^^
  ```

- Warning: `workflows/meerpipe.nf:150:64`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
                      nchans: params.nchans.split(',').collect { it.toInteger() },
                                                                 ^^
  ```

- Warning: `workflows/meerpipe.nf:151:62`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
                      npols:params.npols.split(',').collect  { it.toInteger() },
                                                               ^^
  ```

- Warning: `workflows/meerpipe.nf:215:22`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
              .map { [ it[0] ] }
                       ^^
  ```

- Warning: `workflows/meerpipe.nf:224:19`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          .filter { it[2].baseName != "no_template" }
                    ^^
  ```

- Warning: `workflows/meerpipe.nf:227:19`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
              meta, ephemeris, template, raw_archive, cleaned_archive ->
                    ^^^^^^^^^
  ```

- Warning: `workflows/meerpipe.nf:227:40`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
              meta, ephemeris, template, raw_archive, cleaned_archive ->
                                         ^^^^^^^^^^^
  ```

- Warning: `workflows/meerpipe.nf:231:19`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          .filter { it[2].baseName == "no_template" }
                    ^^
  ```

- Warning: `workflows/meerpipe.nf:234:19`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
              meta, ephemeris, template, raw_archive, cleaned_archive ->
                    ^^^^^^^^^
  ```

- Warning: `workflows/meerpipe.nf:234:53`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
              meta, ephemeris, template, raw_archive, cleaned_archive ->
                                                      ^^^^^^^^^^^^^^^
  ```

- Warning: `workflows/meerpipe.nf:251:27`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
                  .filter { it[1].baseName != "no_template" }
                            ^^
  ```

- Warning: `workflows/meerpipe.nf:253:27`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
                      meta, template, decimated_archives ->
                            ^^^^^^^^
  ```

- Warning: `workflows/meerpipe.nf:297:21`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
                      id, meta, ephem -> [ meta[0], ephem[0] ]
                      ^^
  ```

- Warning: `workflows/only_dm_rm_calc.nf:33:19`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
          obs_csv = Channel.fromPath("none_given")
                    ^^^^^^^
  ```

- Warning: `workflows/only_dm_rm_calc.nf:35:19`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
          obs_csv = Channel.fromPath(params.obs_csv)
                    ^^^^^^^
  ```

- Warning: `workflows/only_dm_rm_calc.nf:73:85`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          pulsar, utc, project_short, beam, band, dur, mode_dur, obs_nchan, obs_nbin, cal_loc, pipe_id, ephemeris, template, n_obs, snr, flux, percent_rfi_zapped, raw_archive, cleaned_archive ->
                                                                                      ^^^^^^^
  ```

- Warning: `workflows/only_dm_rm_calc.nf:87:60`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
                  nchans: params.nchans.split(',').collect { it.toInteger() },
                                                             ^^
  ```

- Warning: `workflows/only_dm_rm_calc.nf:88:58`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
                  npols:params.npols.split(',').collect  { it.toInteger() },
                                                           ^^
  ```

- Warning: `workflows/only_dm_rm_calc.nf:108:23`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
                  meta, ephemeris, template, raw_archive, cleaned_archive, results_json, rm_image, dm_image ->
                        ^^^^^^^^^
  ```

- Warning: `workflows/only_dm_rm_calc.nf:108:34`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
                  meta, ephemeris, template, raw_archive, cleaned_archive, results_json, rm_image, dm_image ->
                                   ^^^^^^^^
  ```

- Warning: `workflows/only_dm_rm_calc.nf:108:44`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
                  meta, ephemeris, template, raw_archive, cleaned_archive, results_json, rm_image, dm_image ->
                                             ^^^^^^^^^^^
  ```

- Warning: `workflows/only_dm_rm_calc.nf:108:57`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
                  meta, ephemeris, template, raw_archive, cleaned_archive, results_json, rm_image, dm_image ->
                                                          ^^^^^^^^^^^^^^^
  ```

- Warning: `workflows/only_toas_and_residuals.nf:46:19`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
          obs_csv = Channel.fromPath("none_given")
                    ^^^^^^^
  ```

- Warning: `workflows/only_toas_and_residuals.nf:48:19`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
          obs_csv = Channel.fromPath(params.obs_csv)
                    ^^^^^^^
  ```

- Warning: `workflows/only_toas_and_residuals.nf:80:89`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
              pulsar, utc, project_short, beam, band, dur, mode_dur, obs_nchan, obs_nbin, cal_loc, pipe_id, ephemeris, template, n_obs, snr, flux, percent_rfi_zapped, raw_archive, cleaned_archive ->
                                                                                          ^^^^^^^
  ```

- Warning: `workflows/only_toas_and_residuals.nf:94:64`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
                      nchans: params.nchans.split(',').collect { it.toInteger() },
                                                                 ^^
  ```

- Warning: `workflows/only_toas_and_residuals.nf:95:62`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
                      npols:params.npols.split(',').collect  { it.toInteger() },
                                                               ^^
  ```

- Warning: `workflows/only_toas_and_residuals.nf:113:22`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
              .map { [ it[0] ] }
                       ^^
  ```

- Warning: `workflows/only_toas_and_residuals.nf:122:19`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          .filter { it[2].baseName != "no_template" }
                    ^^
  ```

- Warning: `workflows/only_toas_and_residuals.nf:125:19`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
              meta, ephemeris, template, raw_archive, cleaned_archive ->
                    ^^^^^^^^^
  ```

- Warning: `workflows/only_toas_and_residuals.nf:125:40`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
              meta, ephemeris, template, raw_archive, cleaned_archive ->
                                         ^^^^^^^^^^^
  ```

- Warning: `workflows/only_toas_and_residuals.nf:140:27`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
                  .filter { it[1].baseName != "no_template" }
                            ^^
  ```

- Warning: `workflows/only_toas_and_residuals.nf:142:27`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
                      meta, template, decimated_archives ->
                            ^^^^^^^^
  ```

- Warning: `workflows/only_toas_and_residuals.nf:186:21`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
                      id, meta, ephem -> [ meta[0], ephem[0] ]
                      ^^
  ```
