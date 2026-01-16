# Nextflow lint results

- Generated: 2026-01-16T10:28:47.639887306Z
- Nextflow version: 25.12.0-edge
- Summary: 21 errors, 148 warnings

## :x: Errors

- Error: `conf/modules.config:40:17`: Unexpected input: ':'

  ```nextflow
          withName: 'TRIMMOMATIC' {
                  ^
  ```

- Error: `modules/nf-core/untarfiles/main.nf:1:1`: Statements cannot be mixed with script declarations -- move statements into a process, workflow, or function

  ```nextflow
  def deprecation_message = """
  ^^^
  ```

- Error: `modules/nf-core/untarfiles/main.nf:27:18`: `deprecation_message` is not defined

  ```nextflow
      assert true: deprecation_message
                   ^^^^^^^^^^^^^^^^^^^
  ```

- Error: `modules/nf-core/untarfiles/main.nf:49:18`: `deprecation_message` is not defined

  ```nextflow
      assert true: deprecation_message
                   ^^^^^^^^^^^^^^^^^^^
  ```

- Error: `subworkflows/local/cat_fractions/main.nf:22:13`: Variables in a closure should be declared with `def`

  ```nextflow
              meta2 = meta[0].clone()  // take first map only and create a copy
              ^^^^^
  ```

- Error: `subworkflows/local/deeptools_qc/main.nf:71:26`: `bam` is already declared

  ```nextflow
              .map { meta, bam, bai ->
                           ^^^
  ```

- Error: `subworkflows/local/deeptools_qc/main.nf:71:31`: `bai` is already declared

  ```nextflow
              .map { meta, bam, bai ->
                                ^^^
  ```

- Error: `workflows/sammyseq.nf:50:1`: Statements cannot be mixed with script declarations -- move statements into a process, workflow, or function

  ```nextflow
  if (params.fasta) { ch_fasta =  Channel.fromPath(params.fasta) } else { exit 1, 'Fasta reference genome not specified!' }
  ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  ```

- Error: `workflows/sammyseq.nf:53:1`: Statements cannot be mixed with script declarations -- move statements into a process, workflow, or function

  ```nextflow
  ch_fasta_meta = ch_fasta.map{ it -> [[id:it[0].baseName], it] }.collect()
  ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  ```

- Error: `workflows/sammyseq.nf:61:1`: Statements cannot be mixed with script declarations -- move statements into a process, workflow, or function

  ```nextflow
  ch_multiqc_config          = Channel.fromPath("$projectDir/assets/multiqc_config.yml", checkIfExists: true)
  ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  ```

- Error: `workflows/sammyseq.nf:62:1`: Statements cannot be mixed with script declarations -- move statements into a process, workflow, or function

  ```nextflow
  ch_multiqc_custom_config   = params.multiqc_config ? Channel.fromPath( params.multiqc_config, checkIfExists: true ) : Channel.empty()
  ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  ```

- Error: `workflows/sammyseq.nf:63:1`: Statements cannot be mixed with script declarations -- move statements into a process, workflow, or function

  ```nextflow
  ch_multiqc_logo            = params.multiqc_logo   ? Channel.fromPath( params.multiqc_logo, checkIfExists: true ) : Channel.empty()
  ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  ```

- Error: `workflows/sammyseq.nf:64:1`: Statements cannot be mixed with script declarations -- move statements into a process, workflow, or function

  ```nextflow
  ch_multiqc_custom_methods_description = params.multiqc_methods_description ? file(params.multiqc_methods_description, checkIfExists: true) : file("$projectDir/assets/methods_description_template.yml", checkIfExists: true)
  ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  ```

- Error: `workflows/sammyseq.nf:160:21`: Variables in a closure should be declared with `def`

  ```nextflow
                      newid=id.id + "_trim"
                      ^^^^^
  ```

- Error: `workflows/sammyseq.nf:161:21`: Variables in a closure should be declared with `def`

  ```nextflow
                      sng=meta.subMap('single_end').single_end
                      ^^^
  ```

- Error: `workflows/sammyseq.nf:162:21`: Variables in a closure should be declared with `def`

  ```nextflow
                      newmeta=[id: newid, single_end: sng]
                      ^^^^^^^
  ```

- Error: `workflows/sammyseq.nf:195:13`: `ch_fasta_meta` is not defined

  ```nextflow
              ch_fasta_meta,
              ^^^^^^^^^^^^^
  ```

- Error: `workflows/sammyseq.nf:205:13`: `ch_fasta_meta` is not defined

  ```nextflow
              ch_fasta_meta,
              ^^^^^^^^^^^^^
  ```

- Error: `workflows/sammyseq.nf:224:9`: `ch_fasta_meta` is not defined

  ```nextflow
          ch_fasta_meta,
          ^^^^^^^^^^^^^
  ```

- Error: `workflows/sammyseq.nf:245:9`: `ch_fasta_meta` is not defined

  ```nextflow
          ch_fasta_meta
          ^^^^^^^^^^^^^
  ```

- Error: `workflows/sammyseq.nf:260:21`: `ch_fasta_meta` is not defined

  ```nextflow
      ch_fasta_path = ch_fasta_meta.map { it[1] }
                      ^^^^^^^^^^^^^
  ```

## :warning: Warnings

- Warning: `modules/local/differential_enrichment/main.nf:29:5`: Variable was declared but not used

  ```nextflow
      test_group = contrast_data[0]
      ^^^^^^^^^^
  ```

- Warning: `modules/local/differential_enrichment/main.nf:30:5`: Variable was declared but not used

  ```nextflow
      ref_group = contrast_data[1]
      ^^^^^^^^^
  ```

- Warning: `modules/local/differential_enrichment/main.nf:31:5`: Variable was declared but not used

  ```nextflow
      contrast_name = "${contrast_data[0]}vs${contrast_data[1]}"
      ^^^^^^^^^^^^^
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

- Warning: `modules/nf-core/trimgalore/main.nf:47:31`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          args_list.removeAll { it.toLowerCase().contains('_r2 ') }
                                ^^
  ```

- Warning: `modules/nf-core/untarfiles/main.nf:1:5`: Variable was declared but not used

  ```nextflow
  def deprecation_message = """
      ^^^^^^^^^^^^^^^^^^^
  ```

- Warning: `subworkflows/local/bigwig_plot_deeptools/main.nf:15:19`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_versions = Channel.empty()
                    ^^^^^^^
  ```

- Warning: `subworkflows/local/cat_fractions/main.nf:12:19`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_versions = Channel.empty()
                    ^^^^^^^
  ```

- Warning: `subworkflows/local/cat_fractions/main.nf:29:19`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          .filter { meta, fastq -> fastq.size() > 1 }
                    ^^^^
  ```

- Warning: `subworkflows/local/cat_fractions/main.nf:42:23`: Variable was declared but not used

  ```nextflow
          ).reads.set { cat_fastq_output }
                        ^^^^^^^^^^^^^^^^
  ```

- Warning: `subworkflows/local/deeptools_qc/main.nf:20:19`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_versions = Channel.empty()
                    ^^^^^^^
  ```

- Warning: `subworkflows/local/deeptools_qc/main.nf:62:36`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_fingerprint_matrix_global = Channel.empty()
                                     ^^^^^^^
  ```

- Warning: `subworkflows/local/deeptools_qc/main.nf:63:37`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_fingerprint_metrics_global = Channel.empty()
                                      ^^^^^^^
  ```

- Warning: `subworkflows/local/deeptools_qc/main.nf:64:36`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_fingerprint_region_matrix = Channel.empty()
                                     ^^^^^^^
  ```

- Warning: `subworkflows/local/deeptools_qc/main.nf:65:37`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_fingerprint_region_metrics = Channel.empty()
                                      ^^^^^^^
  ```

- Warning: `subworkflows/local/differential_solubility_analysis/main.nf:20:19`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_versions = Channel.empty()
                    ^^^^^^^
  ```

- Warning: `subworkflows/local/differential_solubility_analysis/main.nf:26:29`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          .filter { csv_meta, mle_file -> csv_meta.csv_expid_filter }
                              ^^^^^^^^
  ```

- Warning: `subworkflows/local/differential_solubility_analysis/main.nf:35:20`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_contrasts = Channel
                     ^^^^^^^
  ```

- Warning: `subworkflows/local/filter_bam_samtools/main.nf:15:19`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_versions = Channel.empty()
                    ^^^^^^^
  ```

- Warning: `subworkflows/local/filter_bam_samtools/main.nf:24:23`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          bam_bai.map { it[2].getName().tokenize('.')[-1] }
                        ^^
  ```

- Warning: `subworkflows/local/generate_comparisons/main.nf:17:29`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_comparison_results = Channel.empty()
                              ^^^^^^^
  ```

- Warning: `subworkflows/local/generate_comparisons/main.nf:18:19`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_versions = Channel.empty()
                    ^^^^^^^
  ```

- Warning: `subworkflows/local/generate_comparisons/main.nf:21:25`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      comparisons_ch_s1 = Channel.empty()
                          ^^^^^^^
  ```

- Warning: `subworkflows/local/generate_comparisons/main.nf:22:25`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      comparisons_ch_s2 = Channel.empty()
                          ^^^^^^^
  ```

- Warning: `subworkflows/local/generate_comparisons/main.nf:26:9`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
          Channel
          ^^^^^^^
  ```

- Warning: `subworkflows/local/generate_comparisons/main.nf:40:70`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          def comparison_list = params.comparison.split(',').collect { it.trim() }
                                                                       ^^
  ```

- Warning: `subworkflows/local/generate_comparisons/main.nf:44:26`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
              .map { meta, fastqs -> meta }
                           ^^^^^^
  ```

- Warning: `subworkflows/local/generate_comparisons/main.nf:49:64`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
                      def samples_by_expID = meta_list.groupBy { it.experimentalID } // Group samples by experimental ID
                                                                 ^^
  ```

- Warning: `subworkflows/local/generate_comparisons/main.nf:52:49`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
                          def s1 = samples.find { it.fraction == frac1 }?.id
                                                  ^^
  ```

- Warning: `subworkflows/local/generate_comparisons/main.nf:53:49`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
                          def s2 = samples.find { it.fraction == frac2 }?.id
                                                  ^^
  ```

- Warning: `subworkflows/local/generate_comparisons/main.nf:85:16`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          .map { sample1, comparison, file, meta ->
                 ^^^^^^^
  ```

- Warning: `subworkflows/local/generate_comparisons/main.nf:92:16`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          .map { sample2, comparison, file, meta ->
                 ^^^^^^^
  ```

- Warning: `subworkflows/local/generate_comparisons/main.nf:100:16`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          .map { comparison, f1, meta1, f2, meta2 ->
                 ^^^^^^^^^^
  ```

- Warning: `subworkflows/local/generate_comparisons/main.nf:137:15`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
              ? Channel.value([[:], file(params.blacklist)])
                ^^^^^^^
  ```

- Warning: `subworkflows/local/generate_comparisons/main.nf:138:15`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
              : Channel.value([[:], []])
                ^^^^^^^
  ```

- Warning: `subworkflows/local/genome_binning/main.nf:18:19`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_versions = Channel.empty()
                    ^^^^^^^
  ```

- Warning: `subworkflows/local/genome_binning/main.nf:23:27`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_keep_regions_bed = Channel.empty()
                            ^^^^^^^
  ```

- Warning: `subworkflows/local/genome_binning/main.nf:29:28`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
              ).gunzip.map { it[1] }
                             ^^
  ```

- Warning: `subworkflows/local/genome_binning/main.nf:32:35`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
              ch_keep_regions_bed = Channel.fromPath(keep_regions_bed_param, checkIfExists: true)
                                    ^^^^^^^
  ```

- Warning: `subworkflows/local/prepare_genome/main.nf:33:5`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
      fasta              //    path: path to genome fasta file
      ^^^^^
  ```

- Warning: `subworkflows/local/prepare_genome/main.nf:34:5`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
      aligner            //    string: aligner name
      ^^^^^^^
  ```

- Warning: `subworkflows/local/prepare_genome/main.nf:35:5`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
      gtf                //    file: /path/to/genome.gtf
      ^^^
  ```

- Warning: `subworkflows/local/prepare_genome/main.nf:36:5`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
      tss_bed            //    file: /path/to/tss.bed
      ^^^^^^^
  ```

- Warning: `subworkflows/local/prepare_genome/main.nf:38:5`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
      blacklist          //    file: /path/to/blacklist.bed
      ^^^^^^^^^
  ```

- Warning: `subworkflows/local/prepare_genome/main.nf:39:5`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
      gene_bed           //    file: /path/to/gene.bed
      ^^^^^^^^
  ```

- Warning: `subworkflows/local/prepare_genome/main.nf:40:5`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
      bwa_index          //    file: /path/to/bwa/index/
      ^^^^^^^^^
  ```

- Warning: `subworkflows/local/prepare_genome/main.nf:41:5`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
      bowtie2_index      //    file: /path/to/bowtie2/index/
      ^^^^^^^^^^^^^
  ```

- Warning: `subworkflows/local/prepare_genome/main.nf:42:5`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
      chrom_sizes        //    file: /path/to/genome.sizes
      ^^^^^^^^^^^
  ```

- Warning: `subworkflows/local/prepare_genome/main.nf:43:5`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
      fai                //    file: /path/to/genome.fai
      ^^^
  ```

- Warning: `subworkflows/local/prepare_genome/main.nf:44:5`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
      binsize            //    binsize: genome binning
      ^^^^^^^
  ```

- Warning: `subworkflows/local/prepare_genome/main.nf:47:19`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_versions = Channel.empty()
                    ^^^^^^^
  ```

- Warning: `subworkflows/local/prepare_genome/main.nf:52:16`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_fasta = Channel.empty()
                 ^^^^^^^
  ```

- Warning: `subworkflows/local/prepare_genome/main.nf:54:74`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          ch_fasta    = GUNZIP_FASTA ( [ [:], params.fasta ] ).gunzip.map{ it[1] }
                                                                           ^^
  ```

- Warning: `subworkflows/local/prepare_genome/main.nf:57:20`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
          ch_fasta = Channel.value(file(params.fasta))
                     ^^^^^^^
  ```

- Warning: `subworkflows/local/prepare_genome/main.nf:72:14`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_gtf = Channel.empty()
               ^^^^^^^
  ```

- Warning: `subworkflows/local/prepare_genome/main.nf:75:74`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
              ch_gtf      = GUNZIP_GTF ( [ [:], params.gtf ] ).gunzip.map{ it[1] }
                                                                           ^^
  ```

- Warning: `subworkflows/local/prepare_genome/main.nf:78:22`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
              ch_gtf = Channel.value(file(params.gtf))
                       ^^^^^^^
  ```

- Warning: `subworkflows/local/prepare_genome/main.nf:85:18`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_tss_bed = Channel.empty()
                   ^^^^^^^
  ```

- Warning: `subworkflows/local/prepare_genome/main.nf:88:81`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
              ch_tss_bed = GUNZIP_TSS_BED ( [ [:], params.tss_bed ] ).gunzip.map{ it[1] }
                                                                                  ^^
  ```

- Warning: `subworkflows/local/prepare_genome/main.nf:91:26`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
              ch_tss_bed = Channel.value(file(params.tss_bed))
                           ^^^^^^^
  ```

- Warning: `subworkflows/local/prepare_genome/main.nf:98:20`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_blacklist = Channel.empty()
                     ^^^^^^^
  ```

- Warning: `subworkflows/local/prepare_genome/main.nf:101:87`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
              ch_blacklist = GUNZIP_BLACKLIST ( [ [:], params.blacklist ] ).gunzip.map{ meta, file -> tuple([id: 'blacklist'], file) }
                                                                                        ^^^^
  ```

- Warning: `subworkflows/local/prepare_genome/main.nf:104:28`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
              ch_blacklist = Channel.value(tuple([id: 'blacklist'], file(params.blacklist)))
                             ^^^^^^^
  ```

- Warning: `subworkflows/local/prepare_genome/main.nf:111:14`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_fai = Channel.empty()
               ^^^^^^^
  ```

- Warning: `subworkflows/local/prepare_genome/main.nf:114:66`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
              ch_fai = GUNZIP_FAI([ [:], params.fai ]).gunzip.map{ it[1] }
                                                                   ^^
  ```

- Warning: `subworkflows/local/prepare_genome/main.nf:117:22`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
              ch_fai = Channel.value(file(params.fai))
                       ^^^^^^^
  ```

- Warning: `subworkflows/local/prepare_genome/main.nf:121:39`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
              ch_fasta.map { tuple([:], it) },
                                        ^^
  ```

- Warning: `subworkflows/local/prepare_genome/main.nf:125:51`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          ch_fai = SAMTOOLS_FAIDX_FAI.out.fai.map { it[1] }
                                                    ^^
  ```

- Warning: `subworkflows/local/prepare_genome/main.nf:132:22`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_chrom_sizes = Channel.empty()
                       ^^^^^^^
  ```

- Warning: `subworkflows/local/prepare_genome/main.nf:135:90`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
              ch_chrom_sizes = GUNZIP_CHROM_SIZES([ [:], params.chrom_sizes ]).gunzip.map{ it[1] }
                                                                                           ^^
  ```

- Warning: `subworkflows/local/prepare_genome/main.nf:138:30`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
              ch_chrom_sizes = Channel.value(file(params.chrom_sizes))
                               ^^^^^^^
  ```

- Warning: `subworkflows/local/prepare_genome/main.nf:142:39`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
              ch_fasta.map { tuple([:], it) },
                                        ^^
  ```

- Warning: `subworkflows/local/prepare_genome/main.nf:146:69`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          ch_chrom_sizes = SAMTOOLS_FAIDX_CHROM_SIZES.out.sizes.map { it[1] }
                                                                      ^^
  ```

- Warning: `subworkflows/local/prepare_genome/main.nf:154:30`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_genome_filtered_bed = Channel.empty()
                               ^^^^^^^
  ```

- Warning: `subworkflows/local/prepare_genome/main.nf:167:20`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_bwa_index = Channel.empty()
                     ^^^^^^^
  ```

- Warning: `subworkflows/local/prepare_genome/main.nf:177:62`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
              ch_bwa_index = BWA_INDEX ( ch_fasta.map { [ [:], it ] } ).index
                                                               ^^
  ```

- Warning: `subworkflows/local/prepare_genome/main.nf:185:24`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_bowtie2_index = Channel.empty()
                         ^^^^^^^
  ```

- Warning: `subworkflows/local/prepare_genome/main.nf:195:70`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
              ch_bowtie2_index = BOWTIE2_BUILD ( ch_fasta.map { [ [:], it ] } ).index
                                                                       ^^
  ```

- Warning: `subworkflows/local/utils_nfcore_sammyseq_pipeline/main.nf:32:5`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
      monochrome_logs   // boolean: Do not use coloured log outputs
      ^^^^^^^^^^^^^^^
  ```

- Warning: `subworkflows/local/utils_nfcore_sammyseq_pipeline/main.nf:35:5`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
      input             //  string: Path to input samplesheet
      ^^^^^
  ```

- Warning: `subworkflows/local/utils_nfcore_sammyseq_pipeline/main.nf:42:19`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_versions = Channel.empty()
                    ^^^^^^^
  ```

- Warning: `subworkflows/local/utils_nfcore_sammyseq_pipeline/main.nf:67:144`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
      after_text = """${workflow.manifest.doi ? "\n* The pipeline\n" : ""}${workflow.manifest.doi.tokenize(",").collect { "    https://doi.org/${it.trim().replace('https://doi.org/','')}"}.join("\n")}${workflow.manifest.doi ? "\n" : ""}
                                                                                                                                                 ^^
  ```

- Warning: `subworkflows/local/utils_nfcore_sammyseq_pipeline/main.nf:104:5`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      Channel
      ^^^^^^^
  ```

- Warning: `subworkflows/nf-core/bam_markduplicates_picard/main.nf:18:19`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_versions = Channel.empty()
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

- Warning: `subworkflows/nf-core/fastq_align_bwaaln/main.nf:18:19`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_versions = Channel.empty()
                    ^^^^^^^
  ```

- Warning: `subworkflows/nf-core/fastq_align_dna/main.nf:27:27`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
          ch_bam_index    = Channel.empty()
                            ^^^^^^^
  ```

- Warning: `subworkflows/nf-core/fastq_align_dna/main.nf:28:27`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
          ch_bam          = Channel.empty()
                            ^^^^^^^
  ```

- Warning: `subworkflows/nf-core/fastq_align_dna/main.nf:29:27`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
          ch_reports      = Channel.empty()
                            ^^^^^^^
  ```

- Warning: `subworkflows/nf-core/fastq_align_dna/main.nf:30:27`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
          ch_versions     = Channel.empty()
                            ^^^^^^^
  ```

- Warning: `subworkflows/nf-core/utils_nfcore_pipeline/main.nf:101:98`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      return ch_versions.unique().map { version -> processVersionsFromYAML(version) }.unique().mix(Channel.of(workflowVersionToYAML()))
                                                                                                   ^^^^^^^
  ```

- Warning: `workflows/sammyseq.nf:50:33`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
  if (params.fasta) { ch_fasta =  Channel.fromPath(params.fasta) } else { exit 1, 'Fasta reference genome not specified!' }
                                  ^^^^^^^
  ```

- Warning: `workflows/sammyseq.nf:53:1`: Variable was declared but not used

  ```nextflow
  ch_fasta_meta = ch_fasta.map{ it -> [[id:it[0].baseName], it] }.collect()
  ^^^^^^^^^^^^^
  ```

- Warning: `workflows/sammyseq.nf:61:1`: Variable was declared but not used

  ```nextflow
  ch_multiqc_config          = Channel.fromPath("$projectDir/assets/multiqc_config.yml", checkIfExists: true)
  ^^^^^^^^^^^^^^^^^
  ```

- Warning: `workflows/sammyseq.nf:61:30`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
  ch_multiqc_config          = Channel.fromPath("$projectDir/assets/multiqc_config.yml", checkIfExists: true)
                               ^^^^^^^
  ```

- Warning: `workflows/sammyseq.nf:62:1`: Variable was declared but not used

  ```nextflow
  ch_multiqc_custom_config   = params.multiqc_config ? Channel.fromPath( params.multiqc_config, checkIfExists: true ) : Channel.empty()
  ^^^^^^^^^^^^^^^^^^^^^^^^
  ```

- Warning: `workflows/sammyseq.nf:62:54`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
  ch_multiqc_custom_config   = params.multiqc_config ? Channel.fromPath( params.multiqc_config, checkIfExists: true ) : Channel.empty()
                                                       ^^^^^^^
  ```

- Warning: `workflows/sammyseq.nf:62:119`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
  ch_multiqc_custom_config   = params.multiqc_config ? Channel.fromPath( params.multiqc_config, checkIfExists: true ) : Channel.empty()
                                                                                                                        ^^^^^^^
  ```

- Warning: `workflows/sammyseq.nf:63:1`: Variable was declared but not used

  ```nextflow
  ch_multiqc_logo            = params.multiqc_logo   ? Channel.fromPath( params.multiqc_logo, checkIfExists: true ) : Channel.empty()
  ^^^^^^^^^^^^^^^
  ```

- Warning: `workflows/sammyseq.nf:63:54`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
  ch_multiqc_logo            = params.multiqc_logo   ? Channel.fromPath( params.multiqc_logo, checkIfExists: true ) : Channel.empty()
                                                       ^^^^^^^
  ```

- Warning: `workflows/sammyseq.nf:63:117`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
  ch_multiqc_logo            = params.multiqc_logo   ? Channel.fromPath( params.multiqc_logo, checkIfExists: true ) : Channel.empty()
                                                                                                                      ^^^^^^^
  ```

- Warning: `workflows/sammyseq.nf:64:1`: Variable was declared but not used

  ```nextflow
  ch_multiqc_custom_methods_description = params.multiqc_methods_description ? file(params.multiqc_methods_description, checkIfExists: true) : file("$projectDir/assets/methods_description_template.yml", checkIfExists: true)
  ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  ```

- Warning: `workflows/sammyseq.nf:79:19`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_versions = Channel.empty()
                    ^^^^^^^
  ```

- Warning: `workflows/sammyseq.nf:80:24`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_multiqc_files = Channel.empty()
                         ^^^^^^^
  ```

- Warning: `workflows/sammyseq.nf:146:17`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_trimmed= Channel.empty()
                  ^^^^^^^
  ```

- Warning: `workflows/sammyseq.nf:176:68`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
      ch_multiqc_files = ch_multiqc_files.mix(FASTQC.out.zip.collect{it[1]})
                                                                     ^^
  ```

- Warning: `workflows/sammyseq.nf:183:22`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_aligned_bam = Channel.empty()
                       ^^^^^^^
  ```

- Warning: `workflows/sammyseq.nf:225:59`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          PREPARE_GENOME.out.fai.collect { [ [id: 'fasta'], it ] }
                                                            ^^
  ```

- Warning: `workflows/sammyseq.nf:229:5`: Variable was declared but not used

  ```nextflow
      ch_mle_in = BAM_MARKDUPLICATES_PICARD.out.bam
      ^^^^^^^^^
  ```

- Warning: `workflows/sammyseq.nf:258:48`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
      ch_fai_path = PREPARE_GENOME.out.fai.map { it[1] }
                                                 ^^
  ```

- Warning: `workflows/sammyseq.nf:260:41`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
      ch_fasta_path = ch_fasta_meta.map { it[1] }
                                          ^^
  ```

- Warning: `workflows/sammyseq.nf:267:59`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
          params.blacklist ? PREPARE_GENOME.out.blacklist : Channel.value(tuple([ id:'no_blacklist' ], []))
                                                            ^^^^^^^
  ```

- Warning: `workflows/sammyseq.nf:280:55`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      params.blacklist ? PREPARE_GENOME.out.blacklist : Channel.value(tuple([ id:'no_blacklist' ], []))
                                                        ^^^^^^^
  ```

- Warning: `workflows/sammyseq.nf:282:5`: Variable was declared but not used

  ```nextflow
      ch_dt_corrmatrix     = DEEPTOOLS_QC.out.correlation_matrix
      ^^^^^^^^^^^^^^^^
  ```

- Warning: `workflows/sammyseq.nf:283:5`: Variable was declared but not used

  ```nextflow
      ch_dt_pcadata        = DEEPTOOLS_QC.out.pca_data
      ^^^^^^^^^^^^^
  ```

- Warning: `workflows/sammyseq.nf:285:9`: Variable was declared but not used

  ```nextflow
          ch_dt_fpmatrix_global = DEEPTOOLS_QC.out.fingerprint_matrix_global
          ^^^^^^^^^^^^^^^^^^^^^
  ```

- Warning: `workflows/sammyseq.nf:286:9`: Variable was declared but not used

  ```nextflow
          ch_dt_fpmetrics_global = DEEPTOOLS_QC.out.fingerprint_metrics_global
          ^^^^^^^^^^^^^^^^^^^^^^
  ```

- Warning: `workflows/sammyseq.nf:288:13`: Variable was declared but not used

  ```nextflow
              ch_dt_fpmatrix_region = DEEPTOOLS_QC.out.fingerprint_matrix_region
              ^^^^^^^^^^^^^^^^^^^^^
  ```

- Warning: `workflows/sammyseq.nf:289:13`: Variable was declared but not used

  ```nextflow
              ch_dt_fpmetrics_region = DEEPTOOLS_QC.out.fingerprint_metrics_region
              ^^^^^^^^^^^^^^^^^^^^^^
  ```

- Warning: `workflows/sammyseq.nf:299:44`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
                  def sorted = values.sort { it[1].getBaseName() }
                                             ^^
  ```

- Warning: `workflows/sammyseq.nf:300:50`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
                  def sorted_bw = sorted.collect { it[1] }
                                                   ^^
  ```

- Warning: `workflows/sammyseq.nf:301:54`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
                  def sorted_labels = sorted.collect { it[0].id }
                                                       ^^
  ```

- Warning: `workflows/sammyseq.nf:328:24`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
                  .map { meta, bed -> bed }
                         ^^^^
  ```

- Warning: `workflows/sammyseq.nf:340:33`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
          ch_comparison_results = Channel.empty()
                                  ^^^^^^^
  ```

- Warning: `workflows/sammyseq.nf:395:32`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_multiqc_config        = Channel.fromPath(
                                 ^^^^^^^
  ```

- Warning: `workflows/sammyseq.nf:398:9`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
          Channel.fromPath(params.multiqc_config, checkIfExists: true) :
          ^^^^^^^
  ```

- Warning: `workflows/sammyseq.nf:399:9`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
          Channel.empty()
          ^^^^^^^
  ```

- Warning: `workflows/sammyseq.nf:401:9`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
          Channel.fromPath(params.multiqc_logo, checkIfExists: true) :
          ^^^^^^^
  ```

- Warning: `workflows/sammyseq.nf:402:9`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
          Channel.empty()
          ^^^^^^^
  ```

- Warning: `workflows/sammyseq.nf:406:27`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_workflow_summary = Channel.value(paramsSummaryMultiqc(summary_params))
                            ^^^^^^^
  ```

- Warning: `workflows/sammyseq.nf:412:45`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_methods_description                = Channel.value(
                                              ^^^^^^^
  ```

- Warning: `workflows/sammyseq.nf:424:91`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
      ch_multiqc_files = ch_multiqc_files.mix(BAM_MARKDUPLICATES_PICARD.out.metrics.collect{it[1]}.ifEmpty([]))
                                                                                            ^^
  ```

- Warning: `workflows/sammyseq.nf:428:83`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
      ch_multiqc_files = ch_multiqc_files.mix(FILTER_BAM_SAMTOOLS.out.stats.collect{it[1]}.ifEmpty([]))
                                                                                    ^^
  ```

- Warning: `workflows/sammyseq.nf:429:86`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
      ch_multiqc_files = ch_multiqc_files.mix(FILTER_BAM_SAMTOOLS.out.flagstat.collect{it[1]}.ifEmpty([]))
                                                                                       ^^
  ```

- Warning: `workflows/sammyseq.nf:430:86`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
      ch_multiqc_files = ch_multiqc_files.mix(FILTER_BAM_SAMTOOLS.out.idxstats.collect{it[1]}.ifEmpty([]))
                                                                                       ^^
  ```

- Warning: `workflows/sammyseq.nf:432:89`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
      ch_multiqc_files = ch_multiqc_files.mix(DEEPTOOLS_QC.out.correlation_matrix.collect{it[1]}.ifEmpty([]))
                                                                                          ^^
  ```

- Warning: `workflows/sammyseq.nf:433:79`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
      ch_multiqc_files = ch_multiqc_files.mix(DEEPTOOLS_QC.out.pca_data.collect{it[1]}.ifEmpty([]))
                                                                                ^^
  ```

- Warning: `workflows/sammyseq.nf:436:100`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          ch_multiqc_files = ch_multiqc_files.mix(DEEPTOOLS_QC.out.fingerprint_matrix_global.collect{it[1]}.ifEmpty([]))
                                                                                                     ^^
  ```

- Warning: `workflows/sammyseq.nf:437:101`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          ch_multiqc_files = ch_multiqc_files.mix(DEEPTOOLS_QC.out.fingerprint_metrics_global.collect{it[1]}.ifEmpty([]))
                                                                                                      ^^
  ```

- Warning: `workflows/sammyseq.nf:441:100`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          ch_multiqc_files  = ch_multiqc_files.mix(BIGWIG_PLOT_DEEPTOOLS.out.plotprofile_pdf.collect{it[1]}.ifEmpty([]))
                                                                                                     ^^
  ```

- Warning: `workflows/sammyseq.nf:442:102`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          ch_multiqc_files  = ch_multiqc_files.mix(BIGWIG_PLOT_DEEPTOOLS.out.plotprofile_table.collect{it[1]}.ifEmpty([]))
                                                                                                       ^^
  ```

- Warning: `workflows/sammyseq.nf:455:75`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      multiqc_report = !params.skip_multiqc ? MULTIQC.out.report.toList() : Channel.empty() // channel: /path/to/multiqc_report.html
                                                                            ^^^^^^^
  ```
