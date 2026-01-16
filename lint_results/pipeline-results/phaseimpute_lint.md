# Nextflow lint results

- Generated: 2026-01-16T10:25:52.052750613Z
- Nextflow version: 25.12.0-edge
- Summary: 1 error, 128 warnings

## :x: Errors

- Error: `modules/nf-core/samtools/merge/main.nf:51:9`: `index` is already declared

  ```nextflow
      def index = args.contains("--write-index") ? "touch ${prefix}.${index_type}" : ""
          ^^^^^
  ```

## :warning: Warnings

- Warning: `main.nf:55:31`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_input_impute         = Channel.empty()
                                ^^^^^^^
  ```

- Warning: `main.nf:56:31`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_input_simulate       = Channel.empty()
                                ^^^^^^^
  ```

- Warning: `main.nf:57:31`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_input_validate       = Channel.empty()
                                ^^^^^^^
  ```

- Warning: `main.nf:60:32`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
      lst_chr = ch_regions.map { it[0].chr }
                                 ^^
  ```

- Warning: `modules/nf-core/bcftools/concat/main.nf:32:27`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
      def input = vcfs.sort{it.toString()}.join(" ")
                            ^^
  ```

- Warning: `modules/nf-core/bcftools/convert/main.nf:87:39`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          hap = args_split.findIndexOf{ it == '--haplegendsample'}
                                        ^^
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

- Warning: `modules/nf-core/bcftools/merge/main.nf:27:58`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
      def input = (vcfs.collect().size() > 1) ? vcfs.sort{ it.name } : vcfs
                                                           ^^
  ```

- Warning: `modules/nf-core/bcftools/norm/main.nf:56:65`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          if (['--write-index=tbi', '-W=tbi'].any { args.contains(it) }  && extension == 'vcf.gz') {
                                                                  ^^
  ```

- Warning: `modules/nf-core/bcftools/norm/main.nf:58:126`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          } else if (['--write-index=tbi', '-W=tbi', '--write-index=csi', '-W=csi', '--write-index', '-W'].any { args.contains(it) }) {
                                                                                                                               ^^
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

- Warning: `modules/nf-core/glimpse/chunk/main.nf:40:9`: Variable was declared but not used

  ```nextflow
      def args    = task.ext.args   ?: ""
          ^^^^
  ```

- Warning: `modules/nf-core/glimpse/ligate/main.nf:42:9`: Variable was declared but not used

  ```nextflow
      def args    = task.ext.args   ?: ""
          ^^^^
  ```

- Warning: `modules/nf-core/glimpse/phase/main.nf:47:9`: Variable was declared but not used

  ```nextflow
      def args   = task.ext.args   ?: ''
          ^^^^
  ```

- Warning: `modules/nf-core/glimpse2/phase/main.nf:45:9`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          it.toString().endsWithAny("cram", "bam")          ? "bam" :
          ^^
  ```

- Warning: `modules/nf-core/glimpse2/phase/main.nf:46:9`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          it.toString().endsWithAny("vcf", "bcf", "vcf.gz") ? "gl"  :
          ^^
  ```

- Warning: `modules/nf-core/glimpse2/phase/main.nf:47:9`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          it.getExtension()
          ^^
  ```

- Warning: `modules/nf-core/gunzip/main.nf:43:9`: Variable was declared but not used

  ```nextflow
      def args = task.ext.args ?: ''
          ^^^^
  ```

- Warning: `modules/nf-core/minimac4/compressref/main.nf:37:9`: Variable was declared but not used

  ```nextflow
      def args   = task.ext.args   ?: ''
          ^^^^
  ```

- Warning: `modules/nf-core/quilt/quilt/main.nf:28:56`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
      def extensions                  =   bams.collect { it.extension }
                                                         ^^
  ```

- Warning: `subworkflows/local/bam_chr_rename_samtools/main.nf:10:19`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_versions = Channel.empty()
                    ^^^^^^^
  ```

- Warning: `subworkflows/local/bam_downsample_samtools/main.nf:13:24`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_versions      = Channel.empty()
                         ^^^^^^^
  ```

- Warning: `subworkflows/local/bam_extract_region_samtools/main.nf:13:19`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_versions = Channel.empty()
                    ^^^^^^^
  ```

- Warning: `subworkflows/local/bam_impute_quilt/main.nf:14:19`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_versions = Channel.empty()
                    ^^^^^^^
  ```

- Warning: `subworkflows/local/bam_impute_quilt/main.nf:49:18`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
          .combine(Channel.of([[], [], [], []]))
                   ^^^^^^^
  ```

- Warning: `subworkflows/local/utils_nfcore_phaseimpute_pipeline/main.nf:175:26`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
          ch_input_truth = Channel.of([[], [], []])
                           ^^^^^^^
  ```

- Warning: `subworkflows/local/vcf_chr_rename_bcftools/main.nf:9:19`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_versions = Channel.empty()
                    ^^^^^^^
  ```

- Warning: `subworkflows/local/vcf_chunk_glimpse/main.nf:13:19`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_versions = Channel.empty()
                    ^^^^^^^
  ```

- Warning: `subworkflows/local/vcf_concordance_glimpse2/main.nf:18:24`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_versions      = Channel.empty()
                         ^^^^^^^
  ```

- Warning: `subworkflows/local/vcf_concordance_glimpse2/main.nf:19:24`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_multiqc_files = Channel.empty()
                         ^^^^^^^
  ```

- Warning: `subworkflows/local/vcf_concordance_glimpse2/main.nf:28:33`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          .combine(ch_region.map{[it[1]]}.collect().toList())
                                  ^^
  ```

- Warning: `subworkflows/local/vcf_concordance_glimpse2/main.nf:70:55`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
                  def all_files = sorted_list.collect { it[1] }
                                                        ^^
  ```

- Warning: `subworkflows/local/vcf_impute_glimpse1/main.nf:15:19`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_versions = Channel.empty()
                    ^^^^^^^
  ```

- Warning: `subworkflows/local/vcf_impute_glimpse1/main.nf:17:20`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      samples_file = Channel.of([[]]).collect()
                     ^^^^^^^
  ```

- Warning: `subworkflows/local/vcf_impute_glimpse1/main.nf:18:20`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      gmap_file    = Channel.of([[]]).collect()
                     ^^^^^^^
  ```

- Warning: `subworkflows/local/vcf_normalize_bcftools/main.nf:13:19`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_versions = Channel.empty()
                    ^^^^^^^
  ```

- Warning: `subworkflows/local/vcf_phase_shapeit5/main.nf:19:19`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_versions = Channel.empty()
                    ^^^^^^^
  ```

- Warning: `subworkflows/local/vcf_phase_shapeit5/main.nf:75:30`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
                      .collect{it.first()},
                               ^^
  ```

- Warning: `subworkflows/local/vcf_sites_extract_bcftools/main.nf:13:19`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_versions = Channel.empty()
                    ^^^^^^^
  ```

- Warning: `subworkflows/local/vcf_split_bcftools/main.nf:9:19`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_versions = Channel.empty()
                    ^^^^^^^
  ```

- Warning: `workflows/chrcheck/function.nf:10:53`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
                  chr.readLines()*.split(' ').collect{it[0]},
                                                      ^^
  ```

- Warning: `workflows/chrcheck/function.nf:37:47`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
              chr_target.each{ new_chr += "chr${it}" }
                                                ^^
  ```

- Warning: `workflows/chrcheck/function.nf:38:37`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
              diff.each{ to_rename += it.replace('chr', '') }
                                      ^^
  ```

- Warning: `workflows/chrcheck/function.nf:40:41`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
              chr_target.each{ new_chr += it.replace('chr', '') }
                                          ^^
  ```

- Warning: `workflows/chrcheck/function.nf:41:43`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
              diff.each{ to_rename += "chr${it}" }
                                            ^^
  ```

- Warning: `workflows/chrcheck/main.nf:19:23`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
          ch_versions = Channel.empty()
                        ^^^^^^^
  ```

- Warning: `workflows/chrcheck/main.nf:22:18`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
              bam: it[1] =~ 'bam|cram'
                   ^^
  ```

- Warning: `workflows/chrcheck/main.nf:23:18`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
              vcf: it[1] =~ 'vcf|bcf'
                   ^^
  ```

- Warning: `workflows/chrcheck/main.nf:24:20`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
              other: it[1].size() > 0
                     ^^
  ```

- Warning: `workflows/chrcheck/main.nf:29:28`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
              error "File: ${it[1]} is not a VCF, BCFT or BAM, CRAM file."
                             ^^
  ```

- Warning: `workflows/chrcheck/main.nf:33:24`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
          ch_vcf_split = Channel.empty()
                         ^^^^^^^
  ```

- Warning: `workflows/chrcheck/main.nf:39:24`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
          ch_bam_split = Channel.empty()
                         ^^^^^^^
  ```

- Warning: `workflows/chrcheck/main.nf:46:30`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
              ch_bam_renamed = Channel.empty()
                               ^^^^^^^
  ```

- Warning: `workflows/chrcheck/main.nf:54:30`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
              ch_vcf_renamed = Channel.empty()
                               ^^^^^^^
  ```

- Warning: `workflows/chrcheck/main.nf:61:33`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
                  def chr_names = it[3].size() > params.max_chr_names ? it[3][0..params.max_chr_names - 1] + ['...'] : it[3]
                                  ^^
  ```

- Warning: `workflows/chrcheck/main.nf:61:71`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
                  def chr_names = it[3].size() > params.max_chr_names ? it[3][0..params.max_chr_names - 1] + ['...'] : it[3]
                                                                        ^^
  ```

- Warning: `workflows/chrcheck/main.nf:61:118`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
                  def chr_names = it[3].size() > params.max_chr_names ? it[3][0..params.max_chr_names - 1] + ['...'] : it[3]
                                                                                                                       ^^
  ```

- Warning: `workflows/chrcheck/main.nf:62:61`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
                  error "Contig names: ${chr_names} in VCF: ${it[1]} are not present in reference genome with same writing. Please set `rename_chr` to `true` to rename the contigs."
                                                              ^^
  ```

- Warning: `workflows/chrcheck/main.nf:65:33`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
                  def chr_names = it[3].size() > params.max_chr_names ? it[3][0..params.max_chr_names - 1] + ['...'] : it[3]
                                  ^^
  ```

- Warning: `workflows/chrcheck/main.nf:65:71`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
                  def chr_names = it[3].size() > params.max_chr_names ? it[3][0..params.max_chr_names - 1] + ['...'] : it[3]
                                                                        ^^
  ```

- Warning: `workflows/chrcheck/main.nf:65:118`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
                  def chr_names = it[3].size() > params.max_chr_names ? it[3][0..params.max_chr_names - 1] + ['...'] : it[3]
                                                                                                                       ^^
  ```

- Warning: `workflows/chrcheck/main.nf:66:61`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
                  error "Contig names: ${chr_names} in BAM: ${it[1]} are not present in reference genome with same writing. Please set `rename_chr` to `true` to rename the contigs."
                                                              ^^
  ```

- Warning: `workflows/chrcheck/main.nf:68:30`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
              ch_vcf_renamed = Channel.empty()
                               ^^^^^^^
  ```

- Warning: `workflows/chrcheck/main.nf:69:30`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
              ch_bam_renamed = Channel.empty()
                               ^^^^^^^
  ```

- Warning: `workflows/phaseimpute/main.nf:111:24`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_multiqc_files = Channel.empty()
                         ^^^^^^^
  ```

- Warning: `workflows/phaseimpute/main.nf:119:23`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
              .map{ if (it != "bam" & it != "cram") {
                        ^^
  ```

- Warning: `workflows/phaseimpute/main.nf:119:37`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
              .map{ if (it != "bam" & it != "cram") {
                                      ^^
  ```

- Warning: `workflows/phaseimpute/main.nf:120:113`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
                  error "All input files must be in the same format, either BAM or CRAM, to perform simulation: ${it}"
                                                                                                                  ^^
  ```

- Warning: `workflows/phaseimpute/main.nf:157:80`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          ch_multiqc_files = ch_multiqc_files.mix(FILTER_CHR_INP.out.output.map{ it[1] })
                                                                                 ^^
  ```

- Warning: `workflows/phaseimpute/main.nf:175:84`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
              ch_multiqc_files = ch_multiqc_files.mix(FILTER_CHR_DWN.out.output.map{ it[1] })
                                                                                     ^^
  ```

- Warning: `workflows/phaseimpute/main.nf:213:60`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
                  VCF_NORMALIZE_BCFTOOLS.out.vcf_tbi.combine(Channel.of([[]])),
                                                             ^^^^^^^
  ```

- Warning: `workflows/phaseimpute/main.nf:270:22`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
                  bam: it[1] =~ 'bam|cram'
                       ^^
  ```

- Warning: `workflows/phaseimpute/main.nf:271:22`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
                  vcf: it[1] =~ '(vcf|bcf)(.gz)*'
                       ^^
  ```

- Warning: `workflows/phaseimpute/main.nf:284:73`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
                  .collect{ nb_batch += 1; [[id: "all", batch: nb_batch], it] } }
                                                                          ^^
  ```

- Warning: `workflows/phaseimpute/main.nf:285:43`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
              .map { list -> [list.collect{ it[0] }, list.collect{ it[1] }] }
                                            ^^
  ```

- Warning: `workflows/phaseimpute/main.nf:285:66`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
              .map { list -> [list.collect{ it[0] }, list.collect{ it[1] }] }
                                                                   ^^
  ```

- Warning: `workflows/phaseimpute/main.nf:288:53`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
                  metaI + [metas: filestuples.collect{it[0].findAll{it.key != "batch"}}],
                                                      ^^
  ```

- Warning: `workflows/phaseimpute/main.nf:288:67`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
                  metaI + [metas: filestuples.collect{it[0].findAll{it.key != "batch"}}],
                                                                    ^^
  ```

- Warning: `workflows/phaseimpute/main.nf:289:37`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
                  filestuples.collect{it[1]}, filestuples.collect{it[2]}
                                      ^^
  ```

- Warning: `workflows/phaseimpute/main.nf:289:65`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
                  filestuples.collect{it[1]}, filestuples.collect{it[2]}
                                                                  ^^
  ```

- Warning: `workflows/phaseimpute/main.nf:294:50`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
                  meta, file, meta.metas.collect { it.id }
                                                   ^^
  ```

- Warning: `workflows/phaseimpute/main.nf:302:61`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          if (params.panel && !params.steps.split(',').find { it in ["all", "panelprep"] }) {
                                                              ^^
  ```

- Warning: `workflows/phaseimpute/main.nf:430:46`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
                  ch_input_bams_withlist.map{ [it[0], it[1], it[2], it[4], it[5]] },
                                               ^^
  ```

- Warning: `workflows/phaseimpute/main.nf:430:53`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
                  ch_input_bams_withlist.map{ [it[0], it[1], it[2], it[4], it[5]] },
                                                      ^^
  ```

- Warning: `workflows/phaseimpute/main.nf:430:60`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
                  ch_input_bams_withlist.map{ [it[0], it[1], it[2], it[4], it[5]] },
                                                             ^^
  ```

- Warning: `workflows/phaseimpute/main.nf:430:67`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
                  ch_input_bams_withlist.map{ [it[0], it[1], it[2], it[4], it[5]] },
                                                                    ^^
  ```

- Warning: `workflows/phaseimpute/main.nf:430:74`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
                  ch_input_bams_withlist.map{ [it[0], it[1], it[2], it[4], it[5]] },
                                                                           ^^
  ```

- Warning: `workflows/phaseimpute/main.nf:479:59`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
                  .map { meta_vcf, vcf, index, meta_region, region ->
                                                            ^^^^^^
  ```

- Warning: `workflows/phaseimpute/main.nf:521:28`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
              ch_fasta.map{ [it[0], it[1]] })
                             ^^
  ```

- Warning: `workflows/phaseimpute/main.nf:521:35`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
              ch_fasta.map{ [it[0], it[1]] })
                                    ^^
  ```

- Warning: `workflows/phaseimpute/main.nf:523:86`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          ch_multiqc_files = ch_multiqc_files.mix(BCFTOOLS_STATS_TOOLS.out.stats.map{ [it[1]] })
                                                                                       ^^
  ```

- Warning: `workflows/phaseimpute/main.nf:552:28`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
              ch_fasta.map{ [it[0], it[1]] })
                             ^^
  ```

- Warning: `workflows/phaseimpute/main.nf:552:35`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
              ch_fasta.map{ [it[0], it[1]] })
                                    ^^
  ```

- Warning: `workflows/phaseimpute/main.nf:554:86`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          ch_multiqc_files = ch_multiqc_files.mix(BCFTOOLS_STATS_PANEL.out.stats.map{ [it[1]] })
                                                                                       ^^
  ```

- Warning: `workflows/phaseimpute/main.nf:556:24`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
          ch_truth_vcf = Channel.empty()
                         ^^^^^^^
  ```

- Warning: `workflows/phaseimpute/main.nf:560:21`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
              .map { [it[0], it[1], it[2], getFileExtension(it[1])] }
                      ^^
  ```

- Warning: `workflows/phaseimpute/main.nf:560:28`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
              .map { [it[0], it[1], it[2], getFileExtension(it[1])] }
                             ^^
  ```

- Warning: `workflows/phaseimpute/main.nf:560:35`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
              .map { [it[0], it[1], it[2], getFileExtension(it[1])] }
                                    ^^
  ```

- Warning: `workflows/phaseimpute/main.nf:560:59`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
              .map { [it[0], it[1], it[2], getFileExtension(it[1])] }
                                                            ^^
  ```

- Warning: `workflows/phaseimpute/main.nf:562:22`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
                  bam: it[3] =~ 'bam|cram'
                       ^^
  ```

- Warning: `workflows/phaseimpute/main.nf:563:22`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
                  vcf: it[3] =~ '(vcf|bcf)(.gz)*'
                       ^^
  ```

- Warning: `workflows/phaseimpute/main.nf:571:33`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
              ch_truth.bam.map { [it[0], it[1], it[2]] },
                                  ^^
  ```

- Warning: `workflows/phaseimpute/main.nf:571:40`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
              ch_truth.bam.map { [it[0], it[1], it[2]] },
                                         ^^
  ```

- Warning: `workflows/phaseimpute/main.nf:571:47`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
              ch_truth.bam.map { [it[0], it[1], it[2]] },
                                                ^^
  ```

- Warning: `workflows/phaseimpute/main.nf:583:21`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
              .map { [it[0], it[1], it[2]] }
                      ^^
  ```

- Warning: `workflows/phaseimpute/main.nf:583:28`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
              .map { [it[0], it[1], it[2]] }
                             ^^
  ```

- Warning: `workflows/phaseimpute/main.nf:583:35`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
              .map { [it[0], it[1], it[2]] }
                                    ^^
  ```

- Warning: `workflows/phaseimpute/main.nf:606:28`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
              ch_fasta.map{ [it[0], it[1]] }
                             ^^
  ```

- Warning: `workflows/phaseimpute/main.nf:606:35`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
              ch_fasta.map{ [it[0], it[1]] }
                                    ^^
  ```

- Warning: `workflows/phaseimpute/main.nf:609:86`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          ch_multiqc_files = ch_multiqc_files.mix(BCFTOOLS_STATS_TRUTH.out.stats.map{ [it[1]] })
                                                                                       ^^
  ```

- Warning: `workflows/phaseimpute/main.nf:626:26`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      def topic_versions = Channel.topic("versions")
                           ^^^^^^^
  ```

- Warning: `workflows/phaseimpute/main.nf:655:45`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_multiqc_config                     = Channel.fromPath("$projectDir/assets/multiqc_config.yml", checkIfExists: true)
                                              ^^^^^^^
  ```

- Warning: `workflows/phaseimpute/main.nf:656:69`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_multiqc_custom_config              = params.multiqc_config ? Channel.fromPath(params.multiqc_config, checkIfExists: true) : Channel.empty()
                                                                      ^^^^^^^
  ```

- Warning: `workflows/phaseimpute/main.nf:656:132`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_multiqc_custom_config              = params.multiqc_config ? Channel.fromPath(params.multiqc_config, checkIfExists: true) : Channel.empty()
                                                                                                                                     ^^^^^^^
  ```

- Warning: `workflows/phaseimpute/main.nf:657:67`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_multiqc_logo                       = params.multiqc_logo ? Channel.fromPath(params.multiqc_logo, checkIfExists: true) : Channel.empty()
                                                                    ^^^^^^^
  ```

- Warning: `workflows/phaseimpute/main.nf:657:128`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_multiqc_logo                       = params.multiqc_logo ? Channel.fromPath(params.multiqc_logo, checkIfExists: true) : Channel.empty()
                                                                                                                                 ^^^^^^^
  ```

- Warning: `workflows/phaseimpute/main.nf:659:45`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_workflow_summary                   = Channel.value(paramsSummaryMultiqc(summary_params))
                                              ^^^^^^^
  ```

- Warning: `workflows/phaseimpute/main.nf:662:45`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_methods_description                = Channel.value(methodsDescriptionText(ch_multiqc_custom_methods_description))
                                              ^^^^^^^
  ```

- Warning: `workflows/phaseimpute/main.nf:665:76`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_multiqc_replace_names              = params.multiqc_replace_names ? Channel.fromPath(params.multiqc_replace_names, checkIfExists: true) : Channel.empty()
                                                                             ^^^^^^^
  ```

- Warning: `workflows/phaseimpute/main.nf:665:146`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_multiqc_replace_names              = params.multiqc_replace_names ? Channel.fromPath(params.multiqc_replace_names, checkIfExists: true) : Channel.empty()
                                                                                                                                                   ^^^^^^^
  ```

- Warning: `workflows/phaseimpute/main.nf:666:75`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_multiqc_sample_names               = params.multiqc_sample_names ? Channel.fromPath(params.multiqc_sample_names, checkIfExists: true) : Channel.empty()
                                                                            ^^^^^^^
  ```

- Warning: `workflows/phaseimpute/main.nf:666:144`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_multiqc_sample_names               = params.multiqc_sample_names ? Channel.fromPath(params.multiqc_sample_names, checkIfExists: true) : Channel.empty()
                                                                                                                                                 ^^^^^^^
  ```
