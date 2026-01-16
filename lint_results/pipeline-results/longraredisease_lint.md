# Nextflow lint results

- Generated: 2026-01-16T06:33:49.674216761Z
- Nextflow version: 25.12.0-edge
- Summary: 6 errors, 121 warnings

## :x: Errors

- Error: `nextflow.config:373:39`: `manifest` is not defined

  ```nextflow
  \033[0;35m  nf-core/longraredisease ${manifest.version}\033[0m
                                        ^^^^^^^^
  ```

- Error: `nextflow.config:376:26`: `manifest` is not defined

  ```nextflow
          afterText = """${manifest.doi ? "\n* The pipeline\n" : ""}${manifest.doi.tokenize(",").collect { "    https://doi.org/${it.trim().replace('https://doi.org/','')}"}.join("\n")}${manifest.doi ? "\n" : ""}
                           ^^^^^^^^
  ```

- Error: `nextflow.config:376:69`: `manifest` is not defined

  ```nextflow
          afterText = """${manifest.doi ? "\n* The pipeline\n" : ""}${manifest.doi.tokenize(",").collect { "    https://doi.org/${it.trim().replace('https://doi.org/','')}"}.join("\n")}${manifest.doi ? "\n" : ""}
                                                                      ^^^^^^^^
  ```

- Error: `nextflow.config:376:186`: `manifest` is not defined

  ```nextflow
          afterText = """${manifest.doi ? "\n* The pipeline\n" : ""}${manifest.doi.tokenize(",").collect { "    https://doi.org/${it.trim().replace('https://doi.org/','')}"}.join("\n")}${manifest.doi ? "\n" : ""}
                                                                                                                                                                                           ^^^^^^^^
  ```

- Error: `nextflow.config:385:22`: `validation` is not defined

  ```nextflow
          beforeText = validation.help.beforeText
                       ^^^^^^^^^^
  ```

- Error: `nextflow.config:386:21`: `validation` is not defined

  ```nextflow
          afterText = validation.help.afterText
                      ^^^^^^^^^^
  ```

## :warning: Warnings

- Warning: `modules/local/SvAnna/main.nf:28:71`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          hpo_args = hpo_terms.split(';').collect { "--phenotype-term ${it}" }.join(' ')
                                                                        ^^
  ```

- Warning: `modules/local/generate_sv_plots/main.nf:43:9`: Variable was declared but not used

  ```nextflow
      def args = task.ext.args ?: ''
          ^^^^
  ```

- Warning: `modules/local/normalize_cutesv/main.nf:19:9`: Variable was declared but not used

  ```nextflow
      def args = task.ext.args ?: ''
          ^^^^
  ```

- Warning: `modules/local/normalize_merged_sv/main.nf:19:9`: Variable was declared but not used

  ```nextflow
      def args = task.ext.args ?: ''
          ^^^^
  ```

- Warning: `modules/local/round_dp/main.nf:19:9`: Variable was declared but not used

  ```nextflow
      def args = task.ext.args ?: ''
          ^^^^
  ```

- Warning: `modules/local/spectre/main.nf:29:9`: Variable was declared but not used

  ```nextflow
      def prefix = task.ext.prefix ?: "${meta.id}"
          ^^^^^^
  ```

- Warning: `modules/local/straglr/main.nf:39:9`: Variable was declared but not used

  ```nextflow
      def args = task.ext.args ?: ''
          ^^^^
  ```

- Warning: `modules/nf-core/bcftools/concat/main.nf:32:27`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
      def input = vcfs.sort{it.toString()}.join(" ")
                            ^^
  ```

- Warning: `modules/nf-core/bcftools/isec/main.nf:35:9`: Variable was declared but not used

  ```nextflow
      def args = task.ext.args   ?: ''
          ^^^^
  ```

- Warning: `modules/nf-core/bcftools/merge/main.nf:28:58`: Implicit closure parameter is deprecated, declare an explicit parameter instead

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

- Warning: `modules/nf-core/clair3/main.nf:72:9`: Variable was declared but not used

  ```nextflow
      def args = task.ext.args ?: ''
          ^^^^
  ```

- Warning: `modules/nf-core/deepvariant/vcfstatsreport/main.nf:25:9`: Variable was declared but not used

  ```nextflow
      def args = task.ext.args ?: ''
          ^^^^
  ```

- Warning: `modules/nf-core/gunzip/main.nf:43:9`: Variable was declared but not used

  ```nextflow
      def args = task.ext.args ?: ''
          ^^^^
  ```

- Warning: `modules/nf-core/hifiasm/main.nf:36:75`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
      def long_reads_sorted = long_reads instanceof List ? long_reads.sort{ it.name } : long_reads
                                                                            ^^
  ```

- Warning: `modules/nf-core/hifiasm/main.nf:37:69`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
      def ul_reads_sorted = ul_reads instanceof List ? ul_reads.sort{ it.name } : ul_reads
                                                                      ^^
  ```

- Warning: `modules/nf-core/jasminesv/main.nf:37:39`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
      def unzip_inputs = vcfs.collect { it.name.endsWith(".vcf.gz") ? "    bgzip -d --threads ${task.cpus} ${args4} ${it}" : "" }.join("\n")
                                        ^^
  ```

- Warning: `modules/nf-core/jasminesv/main.nf:37:117`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
      def unzip_inputs = vcfs.collect { it.name.endsWith(".vcf.gz") ? "    bgzip -d --threads ${task.cpus} ${args4} ${it}" : "" }.join("\n")
                                                                                                                      ^^
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

- Warning: `modules/nf-core/yak/count/main.nf:39:9`: Variable was declared but not used

  ```nextflow
      def args = task.ext.args ?: ''
          ^^^^
  ```

- Warning: `nextflow.config:376:129`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          afterText = """${manifest.doi ? "\n* The pipeline\n" : ""}${manifest.doi.tokenize(",").collect { "    https://doi.org/${it.trim().replace('https://doi.org/','')}"}.join("\n")}${manifest.doi ? "\n" : ""}
                                                                                                                                  ^^
  ```

- Warning: `subworkflows/local/align.nf:15:19`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_versions = Channel.empty()
                    ^^^^^^^
  ```

- Warning: `subworkflows/local/align.nf:40:40`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
              .map { meta_sample, reads, meta_ref, index ->
                                         ^^^^^^^^
  ```

- Warning: `subworkflows/local/align.nf:52:54`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
              ch_align_input.map { meta_sample, reads, meta_index, index ->
                                                       ^^^^^^^^^^
  ```

- Warning: `subworkflows/local/align.nf:52:66`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
              ch_align_input.map { meta_sample, reads, meta_index, index ->
                                                                   ^^^^^
  ```

- Warning: `subworkflows/local/align.nf:55:34`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
              ch_align_input.map { meta_sample, reads, meta_index, index ->
                                   ^^^^^^^^^^^
  ```

- Warning: `subworkflows/local/align.nf:55:47`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
              ch_align_input.map { meta_sample, reads, meta_index, index ->
                                                ^^^^^
  ```

- Warning: `subworkflows/local/assemble_reads.nf:15:25`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      software_versions = Channel.empty()
                          ^^^^^^^
  ```

- Warning: `subworkflows/local/bam2fastq.nf:15:19`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_versions = Channel.empty()
                    ^^^^^^^
  ```

- Warning: `subworkflows/local/call_cnv_spectre.nf:22:19`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_versions = Channel.empty()
                    ^^^^^^^
  ```

- Warning: `subworkflows/local/call_snv.nf:19:19`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_versions = Channel.empty()
                    ^^^^^^^
  ```

- Warning: `subworkflows/local/call_snv.nf:45:13`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
              Channel.value([]),   // empty channel for samples
              ^^^^^^^
  ```

- Warning: `subworkflows/local/call_snv.nf:46:13`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
              Channel.value([]),   // empty channel for regions
              ^^^^^^^
  ```

- Warning: `subworkflows/local/call_snv.nf:47:13`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
              Channel.value([])    // empty channel for filters
              ^^^^^^^
  ```

- Warning: `subworkflows/local/call_snv.nf:77:17`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
                  Channel.value([]),
                  ^^^^^^^
  ```

- Warning: `subworkflows/local/call_snv.nf:78:17`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
                  Channel.value([]),
                  ^^^^^^^
  ```

- Warning: `subworkflows/local/call_snv.nf:79:17`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
                  Channel.value([])
                  ^^^^^^^
  ```

- Warning: `subworkflows/local/call_snv.nf:93:36`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
          ch_final_deepvariant_vcf = Channel.empty()
                                     ^^^^^^^
  ```

- Warning: `subworkflows/local/call_snv.nf:94:36`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
          ch_final_deepvariant_tbi = Channel.empty()
                                     ^^^^^^^
  ```

- Warning: `subworkflows/local/call_str.nf:14:19`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_versions = Channel.empty()
                    ^^^^^^^
  ```

- Warning: `subworkflows/local/call_sv.nf:23:19`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_versions = Channel.empty()
                    ^^^^^^^
  ```

- Warning: `subworkflows/local/filter_sv.nf:20:15`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
  ch_versions = Channel.empty()
                ^^^^^^^
  ```

- Warning: `subworkflows/local/filter_sv.nf:21:31`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
  target_bed_ch = target_bed ?: Channel.value([])
                                ^^^^^^^
  ```

- Warning: `subworkflows/local/filter_sv.nf:26:5`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      Channel.value([]),
      ^^^^^^^
  ```

- Warning: `subworkflows/local/filter_sv.nf:28:5`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      Channel.value([])
      ^^^^^^^
  ```

- Warning: `subworkflows/local/filter_sv.nf:48:20`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
              .map { clean_meta, vcf, tbi, original_meta, summary, bed ->
                     ^^^^^^^^^^
  ```

- Warning: `subworkflows/local/filter_sv.nf:53:54`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
              ch_sv_mosdepth_bed.map { meta, vcf, tbi, summary, bed -> tuple(meta, vcf, tbi) },
                                                       ^^^^^^^
  ```

- Warning: `subworkflows/local/filter_sv.nf:53:63`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
              ch_sv_mosdepth_bed.map { meta, vcf, tbi, summary, bed -> tuple(meta, vcf, tbi) },
                                                                ^^^
  ```

- Warning: `subworkflows/local/filter_sv.nf:54:44`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
              ch_sv_mosdepth_bed.map { meta, vcf, tbi, summary, bed -> tuple(meta, summary) },
                                             ^^^
  ```

- Warning: `subworkflows/local/filter_sv.nf:54:49`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
              ch_sv_mosdepth_bed.map { meta, vcf, tbi, summary, bed -> tuple(meta, summary) },
                                                  ^^^
  ```

- Warning: `subworkflows/local/filter_sv.nf:54:63`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
              ch_sv_mosdepth_bed.map { meta, vcf, tbi, summary, bed -> tuple(meta, summary) },
                                                                ^^^
  ```

- Warning: `subworkflows/local/filter_sv.nf:55:44`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
              ch_sv_mosdepth_bed.map { meta, vcf, tbi, summary, bed -> tuple(meta, bed) },
                                             ^^^
  ```

- Warning: `subworkflows/local/filter_sv.nf:55:49`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
              ch_sv_mosdepth_bed.map { meta, vcf, tbi, summary, bed -> tuple(meta, bed) },
                                                  ^^^
  ```

- Warning: `subworkflows/local/filter_sv.nf:55:54`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
              ch_sv_mosdepth_bed.map { meta, vcf, tbi, summary, bed -> tuple(meta, bed) },
                                                       ^^^^^^^
  ```

- Warning: `subworkflows/local/longphase.nf:12:19`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_versions = Channel.empty()
                    ^^^^^^^
  ```

- Warning: `subworkflows/local/merge_sv.nf:16:19`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_versions = Channel.empty()
                    ^^^^^^^
  ```

- Warning: `subworkflows/local/merge_sv.nf:23:24`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
          ch_chr_norm ?: Channel.value([])
                         ^^^^^^^
  ```

- Warning: `subworkflows/local/merge_sv.nf:32:75`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
      jasmine_vcf = NORMALIZE_JASMINE.out.vcf_with_samples.map { meta, vcf, samples -> [meta, vcf] }
                                                                            ^^^^^^^
  ```

- Warning: `subworkflows/local/merge_sv.nf:39:9`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
          Channel.value([]),  // regions - use Channel.value([]) instead of []
          ^^^^^^^
  ```

- Warning: `subworkflows/local/merge_sv.nf:40:9`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
          Channel.value([]),  // targets
          ^^^^^^^
  ```

- Warning: `subworkflows/local/merge_sv.nf:41:9`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
          Channel.value([])   // samples
          ^^^^^^^
  ```

- Warning: `subworkflows/local/merge_sv.nf:49:68`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
                  NORMALIZE_JASMINE.out.vcf_with_samples.map { meta, vcf, samples -> [meta, samples] },
                                                                     ^^^
  ```

- Warning: `subworkflows/local/methyl.nf:16:19`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_versions = Channel.empty()
                    ^^^^^^^
  ```

- Warning: `subworkflows/local/mosdepth.nf:15:19`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_versions = Channel.empty()
                    ^^^^^^^
  ```

- Warning: `subworkflows/local/nanoplot.nf:11:19`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_versions = Channel.empty()
                    ^^^^^^^
  ```

- Warning: `subworkflows/local/unify_vcf.nf:16:19`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_versions = Channel.empty()
                    ^^^^^^^
  ```

- Warning: `subworkflows/local/utils_nfcore_longraredisease_pipeline/main.nf:31:5`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
      monochrome_logs   // boolean: Do not use coloured log outputs
      ^^^^^^^^^^^^^^^
  ```

- Warning: `subworkflows/local/utils_nfcore_longraredisease_pipeline/main.nf:34:5`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
      input             //  string: Path to input samplesheet
      ^^^^^
  ```

- Warning: `subworkflows/local/utils_nfcore_longraredisease_pipeline/main.nf:38:19`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_versions = Channel.empty()
                    ^^^^^^^
  ```

- Warning: `subworkflows/local/utils_nfcore_longraredisease_pipeline/main.nf:75:5`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      Channel
      ^^^^^^^
  ```

- Warning: `subworkflows/nf-core/bam_stats_samtools/main.nf:15:19`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_versions = Channel.empty()
                    ^^^^^^^
  ```

- Warning: `subworkflows/nf-core/utils_nfcore_pipeline/main.nf:101:98`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      return ch_versions.unique().map { version -> processVersionsFromYAML(version) }.unique().mix(Channel.of(workflowVersionToYAML()))
                                                                                                   ^^^^^^^
  ```

- Warning: `workflows/longraredisease.nf:82:22`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_samplesheet = Channel.fromList(samplesheet_data)
                       ^^^^^^^
  ```

- Warning: `workflows/longraredisease.nf:109:19`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_versions = Channel.empty()
                    ^^^^^^^
  ```

- Warning: `workflows/longraredisease.nf:111:16`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_fasta = Channel
                 ^^^^^^^
  ```

- Warning: `workflows/longraredisease.nf:129:18`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
          ch_trf = Channel
                   ^^^^^^^
  ```

- Warning: `workflows/longraredisease.nf:134:18`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
          ch_trf = Channel.empty()
                   ^^^^^^^
  ```

- Warning: `workflows/longraredisease.nf:159:21`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
                      it.name.endsWith('.fastq.gz') || it.name.endsWith('.fq.gz')
                      ^^
  ```

- Warning: `workflows/longraredisease.nf:159:54`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
                      it.name.endsWith('.fastq.gz') || it.name.endsWith('.fq.gz')
                                                       ^^
  ```

- Warning: `workflows/longraredisease.nf:231:68`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
                      def bam_files = bam_path.listFiles().findAll { it.name.endsWith('.bam') }
                                                                     ^^
  ```

- Warning: `workflows/longraredisease.nf:297:65`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          ch_final_sorted_bam = ch_aligned_input.map { meta, bam, bai -> [meta, bam] }
                                                                  ^^^
  ```

- Warning: `workflows/longraredisease.nf:298:60`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          ch_final_sorted_bai = ch_aligned_input.map { meta, bam, bai -> [meta, bai] }
                                                             ^^^
  ```

- Warning: `workflows/longraredisease.nf:438:78`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          ch_sniffles_vcf = filter_sv_sniffles.out.ch_vcf_tbi.map { meta, vcf, tbi -> [meta, vcf] }
                                                                               ^^^
  ```

- Warning: `workflows/longraredisease.nf:439:70`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          ch_svim_vcf = filter_sv_svim.out.ch_vcf_tbi.map { meta, vcf, tbi -> [meta, vcf] }
                                                                       ^^^
  ```

- Warning: `workflows/longraredisease.nf:440:74`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          ch_cutesv_vcf = filter_sv_cutesv.out.ch_vcf_tbi.map { meta, vcf, tbi -> [meta, vcf] }
                                                                           ^^^
  ```

- Warning: `workflows/longraredisease.nf:556:23`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
              .filter { meta, data ->
                        ^^^^
  ```

- Warning: `workflows/longraredisease.nf:574:24`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
          ch_svanna_db = Channel
                         ^^^^^^^
  ```

- Warning: `workflows/longraredisease.nf:580:55`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
              ch_sv_vcf_for_annotation.map { meta, vcf, hpo_terms -> [meta, vcf] },
                                                        ^^^^^^^^^
  ```

- Warning: `workflows/longraredisease.nf:582:44`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
              ch_sv_vcf_for_annotation.map { meta, vcf, hpo_terms -> hpo_terms }
                                             ^^^^
  ```

- Warning: `workflows/longraredisease.nf:582:50`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
              ch_sv_vcf_for_annotation.map { meta, vcf, hpo_terms -> hpo_terms }
                                                   ^^^
  ```

- Warning: `workflows/longraredisease.nf:604:28`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_sv_vcf_downstream = Channel.empty()
                             ^^^^^^^
  ```

- Warning: `workflows/longraredisease.nf:605:23`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_sv_vcf_final = Channel.empty()
                        ^^^^^^^
  ```

- Warning: `workflows/longraredisease.nf:664:22`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
          ch_snv_vcf = Channel.empty()
                       ^^^^^^^
  ```

- Warning: `workflows/longraredisease.nf:665:22`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
          ch_snv_tbi = Channel.empty()
                       ^^^^^^^
  ```

- Warning: `workflows/longraredisease.nf:688:20`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
              .map { sample_key, original_meta, bam, bai, snv_vcf, sv_vcf ->
                     ^^^^^^^^^^
  ```

- Warning: `workflows/longraredisease.nf:714:22`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_spectre_vcf = Channel.empty()
                       ^^^^^^^
  ```

- Warning: `workflows/longraredisease.nf:715:22`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_hificnv_vcf = Channel.empty()
                       ^^^^^^^
  ```

- Warning: `workflows/longraredisease.nf:722:26`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
              .map { meta, data -> meta.id }  // Extract sample ID from samplesheet
                           ^^^^
  ```

- Warning: `workflows/longraredisease.nf:723:22`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
              .combine(Channel.fromPath(params.spectre_test_clair3_vcf, checkIfExists: true))
                       ^^^^^^^
  ```

- Warning: `workflows/longraredisease.nf:724:22`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
              .combine(Channel.fromPath(params.spectre_test_fasta_file, checkIfExists: true))
                       ^^^^^^^
  ```

- Warning: `workflows/longraredisease.nf:725:31`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
              .map { sample_id, vcf_file, fasta ->
                                ^^^^^^^^
  ```

- Warning: `workflows/longraredisease.nf:748:44`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          ch_spectre_bed = ch_combined.map { meta, vcf, bed -> bed }
                                             ^^^^
  ```

- Warning: `workflows/longraredisease.nf:748:50`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          ch_spectre_bed = ch_combined.map { meta, vcf, bed -> bed }
                                                   ^^^
  ```

- Warning: `workflows/longraredisease.nf:749:44`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          ch_spectre_vcf = ch_combined.map { meta, vcf, bed -> vcf }
                                             ^^^^
  ```

- Warning: `workflows/longraredisease.nf:749:55`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          ch_spectre_vcf = ch_combined.map { meta, vcf, bed -> vcf }
                                                        ^^^
  ```

- Warning: `workflows/longraredisease.nf:752:22`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          .map { meta, data -> meta.id }
                       ^^^^
  ```

- Warning: `workflows/longraredisease.nf:754:42`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
              ch_combined.map { meta, vcf, bed -> [meta.id, vcf] },
                                           ^^^
  ```

- Warning: `workflows/longraredisease.nf:757:18`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
          .combine(Channel.fromPath(params.fasta_file, checkIfExists: true))
                   ^^^^^^^
  ```

- Warning: `workflows/longraredisease.nf:758:27`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          .map { sample_id, vcf_file, fasta ->
                            ^^^^^^^^
  ```

- Warning: `workflows/longraredisease.nf:790:13`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
              Channel.empty()
              ^^^^^^^
  ```

- Warning: `workflows/longraredisease.nf:818:22`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
          ch_str_vcf = Channel.empty()
                       ^^^^^^^
  ```

- Warning: `workflows/longraredisease.nf:837:37`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          ch_combined.map { meta, sv, cnv, str -> [meta, sv ?: []] },           // ch_sv_vcfs
                                      ^^^
  ```

- Warning: `workflows/longraredisease.nf:837:42`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          ch_combined.map { meta, sv, cnv, str -> [meta, sv ?: []] },           // ch_sv_vcfs
                                           ^^^
  ```

- Warning: `workflows/longraredisease.nf:838:33`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          ch_combined.map { meta, sv, cnv, str -> [meta, cnv ?: []] },    // ch_cnv_vcf
                                  ^^
  ```

- Warning: `workflows/longraredisease.nf:838:42`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          ch_combined.map { meta, sv, cnv, str -> [meta, cnv ?: []] },    // ch_cnv_vcf
                                           ^^^
  ```

- Warning: `workflows/longraredisease.nf:839:33`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          ch_combined.map { meta, sv, cnv, str -> [meta, str ?: []] },    // ch_repeat_vcf
                                  ^^
  ```

- Warning: `workflows/longraredisease.nf:839:37`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          ch_combined.map { meta, sv, cnv, str -> [meta, str ?: []] },    // ch_repeat_vcf
                                      ^^^
  ```
