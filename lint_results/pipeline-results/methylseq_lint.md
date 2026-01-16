# Nextflow lint results

- Generated: 2026-01-16T06:35:11.498808155Z
- Nextflow version: 25.12.0-edge
- Summary: 3 errors, 65 warnings

## :x: Errors

- Error: `modules/nf-core/rastair/mbiasparser/main.nf:15:26`: `trim_OT` is not defined

  ```nextflow
      tuple val(meta), env(trim_OT), env(trim_OB),                    emit: mbias_processed_str
                           ^^^^^^^
  ```

- Error: `modules/nf-core/rastair/mbiasparser/main.nf:15:40`: `trim_OB` is not defined

  ```nextflow
      tuple val(meta), env(trim_OT), env(trim_OB),                    emit: mbias_processed_str
                                         ^^^^^^^
  ```

- Error: `nextflow.config:251:23`: Invalid include source: '/home/runner/work/strict-syntax-health/strict-syntax-health/pipelines/methylseq/conf/aws/batch/nextflow.config'

  ```nextflow
      aws_batch       { includeConfig 'conf/aws/batch/nextflow.config' }
                        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  ```

## :warning: Warnings

- Warning: `conf/modules/bismark_genomepreparation.config:9:23`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
              saveAs: { it =~ /.*\.yml/ ? null : it },
                        ^^
  ```

- Warning: `conf/modules/bismark_genomepreparation.config:9:48`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
              saveAs: { it =~ /.*\.yml/ ? null : it },
                                                 ^^
  ```

- Warning: `conf/modules/bwameth_index.config:7:23`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
              saveAs: { it.equals('versions.yml') ? null : it.tokenize("/").last() },
                        ^^
  ```

- Warning: `conf/modules/bwameth_index.config:7:58`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
              saveAs: { it.equals('versions.yml') ? null : it.tokenize("/").last() },
                                                           ^^
  ```

- Warning: `modules/nf-core/bismark/align/main.nf:51:18`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          } catch (all) {
                   ^^^
  ```

- Warning: `modules/nf-core/bismark/align/main.nf:67:9`: Variable was declared but not used

  ```nextflow
      def args = task.ext.args ?: ''
          ^^^^
  ```

- Warning: `modules/nf-core/bismark/coverage2cytosine/main.nf:42:9`: Variable was declared but not used

  ```nextflow
      def args = task.ext.args ?: ''
          ^^^^
  ```

- Warning: `modules/nf-core/bismark/deduplicate/main.nf:23:9`: Variable was declared but not used

  ```nextflow
      def prefix  = task.ext.prefix ?: "${meta.id}"
          ^^^^^^
  ```

- Warning: `modules/nf-core/bismark/deduplicate/main.nf:38:9`: Variable was declared but not used

  ```nextflow
      def args = task.ext.args ?: ''
          ^^^^
  ```

- Warning: `modules/nf-core/bismark/genomepreparation/main.nf:34:9`: Variable was declared but not used

  ```nextflow
      def args = task.ext.args ?: ''
          ^^^^
  ```

- Warning: `modules/nf-core/bismark/methylationextractor/main.nf:54:9`: Variable was declared but not used

  ```nextflow
      def args = task.ext.args ?: ''
          ^^^^
  ```

- Warning: `modules/nf-core/bismark/report/main.nf:32:9`: Variable was declared but not used

  ```nextflow
      def args = task.ext.args ?: ''
          ^^^^
  ```

- Warning: `modules/nf-core/bismark/summary/main.nf:24:9`: Variable was declared but not used

  ```nextflow
      def args = task.ext.args ?: ''
          ^^^^
  ```

- Warning: `modules/nf-core/bismark/summary/main.nf:35:9`: Variable was declared but not used

  ```nextflow
      def args = task.ext.args ?: ''
          ^^^^
  ```

- Warning: `modules/nf-core/bwameth/index/main.nf:22:9`: Variable was declared but not used

  ```nextflow
      def args = task.ext.args ?: ''
          ^^^^
  ```

- Warning: `modules/nf-core/bwameth/index/main.nf:37:9`: Variable was declared but not used

  ```nextflow
      def args = task.ext.args ?: ''
          ^^^^
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

- Warning: `modules/nf-core/gunzip/main.nf:43:9`: Variable was declared but not used

  ```nextflow
      def args = task.ext.args ?: ''
          ^^^^
  ```

- Warning: `modules/nf-core/parabricks/fq2bammeth/main.nf:35:83`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
      def known_sites_command = known_sites ? known_sites.collect { "--knownSites ${it}" }.join(' ') : ""
                                                                                    ^^
  ```

- Warning: `modules/nf-core/rastair/call/main.nf:25:9`: Variable was declared but not used

  ```nextflow
      def args = task.ext.args ?: ''
          ^^^^
  ```

- Warning: `modules/nf-core/rastair/mbias/main.nf:23:9`: Variable was declared but not used

  ```nextflow
      def args = task.ext.args ?: ''
          ^^^^
  ```

- Warning: `modules/nf-core/trimgalore/main.nf:47:31`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          args_list.removeAll { it.toLowerCase().contains('_r2 ') }
                                ^^
  ```

- Warning: `subworkflows/local/targeted_sequencing/main.nf:28:19`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_versions = Channel.empty()
                    ^^^^^^^
  ```

- Warning: `subworkflows/local/targeted_sequencing/main.nf:29:25`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_picard_metrics = Channel.empty()
                          ^^^^^^^
  ```

- Warning: `subworkflows/local/targeted_sequencing/main.nf:70:72`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          ch_intervals = PICARD_BEDTOINTERVALLIST.out.intervallist.map { it[1] }
                                                                         ^^
  ```

- Warning: `subworkflows/local/utils_nfcore_methylseq_pipeline/main.nf:32:5`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
      monochrome_logs   // boolean: Do not use coloured log outputs
      ^^^^^^^^^^^^^^^
  ```

- Warning: `subworkflows/local/utils_nfcore_methylseq_pipeline/main.nf:35:5`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
      input             //  string: Path to input samplesheet
      ^^^^^
  ```

- Warning: `subworkflows/local/utils_nfcore_methylseq_pipeline/main.nf:109:37`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
              meta, fastq_1, fastq_2, genome ->
                                      ^^^^^^
  ```

- Warning: `subworkflows/local/utils_nfcore_methylseq_pipeline/main.nf:241:9`: Variable was declared but not used

  ```nextflow
      def citation_text = [
          ^^^^^^^^^^^^^
  ```

- Warning: `subworkflows/nf-core/bam_methyldackel/main.nf:13:40`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_methydackel_extract_bedgraph  = Channel.empty()
                                         ^^^^^^^
  ```

- Warning: `subworkflows/nf-core/bam_methyldackel/main.nf:14:40`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_methydackel_extract_methylkit = Channel.empty()
                                         ^^^^^^^
  ```

- Warning: `subworkflows/nf-core/bam_methyldackel/main.nf:15:40`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_methydackel_mbias             = Channel.empty()
                                         ^^^^^^^
  ```

- Warning: `subworkflows/nf-core/bam_methyldackel/main.nf:16:40`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_multiqc_files                 = Channel.empty()
                                         ^^^^^^^
  ```

- Warning: `subworkflows/nf-core/bam_methyldackel/main.nf:17:40`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_versions                      = Channel.empty()
                                         ^^^^^^^
  ```

- Warning: `subworkflows/nf-core/bam_methyldackel/main.nf:45:65`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
      ch_multiqc_files = ch_methydackel_extract_bedgraph.collect{ meta, bedgraph -> bedgraph  }
                                                                  ^^^^
  ```

- Warning: `subworkflows/nf-core/bam_methyldackel/main.nf:46:72`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
                          .mix(ch_methydackel_extract_methylkit.collect{ meta, methylkit -> methylkit })
                                                                         ^^^^
  ```

- Warning: `subworkflows/nf-core/bam_methyldackel/main.nf:47:60`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
                          .mix(ch_methydackel_mbias.collect{ meta, txt -> txt  })
                                                             ^^^^
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

- Warning: `subworkflows/nf-core/bam_taps_conversion/main.nf:21:24`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_rastair_mbias = Channel.empty()
                         ^^^^^^^
  ```

- Warning: `subworkflows/nf-core/bam_taps_conversion/main.nf:22:24`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_rastair_call  = Channel.empty()
                         ^^^^^^^
  ```

- Warning: `subworkflows/nf-core/bam_taps_conversion/main.nf:23:24`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_versions      = Channel.empty()
                         ^^^^^^^
  ```

- Warning: `subworkflows/nf-core/bam_taps_conversion/main.nf:47:53`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          ch_rastair_mbiasparser.map{ meta, nOT_clip, nOB_clip -> [ meta, nOT_clip ] },
                                                      ^^^^^^^^
  ```

- Warning: `subworkflows/nf-core/bam_taps_conversion/main.nf:48:43`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          ch_rastair_mbiasparser.map{ meta, nOT_clip, nOB_clip -> [ meta, nOB_clip ] },
                                            ^^^^^^^^
  ```

- Warning: `subworkflows/nf-core/fasta_index_bismark_bwameth/main.nf:20:24`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_fasta         = Channel.empty()
                         ^^^^^^^
  ```

- Warning: `subworkflows/nf-core/fasta_index_bismark_bwameth/main.nf:21:24`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_fasta_index   = Channel.empty()
                         ^^^^^^^
  ```

- Warning: `subworkflows/nf-core/fasta_index_bismark_bwameth/main.nf:22:24`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_bismark_index = Channel.empty()
                         ^^^^^^^
  ```

- Warning: `subworkflows/nf-core/fasta_index_bismark_bwameth/main.nf:23:24`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_bwameth_index = Channel.empty()
                         ^^^^^^^
  ```

- Warning: `subworkflows/nf-core/fasta_index_bismark_bwameth/main.nf:24:24`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_versions      = Channel.empty()
                         ^^^^^^^
  ```

- Warning: `subworkflows/nf-core/fasta_index_bismark_bwameth/main.nf:29:22`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
              gzipped: it[1].toString().endsWith('.gz')
                       ^^
  ```

- Warning: `subworkflows/nf-core/fasta_index_bismark_bwameth/main.nf:50:30`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
                      gzipped: it[1].toString().endsWith('.gz')
                               ^^
  ```

- Warning: `subworkflows/nf-core/fasta_index_bismark_bwameth/main.nf:79:30`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
                      gzipped: it[1].toString().endsWith('.gz')
                               ^^
  ```

- Warning: `subworkflows/nf-core/fasta_index_methylseq/main.nf:34:22`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
              gzipped: it[1].toString().endsWith('.gz')
                       ^^
  ```

- Warning: `subworkflows/nf-core/fasta_index_methylseq/main.nf:55:30`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
                      gzipped: it[1].toString().endsWith('.gz')
                               ^^
  ```

- Warning: `subworkflows/nf-core/fasta_index_methylseq/main.nf:93:30`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
                      gzipped: it[1].toString().endsWith('.gz')
                               ^^
  ```

- Warning: `subworkflows/nf-core/fasta_index_methylseq/main.nf:123:30`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
                      gzipped: it[1].toString().endsWith('.gz')
                               ^^
  ```

- Warning: `subworkflows/nf-core/fastq_align_bwa/main.nf:16:19`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_versions = Channel.empty()
                    ^^^^^^^
  ```

- Warning: `subworkflows/nf-core/utils_nfcore_pipeline/main.nf:101:98`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      return ch_versions.unique().map { version -> processVersionsFromYAML(version) }.unique().mix(Channel.of(workflowVersionToYAML()))
                                                                                                   ^^^^^^^
  ```

- Warning: `workflows/methylseq/main.nf:198:88`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          ch_versions    = ch_versions.mix(FASTQ_ALIGN_DEDUP_BWAMEM.out.versions.unique{ it.baseName })
                                                                                         ^^
  ```

- Warning: `workflows/methylseq/main.nf:368:89`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
              ch_multiqc_files = ch_multiqc_files.mix(QUALIMAP_BAMQC.out.results.collect{ it[1] }.ifEmpty([]))
                                                                                          ^^
  ```

- Warning: `workflows/methylseq/main.nf:371:86`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
              ch_multiqc_files = ch_multiqc_files.mix(PRESEQ_LCEXTRAP.out.log.collect{ it[1] }.ifEmpty([]))
                                                                                       ^^
  ```

- Warning: `workflows/methylseq/main.nf:375:81`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
              ch_multiqc_files = ch_multiqc_files.mix(TRIMGALORE.out.log.collect{ it[1] })
                                                                                  ^^
  ```

- Warning: `workflows/methylseq/main.nf:379:105`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
                  ch_multiqc_files = ch_multiqc_files.mix(TARGETED_SEQUENCING.out.picard_metrics.collect{ it[1] }.ifEmpty([]))
                                                                                                          ^^
  ```

- Warning: `workflows/methylseq/main.nf:383:77`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
              ch_multiqc_files = ch_multiqc_files.mix(FASTQC.out.zip.collect{ it[1] }.ifEmpty([]))
                                                                              ^^
  ```
