# Nextflow lint results

- Generated: 2026-01-16T06:35:03.171746471Z
- Nextflow version: 25.12.0-edge
- Summary: 81 warnings

## :warning: Warnings

- Warning: `modules/local/bed2bedgraphs/modkit_bedgraphs/main.nf:58:9`: Variable was declared but not used

  ```nextflow
      def args   = task.ext.args ?: ''
          ^^^^
  ```

- Warning: `modules/local/bed2bedgraphs/pbcpgtools_bedgraphs/main.nf:44:9`: Variable was declared but not used

  ```nextflow
      def args   = task.ext.args ?: ''
          ^^^^
  ```

- Warning: `modules/local/dorado/aligner/main.nf:36:9`: Variable was declared but not used

  ```nextflow
      def args   = task.ext.args ?: ''
          ^^^^
  ```

- Warning: `modules/local/modkit/dmrpair/main.nf:27:45`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
      def a_params    = bed_hp1.collect { "-a $it" }.join(' ')
                                              ^^
  ```

- Warning: `modules/local/modkit/dmrpair/main.nf:28:45`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
      def b_params    = bed_hp2.collect { "-b $it" }.join(' ')
                                              ^^
  ```

- Warning: `modules/local/pb_cpg_tools/main.nf:43:9`: Variable was declared but not used

  ```nextflow
      def args   = task.ext.args ?: ''
          ^^^^
  ```

- Warning: `modules/local/rename_fastq/main.nf:22:9`: Variable was declared but not used

  ```nextflow
      def args   = task.ext.args ?: ''
          ^^^^
  ```

- Warning: `modules/local/samtools/merge/main.nf:38:9`: Variable was declared but not used

  ```nextflow
      def args   = task.ext.args ?: ''
          ^^^^
  ```

- Warning: `modules/local/samtools/reset/main.nf:36:9`: Variable was declared but not used

  ```nextflow
      def args   = task.ext.args ?: ''
          ^^^^
  ```

- Warning: `modules/local/samtools/split_strands/main.nf:42:9`: Variable was declared but not used

  ```nextflow
      def args   = task.ext.args ?: ''
          ^^^^
  ```

- Warning: `modules/nf-core/clair3/main.nf:72:9`: Variable was declared but not used

  ```nextflow
      def args = task.ext.args ?: ''
          ^^^^
  ```

- Warning: `modules/nf-core/gawk/main.nf:26:54`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
      suffix    = task.ext.suffix ?: "${input.collect{ it.getExtension()}.get(0)}" // use the first extension of the input files
                                                       ^^
  ```

- Warning: `modules/nf-core/gawk/main.nf:29:37`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
      lst_gz     = input.findResults{ it.getExtension().endsWith("gz") ? it.toString() : null }
                                      ^^
  ```

- Warning: `modules/nf-core/gawk/main.nf:29:72`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
      lst_gz     = input.findResults{ it.getExtension().endsWith("gz") ? it.toString() : null }
                                                                         ^^
  ```

- Warning: `modules/nf-core/gawk/main.nf:31:34`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
      input_cmd  = input.collect { it.toString() - ~/\.gz$/ }.join(" ")
                                   ^^
  ```

- Warning: `modules/nf-core/gawk/main.nf:34:49`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
      cleanup    = lst_gz ? "rm ${lst_gz.collect{ it - ~/\.gz$/ }.join(" ")}" : ""
                                                  ^^
  ```

- Warning: `modules/nf-core/gawk/main.nf:37:16`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          assert it.name != "${prefix}.${suffix}" : "Input and output names are the same, set prefix in module configuration to disambiguate!"
                 ^^
  ```

- Warning: `modules/nf-core/gunzip/main.nf:43:9`: Variable was declared but not used

  ```nextflow
      def args = task.ext.args ?: ''
          ^^^^
  ```

- Warning: `modules/nf-core/minimap2/align/main.nf:67:9`: Variable was declared but not used

  ```nextflow
      def target = reference ?: (bam_input ? error("BAM input requires reference") : reads)
          ^^^^^^
  ```

- Warning: `modules/nf-core/modkit/pileup/main.nf:58:9`: Variable was declared but not used

  ```nextflow
      def args   = task.ext.args ?: ''
          ^^^^
  ```

- Warning: `modules/nf-core/pbmm2/align/main.nf:41:9`: Variable was declared but not used

  ```nextflow
      def args = task.ext.args ?: ''
          ^^^^
  ```

- Warning: `modules/nf-core/pigz/compress/main.nf:35:9`: Variable was declared but not used

  ```nextflow
      def args = task.ext.args ?: ''
          ^^^^
  ```

- Warning: `subworkflows/local/ONT_main.nf:35:20`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ont_versions = Channel.empty()
                     ^^^^^^^
  ```

- Warning: `subworkflows/local/ONT_main.nf:36:20`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      map_stat     = Channel.empty()
                     ^^^^^^^
  ```

- Warning: `subworkflows/local/ONT_main.nf:41:19`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          .filter { it[1].toString().endsWith('.pod5') || file(it[1]).isDirectory() }
                    ^^
  ```

- Warning: `subworkflows/local/ONT_main.nf:41:62`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          .filter { it[1].toString().endsWith('.pod5') || file(it[1]).isDirectory() }
                                                               ^^
  ```

- Warning: `subworkflows/local/ONT_main.nf:52:34`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          .mix ( ch_input.filter { it[1].toString().endsWith('.bam') } )
                                   ^^
  ```

- Warning: `subworkflows/local/ONT_main.nf:60:66`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
      map_stat = map_stat.mix(FASTQ_UNZIP.out.fastqc_log.collect { it[1] }.ifEmpty([]))
                                                                   ^^
  ```

- Warning: `subworkflows/local/Pacbio_main.nf:37:23`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      pacbio_versions = Channel.empty()
                        ^^^^^^^
  ```

- Warning: `subworkflows/local/Pacbio_main.nf:38:23`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      map_stat        = Channel.empty()
                        ^^^^^^^
  ```

- Warning: `subworkflows/local/Pacbio_main.nf:40:13`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      input = Channel.empty()
              ^^^^^^^
  ```

- Warning: `subworkflows/local/Pacbio_main.nf:86:66`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
      map_stat = map_stat.mix(FASTQ_UNZIP.out.fastqc_log.collect { it[1] }.ifEmpty([]))
                                                                   ^^
  ```

- Warning: `subworkflows/local/ont_align/main.nf:25:16`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      versions = Channel.empty()
                 ^^^^^^^
  ```

- Warning: `subworkflows/local/ont_fiberseq/main.nf:23:16`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      versions = Channel.empty()
                 ^^^^^^^
  ```

- Warning: `subworkflows/local/ont_trim_repair/main.nf:29:16`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      versions = Channel.empty()
                 ^^^^^^^
  ```

- Warning: `subworkflows/local/pacbio_align_minimap2/main.nf:26:16`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      versions = Channel.empty()
                 ^^^^^^^
  ```

- Warning: `subworkflows/local/pacbio_align_pbmm2/main.nf:28:16`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      versions = Channel.empty()
                 ^^^^^^^
  ```

- Warning: `subworkflows/local/pacbio_fiberseq/main.nf:22:16`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      versions = Channel.empty()
                 ^^^^^^^
  ```

- Warning: `subworkflows/local/pacbio_split_strand_pbcpg_pileup/main.nf:26:16`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      versions = Channel.empty()
                 ^^^^^^^
  ```

- Warning: `subworkflows/local/shared_bed2bedgraph/main.nf:25:36`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
      modkit_input = in_bed.filter { it[0].method == 'ont' || (it[0].method == 'pacbio' && params.pileup_method == 'modkit') }
                                     ^^
  ```

- Warning: `subworkflows/local/shared_bed2bedgraph/main.nf:25:62`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
      modkit_input = in_bed.filter { it[0].method == 'ont' || (it[0].method == 'pacbio' && params.pileup_method == 'modkit') }
                                                               ^^
  ```

- Warning: `subworkflows/local/shared_bed2bedgraph/main.nf:26:35`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
      pbcpg_input = in_bed.filter { it[0].method == 'pacbio' && params.pileup_method == 'pbcpgtools' }
                                    ^^
  ```

- Warning: `subworkflows/local/shared_dss_haplotype_level/main.nf:25:16`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      versions = Channel.empty()
                 ^^^^^^^
  ```

- Warning: `subworkflows/local/shared_dss_population_scale/main.nf:26:16`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      versions = Channel.empty()
                 ^^^^^^^
  ```

- Warning: `subworkflows/local/shared_dss_population_scale/main.nf:49:46`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
              def metas = sampleList.collect { it[0] }
                                               ^^
  ```

- Warning: `subworkflows/local/shared_dss_population_scale/main.nf:50:46`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
              def beds  = sampleList.collect { it[1] }
                                               ^^
  ```

- Warning: `subworkflows/local/shared_dss_population_scale/main.nf:58:46`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
              def metas = sampleList.collect { it[0] }
                                               ^^
  ```

- Warning: `subworkflows/local/shared_dss_population_scale/main.nf:59:46`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
              def beds  = sampleList.collect { it[1] }
                                               ^^
  ```

- Warning: `subworkflows/local/shared_dss_population_scale/preprocess/main.nf:23:16`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      versions = Channel.empty()
                 ^^^^^^^
  ```

- Warning: `subworkflows/local/shared_fastqc_unzip/main.nf:22:16`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      versions = Channel.empty()
                 ^^^^^^^
  ```

- Warning: `subworkflows/local/shared_fastqc_unzip/main.nf:23:18`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      fastqc_log = Channel.empty()
                   ^^^^^^^
  ```

- Warning: `subworkflows/local/shared_fastqc_unzip/main.nf:31:58`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
      fastqc_log = fastqc_log.mix(FASTQC.out.zip.collect { it[1] }.ifEmpty([]))
                                                           ^^
  ```

- Warning: `subworkflows/local/shared_fastqc_unzip/main.nf:35:19`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          .filter { it[1] =~ /fa\.gz$|fna\.gz$|fasta\.gz$/ }
                    ^^
  ```

- Warning: `subworkflows/local/shared_fastqc_unzip/main.nf:40:21`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          .filter { !(it[2] =~ /fa\.gz$|fna\.gz$|fasta\.gz$/) }
                      ^^
  ```

- Warning: `subworkflows/local/shared_gunzip_awk/main.nf:22:16`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      versions = Channel.empty()
                 ^^^^^^^
  ```

- Warning: `subworkflows/local/shared_gunzip_awk/main.nf:26:19`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          .filter { it[1] =~ /\.vcf\.gz$/ }
                    ^^
  ```

- Warning: `subworkflows/local/shared_modkit_dmr_haplotype_level/main.nf:25:16`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      versions = Channel.empty()
                 ^^^^^^^
  ```

- Warning: `subworkflows/local/shared_modkit_dmr_population_scale/main.nf:26:16`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      versions = Channel.empty()
                 ^^^^^^^
  ```

- Warning: `subworkflows/local/shared_modkit_dmr_population_scale/main.nf:50:46`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
              def metas = sampleList.collect { it[0] }
                                               ^^
  ```

- Warning: `subworkflows/local/shared_modkit_dmr_population_scale/main.nf:51:46`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
              def beds  = sampleList.collect { it[1] }
                                               ^^
  ```

- Warning: `subworkflows/local/shared_modkit_dmr_population_scale/main.nf:52:46`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
              def tbis  = sampleList.collect { it[2] }
                                               ^^
  ```

- Warning: `subworkflows/local/shared_modkit_dmr_population_scale/main.nf:60:46`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
              def metas = sampleList.collect { it[0] }
                                               ^^
  ```

- Warning: `subworkflows/local/shared_modkit_dmr_population_scale/main.nf:61:46`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
              def beds  = sampleList.collect { it[1] }
                                               ^^
  ```

- Warning: `subworkflows/local/shared_modkit_dmr_population_scale/main.nf:62:46`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
              def tbis  = sampleList.collect { it[2] }
                                               ^^
  ```

- Warning: `subworkflows/local/shared_modkit_dmr_population_scale/preprocess/main.nf:23:16`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      versions = Channel.empty()
                 ^^^^^^^
  ```

- Warning: `subworkflows/local/shared_modkit_pileup/main.nf:24:16`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      versions = Channel.empty()
                 ^^^^^^^
  ```

- Warning: `subworkflows/local/shared_snvcall_clair3/main.nf:23:16`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      versions = Channel.empty()
                 ^^^^^^^
  ```

- Warning: `subworkflows/local/shared_whatshap/main.nf:25:16`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      versions = Channel.empty()
                 ^^^^^^^
  ```

- Warning: `subworkflows/local/utils_nfcore_methylong_pipeline/main.nf:31:5`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
      monochrome_logs   // boolean: Do not use coloured log outputs
      ^^^^^^^^^^^^^^^
  ```

- Warning: `subworkflows/local/utils_nfcore_methylong_pipeline/main.nf:34:5`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
      input             //  string: Path to input samplesheet
      ^^^^^
  ```

- Warning: `subworkflows/local/utils_nfcore_methylong_pipeline/main.nf:98:5`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      Channel
      ^^^^^^^
  ```

- Warning: `subworkflows/local/utils_nfcore_methylong_pipeline/main.nf:134:9`: Variable was declared but not used

  ```nextflow
      def multiqc_reports = multiqc_report.toList()
          ^^^^^^^^^^^^^^^
  ```

- Warning: `workflows/methylong.nf:30:19`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_versions = Channel.empty()
                    ^^^^^^^
  ```

- Warning: `workflows/methylong.nf:31:24`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_multiqc_files = Channel.empty()
                         ^^^^^^^
  ```

- Warning: `workflows/methylong.nf:38:19`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          .filter { it[0].method == "pacbio" }
                    ^^
  ```

- Warning: `workflows/methylong.nf:42:19`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          .filter { it[0].method == "ont" }
                    ^^
  ```

- Warning: `workflows/methylong.nf:51:75`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
      ch_multiqc_files = ch_multiqc_files.mix(PACBIO.out.map_stat.collect { it[1] }.ifEmpty([]))
                                                                            ^^
  ```

- Warning: `workflows/methylong.nf:56:72`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
      ch_multiqc_files = ch_multiqc_files.mix(ONT.out.map_stat.collect { it[1] }.ifEmpty([]))
                                                                         ^^
  ```

- Warning: `workflows/methylong.nf:116:19`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          .filter { it != null &&!(it instanceof List && it.contains(null)) }
                    ^^
  ```

- Warning: `workflows/methylong.nf:116:34`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          .filter { it != null &&!(it instanceof List && it.contains(null)) }
                                   ^^
  ```

- Warning: `workflows/methylong.nf:116:56`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          .filter { it != null &&!(it instanceof List && it.contains(null)) }
                                                         ^^
  ```
