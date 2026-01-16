# Nextflow lint results

- Generated: 2026-01-16T06:30:16.082743776Z
- Nextflow version: 25.12.0-edge
- Summary: 17 errors, 152 warnings

## :x: Errors

- Error: `conf/flowswitch.config:32:1`: If statements cannot be mixed with config statements

  ```nextflow
  if(params.consensus_peak_mode == 'all') { params.run_consensus_all  = true  }
  ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  ```

- Error: `conf/flowswitch.config:33:1`: If statements cannot be mixed with config statements

  ```nextflow
  if(params.remove_linear_duplicates)     { params.run_remove_linear_dups = true  }
  ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  ```

- Error: `conf/flowswitch.config:35:1`: If statements cannot be mixed with config statements

  ```nextflow
  if(params.skip_removeduplicates || !params.run_mark_dups) { params.run_remove_dups        = false }
  ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  ```

- Error: `conf/flowswitch.config:36:1`: If statements cannot be mixed with config statements

  ```nextflow
  if(params.skip_removeduplicates)                          { params.run_remove_linear_dups = false }
  ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  ```

- Error: `conf/flowswitch.config:37:1`: If statements cannot be mixed with config statements

  ```nextflow
  if(params.skip_preseq)                                    { params.run_preseq             = false }
  ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  ```

- Error: `conf/flowswitch.config:38:1`: If statements cannot be mixed with config statements

  ```nextflow
  if(params.skip_heatmaps)                                  { params.run_deeptools_heatmaps = false }
  ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  ```

- Error: `conf/flowswitch.config:39:1`: If statements cannot be mixed with config statements

  ```nextflow
  if(params.skip_dt_qc)                                     { params.run_deeptools_qc       = false }
  ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  ```

- Error: `conf/flowswitch.config:40:1`: If statements cannot be mixed with config statements

  ```nextflow
  if(params.skip_peak_qc)                                   { params.run_peak_qc            = false }
  ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  ```

- Error: `conf/flowswitch.config:41:1`: If statements cannot be mixed with config statements

  ```nextflow
  if(params.skip_igv)                                       { params.run_igv                = false }
  ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  ```

- Error: `conf/flowswitch.config:42:1`: If statements cannot be mixed with config statements

  ```nextflow
  if(params.skip_reporting) {
  ^
  ```

- Error: `conf/flowswitch.config:48:1`: If statements cannot be mixed with config statements

  ```nextflow
  if(params.only_input) {
  ^
  ```

- Error: `conf/flowswitch.config:63:1`: If statements cannot be mixed with config statements

  ```nextflow
  if(params.only_genome) {
  ^
  ```

- Error: `conf/flowswitch.config:77:1`: If statements cannot be mixed with config statements

  ```nextflow
  if(params.only_preqc) {
  ^
  ```

- Error: `conf/flowswitch.config:90:1`: If statements cannot be mixed with config statements

  ```nextflow
  if(params.only_alignment) {
  ^
  ```

- Error: `conf/flowswitch.config:101:1`: If statements cannot be mixed with config statements

  ```nextflow
  if(params.only_filtering) {
  ^
  ```

- Error: `conf/flowswitch.config:107:1`: If statements cannot be mixed with config statements

  ```nextflow
  if(params.only_peak_calling) {
  ^
  ```

- Error: `conf/flowswitch.config:112:1`: If statements cannot be mixed with config statements

  ```nextflow
  if(params.skip_multiqc) { params.run_multiqc = false }
  ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  ```

## :warning: Warnings

- Warning: `main.nf:49:74`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
      callers = params.peakcaller ? params.peakcaller.split(',').collect { it.trim().toLowerCase() } : ['seacr']
                                                                           ^^
  ```

- Warning: `main.nf:59:29`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
          params.blacklist ? (Channel.from(file(params.blacklist, checkIfExists: true))) : Channel.empty(),
                              ^^^^^^^
  ```

- Warning: `main.nf:59:90`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
          params.blacklist ? (Channel.from(file(params.blacklist, checkIfExists: true))) : Channel.empty(),
                                                                                           ^^^^^^^
  ```

- Warning: `modules/local/python/igv_session.nf:33:36`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          file_list = beds.collect { it.toString() }.sort()
                                     ^^
  ```

- Warning: `modules/local/python/igv_session.nf:34:47`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          file_list += secondary_beds.collect { it.toString() }.sort()
                                                ^^
  ```

- Warning: `modules/local/python/igv_session.nf:35:39`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          file_list += bigwig.collect { it.toString() }.sort()
                                        ^^
  ```

- Warning: `modules/local/python/igv_session.nf:38:64`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          file_list = (bigwig + secondary_beds + beds).collect { it.toString() }.sort()
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

- Warning: `modules/nf-core/gunzip/main.nf:43:9`: Variable was declared but not used

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

- Warning: `subworkflows/local/align_bowtie2.nf:19:19`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_versions = Channel.empty()
                    ^^^^^^^
  ```

- Warning: `subworkflows/local/align_bowtie2.nf:24:34`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
      ch_index = index.map { [[id: it.baseName], it] }
                                   ^^
  ```

- Warning: `subworkflows/local/align_bowtie2.nf:24:48`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
      ch_index = index.map { [[id: it.baseName], it] }
                                                 ^^
  ```

- Warning: `subworkflows/local/align_bowtie2.nf:27:28`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          ch_index.collect { it[1] },
                             ^^
  ```

- Warning: `subworkflows/local/align_bowtie2.nf:36:50`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
      ch_spikein_index = spikein_index.map { [[id: it.baseName], it] }
                                                   ^^
  ```

- Warning: `subworkflows/local/align_bowtie2.nf:36:64`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
      ch_spikein_index = spikein_index.map { [[id: it.baseName], it] }
                                                                 ^^
  ```

- Warning: `subworkflows/local/align_bowtie2.nf:39:36`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          ch_spikein_index.collect { it[1] },
                                     ^^
  ```

- Warning: `subworkflows/local/consensus_peaks.nf:14:19`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_versions = Channel.empty()
                    ^^^^^^^
  ```

- Warning: `subworkflows/local/deduplicate_linear.nf:23:14`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_bam = Channel.empty()
               ^^^^^^^
  ```

- Warning: `subworkflows/local/deduplicate_linear.nf:24:18`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_metrics = Channel.empty()
                   ^^^^^^^
  ```

- Warning: `subworkflows/local/deduplicate_linear.nf:25:19`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_versions = Channel.empty()
                    ^^^^^^^
  ```

- Warning: `subworkflows/local/deduplicate_linear.nf:26:28`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_linear_duplicates = Channel.empty()
                             ^^^^^^^
  ```

- Warning: `subworkflows/local/deeptools_qc.nf:17:19`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_versions = Channel.empty()
                    ^^^^^^^
  ```

- Warning: `subworkflows/local/extract_fragments.nf:15:19`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_versions = Channel.empty()
                    ^^^^^^^
  ```

- Warning: `subworkflows/local/extract_metadata_awk.nf:15:19`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_versions = Channel.empty()
                    ^^^^^^^
  ```

- Warning: `subworkflows/local/extract_metadata_awk.nf:16:19`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_metadata = Channel.empty()
                    ^^^^^^^
  ```

- Warning: `subworkflows/local/fastqc_trimgalore.nf:15:19`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_versions = Channel.empty()
                    ^^^^^^^
  ```

- Warning: `subworkflows/local/fastqc_trimgalore.nf:17:19`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      fastqc_html = Channel.empty()
                    ^^^^^^^
  ```

- Warning: `subworkflows/local/fastqc_trimgalore.nf:18:18`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      fastqc_zip = Channel.empty()
                   ^^^^^^^
  ```

- Warning: `subworkflows/local/fastqc_trimgalore.nf:25:17`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      trim_html = Channel.empty()
                  ^^^^^^^
  ```

- Warning: `subworkflows/local/fastqc_trimgalore.nf:26:16`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      trim_zip = Channel.empty()
                 ^^^^^^^
  ```

- Warning: `subworkflows/local/fastqc_trimgalore.nf:27:16`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      trim_log = Channel.empty()
                 ^^^^^^^
  ```

- Warning: `subworkflows/local/mark_duplicates_picard.nf:18:14`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_bam = Channel.empty()
               ^^^^^^^
  ```

- Warning: `subworkflows/local/mark_duplicates_picard.nf:19:14`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_bai = Channel.empty()
               ^^^^^^^
  ```

- Warning: `subworkflows/local/mark_duplicates_picard.nf:20:18`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_metrics = Channel.empty()
                   ^^^^^^^
  ```

- Warning: `subworkflows/local/mark_duplicates_picard.nf:21:16`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_stats = Channel.empty()
                 ^^^^^^^
  ```

- Warning: `subworkflows/local/mark_duplicates_picard.nf:22:19`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_flagstat = Channel.empty()
                    ^^^^^^^
  ```

- Warning: `subworkflows/local/mark_duplicates_picard.nf:23:19`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_idxstats = Channel.empty()
                    ^^^^^^^
  ```

- Warning: `subworkflows/local/mark_duplicates_picard.nf:24:19`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_versions = Channel.empty()
                    ^^^^^^^
  ```

- Warning: `subworkflows/local/peak_qc.nf:28:19`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_versions = Channel.empty()
                    ^^^^^^^
  ```

- Warning: `subworkflows/local/prepare_genome.nf:30:19`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_versions = Channel.empty()
                    ^^^^^^^
  ```

- Warning: `subworkflows/local/prepare_genome.nf:31:24`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_spikein_fasta = Channel.empty()
                         ^^^^^^^
  ```

- Warning: `subworkflows/local/prepare_genome.nf:41:20`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
          ch_fasta = Channel.from(file(params.fasta)).map { row -> [[id: "fasta"], row] }
                     ^^^^^^^
  ```

- Warning: `subworkflows/local/prepare_genome.nf:53:32`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
              ch_spikein_fasta = Channel.from(file(params.spikein_fasta)).map { row -> [[id: "spikein_fasta"], row] }
                                 ^^^^^^^
  ```

- Warning: `subworkflows/local/prepare_genome.nf:61:14`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_gtf = Channel.empty()
               ^^^^^^^
  ```

- Warning: `subworkflows/local/prepare_genome.nf:63:61`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          ch_gtf = GUNZIP_GTF([[:], params.gtf]).gunzip.map { it[1] }
                                                              ^^
  ```

- Warning: `subworkflows/local/prepare_genome.nf:67:18`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
          ch_gtf = Channel.from(file(params.gtf))
                   ^^^^^^^
  ```

- Warning: `subworkflows/local/prepare_genome.nf:70:19`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_gene_bed = Channel.empty()
                    ^^^^^^^
  ```

- Warning: `subworkflows/local/prepare_genome.nf:76:75`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
              ch_gene_bed = GUNZIP_BED([[:], params.gene_bed]).gunzip.map { it[1] }
                                                                            ^^
  ```

- Warning: `subworkflows/local/prepare_genome.nf:80:27`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
              ch_gene_bed = Channel.from(file(params.gene_bed))
                            ^^^^^^^
  ```

- Warning: `subworkflows/local/prepare_genome.nf:128:62`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
      ch_chrom_sizes = TARGET_CHROMSIZES(ch_fasta).sizes.map { it[1] }
                                                               ^^
  ```

- Warning: `subworkflows/local/prepare_genome.nf:134:79`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
      ch_spikein_chrom_sizes = SPIKEIN_CHROMSIZES(ch_spikein_fasta).sizes.map { it[1] }
                                                                                ^^
  ```

- Warning: `subworkflows/local/prepare_genome.nf:139:20`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_bt2_index = Channel.empty()
                     ^^^^^^^
  ```

- Warning: `subworkflows/local/prepare_genome.nf:140:28`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_bt2_spikein_index = Channel.empty()
                             ^^^^^^^
  ```

- Warning: `subworkflows/local/prepare_genome.nf:174:33`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_genome_include_regions = Channel.empty()
                                  ^^^^^^^
  ```

- Warning: `subworkflows/local/prepare_peakcalling.nf:21:19`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_versions = Channel.empty()
                    ^^^^^^^
  ```

- Warning: `subworkflows/local/prepare_peakcalling.nf:22:19`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_bedgraph = Channel.empty()
                    ^^^^^^^
  ```

- Warning: `subworkflows/local/prepare_peakcalling.nf:42:49`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
                  def denominator = row[3].find { it.key == "bt2_total_aligned" }?.value.toInteger()
                                                  ^^
  ```

- Warning: `subworkflows/local/prepare_peakcalling.nf:77:25`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
                  .map { [it[0].id, it[0].group, it[2]] }
                          ^^
  ```

- Warning: `subworkflows/local/prepare_peakcalling.nf:77:35`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
                  .map { [it[0].id, it[0].group, it[2]] }
                                    ^^
  ```

- Warning: `subworkflows/local/prepare_peakcalling.nf:77:48`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
                  .map { [it[0].id, it[0].group, it[2]] }
                                                 ^^
  ```

- Warning: `subworkflows/local/prepare_peakcalling.nf:157:25`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
                  .map { [it[0].id, it[0].group, it[3]] }
                          ^^
  ```

- Warning: `subworkflows/local/prepare_peakcalling.nf:157:35`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
                  .map { [it[0].id, it[0].group, it[3]] }
                                    ^^
  ```

- Warning: `subworkflows/local/prepare_peakcalling.nf:157:48`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
                  .map { [it[0].id, it[0].group, it[3]] }
                                                 ^^
  ```

- Warning: `subworkflows/local/samtools_view_sort_stats.nf:17:19`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_versions = Channel.empty()
                    ^^^^^^^
  ```

- Warning: `subworkflows/local/utils_nfcore_cutandrun_pipeline/main.nf:32:5`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
      monochrome_logs   // boolean: Do not use coloured log outputs
      ^^^^^^^^^^^^^^^
  ```

- Warning: `subworkflows/local/utils_nfcore_cutandrun_pipeline/main.nf:42:19`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_versions = Channel.empty()
                    ^^^^^^^
  ```

- Warning: `subworkflows/local/utils_nfcore_cutandrun_pipeline/main.nf:67:144`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
      after_text = """${workflow.manifest.doi ? "\n* The pipeline\n" : ""}${workflow.manifest.doi.tokenize(",").collect { "    https://doi.org/${it.trim().replace('https://doi.org/', '')}" }.join("\n")}${workflow.manifest.doi ? "\n" : ""}
                                                                                                                                                 ^^
  ```

- Warning: `subworkflows/local/utils_nfcore_cutandrun_pipeline/main.nf:103:22`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_samplesheet = Channel.fromList(samplesheetToList(input, "${projectDir}/assets/schema_input.json"))
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

- Warning: `subworkflows/nf-core/utils_nfcore_pipeline/main.nf:101:98`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      return ch_versions.unique().map { version -> processVersionsFromYAML(version) }.unique().mix(Channel.of(workflowVersionToYAML()))
                                                                                                   ^^^^^^^
  ```

- Warning: `workflows/cutandrun.nf:94:23`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      def ch_versions = Channel.empty()
                        ^^^^^^^
  ```

- Warning: `workflows/cutandrun.nf:95:28`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      def ch_multiqc_files = Channel.empty()
                             ^^^^^^^
  ```

- Warning: `workflows/cutandrun.nf:149:92`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          ch_multiqc_files = ch_multiqc_files.mix(FASTQC_TRIMGALORE.out.fastqc_zip.collect { it[1] }.ifEmpty([]))
                                                                                             ^^
  ```

- Warning: `workflows/cutandrun.nf:150:90`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          ch_multiqc_files = ch_multiqc_files.mix(FASTQC_TRIMGALORE.out.trim_zip.collect { it[1] }.ifEmpty([]))
                                                                                           ^^
  ```

- Warning: `workflows/cutandrun.nf:151:90`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          ch_multiqc_files = ch_multiqc_files.mix(FASTQC_TRIMGALORE.out.trim_log.collect { it[1] }.ifEmpty([]))
                                                                                           ^^
  ```

- Warning: `workflows/cutandrun.nf:159:19`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_orig_bam = Channel.empty()
                    ^^^^^^^
  ```

- Warning: `workflows/cutandrun.nf:160:27`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_orig_spikein_bam = Channel.empty()
                            ^^^^^^^
  ```

- Warning: `workflows/cutandrun.nf:161:22`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_bowtie2_log = Channel.empty()
                       ^^^^^^^
  ```

- Warning: `workflows/cutandrun.nf:162:30`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_bowtie2_spikein_log = Channel.empty()
                               ^^^^^^^
  ```

- Warning: `workflows/cutandrun.nf:163:23`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_samtools_bam = Channel.empty()
                        ^^^^^^^
  ```

- Warning: `workflows/cutandrun.nf:164:23`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_samtools_bai = Channel.empty()
                        ^^^^^^^
  ```

- Warning: `workflows/cutandrun.nf:165:28`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_samtools_flagstat = Channel.empty()
                             ^^^^^^^
  ```

- Warning: `workflows/cutandrun.nf:166:31`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_samtools_spikein_bam = Channel.empty()
                                ^^^^^^^
  ```

- Warning: `workflows/cutandrun.nf:167:31`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_samtools_spikein_bai = Channel.empty()
                                ^^^^^^^
  ```

- Warning: `workflows/cutandrun.nf:168:33`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_samtools_spikein_stats = Channel.empty()
                                  ^^^^^^^
  ```

- Warning: `workflows/cutandrun.nf:169:36`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_samtools_spikein_flagstat = Channel.empty()
                                     ^^^^^^^
  ```

- Warning: `workflows/cutandrun.nf:170:36`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_samtools_spikein_idxstats = Channel.empty()
                                     ^^^^^^^
  ```

- Warning: `workflows/cutandrun.nf:195:87`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
              ch_multiqc_files = ch_multiqc_files.mix(ALIGN_BOWTIE2.out.stats.collect { it[1] }.ifEmpty([]))
                                                                                        ^^
  ```

- Warning: `workflows/cutandrun.nf:196:90`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
              ch_multiqc_files = ch_multiqc_files.mix(ALIGN_BOWTIE2.out.idxstats.collect { it[1] }.ifEmpty([]))
                                                                                           ^^
  ```

- Warning: `workflows/cutandrun.nf:205:30`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_metadata_bt2_target = Channel.empty()
                               ^^^^^^^
  ```

- Warning: `workflows/cutandrun.nf:206:31`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_metadata_bt2_spikein = Channel.empty()
                                ^^^^^^^
  ```

- Warning: `workflows/cutandrun.nf:238:58`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
              PREPARE_GENOME.out.allowed_regions.collect { it[1] }.ifEmpty([]),
                                                           ^^
  ```

- Warning: `workflows/cutandrun.nf:246:82`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          ch_multiqc_files = ch_multiqc_files.mix(FILTER_READS.out.stats.collect { it[1] }.ifEmpty([]))
                                                                                   ^^
  ```

- Warning: `workflows/cutandrun.nf:247:85`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          ch_multiqc_files = ch_multiqc_files.mix(FILTER_READS.out.idxstats.collect { it[1] }.ifEmpty([]))
                                                                                      ^^
  ```

- Warning: `workflows/cutandrun.nf:260:89`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          ch_multiqc_files = ch_multiqc_files.mix(PRESEQ_LCEXTRAP.out.lc_extrap.collect { it[1] }.ifEmpty([]))
                                                                                          ^^
  ```

- Warning: `workflows/cutandrun.nf:266:33`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_markduplicates_metrics = Channel.empty()
                                  ^^^^^^^
  ```

- Warning: `workflows/cutandrun.nf:281:92`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          ch_multiqc_files = ch_multiqc_files.mix(MARK_DUPLICATES_PICARD.out.stats.collect { it[1] }.ifEmpty([]))
                                                                                             ^^
  ```

- Warning: `workflows/cutandrun.nf:282:95`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          ch_multiqc_files = ch_multiqc_files.mix(MARK_DUPLICATES_PICARD.out.idxstats.collect { it[1] }.ifEmpty([]))
                                                                                                ^^
  ```

- Warning: `workflows/cutandrun.nf:303:88`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          ch_multiqc_files = ch_multiqc_files.mix(DEDUPLICATE_PICARD.out.stats.collect { it[1] }.ifEmpty([]))
                                                                                         ^^
  ```

- Warning: `workflows/cutandrun.nf:304:91`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          ch_multiqc_files = ch_multiqc_files.mix(DEDUPLICATE_PICARD.out.idxstats.collect { it[1] }.ifEmpty([]))
                                                                                            ^^
  ```

- Warning: `workflows/cutandrun.nf:312:37`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_metadata_picard_duplicates = Channel.empty()
                                      ^^^^^^^
  ```

- Warning: `workflows/cutandrun.nf:328:25`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_linear_metrics = Channel.empty()
                          ^^^^^^^
  ```

- Warning: `workflows/cutandrun.nf:342:88`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          ch_multiqc_files = ch_multiqc_files.mix(DEDUPLICATE_LINEAR.out.stats.collect { it[1] }.ifEmpty([]))
                                                                                         ^^
  ```

- Warning: `workflows/cutandrun.nf:343:91`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          ch_multiqc_files = ch_multiqc_files.mix(DEDUPLICATE_LINEAR.out.idxstats.collect { it[1] }.ifEmpty([]))
                                                                                            ^^
  ```

- Warning: `workflows/cutandrun.nf:344:101`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          ch_multiqc_files = ch_multiqc_files.mix(DEDUPLICATE_LINEAR.out.linear_metrics_mqc.collect { it[1] }.ifEmpty([]))
                                                                                                      ^^
  ```

- Warning: `workflows/cutandrun.nf:347:19`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_bedgraph = Channel.empty()
                    ^^^^^^^
  ```

- Warning: `workflows/cutandrun.nf:348:17`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_bigwig = Channel.empty()
                  ^^^^^^^
  ```

- Warning: `workflows/cutandrun.nf:349:22`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_seacr_peaks = Channel.empty()
                       ^^^^^^^
  ```

- Warning: `workflows/cutandrun.nf:350:22`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_macs2_peaks = Channel.empty()
                       ^^^^^^^
  ```

- Warning: `workflows/cutandrun.nf:351:24`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_peaks_primary = Channel.empty()
                         ^^^^^^^
  ```

- Warning: `workflows/cutandrun.nf:352:26`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_peaks_secondary = Channel.empty()
                           ^^^^^^^
  ```

- Warning: `workflows/cutandrun.nf:353:24`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_peaks_summits = Channel.empty()
                         ^^^^^^^
  ```

- Warning: `workflows/cutandrun.nf:354:26`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_consensus_peaks = Channel.empty()
                           ^^^^^^^
  ```

- Warning: `workflows/cutandrun.nf:355:33`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_consensus_peaks_unfilt = Channel.empty()
                                  ^^^^^^^
  ```

- Warning: `workflows/cutandrun.nf:590:48`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
                  PREPARE_GENOME.out.fasta.map { it[1] },
                                                 ^^
  ```

- Warning: `workflows/cutandrun.nf:591:54`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
                  PREPARE_GENOME.out.fasta_index.map { it[1] },
                                                       ^^
  ```

- Warning: `workflows/cutandrun.nf:593:44`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
                  ch_peaks_primary.collect { it[1] }.filter { it -> it.size() > 1 }.ifEmpty([]),
                                             ^^
  ```

- Warning: `workflows/cutandrun.nf:594:46`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
                  ch_peaks_secondary.collect { it[1] }.filter { it -> it.size() > 1 }.ifEmpty([]),
                                               ^^
  ```

- Warning: `workflows/cutandrun.nf:595:37`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
                  ch_bigwig.collect { it[1] }.ifEmpty([]),
                                      ^^
  ```

- Warning: `workflows/cutandrun.nf:606:27`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
                  .filter { it[0].is_control == false }
                            ^^
  ```

- Warning: `workflows/cutandrun.nf:681:44`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
                      ch_bigwig_no_igg.map { it[1] }.toSortedList().map { [[id: 'all_genes'], it] },
                                             ^^
  ```

- Warning: `workflows/cutandrun.nf:681:93`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
                      ch_bigwig_no_igg.map { it[1] }.toSortedList().map { [[id: 'all_genes'], it] },
                                                                                              ^^
  ```

- Warning: `workflows/cutandrun.nf:704:99`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
              ch_multiqc_files = ch_multiqc_files.mix(DEEPTOOLS_QC.out.correlation_matrix.collect { it[1] }.ifEmpty([]))
                                                                                                    ^^
  ```

- Warning: `workflows/cutandrun.nf:705:89`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
              ch_multiqc_files = ch_multiqc_files.mix(DEEPTOOLS_QC.out.pca_data.collect { it[1] }.ifEmpty([]))
                                                                                          ^^
  ```

- Warning: `workflows/cutandrun.nf:706:99`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
              ch_multiqc_files = ch_multiqc_files.mix(DEEPTOOLS_QC.out.fingerprint_matrix.collect { it[1] }.ifEmpty([]))
                                                                                                    ^^
  ```

- Warning: `workflows/cutandrun.nf:750:92`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
              ch_multiqc_files = ch_multiqc_files.mix(PEAK_QC.out.primary_frip_mqc.collect { it[1] }.ifEmpty([]))
                                                                                             ^^
  ```

- Warning: `workflows/cutandrun.nf:751:93`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
              ch_multiqc_files = ch_multiqc_files.mix(PEAK_QC.out.primary_count_mqc.collect { it[1] }.ifEmpty([]))
                                                                                              ^^
  ```

- Warning: `workflows/cutandrun.nf:752:95`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
              ch_multiqc_files = ch_multiqc_files.mix(PEAK_QC.out.consensus_count_mqc.collect { it[1] }.ifEmpty([]))
                                                                                                ^^
  ```

- Warning: `workflows/cutandrun.nf:753:91`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
              ch_multiqc_files = ch_multiqc_files.mix(PEAK_QC.out.reprod_perc_mqc.collect { it[1] }.ifEmpty([]))
                                                                                            ^^
  ```

- Warning: `workflows/cutandrun.nf:798:90`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          ch_multiqc_files = ch_multiqc_files.mix(FRAG_LEN_HIST.out.frag_len_mqc.collect { it[1] }.ifEmpty([]))
                                                                                           ^^
  ```

- Warning: `workflows/cutandrun.nf:803:74`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          ch_multiqc_files = ch_multiqc_files.mix(ch_bowtie2_log.collect { it[1] }.ifEmpty([]))
                                                                           ^^
  ```

- Warning: `workflows/cutandrun.nf:804:82`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          ch_multiqc_files = ch_multiqc_files.mix(ch_bowtie2_spikein_log.collect { it[1] }.ifEmpty([]))
                                                                                   ^^
  ```

- Warning: `workflows/cutandrun.nf:805:80`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          ch_multiqc_files = ch_multiqc_files.mix(ch_samtools_flagstat.collect { it[1] }.ifEmpty([]))
                                                                                 ^^
  ```

- Warning: `workflows/cutandrun.nf:806:85`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          ch_multiqc_files = ch_multiqc_files.mix(ch_markduplicates_metrics.collect { it[1] }.ifEmpty([]))
                                                                                      ^^
  ```

- Warning: `workflows/cutandrun.nf:818:29`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
          ch_multiqc_config = Channel.fromPath("${projectDir}/assets/multiqc_config.yml", checkIfExists: true)
                              ^^^^^^^
  ```

- Warning: `workflows/cutandrun.nf:819:60`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
          ch_multiqc_custom_config = params.multiqc_config ? Channel.fromPath(params.multiqc_config, checkIfExists: true) : Channel.empty()
                                                             ^^^^^^^
  ```

- Warning: `workflows/cutandrun.nf:819:123`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
          ch_multiqc_custom_config = params.multiqc_config ? Channel.fromPath(params.multiqc_config, checkIfExists: true) : Channel.empty()
                                                                                                                            ^^^^^^^
  ```

- Warning: `workflows/cutandrun.nf:820:49`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
          ch_multiqc_logo = params.multiqc_logo ? Channel.fromPath(params.multiqc_logo, checkIfExists: true) : Channel.empty()
                                                  ^^^^^^^
  ```

- Warning: `workflows/cutandrun.nf:820:110`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
          ch_multiqc_logo = params.multiqc_logo ? Channel.fromPath(params.multiqc_logo, checkIfExists: true) : Channel.empty()
                                                                                                               ^^^^^^^
  ```

- Warning: `workflows/cutandrun.nf:822:31`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
          ch_workflow_summary = Channel.value(paramsSummaryMultiqc(summary_params))
                                ^^^^^^^
  ```

- Warning: `workflows/cutandrun.nf:824:34`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
          ch_methods_description = Channel.value(methodsDescriptionText(ch_multiqc_custom_methods_description))
                                   ^^^^^^^
  ```

- Warning: `workflows/cutandrun.nf:887:98`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      return ch_versions.unique().map { version -> processVersionsFromYAML(version) }.unique().mix(Channel.of(workflowVersionToYAML()))
                                                                                                   ^^^^^^^
  ```
