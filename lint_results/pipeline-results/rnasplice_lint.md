# Nextflow lint results

- Generated: 2026-09-09T00:22:14.576402066Z
- Nextflow version: 26.08.0-edge
- Summary: 14 errors, 17 warnings

## :x: Errors

- Error: `modules/local/splitfiles/main.nf:40:28`: Unexpected character: '$'

  ```nextflow
          suppa_split_file: "$(Rscript --version 2>&1 | sed -n '1p' | sed 's/.*version //; s/ (.*//')"
                             ^
  ```

- Error: `subworkflows/local/suppa/main.nf:11:1`: Module could not be parsed: '/home/runner/work/strict-syntax-health/strict-syntax-health/pipelines/rnasplice/modules/local/splitfiles/main.nf'

  ```nextflow
  include { SPLIT_FILES as SPLIT_FILES_TPM                   } from '../../../modules/local/splitfiles'
  ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  ```

- Error: `subworkflows/local/suppa/main.nf:12:1`: Module could not be parsed: '/home/runner/work/strict-syntax-health/strict-syntax-health/pipelines/rnasplice/modules/local/splitfiles/main.nf'

  ```nextflow
  include { SPLIT_FILES as SPLIT_FILES_IOE                   } from '../../../modules/local/splitfiles'
  ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  ```

- Error: `subworkflows/local/suppa/main.nf:13:1`: Module could not be parsed: '/home/runner/work/strict-syntax-health/strict-syntax-health/pipelines/rnasplice/modules/local/splitfiles/main.nf'

  ```nextflow
  include { SPLIT_FILES as SPLIT_FILES_IOI                   } from '../../../modules/local/splitfiles'
  ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  ```

- Error: `subworkflows/local/suppa/main.nf:66:5`: `SPLIT_FILES_TPM` is not defined

  ```nextflow
      SPLIT_FILES_TPM (
      ^^^^^^^^^^^^^^^
  ```

- Error: `subworkflows/local/suppa/main.nf:73:21`: `SPLIT_FILES_TPM` is not defined

  ```nextflow
      ch_split_tpms = SPLIT_FILES_TPM.out.tpms
                      ^^^^^^^^^^^^^^^
  ```

- Error: `subworkflows/local/suppa/main.nf:115:9`: `SPLIT_FILES_IOE` is not defined

  ```nextflow
          SPLIT_FILES_IOE (
          ^^^^^^^^^^^^^^^
  ```

- Error: `subworkflows/local/suppa/main.nf:122:31`: `SPLIT_FILES_IOE` is not defined

  ```nextflow
          ch_split_events_psi = SPLIT_FILES_IOE.out.psis
                                ^^^^^^^^^^^^^^^
  ```

- Error: `subworkflows/local/suppa/main.nf:134:13`: `SPLIT_FILES_TPM` is not defined

  ```nextflow
              SPLIT_FILES_TPM.out.tpms
              ^^^^^^^^^^^^^^^
  ```

- Error: `subworkflows/local/suppa/main.nf:155:13`: `SPLIT_FILES_IOE` is not defined

  ```nextflow
              SPLIT_FILES_IOE.out.psis
              ^^^^^^^^^^^^^^^
  ```

- Error: `subworkflows/local/suppa/main.nf:298:9`: `SPLIT_FILES_IOI` is not defined

  ```nextflow
          SPLIT_FILES_IOI (
          ^^^^^^^^^^^^^^^
  ```

- Error: `subworkflows/local/suppa/main.nf:305:32`: `SPLIT_FILES_IOI` is not defined

  ```nextflow
          ch_split_isoform_psi = SPLIT_FILES_IOI.out.psis
                                 ^^^^^^^^^^^^^^^
  ```

- Error: `subworkflows/local/suppa/main.nf:317:13`: `SPLIT_FILES_TPM` is not defined

  ```nextflow
              SPLIT_FILES_TPM.out.tpms
              ^^^^^^^^^^^^^^^
  ```

- Error: `subworkflows/local/suppa/main.nf:338:13`: `SPLIT_FILES_IOI` is not defined

  ```nextflow
              SPLIT_FILES_IOI.out.psis
              ^^^^^^^^^^^^^^^
  ```

## :warning: Warnings

- Warning: `conf/modules.config:321:23`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
              saveAs: { filename -> null }
                        ^^^^^^^^
  ```

- Warning: `conf/modules.config:330:23`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
              saveAs: { filename -> null }
                        ^^^^^^^^
  ```

- Warning: `conf/modules.config:339:23`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
              saveAs: { filename -> null }
                        ^^^^^^^^
  ```

- Warning: `conf/modules.config:348:23`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
              saveAs: { filename -> null }
                        ^^^^^^^^
  ```

- Warning: `conf/modules.config:370:23`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
              saveAs: { filename -> null }
                        ^^^^^^^^
  ```

- Warning: `modules/local/mergeevents/main.nf:21:9`: Variable was declared but not used

  ```nextflow
      def args = task.ext.args ?: ''
          ^^^^
  ```

- Warning: `modules/local/misopysettings/main.nf:26:9`: Variable was declared but not used

  ```nextflow
      def prefix = task.ext.prefix ?: "${meta.id}"
          ^^^^^^
  ```

- Warning: `modules/local/tximeta/tximport/main.nf:50:9`: Variable was declared but not used

  ```nextflow
      def prefix            = task.ext.prefix ?: meta.id
          ^^^^^^
  ```

- Warning: `modules/local/tximeta/tximport/main.nf:51:9`: Variable was declared but not used

  ```nextflow
      def ignore_tx_version = task.ext.args ?: 'false'
          ^^^^^^^^^^^^^^^^^
  ```

- Warning: `modules/nf-core/misopy/index/main.nf:23:9`: Variable was declared but not used

  ```nextflow
      def prefix = task.ext.prefix ?: "${meta.id}"
          ^^^^^^
  ```

- Warning: `subworkflows/local/utils_nfcore_rnasplice_pipeline/main.nf:493:22`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          .map { meta, fastq -> meta.single_end }
                       ^^^^^
  ```

- Warning: `subworkflows/local/utils_nfcore_rnasplice_pipeline/main.nf:497:17`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
              if (it.size() > 1) {
                  ^^
  ```

- Warning: `subworkflows/local/utils_nfcore_rnasplice_pipeline/main.nf:508:22`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          .map { meta, fastq -> meta.strandedness }
                       ^^^^^
  ```

- Warning: `subworkflows/local/utils_nfcore_rnasplice_pipeline/main.nf:512:17`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
              if (it.size() > 1) {
                  ^^
  ```

- Warning: `workflows/rnasplice.nf:92:20`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          .flatMap { it }
                     ^^
  ```

- Warning: `workflows/rnasplice.nf:93:16`: Variable was declared but not used

  ```nextflow
          .set { ch_contrasts }
                 ^^^^^^^^^^^^
  ```

- Warning: `workflows/rnasplice.nf:184:9`: Variable was declared but not used

  ```nextflow
          ch_transcriptome_bam_index = BAM_SORT_STATS_SAMTOOLS.out.index
          ^^^^^^^^^^^^^^^^^^^^^^^^^^
  ```
