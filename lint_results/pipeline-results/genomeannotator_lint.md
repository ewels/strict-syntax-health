# Nextflow lint results

- Generated: 2026-01-16T10:21:12.551179534Z
- Nextflow version: 25.12.0-edge
- Summary: 85 errors, 148 warnings

## :x: Errors

- Error: `assets/pasa/alignAssembly.config:2:1`: Unexpected character: '#'

  ```nextflow
  ## templated variables to be replaced exist as <__var_name__>
  ^
  ```

- Error: `assets/pasa/annotationCompare.config:2:1`: Unexpected character: '#'

  ```nextflow
  ## templated variables to be replaced exist as <__var_name__>
  ^
  ```

- Error: `conf/base.config:13:16`: `check_max` is not defined

  ```nextflow
      cpus   = { check_max( 1    * task.attempt, 'cpus'   ) }
                 ^^^^^^^^^
  ```

- Error: `conf/base.config:14:16`: `check_max` is not defined

  ```nextflow
      memory = { check_max( 6.GB * task.attempt, 'memory' ) }
                 ^^^^^^^^^
  ```

- Error: `conf/base.config:15:16`: `check_max` is not defined

  ```nextflow
      time   = { check_max( 4.h  * task.attempt, 'time'   ) }
                 ^^^^^^^^^
  ```

- Error: `conf/base.config:27:20`: `check_max` is not defined

  ```nextflow
          cpus   = { check_max( 2     * task.attempt, 'cpus'    ) }
                     ^^^^^^^^^
  ```

- Error: `conf/base.config:28:20`: `check_max` is not defined

  ```nextflow
          memory = { check_max( 12.GB * task.attempt, 'memory'  ) }
                     ^^^^^^^^^
  ```

- Error: `conf/base.config:29:20`: `check_max` is not defined

  ```nextflow
          time   = { check_max( 4.h   * task.attempt, 'time'    ) }
                     ^^^^^^^^^
  ```

- Error: `conf/base.config:32:20`: `check_max` is not defined

  ```nextflow
          cpus   = { check_max( 6     * task.attempt, 'cpus'    ) }
                     ^^^^^^^^^
  ```

- Error: `conf/base.config:33:20`: `check_max` is not defined

  ```nextflow
          memory = { check_max( 36.GB * task.attempt, 'memory'  ) }
                     ^^^^^^^^^
  ```

- Error: `conf/base.config:34:20`: `check_max` is not defined

  ```nextflow
          time   = { check_max( 8.h   * task.attempt, 'time'    ) }
                     ^^^^^^^^^
  ```

- Error: `conf/base.config:37:20`: `check_max` is not defined

  ```nextflow
          cpus   = { check_max( 12    * task.attempt, 'cpus'    ) }
                     ^^^^^^^^^
  ```

- Error: `conf/base.config:38:20`: `check_max` is not defined

  ```nextflow
          memory = { check_max( 72.GB * task.attempt, 'memory'  ) }
                     ^^^^^^^^^
  ```

- Error: `conf/base.config:39:20`: `check_max` is not defined

  ```nextflow
          time   = { check_max( 16.h  * task.attempt, 'time'    ) }
                     ^^^^^^^^^
  ```

- Error: `conf/base.config:42:20`: `check_max` is not defined

  ```nextflow
          time   = { check_max( 20.h  * task.attempt, 'time'    ) }
                     ^^^^^^^^^
  ```

- Error: `conf/base.config:45:20`: `check_max` is not defined

  ```nextflow
          cpus   = { check_max( 12    * task.attempt, 'cpus'    ) }
                     ^^^^^^^^^
  ```

- Error: `conf/base.config:46:20`: `check_max` is not defined

  ```nextflow
          memory = { check_max( 72.GB * task.attempt, 'memory'  ) }
                     ^^^^^^^^^
  ```

- Error: `conf/base.config:47:20`: `check_max` is not defined

  ```nextflow
          time   = { check_max( 72.h  * task.attempt, 'time'    ) }
                     ^^^^^^^^^
  ```

- Error: `conf/base.config:50:20`: `check_max` is not defined

  ```nextflow
          memory = { check_max( 200.GB * task.attempt, 'memory' ) }
                     ^^^^^^^^^
  ```

- Error: `main.nf:28:1`: Statements cannot be mixed with script declarations -- move statements into a process, workflow, or function

  ```nextflow
  WorkflowMain.initialise(workflow, params, log)
  ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  ```

- Error: `main.nf:28:1`: `WorkflowMain` is not defined

  ```nextflow
  WorkflowMain.initialise(workflow, params, log)
  ^^^^^^^^^^^^
  ```

- Error: `modules/local/augustus/augustusbatch.nf:11:9`: `AUGUSTUS_CONFIG_PATH` is not defined

  ```nextflow
      env AUGUSTUS_CONFIG_PATH
          ^^^^^^^^^^^^^^^^^^^^
  ```

- Error: `modules/local/augustus/training.nf:13:9`: `AUGUSTUS_CONFIG_PATH` is not defined

  ```nextflow
      env AUGUSTUS_CONFIG_PATH
          ^^^^^^^^^^^^^^^^^^^^
  ```

- Error: `modules/local/helper/addexons.nf:14:27`: `models` is not defined

  ```nextflow
      tuple val(meta), path(models), emit: gff
                            ^^^^^^
  ```

- Error: `modules/local/helper/pasa2training.nf:5:5`: Invalid process directive

  ```nextflow
      if (params.enable_conda) {
      ^
  ```

- Error: `modules/local/kraken.nf:5:5`: Invalid process directive

  ```nextflow
      if (params.enable_conda) {
      ^
  ```

- Error: `modules/local/pasa/alignassemble.nf:5:5`: Invalid process directive

  ```nextflow
      if (params.enable_conda) {
      ^
  ```

- Error: `modules/local/pasa/asmblstotraining.nf:5:5`: Invalid process directive

  ```nextflow
      if (params.enable_conda) {
      ^
  ```

- Error: `modules/local/pasa/seqclean.nf:5:5`: Invalid process directive

  ```nextflow
      if (params.enable_conda) {
      ^
  ```

- Error: `modules/local/repeatmasker/repeatmask.nf:12:9`: `LIBDIR` is not defined

  ```nextflow
      env LIBDIR
          ^^^^^^
  ```

- Error: `modules/local/satsuma2/satsumasynteny2.nf:5:5`: Invalid process directive

  ```nextflow
      if (params.enable_conda) {
      ^
  ```

- Error: `nextflow.config:120:5`: Unexpected input: 'includeConfig'

  ```nextflow
      includeConfig "${params.custom_config_base}/nfcore_custom.config"
      ^
  ```

- Error: `subworkflows/local/genome_align.nf:98:5`: `array` was assigned but not declared

  ```nextflow
      array = [ meta, file(row.fasta), file(row.gtf) ]
      ^^^^^
  ```

- Error: `subworkflows/local/genome_align.nf:100:12`: `array` is not defined

  ```nextflow
      return array
             ^^^^^
  ```

- Error: `workflows/genomeannotator.nf:7:1`: Statements cannot be mixed with script declarations -- move statements into a process, workflow, or function

  ```nextflow
  def summary_params = NfcoreSchema.paramsSummaryMap(workflow, params)
  ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  ```

- Error: `workflows/genomeannotator.nf:7:22`: `NfcoreSchema` is not defined

  ```nextflow
  def summary_params = NfcoreSchema.paramsSummaryMap(workflow, params)
                       ^^^^^^^^^^^^
  ```

- Error: `workflows/genomeannotator.nf:10:1`: Statements cannot be mixed with script declarations -- move statements into a process, workflow, or function

  ```nextflow
  WorkflowGenomeannotator.initialise(params, log)
  ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  ```

- Error: `workflows/genomeannotator.nf:10:1`: `WorkflowGenomeannotator` is not defined

  ```nextflow
  WorkflowGenomeannotator.initialise(params, log)
  ^^^^^^^^^^^^^^^^^^^^^^^
  ```

- Error: `workflows/genomeannotator.nf:12:1`: Statements cannot be mixed with script declarations -- move statements into a process, workflow, or function

  ```nextflow
  def checkPathParamList = [ params.multiqc_config, params.assembly ]
  ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  ```

- Error: `workflows/genomeannotator.nf:13:1`: `for` loops are no longer supported

  ```nextflow
  for (param in checkPathParamList) { if (param) { file(param, checkIfExists: true) } }
  ^^^
  ```

- Error: `workflows/genomeannotator.nf:13:1`: Statements cannot be mixed with script declarations -- move statements into a process, workflow, or function

  ```nextflow
  for (param in checkPathParamList) { if (param) { file(param, checkIfExists: true) } }
  ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  ```

- Error: `workflows/genomeannotator.nf:13:6`: `param` is not defined

  ```nextflow
  for (param in checkPathParamList) { if (param) { file(param, checkIfExists: true) } }
       ^^^^^
  ```

- Error: `workflows/genomeannotator.nf:13:40`: `param` is not defined

  ```nextflow
  for (param in checkPathParamList) { if (param) { file(param, checkIfExists: true) } }
                                         ^^^^^^^
  ```

- Error: `workflows/genomeannotator.nf:13:55`: `param` is not defined

  ```nextflow
  for (param in checkPathParamList) { if (param) { file(param, checkIfExists: true) } }
                                                        ^^^^^
  ```

- Error: `workflows/genomeannotator.nf:16:1`: Statements cannot be mixed with script declarations -- move statements into a process, workflow, or function

  ```nextflow
  if (params.assembly) { ch_genome = file(params.assembly, checkIfExists: true) } else { exit 1, 'No assembly specified!' }
  ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  ```

- Error: `workflows/genomeannotator.nf:19:1`: Statements cannot be mixed with script declarations -- move statements into a process, workflow, or function

  ```nextflow
  if (params.proteins) { ch_proteins = file(params.proteins, checkIfExists: true) } else { ch_proteins = Channel.empty() }
  ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  ```

- Error: `workflows/genomeannotator.nf:20:1`: Statements cannot be mixed with script declarations -- move statements into a process, workflow, or function

  ```nextflow
  if (params.proteins_targeted) { ch_proteins_targeted = file(params.proteins_targeted, checkIfExists: true) } else { ch_proteins_targeted = Channel.empty() }
  ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  ```

- Error: `workflows/genomeannotator.nf:21:1`: Statements cannot be mixed with script declarations -- move statements into a process, workflow, or function

  ```nextflow
  if (params.transcripts) { ch_t = file(params.transcripts) } else { ch_transcripts = Channel.empty() }
  ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  ```

- Error: `workflows/genomeannotator.nf:22:1`: Statements cannot be mixed with script declarations -- move statements into a process, workflow, or function

  ```nextflow
  if (params.rnaseq_samples) { ch_samplesheet = file(params.rnaseq_samples, checkIfExists: true) } else { ch_samplesheet = Channel.empty() }
  ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  ```

- Error: `workflows/genomeannotator.nf:23:1`: Statements cannot be mixed with script declarations -- move statements into a process, workflow, or function

  ```nextflow
  if (params.rm_lib) { ch_repeats = Channel.fromPath(file(params.rm_lib, checkIfExists: true)) } else { ch_repeats = Channel.fromPath("${workflow.projectDir}/assets/repeatmasker/repeats.fa") }
  ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  ```

- Error: `workflows/genomeannotator.nf:24:1`: Statements cannot be mixed with script declarations -- move statements into a process, workflow, or function

  ```nextflow
  if (params.aug_config_dir) { ch_aug_config_folder = file(params.aug_config_dir, checkIfExists: true) } else { ch_aug_config_folder = Channel.from(params.aug_config_container) }
  ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  ```

- Error: `workflows/genomeannotator.nf:25:1`: Statements cannot be mixed with script declarations -- move statements into a process, workflow, or function

  ```nextflow
  if (params.references) { ch_ref_genomes = Channel.fromPath(params.references, checkIfExists: true)  } else { ch_ref_genomes = Channel.empty() }
  ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  ```

- Error: `workflows/genomeannotator.nf:26:1`: Statements cannot be mixed with script declarations -- move statements into a process, workflow, or function

  ```nextflow
  if (params.rm_db)  { ch_rm_db = file(params.rm_db) } else { ch_rm_db = Channel.empty() }
  ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  ```

- Error: `workflows/genomeannotator.nf:34:1`: Statements cannot be mixed with script declarations -- move statements into a process, workflow, or function

  ```nextflow
  ch_multiqc_config        = file("$projectDir/assets/multiqc_config.yaml", checkIfExists: true)
  ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  ```

- Error: `workflows/genomeannotator.nf:35:1`: Statements cannot be mixed with script declarations -- move statements into a process, workflow, or function

  ```nextflow
  ch_multiqc_custom_config = params.multiqc_config ? Channel.fromPath(params.multiqc_config) : Channel.empty()
  ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  ```

- Error: `workflows/genomeannotator.nf:36:1`: Statements cannot be mixed with script declarations -- move statements into a process, workflow, or function

  ```nextflow
  ch_aug_extrinsic_cfg = params.aug_extrinsic_cfg ? Channel.from( file(params.aug_extrinsic_cfg, checkIfExists: true) ) : Channel.from( file("${workflow.projectDir}/assets/augustus/augustus_default.cfg"))
  ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  ```

- Error: `workflows/genomeannotator.nf:37:1`: Statements cannot be mixed with script declarations -- move statements into a process, workflow, or function

  ```nextflow
  ch_evm_weights = Channel.from(file(params.evm_weights, checkIfExists: true))
  ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  ```

- Error: `workflows/genomeannotator.nf:38:1`: Statements cannot be mixed with script declarations -- move statements into a process, workflow, or function

  ```nextflow
  ch_rfam_cm = file("${workflow.projectDir}/assets/rfam/14.2/Rfam.cm.gz", checkIfExists: true)
  ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  ```

- Error: `workflows/genomeannotator.nf:39:1`: Statements cannot be mixed with script declarations -- move statements into a process, workflow, or function

  ```nextflow
  ch_rfam_family = file("${workflow.projectDir}/assets/rfam/14.2/family.txt.gz", checkIfExists: true)
  ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  ```

- Error: `workflows/genomeannotator.nf:88:1`: Statements cannot be mixed with script declarations -- move statements into a process, workflow, or function

  ```nextflow
  def multiqc_report = []
  ^^^^^^^^^^^^^^^^^^^^^^^
  ```

- Error: `workflows/genomeannotator.nf:109:11`: `ch_t` is not defined

  ```nextflow
            ch_t
            ^^^^
  ```

- Error: `workflows/genomeannotator.nf:117:26`: `ch_aug_config_folder` is not defined

  ```nextflow
      AUGUSTUS_STAGECONFIG(ch_aug_config_folder)
                           ^^^^^^^^^^^^^^^^^^^^
  ```

- Error: `workflows/genomeannotator.nf:124:9`: `ch_genome` is not defined

  ```nextflow
          ch_genome
          ^^^^^^^^^
  ```

- Error: `workflows/genomeannotator.nf:134:11`: `ch_rfam_cm` is not defined

  ```nextflow
            ch_rfam_cm,
            ^^^^^^^^^^
  ```

- Error: `workflows/genomeannotator.nf:135:11`: `ch_rfam_family` is not defined

  ```nextflow
            ch_rfam_family
            ^^^^^^^^^^^^^^
  ```

- Error: `workflows/genomeannotator.nf:145:11`: `ch_ref_genomes` is not defined

  ```nextflow
            ch_ref_genomes
            ^^^^^^^^^^^^^^
  ```

- Error: `workflows/genomeannotator.nf:169:11`: `ch_rm_db` is not defined

  ```nextflow
            ch_rm_db
            ^^^^^^^^
  ```

- Error: `workflows/genomeannotator.nf:178:11`: `ch_rm_db` is not defined

  ```nextflow
            ch_rm_db
            ^^^^^^^^
  ```

- Error: `workflows/genomeannotator.nf:189:11`: `ch_proteins` is not defined

  ```nextflow
            ch_proteins,
            ^^^^^^^^^^^
  ```

- Error: `workflows/genomeannotator.nf:202:11`: `ch_proteins_targeted` is not defined

  ```nextflow
            ch_proteins_targeted,
            ^^^^^^^^^^^^^^^^^^^^
  ```

- Error: `workflows/genomeannotator.nf:216:11`: `ch_samplesheet` is not defined

  ```nextflow
            ch_samplesheet
            ^^^^^^^^^^^^^^
  ```

- Error: `workflows/genomeannotator.nf:222:9`: Variables in a closure should be declared with `def`

  ```nextflow
          new_meta = [:]
          ^^^^^^^^
  ```

- Error: `workflows/genomeannotator.nf:290:11`: `AUGUSTUS_TRAINING` is not defined

  ```nextflow
            AUGUSTUS_TRAINING(
            ^^^^^^^^^^^^^^^^^
  ```

- Error: `workflows/genomeannotator.nf:293:33`: `AUGUSTUS_TRAINING` is not defined

  ```nextflow
            ch_aug_config_final = AUGUSTUS_TRAINING.out.aug_config_folder
                                  ^^^^^^^^^^^^^^^^^
  ```

- Error: `workflows/genomeannotator.nf:295:11`: `AUGUSTUS_TRAINING` is not defined

  ```nextflow
            AUGUSTUS_TRAINING(
            ^^^^^^^^^^^^^^^^^
  ```

- Error: `workflows/genomeannotator.nf:298:33`: `AUGUSTUS_TRAINING` is not defined

  ```nextflow
            ch_aug_config_final = AUGUSTUS_TRAINING.out.aug_config_folder
                                  ^^^^^^^^^^^^^^^^^
  ```

- Error: `workflows/genomeannotator.nf:314:8`: `ch_aug_extrinsic_cfg` is not defined

  ```nextflow
         ch_aug_extrinsic_cfg,
         ^^^^^^^^^^^^^^^^^^^^
  ```

- Error: `workflows/genomeannotator.nf:329:11`: `ch_evm_weights` is not defined

  ```nextflow
            ch_evm_weights
            ^^^^^^^^^^^^^^
  ```

- Error: `workflows/genomeannotator.nf:357:27`: `WorkflowGenomeannotator` is not defined

  ```nextflow
      workflow_summary    = WorkflowGenomeannotator.paramsSummaryMultiqc(workflow, summary_params)
                            ^^^^^^^^^^^^^^^^^^^^^^^
  ```

- Error: `workflows/genomeannotator.nf:357:82`: `summary_params` is not defined

  ```nextflow
      workflow_summary    = WorkflowGenomeannotator.paramsSummaryMultiqc(workflow, summary_params)
                                                                                   ^^^^^^^^^^^^^^
  ```

- Error: `workflows/genomeannotator.nf:361:58`: `ch_multiqc_config` is not defined

  ```nextflow
      ch_multiqc_files = ch_multiqc_files.mix(Channel.from(ch_multiqc_config))
                                                           ^^^^^^^^^^^^^^^^^
  ```

- Error: `workflows/genomeannotator.nf:362:45`: `ch_multiqc_custom_config` is not defined

  ```nextflow
      ch_multiqc_files = ch_multiqc_files.mix(ch_multiqc_custom_config.collect().ifEmpty([]))
                                              ^^^^^^^^^^^^^^^^^^^^^^^^
  ```

- Error: `workflows/genomeannotator.nf:380:1`: Statements cannot be mixed with script declarations -- move statements into a process, workflow, or function

  ```nextflow
  workflow.onComplete {
  ^
  ```

- Error: `workflows/genomeannotator.nf:382:9`: `NfcoreTemplate` is not defined

  ```nextflow
          NfcoreTemplate.email(workflow, params, summary_params, projectDir, log, multiqc_report)
          ^^^^^^^^^^^^^^
  ```

- Error: `workflows/genomeannotator.nf:384:5`: `NfcoreTemplate` is not defined

  ```nextflow
      NfcoreTemplate.summary(workflow, params, log)
      ^^^^^^^^^^^^^^
  ```

## :warning: Warnings

- Warning: `modules/local/augustus/aligntohints.nf:21:9`: Variable was declared but not used

  ```nextflow
      def args = task.ext.args ?: ''
          ^^^^
  ```

- Warning: `modules/local/augustus/aligntohints.nf:22:9`: Variable was declared but not used

  ```nextflow
      def prefix = task.ext.prefix ?: "${meta.id}"
          ^^^^^^
  ```

- Warning: `modules/local/augustus/augustusbatch.nf:22:9`: Variable was declared but not used

  ```nextflow
      def prefix = task.ext.prefix ?: "${meta.id}"
          ^^^^^^
  ```

- Warning: `modules/local/augustus/bam2hints.nf:19:9`: Variable was declared but not used

  ```nextflow
      def args = task.ext.args ?: ''
          ^^^^
  ```

- Warning: `modules/local/augustus/fixjoingenes.nf:18:9`: Variable was declared but not used

  ```nextflow
      def args = task.ext.args ?: ''
          ^^^^
  ```

- Warning: `modules/local/augustus/fixjoingenes.nf:19:9`: Variable was declared but not used

  ```nextflow
      def prefix = task.ext.prefix ?: "${meta.id}"
          ^^^^^^
  ```

- Warning: `modules/local/augustus/stageconfig.nf:18:9`: Variable was declared but not used

  ```nextflow
      def args = task.ext.args ?: ''
          ^^^^
  ```

- Warning: `modules/local/augustus/training.nf:22:9`: Variable was declared but not used

  ```nextflow
      def args = task.ext.args ?: ''
          ^^^^
  ```

- Warning: `modules/local/augustus/training.nf:23:9`: Variable was declared but not used

  ```nextflow
      def prefix = task.ext.prefix ?: "${meta.id}"
          ^^^^^^
  ```

- Warning: `modules/local/busco/busco.nf:22:9`: Variable was declared but not used

  ```nextflow
      def args = task.ext.args ?: ''
          ^^^^
  ```

- Warning: `modules/local/busco/busco.nf:23:9`: Variable was declared but not used

  ```nextflow
      def prefix = task.ext.prefix ?: "${meta.id}"
          ^^^^^^
  ```

- Warning: `modules/local/busco/downloaddb.nf:21:9`: Variable was declared but not used

  ```nextflow
      def args = task.ext.args ?: ''
          ^^^^
  ```

- Warning: `modules/local/cat/fasta.nf:18:9`: Variable was declared but not used

  ```nextflow
      def args = task.ext.args ?: ''
          ^^^^
  ```

- Warning: `modules/local/cat/gff.nf:21:9`: Variable was declared but not used

  ```nextflow
      def args = task.ext.args ?: ''
          ^^^^
  ```

- Warning: `modules/local/evidencemodeler/execute.nf:18:9`: Variable was declared but not used

  ```nextflow
      def args = task.ext.args ?: ''
          ^^^^
  ```

- Warning: `modules/local/evidencemodeler/execute.nf:19:9`: Variable was declared but not used

  ```nextflow
      def prefix = task.ext.prefix ?: "${meta.id}"
          ^^^^^^
  ```

- Warning: `modules/local/evidencemodeler/merge.nf:20:9`: Variable was declared but not used

  ```nextflow
      def args = task.ext.args ?: ''
          ^^^^
  ```

- Warning: `modules/local/evidencemodeler/merge.nf:21:9`: Variable was declared but not used

  ```nextflow
      def prefix = task.ext.prefix ?: "${meta.id}"
          ^^^^^^
  ```

- Warning: `modules/local/evidencemodeler/partition.nf:24:9`: Variable was declared but not used

  ```nextflow
      def args = task.ext.args ?: ''
          ^^^^
  ```

- Warning: `modules/local/evidencemodeler/partition.nf:25:9`: Variable was declared but not used

  ```nextflow
      def prefix = task.ext.prefix ?: "${meta.id}"
          ^^^^^^
  ```

- Warning: `modules/local/exonerate/fastaclean.nf:18:9`: Variable was declared but not used

  ```nextflow
      def args = task.ext.args ?: ''
          ^^^^
  ```

- Warning: `modules/local/exonerate/fastaclean.nf:19:9`: Variable was declared but not used

  ```nextflow
      def prefix = task.ext.prefix ?: "${meta.id}"
          ^^^^^^
  ```

- Warning: `modules/local/fastasplitter.nf:19:9`: Variable was declared but not used

  ```nextflow
      def args = task.ext.args ?: ''
          ^^^^
  ```

- Warning: `modules/local/fastasplitter.nf:20:9`: Variable was declared but not used

  ```nextflow
      def prefix = task.ext.prefix ?: "${meta.id}"
          ^^^^^^
  ```

- Warning: `modules/local/fastp.nf:20:9`: Variable was declared but not used

  ```nextflow
      def args = task.ext.args ?: ''
          ^^^^
  ```

- Warning: `modules/local/gaas/fastacleaner.nf:18:9`: Variable was declared but not used

  ```nextflow
      def args = task.ext.args ?: ''
          ^^^^
  ```

- Warning: `modules/local/gaas/fastacleaner.nf:19:9`: Variable was declared but not used

  ```nextflow
      def prefix = task.ext.prefix ?: "${meta.id}"
          ^^^^^^
  ```

- Warning: `modules/local/gaas/fastafilterbysize.nf:19:9`: Variable was declared but not used

  ```nextflow
      def args = task.ext.args ?: ''
          ^^^^
  ```

- Warning: `modules/local/gaas/fastastatistics.nf:18:9`: Variable was declared but not used

  ```nextflow
      def args = task.ext.args ?: ''
          ^^^^
  ```

- Warning: `modules/local/gffread.nf:20:9`: Variable was declared but not used

  ```nextflow
      def args = task.ext.args ?: ''
          ^^^^
  ```

- Warning: `modules/local/gffread.nf:21:5`: Variable was declared but not used

  ```nextflow
      prefix = task.ext.prefix ?: "${meta.id}"
      ^^^^^^
  ```

- Warning: `modules/local/helper/addexons.nf:18:9`: Variable was declared but not used

  ```nextflow
      def args = task.ext.args ?: ''
          ^^^^
  ```

- Warning: `modules/local/helper/bamtogff.nf:18:9`: Variable was declared but not used

  ```nextflow
      def args = task.ext.args ?: ''
          ^^^^
  ```

- Warning: `modules/local/helper/bamtogff.nf:19:9`: Variable was declared but not used

  ```nextflow
      def prefix = task.ext.prefix ?: "${meta.id}"
          ^^^^^^
  ```

- Warning: `modules/local/helper/creategffids.nf:18:9`: Variable was declared but not used

  ```nextflow
      def args = task.ext.args ?: ''
          ^^^^
  ```

- Warning: `modules/local/helper/creategffids.nf:19:9`: Variable was declared but not used

  ```nextflow
      def prefix = task.ext.prefix ?: "${meta.id}"
          ^^^^^^
  ```

- Warning: `modules/local/helper/downloadrfam.nf:20:9`: Variable was declared but not used

  ```nextflow
      def args = task.ext.args ?: ''
          ^^^^
  ```

- Warning: `modules/local/helper/evm2gff.nf:18:9`: Variable was declared but not used

  ```nextflow
      def args = task.ext.args ?: ''
          ^^^^
  ```

- Warning: `modules/local/helper/gtf2hints.nf:19:9`: Variable was declared but not used

  ```nextflow
      def args = task.ext.args ?: ''
          ^^^^
  ```

- Warning: `modules/local/helper/kraken2gff.nf:18:9`: Variable was declared but not used

  ```nextflow
      def args = task.ext.args ?: ''
          ^^^^
  ```

- Warning: `modules/local/helper/kraken2gff.nf:19:9`: Variable was declared but not used

  ```nextflow
      def prefix = task.ext.prefix ?: "${meta.id}"
          ^^^^^^
  ```

- Warning: `modules/local/helper/match2gmod.nf:18:9`: Variable was declared but not used

  ```nextflow
      def args = task.ext.args ?: ''
          ^^^^
  ```

- Warning: `modules/local/helper/match2gmod.nf:19:9`: Variable was declared but not used

  ```nextflow
      def prefix = task.ext.prefix ?: "${meta.id}"
          ^^^^^^
  ```

- Warning: `modules/local/helper/minimaptohints.nf:20:9`: Variable was declared but not used

  ```nextflow
      def args = task.ext.args ?: ''
          ^^^^
  ```

- Warning: `modules/local/helper/pasa2training.nf:19:9`: Variable was declared but not used

  ```nextflow
      def args = task.ext.args ?: ''
          ^^^^
  ```

- Warning: `modules/local/helper/rfamtogff.nf:21:9`: Variable was declared but not used

  ```nextflow
      def args = task.ext.args ?: ''
          ^^^^
  ```

- Warning: `modules/local/helper/spalntoevm.nf:18:9`: Variable was declared but not used

  ```nextflow
      def args = task.ext.args ?: ''
          ^^^^
  ```

- Warning: `modules/local/helper/spalntoevm.nf:19:9`: Variable was declared but not used

  ```nextflow
      def prefix = task.ext.prefix ?: "${meta.id}"
          ^^^^^^
  ```

- Warning: `modules/local/helper/spalntogmod.nf:18:9`: Variable was declared but not used

  ```nextflow
      def args = task.ext.args ?: ''
          ^^^^
  ```

- Warning: `modules/local/helper/spalntogmod.nf:19:9`: Variable was declared but not used

  ```nextflow
      def prefix = task.ext.prefix ?: "${meta.id}"
          ^^^^^^
  ```

- Warning: `modules/local/helper/spalntotraining.nf:18:9`: Variable was declared but not used

  ```nextflow
      def args = task.ext.args ?: ''
          ^^^^
  ```

- Warning: `modules/local/helper/spalntotraining.nf:19:9`: Variable was declared but not used

  ```nextflow
      def prefix = task.ext.prefix ?: "${meta.id}"
          ^^^^^^
  ```

- Warning: `modules/local/infernal/press.nf:18:9`: Variable was declared but not used

  ```nextflow
      def args = task.ext.args ?: ''
          ^^^^
  ```

- Warning: `modules/local/infernal/search.nf:19:9`: Variable was declared but not used

  ```nextflow
      def args = task.ext.args ?: ''
          ^^^^
  ```

- Warning: `modules/local/infernal/search.nf:20:9`: Variable was declared but not used

  ```nextflow
      def prefix = task.ext.prefix ?: "${meta.id}"
          ^^^^^^
  ```

- Warning: `modules/local/kraken.nf:19:9`: Variable was declared but not used

  ```nextflow
      def args = task.ext.args ?: ''
          ^^^^
  ```

- Warning: `modules/local/kraken.nf:20:9`: Variable was declared but not used

  ```nextflow
      def prefix = task.ext.prefix ?: "${meta.id}"
          ^^^^^^
  ```

- Warning: `modules/local/minimap2/align.nf:20:9`: Variable was declared but not used

  ```nextflow
      def args = task.ext.args ?: ''
          ^^^^
  ```

- Warning: `modules/local/minimap2/align.nf:21:9`: Variable was declared but not used

  ```nextflow
      def prefix = task.ext.prefix ?: "${meta.id}"
          ^^^^^^
  ```

- Warning: `modules/local/pasa/alignassemble.nf:23:9`: Variable was declared but not used

  ```nextflow
      def args = task.ext.args ?: ''
          ^^^^
  ```

- Warning: `modules/local/pasa/asmblstotraining.nf:19:9`: Variable was declared but not used

  ```nextflow
      def args = task.ext.args ?: ''
          ^^^^
  ```

- Warning: `modules/local/pasa/asmblstotraining.nf:20:9`: Variable was declared but not used

  ```nextflow
      def prefix = task.ext.prefix ?: "${meta.id}"
          ^^^^^^
  ```

- Warning: `modules/local/pasa/seqclean.nf:18:9`: Variable was declared but not used

  ```nextflow
      def args = task.ext.args ?: ''
          ^^^^
  ```

- Warning: `modules/local/pasa/seqclean.nf:19:9`: Variable was declared but not used

  ```nextflow
      def prefix = task.ext.prefix ?: "${meta.id}"
          ^^^^^^
  ```

- Warning: `modules/local/repeatmasker/repeatmask.nf:24:9`: Variable was declared but not used

  ```nextflow
      def args = task.ext.args ?: ''
          ^^^^
  ```

- Warning: `modules/local/repeatmasker/repeatmask.nf:25:9`: Variable was declared but not used

  ```nextflow
      def prefix = task.ext.prefix ?: "${meta.id}"
          ^^^^^^
  ```

- Warning: `modules/local/repeatmasker/stagelib.nf:21:9`: Variable was declared but not used

  ```nextflow
      def args = task.ext.args ?: ''
          ^^^^
  ```

- Warning: `modules/local/repeatmasker/stagelib.nf:29:13`: The use of `baseDir` in a process is discouraged -- input files should be provided as process inputs

  ```nextflow
         cp ${baseDir}/assets/repeatmasker/my_genome.fa .
              ^^^^^^^
  ```

- Warning: `modules/local/repeatmasker/stagelib.nf:30:13`: The use of `baseDir` in a process is discouraged -- input files should be provided as process inputs

  ```nextflow
         cp ${baseDir}/assets/repeatmasker/repeats.fa .
              ^^^^^^^
  ```

- Warning: `modules/local/repeatmodeler.nf:18:9`: Variable was declared but not used

  ```nextflow
      def args = task.ext.args ?: ''
          ^^^^
  ```

- Warning: `modules/local/repeatmodeler.nf:19:9`: Variable was declared but not used

  ```nextflow
      def prefix = task.ext.prefix ?: "${meta.id}"
          ^^^^^^
  ```

- Warning: `modules/local/satsuma2/satsumasynteny2.nf:20:9`: Variable was declared but not used

  ```nextflow
      def args = task.ext.args ?: ''
          ^^^^
  ```

- Warning: `modules/local/satsuma2/satsumasynteny2.nf:21:9`: Variable was declared but not used

  ```nextflow
      def prefix = task.ext.prefix ?: "${meta.id}"
          ^^^^^^
  ```

- Warning: `modules/local/spaln/align.nf:22:9`: Variable was declared but not used

  ```nextflow
      def args = task.ext.args ?: ''
          ^^^^
  ```

- Warning: `modules/local/spaln/align.nf:23:9`: Variable was declared but not used

  ```nextflow
      def prefix = task.ext.prefix ?: "${meta.id}"
          ^^^^^^
  ```

- Warning: `modules/local/spaln/makeindex.nf:18:9`: Variable was declared but not used

  ```nextflow
      def args = task.ext.args ?: ''
          ^^^^
  ```

- Warning: `modules/local/spaln/makeindex.nf:19:9`: Variable was declared but not used

  ```nextflow
      def prefix = task.ext.prefix ?: "${meta.id}"
          ^^^^^^
  ```

- Warning: `modules/local/spaln/merge.nf:20:9`: Variable was declared but not used

  ```nextflow
      def args = task.ext.args ?: ''
          ^^^^
  ```

- Warning: `modules/local/spaln/merge.nf:21:9`: Variable was declared but not used

  ```nextflow
      def prefix = task.ext.prefix ?: "${meta.id}"
          ^^^^^^
  ```

- Warning: `modules/local/star/align.nf:23:9`: Variable was declared but not used

  ```nextflow
      def args = task.ext.args ?: ''
          ^^^^
  ```

- Warning: `modules/local/star/index.nf:18:9`: Variable was declared but not used

  ```nextflow
      def args = task.ext.args ?: ''
          ^^^^
  ```

- Warning: `modules/local/star/index.nf:19:9`: Variable was declared but not used

  ```nextflow
      def prefix = task.ext.prefix ?: "${meta.id}"
          ^^^^^^
  ```

- Warning: `modules/local/trinity/genomeguided.nf:19:9`: Variable was declared but not used

  ```nextflow
      def args = task.ext.args ?: ''
          ^^^^
  ```

- Warning: `modules/local/trinity/genomeguided.nf:20:9`: Variable was declared but not used

  ```nextflow
      def prefix = task.ext.prefix ?: "${meta.id}"
          ^^^^^^
  ```

- Warning: `modules/nf-core/modules/cat/fastq/main.nf:21:9`: Variable was declared but not used

  ```nextflow
      def args = task.ext.args ?: ''
          ^^^^
  ```

- Warning: `modules/nf-core/modules/cat/fastq/main.nf:23:35`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
      def readList = reads.collect{ it.toString() }
                                    ^^
  ```

- Warning: `modules/nf-core/modules/custom/dumpsoftwareversions/main.nf:22:9`: Variable was declared but not used

  ```nextflow
      def args = task.ext.args ?: ''
          ^^^^
  ```

- Warning: `subworkflows/local/augustus_pipeline.nf:28:41`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
         aug_config_folder.collect().map{ it[0].toString() },
                                          ^^
  ```

- Warning: `subworkflows/local/augustus_pipeline.nf:50:12`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
      .map { k,m,f -> tuple(m,f) }
             ^
  ```

- Warning: `subworkflows/local/busco_qc.nf:22:24`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
        ch_lineage_dir = Channel.from([busco_lineage,busco_db_path])
                         ^^^^^^^
  ```

- Warning: `subworkflows/local/evm.nf:18:5`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
      evm_config
      ^^^^^^^^^^
  ```

- Warning: `subworkflows/local/genome_align.nf:23:37`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
         .map { create_target_channel(it) }
                                      ^^
  ```

- Warning: `subworkflows/local/genome_align.nf:30:26`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
         targets.map { m,f,g ->
                           ^
  ```

- Warning: `subworkflows/local/genome_align.nf:46:27`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
            targets.map { m,f,g ->
                            ^
  ```

- Warning: `subworkflows/local/genome_align.nf:62:46`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
         row[1..-1].collect { [row[0].clone(), it]  }
                                               ^^
  ```

- Warning: `subworkflows/local/input_check.nf:15:37`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          .map { create_fastq_channel(it) }
                                      ^^
  ```

- Warning: `subworkflows/local/ncrna.nf:29:38`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
        GUNZIP_RFAM_CM.out.gunzip.map {m,f -> f}
                                       ^
  ```

- Warning: `subworkflows/local/ncrna.nf:50:12`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
      .map { k,m,f -> tuple(m,f) }
             ^
  ```

- Warning: `subworkflows/local/ncrna.nf:55:41`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
        GUNZIP_RFAM_FAMILY.out.gunzip.map{m,f -> f}
                                          ^
  ```

- Warning: `subworkflows/local/repeatmasker.nf:26:31`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
         GUNZIP.out.gunzip.map {m,g -> g}
                                ^
  ```

- Warning: `subworkflows/local/repeatmasker.nf:30:56`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
         REPEATMASKER_STAGELIB.out.library.collect().map{it[0].toString()},
                                                         ^^
  ```

- Warning: `subworkflows/local/rnaseq_align.nf:25:37`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          .map { create_fastq_channel(it) }
                                      ^^
  ```

- Warning: `subworkflows/local/rnaseq_align.nf:61:8`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
         Channel.from(params.dummy_gff).collect(),
         ^^^^^^^
  ```

- Warning: `workflows/genomeannotator.nf:16:24`: Variable was declared but not used

  ```nextflow
  if (params.assembly) { ch_genome = file(params.assembly, checkIfExists: true) } else { exit 1, 'No assembly specified!' }
                         ^^^^^^^^^
  ```

- Warning: `workflows/genomeannotator.nf:19:104`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
  if (params.proteins) { ch_proteins = file(params.proteins, checkIfExists: true) } else { ch_proteins = Channel.empty() }
                                                                                                         ^^^^^^^
  ```

- Warning: `workflows/genomeannotator.nf:20:140`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
  if (params.proteins_targeted) { ch_proteins_targeted = file(params.proteins_targeted, checkIfExists: true) } else { ch_proteins_targeted = Channel.empty() }
                                                                                                                                             ^^^^^^^
  ```

- Warning: `workflows/genomeannotator.nf:21:27`: Variable was declared but not used

  ```nextflow
  if (params.transcripts) { ch_t = file(params.transcripts) } else { ch_transcripts = Channel.empty() }
                            ^^^^
  ```

- Warning: `workflows/genomeannotator.nf:21:68`: Variable was declared but not used

  ```nextflow
  if (params.transcripts) { ch_t = file(params.transcripts) } else { ch_transcripts = Channel.empty() }
                                                                     ^^^^^^^^^^^^^^
  ```

- Warning: `workflows/genomeannotator.nf:21:85`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
  if (params.transcripts) { ch_t = file(params.transcripts) } else { ch_transcripts = Channel.empty() }
                                                                                      ^^^^^^^
  ```

- Warning: `workflows/genomeannotator.nf:22:122`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
  if (params.rnaseq_samples) { ch_samplesheet = file(params.rnaseq_samples, checkIfExists: true) } else { ch_samplesheet = Channel.empty() }
                                                                                                                           ^^^^^^^
  ```

- Warning: `workflows/genomeannotator.nf:23:35`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
  if (params.rm_lib) { ch_repeats = Channel.fromPath(file(params.rm_lib, checkIfExists: true)) } else { ch_repeats = Channel.fromPath("${workflow.projectDir}/assets/repeatmasker/repeats.fa") }
                                    ^^^^^^^
  ```

- Warning: `workflows/genomeannotator.nf:23:116`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
  if (params.rm_lib) { ch_repeats = Channel.fromPath(file(params.rm_lib, checkIfExists: true)) } else { ch_repeats = Channel.fromPath("${workflow.projectDir}/assets/repeatmasker/repeats.fa") }
                                                                                                                     ^^^^^^^
  ```

- Warning: `workflows/genomeannotator.nf:24:134`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
  if (params.aug_config_dir) { ch_aug_config_folder = file(params.aug_config_dir, checkIfExists: true) } else { ch_aug_config_folder = Channel.from(params.aug_config_container) }
                                                                                                                                       ^^^^^^^
  ```

- Warning: `workflows/genomeannotator.nf:25:43`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
  if (params.references) { ch_ref_genomes = Channel.fromPath(params.references, checkIfExists: true)  } else { ch_ref_genomes = Channel.empty() }
                                            ^^^^^^^
  ```

- Warning: `workflows/genomeannotator.nf:25:127`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
  if (params.references) { ch_ref_genomes = Channel.fromPath(params.references, checkIfExists: true)  } else { ch_ref_genomes = Channel.empty() }
                                                                                                                                ^^^^^^^
  ```

- Warning: `workflows/genomeannotator.nf:26:72`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
  if (params.rm_db)  { ch_rm_db = file(params.rm_db) } else { ch_rm_db = Channel.empty() }
                                                                         ^^^^^^^
  ```

- Warning: `workflows/genomeannotator.nf:34:1`: Variable was declared but not used

  ```nextflow
  ch_multiqc_config        = file("$projectDir/assets/multiqc_config.yaml", checkIfExists: true)
  ^^^^^^^^^^^^^^^^^
  ```

- Warning: `workflows/genomeannotator.nf:35:1`: Variable was declared but not used

  ```nextflow
  ch_multiqc_custom_config = params.multiqc_config ? Channel.fromPath(params.multiqc_config) : Channel.empty()
  ^^^^^^^^^^^^^^^^^^^^^^^^
  ```

- Warning: `workflows/genomeannotator.nf:35:52`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
  ch_multiqc_custom_config = params.multiqc_config ? Channel.fromPath(params.multiqc_config) : Channel.empty()
                                                     ^^^^^^^
  ```

- Warning: `workflows/genomeannotator.nf:35:94`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
  ch_multiqc_custom_config = params.multiqc_config ? Channel.fromPath(params.multiqc_config) : Channel.empty()
                                                                                               ^^^^^^^
  ```

- Warning: `workflows/genomeannotator.nf:36:1`: Variable was declared but not used

  ```nextflow
  ch_aug_extrinsic_cfg = params.aug_extrinsic_cfg ? Channel.from( file(params.aug_extrinsic_cfg, checkIfExists: true) ) : Channel.from( file("${workflow.projectDir}/assets/augustus/augustus_default.cfg"))
  ^^^^^^^^^^^^^^^^^^^^
  ```

- Warning: `workflows/genomeannotator.nf:36:51`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
  ch_aug_extrinsic_cfg = params.aug_extrinsic_cfg ? Channel.from( file(params.aug_extrinsic_cfg, checkIfExists: true) ) : Channel.from( file("${workflow.projectDir}/assets/augustus/augustus_default.cfg"))
                                                    ^^^^^^^
  ```

- Warning: `workflows/genomeannotator.nf:36:121`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
  ch_aug_extrinsic_cfg = params.aug_extrinsic_cfg ? Channel.from( file(params.aug_extrinsic_cfg, checkIfExists: true) ) : Channel.from( file("${workflow.projectDir}/assets/augustus/augustus_default.cfg"))
                                                                                                                          ^^^^^^^
  ```

- Warning: `workflows/genomeannotator.nf:37:1`: Variable was declared but not used

  ```nextflow
  ch_evm_weights = Channel.from(file(params.evm_weights, checkIfExists: true))
  ^^^^^^^^^^^^^^
  ```

- Warning: `workflows/genomeannotator.nf:37:18`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
  ch_evm_weights = Channel.from(file(params.evm_weights, checkIfExists: true))
                   ^^^^^^^
  ```

- Warning: `workflows/genomeannotator.nf:38:1`: Variable was declared but not used

  ```nextflow
  ch_rfam_cm = file("${workflow.projectDir}/assets/rfam/14.2/Rfam.cm.gz", checkIfExists: true)
  ^^^^^^^^^^
  ```

- Warning: `workflows/genomeannotator.nf:39:1`: Variable was declared but not used

  ```nextflow
  ch_rfam_family = file("${workflow.projectDir}/assets/rfam/14.2/family.txt.gz", checkIfExists: true)
  ^^^^^^^^^^^^^^
  ```

- Warning: `workflows/genomeannotator.nf:92:20`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_empty_gff = Channel.fromPath(params.dummy_gff)
                     ^^^^^^^
  ```

- Warning: `workflows/genomeannotator.nf:93:19`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_versions = Channel.empty()
                    ^^^^^^^
  ```

- Warning: `workflows/genomeannotator.nf:94:16`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_hints = Channel.empty()
                 ^^^^^^^
  ```

- Warning: `workflows/genomeannotator.nf:95:5`: Variable was declared but not used

  ```nextflow
      ch_repeats_lib = Channel.empty()
      ^^^^^^^^^^^^^^
  ```

- Warning: `workflows/genomeannotator.nf:95:22`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_repeats_lib = Channel.empty()
                       ^^^^^^^
  ```

- Warning: `workflows/genomeannotator.nf:96:23`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_proteins_gff = Channel.from([])
                        ^^^^^^^
  ```

- Warning: `workflows/genomeannotator.nf:97:26`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_transcripts_gff = Channel.from([])
                           ^^^^^^^
  ```

- Warning: `workflows/genomeannotator.nf:98:20`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_genes_gff = Channel.empty()
                     ^^^^^^^
  ```

- Warning: `workflows/genomeannotator.nf:99:22`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_transcripts = Channel.empty()
                       ^^^^^^^
  ```

- Warning: `workflows/genomeannotator.nf:100:20`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_genome_rm = Channel.empty()
                     ^^^^^^^
  ```

- Warning: `workflows/genomeannotator.nf:101:22`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_proteins_fa = Channel.empty()
                       ^^^^^^^
  ```

- Warning: `workflows/genomeannotator.nf:102:19`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_busco_qc = Channel.empty()
                    ^^^^^^^
  ```

- Warning: `workflows/genomeannotator.nf:159:50`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
         ch_repeats = REPEATMODELER.out.fasta.map {m,fasta -> fasta}
                                                   ^
  ```

- Warning: `workflows/genomeannotator.nf:274:33`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
             ch_transcripts.map { m,t -> t }.collectFile(name: "transcripts.merged.fa").map { it ->
                                  ^
  ```

- Warning: `workflows/genomeannotator.nf:326:28`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
            ch_genes_gff.map{m,g -> g}.collectFile(name: 'genes.gff3'),
                             ^
  ```

- Warning: `workflows/genomeannotator.nf:327:31`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
            ch_proteins_gff.map{m,p -> p}.mix(ch_empty_gff).collectFile(name: 'proteins.gff3'),
                                ^
  ```

- Warning: `workflows/genomeannotator.nf:328:34`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
            ch_transcripts_gff.map{m,t ->t}.mix(ch_empty_gff).collectFile(name: 'transcripts.gff3'),
                                   ^
  ```

- Warning: `workflows/genomeannotator.nf:358:27`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_workflow_summary = Channel.value(workflow_summary)
                            ^^^^^^^
  ```

- Warning: `workflows/genomeannotator.nf:360:24`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_multiqc_files = Channel.empty()
                         ^^^^^^^
  ```

- Warning: `workflows/genomeannotator.nf:361:45`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_multiqc_files = ch_multiqc_files.mix(Channel.from(ch_multiqc_config))
                                              ^^^^^^^
  ```

- Warning: `workflows/genomeannotator.nf:370:5`: Variable was declared but not used

  ```nextflow
      multiqc_report = MULTIQC.out.report.toList()
      ^^^^^^^^^^^^^^
  ```
