# Nextflow lint results

- Generated: 2026-01-16T10:20:30.972057769Z
- Nextflow version: 25.12.0-edge
- Summary: 121 errors, 380 warnings

## :x: Errors

- Error: `conf/modules.config:1025:15`: `meta` is not defined

  ```nextflow
              { meta.strandedness } == "single" ? '--singleStranded' : '',
                ^^^^
  ```

- Error: `conf/modules.config:1404:15`: `meta` is not defined

  ```nextflow
              { meta.strandedness } == "single" ? '--singleStranded' : '',
                ^^^^
  ```

- Error: `main.nf:19:1`: Module could not be parsed: '/home/runner/work/strict-syntax-health/strict-syntax-health/pipelines/eager/subworkflows/local/utils_nfcore_eager_pipeline/main.nf'

  ```nextflow
  include { PIPELINE_INITIALISATION } from './subworkflows/local/utils_nfcore_eager_pipeline'
  ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  ```

- Error: `main.nf:20:1`: Module could not be parsed: '/home/runner/work/strict-syntax-health/strict-syntax-health/pipelines/eager/subworkflows/local/utils_nfcore_eager_pipeline/main.nf'

  ```nextflow
  include { PIPELINE_COMPLETION     } from './subworkflows/local/utils_nfcore_eager_pipeline'
  ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  ```

- Error: `main.nf:21:1`: Module could not be parsed: '/home/runner/work/strict-syntax-health/strict-syntax-health/pipelines/eager/subworkflows/local/utils_nfcore_eager_pipeline/main.nf'

  ```nextflow
  include { getGenomeAttribute      } from './subworkflows/local/utils_nfcore_eager_pipeline'
  ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  ```

- Error: `main.nf:32:16`: `getGenomeAttribute` is not defined

  ```nextflow
  params.fasta = getGenomeAttribute('fasta')
                 ^^^^^^^^^^^^^^^^^^
  ```

- Error: `main.nf:73:5`: `PIPELINE_INITIALISATION` is not defined

  ```nextflow
      PIPELINE_INITIALISATION (
      ^^^^^^^^^^^^^^^^^^^^^^^
  ```

- Error: `main.nf:86:9`: `PIPELINE_INITIALISATION` is not defined

  ```nextflow
          PIPELINE_INITIALISATION.out.samplesheet_fastqs,
          ^^^^^^^^^^^^^^^^^^^^^^^
  ```

- Error: `main.nf:87:9`: `PIPELINE_INITIALISATION` is not defined

  ```nextflow
          PIPELINE_INITIALISATION.out.samplesheet_bams,
          ^^^^^^^^^^^^^^^^^^^^^^^
  ```

- Error: `main.nf:92:5`: `PIPELINE_COMPLETION` is not defined

  ```nextflow
      PIPELINE_COMPLETION (
      ^^^^^^^^^^^^^^^^^^^
  ```

- Error: `modules/nf-core/bwa/index/main.nf:14:27`: `bwa` is not defined

  ```nextflow
      tuple val(meta), path(bwa) , emit: index
                            ^^^
  ```

- Error: `modules/nf-core/samtools/mpileup/main.nf:23:9`: `intervals` is already declared

  ```nextflow
      def intervals = intervals ? "-l ${intervals}" : ""
          ^^^^^^^^^
  ```

- Error: `modules/nf-core/samtools/view/main.nf:64:9`: `index` is already declared

  ```nextflow
      def index = args.contains("--write-index") ? "touch ${prefix}.csi" : ""
          ^^^^^
  ```

- Error: `nextflow.config:632:29`: `manifest` is not defined

  ```nextflow
  \033[0;35m  nf-core/eager ${manifest.version}\033[0m
                              ^^^^^^^^
  ```

- Error: `nextflow.config:635:36`: `manifest` is not defined

  ```nextflow
          afterText           = """${manifest.doi ? "\n* The pipeline\n" : ""}${manifest.doi.tokenize(",").collect { "    https://doi.org/${it.trim().replace('https://doi.org/', '')}" }.join("\n")}${manifest.doi ? "\n" : ""}
                                     ^^^^^^^^
  ```

- Error: `nextflow.config:635:79`: `manifest` is not defined

  ```nextflow
          afterText           = """${manifest.doi ? "\n* The pipeline\n" : ""}${manifest.doi.tokenize(",").collect { "    https://doi.org/${it.trim().replace('https://doi.org/', '')}" }.join("\n")}${manifest.doi ? "\n" : ""}
                                                                                ^^^^^^^^
  ```

- Error: `nextflow.config:635:198`: `manifest` is not defined

  ```nextflow
          afterText           = """${manifest.doi ? "\n* The pipeline\n" : ""}${manifest.doi.tokenize(",").collect { "    https://doi.org/${it.trim().replace('https://doi.org/', '')}" }.join("\n")}${manifest.doi ? "\n" : ""}
                                                                                                                                                                                                       ^^^^^^^^
  ```

- Error: `nextflow.config:644:22`: `validation` is not defined

  ```nextflow
          beforeText = validation.help.beforeText
                       ^^^^^^^^^^
  ```

- Error: `nextflow.config:645:22`: `validation` is not defined

  ```nextflow
          afterText  = validation.help.afterText
                       ^^^^^^^^^^
  ```

- Error: `subworkflows/local/calculate_damage.nf:5:1`: Module could not be parsed: '/home/runner/work/strict-syntax-health/strict-syntax-health/pipelines/eager/subworkflows/local/utils_nfcore_eager_pipeline/main.nf'

  ```nextflow
  include { addNewMetaFromAttributes           } from '../../subworkflows/local/utils_nfcore_eager_pipeline/main'
  ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  ```

- Error: `subworkflows/local/calculate_damage.nf:24:13`: `addNewMetaFromAttributes` is not defined

  ```nextflow
              addNewMetaFromAttributes( it, "id" , "reference" , false )
              ^^^^^^^^^^^^^^^^^^^^^^^^
  ```

- Error: `subworkflows/local/calculate_damage.nf:30:13`: `addNewMetaFromAttributes` is not defined

  ```nextflow
              addNewMetaFromAttributes( it, "reference" , "reference" , false )
              ^^^^^^^^^^^^^^^^^^^^^^^^
  ```

- Error: `subworkflows/local/calculate_damage.nf:37:51`: `fasta` is already declared

  ```nextflow
                  ignore_me, meta, bam, bai, meta2, fasta, fasta_fai ->
                                                    ^^^^^
  ```

- Error: `subworkflows/local/calculate_damage.nf:37:58`: `fasta_fai` is already declared

  ```nextflow
                  ignore_me, meta, bam, bai, meta2, fasta, fasta_fai ->
                                                           ^^^^^^^^^
  ```

- Error: `subworkflows/local/circularmapper.nf:8:1`: Module could not be parsed: '/home/runner/work/strict-syntax-health/strict-syntax-health/pipelines/eager/subworkflows/local/utils_nfcore_eager_pipeline/main.nf'

  ```nextflow
  include { addNewMetaFromAttributes                           } from '../../subworkflows/local/utils_nfcore_eager_pipeline/main'
  ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  ```

- Error: `subworkflows/local/circularmapper.nf:37:37`: `addNewMetaFromAttributes` is not defined

  ```nextflow
                                      addNewMetaFromAttributes( it, "id" , "reference" , false )
                                      ^^^^^^^^^^^^^^^^^^^^^^^^
  ```

- Error: `subworkflows/local/circularmapper.nf:44:41`: Variables in a closure should be declared with `def`

  ```nextflow
                                          new_meta = meta + [ reference: meta.id_index ]
                                          ^^^^^^^^
  ```

- Error: `subworkflows/local/circularmapper.nf:49:37`: `addNewMetaFromAttributes` is not defined

  ```nextflow
                                      addNewMetaFromAttributes( it, "reference" , "reference" , false )
                                      ^^^^^^^^^^^^^^^^^^^^^^^^
  ```

- Error: `subworkflows/local/deduplicate.nf:5:1`: Module could not be parsed: '/home/runner/work/strict-syntax-health/strict-syntax-health/pipelines/eager/subworkflows/local/utils_nfcore_eager_pipeline/main.nf'

  ```nextflow
  include { addNewMetaFromAttributes                        } from '../../subworkflows/local/utils_nfcore_eager_pipeline/main'
  ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  ```

- Error: `subworkflows/local/deduplicate.nf:8:1`: Module could not be parsed: '/home/runner/work/strict-syntax-health/strict-syntax-health/pipelines/eager/subworkflows/nf-core/bam_split_by_region/main.nf'

  ```nextflow
  include { BAM_SPLIT_BY_REGION                             } from '../../subworkflows/nf-core/bam_split_by_region/main'
  ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  ```

- Error: `subworkflows/local/deduplicate.nf:29:9`: `addNewMetaFromAttributes` is not defined

  ```nextflow
          addNewMetaFromAttributes( it, "id" , "reference" , false )
          ^^^^^^^^^^^^^^^^^^^^^^^^
  ```

- Error: `subworkflows/local/deduplicate.nf:40:9`: `addNewMetaFromAttributes` is not defined

  ```nextflow
          addNewMetaFromAttributes( it, "id" , "reference" , true )
          ^^^^^^^^^^^^^^^^^^^^^^^^
  ```

- Error: `subworkflows/local/deduplicate.nf:47:13`: `addNewMetaFromAttributes` is not defined

  ```nextflow
              addNewMetaFromAttributes( it, "reference" , "reference" , false )
              ^^^^^^^^^^^^^^^^^^^^^^^^
  ```

- Error: `subworkflows/local/deduplicate.nf:59:5`: `BAM_SPLIT_BY_REGION` is not defined

  ```nextflow
      BAM_SPLIT_BY_REGION( ch_bam_for_split )
      ^^^^^^^^^^^^^^^^^^^
  ```

- Error: `subworkflows/local/deduplicate.nf:60:38`: `BAM_SPLIT_BY_REGION` is not defined

  ```nextflow
      ch_versions   = ch_versions.mix( BAM_SPLIT_BY_REGION.out.versions )
                                       ^^^^^^^^^^^^^^^^^^^
  ```

- Error: `subworkflows/local/deduplicate.nf:64:35`: `BAM_SPLIT_BY_REGION` is not defined

  ```nextflow
          ch_markduplicates_input = BAM_SPLIT_BY_REGION.out.bam_bai
                                    ^^^^^^^^^^^^^^^^^^^
  ```

- Error: `subworkflows/local/deduplicate.nf:67:17`: `addNewMetaFromAttributes` is not defined

  ```nextflow
                  addNewMetaFromAttributes( it, "reference" , "reference" , false )
                  ^^^^^^^^^^^^^^^^^^^^^^^^
  ```

- Error: `subworkflows/local/deduplicate.nf:74:51`: `fasta` is already declared

  ```nextflow
                  ignore_me, meta, bam, bai, meta2, fasta, fasta_fai ->
                                                    ^^^^^
  ```

- Error: `subworkflows/local/deduplicate.nf:74:58`: `fasta_fai` is already declared

  ```nextflow
                  ignore_me, meta, bam, bai, meta2, fasta, fasta_fai ->
                                                           ^^^^^^^^^
  ```

- Error: `subworkflows/local/deduplicate.nf:91:26`: `BAM_SPLIT_BY_REGION` is not defined

  ```nextflow
          ch_dedup_input = BAM_SPLIT_BY_REGION.out.bam_bai
                           ^^^^^^^^^^^^^^^^^^^
  ```

- Error: `subworkflows/local/deduplicate.nf:106:13`: Variables in a closure should be declared with `def`

  ```nextflow
              meta2 = meta.clone().findAll{ it.key != 'genomic_region' }
              ^^^^^
  ```

- Error: `subworkflows/local/deduplicate.nf:112:13`: `addNewMetaFromAttributes` is not defined

  ```nextflow
              addNewMetaFromAttributes( it, "reference" , "reference" , false )
              ^^^^^^^^^^^^^^^^^^^^^^^^
  ```

- Error: `subworkflows/local/deduplicate.nf:120:35`: `meta2` is already declared

  ```nextflow
              ignore_me, meta, bam, meta2, fasta, fasta_fai ->
                                    ^^^^^
  ```

- Error: `subworkflows/local/deduplicate.nf:120:42`: `fasta` is already declared

  ```nextflow
              ignore_me, meta, bam, meta2, fasta, fasta_fai ->
                                           ^^^^^
  ```

- Error: `subworkflows/local/deduplicate.nf:120:49`: `fasta_fai` is already declared

  ```nextflow
              ignore_me, meta, bam, meta2, fasta, fasta_fai ->
                                                  ^^^^^^^^^
  ```

- Error: `subworkflows/local/elongate_reference.nf:8:1`: Module could not be parsed: '/home/runner/work/strict-syntax-health/strict-syntax-health/pipelines/eager/subworkflows/local/utils_nfcore_eager_pipeline/main.nf'

  ```nextflow
  include { addNewMetaFromAttributes            } from '../../subworkflows/local/utils_nfcore_eager_pipeline/main'
  ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  ```

- Error: `subworkflows/local/elongate_reference.nf:75:33`: `addNewMetaFromAttributes` is not defined

  ```nextflow
                                  addNewMetaFromAttributes( it, "id", "id", false )
                                  ^^^^^^^^^^^^^^^^^^^^^^^^
  ```

- Error: `subworkflows/local/estimate_contamination.nf:5:1`: Module could not be parsed: '/home/runner/work/strict-syntax-health/strict-syntax-health/pipelines/eager/subworkflows/local/utils_nfcore_eager_pipeline/main.nf'

  ```nextflow
  include { addNewMetaFromAttributes         } from '../../subworkflows/local/utils_nfcore_eager_pipeline/main'
  ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  ```

- Error: `subworkflows/local/estimate_contamination.nf:24:17`: `addNewMetaFromAttributes` is not defined

  ```nextflow
                  addNewMetaFromAttributes( it, "id" , "reference" , false )
                  ^^^^^^^^^^^^^^^^^^^^^^^^
  ```

- Error: `subworkflows/local/estimate_contamination.nf:29:17`: `addNewMetaFromAttributes` is not defined

  ```nextflow
                  addNewMetaFromAttributes( it, "reference" , "reference" , false )
                  ^^^^^^^^^^^^^^^^^^^^^^^^
  ```

- Error: `subworkflows/local/genotype.nf:18:1`: Module could not be parsed: '/home/runner/work/strict-syntax-health/strict-syntax-health/pipelines/eager/subworkflows/local/utils_nfcore_eager_pipeline/main.nf'

  ```nextflow
  include { addNewMetaFromAttributes                          } from '../../subworkflows/local/utils_nfcore_eager_pipeline/main'
  ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  ```

- Error: `subworkflows/local/genotype.nf:60:17`: `addNewMetaFromAttributes` is not defined

  ```nextflow
                  addNewMetaFromAttributes( it, "id" , "reference" , false )
                  ^^^^^^^^^^^^^^^^^^^^^^^^
  ```

- Error: `subworkflows/local/genotype.nf:66:17`: `addNewMetaFromAttributes` is not defined

  ```nextflow
                  addNewMetaFromAttributes( it, ["reference", "strandedness"] , ["reference", "strandedness"] , false )
                  ^^^^^^^^^^^^^^^^^^^^^^^^
  ```

- Error: `subworkflows/local/genotype.nf:78:21`: `addNewMetaFromAttributes` is not defined

  ```nextflow
                      addNewMetaFromAttributes( it, "reference", "reference" , false )
                      ^^^^^^^^^^^^^^^^^^^^^^^^
  ```

- Error: `subworkflows/local/genotype.nf:98:21`: `addNewMetaFromAttributes` is not defined

  ```nextflow
                      addNewMetaFromAttributes( it, "reference", "reference" , false )
                      ^^^^^^^^^^^^^^^^^^^^^^^^
  ```

- Error: `subworkflows/local/genotype.nf:119:21`: `addNewMetaFromAttributes` is not defined

  ```nextflow
                      addNewMetaFromAttributes( it, "reference" , "reference" , false )
                      ^^^^^^^^^^^^^^^^^^^^^^^^
  ```

- Error: `subworkflows/local/genotype.nf:150:17`: `addNewMetaFromAttributes` is not defined

  ```nextflow
                  addNewMetaFromAttributes( it, "reference" , "reference" , false )
                  ^^^^^^^^^^^^^^^^^^^^^^^^
  ```

- Error: `subworkflows/local/genotype.nf:166:17`: `addNewMetaFromAttributes` is not defined

  ```nextflow
                  addNewMetaFromAttributes( it, "id" , "reference" , false )
                  ^^^^^^^^^^^^^^^^^^^^^^^^
  ```

- Error: `subworkflows/local/genotype.nf:193:17`: `addNewMetaFromAttributes` is not defined

  ```nextflow
                  addNewMetaFromAttributes( it, "reference" , "reference" , false )
                  ^^^^^^^^^^^^^^^^^^^^^^^^
  ```

- Error: `subworkflows/local/genotype.nf:216:17`: `addNewMetaFromAttributes` is not defined

  ```nextflow
                  addNewMetaFromAttributes( it, "reference" , "reference" , false )
                  ^^^^^^^^^^^^^^^^^^^^^^^^
  ```

- Error: `subworkflows/local/genotype.nf:257:17`: `addNewMetaFromAttributes` is not defined

  ```nextflow
                  addNewMetaFromAttributes( it, "reference" , "reference" , false )
                  ^^^^^^^^^^^^^^^^^^^^^^^^
  ```

- Error: `subworkflows/local/genotype.nf:273:17`: `addNewMetaFromAttributes` is not defined

  ```nextflow
                  addNewMetaFromAttributes( it, "id" , "reference" , false )
                  ^^^^^^^^^^^^^^^^^^^^^^^^
  ```

- Error: `subworkflows/local/genotype.nf:308:17`: `addNewMetaFromAttributes` is not defined

  ```nextflow
                  addNewMetaFromAttributes( it, "reference" , "reference" , false )
                  ^^^^^^^^^^^^^^^^^^^^^^^^
  ```

- Error: `subworkflows/local/genotype.nf:326:17`: `addNewMetaFromAttributes` is not defined

  ```nextflow
                  addNewMetaFromAttributes( it, "id" , "reference" , false )
                  ^^^^^^^^^^^^^^^^^^^^^^^^
  ```

- Error: `subworkflows/local/genotype.nf:365:17`: `addNewMetaFromAttributes` is not defined

  ```nextflow
                  addNewMetaFromAttributes( it, "reference" , "reference" , false )
                  ^^^^^^^^^^^^^^^^^^^^^^^^
  ```

- Error: `subworkflows/local/genotype.nf:375:21`: Variables in a closure should be declared with `def`

  ```nextflow
                      new_meta = [ sample_id: ids, strandedness: strandedness, single_end: single_ends, reference: reference ]
                      ^^^^^^^^
  ```

- Error: `subworkflows/local/genotype.nf:393:17`: `addNewMetaFromAttributes` is not defined

  ```nextflow
                  addNewMetaFromAttributes( it, "id" , "reference" , false )
                  ^^^^^^^^^^^^^^^^^^^^^^^^
  ```

- Error: `subworkflows/local/genotype.nf:424:17`: `addNewMetaFromAttributes` is not defined

  ```nextflow
                  addNewMetaFromAttributes( it, "reference" , "reference" , false )
                  ^^^^^^^^^^^^^^^^^^^^^^^^
  ```

- Error: `subworkflows/local/manipulate_damage.nf:5:1`: Module could not be parsed: '/home/runner/work/strict-syntax-health/strict-syntax-health/pipelines/eager/subworkflows/local/utils_nfcore_eager_pipeline/main.nf'

  ```nextflow
  include { addNewMetaFromAttributes                                } from '../../subworkflows/local/utils_nfcore_eager_pipeline/main'
  ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  ```

- Error: `subworkflows/local/manipulate_damage.nf:34:13`: `addNewMetaFromAttributes` is not defined

  ```nextflow
              addNewMetaFromAttributes( it, "id" , "reference" , false )
              ^^^^^^^^^^^^^^^^^^^^^^^^
  ```

- Error: `subworkflows/local/manipulate_damage.nf:40:13`: `addNewMetaFromAttributes` is not defined

  ```nextflow
              addNewMetaFromAttributes( it, "reference" , "reference" , false )
              ^^^^^^^^^^^^^^^^^^^^^^^^
  ```

- Error: `subworkflows/local/manipulate_damage.nf:113:25`: `addNewMetaFromAttributes` is not defined

  ```nextflow
                          addNewMetaFromAttributes( it, "id" , "reference" , false )
                          ^^^^^^^^^^^^^^^^^^^^^^^^
  ```

- Error: `subworkflows/local/manipulate_damage.nf:117:28`: `addNewMetaFromAttributes` is not defined

  ```nextflow
                      .map { addNewMetaFromAttributes( it, "reference" , "reference" , false ) }
                             ^^^^^^^^^^^^^^^^^^^^^^^^
  ```

- Error: `subworkflows/local/manipulate_damage.nf:157:21`: Variables in a closure should be declared with `def`

  ```nextflow
                      trim_left  = meta.strandedness == 'single' ? ( meta.damage_treatment == 'none' ? params.damage_manipulation_bamutils_trim_single_stranded_none_udg_left  : meta.damage_treatment == 'half' ? params.damage_manipulation_bamutils_trim_single_stranded_half_udg_left  : 0 ) : ( meta.damage_treatment == 'none' ? params.damage_manipulation_bamutils_trim_double_stranded_none_udg_left  : meta.damage_treatment == 'half' ? params.damage_manipulation_bamutils_trim_double_stranded_half_udg_left  : 0 )
                      ^^^^^^^^^
  ```

- Error: `subworkflows/local/manipulate_damage.nf:158:21`: Variables in a closure should be declared with `def`

  ```nextflow
                      trim_right = meta.strandedness == 'single' ? ( meta.damage_treatment == 'none' ? params.damage_manipulation_bamutils_trim_single_stranded_none_udg_right : meta.damage_treatment == 'half' ? params.damage_manipulation_bamutils_trim_single_stranded_half_udg_right : 0 ) : ( meta.damage_treatment == 'none' ? params.damage_manipulation_bamutils_trim_double_stranded_none_udg_right : meta.damage_treatment == 'half' ? params.damage_manipulation_bamutils_trim_double_stranded_half_udg_right : 0 )
                      ^^^^^^^^^^
  ```

- Error: `subworkflows/local/map.nf:41:23`: `reads` is already declared

  ```nextflow
                  meta, reads ->
                        ^^^^^
  ```

- Error: `subworkflows/local/map.nf:42:21`: Variables in a closure should be declared with `def`

  ```nextflow
                      new_meta = meta.clone()
                      ^^^^^^^^
  ```

- Error: `subworkflows/local/map.nf:55:49`: `index` is already declared

  ```nextflow
          ch_index_for_mapping = index.map{ meta, index, fasta -> [ meta, index ] }
                                                  ^^^^^
  ```

- Error: `subworkflows/local/map.nf:74:39`: `reads` is already declared

  ```nextflow
                                  meta, reads, meta2, index, fasta ->
                                        ^^^^^
  ```

- Error: `subworkflows/local/map.nf:74:53`: `index` is already declared

  ```nextflow
                                  meta, reads, meta2, index, fasta ->
                                                      ^^^^^
  ```

- Error: `subworkflows/local/map.nf:91:56`: `index` is already declared

  ```nextflow
                              .combine( index.map{ meta, index, fasta -> [ meta, index ] } )
                                                         ^^^^^
  ```

- Error: `subworkflows/local/map.nf:93:39`: `reads` is already declared

  ```nextflow
                                  meta, reads, meta2, index ->
                                        ^^^^^
  ```

- Error: `subworkflows/local/map.nf:93:53`: `index` is already declared

  ```nextflow
                                  meta, reads, meta2, index ->
                                                      ^^^^^
  ```

- Error: `subworkflows/local/map.nf:120:56`: `index` is already declared

  ```nextflow
                              .combine( index.map{ meta, index, fasta -> [ meta, index ] } )
                                                         ^^^^^
  ```

- Error: `subworkflows/local/map.nf:122:39`: `reads` is already declared

  ```nextflow
                                  meta, reads, meta2, index ->
                                        ^^^^^
  ```

- Error: `subworkflows/local/map.nf:122:53`: `index` is already declared

  ```nextflow
                                  meta, reads, meta2, index ->
                                                      ^^^^^
  ```

- Error: `subworkflows/local/merge_libraries.nf:5:1`: Module could not be parsed: '/home/runner/work/strict-syntax-health/strict-syntax-health/pipelines/eager/subworkflows/local/utils_nfcore_eager_pipeline/main.nf'

  ```nextflow
  include { addNewMetaFromAttributes                                } from '../../subworkflows/local/utils_nfcore_eager_pipeline/main'
  ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  ```

- Error: `subworkflows/local/merge_libraries.nf:21:16`: `addNewMetaFromAttributes` is not defined

  ```nextflow
          .map { addNewMetaFromAttributes( it, ["id", "sample_id", "strandedness", "reference"], ["id", "sample_id", "strandedness", "reference"], false ) }
                 ^^^^^^^^^^^^^^^^^^^^^^^^
  ```

- Error: `subworkflows/local/metagenomics.nf:2:1`: Module could not be parsed: '/home/runner/work/strict-syntax-health/strict-syntax-health/pipelines/eager/subworkflows/local/metagenomics_profiling.nf'

  ```nextflow
  include { METAGENOMICS_PROFILING        } from './metagenomics_profiling'
  ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  ```

- Error: `subworkflows/local/metagenomics.nf:3:1`: Included name 'METAGENOMICS_POSTPROCESSING' is not defined in module '/home/runner/work/strict-syntax-health/strict-syntax-health/pipelines/eager/subworkflows/local/metagenomics_postprocessing.nf'

  ```nextflow
  include { METAGENOMICS_POSTPROCESSING   } from './metagenomics_postprocessing'
  ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  ```

- Error: `subworkflows/local/metagenomics.nf:39:5`: `METAGENOMICS_PROFILING` is not defined

  ```nextflow
      METAGENOMICS_PROFILING( ch_reads_for_metagenomics, ch_database )
      ^^^^^^^^^^^^^^^^^^^^^^
  ```

- Error: `subworkflows/local/metagenomics.nf:40:41`: `METAGENOMICS_PROFILING` is not defined

  ```nextflow
      ch_versions      = ch_versions.mix( METAGENOMICS_PROFILING.out.versions )
                                          ^^^^^^^^^^^^^^^^^^^^^^
  ```

- Error: `subworkflows/local/metagenomics.nf:41:46`: `METAGENOMICS_PROFILING` is not defined

  ```nextflow
      ch_multiqc_files = ch_multiqc_files.mix( METAGENOMICS_PROFILING.out.mqc.collect{it[1]}.ifEmpty([]) )
                                               ^^^^^^^^^^^^^^^^^^^^^^
  ```

- Error: `subworkflows/local/metagenomics.nf:49:9`: `METAGENOMICS_POSTPROCESSING` is not defined

  ```nextflow
          METAGENOMICS_POSTPROCESSING ( METAGENOMICS_PROFILING.out.postprocessing_input, ch_tax_list, ch_ncbi_dir )
          ^^^^^^^^^^^^^^^^^^^^^^^^^^^
  ```

- Error: `subworkflows/local/metagenomics.nf:49:39`: `METAGENOMICS_PROFILING` is not defined

  ```nextflow
          METAGENOMICS_POSTPROCESSING ( METAGENOMICS_PROFILING.out.postprocessing_input, ch_tax_list, ch_ncbi_dir )
                                        ^^^^^^^^^^^^^^^^^^^^^^
  ```

- Error: `subworkflows/local/metagenomics.nf:51:45`: `METAGENOMICS_POSTPROCESSING` is not defined

  ```nextflow
          ch_versions      = ch_versions.mix( METAGENOMICS_POSTPROCESSING.out.versions )
                                              ^^^^^^^^^^^^^^^^^^^^^^^^^^^
  ```

- Error: `subworkflows/local/metagenomics.nf:52:50`: `METAGENOMICS_POSTPROCESSING` is not defined

  ```nextflow
          ch_multiqc_files = ch_multiqc_files.mix( METAGENOMICS_POSTPROCESSING.out.mqc.collect{it[1]}.ifEmpty([]) )
                                                   ^^^^^^^^^^^^^^^^^^^^^^^^^^^
  ```

- Error: `subworkflows/local/metagenomics_postprocessing.nf:7:1`: Invalid workflow definition -- check for missing or out-of-order section labels

  ```nextflow
  workflow METAGENOMICS_POSTPROCESSING {
  ^
  ```

- Error: `subworkflows/local/metagenomics_profiling.nf:85:72`: Unexpected input: '%'

  ```nextflow
                      id:"${meta.strandedness}stranded_${groups_counter++%n_groups}"
                                                                         ^
  ```

- Error: `subworkflows/local/preprocessing_adapterremoval.nf:48:26`: `reads` is already declared

  ```nextflow
              .map { meta, reads ->
                           ^^^^^
  ```

- Error: `subworkflows/local/preprocessing_adapterremoval.nf:72:26`: `reads` is already declared

  ```nextflow
              .map { meta, reads ->
                           ^^^^^
  ```

- Error: `subworkflows/local/preprocessing_fastp.nf:35:51`: `reads` is already declared

  ```nextflow
                                              meta, reads ->
                                                    ^^^^^
  ```

- Error: `subworkflows/local/reference_indexing_single.nf:4:1`: Module could not be parsed: '/home/runner/work/strict-syntax-health/strict-syntax-health/pipelines/eager/subworkflows/local/utils_nfcore_eager_pipeline/main.nf'

  ```nextflow
  include { grabUngzippedExtension          } from '../../subworkflows/local/utils_nfcore_eager_pipeline/main'
  ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  ```

- Error: `subworkflows/local/reference_indexing_single.nf:25:21`: `grabUngzippedExtension` is not defined

  ```nextflow
      def fasta_ext = grabUngzippedExtension(fasta)
                      ^^^^^^^^^^^^^^^^^^^^^^
  ```

- Error: `subworkflows/local/reference_indexing_single.nf:90:43`: `fasta` is already declared

  ```nextflow
                                      meta, fasta, fai, dict, mapper_index ->
                                            ^^^^^
  ```

- Error: `subworkflows/local/reference_indexing_single.nf:108:43`: `fasta` is already declared

  ```nextflow
                                      meta, fasta, fai, dict, mapper_index, circular_target, mitochondrion_header, contamination_estimation_angsd_hapmap, pmd_masked_fasta, pmd_bed_for_masking, capture_bed, pileupcaller_bed, pileupcaller_snp, sexdet_bed, bedtools_feature, genotyping_gatk_dbsnp, circularmapper_elongated_fasta, circularmapper_elongated_index ->
                                            ^^^^^
  ```

- Error: `subworkflows/local/run_sex_determination.nf:5:1`: Module could not be parsed: '/home/runner/work/strict-syntax-health/strict-syntax-health/pipelines/eager/subworkflows/local/utils_nfcore_eager_pipeline/main.nf'

  ```nextflow
  include { addNewMetaFromAttributes                       } from '../../subworkflows/local/utils_nfcore_eager_pipeline/main'
  ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  ```

- Error: `subworkflows/local/run_sex_determination.nf:27:17`: `addNewMetaFromAttributes` is not defined

  ```nextflow
                  addNewMetaFromAttributes( it, "id" , "reference" , false )
                  ^^^^^^^^^^^^^^^^^^^^^^^^
  ```

- Error: `subworkflows/local/run_sex_determination.nf:33:17`: `addNewMetaFromAttributes` is not defined

  ```nextflow
                  addNewMetaFromAttributes( it, "reference" , "reference" , false )
                  ^^^^^^^^^^^^^^^^^^^^^^^^
  ```

- Error: `subworkflows/local/utils_nfcore_eager_pipeline/main.nf:391:22`: Unexpected input: 'i'

  ```nextflow
              for (int i = 0; i < source_attributes.size(); i++) {
                       ^
  ```

- Error: `subworkflows/nf-core/bam_split_by_region/main.nf:29:44`: Unexpected input: '='

  ```nextflow
              if (! stats['start'] ) [ chrom = stats['seq_name'] ]
                                             ^
  ```

- Error: `workflows/eager.nf:10:1`: Module could not be parsed: '/home/runner/work/strict-syntax-health/strict-syntax-health/pipelines/eager/subworkflows/local/utils_nfcore_eager_pipeline/main.nf'

  ```nextflow
  include { methodsDescriptionText                              } from '../subworkflows/local/utils_nfcore_eager_pipeline'
  ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  ```

- Error: `workflows/eager.nf:11:1`: Module could not be parsed: '/home/runner/work/strict-syntax-health/strict-syntax-health/pipelines/eager/subworkflows/local/utils_nfcore_eager_pipeline/main.nf'

  ```nextflow
  include { addNewMetaFromAttributes                            } from '../subworkflows/local/utils_nfcore_eager_pipeline/main'
  ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  ```

- Error: `workflows/eager.nf:276:13`: `addNewMetaFromAttributes` is not defined

  ```nextflow
              addNewMetaFromAttributes(it, "id", "reference", false)
              ^^^^^^^^^^^^^^^^^^^^^^^^
  ```

- Error: `workflows/eager.nf:283:17`: `addNewMetaFromAttributes` is not defined

  ```nextflow
                  addNewMetaFromAttributes(it, "reference", "reference", false)
                  ^^^^^^^^^^^^^^^^^^^^^^^^
  ```

- Error: `workflows/eager.nf:319:17`: Variables in a closure should be declared with `def`

  ```nextflow
                  new_meta = meta.clone().findAll { it.key !in ['single_end', 'reference'] }
                  ^^^^^^^^
  ```

- Error: `workflows/eager.nf:370:13`: `addNewMetaFromAttributes` is not defined

  ```nextflow
              addNewMetaFromAttributes(it, "id", "reference", false)
              ^^^^^^^^^^^^^^^^^^^^^^^^
  ```

- Error: `workflows/eager.nf:374:17`: `addNewMetaFromAttributes` is not defined

  ```nextflow
                  addNewMetaFromAttributes(it, "reference", "reference", false)
                  ^^^^^^^^^^^^^^^^^^^^^^^^
  ```

- Error: `workflows/eager.nf:449:13`: `addNewMetaFromAttributes` is not defined

  ```nextflow
              addNewMetaFromAttributes(it, "id", "reference", false)
              ^^^^^^^^^^^^^^^^^^^^^^^^
  ```

- Error: `workflows/eager.nf:454:17`: `addNewMetaFromAttributes` is not defined

  ```nextflow
                  addNewMetaFromAttributes(it, "reference", "reference", false)
                  ^^^^^^^^^^^^^^^^^^^^^^^^
  ```

- Error: `workflows/eager.nf:602:9`: `methodsDescriptionText` is not defined

  ```nextflow
          methodsDescriptionText(ch_multiqc_custom_methods_description)
          ^^^^^^^^^^^^^^^^^^^^^^
  ```

## :warning: Warnings

- Warning: `modules/local/samtools_view_genome.nf:21:9`: Variable was declared but not used

  ```nextflow
      def args = task.ext.args ?: ''
          ^^^^
  ```

- Warning: `modules/nf-core/angsd/gl/main.nf:101:9`: Variable was declared but not used

  ```nextflow
      def args = task.ext.args ?: ''
          ^^^^
  ```

- Warning: `modules/nf-core/bcftools/index/main.nf:23:9`: Variable was declared but not used

  ```nextflow
      def prefix = task.ext.prefix ?: "${meta.id}"
          ^^^^^^
  ```

- Warning: `modules/nf-core/bcftools/index/main.nf:40:9`: Variable was declared but not used

  ```nextflow
      def prefix = task.ext.prefix ?: "${meta.id}"
          ^^^^^^
  ```

- Warning: `modules/nf-core/bwa/mem/main.nf:56:9`: Variable was declared but not used

  ```nextflow
      def args = task.ext.args ?: ''
          ^^^^
  ```

- Warning: `modules/nf-core/bwa/mem/main.nf:59:9`: Variable was declared but not used

  ```nextflow
      def samtools_command = sort_bam ? 'sort' : 'view'
          ^^^^^^^^^^^^^^^^
  ```

- Warning: `modules/nf-core/cat/cat/main.nf:23:40`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
      def file_list = files_in.collect { it.toString() }
                                         ^^
  ```

- Warning: `modules/nf-core/cat/cat/main.nf:58:42`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
      def file_list   = files_in.collect { it.toString() }
                                           ^^
  ```

- Warning: `modules/nf-core/cat/fastq/main.nf:21:9`: Variable was declared but not used

  ```nextflow
      def args = task.ext.args ?: ''
          ^^^^
  ```

- Warning: `modules/nf-core/cat/fastq/main.nf:23:59`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
      def readList = reads instanceof List ? reads.collect{ it.toString() } : [reads.toString()]
                                                            ^^
  ```

- Warning: `modules/nf-core/cat/fastq/main.nf:54:59`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
      def readList = reads instanceof List ? reads.collect{ it.toString() } : [reads.toString()]
                                                            ^^
  ```

- Warning: `modules/nf-core/circularmapper/circulargenerator/main.nf:50:9`: Variable was declared but not used

  ```nextflow
      def args   = task.ext.args ?: ''
          ^^^^
  ```

- Warning: `modules/nf-core/circularmapper/realignsamfile/main.nf:49:9`: Variable was declared but not used

  ```nextflow
      def args = task.ext.args ?: ''
          ^^^^
  ```

- Warning: `modules/nf-core/dedup/main.nf:25:5`: Variable was declared but not used

  ```nextflow
      prefix   = task.ext.prefix ?: "${meta.id}"
      ^^^^^^
  ```

- Warning: `modules/nf-core/kraken2/kraken2/main.nf:60:9`: Variable was declared but not used

  ```nextflow
      def args = task.ext.args ?: ''
          ^^^^
  ```

- Warning: `modules/nf-core/kraken2/kraken2/main.nf:62:9`: Variable was declared but not used

  ```nextflow
      def paired       = meta.single_end ? "" : "--paired"
          ^^^^^^
  ```

- Warning: `modules/nf-core/kraken2/kraken2/main.nf:65:9`: Variable was declared but not used

  ```nextflow
      def readclassification_option = save_reads_assignment ? "--output ${prefix}.kraken2.classifiedreads.txt" : "--output /dev/null"
          ^^^^^^^^^^^^^^^^^^^^^^^^^
  ```

- Warning: `modules/nf-core/kraken2/kraken2/main.nf:66:9`: Variable was declared but not used

  ```nextflow
      def compress_reads_command = save_output_fastqs ? "pigz -p $task.cpus *.fastq" : ""
          ^^^^^^^^^^^^^^^^^^^^^^
  ```

- Warning: `modules/nf-core/mapad/index/main.nf:22:9`: Variable was declared but not used

  ```nextflow
      def prefix = task.ext.prefix ?: "${meta.id}"
          ^^^^^^
  ```

- Warning: `modules/nf-core/mapdamage2/main.nf:40:9`: Variable was declared but not used

  ```nextflow
      def prefix = task.ext.prefix ?: "${meta.id}"
          ^^^^^^
  ```

- Warning: `modules/nf-core/mtnucratio/main.nf:24:9`: Variable was declared but not used

  ```nextflow
      def prefix = task.ext.prefix ?: "${meta.id}"
          ^^^^^^
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

- Warning: `modules/nf-core/taxpasta/merge/main.nf:31:9`: Variable was declared but not used

  ```nextflow
      def prefix = task.ext.prefix ?: "${meta.id}"
          ^^^^^^
  ```

- Warning: `modules/nf-core/taxpasta/standardise/main.nf:29:9`: Variable was declared but not used

  ```nextflow
      def prefix = task.ext.prefix ?: "${meta.id}"
          ^^^^^^
  ```

- Warning: `nextflow.config:635:139`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          afterText           = """${manifest.doi ? "\n* The pipeline\n" : ""}${manifest.doi.tokenize(",").collect { "    https://doi.org/${it.trim().replace('https://doi.org/', '')}" }.join("\n")}${manifest.doi ? "\n" : ""}
                                                                                                                                            ^^
  ```

- Warning: `subworkflows/local/bamfiltering.nf:21:25`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_versions       = Channel.empty()
                          ^^^^^^^
  ```

- Warning: `subworkflows/local/bamfiltering.nf:22:25`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_multiqc_files  = Channel.empty()
                          ^^^^^^^
  ```

- Warning: `subworkflows/local/bamfiltering.nf:23:25`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_flagstats_file = Channel.empty()
                          ^^^^^^^
  ```

- Warning: `subworkflows/local/bamfiltering.nf:84:49`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          SAMTOOLS_FASTQ_METAGENOMICS ( bam.map{[ it[0], it[1] ]}, false )
                                                  ^^
  ```

- Warning: `subworkflows/local/bamfiltering.nf:84:56`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          SAMTOOLS_FASTQ_METAGENOMICS ( bam.map{[ it[0], it[1] ]}, false )
                                                         ^^
  ```

- Warning: `subworkflows/local/bamfiltering.nf:89:100`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
              ch_paired_fastq_for_cat_metagenomics = SAMTOOLS_FASTQ_METAGENOMICS.out.fastq.filter { !it[0].single_end }
                                                                                                     ^^
  ```

- Warning: `subworkflows/local/bamfiltering.nf:94:50`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
                                          .filter{ it[0].single_end }
                                                   ^^
  ```

- Warning: `subworkflows/local/bamfiltering.nf:103:37`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
          ch_fastq_for_metagenomics = Channel.empty()
                                      ^^^^^^^
  ```

- Warning: `subworkflows/local/calculate_damage.nf:17:25`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_versions       = Channel.empty()
                          ^^^^^^^
  ```

- Warning: `subworkflows/local/calculate_damage.nf:18:25`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_multiqc_files  = Channel.empty()
                          ^^^^^^^
  ```

- Warning: `subworkflows/local/calculate_damage.nf:24:39`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
              addNewMetaFromAttributes( it, "id" , "reference" , false )
                                        ^^
  ```

- Warning: `subworkflows/local/calculate_damage.nf:30:39`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
              addNewMetaFromAttributes( it, "reference" , "reference" , false )
                                        ^^
  ```

- Warning: `subworkflows/local/calculate_damage.nf:37:17`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
                  ignore_me, meta, bam, bai, meta2, fasta, fasta_fai ->
                  ^^^^^^^^^
  ```

- Warning: `subworkflows/local/calculate_damage.nf:37:39`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
                  ignore_me, meta, bam, bai, meta2, fasta, fasta_fai ->
                                        ^^^
  ```

- Warning: `subworkflows/local/calculate_damage.nf:37:44`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
                  ignore_me, meta, bam, bai, meta2, fasta, fasta_fai ->
                                             ^^^^^
  ```

- Warning: `subworkflows/local/circularmapper.nf:19:25`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_versions       = Channel.empty()
                          ^^^^^^^
  ```

- Warning: `subworkflows/local/circularmapper.nf:20:25`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_multiqc_files  = Channel.empty()
                          ^^^^^^^
  ```

- Warning: `subworkflows/local/circularmapper.nf:21:25`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_realigned_bams = Channel.empty()
                          ^^^^^^^
  ```

- Warning: `subworkflows/local/circularmapper.nf:22:25`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_realigned_bais = Channel.empty()
                          ^^^^^^^
  ```

- Warning: `subworkflows/local/circularmapper.nf:23:5`: Variable was declared but not used

  ```nextflow
      ch_realigned_csis = Channel.empty()
      ^^^^^^^^^^^^^^^^^
  ```

- Warning: `subworkflows/local/circularmapper.nf:23:25`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_realigned_csis = Channel.empty()
                          ^^^^^^^
  ```

- Warning: `subworkflows/local/circularmapper.nf:32:43`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
                                      meta, index, reference, elongated_chr_list ->
                                            ^^^^^
  ```

- Warning: `subworkflows/local/circularmapper.nf:37:63`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
                                      addNewMetaFromAttributes( it, "id" , "reference" , false )
                                                                ^^
  ```

- Warning: `subworkflows/local/circularmapper.nf:49:63`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
                                      addNewMetaFromAttributes( it, "reference" , "reference" , false )
                                                                ^^
  ```

- Warning: `subworkflows/local/circularmapper.nf:53:37`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
                                      ignore_me, meta, bam, ref_meta, ref_fasta, elongated_chr_list ->
                                      ^^^^^^^^^
  ```

- Warning: `subworkflows/local/deduplicate.nf:23:19`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_versions = Channel.empty()
                    ^^^^^^^
  ```

- Warning: `subworkflows/local/deduplicate.nf:24:25`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_multiqc_files  = Channel.empty()
                          ^^^^^^^
  ```

- Warning: `subworkflows/local/deduplicate.nf:29:35`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          addNewMetaFromAttributes( it, "id" , "reference" , false )
                                    ^^
  ```

- Warning: `subworkflows/local/deduplicate.nf:40:35`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          addNewMetaFromAttributes( it, "id" , "reference" , true )
                                    ^^
  ```

- Warning: `subworkflows/local/deduplicate.nf:47:39`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
              addNewMetaFromAttributes( it, "reference" , "reference" , false )
                                        ^^
  ```

- Warning: `subworkflows/local/deduplicate.nf:54:13`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
              ignore_me, meta, bam, bai, regions ->
              ^^^^^^^^^
  ```

- Warning: `subworkflows/local/deduplicate.nf:67:43`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
                  addNewMetaFromAttributes( it, "reference" , "reference" , false )
                                            ^^
  ```

- Warning: `subworkflows/local/deduplicate.nf:74:17`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
                  ignore_me, meta, bam, bai, meta2, fasta, fasta_fai ->
                  ^^^^^^^^^
  ```

- Warning: `subworkflows/local/deduplicate.nf:74:39`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
                  ignore_me, meta, bam, bai, meta2, fasta, fasta_fai ->
                                        ^^^
  ```

- Warning: `subworkflows/local/deduplicate.nf:93:28`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
                  meta, bam, bai ->
                             ^^^
  ```

- Warning: `subworkflows/local/deduplicate.nf:106:43`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
              meta2 = meta.clone().findAll{ it.key != 'genomic_region' }
                                            ^^
  ```

- Warning: `subworkflows/local/deduplicate.nf:112:39`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
              addNewMetaFromAttributes( it, "reference" , "reference" , false )
                                        ^^
  ```

- Warning: `subworkflows/local/deduplicate.nf:120:13`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
              ignore_me, meta, bam, meta2, fasta, fasta_fai ->
              ^^^^^^^^^
  ```

- Warning: `subworkflows/local/elongate_reference.nf:16:29`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_versions           = Channel.empty()
                              ^^^^^^^
  ```

- Warning: `subworkflows/local/elongate_reference.nf:17:29`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_multiqc_files      = Channel.empty()
                              ^^^^^^^
  ```

- Warning: `subworkflows/local/elongate_reference.nf:18:29`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_circular_reference = Channel.empty()
                              ^^^^^^^
  ```

- Warning: `subworkflows/local/elongate_reference.nf:19:29`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_elongated_unzipped = Channel.empty()
                              ^^^^^^^
  ```

- Warning: `subworkflows/local/elongate_reference.nf:20:29`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_elongated_chr      = Channel.empty()
                              ^^^^^^^
  ```

- Warning: `subworkflows/local/elongate_reference.nf:25:33`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
                                  meta, circular_target, circularmapper_elongated_fasta, circularmapper_elongated_index ->
                                  ^^^^
  ```

- Warning: `subworkflows/local/elongate_reference.nf:25:39`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
                                  meta, circular_target, circularmapper_elongated_fasta, circularmapper_elongated_index ->
                                        ^^^^^^^^^^^^^^^
  ```

- Warning: `subworkflows/local/elongate_reference.nf:25:88`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
                                  meta, circular_target, circularmapper_elongated_fasta, circularmapper_elongated_index ->
                                                                                         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  ```

- Warning: `subworkflows/local/elongate_reference.nf:32:39`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
                                  meta, circular_target, circularmapper_elongated_fasta, circularmapper_elongated_index ->
                                        ^^^^^^^^^^^^^^^
  ```

- Warning: `subworkflows/local/elongate_reference.nf:32:88`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
                                  meta, circular_target, circularmapper_elongated_fasta, circularmapper_elongated_index ->
                                                                                         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  ```

- Warning: `subworkflows/local/elongate_reference.nf:43:41`: Variable was declared but not used

  ```nextflow
                                      def final_fasta = unzipped_fasta ?: circularmapper_elongated_fasta
                                          ^^^^^^^^^^^
  ```

- Warning: `subworkflows/local/elongate_reference.nf:59:33`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
                                  meta, circular_target, circularmapper_elongated_fasta, circularmapper_elongated_index ->
                                  ^^^^
  ```

- Warning: `subworkflows/local/elongate_reference.nf:75:59`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
                                  addNewMetaFromAttributes( it, "id", "id", false )
                                                            ^^
  ```

- Warning: `subworkflows/local/elongate_reference.nf:82:56`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
                                  meta, circular_target, circularmapper_elongated_fasta, circularmapper_elongated_index, fasta, fai, dict, mapindex ->
                                                         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  ```

- Warning: `subworkflows/local/elongate_reference.nf:82:88`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
                                  meta, circular_target, circularmapper_elongated_fasta, circularmapper_elongated_index, fasta, fai, dict, mapindex ->
                                                                                         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  ```

- Warning: `subworkflows/local/elongate_reference.nf:82:127`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
                                  meta, circular_target, circularmapper_elongated_fasta, circularmapper_elongated_index, fasta, fai, dict, mapindex ->
                                                                                                                                ^^^
  ```

- Warning: `subworkflows/local/elongate_reference.nf:82:132`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
                                  meta, circular_target, circularmapper_elongated_fasta, circularmapper_elongated_index, fasta, fai, dict, mapindex ->
                                                                                                                                     ^^^^
  ```

- Warning: `subworkflows/local/elongate_reference.nf:82:138`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
                                  meta, circular_target, circularmapper_elongated_fasta, circularmapper_elongated_index, fasta, fai, dict, mapindex ->
                                                                                                                                           ^^^^^^^^
  ```

- Warning: `subworkflows/local/elongate_reference.nf:86:33`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
                                  meta, fasta, circular_target ->
                                  ^^^^
  ```

- Warning: `subworkflows/local/elongate_reference.nf:96:33`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
                                  ignore_me, chr_list, meta, fasta, fai, dict, mapindex ->
                                  ^^^^^^^^^
  ```

- Warning: `subworkflows/local/elongate_reference.nf:96:60`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
                                  ignore_me, chr_list, meta, fasta, fai, dict, mapindex ->
                                                             ^^^^^
  ```

- Warning: `subworkflows/local/elongate_reference.nf:96:67`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
                                  ignore_me, chr_list, meta, fasta, fai, dict, mapindex ->
                                                                    ^^^
  ```

- Warning: `subworkflows/local/elongate_reference.nf:96:72`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
                                  ignore_me, chr_list, meta, fasta, fai, dict, mapindex ->
                                                                         ^^^^
  ```

- Warning: `subworkflows/local/elongate_reference.nf:96:78`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
                                  ignore_me, chr_list, meta, fasta, fai, dict, mapindex ->
                                                                               ^^^^^^^^
  ```

- Warning: `subworkflows/local/elongate_reference.nf:105:56`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
                                  meta, circular_target, circularmapper_elongated_fasta, circularmapper_elongated_index, fasta, fai, dict, mapindex ->
                                                         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  ```

- Warning: `subworkflows/local/elongate_reference.nf:105:88`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
                                  meta, circular_target, circularmapper_elongated_fasta, circularmapper_elongated_index, fasta, fai, dict, mapindex ->
                                                                                         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  ```

- Warning: `subworkflows/local/elongate_reference.nf:105:127`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
                                  meta, circular_target, circularmapper_elongated_fasta, circularmapper_elongated_index, fasta, fai, dict, mapindex ->
                                                                                                                                ^^^
  ```

- Warning: `subworkflows/local/elongate_reference.nf:105:132`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
                                  meta, circular_target, circularmapper_elongated_fasta, circularmapper_elongated_index, fasta, fai, dict, mapindex ->
                                                                                                                                     ^^^^
  ```

- Warning: `subworkflows/local/elongate_reference.nf:105:138`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
                                  meta, circular_target, circularmapper_elongated_fasta, circularmapper_elongated_index, fasta, fai, dict, mapindex ->
                                                                                                                                           ^^^^^^^^
  ```

- Warning: `subworkflows/local/elongate_reference.nf:125:39`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
                                  meta, circular_target, circularmapper_elongated_fasta, circularmapper_elongated_index ->
                                        ^^^^^^^^^^^^^^^
  ```

- Warning: `subworkflows/local/elongate_reference.nf:125:88`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
                                  meta, circular_target, circularmapper_elongated_fasta, circularmapper_elongated_index ->
                                                                                         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  ```

- Warning: `subworkflows/local/elongate_reference.nf:139:39`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
                                  meta, circular_target, circularmapper_elongated_fasta, circularmapper_elongated_index ->
                                        ^^^^^^^^^^^^^^^
  ```

- Warning: `subworkflows/local/estimate_contamination.nf:17:25`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_versions       = Channel.empty()
                          ^^^^^^^
  ```

- Warning: `subworkflows/local/estimate_contamination.nf:18:25`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_multiqc_files  = Channel.empty()
                          ^^^^^^^
  ```

- Warning: `subworkflows/local/estimate_contamination.nf:24:43`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
                  addNewMetaFromAttributes( it, "id" , "reference" , false )
                                            ^^
  ```

- Warning: `subworkflows/local/estimate_contamination.nf:29:43`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
                  addNewMetaFromAttributes( it, "reference" , "reference" , false )
                                            ^^
  ```

- Warning: `subworkflows/local/estimate_contamination.nf:36:17`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
                  ignore_me, meta, bam, bai, meta2, hapmap ->
                  ^^^^^^^^^
  ```

- Warning: `subworkflows/local/estimate_contamination.nf:36:44`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
                  ignore_me, meta, bam, bai, meta2, hapmap ->
                                             ^^^^^
  ```

- Warning: `subworkflows/local/estimate_contamination.nf:46:35`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
                              .map{ it[1] } //remove meta
                                    ^^
  ```

- Warning: `subworkflows/local/genotype.nf:28:42`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_versions                        = Channel.empty()
                                           ^^^^^^^
  ```

- Warning: `subworkflows/local/genotype.nf:29:42`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_multiqc_files                   = Channel.empty()
                                           ^^^^^^^
  ```

- Warning: `subworkflows/local/genotype.nf:30:42`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_pileupcaller_genotypes          = Channel.empty()
                                           ^^^^^^^
  ```

- Warning: `subworkflows/local/genotype.nf:31:42`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_eigenstrat_coverage_stats       = Channel.empty()
                                           ^^^^^^^
  ```

- Warning: `subworkflows/local/genotype.nf:32:42`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_angsd_genotype_likelihoods      = Channel.empty()
                                           ^^^^^^^
  ```

- Warning: `subworkflows/local/genotype.nf:33:42`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_genotypes_vcf                   = Channel.empty()
                                           ^^^^^^^
  ```

- Warning: `subworkflows/local/genotype.nf:34:42`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_bcftools_stats                  = Channel.empty()
                                           ^^^^^^^
  ```

- Warning: `subworkflows/local/genotype.nf:43:23`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
              .filter { it[0] != [] }
                        ^^
  ```

- Warning: `subworkflows/local/genotype.nf:54:45`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
                  ref_meta, fasta, fai, dict, empty ->
                                              ^^^^^
  ```

- Warning: `subworkflows/local/genotype.nf:60:43`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
                  addNewMetaFromAttributes( it, "id" , "reference" , false )
                                            ^^
  ```

- Warning: `subworkflows/local/genotype.nf:66:43`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
                  addNewMetaFromAttributes( it, ["reference", "strandedness"] , ["reference", "strandedness"] , false )
                                            ^^
  ```

- Warning: `subworkflows/local/genotype.nf:70:42`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
                  combo_meta, metas, bams, bais ->
                                           ^^^^
  ```

- Warning: `subworkflows/local/genotype.nf:78:47`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
                      addNewMetaFromAttributes( it, "reference", "reference" , false )
                                                ^^
  ```

- Warning: `subworkflows/local/genotype.nf:82:27`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
                  .filter { it[7] != []}
                            ^^
  ```

- Warning: `subworkflows/local/genotype.nf:84:21`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
                      ignore_me, combo_meta, bams, ref_meta, fasta, fai, dict, bed, snp ->
                      ^^^^^^^^^
  ```

- Warning: `subworkflows/local/genotype.nf:84:50`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
                      ignore_me, combo_meta, bams, ref_meta, fasta, fai, dict, bed, snp ->
                                                   ^^^^^^^^
  ```

- Warning: `subworkflows/local/genotype.nf:84:67`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
                      ignore_me, combo_meta, bams, ref_meta, fasta, fai, dict, bed, snp ->
                                                                    ^^^
  ```

- Warning: `subworkflows/local/genotype.nf:84:72`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
                      ignore_me, combo_meta, bams, ref_meta, fasta, fai, dict, bed, snp ->
                                                                         ^^^^
  ```

- Warning: `subworkflows/local/genotype.nf:84:83`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
                      ignore_me, combo_meta, bams, ref_meta, fasta, fai, dict, bed, snp ->
                                                                                    ^^^
  ```

- Warning: `subworkflows/local/genotype.nf:98:47`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
                      addNewMetaFromAttributes( it, "reference", "reference" , false )
                                                ^^
  ```

- Warning: `subworkflows/local/genotype.nf:102:21`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
                      ignore_me, meta, mpileup, ref_meta, fasta, fai, dict, bed, snp ->
                      ^^^^^^^^^
  ```

- Warning: `subworkflows/local/genotype.nf:102:47`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
                      ignore_me, meta, mpileup, ref_meta, fasta, fai, dict, bed, snp ->
                                                ^^^^^^^^
  ```

- Warning: `subworkflows/local/genotype.nf:102:57`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
                      ignore_me, meta, mpileup, ref_meta, fasta, fai, dict, bed, snp ->
                                                          ^^^^^
  ```

- Warning: `subworkflows/local/genotype.nf:102:64`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
                      ignore_me, meta, mpileup, ref_meta, fasta, fai, dict, bed, snp ->
                                                                 ^^^
  ```

- Warning: `subworkflows/local/genotype.nf:102:69`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
                      ignore_me, meta, mpileup, ref_meta, fasta, fai, dict, bed, snp ->
                                                                      ^^^^
  ```

- Warning: `subworkflows/local/genotype.nf:102:75`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
                      ignore_me, meta, mpileup, ref_meta, fasta, fai, dict, bed, snp ->
                                                                            ^^^
  ```

- Warning: `subworkflows/local/genotype.nf:119:47`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
                      addNewMetaFromAttributes( it, "reference" , "reference" , false )
                                                ^^
  ```

- Warning: `subworkflows/local/genotype.nf:123:33`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
                      combo_meta, metas, geno, snp, ind ->
                                  ^^^^^
  ```

- Warning: `subworkflows/local/genotype.nf:150:43`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
                  addNewMetaFromAttributes( it, "reference" , "reference" , false )
                                            ^^
  ```

- Warning: `subworkflows/local/genotype.nf:157:23`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
              .filter { it[0] != [] }
                        ^^
  ```

- Warning: `subworkflows/local/genotype.nf:166:43`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
                  addNewMetaFromAttributes( it, "id" , "reference" , false )
                                            ^^
  ```

- Warning: `subworkflows/local/genotype.nf:172:17`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
                  ignore_me, meta, bam, bai, ref_meta, fasta, fai, dict, dbsnp ->
                  ^^^^^^^^^
  ```

- Warning: `subworkflows/local/genotype.nf:172:72`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
                  ignore_me, meta, bam, bai, ref_meta, fasta, fai, dict, dbsnp ->
                                                                         ^^^^^
  ```

- Warning: `subworkflows/local/genotype.nf:193:43`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
                  addNewMetaFromAttributes( it, "reference" , "reference" , false )
                                            ^^
  ```

- Warning: `subworkflows/local/genotype.nf:197:17`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
                  ignore_me, meta, bam, bai, intervals, ref_meta, fasta, fai, dict, dbsnp ->
                  ^^^^^^^^^
  ```

- Warning: `subworkflows/local/genotype.nf:197:83`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
                  ignore_me, meta, bam, bai, intervals, ref_meta, fasta, fai, dict, dbsnp ->
                                                                                    ^^^^^
  ```

- Warning: `subworkflows/local/genotype.nf:216:43`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
                  addNewMetaFromAttributes( it, "reference" , "reference" , false )
                                            ^^
  ```

- Warning: `subworkflows/local/genotype.nf:220:17`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
                  ignore_me, meta, bam, bai, ref_meta, fasta, fai, dict, dbsnp ->
                  ^^^^^^^^^
  ```

- Warning: `subworkflows/local/genotype.nf:257:43`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
                  addNewMetaFromAttributes( it, "reference" , "reference" , false )
                                            ^^
  ```

- Warning: `subworkflows/local/genotype.nf:264:23`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
              .filter { it[0] != [] }
                        ^^
  ```

- Warning: `subworkflows/local/genotype.nf:273:43`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
                  addNewMetaFromAttributes( it, "id" , "reference" , false )
                                            ^^
  ```

- Warning: `subworkflows/local/genotype.nf:279:17`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
                  ignore_me, meta, bam, bai, ref_meta, fasta, fai, dict, dbsnp ->
                  ^^^^^^^^^
  ```

- Warning: `subworkflows/local/genotype.nf:308:43`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
                  addNewMetaFromAttributes( it, "reference" , "reference" , false )
                                            ^^
  ```

- Warning: `subworkflows/local/genotype.nf:317:23`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
              .filter { it[0] != [] }
                        ^^
  ```

- Warning: `subworkflows/local/genotype.nf:326:43`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
                  addNewMetaFromAttributes( it, "id" , "reference" , false )
                                            ^^
  ```

- Warning: `subworkflows/local/genotype.nf:332:17`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
                  ignore_me, meta, bam, bai, ref_meta, fasta, fai, dict, dbsnp ->
                  ^^^^^^^^^
  ```

- Warning: `subworkflows/local/genotype.nf:332:66`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
                  ignore_me, meta, bam, bai, ref_meta, fasta, fai, dict, dbsnp ->
                                                                   ^^^^
  ```

- Warning: `subworkflows/local/genotype.nf:332:72`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
                  ignore_me, meta, bam, bai, ref_meta, fasta, fai, dict, dbsnp ->
                                                                         ^^^^^
  ```

- Warning: `subworkflows/local/genotype.nf:365:43`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
                  addNewMetaFromAttributes( it, "reference" , "reference" , false )
                                            ^^
  ```

- Warning: `subworkflows/local/genotype.nf:370:25`: Variable was declared but not used

  ```nextflow
                      def new_map = [:]
                          ^^^^^^^
  ```

- Warning: `subworkflows/local/genotype.nf:384:23`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
              .filter { it[0] != [] }
                        ^^
  ```

- Warning: `subworkflows/local/genotype.nf:393:43`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
                  addNewMetaFromAttributes( it, "id" , "reference" , false )
                                            ^^
  ```

- Warning: `subworkflows/local/genotype.nf:400:17`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
                  ignore_me, meta, bam, bai, ref_meta, fasta, fai, dict, dbsnp ->
                  ^^^^^^^^^
  ```

- Warning: `subworkflows/local/genotype.nf:400:39`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
                  ignore_me, meta, bam, bai, ref_meta, fasta, fai, dict, dbsnp ->
                                        ^^^
  ```

- Warning: `subworkflows/local/genotype.nf:400:44`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
                  ignore_me, meta, bam, bai, ref_meta, fasta, fai, dict, dbsnp ->
                                             ^^^^^^^^
  ```

- Warning: `subworkflows/local/genotype.nf:400:54`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
                  ignore_me, meta, bam, bai, ref_meta, fasta, fai, dict, dbsnp ->
                                                       ^^^^^
  ```

- Warning: `subworkflows/local/genotype.nf:400:61`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
                  ignore_me, meta, bam, bai, ref_meta, fasta, fai, dict, dbsnp ->
                                                              ^^^
  ```

- Warning: `subworkflows/local/genotype.nf:400:66`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
                  ignore_me, meta, bam, bai, ref_meta, fasta, fai, dict, dbsnp ->
                                                                   ^^^^
  ```

- Warning: `subworkflows/local/genotype.nf:400:72`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
                  ignore_me, meta, bam, bai, ref_meta, fasta, fai, dict, dbsnp ->
                                                                         ^^^^^
  ```

- Warning: `subworkflows/local/genotype.nf:424:43`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
                  addNewMetaFromAttributes( it, "reference" , "reference" , false )
                                            ^^
  ```

- Warning: `subworkflows/local/genotype.nf:428:17`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
                  ignore_me, meta, vcf, tbi, ref_meta, fasta, fai, dict, dbsnp ->
                  ^^^^^^^^^
  ```

- Warning: `subworkflows/local/genotype.nf:428:61`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
                  ignore_me, meta, vcf, tbi, ref_meta, fasta, fai, dict, dbsnp ->
                                                              ^^^
  ```

- Warning: `subworkflows/local/genotype.nf:428:66`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
                  ignore_me, meta, vcf, tbi, ref_meta, fasta, fai, dict, dbsnp ->
                                                                   ^^^^
  ```

- Warning: `subworkflows/local/genotype.nf:428:72`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
                  ignore_me, meta, vcf, tbi, ref_meta, fasta, fai, dict, dbsnp ->
                                                                         ^^^^^
  ```

- Warning: `subworkflows/local/manipulate_damage.nf:24:32`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_versions              = Channel.empty()
                                 ^^^^^^^
  ```

- Warning: `subworkflows/local/manipulate_damage.nf:25:32`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_rescaled_bams         = Channel.empty()
                                 ^^^^^^^
  ```

- Warning: `subworkflows/local/manipulate_damage.nf:26:32`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_pmd_filtered_bams     = Channel.empty()
                                 ^^^^^^^
  ```

- Warning: `subworkflows/local/manipulate_damage.nf:27:32`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_trimmed_bams          = Channel.empty()
                                 ^^^^^^^
  ```

- Warning: `subworkflows/local/manipulate_damage.nf:28:32`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_pmd_filtered_flagstat = Channel.empty() // Only run flagstat on pmd filtered bam, since rescaling and trimming does not change the number of reads
                                 ^^^^^^^
  ```

- Warning: `subworkflows/local/manipulate_damage.nf:34:39`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
              addNewMetaFromAttributes( it, "id" , "reference" , false )
                                        ^^
  ```

- Warning: `subworkflows/local/manipulate_damage.nf:40:39`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
              addNewMetaFromAttributes( it, "reference" , "reference" , false )
                                        ^^
  ```

- Warning: `subworkflows/local/manipulate_damage.nf:47:17`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
                  ignore_me, meta, bam, bai, ref_meta, fasta ->
                  ^^^^^^^^^
  ```

- Warning: `subworkflows/local/manipulate_damage.nf:47:34`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
                  ignore_me, meta, bam, bai, ref_meta, fasta ->
                                   ^^^
  ```

- Warning: `subworkflows/local/manipulate_damage.nf:47:39`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
                  ignore_me, meta, bam, bai, ref_meta, fasta ->
                                        ^^^
  ```

- Warning: `subworkflows/local/manipulate_damage.nf:47:44`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
                  ignore_me, meta, bam, bai, ref_meta, fasta ->
                                             ^^^^^^^^
  ```

- Warning: `subworkflows/local/manipulate_damage.nf:47:54`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
                  ignore_me, meta, bam, bai, ref_meta, fasta ->
                                                       ^^^^^
  ```

- Warning: `subworkflows/local/manipulate_damage.nf:54:17`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
                  ignore_me, meta, bam, bai, ref_meta, fasta ->
                  ^^^^^^^^^
  ```

- Warning: `subworkflows/local/manipulate_damage.nf:54:44`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
                  ignore_me, meta, bam, bai, ref_meta, fasta ->
                                             ^^^^^^^^
  ```

- Warning: `subworkflows/local/manipulate_damage.nf:54:54`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
                  ignore_me, meta, bam, bai, ref_meta, fasta ->
                                                       ^^^^^
  ```

- Warning: `subworkflows/local/manipulate_damage.nf:60:17`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
                  ignore_me, meta, bam, bai, ref_meta, fasta ->
                  ^^^^^^^^^
  ```

- Warning: `subworkflows/local/manipulate_damage.nf:60:39`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
                  ignore_me, meta, bam, bai, ref_meta, fasta ->
                                        ^^^
  ```

- Warning: `subworkflows/local/manipulate_damage.nf:60:44`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
                  ignore_me, meta, bam, bai, ref_meta, fasta ->
                                             ^^^^^^^^
  ```

- Warning: `subworkflows/local/manipulate_damage.nf:81:25`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
                          meta, masked_fasta, bed, fasta ->
                          ^^^^
  ```

- Warning: `subworkflows/local/manipulate_damage.nf:81:50`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
                          meta, masked_fasta, bed, fasta ->
                                                   ^^^^^
  ```

- Warning: `subworkflows/local/manipulate_damage.nf:89:31`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
                          meta, masked_fasta, bed, fasta ->
                                ^^^^^^^^^^^^
  ```

- Warning: `subworkflows/local/manipulate_damage.nf:100:45`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
                          meta, masked_fasta, bed, fasta ->
                                              ^^^
  ```

- Warning: `subworkflows/local/manipulate_damage.nf:100:50`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
                          meta, masked_fasta, bed, fasta ->
                                                   ^^^^^
  ```

- Warning: `subworkflows/local/manipulate_damage.nf:106:31`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
                          meta, masked_fasta, bed, fasta ->
                                ^^^^^^^^^^^^
  ```

- Warning: `subworkflows/local/manipulate_damage.nf:106:45`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
                          meta, masked_fasta, bed, fasta ->
                                              ^^^
  ```

- Warning: `subworkflows/local/manipulate_damage.nf:113:51`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
                          addNewMetaFromAttributes( it, "id" , "reference" , false )
                                                    ^^
  ```

- Warning: `subworkflows/local/manipulate_damage.nf:117:54`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
                      .map { addNewMetaFromAttributes( it, "reference" , "reference" , false ) }
                                                       ^^
  ```

- Warning: `subworkflows/local/manipulate_damage.nf:120:25`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
                          combine_meta, meta, bam, bai, ref_meta, fasta ->
                          ^^^^^^^^^^^^
  ```

- Warning: `subworkflows/local/manipulate_damage.nf:120:55`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
                          combine_meta, meta, bam, bai, ref_meta, fasta ->
                                                        ^^^^^^^^
  ```

- Warning: `subworkflows/local/manipulate_damage.nf:143:32`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
                      meta, bam, bai ->
                                 ^^^
  ```

- Warning: `subworkflows/local/manipulate_damage.nf:149:32`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
                      meta, bam, bai ->
                                 ^^^
  ```

- Warning: `subworkflows/local/map.nf:28:25`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_versions       = Channel.empty()
                          ^^^^^^^
  ```

- Warning: `subworkflows/local/map.nf:29:25`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_multiqc_files  = Channel.empty()
                          ^^^^^^^
  ```

- Warning: `subworkflows/local/map.nf:55:56`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          ch_index_for_mapping = index.map{ meta, index, fasta -> [ meta, index ] }
                                                         ^^^^^
  ```

- Warning: `subworkflows/local/map.nf:91:63`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
                              .combine( index.map{ meta, index, fasta -> [ meta, index ] } )
                                                                ^^^^^
  ```

- Warning: `subworkflows/local/map.nf:110:39`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
                                  meta, elongated_fasta, elongated_index ->
                                        ^^^^^^^^^^^^^^^
  ```

- Warning: `subworkflows/local/map.nf:120:63`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
                              .combine( index.map{ meta, index, fasta -> [ meta, index ] } )
                                                                ^^^^^
  ```

- Warning: `subworkflows/local/map.nf:162:70`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
                                      new_meta = meta.clone().findAll{ it.key !in ['lane', 'colour_chemistry', 'shard_number'] }
                                                                       ^^
  ```

- Warning: `subworkflows/local/map.nf:167:37`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
                                      meta, bam ->
                                      ^^^^
  ```

- Warning: `subworkflows/local/merge_lanes_inputbam.nf:15:25`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_versions       = Channel.empty()
                          ^^^^^^^
  ```

- Warning: `subworkflows/local/merge_lanes_inputbam.nf:16:25`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_multiqc_files  = Channel.empty()
                          ^^^^^^^
  ```

- Warning: `subworkflows/local/merge_lanes_inputbam.nf:19:77`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
                                  .map { meta, bam -> [ meta.clone().findAll{ it.key !in ['lane', 'colour_chemistry', 'shard_number'] }, bam ] }
                                                                              ^^
  ```

- Warning: `subworkflows/local/merge_lanes_inputbam.nf:22:37`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
                                      meta, bam ->
                                      ^^^^
  ```

- Warning: `subworkflows/local/merge_libraries.nf:17:24`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_versions      = Channel.empty()
                         ^^^^^^^
  ```

- Warning: `subworkflows/local/merge_libraries.nf:18:24`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_multiqc_files = Channel.empty()
                         ^^^^^^^
  ```

- Warning: `subworkflows/local/merge_libraries.nf:21:42`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          .map { addNewMetaFromAttributes( it, ["id", "sample_id", "strandedness", "reference"], ["id", "sample_id", "strandedness", "reference"], false ) }
                                           ^^
  ```

- Warning: `subworkflows/local/merge_libraries.nf:25:19`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
              meta, lib_metas, bam, bai ->
                    ^^^^^^^^^
  ```

- Warning: `subworkflows/local/merge_libraries.nf:25:35`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
              meta, lib_metas, bam, bai ->
                                    ^^^
  ```

- Warning: `subworkflows/local/metagenomics.nf:14:39`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_multiqc_files                = Channel.empty()
                                        ^^^^^^^
  ```

- Warning: `subworkflows/local/metagenomics.nf:15:39`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_versions                     = Channel.empty()
                                        ^^^^^^^
  ```

- Warning: `subworkflows/local/metagenomics.nf:30:97`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          ch_multiqc_files = ch_multiqc_files.mix(METAGENOMICS_COMPLEXITYFILTER.out.fastq.collect{it[1]}.ifEmpty([]))
                                                                                                  ^^
  ```

- Warning: `subworkflows/local/metagenomics.nf:41:85`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
      ch_multiqc_files = ch_multiqc_files.mix( METAGENOMICS_PROFILING.out.mqc.collect{it[1]}.ifEmpty([]) )
                                                                                      ^^
  ```

- Warning: `subworkflows/local/metagenomics.nf:52:94`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          ch_multiqc_files = ch_multiqc_files.mix( METAGENOMICS_POSTPROCESSING.out.mqc.collect{it[1]}.ifEmpty([]) )
                                                                                               ^^
  ```

- Warning: `subworkflows/local/preprocessing.nf:17:25`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_versions       = Channel.empty()
                          ^^^^^^^
  ```

- Warning: `subworkflows/local/preprocessing.nf:18:25`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_multiqc_files  = Channel.empty()
                          ^^^^^^^
  ```

- Warning: `subworkflows/local/preprocessing_adapterremoval.nf:16:19`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_versions = Channel.empty()
                    ^^^^^^^
  ```

- Warning: `subworkflows/local/preprocessing_adapterremoval.nf:17:29`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_multiqc_files      = Channel.empty()
                              ^^^^^^^
  ```

- Warning: `subworkflows/local/preprocessing_adapterremoval.nf:21:49`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
                                          single: it[0].single_end
                                                  ^^
  ```

- Warning: `subworkflows/local/preprocessing_adapterremoval.nf:22:50`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
                                          paired: !it[0].single_end
                                                   ^^
  ```

- Warning: `subworkflows/local/preprocessing_adapterremoval.nf:41:27`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
          ch_concat_fastq = Channel.empty()
                            ^^^^^^^
  ```

- Warning: `subworkflows/local/preprocessing_adapterremoval.nf:67:27`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
          ch_concat_fastq = Channel.empty()
                            ^^^^^^^
  ```

- Warning: `subworkflows/local/preprocessing_fastp.nf:14:29`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_versions           = Channel.empty()
                              ^^^^^^^
  ```

- Warning: `subworkflows/local/preprocessing_fastp.nf:15:29`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_multiqc_files      = Channel.empty()
                              ^^^^^^^
  ```

- Warning: `subworkflows/local/preprocessing_fastp.nf:19:41`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
                                  single: it[0]['single_end'] == true
                                          ^^
  ```

- Warning: `subworkflows/local/preprocessing_fastp.nf:20:41`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
                                  paired: it[0]['single_end'] == false
                                          ^^
  ```

- Warning: `subworkflows/local/reference_indexing.nf:20:19`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_versions = Channel.empty()
                    ^^^^^^^
  ```

- Warning: `subworkflows/local/reference_indexing.nf:60:30`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
                      .filter{ it[1] != "" }
                               ^^
  ```

- Warning: `subworkflows/local/reference_indexing.nf:63:30`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
                      .filter{ it[1] != "" }
                               ^^
  ```

- Warning: `subworkflows/local/reference_indexing.nf:67:25`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
                          meta, pmd_masked_fasta ->
                          ^^^^
  ```

- Warning: `subworkflows/local/reference_indexing.nf:73:25`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
                          meta, pmd_masked_fasta ->
                          ^^^^
  ```

- Warning: `subworkflows/local/reference_indexing.nf:83:25`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
                          meta, pmd_bed_for_masking ->
                          ^^^^
  ```

- Warning: `subworkflows/local/reference_indexing.nf:89:25`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
                          meta, pmd_bed_for_masking ->
                          ^^^^
  ```

- Warning: `subworkflows/local/reference_indexing.nf:102:25`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
                          meta, capture_bed ->
                          ^^^^
  ```

- Warning: `subworkflows/local/reference_indexing.nf:108:25`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
                          meta, capture_bed ->
                          ^^^^
  ```

- Warning: `subworkflows/local/reference_indexing.nf:117:31`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
                      .filter { it[1] != "" || it[2] != "" } // They go together or not at all.
                                ^^
  ```

- Warning: `subworkflows/local/reference_indexing.nf:117:46`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
                      .filter { it[1] != "" || it[2] != "" } // They go together or not at all.
                                               ^^
  ```

- Warning: `subworkflows/local/reference_indexing.nf:120:30`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
                      .filter{ it != null } // Remove null channel which arises if empty cause error returns null.
                               ^^
  ```

- Warning: `subworkflows/local/reference_indexing.nf:123:31`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
                      .filter { it[1] != "" }
                                ^^
  ```

- Warning: `subworkflows/local/reference_indexing.nf:126:31`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
                      .filter { it[1] != "" }
                                ^^
  ```

- Warning: `subworkflows/local/reference_indexing.nf:129:19`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          .filter { it[1] != "" }
                    ^^
  ```

- Warning: `subworkflows/local/reference_indexing.nf:135:9`: Variable was declared but not used

  ```nextflow
          ch_elongated_for_gunzip = ch_reference_to_elongate
          ^^^^^^^^^^^^^^^^^^^^^^^
  ```

- Warning: `subworkflows/local/reference_indexing.nf:137:29`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
                              meta, circular_target, circularmapper_elongatedfasta, circularmapper_elongatedindex ->
                              ^^^^
  ```

- Warning: `subworkflows/local/reference_indexing.nf:137:52`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
                              meta, circular_target, circularmapper_elongatedfasta, circularmapper_elongatedindex ->
                                                     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  ```

- Warning: `subworkflows/local/reference_indexing.nf:137:83`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
                              meta, circular_target, circularmapper_elongatedfasta, circularmapper_elongatedindex ->
                                                                                    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  ```

- Warning: `subworkflows/local/reference_indexing.nf:150:33`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
          ch_elongated_chr_list = Channel.empty()
                                  ^^^^^^^
  ```

- Warning: `subworkflows/local/reference_indexing_multi.nf:18:19`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_versions = Channel.empty()
                    ^^^^^^^
  ```

- Warning: `subworkflows/local/reference_indexing_multi.nf:21:41`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_splitreferencesheet_for_branch = Channel
                                          ^^^^^^^
  ```

- Warning: `subworkflows/local/reference_indexing_multi.nf:70:75`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
      ch_fasta_for_gunzip = ch_input_from_referencesheet.generated.branch { meta, fasta, fai, dict, mapper_index ->
                                                                            ^^^^
  ```

- Warning: `subworkflows/local/reference_indexing_multi.nf:70:88`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
      ch_fasta_for_gunzip = ch_input_from_referencesheet.generated.branch { meta, fasta, fai, dict, mapper_index ->
                                                                                         ^^^
  ```

- Warning: `subworkflows/local/reference_indexing_multi.nf:70:93`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
      ch_fasta_for_gunzip = ch_input_from_referencesheet.generated.branch { meta, fasta, fai, dict, mapper_index ->
                                                                                              ^^^^
  ```

- Warning: `subworkflows/local/reference_indexing_multi.nf:70:99`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
      ch_fasta_for_gunzip = ch_input_from_referencesheet.generated.branch { meta, fasta, fai, dict, mapper_index ->
                                                                                                    ^^^^^^^^^^^^
  ```

- Warning: `subworkflows/local/reference_indexing_multi.nf:94:60`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
      ch_fasta_for_faidx = ch_fasta_for_faiindexing.branch { meta, fasta, fai, dict, mapper_index ->
                                                             ^^^^
  ```

- Warning: `subworkflows/local/reference_indexing_multi.nf:94:66`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
      ch_fasta_for_faidx = ch_fasta_for_faiindexing.branch { meta, fasta, fai, dict, mapper_index ->
                                                                   ^^^^^
  ```

- Warning: `subworkflows/local/reference_indexing_multi.nf:94:78`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
      ch_fasta_for_faidx = ch_fasta_for_faiindexing.branch { meta, fasta, fai, dict, mapper_index ->
                                                                               ^^^^
  ```

- Warning: `subworkflows/local/reference_indexing_multi.nf:94:84`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
      ch_fasta_for_faidx = ch_fasta_for_faiindexing.branch { meta, fasta, fai, dict, mapper_index ->
                                                                                     ^^^^^^^^^^^^
  ```

- Warning: `subworkflows/local/reference_indexing_multi.nf:100:74`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
      ch_faidx_input = ch_fasta_for_faidx.forfaidx.multiMap { meta, fasta, fai, dict, mapper_index ->
                                                                           ^^^
  ```

- Warning: `subworkflows/local/reference_indexing_multi.nf:123:60`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
      ch_fasta_for_dict = ch_fasta_for_dictindexing.branch { meta, fasta, fai, dict, mapper_index ->
                                                             ^^^^
  ```

- Warning: `subworkflows/local/reference_indexing_multi.nf:123:66`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
      ch_fasta_for_dict = ch_fasta_for_dictindexing.branch { meta, fasta, fai, dict, mapper_index ->
                                                                   ^^^^^
  ```

- Warning: `subworkflows/local/reference_indexing_multi.nf:123:73`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
      ch_fasta_for_dict = ch_fasta_for_dictindexing.branch { meta, fasta, fai, dict, mapper_index ->
                                                                          ^^^
  ```

- Warning: `subworkflows/local/reference_indexing_multi.nf:123:84`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
      ch_fasta_for_dict = ch_fasta_for_dictindexing.branch { meta, fasta, fai, dict, mapper_index ->
                                                                                     ^^^^^^^^^^^^
  ```

- Warning: `subworkflows/local/reference_indexing_multi.nf:128:76`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
      ch_dict_input = ch_fasta_for_dict.fordict.multiMap { meta, fasta, fai, dict, mapper_index ->
                                                                             ^^^^
  ```

- Warning: `subworkflows/local/reference_indexing_multi.nf:151:67`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
      ch_fasta_for_mapperindex = ch_dict_formapperindexing.branch { meta, fasta, fai, dict, mapper_index ->
                                                                    ^^^^
  ```

- Warning: `subworkflows/local/reference_indexing_multi.nf:151:73`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
      ch_fasta_for_mapperindex = ch_dict_formapperindexing.branch { meta, fasta, fai, dict, mapper_index ->
                                                                          ^^^^^
  ```

- Warning: `subworkflows/local/reference_indexing_multi.nf:151:80`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
      ch_fasta_for_mapperindex = ch_dict_formapperindexing.branch { meta, fasta, fai, dict, mapper_index ->
                                                                                 ^^^
  ```

- Warning: `subworkflows/local/reference_indexing_multi.nf:151:85`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
      ch_fasta_for_mapperindex = ch_dict_formapperindexing.branch { meta, fasta, fai, dict, mapper_index ->
                                                                                      ^^^^
  ```

- Warning: `subworkflows/local/reference_indexing_multi.nf:156:94`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
      ch_mapindex_input = ch_fasta_for_mapperindex.forindex.multiMap { meta, fasta, fai, dict, mapper_index ->
                                                                                               ^^^^^^^^^^^^
  ```

- Warning: `subworkflows/local/reference_indexing_single.nf:23:19`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_versions = Channel.empty()
                    ^^^^^^^
  ```

- Warning: `subworkflows/local/reference_indexing_single.nf:30:21`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
          ch_gz_ref = Channel.fromPath(fasta).map{[[], it]}
                      ^^^^^^^
  ```

- Warning: `subworkflows/local/reference_indexing_single.nf:30:54`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          ch_gz_ref = Channel.fromPath(fasta).map{[[], it]}
                                                       ^^
  ```

- Warning: `subworkflows/local/reference_indexing_single.nf:32:70`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          ch_ungz_ref = GUNZIP_FASTA.out.gunzip.map{[[id: clean_name], it[1] ]}
                                                                       ^^
  ```

- Warning: `subworkflows/local/reference_indexing_single.nf:35:23`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
          ch_ungz_ref = Channel.fromPath(fasta).map{[[id: clean_name], it ]}
                        ^^^^^^^
  ```

- Warning: `subworkflows/local/reference_indexing_single.nf:35:70`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          ch_ungz_ref = Channel.fromPath(fasta).map{[[id: clean_name], it ]}
                                                                       ^^
  ```

- Warning: `subworkflows/local/reference_indexing_single.nf:40:104`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          ch_fasta_fai = SAMTOOLS_FAIDX ( ch_ungz_ref, [ [], [] ] ).fai.map{[ [id: clean_name - '.fai'], it[1] ] }
                                                                                                         ^^
  ```

- Warning: `subworkflows/local/reference_indexing_single.nf:43:24`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
          ch_fasta_fai = Channel.fromPath(fasta_fai).map{[[id: clean_name], it ]}
                         ^^^^^^^
  ```

- Warning: `subworkflows/local/reference_indexing_single.nf:43:75`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          ch_fasta_fai = Channel.fromPath(fasta_fai).map{[[id: clean_name], it ]}
                                                                            ^^
  ```

- Warning: `subworkflows/local/reference_indexing_single.nf:48:121`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          ch_fasta_dict = PICARD_CREATESEQUENCEDICTIONARY ( ch_ungz_ref ).reference_dict.map{[ [id: clean_name - '.fai'], it[1] ] }
                                                                                                                          ^^
  ```

- Warning: `subworkflows/local/reference_indexing_single.nf:51:25`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
          ch_fasta_dict = Channel.fromPath(fasta_dict).map{[[id: clean_name], it ]}
                          ^^^^^^^
  ```

- Warning: `subworkflows/local/reference_indexing_single.nf:51:77`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          ch_fasta_dict = Channel.fromPath(fasta_dict).map{[[id: clean_name], it ]}
                                                                              ^^
  ```

- Warning: `subworkflows/local/reference_indexing_single.nf:61:39`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
              ch_fasta_mapperindexdir = Channel.fromPath(fasta_mapperindexdir).map{[[id: clean_name], it ]}
                                        ^^^^^^^
  ```

- Warning: `subworkflows/local/reference_indexing_single.nf:61:101`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
              ch_fasta_mapperindexdir = Channel.fromPath(fasta_mapperindexdir).map{[[id: clean_name], it ]}
                                                                                                      ^^
  ```

- Warning: `subworkflows/local/reference_indexing_single.nf:70:39`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
              ch_fasta_mapperindexdir = Channel.fromPath(fasta_mapperindexdir).map{[[id: clean_name], it ]}
                                        ^^^^^^^
  ```

- Warning: `subworkflows/local/reference_indexing_single.nf:70:101`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
              ch_fasta_mapperindexdir = Channel.fromPath(fasta_mapperindexdir).map{[[id: clean_name], it ]}
                                                                                                      ^^
  ```

- Warning: `subworkflows/local/reference_indexing_single.nf:79:39`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
              ch_fasta_mapperindexdir = Channel.fromPath(fasta_mapperindexdir).map{[[id: clean_name], it ]}
                                        ^^^^^^^
  ```

- Warning: `subworkflows/local/reference_indexing_single.nf:79:101`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
              ch_fasta_mapperindexdir = Channel.fromPath(fasta_mapperindexdir).map{[[id: clean_name], it ]}
                                                                                                      ^^
  ```

- Warning: `subworkflows/local/run_sex_determination.nf:17:25`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_versions       = Channel.empty()
                          ^^^^^^^
  ```

- Warning: `subworkflows/local/run_sex_determination.nf:18:25`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_multiqc_files  = Channel.empty()
                          ^^^^^^^
  ```

- Warning: `subworkflows/local/run_sex_determination.nf:27:43`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
                  addNewMetaFromAttributes( it, "id" , "reference" , false )
                                            ^^
  ```

- Warning: `subworkflows/local/run_sex_determination.nf:33:43`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
                  addNewMetaFromAttributes( it, "reference" , "reference" , false )
                                            ^^
  ```

- Warning: `subworkflows/local/run_sex_determination.nf:38:41`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
                  combo_meta, metas, bam, bai, ref_meta, bed ->
                                          ^^^
  ```

- Warning: `subworkflows/nf-core/bam_docounts_contamination_angsd/main.nf:16:19`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_versions = Channel.empty()
                    ^^^^^^^
  ```

- Warning: `subworkflows/nf-core/fastq_align_bwaaln/main.nf:18:19`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_versions = Channel.empty()
                    ^^^^^^^
  ```

- Warning: `subworkflows/nf-core/fastq_align_bwaaln/main.nf:45:42`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
                              meta, reads, meta_index, index ->
                                           ^^^^^^^^^^
  ```

- Warning: `subworkflows/nf-core/fastq_align_bwaaln/main.nf:53:57`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
      ch_reads_newid = ch_prepped_input.map{ meta, reads, meta_index, index -> [ meta, reads ] }
                                                          ^^^^^^^^^^
  ```

- Warning: `subworkflows/nf-core/fastq_align_bwaaln/main.nf:53:69`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
      ch_reads_newid = ch_prepped_input.map{ meta, reads, meta_index, index -> [ meta, reads ] }
                                                                      ^^^^^
  ```

- Warning: `subworkflows/nf-core/fastq_align_bwaaln/main.nf:54:50`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
      ch_index_newid = ch_prepped_input.map{ meta, reads, meta_index, index -> [ meta, index ] }
                                                   ^^^^^
  ```

- Warning: `subworkflows/nf-core/fastq_align_bwaaln/main.nf:54:57`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
      ch_index_newid = ch_prepped_input.map{ meta, reads, meta_index, index -> [ meta, index ] }
                                                          ^^^^^^^^^^
  ```

- Warning: `subworkflows/nf-core/fastq_align_bwaaln/main.nf:63:35`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
                              meta, reads, sai ->
                                    ^^^^^
  ```

- Warning: `subworkflows/nf-core/fastq_align_bwaaln/main.nf:63:42`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
                              meta, reads, sai ->
                                           ^^^
  ```

- Warning: `subworkflows/nf-core/utils_nfcore_pipeline/main.nf:101:98`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      return ch_versions.unique().map { version -> processVersionsFromYAML(version) }.unique().mix(Channel.of(workflowVersionToYAML()))
                                                                                                   ^^^^^^^
  ```

- Warning: `workflows/eager.nf:81:19`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_versions = Channel.empty()
                    ^^^^^^^
  ```

- Warning: `workflows/eager.nf:82:24`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_multiqc_files = Channel.empty()
                         ^^^^^^^
  ```

- Warning: `workflows/eager.nf:112:29`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
              .filter { meta, reads ->
                              ^^^^^
  ```

- Warning: `workflows/eager.nf:124:83`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          ch_paired_end_reads = SAMTOOLS_CONVERT_BAM_INPUT.out.fastq.filter { meta, reads ->
                                                                                    ^^^^^
  ```

- Warning: `workflows/eager.nf:156:73`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          ch_multiqc_files = ch_multiqc_files.mix(FALCO.out.txt.collect { it[1] }.ifEmpty([]))
                                                                          ^^
  ```

- Warning: `workflows/eager.nf:161:74`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          ch_multiqc_files = ch_multiqc_files.mix(FASTQC.out.zip.collect { it[1] }.ifEmpty([]))
                                                                           ^^
  ```

- Warning: `workflows/eager.nf:172:81`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          ch_multiqc_files = ch_multiqc_files.mix(PREPROCESSING.out.mqc.collect { it[1] }.ifEmpty([]))
                                                                                  ^^
  ```

- Warning: `workflows/eager.nf:181:84`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
      ch_reference_for_mapping = REFERENCE_INDEXING.out.reference.map { meta, fasta, fai, dict, index ->
                                                                                     ^^^
  ```

- Warning: `workflows/eager.nf:181:89`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
      ch_reference_for_mapping = REFERENCE_INDEXING.out.reference.map { meta, fasta, fai, dict, index ->
                                                                                          ^^^^
  ```

- Warning: `workflows/eager.nf:188:67`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
      ch_multiqc_files = ch_multiqc_files.mix(MAP.out.mqc.collect { it[1] }.ifEmpty([]))
                                                                    ^^
  ```

- Warning: `workflows/eager.nf:213:51`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
          ch_bams_from_input_lanemerged           = Channel.empty()
                                                    ^^^^^^^
  ```

- Warning: `workflows/eager.nf:214:51`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
          ch_flagstat_bams_from_input_lanemerged  = Channel.empty()
                                                    ^^^^^^^
  ```

- Warning: `workflows/eager.nf:231:78`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          ch_multiqc_files = ch_multiqc_files.mix(FILTER_BAM.out.mqc.collect { it[1] }.ifEmpty([]))
                                                                               ^^
  ```

- Warning: `workflows/eager.nf:245:96`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
      ch_fasta_for_deduplication = REFERENCE_INDEXING.out.reference.multiMap { meta, fasta, fai, dict, index ->
                                                                                                 ^^^^
  ```

- Warning: `workflows/eager.nf:245:102`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
      ch_fasta_for_deduplication = REFERENCE_INDEXING.out.reference.multiMap { meta, fasta, fai, dict, index ->
                                                                                                       ^^^^^
  ```

- Warning: `workflows/eager.nf:258:32`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
          ch_dedupped_flagstat = Channel.empty()
                                 ^^^^^^^
  ```

- Warning: `workflows/eager.nf:268:79`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
      ch_multiqc_files = ch_multiqc_files.mix(MERGE_LIBRARIES.out.mqc.collect { it[1] }.ifEmpty([]))
                                                                                ^^
  ```

- Warning: `workflows/eager.nf:276:38`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
              addNewMetaFromAttributes(it, "id", "reference", false)
                                       ^^
  ```

- Warning: `workflows/eager.nf:279:31`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
              .map { meta, bam, bai ->
                                ^^^
  ```

- Warning: `workflows/eager.nf:283:42`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
                  addNewMetaFromAttributes(it, "reference", "reference", false)
                                           ^^
  ```

- Warning: `workflows/eager.nf:289:23`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
              .branch { ignore_meta, meta, bam, meta2, snp_capture_bed ->
                        ^^^^^^^^^^^
  ```

- Warning: `workflows/eager.nf:289:36`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
              .branch { ignore_meta, meta, bam, meta2, snp_capture_bed ->
                                     ^^^^
  ```

- Warning: `workflows/eager.nf:289:42`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
              .branch { ignore_meta, meta, bam, meta2, snp_capture_bed ->
                                           ^^^
  ```

- Warning: `workflows/eager.nf:289:47`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
              .branch { ignore_meta, meta, bam, meta2, snp_capture_bed ->
                                                ^^^^^
  ```

- Warning: `workflows/eager.nf:293:71`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          ch_qualimap_input_with = ch_qualimap_input.withbed.multiMap { ignore_meta, meta, bam, meta2, snp_capture_bed ->
                                                                        ^^^^^^^^^^^
  ```

- Warning: `workflows/eager.nf:293:95`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          ch_qualimap_input_with = ch_qualimap_input.withbed.multiMap { ignore_meta, meta, bam, meta2, snp_capture_bed ->
                                                                                                ^^^^^
  ```

- Warning: `workflows/eager.nf:299:67`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          ch_qualimap_input_without = ch_qualimap_input.nobed.map { ignore_meta, meta, bam, meta2, snp_capture_bed ->
                                                                    ^^^^^^^^^^^
  ```

- Warning: `workflows/eager.nf:299:91`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          ch_qualimap_input_without = ch_qualimap_input.nobed.map { ignore_meta, meta, bam, meta2, snp_capture_bed ->
                                                                                            ^^^^^
  ```

- Warning: `workflows/eager.nf:299:98`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          ch_qualimap_input_without = ch_qualimap_input.nobed.map { ignore_meta, meta, bam, meta2, snp_capture_bed ->
                                                                                                   ^^^^^^^^^^^^^^^
  ```

- Warning: `workflows/eager.nf:319:51`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
                  new_meta = meta.clone().findAll { it.key !in ['single_end', 'reference'] }
                                                    ^^
  ```

- Warning: `workflows/eager.nf:326:47`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
              new_meta = meta.clone().findAll { it.key !in ['lane', 'colour_chemistry', 'single_end'] }
                                                ^^
  ```

- Warning: `workflows/eager.nf:333:20`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
              .map { meta_join, meta_bam, bam, bai, meta_fastq, fastqs ->
                     ^^^^^^^^^
  ```

- Warning: `workflows/eager.nf:348:23`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
          ch_database = Channel.fromPath(params.metagenomics_profiling_database)
                        ^^^^^^^
  ```

- Warning: `workflows/eager.nf:351:23`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
          ch_tax_list = Channel.empty()
                        ^^^^^^^
  ```

- Warning: `workflows/eager.nf:352:23`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
          ch_ncbi_dir = Channel.empty()
                        ^^^^^^^
  ```

- Warning: `workflows/eager.nf:355:27`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
              ch_tax_list = Channel.fromPath(params.metagenomics_maltextract_taxonlist, checkIfExists: true)
                            ^^^^^^^
  ```

- Warning: `workflows/eager.nf:356:27`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
              ch_ncbi_dir = Channel.fromPath(params.metagenomics_maltextract_ncbidir, checkIfExists: true)
                            ^^^^^^^
  ```

- Warning: `workflows/eager.nf:370:38`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
              addNewMetaFromAttributes(it, "id", "reference", false)
                                       ^^
  ```

- Warning: `workflows/eager.nf:374:42`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
                  addNewMetaFromAttributes(it, "reference", "reference", false)
                                           ^^
  ```

- Warning: `workflows/eager.nf:380:25`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
              .multiMap { ignore_meta, meta, bam, bai, meta2, mito_header ->
                          ^^^^^^^^^^^
  ```

- Warning: `workflows/eager.nf:380:49`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
              .multiMap { ignore_meta, meta, bam, bai, meta2, mito_header ->
                                                  ^^^
  ```

- Warning: `workflows/eager.nf:385:77`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          MTNUCRATIO(mtnucratio_input.bam, mtnucratio_input.mito_header.map { it[1] })
                                                                              ^^
  ```

- Warning: `workflows/eager.nf:386:85`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          ch_multiqc_files = ch_multiqc_files.mix(MTNUCRATIO.out.mtnucratio.collect { it[1] }.ifEmpty([]))
                                                                                      ^^
  ```

- Warning: `workflows/eager.nf:425:73`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
      ch_multiqc_files = ch_multiqc_files.mix(ENDORSPY.out.json.collect { it[1] }.ifEmpty([]))
                                                                          ^^
  ```

- Warning: `workflows/eager.nf:432:57`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          PRESEQ_CCURVE(ch_reads_for_deduplication.map { [it[0], it[1]] })
                                                          ^^
  ```

- Warning: `workflows/eager.nf:432:64`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          PRESEQ_CCURVE(ch_reads_for_deduplication.map { [it[0], it[1]] })
                                                                 ^^
  ```

- Warning: `workflows/eager.nf:433:85`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          ch_multiqc_files = ch_multiqc_files.mix(PRESEQ_CCURVE.out.c_curve.collect { it[1] }.ifEmpty([]))
                                                                                      ^^
  ```

- Warning: `workflows/eager.nf:437:59`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          PRESEQ_LCEXTRAP(ch_reads_for_deduplication.map { [it[0], it[1]] })
                                                            ^^
  ```

- Warning: `workflows/eager.nf:437:66`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          PRESEQ_LCEXTRAP(ch_reads_for_deduplication.map { [it[0], it[1]] })
                                                                   ^^
  ```

- Warning: `workflows/eager.nf:438:89`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          ch_multiqc_files = ch_multiqc_files.mix(PRESEQ_LCEXTRAP.out.lc_extrap.collect { it[1] }.ifEmpty([]))
                                                                                          ^^
  ```

- Warning: `workflows/eager.nf:449:38`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
              addNewMetaFromAttributes(it, "id", "reference", false)
                                       ^^
  ```

- Warning: `workflows/eager.nf:454:42`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
                  addNewMetaFromAttributes(it, "reference", "reference", false)
                                           ^^
  ```

- Warning: `workflows/eager.nf:460:20`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
              .map { ignore_meta, meta, bam, bai, meta2, bedtools_feature ->
                     ^^^^^^^^^^^
  ```

- Warning: `workflows/eager.nf:460:49`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
              .map { ignore_meta, meta, bam, bai, meta2, bedtools_feature ->
                                                  ^^^^^
  ```

- Warning: `workflows/eager.nf:463:23`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
              .branch { meta, bedtools_feature, bam, bai ->
                        ^^^^
  ```

- Warning: `workflows/eager.nf:463:47`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
              .branch { meta, bedtools_feature, bam, bai ->
                                                ^^^
  ```

- Warning: `workflows/eager.nf:463:52`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
              .branch { meta, bedtools_feature, bam, bai ->
                                                     ^^^
  ```

- Warning: `workflows/eager.nf:489:100`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
      ch_fasta_for_damagecalculation = REFERENCE_INDEXING.out.reference.multiMap { meta, fasta, fai, dict, index ->
                                                                                                     ^^^^
  ```

- Warning: `workflows/eager.nf:489:106`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
      ch_fasta_for_damagecalculation = REFERENCE_INDEXING.out.reference.multiMap { meta, fasta, fai, dict, index ->
                                                                                                           ^^^^^
  ```

- Warning: `workflows/eager.nf:497:84`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          ch_multiqc_files = ch_multiqc_files.mix(CALCULATE_DAMAGE.out.mqc.collect { it[1] }.ifEmpty([]))
                                                                                     ^^
  ```

- Warning: `workflows/eager.nf:509:85`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          ch_multiqc_files = ch_multiqc_files.mix(RUN_SEXDETERRMINE.out.mqc.collect { it[1] }.ifEmpty([]))
                                                                                      ^^
  ```

- Warning: `workflows/eager.nf:521:90`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          ch_multiqc_files = ch_multiqc_files.mix(ESTIMATE_CONTAMINATION.out.mqc.collect { it[1] }.ifEmpty([]))
                                                                                           ^^
  ```

- Warning: `workflows/eager.nf:530:90`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          ch_multiqc_files = ch_multiqc_files.mix(MANIPULATE_DAMAGE.out.flagstat.collect { it[1] }.ifEmpty([]))
                                                                                           ^^
  ```

- Warning: `workflows/eager.nf:538:94`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          ch_multiqc_files = ch_multiqc_files.mix(MERGE_LIBRARIES_GENOTYPING.out.mqc.collect { it[1] }.ifEmpty([]))
                                                                                               ^^
  ```

- Warning: `workflows/eager.nf:549:102`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          ch_reference_for_genotyping = REFERENCE_INDEXING.out.reference.map { meta, fasta, fai, dict, mapindex ->
                                                                                                       ^^^^^^^^
  ```

- Warning: `workflows/eager.nf:560:76`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          ch_multiqc_files = ch_multiqc_files.mix(GENOTYPE.out.mqc.collect { it[1] }.ifEmpty([]))
                                                                             ^^
  ```

- Warning: `workflows/eager.nf:579:25`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_multiqc_config = Channel.fromPath(
                          ^^^^^^^
  ```

- Warning: `workflows/eager.nf:584:11`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
          ? Channel.fromPath(params.multiqc_config, checkIfExists: true)
            ^^^^^^^
  ```

- Warning: `workflows/eager.nf:585:11`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
          : Channel.empty()
            ^^^^^^^
  ```

- Warning: `workflows/eager.nf:587:11`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
          ? Channel.fromPath(params.multiqc_logo, checkIfExists: true)
            ^^^^^^^
  ```

- Warning: `workflows/eager.nf:588:11`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
          : Channel.empty()
            ^^^^^^^
  ```

- Warning: `workflows/eager.nf:594:27`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_workflow_summary = Channel.value(paramsSummaryMultiqc(summary_params))
                            ^^^^^^^
  ```

- Warning: `workflows/eager.nf:601:30`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_methods_description = Channel.value(
                               ^^^^^^^
  ```

- Warning: `workflows/eager.nf:614:78`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          ch_multiqc_files = ch_multiqc_files.mix(ch_qualimap_output.collect { it[1] }.ifEmpty([]))
                                                                               ^^
  ```
