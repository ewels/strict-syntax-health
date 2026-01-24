# Nextflow lint results

- Generated: 2026-01-24T00:18:23.039319374Z
- Nextflow version: 25.12.0-edge
- Summary: 26 errors, 70 warnings

## :x: Errors

- Error: `modules/local/collect/featurecounts/main.nf:9:5`: Unexpected input: '}'

  ```nextflow
      }"
      ^
  ```

- Error: `modules/local/collect/stats/main.nf:9:5`: Unexpected input: '}'

  ```nextflow
      }"
      ^
  ```

- Error: `modules/local/prokkagff2tsv/main.nf:9:5`: Unexpected input: '}'

  ```nextflow
      }"
      ^
  ```

- Error: `modules/local/tidyverse/joinmetadata/main.nf:9:5`: Unexpected input: '}'

  ```nextflow
      }"
      ^
  ```

- Error: `modules/nf-core/custom/dumpsoftwareversions/main.nf:1:1`: Statements cannot be mixed with script declarations -- move statements into a process, workflow, or function

  ```nextflow
  def deprecation_message = """
  ^^^
  ```

- Error: `modules/nf-core/custom/dumpsoftwareversions/main.nf:30:18`: `deprecation_message` is not defined

  ```nextflow
      assert true: deprecation_message
                   ^^^^^^^^^^^^^^^^^^^
  ```

- Error: `subworkflows/local/sourmash/main.nf:82:89`: Unexpected input: ')'

  ```nextflow
                  .combine(ch_indexes.map { index -> [ [ id: sprintf("remoteidx_%02d", i++) ], index ] })
                                                                                          ^
  ```

- Error: `workflows/magmap.nf:14:1`: Module could not be parsed: '/home/runner/work/strict-syntax-health/strict-syntax-health/pipelines/magmap/modules/local/collect/featurecounts/main.nf'

  ```nextflow
  include { COLLECT_FEATURECOUNTS                  } from '../modules/local/collect/featurecounts'
  ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  ```

- Error: `workflows/magmap.nf:15:1`: Module could not be parsed: '/home/runner/work/strict-syntax-health/strict-syntax-health/pipelines/magmap/modules/local/collect/stats/main.nf'

  ```nextflow
  include { COLLECT_STATS                          } from '../modules/local/collect/stats'
  ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  ```

- Error: `workflows/magmap.nf:26:1`: Module could not be parsed: '/home/runner/work/strict-syntax-health/strict-syntax-health/pipelines/magmap/modules/local/prokkagff2tsv/main.nf'

  ```nextflow
  include { PROKKAGFF2TSV                          } from '../modules/local/prokkagff2tsv'
  ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  ```

- Error: `workflows/magmap.nf:29:1`: Module could not be parsed: '/home/runner/work/strict-syntax-health/strict-syntax-health/pipelines/magmap/subworkflows/local/sourmash/main.nf'

  ```nextflow
  include { SOURMASH                               } from '../subworkflows/local/sourmash'
  ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  ```

- Error: `workflows/magmap.nf:31:1`: Module could not be parsed: '/home/runner/work/strict-syntax-health/strict-syntax-health/pipelines/magmap/modules/local/tidyverse/joinmetadata/main.nf'

  ```nextflow
  include { TIDYVERSE_JOINMETADATA                 } from '../modules/local/tidyverse/joinmetadata/'
  ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  ```

- Error: `workflows/magmap.nf:193:5`: `SOURMASH` is not defined

  ```nextflow
      SOURMASH(
      ^^^^^^^^
  ```

- Error: `workflows/magmap.nf:202:35`: `SOURMASH` is not defined

  ```nextflow
      ch_versions = ch_versions.mix(SOURMASH.out.versions)
                                    ^^^^^^^^
  ```

- Error: `workflows/magmap.nf:203:18`: `SOURMASH` is not defined

  ```nextflow
      ch_genomes = SOURMASH.out.filtered_genomes
                   ^^^^^^^^
  ```

- Error: `workflows/magmap.nf:208:5`: `TIDYVERSE_JOINMETADATA` is not defined

  ```nextflow
      TIDYVERSE_JOINMETADATA(
      ^^^^^^^^^^^^^^^^^^^^^^
  ```

- Error: `workflows/magmap.nf:218:35`: `TIDYVERSE_JOINMETADATA` is not defined

  ```nextflow
      ch_versions = ch_versions.mix(TIDYVERSE_JOINMETADATA.out.versions.first())
                                    ^^^^^^^^^^^^^^^^^^^^^^
  ```

- Error: `workflows/magmap.nf:233:5`: `PROKKAGFF2TSV` is not defined

  ```nextflow
      PROKKAGFF2TSV(
      ^^^^^^^^^^^^^
  ```

- Error: `workflows/magmap.nf:236:35`: `PROKKAGFF2TSV` is not defined

  ```nextflow
      ch_versions = ch_versions.mix(PROKKAGFF2TSV.out.versions)
                                    ^^^^^^^^^^^^^
  ```

- Error: `workflows/magmap.nf:242:17`: `PROKKAGFF2TSV` is not defined

  ```nextflow
                  PROKKAGFF2TSV.out.tsv.map { t -> t[1] }
                  ^^^^^^^^^^^^^
  ```

- Error: `workflows/magmap.nf:317:5`: `COLLECT_FEATURECOUNTS` is not defined

  ```nextflow
      COLLECT_FEATURECOUNTS(ch_collect_featurecounts)
      ^^^^^^^^^^^^^^^^^^^^^
  ```

- Error: `workflows/magmap.nf:318:45`: `COLLECT_FEATURECOUNTS` is not defined

  ```nextflow
      ch_versions           = ch_versions.mix(COLLECT_FEATURECOUNTS.out.versions)
                                              ^^^^^^^^^^^^^^^^^^^^^
  ```

- Error: `workflows/magmap.nf:320:29`: `COLLECT_FEATURECOUNTS` is not defined

  ```nextflow
      ch_fcs_for_stats      = COLLECT_FEATURECOUNTS.out.counts.collect { meta, tsv -> tsv }.map { [ it ] }
                              ^^^^^^^^^^^^^^^^^^^^^
  ```

- Error: `workflows/magmap.nf:321:29`: `COLLECT_FEATURECOUNTS` is not defined

  ```nextflow
      ch_fcs_for_summary    = COLLECT_FEATURECOUNTS.out.counts.map { meta, tsv -> tsv }
                              ^^^^^^^^^^^^^^^^^^^^^
  ```

- Error: `workflows/magmap.nf:327:5`: `COLLECT_STATS` is not defined

  ```nextflow
      COLLECT_STATS(ch_collect_stats.map { s -> s + [[]] }) // The last [[]] is to create a value for the `mergetab` that we have in metatdenovo (which shares the swf)
      ^^^^^^^^^^^^^
  ```

- Error: `workflows/magmap.nf:328:39`: `COLLECT_STATS` is not defined

  ```nextflow
      ch_versions     = ch_versions.mix(COLLECT_STATS.out.versions)
                                        ^^^^^^^^^^^^^
  ```

## :warning: Warnings

- Warning: `modules/local/cat/many/main.nf:21:9`: Variable was declared but not used

  ```nextflow
      def args    = task.ext.args ?: ''
          ^^^^
  ```

- Warning: `modules/local/catprokkatsvs/main.nf:21:9`: Variable was declared but not used

  ```nextflow
      def args = task.ext.args ?: ''
          ^^^^
  ```

- Warning: `modules/nf-core/bbmap/bbduk/main.nf:45:9`: Variable was declared but not used

  ```nextflow
      def args = task.ext.args ?: ''
          ^^^^
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

- Warning: `modules/nf-core/cat/fastq/main.nf:22:60`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
      def readList = reads instanceof List ? reads.collect { it.toString() } : [reads.toString()]
                                                             ^^
  ```

- Warning: `modules/nf-core/cat/fastq/main.nf:58:60`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
      def readList = reads instanceof List ? reads.collect { it.toString() } : [reads.toString()]
                                                             ^^
  ```

- Warning: `modules/nf-core/custom/dumpsoftwareversions/main.nf:1:5`: Variable was declared but not used

  ```nextflow
  def deprecation_message = """
      ^^^^^^^^^^^^^^^^^^^
  ```

- Warning: `modules/nf-core/custom/dumpsoftwareversions/main.nf:31:9`: Variable was declared but not used

  ```nextflow
      def args = task.ext.args ?: ''
          ^^^^
  ```

- Warning: `modules/nf-core/pigz/compress/main.nf:35:9`: Variable was declared but not used

  ```nextflow
      def args = task.ext.args ?: ''
          ^^^^
  ```

- Warning: `modules/nf-core/trimgalore/main.nf:47:31`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          args_list.removeAll { it.toLowerCase().contains('_r2 ') }
                                ^^
  ```

- Warning: `subworkflows/local/concatenate_gffs/main.nf:13:23`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
          ch_versions = Channel.empty()
                        ^^^^^^^
  ```

- Warning: `subworkflows/local/create_bbmap_index/main.nf:12:23`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
          ch_versions = Channel.empty()
                        ^^^^^^^
  ```

- Warning: `subworkflows/local/create_bbmap_index/main.nf:16:58`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          BBMAP_INDEX (CAT_FNA.out.concatenated_files.map{ it[1]})
                                                           ^^
  ```

- Warning: `subworkflows/local/fastqc_trimgalore/main.nf:15:22`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_versions    = Channel.empty()
                       ^^^^^^^
  ```

- Warning: `subworkflows/local/fastqc_trimgalore/main.nf:16:22`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      fastqc_html    = Channel.empty()
                       ^^^^^^^
  ```

- Warning: `subworkflows/local/fastqc_trimgalore/main.nf:17:22`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      fastqc_zip     = Channel.empty()
                       ^^^^^^^
  ```

- Warning: `subworkflows/local/fastqc_trimgalore/main.nf:26:18`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      trim_html  = Channel.empty()
                   ^^^^^^^
  ```

- Warning: `subworkflows/local/fastqc_trimgalore/main.nf:27:18`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      trim_zip   = Channel.empty()
                   ^^^^^^^
  ```

- Warning: `subworkflows/local/fastqc_trimgalore/main.nf:28:18`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      trim_log   = Channel.empty()
                   ^^^^^^^
  ```

- Warning: `subworkflows/local/utils_nfcore_magmap_pipeline/main.nf:32:5`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
      monochrome_logs   // boolean: Do not use coloured log outputs
      ^^^^^^^^^^^^^^^
  ```

- Warning: `subworkflows/local/utils_nfcore_magmap_pipeline/main.nf:35:5`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
      input             //  string: Path to input samplesheet
      ^^^^^
  ```

- Warning: `subworkflows/local/utils_nfcore_magmap_pipeline/main.nf:39:5`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
      genomeinfo              //  string: Path to user-provided genome sheet
      ^^^^^^^^^^
  ```

- Warning: `subworkflows/local/utils_nfcore_magmap_pipeline/main.nf:41:5`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
      genome_store_dir        //  string: Path to a directory where genome annotation files will be stored
      ^^^^^^^^^^^^^^^^
  ```

- Warning: `subworkflows/local/utils_nfcore_magmap_pipeline/main.nf:135:21`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_genomeinfo = Channel.empty()
                      ^^^^^^^
  ```

- Warning: `subworkflows/local/utils_nfcore_magmap_pipeline/main.nf:137:9`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
          Channel
          ^^^^^^^
  ```

- Warning: `subworkflows/local/utils_nfcore_magmap_pipeline/main.nf:152:32`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_remote_genome_sources = Channel.empty()
                                 ^^^^^^^
  ```

- Warning: `subworkflows/local/utils_nfcore_magmap_pipeline/main.nf:154:36`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
          ch_remote_genome_sources = Channel
                                     ^^^^^^^
  ```

- Warning: `subworkflows/local/utils_nfcore_magmap_pipeline/main.nf:156:25`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
              .map { file(it) }
                          ^^
  ```

- Warning: `subworkflows/local/utils_nfcore_magmap_pipeline/main.nf:174:18`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_indexes = Channel.empty()
                   ^^^^^^^
  ```

- Warning: `subworkflows/local/utils_nfcore_magmap_pipeline/main.nf:176:22`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
          ch_indexes = Channel.fromPath(indexes)
                       ^^^^^^^
  ```

- Warning: `subworkflows/local/utils_nfcore_magmap_pipeline/main.nf:182:24`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_gtdb_metadata = Channel.empty()
                         ^^^^^^^
  ```

- Warning: `subworkflows/local/utils_nfcore_magmap_pipeline/main.nf:184:28`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
          ch_gtdb_metadata = Channel
                             ^^^^^^^
  ```

- Warning: `subworkflows/local/utils_nfcore_magmap_pipeline/main.nf:186:25`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
              .map { file(it) }
                          ^^
  ```

- Warning: `subworkflows/local/utils_nfcore_magmap_pipeline/main.nf:189:26`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_gtdbtk_metadata = Channel.empty()
                           ^^^^^^^
  ```

- Warning: `subworkflows/local/utils_nfcore_magmap_pipeline/main.nf:191:30`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
          ch_gtdbtk_metadata = Channel
                               ^^^^^^^
  ```

- Warning: `subworkflows/local/utils_nfcore_magmap_pipeline/main.nf:193:25`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
              .map { file(it) }
                          ^^
  ```

- Warning: `subworkflows/local/utils_nfcore_magmap_pipeline/main.nf:196:26`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_checkm_metadata = Channel.empty()
                           ^^^^^^^
  ```

- Warning: `subworkflows/local/utils_nfcore_magmap_pipeline/main.nf:198:30`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
          ch_checkm_metadata = Channel
                               ^^^^^^^
  ```

- Warning: `subworkflows/local/utils_nfcore_magmap_pipeline/main.nf:200:25`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
              .map { file(it) }
                          ^^
  ```

- Warning: `subworkflows/local/utils_nfcore_magmap_pipeline/main.nf:203:19`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_features = Channel.of(
                    ^^^^^^^
  ```

- Warning: `subworkflows/local/utils_nfcore_magmap_pipeline/main.nf:299:24`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
  def getGenomeAttribute(attribute) {
                         ^^^^^^^^^
  ```

- Warning: `subworkflows/nf-core/bam_sort_stats_samtools/main.nf:16:19`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_versions = Channel.empty()
                    ^^^^^^^
  ```

- Warning: `subworkflows/nf-core/bam_stats_samtools/main.nf:15:19`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_versions = Channel.empty()
                    ^^^^^^^
  ```

- Warning: `workflows/magmap.nf:76:20`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          .flatMap { it.tokenize('\n') }
                     ^^
  ```

- Warning: `workflows/magmap.nf:108:19`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          .branch { meta, reads ->
                    ^^^^
  ```

- Warning: `workflows/magmap.nf:117:68`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
      ch_multiqc_files = ch_multiqc_files.mix(FASTQC.out.zip.collect{it[1]})
                                                                     ^^
  ```

- Warning: `workflows/magmap.nf:149:26`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          .collect { meta, fasta -> meta }
                           ^^^^^
  ```

- Warning: `workflows/magmap.nf:160:32`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
                      .collect { meta, report ->
                                 ^^^^
  ```

- Warning: `workflows/magmap.nf:167:30`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
                      .map { [ it ] }
                               ^^
  ```

- Warning: `workflows/magmap.nf:179:55`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          ch_bbduk_logs = BBMAP_BBDUK.out.log.collect { it[1] }.map { [ it ] }
                                                        ^^
  ```

- Warning: `workflows/magmap.nf:179:71`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          ch_bbduk_logs = BBMAP_BBDUK.out.log.collect { it[1] }.map { [ it ] }
                                                                        ^^
  ```

- Warning: `workflows/magmap.nf:182:78`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          ch_multiqc_files = ch_multiqc_files.mix(BBMAP_BBDUK.out.log.collect{ meta, log -> log })
                                                                               ^^^^
  ```

- Warning: `workflows/magmap.nf:187:22`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
              .map { [ it[0], it[1], it[2], [] ] }
                       ^^
  ```

- Warning: `workflows/magmap.nf:187:29`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
              .map { [ it[0], it[1], it[2], [] ] }
                              ^^
  ```

- Warning: `workflows/magmap.nf:187:36`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
              .map { [ it[0], it[1], it[2], [] ] }
                                     ^^
  ```

- Warning: `workflows/magmap.nf:231:69`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
      ch_multiqc_files = ch_multiqc_files.mix(PROKKA.out.log.collect{ meta, log -> log })
                                                                      ^^^^
  ```

- Warning: `workflows/magmap.nf:261:51`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
      CREATE_BBMAP_INDEX(ch_collected_genomes.map { it.genome_fna })
                                                    ^^
  ```

- Warning: `workflows/magmap.nf:267:49`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
      CONCATENATE_GFFS(ch_collected_genomes.map { it.genome_gff })
                                                  ^^
  ```

- Warning: `workflows/magmap.nf:274:74`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
      ch_multiqc_files = ch_multiqc_files.mix(BBMAP_ALIGN.out.log.collect{ meta, log -> log })
                                                                           ^^^^
  ```

- Warning: `workflows/magmap.nf:284:49`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          .combine(CONCATENATE_GFFS.out.gff.map { it[1] })
                                                  ^^
  ```

- Warning: `workflows/magmap.nf:287:65`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          .combine(BAM_SORT_STATS_SAMTOOLS.out.idxstats.collect { it[1]}.map { [ it ] })
                                                                  ^^
  ```

- Warning: `workflows/magmap.nf:287:80`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          .combine(BAM_SORT_STATS_SAMTOOLS.out.idxstats.collect { it[1]}.map { [ it ] })
                                                                                 ^^
  ```

- Warning: `workflows/magmap.nf:300:80`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
      ch_multiqc_files = ch_multiqc_files.mix(FEATURECOUNTS.out.summary.collect{ meta, log -> log })
                                                                                 ^^^^
  ```

- Warning: `workflows/magmap.nf:309:40`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
              def metas = data.collect { it[0] }
                                         ^^
  ```

- Warning: `workflows/magmap.nf:310:40`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
              def files = data.collect { it[1] }
                                         ^^
  ```

- Warning: `workflows/magmap.nf:320:72`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
      ch_fcs_for_stats      = COLLECT_FEATURECOUNTS.out.counts.collect { meta, tsv -> tsv }.map { [ it ] }
                                                                         ^^^^
  ```

- Warning: `workflows/magmap.nf:320:99`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
      ch_fcs_for_stats      = COLLECT_FEATURECOUNTS.out.counts.collect { meta, tsv -> tsv }.map { [ it ] }
                                                                                                    ^^
  ```

- Warning: `workflows/magmap.nf:321:5`: Variable was declared but not used

  ```nextflow
      ch_fcs_for_summary    = COLLECT_FEATURECOUNTS.out.counts.map { meta, tsv -> tsv }
      ^^^^^^^^^^^^^^^^^^
  ```

- Warning: `workflows/magmap.nf:321:68`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
      ch_fcs_for_summary    = COLLECT_FEATURECOUNTS.out.counts.map { meta, tsv -> tsv }
                                                                     ^^^^
  ```
