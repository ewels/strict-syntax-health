# Nextflow lint results

- Generated: 2026-01-16T10:24:50.067675652Z
- Nextflow version: 25.12.0-edge
- Summary: 34 errors, 162 warnings

## :x: Errors

- Error: `conf/modules.config:217:17`: Unexpected input: ':'

  ```nextflow
          withName: '.*:BAM_DEDUP_STATS_SAMTOOLS_UMITOOLS:UMITOOLS_DEDUP' {
                  ^
  ```

- Error: `modules/local/pints/visualizer/main.nf:47:23`: `chr_name` is not defined

  ```nextflow
      touch ${prefix}_${chr_name}_plus.bigwig
                        ^^^^^^^^
  ```

- Error: `modules/local/pints/visualizer/main.nf:48:23`: `chr_name` is not defined

  ```nextflow
      touch ${prefix}_${chr_name}_minus.bigwig
                        ^^^^^^^^
  ```

- Error: `modules/nf-core/bwa/index/main.nf:16:27`: `bwa` is not defined

  ```nextflow
      tuple val(meta), path(bwa) , emit: index
                            ^^^
  ```

- Error: `modules/nf-core/star/align/main.nf:43:20`: Unexpected input: ','

  ```nextflow
      def reads1 = [], reads2 = []
                     ^
  ```

- Error: `nextflow.config:318:31`: `manifest` is not defined

  ```nextflow
  \033[0;35m  nf-core/nascent ${manifest.version}\033[0m
                                ^^^^^^^^
  ```

- Error: `nextflow.config:321:26`: `manifest` is not defined

  ```nextflow
          afterText = """${manifest.doi ? "\n* The pipeline\n" : ""}${manifest.doi.tokenize(",").collect { "    https://doi.org/${it.trim().replace('https://doi.org/','')}"}.join("\n")}${manifest.doi ? "\n" : ""}
                           ^^^^^^^^
  ```

- Error: `nextflow.config:321:69`: `manifest` is not defined

  ```nextflow
          afterText = """${manifest.doi ? "\n* The pipeline\n" : ""}${manifest.doi.tokenize(",").collect { "    https://doi.org/${it.trim().replace('https://doi.org/','')}"}.join("\n")}${manifest.doi ? "\n" : ""}
                                                                      ^^^^^^^^
  ```

- Error: `nextflow.config:321:186`: `manifest` is not defined

  ```nextflow
          afterText = """${manifest.doi ? "\n* The pipeline\n" : ""}${manifest.doi.tokenize(",").collect { "    https://doi.org/${it.trim().replace('https://doi.org/','')}"}.join("\n")}${manifest.doi ? "\n" : ""}
                                                                                                                                                                                           ^^^^^^^^
  ```

- Error: `nextflow.config:330:22`: `validation` is not defined

  ```nextflow
          beforeText = validation.help.beforeText
                       ^^^^^^^^^^
  ```

- Error: `nextflow.config:331:21`: `validation` is not defined

  ```nextflow
          afterText = validation.help.afterText
                      ^^^^^^^^^^
  ```

- Error: `subworkflows/local/dreg_prep/main.nf:1:1`: Invalid include source: '/home/runner/work/strict-syntax-health/strict-syntax-health/pipelines/nascent/subworkflows/local/modules/nf-core/bedtools/bamtobed/main.nf'

  ```nextflow
  include { BEDTOOLS_BAMTOBED } from '../modules/nf-core/bedtools/bamtobed/main'
  ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  ```

- Error: `subworkflows/local/dreg_prep/main.nf:10:5`: `BEDTOOLS_BAMTOBED` is not defined

  ```nextflow
      BEDTOOLS_BAMTOBED(
      ^^^^^^^^^^^^^^^^^
  ```

- Error: `subworkflows/local/grohmm/main.nf:41:9`: Variables in a closure should be declared with `def`

  ```nextflow
          filename = "${meta.id}.${meta.single_end ? 'SE': 'PE' }.tuning.csv"
          ^^^^^^^^
  ```

- Error: `subworkflows/local/grohmm/main.nf:45:13`: Variables in a closure should be declared with `def`

  ```nextflow
              meta = [
              ^^^^
  ```

- Error: `subworkflows/local/prepare_genome.nf:145:30`: `UNTAR_DRAGMAP_INDEX` is not defined

  ```nextflow
                  ch_dragmap = UNTAR_DRAGMAP_INDEX(dragmap).untar
                               ^^^^^^^^^^^^^^^^^^^
  ```

- Error: `subworkflows/local/prepare_genome.nf:146:47`: `UNTAR_DRAGMAP_INDEX` is not defined

  ```nextflow
                  ch_versions = ch_versions.mix(UNTAR_DRAGMAP_INDEX.out.versions)
                                                ^^^^^^^^^^^^^^^^^^^
  ```

- Error: `subworkflows/local/prepare_genome.nf:161:36`: `UNTAR_BOWTIE2_INDEX` is not defined

  ```nextflow
                  ch_bowtie2_index = UNTAR_BOWTIE2_INDEX(bowtie2_index).untar
                                     ^^^^^^^^^^^^^^^^^^^
  ```

- Error: `subworkflows/local/prepare_genome.nf:162:47`: `UNTAR_BOWTIE2_INDEX` is not defined

  ```nextflow
                  ch_versions = ch_versions.mix(UNTAR_BOWTIE2_INDEX.out.versions)
                                                ^^^^^^^^^^^^^^^^^^^
  ```

- Error: `subworkflows/nf-core/fastq_align_star/main.nf:1:1`: Module could not be parsed: '/home/runner/work/strict-syntax-health/strict-syntax-health/pipelines/nascent/modules/nf-core/star/align/main.nf'

  ```nextflow
  include { STAR_ALIGN                                                       } from '../../../modules/nf-core/star/align/main'
  ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  ```

- Error: `subworkflows/nf-core/fastq_align_star/main.nf:25:5`: `STAR_ALIGN` is not defined

  ```nextflow
      STAR_ALIGN ( ch_reads, ch_index, ch_gtf, val_star_ignore_sjdbgtf, val_seq_platform, val_seq_center )
      ^^^^^^^^^^
  ```

- Error: `subworkflows/nf-core/fastq_align_star/main.nf:26:35`: `STAR_ALIGN` is not defined

  ```nextflow
      ch_versions = ch_versions.mix(STAR_ALIGN.out.versions.first())
                                    ^^^^^^^^^^
  ```

- Error: `subworkflows/nf-core/fastq_align_star/main.nf:31:38`: `STAR_ALIGN` is not defined

  ```nextflow
      BAM_SORT_STATS_SAMTOOLS_GENOME ( STAR_ALIGN.out.bam, ch_fasta )
                                       ^^^^^^^^^^
  ```

- Error: `subworkflows/nf-core/fastq_align_star/main.nf:41:45`: `STAR_ALIGN` is not defined

  ```nextflow
      BAM_SORT_STATS_SAMTOOLS_TRANSCRIPTOME ( STAR_ALIGN.out.bam_transcript, ch_transcripts_fasta )
                                              ^^^^^^^^^^
  ```

- Error: `subworkflows/nf-core/fastq_align_star/main.nf:46:27`: `STAR_ALIGN` is not defined

  ```nextflow
      orig_bam            = STAR_ALIGN.out.bam                                 // channel: [ val(meta), path(bam)            ]
                            ^^^^^^^^^^
  ```

- Error: `subworkflows/nf-core/fastq_align_star/main.nf:47:27`: `STAR_ALIGN` is not defined

  ```nextflow
      log_final           = STAR_ALIGN.out.log_final                           // channel: [ val(meta), path(log_final)      ]
                            ^^^^^^^^^^
  ```

- Error: `subworkflows/nf-core/fastq_align_star/main.nf:48:27`: `STAR_ALIGN` is not defined

  ```nextflow
      log_out             = STAR_ALIGN.out.log_out                             // channel: [ val(meta), path(log_out)        ]
                            ^^^^^^^^^^
  ```

- Error: `subworkflows/nf-core/fastq_align_star/main.nf:49:27`: `STAR_ALIGN` is not defined

  ```nextflow
      log_progress        = STAR_ALIGN.out.log_progress                        // channel: [ val(meta), path(log_progress)   ]
                            ^^^^^^^^^^
  ```

- Error: `subworkflows/nf-core/fastq_align_star/main.nf:50:27`: `STAR_ALIGN` is not defined

  ```nextflow
      bam_sorted          = STAR_ALIGN.out.bam_sorted                          // channel: [ val(meta), path(bam)            ]
                            ^^^^^^^^^^
  ```

- Error: `subworkflows/nf-core/fastq_align_star/main.nf:51:27`: `STAR_ALIGN` is not defined

  ```nextflow
      fastq               = STAR_ALIGN.out.fastq                               // channel: [ val(meta), path(fastq)          ]
                            ^^^^^^^^^^
  ```

- Error: `subworkflows/nf-core/fastq_align_star/main.nf:52:27`: `STAR_ALIGN` is not defined

  ```nextflow
      tab                 = STAR_ALIGN.out.tab                                 // channel: [ val(meta), path(tab)            ]
                            ^^^^^^^^^^
  ```

- Error: `subworkflows/nf-core/fastq_align_star/main.nf:53:27`: `STAR_ALIGN` is not defined

  ```nextflow
      orig_bam_transcript = STAR_ALIGN.out.bam_transcript                      // channel: [ val(meta), path(bam)            ]
                            ^^^^^^^^^^
  ```

- Error: `tests/config/test_data.config:6:5`: Unexpected input: 'includeConfig'

  ```nextflow
      includeConfig "https://raw.githubusercontent.com/nf-core/modules/master/tests/config/test_data.config"
      ^
  ```

- Error: `workflows/nascent.nf:278:13`: Variables in a closure should be declared with `def`

  ```nextflow
              fmeta = meta.findAll { it.key != 'read_group' }
              ^^^^^
  ```

## :warning: Warnings

- Warning: `modules/nf-core/bowtie2/align/main.nf:93:9`: Variable was declared but not used

  ```nextflow
      def reference = fasta && extension=="cram"  ? "--reference ${fasta}" : ""
          ^^^^^^^^^
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

- Warning: `modules/nf-core/bwamem2/mem/main.nf:59:9`: Variable was declared but not used

  ```nextflow
      def args = task.ext.args ?: ''
          ^^^^
  ```

- Warning: `modules/nf-core/bwamem2/mem/main.nf:62:9`: Variable was declared but not used

  ```nextflow
      def samtools_command = sort_bam ? 'sort' : 'view'
          ^^^^^^^^^^^^^^^^
  ```

- Warning: `modules/nf-core/bwamem2/mem/main.nf:66:9`: Variable was declared but not used

  ```nextflow
      def reference = fasta && extension=="cram"  ? "--reference ${fasta}" : ""
          ^^^^^^^^^
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

- Warning: `modules/nf-core/custom/getchromsizes/main.nf:23:9`: Variable was declared but not used

  ```nextflow
      def args = task.ext.args ?: ''
          ^^^^
  ```

- Warning: `modules/nf-core/deeptools/bamcoverage/main.nf:69:9`: Variable was declared but not used

  ```nextflow
      def extension = args.contains("--outFileFormat bedgraph") || args.contains("-of bedgraph") ? ".bedgraph" : ".bigWig"
          ^^^^^^^^^
  ```

- Warning: `modules/nf-core/dragmap/align/main.nf:58:9`: Variable was declared but not used

  ```nextflow
      def args = task.ext.args ?: ''
          ^^^^
  ```

- Warning: `modules/nf-core/dragmap/align/main.nf:61:9`: Variable was declared but not used

  ```nextflow
      def reads_command = meta.single_end ? "-1 $reads" : "-1 ${reads[0]} -2 ${reads[1]}"
          ^^^^^^^^^^^^^
  ```

- Warning: `modules/nf-core/dragmap/align/main.nf:62:9`: Variable was declared but not used

  ```nextflow
      def samtools_command = sort_bam ? 'sort' : 'view'
          ^^^^^^^^^^^^^^^^
  ```

- Warning: `modules/nf-core/dragmap/align/main.nf:66:9`: Variable was declared but not used

  ```nextflow
      def reference = fasta && extension=="cram"  ? "--reference ${fasta}" : ""
          ^^^^^^^^^
  ```

- Warning: `modules/nf-core/gffread/main.nf:26:103`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
      def extension   = args.contains("-T")       ? 'gtf' : ( ( ['-w', '-x', '-y' ].any { args.contains(it) } ) ? 'fasta' : 'gff3' )
                                                                                                        ^^
  ```

- Warning: `modules/nf-core/gffread/main.nf:30:61`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
      def args_sorted = args.replaceAll(/(.*)(-[wxy])(.*)/) { all, pre, param, post -> "$pre $post $param" }.trim()
                                                              ^^^
  ```

- Warning: `modules/nf-core/gffread/main.nf:49:103`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
      def extension   = args.contains("-T")       ? 'gtf' : ( ( ['-w', '-x', '-y' ].any { args.contains(it) } ) ? 'fasta' : 'gff3' )
                                                                                                        ^^
  ```

- Warning: `modules/nf-core/gunzip/main.nf:43:9`: Variable was declared but not used

  ```nextflow
      def args = task.ext.args ?: ''
          ^^^^
  ```

- Warning: `modules/nf-core/homer/pos2bed/main.nf:20:9`: Variable was declared but not used

  ```nextflow
      def args = task.ext.args ?: ''
          ^^^^
  ```

- Warning: `modules/nf-core/rseqc/readdistribution/main.nf:22:9`: Variable was declared but not used

  ```nextflow
      def args = task.ext.args ?: ''
          ^^^^
  ```

- Warning: `modules/nf-core/rseqc/tin/main.nf:24:9`: Variable was declared but not used

  ```nextflow
      def prefix = task.ext.prefix ?: "${meta.id}"
          ^^^^^^
  ```

- Warning: `modules/nf-core/rseqc/tin/main.nf:38:9`: Variable was declared but not used

  ```nextflow
      def prefix = task.ext.prefix ?: "${meta.id}"
          ^^^^^^
  ```

- Warning: `modules/nf-core/unzip/main.nf:38:9`: Variable was declared but not used

  ```nextflow
      def args = task.ext.args ?: ''
          ^^^^
  ```

- Warning: `nextflow.config:321:129`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          afterText = """${manifest.doi ? "\n* The pipeline\n" : ""}${manifest.doi.tokenize(",").collect { "    https://doi.org/${it.trim().replace('https://doi.org/','')}"}.join("\n")}${manifest.doi ? "\n" : ""}
                                                                                                                                  ^^
  ```

- Warning: `subworkflows/local/align_bwamem2/main.nf:16:19`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_versions = Channel.empty()
                    ^^^^^^^
  ```

- Warning: `subworkflows/local/align_dragmap/main.nf:16:19`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_versions = Channel.empty()
                    ^^^^^^^
  ```

- Warning: `subworkflows/local/coverage_graphs/main.nf:13:5`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
      sizes
      ^^^^^
  ```

- Warning: `subworkflows/local/coverage_graphs/main.nf:19:5`: Variable was declared but not used

  ```nextflow
      bam = bam_bai.map { [it[0], it[1]] }
      ^^^
  ```

- Warning: `subworkflows/local/coverage_graphs/main.nf:19:26`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
      bam = bam_bai.map { [it[0], it[1]] }
                           ^^
  ```

- Warning: `subworkflows/local/coverage_graphs/main.nf:19:33`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
      bam = bam_bai.map { [it[0], it[1]] }
                                  ^^
  ```

- Warning: `subworkflows/local/coverage_graphs/main.nf:21:19`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_versions = Channel.empty()
                    ^^^^^^^
  ```

- Warning: `subworkflows/local/dreg_prep/main.nf:6:5`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
      bai
      ^^^
  ```

- Warning: `subworkflows/local/dreg_prep/main.nf:7:5`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
      sizes
      ^^^^^
  ```

- Warning: `subworkflows/local/grohmm/main.nf:20:19`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_versions = Channel.empty()
                    ^^^^^^^
  ```

- Warning: `subworkflows/local/prepare_genome.nf:35:5`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
      hisat2_index
      ^^^^^^^^^^^^
  ```

- Warning: `subworkflows/local/prepare_genome.nf:39:19`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_versions = Channel.empty()
                    ^^^^^^^
  ```

- Warning: `subworkflows/local/prepare_genome.nf:45:60`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          ch_fasta = GUNZIP_FASTA([[:], fasta]).gunzip.map { it[1] }
                                                             ^^
  ```

- Warning: `subworkflows/local/prepare_genome.nf:49:20`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
          ch_fasta = Channel.value(file(fasta))
                     ^^^^^^^
  ```

- Warning: `subworkflows/local/prepare_genome.nf:58:62`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
                  ch_gtf = GUNZIP_GTF([[:], gtf]).gunzip.map { it[1] }
                                                               ^^
  ```

- Warning: `subworkflows/local/prepare_genome.nf:62:26`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
                  ch_gtf = Channel.value(file(gtf))
                           ^^^^^^^
  ```

- Warning: `subworkflows/local/prepare_genome.nf:73:58`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
              ch_gtf = GFFREAD(ch_gff, ch_fasta).gtf.map { it[1] }
                                                           ^^
  ```

- Warning: `subworkflows/local/prepare_genome.nf:83:73`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
              ch_gene_bed = GUNZIP_GENE_BED([[:], gene_bed]).gunzip.map { it[1] }
                                                                          ^^
  ```

- Warning: `subworkflows/local/prepare_genome.nf:98:47`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
      CUSTOM_GETCHROMSIZES(ch_fasta.map { [[:], it] })
                                                ^^
  ```

- Warning: `subworkflows/local/prepare_genome.nf:99:49`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
      ch_fai = CUSTOM_GETCHROMSIZES.out.fai.map { it[1] }
                                                  ^^
  ```

- Warning: `subworkflows/local/prepare_genome.nf:100:59`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
      ch_chrom_sizes = CUSTOM_GETCHROMSIZES.out.sizes.map { it[1] }
                                                            ^^
  ```

- Warning: `subworkflows/local/prepare_genome.nf:106:20`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_bwa_index = Channel.empty()
                     ^^^^^^^
  ```

- Warning: `subworkflows/local/prepare_genome.nf:107:18`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_dragmap = Channel.empty()
                   ^^^^^^^
  ```

- Warning: `subworkflows/local/prepare_genome.nf:108:24`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_bowtie2_index = Channel.empty()
                         ^^^^^^^
  ```

- Warning: `subworkflows/local/prepare_genome.nf:122:59`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
              ch_bwa_index = BWA_INDEX(ch_fasta.map { [[:], it] }).index
                                                            ^^
  ```

- Warning: `subworkflows/local/prepare_genome.nf:138:63`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
              ch_bwa_index = BWAMEM2_INDEX(ch_fasta.map { [[:], it] }).index
                                                                ^^
  ```

- Warning: `subworkflows/local/prepare_genome.nf:154:65`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
              ch_dragmap = DRAGMAP_HASHTABLE(ch_fasta.map { [[:], it] }).hashmap
                                                                  ^^
  ```

- Warning: `subworkflows/local/prepare_genome.nf:170:67`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
              ch_bowtie2_index = BOWTIE2_BUILD(ch_fasta.map { [[:], it] }).index
                                                                    ^^
  ```

- Warning: `subworkflows/local/quality_control.nf:14:26`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
      bam = bam_bai.map { [it[0], it[1]] }
                           ^^
  ```

- Warning: `subworkflows/local/quality_control.nf:14:33`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
      bam = bam_bai.map { [it[0], it[1]] }
                                  ^^
  ```

- Warning: `subworkflows/local/quality_control.nf:16:19`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_versions = Channel.empty()
                    ^^^^^^^
  ```

- Warning: `subworkflows/local/transcript_identification/main.nf:25:19`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_versions = Channel.empty()
                    ^^^^^^^
  ```

- Warning: `subworkflows/local/transcript_identification/main.nf:26:29`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_identification_bed = Channel.empty()
                              ^^^^^^^
  ```

- Warning: `subworkflows/local/transcript_identification/main.nf:28:22`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      grohmm_td_plot = Channel.empty()
                       ^^^^^^^
  ```

- Warning: `subworkflows/local/transcript_identification/main.nf:37:19`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      homer_peaks = Channel.empty()
                    ^^^^^^^
  ```

- Warning: `subworkflows/local/transcript_identification/main.nf:38:20`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      homer_tagdir = Channel.empty()
                     ^^^^^^^
  ```

- Warning: `subworkflows/local/transcript_identification/main.nf:54:21`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          .filter { !(it in skip_chr) }
                      ^^
  ```

- Warning: `subworkflows/local/transcript_identification/main.nf:96:25`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
          ch_filter_bed = Channel.from(params.filter_bed)
                          ^^^^^^^
  ```

- Warning: `subworkflows/local/transcript_identification/main.nf:97:113`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          BEDTOOLS_INTERSECT_FILTER(ch_identification_bed.combine(ch_filter_bed.first()), chrom_sizes.map { [[:], it] })
                                                                                                                  ^^
  ```

- Warning: `subworkflows/local/transcript_identification/main.nf:102:28`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
          ch_intersect_bed = Channel.from(params.intersect_bed)
                             ^^^^^^^
  ```

- Warning: `subworkflows/local/transcript_identification/main.nf:103:109`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          BEDTOOLS_INTERSECT(ch_identification_bed.combine(ch_intersect_bed.first()), chrom_sizes.map { [[:], it] })
                                                                                                              ^^
  ```

- Warning: `subworkflows/local/utils_nfcore_nascent_pipeline/main.nf:30:5`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
      monochrome_logs   // boolean: Do not use coloured log outputs
      ^^^^^^^^^^^^^^^
  ```

- Warning: `subworkflows/local/utils_nfcore_nascent_pipeline/main.nf:33:5`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
      input             //  string: Path to input samplesheet
      ^^^^^
  ```

- Warning: `subworkflows/local/utils_nfcore_nascent_pipeline/main.nf:37:19`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_versions = Channel.empty()
                    ^^^^^^^
  ```

- Warning: `subworkflows/local/utils_nfcore_nascent_pipeline/main.nf:74:5`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      Channel
      ^^^^^^^
  ```

- Warning: `subworkflows/nf-core/bam_dedup_stats_samtools_umitools/main.nf:16:19`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_versions = Channel.empty()
                    ^^^^^^^
  ```

- Warning: `subworkflows/nf-core/bam_rseqc/main.nf:22:26`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
      bam = bam_bai.map{ [ it[0], it[1] ] }
                           ^^
  ```

- Warning: `subworkflows/nf-core/bam_rseqc/main.nf:22:33`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
      bam = bam_bai.map{ [ it[0], it[1] ] }
                                  ^^
  ```

- Warning: `subworkflows/nf-core/bam_rseqc/main.nf:24:16`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      versions = Channel.empty()
                 ^^^^^^^
  ```

- Warning: `subworkflows/nf-core/bam_rseqc/main.nf:29:19`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      bamstat_txt = Channel.empty()
                    ^^^^^^^
  ```

- Warning: `subworkflows/nf-core/bam_rseqc/main.nf:40:30`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      innerdistance_all      = Channel.empty()
                               ^^^^^^^
  ```

- Warning: `subworkflows/nf-core/bam_rseqc/main.nf:41:30`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      innerdistance_distance = Channel.empty()
                               ^^^^^^^
  ```

- Warning: `subworkflows/nf-core/bam_rseqc/main.nf:42:30`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      innerdistance_freq     = Channel.empty()
                               ^^^^^^^
  ```

- Warning: `subworkflows/nf-core/bam_rseqc/main.nf:43:30`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      innerdistance_mean     = Channel.empty()
                               ^^^^^^^
  ```

- Warning: `subworkflows/nf-core/bam_rseqc/main.nf:44:30`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      innerdistance_pdf      = Channel.empty()
                               ^^^^^^^
  ```

- Warning: `subworkflows/nf-core/bam_rseqc/main.nf:45:30`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      innerdistance_rscript  = Channel.empty()
                               ^^^^^^^
  ```

- Warning: `subworkflows/nf-core/bam_rseqc/main.nf:61:27`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      inferexperiment_txt = Channel.empty()
                            ^^^^^^^
  ```

- Warning: `subworkflows/nf-core/bam_rseqc/main.nf:71:39`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      junctionannotation_all          = Channel.empty()
                                        ^^^^^^^
  ```

- Warning: `subworkflows/nf-core/bam_rseqc/main.nf:72:39`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      junctionannotation_bed          = Channel.empty()
                                        ^^^^^^^
  ```

- Warning: `subworkflows/nf-core/bam_rseqc/main.nf:73:39`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      junctionannotation_interact_bed = Channel.empty()
                                        ^^^^^^^
  ```

- Warning: `subworkflows/nf-core/bam_rseqc/main.nf:74:39`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      junctionannotation_xls          = Channel.empty()
                                        ^^^^^^^
  ```

- Warning: `subworkflows/nf-core/bam_rseqc/main.nf:75:39`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      junctionannotation_pdf          = Channel.empty()
                                        ^^^^^^^
  ```

- Warning: `subworkflows/nf-core/bam_rseqc/main.nf:76:39`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      junctionannotation_events_pdf   = Channel.empty()
                                        ^^^^^^^
  ```

- Warning: `subworkflows/nf-core/bam_rseqc/main.nf:77:39`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      junctionannotation_rscript      = Channel.empty()
                                        ^^^^^^^
  ```

- Warning: `subworkflows/nf-core/bam_rseqc/main.nf:78:39`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      junctionannotation_log          = Channel.empty()
                                        ^^^^^^^
  ```

- Warning: `subworkflows/nf-core/bam_rseqc/main.nf:96:34`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      junctionsaturation_all     = Channel.empty()
                                   ^^^^^^^
  ```

- Warning: `subworkflows/nf-core/bam_rseqc/main.nf:97:34`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      junctionsaturation_pdf     = Channel.empty()
                                   ^^^^^^^
  ```

- Warning: `subworkflows/nf-core/bam_rseqc/main.nf:98:34`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      junctionsaturation_rscript = Channel.empty()
                                   ^^^^^^^
  ```

- Warning: `subworkflows/nf-core/bam_rseqc/main.nf:111:28`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      readdistribution_txt = Channel.empty()
                             ^^^^^^^
  ```

- Warning: `subworkflows/nf-core/bam_rseqc/main.nf:122:31`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      readduplication_all     = Channel.empty()
                                ^^^^^^^
  ```

- Warning: `subworkflows/nf-core/bam_rseqc/main.nf:123:31`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      readduplication_seq_xls = Channel.empty()
                                ^^^^^^^
  ```

- Warning: `subworkflows/nf-core/bam_rseqc/main.nf:124:31`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      readduplication_pos_xls = Channel.empty()
                                ^^^^^^^
  ```

- Warning: `subworkflows/nf-core/bam_rseqc/main.nf:125:31`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      readduplication_pdf     = Channel.empty()
                                ^^^^^^^
  ```

- Warning: `subworkflows/nf-core/bam_rseqc/main.nf:126:31`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      readduplication_rscript = Channel.empty()
                                ^^^^^^^
  ```

- Warning: `subworkflows/nf-core/bam_rseqc/main.nf:141:15`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      tin_txt = Channel.empty()
                ^^^^^^^
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

- Warning: `subworkflows/nf-core/fastq_align_bowtie2/main.nf:18:19`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_versions = Channel.empty()
                    ^^^^^^^
  ```

- Warning: `subworkflows/nf-core/fastq_align_bwa/main.nf:16:19`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_versions = Channel.empty()
                    ^^^^^^^
  ```

- Warning: `subworkflows/nf-core/fastq_align_hisat2/main.nf:14:19`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_versions = Channel.empty()
                    ^^^^^^^
  ```

- Warning: `subworkflows/nf-core/fastq_align_star/main.nf:20:19`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_versions = Channel.empty()
                    ^^^^^^^
  ```

- Warning: `subworkflows/nf-core/homer_groseq/main.nf:20:19`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_versions = Channel.empty()
                    ^^^^^^^
  ```

- Warning: `subworkflows/nf-core/homer_groseq/main.nf:22:18`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_uniqmap = Channel.empty()
                   ^^^^^^^
  ```

- Warning: `subworkflows/nf-core/homer_groseq/main.nf:28:67`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          ch_uniqmap = UNZIP([[:], uniqmap]).unzipped_archive.map { it[1] }
                                                                    ^^
  ```

- Warning: `subworkflows/nf-core/utils_nfcore_pipeline/main.nf:101:98`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      return ch_versions.unique().map { version -> processVersionsFromYAML(version) }.unique().mix(Channel.of(workflowVersionToYAML()))
                                                                                                   ^^^^^^^
  ```

- Warning: `workflows/nascent.nf:63:19`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_versions = Channel.empty()
                    ^^^^^^^
  ```

- Warning: `workflows/nascent.nf:64:24`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_multiqc_files = Channel.empty()
                         ^^^^^^^
  ```

- Warning: `workflows/nascent.nf:95:70`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
      ch_multiqc_files = ch_multiqc_files.mix(FASTQC.out.zip.collect { it[1] })
                                                                       ^^
  ```

- Warning: `workflows/nascent.nf:98:16`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_reads = Channel.empty()
                 ^^^^^^^
  ```

- Warning: `workflows/nascent.nf:111:21`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_genome_bam = Channel.empty()
                      ^^^^^^^
  ```

- Warning: `workflows/nascent.nf:112:21`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_genome_bai = Channel.empty()
                      ^^^^^^^
  ```

- Warning: `workflows/nascent.nf:113:25`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_samtools_stats = Channel.empty()
                          ^^^^^^^
  ```

- Warning: `workflows/nascent.nf:114:28`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_samtools_flagstat = Channel.empty()
                             ^^^^^^^
  ```

- Warning: `workflows/nascent.nf:115:28`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_samtools_idxstats = Channel.empty()
                             ^^^^^^^
  ```

- Warning: `workflows/nascent.nf:116:5`: Variable was declared but not used

  ```nextflow
      ch_star_multiqc = Channel.empty()
      ^^^^^^^^^^^^^^^
  ```

- Warning: `workflows/nascent.nf:116:23`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_star_multiqc = Channel.empty()
                        ^^^^^^^
  ```

- Warning: `workflows/nascent.nf:117:5`: Variable was declared but not used

  ```nextflow
      ch_aligner_pca_multiqc = Channel.empty()
      ^^^^^^^^^^^^^^^^^^^^^^
  ```

- Warning: `workflows/nascent.nf:117:30`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_aligner_pca_multiqc = Channel.empty()
                               ^^^^^^^
  ```

- Warning: `workflows/nascent.nf:118:5`: Variable was declared but not used

  ```nextflow
      ch_aligner_clustering_multiqc = Channel.empty()
      ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  ```

- Warning: `workflows/nascent.nf:118:37`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_aligner_clustering_multiqc = Channel.empty()
                                      ^^^^^^^
  ```

- Warning: `workflows/nascent.nf:119:26`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_bowtie2_multiqc = Channel.empty()
                           ^^^^^^^
  ```

- Warning: `workflows/nascent.nf:204:9`: Variable was declared but not used

  ```nextflow
          ch_HISAT2_multiqc = FASTQ_ALIGN_HISAT2.out.summary
          ^^^^^^^^^^^^^^^^^
  ```

- Warning: `workflows/nascent.nf:211:52`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
                  PREPARE_GENOME.out.gtf.map { [[:], it] }
                                                     ^^
  ```

- Warning: `workflows/nascent.nf:226:48`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
              PREPARE_GENOME.out.gtf.map { [[:], it] },
                                                 ^^
  ```

- Warning: `workflows/nascent.nf:231:13`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
              Channel.of([[:], []])
              ^^^^^^^
  ```

- Warning: `workflows/nascent.nf:235:9`: Variable was declared but not used

  ```nextflow
          ch_transcriptome_bam = FASTQ_ALIGN_STAR.out.bam_transcript
          ^^^^^^^^^^^^^^^^^^^^
  ```

- Warning: `workflows/nascent.nf:237:86`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          ch_multiqc_files = ch_multiqc_files.mix(FASTQ_ALIGN_STAR.out.stats.collect { it[1] })
                                                                                       ^^
  ```

- Warning: `workflows/nascent.nf:238:89`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          ch_multiqc_files = ch_multiqc_files.mix(FASTQ_ALIGN_STAR.out.flagstat.collect { it[1] })
                                                                                          ^^
  ```

- Warning: `workflows/nascent.nf:239:89`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          ch_multiqc_files = ch_multiqc_files.mix(FASTQ_ALIGN_STAR.out.idxstats.collect { it[1] })
                                                                                          ^^
  ```

- Warning: `workflows/nascent.nf:240:71`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          ch_multiqc_files = ch_multiqc_files.mix(ch_star_log.collect { it[1] })
                                                                        ^^
  ```

- Warning: `workflows/nascent.nf:278:36`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
              fmeta = meta.findAll { it.key != 'read_group' }
                                     ^^
  ```

- Warning: `workflows/nascent.nf:289:36`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
              fmeta = meta.findAll { it.key != 'read_group' }
                                     ^^
  ```

- Warning: `workflows/nascent.nf:318:25`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
              ).saf.map { it[1] }
                          ^^
  ```

- Warning: `workflows/nascent.nf:344:25`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_multiqc_config = Channel.fromPath(
                          ^^^^^^^
  ```

- Warning: `workflows/nascent.nf:349:11`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
          ? Channel.fromPath(params.multiqc_config, checkIfExists: true)
            ^^^^^^^
  ```

- Warning: `workflows/nascent.nf:350:11`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
          : Channel.empty()
            ^^^^^^^
  ```

- Warning: `workflows/nascent.nf:352:11`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
          ? Channel.fromPath(params.multiqc_logo, checkIfExists: true)
            ^^^^^^^
  ```

- Warning: `workflows/nascent.nf:353:11`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
          : Channel.empty()
            ^^^^^^^
  ```

- Warning: `workflows/nascent.nf:359:27`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_workflow_summary = Channel.value(paramsSummaryMultiqc(summary_params))
                            ^^^^^^^
  ```

- Warning: `workflows/nascent.nf:366:30`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_methods_description = Channel.value(
                               ^^^^^^^
  ```

- Warning: `workflows/nascent.nf:378:70`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
      ch_multiqc_files = ch_multiqc_files.mix(FASTQC.out.zip.collect { it[1] }.ifEmpty([]))
                                                                       ^^
  ```

- Warning: `workflows/nascent.nf:379:74`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
      ch_multiqc_files = ch_multiqc_files.mix(ch_bowtie2_multiqc.collect { it[1] }.ifEmpty([]))
                                                                           ^^
  ```

- Warning: `workflows/nascent.nf:380:73`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
      ch_multiqc_files = ch_multiqc_files.mix(ch_samtools_stats.collect { it[1] }.ifEmpty([]))
                                                                          ^^
  ```

- Warning: `workflows/nascent.nf:381:76`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
      ch_multiqc_files = ch_multiqc_files.mix(ch_samtools_flagstat.collect { it[1] }.ifEmpty([]))
                                                                             ^^
  ```

- Warning: `workflows/nascent.nf:382:76`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
      ch_multiqc_files = ch_multiqc_files.mix(ch_samtools_idxstats.collect { it[1] }.ifEmpty([]))
                                                                             ^^
  ```

- Warning: `workflows/nascent.nf:383:89`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
      ch_multiqc_files = ch_multiqc_files.mix(QUALITY_CONTROL.out.preseq_ccurve.collect { it[1] }.ifEmpty([]))
                                                                                          ^^
  ```

- Warning: `workflows/nascent.nf:384:91`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
      ch_multiqc_files = ch_multiqc_files.mix(QUALITY_CONTROL.out.preseq_lcextrap.collect { it[1] }.ifEmpty([]))
                                                                                            ^^
  ```

- Warning: `workflows/nascent.nf:385:96`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
      ch_multiqc_files = ch_multiqc_files.mix(QUALITY_CONTROL.out.readdistribution_txt.collect { it[1] }.ifEmpty([]))
                                                                                                 ^^
  ```

- Warning: `workflows/nascent.nf:386:99`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
      ch_multiqc_files = ch_multiqc_files.mix(QUALITY_CONTROL.out.readduplication_seq_xls.collect { it[1] }.ifEmpty([]))
                                                                                                    ^^
  ```

- Warning: `workflows/nascent.nf:387:99`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
      ch_multiqc_files = ch_multiqc_files.mix(QUALITY_CONTROL.out.readduplication_pos_xls.collect { it[1] }.ifEmpty([]))
                                                                                                    ^^
  ```

- Warning: `workflows/nascent.nf:388:95`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
      ch_multiqc_files = ch_multiqc_files.mix(QUALITY_CONTROL.out.inferexperiment_txt.collect { it[1] }.ifEmpty([]))
                                                                                                ^^
  ```

- Warning: `workflows/nascent.nf:389:73`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
      ch_multiqc_files = ch_multiqc_files.mix(ch_grohmm_multiqc.collect { it[1] }.ifEmpty([]))
                                                                          ^^
  ```

- Warning: `workflows/nascent.nf:390:72`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
      ch_multiqc_files = ch_multiqc_files.mix(ch_homer_multiqc.collect { it[1] }.ifEmpty([]))
                                                                         ^^
  ```

- Warning: `workflows/nascent.nf:391:99`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
      ch_multiqc_files = ch_multiqc_files.mix(SUBREAD_FEATURECOUNTS_PREDICTED.out.summary.collect { it[1] }.ifEmpty([]))
                                                                                                    ^^
  ```

- Warning: `workflows/nascent.nf:392:94`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
      ch_multiqc_files = ch_multiqc_files.mix(SUBREAD_FEATURECOUNTS_GENE.out.summary.collect { it[1] }.ifEmpty([]))
                                                                                               ^^
  ```
