# Nextflow lint results

- Generated: 2026-01-14T09:18:45.328521305Z
- Nextflow version: 25.12.0-edge
- Summary: 89 errors, 122 warnings

## :x: Errors

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

- Error: `conf/base.config:28:20`: `check_max` is not defined

  ```nextflow
          cpus   = { check_max( 1                  , 'cpus'    ) }
                     ^^^^^^^^^
  ```

- Error: `conf/base.config:29:20`: `check_max` is not defined

  ```nextflow
          memory = { check_max( 6.GB * task.attempt, 'memory'  ) }
                     ^^^^^^^^^
  ```

- Error: `conf/base.config:30:20`: `check_max` is not defined

  ```nextflow
          time   = { check_max( 4.h  * task.attempt, 'time'    ) }
                     ^^^^^^^^^
  ```

- Error: `conf/base.config:33:20`: `check_max` is not defined

  ```nextflow
          cpus   = { check_max( 2     * task.attempt, 'cpus'    ) }
                     ^^^^^^^^^
  ```

- Error: `conf/base.config:34:20`: `check_max` is not defined

  ```nextflow
          memory = { check_max( 12.GB * task.attempt, 'memory'  ) }
                     ^^^^^^^^^
  ```

- Error: `conf/base.config:35:20`: `check_max` is not defined

  ```nextflow
          time   = { check_max( 4.h   * task.attempt, 'time'    ) }
                     ^^^^^^^^^
  ```

- Error: `conf/base.config:38:20`: `check_max` is not defined

  ```nextflow
          cpus   = { check_max( 6     * task.attempt, 'cpus'    ) }
                     ^^^^^^^^^
  ```

- Error: `conf/base.config:39:20`: `check_max` is not defined

  ```nextflow
          memory = { check_max( 36.GB * task.attempt, 'memory'  ) }
                     ^^^^^^^^^
  ```

- Error: `conf/base.config:40:20`: `check_max` is not defined

  ```nextflow
          time   = { check_max( 8.h   * task.attempt, 'time'    ) }
                     ^^^^^^^^^
  ```

- Error: `conf/base.config:43:20`: `check_max` is not defined

  ```nextflow
          cpus   = { check_max( 12    * task.attempt, 'cpus'    ) }
                     ^^^^^^^^^
  ```

- Error: `conf/base.config:44:20`: `check_max` is not defined

  ```nextflow
          memory = { check_max( 72.GB * task.attempt, 'memory'  ) }
                     ^^^^^^^^^
  ```

- Error: `conf/base.config:45:20`: `check_max` is not defined

  ```nextflow
          time   = { check_max( 16.h  * task.attempt, 'time'    ) }
                     ^^^^^^^^^
  ```

- Error: `conf/base.config:48:20`: `check_max` is not defined

  ```nextflow
          time   = { check_max( 48.h  * task.attempt, 'time'    ) }
                     ^^^^^^^^^
  ```

- Error: `conf/base.config:51:20`: `check_max` is not defined

  ```nextflow
          memory = { check_max( 200.GB * task.attempt, 'memory' ) }
                     ^^^^^^^^^
  ```

- Error: `conf/base.config:54:20`: `check_max` is not defined

  ```nextflow
          cpus   = { check_max( 16    * task.attempt, 'cpus'    ) }
                     ^^^^^^^^^
  ```

- Error: `conf/modules.config:208:1`: If statements cannot be mixed with config statements

  ```nextflow
  if(!params.skip_cutadapt){
  ^
  ```

- Error: `conf/modules.config:222:25`: `check_max` is not defined

  ```nextflow
          time        = { check_max( 32.h  * task.attempt, 'time'    ) }
                          ^^^^^^^^^
  ```

- Error: `main.nf:20:21`: `WorkflowMain` is not defined

  ```nextflow
  params.fasta      = WorkflowMain.getGenomeAttribute(params, 'fasta')
                      ^^^^^^^^^^^^
  ```

- Error: `main.nf:21:21`: `WorkflowMain` is not defined

  ```nextflow
  params.bwa_index  = WorkflowMain.getGenomeAttribute(params, 'bwa')
                      ^^^^^^^^^^^^
  ```

- Error: `main.nf:22:21`: `WorkflowMain` is not defined

  ```nextflow
  params.gtf        = WorkflowMain.getGenomeAttribute(params, 'gtf')
                      ^^^^^^^^^^^^
  ```

- Error: `main.nf:23:21`: `WorkflowMain` is not defined

  ```nextflow
  params.gff        = WorkflowMain.getGenomeAttribute(params, 'gff')
                      ^^^^^^^^^^^^
  ```

- Error: `main.nf:24:21`: `WorkflowMain` is not defined

  ```nextflow
  params.gene_bed   = WorkflowMain.getGenomeAttribute(params, 'bed12')
                      ^^^^^^^^^^^^
  ```

- Error: `main.nf:25:21`: `WorkflowMain` is not defined

  ```nextflow
  params.macs_gsize = WorkflowMain.getGenomeAttribute(params, 'macs_gsize')
                      ^^^^^^^^^^^^
  ```

- Error: `main.nf:26:1`: Statements cannot be mixed with script declarations -- move statements into a process or workflow

  ```nextflow
  anno_readme       = WorkflowMain.getGenomeAttribute(params, 'readme')
  ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  ```

- Error: `main.nf:26:21`: `WorkflowMain` is not defined

  ```nextflow
  anno_readme       = WorkflowMain.getGenomeAttribute(params, 'readme')
                      ^^^^^^^^^^^^
  ```

- Error: `main.nf:28:1`: Statements cannot be mixed with script declarations -- move statements into a process or workflow

  ```nextflow
  if (anno_readme && file(anno_readme).exists()) {
  ^
  ```

- Error: `main.nf:42:1`: Statements cannot be mixed with script declarations -- move statements into a process or workflow

  ```nextflow
  if (params.help) {
  ^
  ```

- Error: `main.nf:43:16`: `NfcoreTemplate` is not defined

  ```nextflow
      def logo = NfcoreTemplate.logo(workflow, params.monochrome_logs)
                 ^^^^^^^^^^^^^^
  ```

- Error: `main.nf:44:27`: `WorkflowMain` is not defined

  ```nextflow
      def citation = '\n' + WorkflowMain.citation(workflow) + '\n'
                            ^^^^^^^^^^^^
  ```

- Error: `main.nf:46:54`: `NfcoreTemplate` is not defined

  ```nextflow
      log.info logo + paramsHelp(command) + citation + NfcoreTemplate.dashedLine(params.monochrome_logs)
                                                       ^^^^^^^^^^^^^^
  ```

- Error: `main.nf:51:1`: Statements cannot be mixed with script declarations -- move statements into a process or workflow

  ```nextflow
  if (params.validate_params) {
  ^
  ```

- Error: `main.nf:55:1`: Statements cannot be mixed with script declarations -- move statements into a process or workflow

  ```nextflow
  WorkflowMain.initialise(workflow, params, log)
  ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  ```

- Error: `main.nf:55:1`: `WorkflowMain` is not defined

  ```nextflow
  WorkflowMain.initialise(workflow, params, log)
  ^^^^^^^^^^^^
  ```

- Error: `main.nf:63:1`: Module could not be parsed: '/home/runner/work/strict-syntax-health/strict-syntax-health/pipelines/hicar/workflows/hicar.nf'

  ```nextflow
  include { HICAR } from './workflows/hicar'
  ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  ```

- Error: `main.nf:69:5`: `HICAR` is not defined

  ```nextflow
      HICAR ()
      ^^^^^
  ```

- Error: `modules/local/bioc/enrich.nf:23:56`: `options` is not defined

  ```nextflow
      enrich.r -s ${ucscname} -o "${prefix}/enrichment" $options.args
                                                         ^^^^^^^
  ```

- Error: `modules/local/cooltools/virtual4c.nf:17:13`: `prefix` is not defined

  ```nextflow
      path "${prefix}/*"            , emit: v4c
              ^^^^^^
  ```

- Error: `modules/local/hicexplorer/hicfindtads.nf:26:10`: Unexpected input: '='

  ```nextflow
      for(i=0; i<2; i++){
           ^
  ```

- Error: `modules/local/hipeak/diff_hipeak.nf:5:5`: Invalid process directive

  ```nextflow
      if (workflow.containerEngine == 'singularity' && !params.singularity_pull_docker_container) {
      ^
  ```

- Error: `modules/nf-core/bwa/index/main.nf:14:27`: `bwa` is not defined

  ```nextflow
      tuple val(meta), path(bwa) , emit: index
                            ^^^
  ```

- Error: `nextflow.config:174:5`: Unexpected input: 'includeConfig'

  ```nextflow
      includeConfig "${params.custom_config_base}/nfcore_custom.config"
      ^
  ```

- Error: `subworkflows/local/apa.nf:25:28`: Unexpected input: '\n'

  ```nextflow
          case "hicexplorer":
                             ^
  ```

- Error: `subworkflows/local/callatacpeak.nf:5:5`: Unexpected input: 'as'

  ```nextflow
      as  PAIRTOOLS_SELECT_SHORT              } from '../../modules/nf-core/pairtools/select/main'
      ^
  ```

- Error: `subworkflows/local/compartments.nf:25:26`: Unexpected input: '\n'

  ```nextflow
          case "cooltools":
                           ^
  ```

- Error: `subworkflows/local/compartments_caller/hicexplorer.nf:8:5`: Unexpected input: 'as'

  ```nextflow
      as HICEXPLORER_HICPLOTMATRIX_PCA1 } from '../../../modules/local/hicexplorer/hicplotmatrix'
      ^
  ```

- Error: `subworkflows/local/compartments_caller/homer.nf:10:9`: Unexpected input: 'as'

  ```nextflow
          as UCSC_BEDGRAPHTOBIGWIG_HOMER_COMPARTMENTS } from '../../../modules/nf-core/ucsc/bedgraphtobigwig/main'
          ^
  ```

- Error: `subworkflows/local/compartments_caller/juicer.nf:7:5`: Unexpected input: 'as'

  ```nextflow
      as WIG_TRIM } from '../../../modules/local/bioc/trimbedgraph'
      ^
  ```

- Error: `subworkflows/local/cooler.nf:10:5`: Unexpected input: 'as'

  ```nextflow
      as COOLER_DUMP_PER_GROUP    } from '../../modules/nf-core/cooler/dump/main'
      ^
  ```

- Error: `subworkflows/local/differential_analysis.nf:38:26`: Unexpected input: '\n'

  ```nextflow
              case "edger":
                           ^
  ```

- Error: `subworkflows/local/hipeak.nf:5:1`: Module could not be parsed: '/home/runner/work/strict-syntax-health/strict-syntax-health/pipelines/hicar/subworkflows/local/hipeak/fragment_peak.nf'

  ```nextflow
  include { R1_PEAK } from './hipeak/fragment_peak'
  ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  ```

- Error: `subworkflows/local/hipeak.nf:6:1`: Module could not be parsed: '/home/runner/work/strict-syntax-health/strict-syntax-health/pipelines/hicar/subworkflows/local/hipeak/call_hipeak.nf'

  ```nextflow
  include { HI_PEAK } from './hipeak/call_hipeak'
  ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  ```

- Error: `subworkflows/local/hipeak.nf:29:5`: `R1_PEAK` is not defined

  ```nextflow
      R1_PEAK(
      ^^^^^^^
  ```

- Error: `subworkflows/local/hipeak.nf:37:35`: `R1_PEAK` is not defined

  ```nextflow
      ch_versions = ch_versions.mix(R1_PEAK.out.versions)
                                    ^^^^^^^
  ```

- Error: `subworkflows/local/hipeak.nf:47:35`: `R1_PEAK` is not defined

  ```nextflow
                              .join(R1_PEAK.out.peak.map{[it[0].id, it[1]]})
                                    ^^^^^^^
  ```

- Error: `subworkflows/local/hipeak.nf:50:5`: `HI_PEAK` is not defined

  ```nextflow
      HI_PEAK(
      ^^^^^^^
  ```

- Error: `subworkflows/local/hipeak.nf:61:35`: `HI_PEAK` is not defined

  ```nextflow
      ch_versions = ch_versions.mix(HI_PEAK.out.versions)
                                    ^^^^^^^
  ```

- Error: `subworkflows/local/hipeak.nf:68:23`: `HI_PEAK` is not defined

  ```nextflow
      ch_circos_files = HI_PEAK.out.bedpe
                        ^^^^^^^
  ```

- Error: `subworkflows/local/hipeak.nf:71:23`: `R1_PEAK` is not defined

  ```nextflow
      fragmentPeak    = R1_PEAK.out.peak
                        ^^^^^^^
  ```

- Error: `subworkflows/local/hipeak.nf:72:23`: `HI_PEAK` is not defined

  ```nextflow
      bed4tfea        = HI_PEAK.out.bed4tfea
                        ^^^^^^^
  ```

- Error: `subworkflows/local/hipeak/call_hipeak.nf:11:5`: Unexpected input: 'as'

  ```nextflow
      as BIOC_CHIPPEAKANNO_HIPEAK     } from '../../../modules/local/bioc/chippeakanno'
      ^
  ```

- Error: `subworkflows/local/hipeak/fragment_peak.nf:6:5`: Unexpected input: 'as'

  ```nextflow
      as MERGE_R1READS          } from '../../../modules/local/atacreads/mergereads'
      ^
  ```

- Error: `subworkflows/local/interaction_caller/maps.nf:5:1`: Module could not be parsed: '/home/runner/work/strict-syntax-health/strict-syntax-health/pipelines/hicar/subworkflows/local/interaction_caller/maps_multienzyme.nf'

  ```nextflow
  include { MAPS_MULTIENZYME } from './maps_multienzyme'
  ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  ```

- Error: `subworkflows/local/interaction_caller/maps.nf:6:1`: Module could not be parsed: '/home/runner/work/strict-syntax-health/strict-syntax-health/pipelines/hicar/subworkflows/local/interaction_caller/maps_peak.nf'

  ```nextflow
  include { MAPS_PEAK        } from './maps_peak'
  ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  ```

- Error: `subworkflows/local/interaction_caller/maps.nf:21:18`: `MAPS_MULTIENZYME` is not defined

  ```nextflow
      background = MAPS_MULTIENZYME(
                   ^^^^^^^^^^^^^^^^
  ```

- Error: `subworkflows/local/interaction_caller/maps.nf:25:19`: `MAPS_MULTIENZYME` is not defined

  ```nextflow
      ch_versions = MAPS_MULTIENZYME.out.versions
                    ^^^^^^^^^^^^^^^^
  ```

- Error: `subworkflows/local/interaction_caller/maps.nf:28:33`: `reads` is already declared

  ```nextflow
                      .map{ meta, reads, peaks ->
                                  ^^^^^
  ```

- Error: `subworkflows/local/interaction_caller/maps.nf:34:23`: `background` is already declared

  ```nextflow
                  .map{ background, reads -> //[group, bin_size, macs2, long_bedpe, short_bed, background]
                        ^^^^^^^^^^
  ```

- Error: `subworkflows/local/interaction_caller/maps.nf:34:35`: `reads` is already declared

  ```nextflow
                  .map{ background, reads -> //[group, bin_size, macs2, long_bedpe, short_bed, background]
                                    ^^^^^
  ```

- Error: `subworkflows/local/interaction_caller/maps.nf:37:5`: `MAPS_PEAK` is not defined

  ```nextflow
      MAPS_PEAK(
      ^^^^^^^^^
  ```

- Error: `subworkflows/local/interaction_caller/maps.nf:41:35`: `MAPS_PEAK` is not defined

  ```nextflow
      ch_versions = ch_versions.mix(MAPS_PEAK.out.versions)
                                    ^^^^^^^^^
  ```

- Error: `subworkflows/local/interaction_caller/maps.nf:42:24`: `MAPS_PEAK` is not defined

  ```nextflow
      ch_multiqc_files = MAPS_PEAK.out.stats.collect().ifEmpty(null)
                         ^^^^^^^^^
  ```

- Error: `subworkflows/local/interaction_caller/maps.nf:45:20`: `MAPS_PEAK` is not defined

  ```nextflow
      interactions = MAPS_PEAK.out.peak           // channel: [ meta, bin_size, path(bedpe) ]
                     ^^^^^^^^^
  ```

- Error: `subworkflows/local/interaction_caller/maps_multienzyme.nf:11:9`: Unexpected input: 'as'

  ```nextflow
          as ENSEMBL_UCSC_CONVERT1;
          ^
  ```

- Error: `subworkflows/local/interaction_caller/maps_peak.nf:8:5`: Unexpected input: 'as'

  ```nextflow
      as MAPS_STATS               } from '../../../modules/local/reads_summary'
      ^
  ```

- Error: `subworkflows/local/interactions.nf:30:21`: Unexpected input: '\n'

  ```nextflow
          case "maps":
                      ^
  ```

- Error: `subworkflows/local/pairtools.nf:14:9`: Unexpected input: 'as'

  ```nextflow
          as PAIRTOOLS_SELECT_VP;
          ^
  ```

- Error: `subworkflows/local/tads.nf:28:26`: Unexpected input: '\n'

  ```nextflow
          case "cooltools":
                           ^
  ```

- Error: `subworkflows/local/tads_caller/hicexplorer.nf:5:1`: Module could not be parsed: '/home/runner/work/strict-syntax-health/strict-syntax-health/pipelines/hicar/modules/local/hicexplorer/hicfindtads.nf'

  ```nextflow
  include { HICEXPLORER_HICFINDTADS } from '../../../modules/local/hicexplorer/hicfindtads'
  ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  ```

- Error: `subworkflows/local/tads_caller/hicexplorer.nf:18:5`: `HICEXPLORER_HICFINDTADS` is not defined

  ```nextflow
      HICEXPLORER_HICFINDTADS(
      ^^^^^^^^^^^^^^^^^^^^^^^
  ```

- Error: `subworkflows/local/tads_caller/hicexplorer.nf:22:18`: `HICEXPLORER_HICFINDTADS` is not defined

  ```nextflow
      ch_version = HICEXPLORER_HICFINDTADS.out.versions
                   ^^^^^^^^^^^^^^^^^^^^^^^
  ```

- Error: `subworkflows/local/tads_caller/hicexplorer.nf:25:19`: `HICEXPLORER_HICFINDTADS` is not defined

  ```nextflow
          cool.join(HICEXPLORER_HICFINDTADS.out.tads),
                    ^^^^^^^^^^^^^^^^^^^^^^^
  ```

- Error: `subworkflows/local/tads_caller/hicexplorer.nf:31:17`: `HICEXPLORER_HICFINDTADS` is not defined

  ```nextflow
      tads      = HICEXPLORER_HICFINDTADS.out.tads     // channel: [ val(meta), val(bin), path(domains.bed)]
                  ^^^^^^^^^^^^^^^^^^^^^^^
  ```

- Error: `subworkflows/local/tads_caller/homer.nf:6:5`: Unexpected input: 'as'

  ```nextflow
      as HOMER_FINDTADSANDLOOPS_TADS        } from '../../../modules/local/homer/find_tad_loops'
      ^
  ```

- Error: `subworkflows/local/tfea.nf:17:22`: Unexpected input: '\n'

  ```nextflow
          case "homer":
                       ^
  ```

- Error: `subworkflows/local/v4c.nf:22:26`: Unexpected input: '\n'

  ```nextflow
          case "cooltools":
                           ^
  ```

- Error: `workflows/hicar.nf:643:21`: Unexpected input: '\n'

  ```nextflow
          case 'maps':
                      ^
  ```

## :warning: Warnings

- Warning: `modules/local/atacreads/dumpreads.nf:21:9`: Variable was declared but not used

  ```nextflow
      def software = "awk"
          ^^^^^^^^
  ```

- Warning: `modules/local/bioc/bedpe2bed.nf:19:9`: Variable was declared but not used

  ```nextflow
      def args = task.ext.args ?: ''
          ^^^^
  ```

- Warning: `modules/local/bioc/merge_interactions.nf:19:9`: Variable was declared but not used

  ```nextflow
      def args = task.ext.args ?: ''
          ^^^^
  ```

- Warning: `modules/local/bioc/pair2bam.nf:20:9`: Variable was declared but not used

  ```nextflow
      def prefix   = task.ext.prefix ?: "${meta.id}"
          ^^^^^^
  ```

- Warning: `modules/local/bioc/subsetloops.nf:21:9`: Variable was declared but not used

  ```nextflow
      def args = task.ext.args ?: ''
          ^^^^
  ```

- Warning: `modules/local/cooltools/plotnpz.nf:20:9`: Variable was declared but not used

  ```nextflow
      def args = task.ext.args ?: ''
          ^^^^
  ```

- Warning: `modules/local/hicexplorer/hicpca.nf:23:33`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
      def idx = args.findIndexOf{ it == '--format' | it == '-f' }
                                  ^^
  ```

- Warning: `modules/local/hicexplorer/hicpca.nf:23:52`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
      def idx = args.findIndexOf{ it == '--format' | it == '-f' }
                                                     ^^
  ```

- Warning: `modules/local/hicexplorer/hicpca.nf:38:34`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          .collect{"${prefix}_pca${it}.${format}"}.join(' ')
                                   ^^
  ```

- Warning: `modules/local/hichipper/create_yaml.nf:20:9`: Variable was declared but not used

  ```nextflow
      def args = task.ext.args ?: ''
          ^^^^
  ```

- Warning: `modules/local/hipeak/post_counts.nf:19:9`: Variable was declared but not used

  ```nextflow
      def args   = task.ext.args ?: ''
          ^^^^
  ```

- Warning: `modules/local/homer/find_tad_loops.nf:25:9`: Variable was declared but not used

  ```nextflow
      def prefix = task.ext.prefix ?: "${meta.id}"
          ^^^^^^
  ```

- Warning: `modules/local/homer/install.nf:22:9`: Variable was declared but not used

  ```nextflow
      def args = task.ext.args ?: ''
          ^^^^
  ```

- Warning: `modules/local/juicer/eigenvector.nf:33:21`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
      args.removeIf { it.contains('NONE') }
                      ^^
  ```

- Warning: `modules/local/juicer/eigenvector.nf:34:21`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
      args.removeIf { it.contains('VC_SQRT') }
                      ^^
  ```

- Warning: `modules/local/juicer/eigenvector.nf:35:21`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
      args.removeIf { it.contains('VC') }
                      ^^
  ```

- Warning: `modules/local/juicer/eigenvector.nf:36:21`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
      args.removeIf { it.contains('KR') }
                      ^^
  ```

- Warning: `modules/local/juicer/eigenvector.nf:37:21`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
      args.removeIf { it.contains('SCALE') }
                      ^^
  ```

- Warning: `modules/local/juicer/eigenvector.nf:38:21`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
      args.removeIf { it.contains('BP') }
                      ^^
  ```

- Warning: `modules/local/juicer/eigenvector.nf:39:21`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
      args.removeIf { it.contains('FRAG') }
                      ^^
  ```

- Warning: `modules/local/maps/raw2bg2.nf:20:9`: Variable was declared but not used

  ```nextflow
      def args   = task.ext.args ?: ''
          ^^^^
  ```

- Warning: `modules/local/peakachu/model.nf:21:9`: Variable was declared but not used

  ```nextflow
      def args = task.ext.args ?: ''
          ^^^^
  ```

- Warning: `modules/nf-core/cat/cat/main.nf:23:40`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
      def file_list = files_in.collect { it.toString() }
                                         ^^
  ```

- Warning: `modules/nf-core/cat/cat/main.nf:52:40`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
      def file_list = files_in.collect { it.toString() }
                                         ^^
  ```

- Warning: `modules/nf-core/custom/dumpsoftwareversions/main.nf:22:9`: Variable was declared but not used

  ```nextflow
      def args = task.ext.args ?: ''
          ^^^^
  ```

- Warning: `modules/nf-core/fastqc/main.nf:27:48`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
      def renamed_files = old_new_pairs.collect{ old_name, new_name -> new_name }.join(' ')
                                                 ^^^^^^^^
  ```

- Warning: `modules/nf-core/genmap/index/main.nf:21:9`: Variable was declared but not used

  ```nextflow
      def args = task.ext.args ?: ''
          ^^^^
  ```

- Warning: `modules/nf-core/macs2/callpeak/main.nf:33:40`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          def id = args_list.findIndexOf{it=='--format'}
                                         ^^
  ```

- Warning: `modules/nf-core/samtools/flagstat/main.nf:21:9`: Variable was declared but not used

  ```nextflow
      def args = task.ext.args ?: ''
          ^^^^
  ```

- Warning: `modules/nf-core/samtools/idxstats/main.nf:21:9`: Variable was declared but not used

  ```nextflow
      def args = task.ext.args ?: ''
          ^^^^
  ```

- Warning: `modules/nf-core/samtools/stats/main.nf:22:9`: Variable was declared but not used

  ```nextflow
      def args = task.ext.args ?: ''
          ^^^^
  ```

- Warning: `modules/nf-core/ucsc/bedclip/main.nf:23:9`: Variable was declared but not used

  ```nextflow
      def args = task.ext.args ?: ''
          ^^^^
  ```

- Warning: `modules/nf-core/ucsc/bedgraphtobigwig/main.nf:23:9`: Variable was declared but not used

  ```nextflow
      def args = task.ext.args ?: ''
          ^^^^
  ```

- Warning: `subworkflows/local/apa/juicer.nf:13:5`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
      format                 // output plot format
      ^^^^^^
  ```

- Warning: `subworkflows/local/apa/juicer.nf:16:44`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
      ch_mergedloops = additional_param.map{[it[0], it[1]]}
                                             ^^
  ```

- Warning: `subworkflows/local/apa/juicer.nf:16:51`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
      ch_mergedloops = additional_param.map{[it[0], it[1]]}
                                                    ^^
  ```

- Warning: `subworkflows/local/apa/juicer.nf:19:32`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
      ch_hic_loops = matrix.map{[it[0].bin, it[0], it[1]]}
                                 ^^
  ```

- Warning: `subworkflows/local/apa/juicer.nf:19:43`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
      ch_hic_loops = matrix.map{[it[0].bin, it[0], it[1]]}
                                            ^^
  ```

- Warning: `subworkflows/local/apa/juicer.nf:19:50`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
      ch_hic_loops = matrix.map{[it[0].bin, it[0], it[1]]}
                                                   ^^
  ```

- Warning: `subworkflows/local/apa/juicer.nf:21:31`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
                          .map{[it[1], it[2], it[3]]} // merge by bin
                                ^^
  ```

- Warning: `subworkflows/local/apa/juicer.nf:21:38`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
                          .map{[it[1], it[2], it[3]]} // merge by bin
                                       ^^
  ```

- Warning: `subworkflows/local/apa/juicer.nf:21:45`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
                          .map{[it[1], it[2], it[3]]} // merge by bin
                                              ^^
  ```

- Warning: `subworkflows/local/apa/juicer.nf:25:31`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          additional_param.map{[it[2]]}
                                ^^
  ```

- Warning: `subworkflows/local/coveragescale.nf:12:31`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_versions             = Channel.empty()
                                ^^^^^^^
  ```

- Warning: `subworkflows/local/coveragescale.nf:14:27`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
      min_cnt = counts.map{[it[1].toInteger()]}.collect().map{it.min()}
                            ^^
  ```

- Warning: `subworkflows/local/coveragescale.nf:14:61`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
      min_cnt = counts.map{[it[1].toInteger()]}.collect().map{it.min()}
                                                              ^^
  ```

- Warning: `subworkflows/local/diff_ana/chicdiff.nf:31:23`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      anno            = Channel.empty()      // [bin_size, prefix, [files]]
                        ^^^^^^^
  ```

- Warning: `subworkflows/local/hipeak.nf:23:31`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_versions             = Channel.empty()
                                ^^^^^^^
  ```

- Warning: `subworkflows/local/hipeak.nf:24:31`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_multiqc_files        = Channel.empty()
                                ^^^^^^^
  ```

- Warning: `subworkflows/local/hipeak.nf:25:31`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_circos_files         = Channel.empty()
                                ^^^^^^^
  ```

- Warning: `subworkflows/local/hipeak.nf:26:31`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_track_files          = Channel.empty()
                                ^^^^^^^
  ```

- Warning: `subworkflows/local/hipeak.nf:27:31`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_annotation_files     = Channel.empty()
                                ^^^^^^^
  ```

- Warning: `subworkflows/local/hipeak.nf:46:36`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
      grouped_reads_peak = peak.map{[it[0].id, it[1]]}
                                     ^^
  ```

- Warning: `subworkflows/local/hipeak.nf:46:46`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
      grouped_reads_peak = peak.map{[it[0].id, it[1]]}
                                               ^^
  ```

- Warning: `subworkflows/local/hipeak.nf:47:57`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
                              .join(R1_PEAK.out.peak.map{[it[0].id, it[1]]})
                                                          ^^
  ```

- Warning: `subworkflows/local/hipeak.nf:47:67`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
                              .join(R1_PEAK.out.peak.map{[it[0].id, it[1]]})
                                                                    ^^
  ```

- Warning: `subworkflows/local/hipeak.nf:49:39`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
                              .map{[[id:it[0]], it[1], it[2], it[3]]}
                                        ^^
  ```

- Warning: `subworkflows/local/hipeak.nf:49:47`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
                              .map{[[id:it[0]], it[1], it[2], it[3]]}
                                                ^^
  ```

- Warning: `subworkflows/local/hipeak.nf:49:54`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
                              .map{[[id:it[0]], it[1], it[2], it[3]]}
                                                       ^^
  ```

- Warning: `subworkflows/local/hipeak.nf:49:61`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
                              .map{[[id:it[0]], it[1], it[2], it[3]]}
                                                              ^^
  ```

- Warning: `subworkflows/local/interaction_caller/hicdcplus.nf:20:24`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_multiqc_files = Channel.empty()
                         ^^^^^^^
  ```

- Warning: `subworkflows/local/interaction_caller/hicdcplus.nf:21:15`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_loop = Channel.empty()
                ^^^^^^^
  ```

- Warning: `subworkflows/local/interaction_caller/hicdcplus.nf:25:33`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
                      bedpe.map{[ it[0].bin ]} // bin_size
                                  ^^
  ```

- Warning: `subworkflows/local/interaction_caller/hicdcplus.nf:31:47`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
                                      .map{[[id:it[0].id, bin:it[2]],
                                                ^^
  ```

- Warning: `subworkflows/local/interaction_caller/hicdcplus.nf:31:61`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
                                      .map{[[id:it[0].id, bin:it[2]],
                                                              ^^
  ```

- Warning: `subworkflows/local/interaction_caller/hicdcplus.nf:32:41`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
                                          it[1], it[3]]}
                                          ^^
  ```

- Warning: `subworkflows/local/interaction_caller/hicdcplus.nf:32:48`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
                                          it[1], it[3]]}
                                                 ^^
  ```

- Warning: `subworkflows/local/interaction_caller/hicdcplus.nf:34:75`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
      ch_loop = HICDCPLUS_CALL_LOOPS(ch_reads.combine(additional_param.map{[it[2]]})).interactions
                                                                            ^^
  ```

- Warning: `subworkflows/local/interaction_caller/hicexplorer.nf:13:24`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_multiqc_files = Channel.empty()
                         ^^^^^^^
  ```

- Warning: `subworkflows/local/interaction_caller/hicexplorer.nf:14:15`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_loop = Channel.empty()
                ^^^^^^^
  ```

- Warning: `subworkflows/local/interaction_caller/hicexplorer.nf:15:19`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_versions = Channel.empty()
                    ^^^^^^^
  ```

- Warning: `subworkflows/local/interaction_caller/maps.nf:22:22`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          bedpe.map{ [ it[0].bin ] }.unique(),                   // bin_size
                       ^^
  ```

- Warning: `subworkflows/local/interaction_caller/maps.nf:23:32`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          additional_param.map{[ it[0], it[1], it[2], it[3] ]}   // site, fasta, chrom_size, mappability_bw
                                 ^^
  ```

- Warning: `subworkflows/local/interaction_caller/maps.nf:23:39`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          additional_param.map{[ it[0], it[1], it[2], it[3] ]}   // site, fasta, chrom_size, mappability_bw
                                        ^^
  ```

- Warning: `subworkflows/local/interaction_caller/maps.nf:23:46`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          additional_param.map{[ it[0], it[1], it[2], it[3] ]}   // site, fasta, chrom_size, mappability_bw
                                               ^^
  ```

- Warning: `subworkflows/local/interaction_caller/maps.nf:23:53`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          additional_param.map{[ it[0], it[1], it[2], it[3] ]}   // site, fasta, chrom_size, mappability_bw
                                                      ^^
  ```

- Warning: `subworkflows/local/interaction_caller/maps.nf:30:39`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
                      .cross(bedpe.map{[it[0].id, it[0].bin, it[1]]})// group, bin, bedpe
                                        ^^
  ```

- Warning: `subworkflows/local/interaction_caller/maps.nf:30:49`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
                      .cross(bedpe.map{[it[0].id, it[0].bin, it[1]]})// group, bin, bedpe
                                                  ^^
  ```

- Warning: `subworkflows/local/interaction_caller/maps.nf:30:60`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
                      .cross(bedpe.map{[it[0].id, it[0].bin, it[1]]})// group, bin, bedpe
                                                             ^^
  ```

- Warning: `subworkflows/local/interaction_caller/maps.nf:39:32`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          additional_param.map{[ it[1] ]},            //chrom_size
                                 ^^
  ```

- Warning: `subworkflows/local/interaction_caller/peakachu.nf:13:24`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_multiqc_files = Channel.empty()
                         ^^^^^^^
  ```

- Warning: `subworkflows/local/interaction_caller/peakachu.nf:14:15`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_loop = Channel.empty()
                ^^^^^^^
  ```

- Warning: `subworkflows/local/interaction_caller/peakachu.nf:19:73`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
      ch_loop = PEAKACHU_SCORE(cool.combine(PEAKACHU_MODEL.out.model.map{[it[0], file(it[1].trim(), checkIfExists:true)]}, by:0)).interactions
                                                                          ^^
  ```

- Warning: `subworkflows/local/interaction_caller/peakachu.nf:19:85`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
      ch_loop = PEAKACHU_SCORE(cool.combine(PEAKACHU_MODEL.out.model.map{[it[0], file(it[1].trim(), checkIfExists:true)]}, by:0)).interactions
                                                                                      ^^
  ```

- Warning: `subworkflows/local/preparegenome.nf:30:48`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          ch_fasta = GUNZIP_FASTA.out.gunzip.map{it[1]}
                                                 ^^
  ```

- Warning: `subworkflows/local/preparegenome.nf:38:18`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_version = Channel.empty()
                   ^^^^^^^
  ```

- Warning: `subworkflows/local/preparegenome.nf:39:14`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_gtf = Channel.empty()
               ^^^^^^^
  ```

- Warning: `subworkflows/local/preparegenome.nf:43:48`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
              ch_gtf = GUNZIP_GTF.out.gunzip.map{it[1]}
                                                 ^^
  ```

- Warning: `subworkflows/local/preparegenome.nf:50:48`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
              ch_gff = GUNZIP_GFF.out.gunzip.map{it[1]}
                                                 ^^
  ```

- Warning: `subworkflows/local/preparegenome.nf:61:19`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_gene_bed = Channel.empty()
                    ^^^^^^^
  ```

- Warning: `subworkflows/local/preparegenome.nf:65:58`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
              ch_gene_bed = GUNZIP_GENE_BED.out.gunzip.map{it[1]}
                                                           ^^
  ```

- Warning: `subworkflows/local/preparegenome.nf:90:20`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
              .map { it.seqString.replaceAll('[^acgtACGT]','').length() }
                     ^^
  ```

- Warning: `subworkflows/local/preparegenome.nf:119:24`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
          ch_blacklist = Channel.fromPath(params.blacklist, checkIfExists: true)
                         ^^^^^^^
  ```

- Warning: `subworkflows/local/preparegenome.nf:120:29`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      } else { ch_blacklist = Channel.empty() }
                              ^^^^^^^
  ```

- Warning: `subworkflows/local/preparegenome.nf:152:65`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
              GENMAP_MAPPABILITY.out.wig.map{[[id:'mappability'], it]},
                                                                  ^^
  ```

- Warning: `subworkflows/local/preparegenome.nf:153:36`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
              ch_chrom_sizes).bw.map{it[1]}
                                     ^^
  ```

- Warning: `subworkflows/local/preparegenome.nf:156:26`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
          ch_mappability = Channel.fromPath(params.mappability, checkIfExists: true)
                           ^^^^^^^
  ```

- Warning: `subworkflows/local/preparegenome.nf:162:39`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_bwa_index = params.bwa_index ? Channel.value(file(params.bwa_index)).map{ [['id':ucscname], it] } : BWA_INDEX ( ch_fasta.map{[['id':ucscname], it]} ).index
                                        ^^^^^^^
  ```

- Warning: `subworkflows/local/preparegenome.nf:162:100`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
      ch_bwa_index = params.bwa_index ? Channel.value(file(params.bwa_index)).map{ [['id':ucscname], it] } : BWA_INDEX ( ch_fasta.map{[['id':ucscname], it]} ).index
                                                                                                     ^^
  ```

- Warning: `subworkflows/local/preparegenome.nf:162:151`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
      ch_bwa_index = params.bwa_index ? Channel.value(file(params.bwa_index)).map{ [['id':ucscname], it] } : BWA_INDEX ( ch_fasta.map{[['id':ucscname], it]} ).index
                                                                                                                                                        ^^
  ```

- Warning: `subworkflows/local/tads_caller/cooltools.nf:13:24`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_multiqc_files = Channel.empty()
                         ^^^^^^^
  ```

- Warning: `subworkflows/local/tads_caller/cooltools.nf:14:19`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_versions = Channel.empty()
                    ^^^^^^^
  ```

- Warning: `subworkflows/local/tads_caller/hicexplorer.nf:15:24`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_multiqc_files = Channel.empty()
                         ^^^^^^^
  ```

- Warning: `subworkflows/local/tads_caller/hicexplorer.nf:16:5`: Variable was declared but not used

  ```nextflow
      ch_versions      = Channel.empty()
      ^^^^^^^^^^^
  ```

- Warning: `subworkflows/local/tads_caller/hicexplorer.nf:16:24`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_versions      = Channel.empty()
                         ^^^^^^^
  ```

- Warning: `subworkflows/local/tfea/homer.nf:15:19`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_versions = Channel.empty()
                    ^^^^^^^
  ```

- Warning: `subworkflows/local/tfea/homer.nf:19:50`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          seqlevelsstyle = SEQLEVELS_STYLE(bed.map{it[2]}.collect().map{it[0]}).seqlevels_style
                                                   ^^
  ```

- Warning: `subworkflows/local/tfea/homer.nf:19:71`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          seqlevelsstyle = SEQLEVELS_STYLE(bed.map{it[2]}.collect().map{it[0]}).seqlevels_style
                                                                        ^^
  ```

- Warning: `subworkflows/local/tfea/homer.nf:22:31`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
              ch_bed = bed.map{[it[0].id, it[0], it[1], it[2]]}
                                ^^
  ```

- Warning: `subworkflows/local/tfea/homer.nf:22:41`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
              ch_bed = bed.map{[it[0].id, it[0], it[1], it[2]]}
                                          ^^
  ```

- Warning: `subworkflows/local/tfea/homer.nf:22:48`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
              ch_bed = bed.map{[it[0].id, it[0], it[1], it[2]]}
                                                 ^^
  ```

- Warning: `subworkflows/local/tfea/homer.nf:22:55`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
              ch_bed = bed.map{[it[0].id, it[0], it[1], it[2]]}
                                                        ^^
  ```

- Warning: `subworkflows/local/tfea/homer.nf:23:74`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
              ch_new_bed = ch_bed.combine(ENSEMBL_UCSC_CONVERT(ch_bed.map{[it[0], it[3]]}).tab, by:0)
                                                                           ^^
  ```

- Warning: `subworkflows/local/tfea/homer.nf:23:81`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
              ch_new_bed = ch_bed.combine(ENSEMBL_UCSC_CONVERT(ch_bed.map{[it[0], it[3]]}).tab, by:0)
                                                                                  ^^
  ```

- Warning: `subworkflows/local/tfea/homer.nf:24:35`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
                              .map{[it[1], it[2], it[4]]}
                                    ^^
  ```

- Warning: `subworkflows/local/tfea/homer.nf:24:42`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
                              .map{[it[1], it[2], it[4]]}
                                           ^^
  ```

- Warning: `subworkflows/local/tfea/homer.nf:24:49`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
                              .map{[it[1], it[2], it[4]]}
                                                  ^^
  ```

- Warning: `subworkflows/local/v4c/cooltools.nf:14:20`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          matrix.map{it[3]},
                     ^^
  ```

- Warning: `subworkflows/local/v4c/cooltools.nf:15:21`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          matrix.map{[it[0], it[2]]}).versions
                      ^^
  ```

- Warning: `subworkflows/local/v4c/cooltools.nf:15:28`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          matrix.map{[it[0], it[2]]}).versions
                             ^^
  ```

- Warning: `subworkflows/local/v4c/cooltools.nf:17:21`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          matrix.map{[it[0], it[1]]}
                      ^^
  ```

- Warning: `subworkflows/local/v4c/cooltools.nf:17:28`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          matrix.map{[it[0], it[1]]}
                             ^^
  ```
