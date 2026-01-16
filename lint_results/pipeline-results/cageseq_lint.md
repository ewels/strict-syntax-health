# Nextflow lint results

- Generated: 2026-01-16T10:17:46.544168669Z
- Nextflow version: 25.12.0-edge
- Summary: 62 errors, 69 warnings

## :x: Errors

- Error: `modules/local/cagefightr/enhancer_calling/main.nf:18:5`: The `script:` or `exec:` label is required when other sections are present

  ```nextflow
      """
      ^
  ```

- Error: `modules/local/cager/processing/main.nf:21:5`: The `script:` or `exec:` label is required when other sections are present

  ```nextflow
      """
      ^
  ```

- Error: `modules/local/cager/readin/main.nf:18:5`: The `script:` or `exec:` label is required when other sections are present

  ```nextflow
      """
      ^
  ```

- Error: `modules/local/cager/report/main.nf:20:5`: The `script:` or `exec:` label is required when other sections are present

  ```nextflow
      """
      ^
  ```

- Error: `modules/local/cager/tag_qc/main.nf:21:5`: The `script:` or `exec:` label is required when other sections are present

  ```nextflow
      """
      ^
  ```

- Error: `modules/local/cager/tagcluster_qc/main.nf:21:5`: The `script:` or `exec:` label is required when other sections are present

  ```nextflow
      """
      ^
  ```

- Error: `modules/local/forge_bsgenome/main.nf:13:5`: The `script:` or `exec:` label is required when other sections are present

  ```nextflow
      """
      ^
  ```

- Error: `modules/local/gtf2txdb/main.nf:12:5`: The `script:` or `exec:` label is required when other sections are present

  ```nextflow
      """
      ^
  ```

- Error: `modules/local/relativisation/main.nf:15:5`: The `script:` or `exec:` label is required when other sections are present

  ```nextflow
      """
      ^
  ```

- Error: `modules/local/write_sample_list/main.nf:16:48`: `PWD` is not defined

  ```nextflow
          line="${meta.id},${meta.single_end},[${PWD}/${params.outdir}/bigwig/${bw_or_bam[0]} ${PWD}/${params.outdir}/bigwig/${bw_or_bam[1]}],${meta.id}"
                                                 ^^^
  ```

- Error: `modules/local/write_sample_list/main.nf:16:95`: `PWD` is not defined

  ```nextflow
          line="${meta.id},${meta.single_end},[${PWD}/${params.outdir}/bigwig/${bw_or_bam[0]} ${PWD}/${params.outdir}/bigwig/${bw_or_bam[1]}],${meta.id}"
                                                                                                ^^^
  ```

- Error: `modules/local/write_sample_list/main.nf:21:47`: `PWD` is not defined

  ```nextflow
          line="${meta.id},${meta.single_end},${PWD}/${params.outdir}/samtools_sort/${bw_or_bam[0]},${meta.id}"
                                                ^^^
  ```

- Error: `modules/nf-core/samtools/view/main.nf:64:9`: `index` is already declared

  ```nextflow
      def index = args.contains("--write-index") ? "touch ${prefix}.csi" : ""
          ^^^^^
  ```

- Error: `modules/nf-core/star/align/main.nf:44:20`: Unexpected input: ','

  ```nextflow
      def reads1 = [], reads2 = []
                     ^
  ```

- Error: `subworkflows/local/cager/main.nf:93:5`: `id` was assigned but not declared

  ```nextflow
      id = row.id
      ^^
  ```

- Error: `subworkflows/local/cager/main.nf:94:5`: `single_end` was assigned but not declared

  ```nextflow
      single_end = row.single_end
      ^^^^^^^^^^
  ```

- Error: `subworkflows/local/cager/main.nf:95:5`: `str1_bw` was assigned but not declared

  ```nextflow
      str1_bw = row.path.split(" ")[0].minus('[')
      ^^^^^^^
  ```

- Error: `subworkflows/local/cager/main.nf:96:5`: `new_name` was assigned but not declared

  ```nextflow
      new_name = row.new_name
      ^^^^^^^^
  ```

- Error: `subworkflows/local/cager/main.nf:97:9`: `str1_bw` is not defined

  ```nextflow
      if (str1_bw.split("\\.")[-1].minus(']') != "bam") {
          ^^^^^^^
  ```

- Error: `subworkflows/local/cager/main.nf:98:9`: `str2_bw` was assigned but not declared

  ```nextflow
          str2_bw = row.path.split(" ")[1].minus(']')
          ^^^^^^^
  ```

- Error: `subworkflows/local/cager/main.nf:99:17`: `id` is not defined

  ```nextflow
          return [id, single_end, str1_bw, str2_bw, new_name]
                  ^^
  ```

- Error: `subworkflows/local/cager/main.nf:99:21`: `single_end` is not defined

  ```nextflow
          return [id, single_end, str1_bw, str2_bw, new_name]
                      ^^^^^^^^^^
  ```

- Error: `subworkflows/local/cager/main.nf:99:33`: `str1_bw` is not defined

  ```nextflow
          return [id, single_end, str1_bw, str2_bw, new_name]
                                  ^^^^^^^
  ```

- Error: `subworkflows/local/cager/main.nf:99:42`: `str2_bw` is not defined

  ```nextflow
          return [id, single_end, str1_bw, str2_bw, new_name]
                                           ^^^^^^^
  ```

- Error: `subworkflows/local/cager/main.nf:99:51`: `new_name` is not defined

  ```nextflow
          return [id, single_end, str1_bw, str2_bw, new_name]
                                                    ^^^^^^^^
  ```

- Error: `subworkflows/local/cager/main.nf:101:13`: `id` is not defined

  ```nextflow
      return [id, single_end, str1_bw, new_name]
              ^^
  ```

- Error: `subworkflows/local/cager/main.nf:101:17`: `single_end` is not defined

  ```nextflow
      return [id, single_end, str1_bw, new_name]
                  ^^^^^^^^^^
  ```

- Error: `subworkflows/local/cager/main.nf:101:29`: `str1_bw` is not defined

  ```nextflow
      return [id, single_end, str1_bw, new_name]
                              ^^^^^^^
  ```

- Error: `subworkflows/local/cager/main.nf:101:38`: `new_name` is not defined

  ```nextflow
      return [id, single_end, str1_bw, new_name]
                                       ^^^^^^^^
  ```

- Error: `subworkflows/local/input_from_folder/main.nf:30:17`: Variables in a closure should be declared with `def`

  ```nextflow
                  num_fields_of_interest = "$params.sample_name_fields".toInteger()
                  ^^^^^^^^^^^^^^^^^^^^^^
  ```

- Error: `subworkflows/local/input_from_folder/main.nf:31:17`: Variables in a closure should be declared with `def`

  ```nextflow
                  split_field_num = old_meta.split('_').size()
                  ^^^^^^^^^^^^^^^
  ```

- Error: `subworkflows/local/input_from_folder/main.nf:33:21`: Variables in a closure should be declared with `def`

  ```nextflow
                      sample_name = old_meta
                      ^^^^^^^^^^^
  ```

- Error: `subworkflows/local/input_from_folder/main.nf:34:21`: Variables in a closure should be declared with `def`

  ```nextflow
                      lane_n_fastq = tuple(fastq.name, fastq)
                      ^^^^^^^^^^^^
  ```

- Error: `subworkflows/local/input_from_folder/main.nf:36:21`: Variables in a closure should be declared with `def`

  ```nextflow
                      num_fields_to_cut = split_field_num - num_fields_of_interest
                      ^^^^^^^^^^^^^^^^^
  ```

- Error: `subworkflows/local/input_from_folder/main.nf:46:19`: `lane_n_fastq` is already declared

  ```nextflow
              meta, lane_n_fastq ->
                    ^^^^^^^^^^^^
  ```

- Error: `subworkflows/local/input_from_folder/main.nf:48:17`: Variables in a closure should be declared with `def`

  ```nextflow
                  fastq = lane_n_fastq*.getAt(1).flatten()
                  ^^^^^
  ```

- Error: `subworkflows/local/mapped_inputs/main.nf:19:5`: `files_in` was assigned but not declared

  ```nextflow
      files_in = row.path
      ^^^^^^^^
  ```

- Error: `subworkflows/local/mapped_inputs/main.nf:20:5`: `files` was assigned but not declared

  ```nextflow
      files = files_in.split(' ')
      ^^^^^
  ```

- Error: `subworkflows/local/mapped_inputs/main.nf:20:13`: `files_in` is not defined

  ```nextflow
      files = files_in.split(' ')
              ^^^^^^^^
  ```

- Error: `subworkflows/local/mapped_inputs/main.nf:21:9`: `files` is not defined

  ```nextflow
      if (files.size() == 2){
          ^^^^^
  ```

- Error: `subworkflows/local/mapped_inputs/main.nf:22:9`: `bigwig_1` was assigned but not declared

  ```nextflow
          bigwig_1 = file(files[0].minus('['))
          ^^^^^^^^
  ```

- Error: `subworkflows/local/mapped_inputs/main.nf:22:25`: `files` is not defined

  ```nextflow
          bigwig_1 = file(files[0].minus('['))
                          ^^^^^
  ```

- Error: `subworkflows/local/mapped_inputs/main.nf:23:9`: `bigwig_2` was assigned but not declared

  ```nextflow
          bigwig_2 = file(files[1].minus(']'))
          ^^^^^^^^
  ```

- Error: `subworkflows/local/mapped_inputs/main.nf:23:25`: `files` is not defined

  ```nextflow
          bigwig_2 = file(files[1].minus(']'))
                          ^^^^^
  ```

- Error: `subworkflows/local/mapped_inputs/main.nf:24:17`: `bigwig_1` is not defined

  ```nextflow
          return [bigwig_1, bigwig_2]
                  ^^^^^^^^
  ```

- Error: `subworkflows/local/mapped_inputs/main.nf:24:27`: `bigwig_2` is not defined

  ```nextflow
          return [bigwig_1, bigwig_2]
                            ^^^^^^^^
  ```

- Error: `subworkflows/local/mapped_inputs/main.nf:25:16`: `files` is not defined

  ```nextflow
      } else if (files.size() == 1){
                 ^^^^^
  ```

- Error: `subworkflows/local/mapped_inputs/main.nf:26:9`: `bam` was assigned but not declared

  ```nextflow
          bam = file(files[0].minus('[').minus(']'))
          ^^^
  ```

- Error: `subworkflows/local/mapped_inputs/main.nf:26:20`: `files` is not defined

  ```nextflow
          bam = file(files[0].minus('[').minus(']'))
                     ^^^^^
  ```

- Error: `subworkflows/local/mapped_inputs/main.nf:27:17`: `bam` is not defined

  ```nextflow
          return [bam]
                  ^^^
  ```

- Error: `subworkflows/local/star/main.nf:5:1`: Module could not be parsed: '/home/runner/work/strict-syntax-health/strict-syntax-health/pipelines/cageseq/modules/nf-core/star/align/main.nf'

  ```nextflow
  include { STAR_ALIGN } from '../../../modules/nf-core/star/align/main.nf'
  ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  ```

- Error: `subworkflows/local/star/main.nf:37:9`: `STAR_ALIGN` is not defined

  ```nextflow
          STAR_ALIGN (
          ^^^^^^^^^^
  ```

- Error: `subworkflows/local/star/main.nf:45:39`: `STAR_ALIGN` is not defined

  ```nextflow
          ch_versions = ch_versions.mix(STAR_ALIGN.out.versions)
                                        ^^^^^^^^^^
  ```

- Error: `subworkflows/local/star/main.nf:47:22`: `STAR_ALIGN` is not defined

  ```nextflow
          ch_aligned = STAR_ALIGN.out.bam_sorted_aligned
                       ^^^^^^^^^^
  ```

- Error: `subworkflows/local/star/main.nf:49:49`: `STAR_ALIGN` is not defined

  ```nextflow
          ch_multiqc_files = ch_multiqc_files.mix(STAR_ALIGN.out.log_final.collect{it[1]})
                                                  ^^^^^^^^^^
  ```

- Error: `subworkflows/local/star/main.nf:55:16`: `STAR_ALIGN` is not defined

  ```nextflow
          wigs = STAR_ALIGN.out.wig
                 ^^^^^^^^^^
  ```

- Error: `subworkflows/local/star/main.nf:57:51`: `wigs` is already declared

  ```nextflow
              wigs_for_conversion = wigs.map{ meta, wigs ->
                                                    ^^^^
  ```

- Error: `subworkflows/local/star/main.nf:59:17`: Variables in a closure should be declared with `def`

  ```nextflow
                  wigs_to_use = [wigs[0], wigs[1]]
                  ^^^^^^^^^^^
  ```

- Error: `subworkflows/local/star/main.nf:63:51`: `wigs` is already declared

  ```nextflow
              wigs_for_conversion = wigs.map{ meta, wigs ->
                                                    ^^^^
  ```

- Error: `workflows/customcage.nf:98:1`: Statements cannot be mixed with script declarations -- move statements into a process, workflow, or function

  ```nextflow
  def multiqc_report = []
  ^^^^^^^^^^^^^^^^^^^^^^^
  ```

- Error: `workflows/customcage.nf:194:17`: Variables in a closure should be declared with `def`

  ```nextflow
                  file1 = paths[0]
                  ^^^^^
  ```

- Error: `workflows/customcage.nf:195:17`: Variables in a closure should be declared with `def`

  ```nextflow
                  file2 = paths[1]
                  ^^^^^
  ```

## :warning: Warnings

- Warning: `modules/local/cagefightr/enhancer_calling/main.nf:29:25`: The use of `projectDir` in a process is discouraged -- input files should be provided as process inputs

  ```nextflow
          --project_dir ${projectDir}
                          ^^^^^^^^^^
  ```

- Warning: `modules/local/cager/processing/main.nf:46:25`: The use of `projectDir` in a process is discouraged -- input files should be provided as process inputs

  ```nextflow
          --project_dir ${projectDir} \
                          ^^^^^^^^^^
  ```

- Warning: `modules/local/cager/readin/main.nf:30:25`: The use of `projectDir` in a process is discouraged -- input files should be provided as process inputs

  ```nextflow
          --project_dir ${projectDir} \
                          ^^^^^^^^^^
  ```

- Warning: `modules/local/cager/tag_qc/main.nf:35:25`: The use of `projectDir` in a process is discouraged -- input files should be provided as process inputs

  ```nextflow
          --project_dir ${projectDir}
                          ^^^^^^^^^^
  ```

- Warning: `modules/local/cager/tagcluster_qc/main.nf:39:25`: The use of `projectDir` in a process is discouraged -- input files should be provided as process inputs

  ```nextflow
          --project_dir ${projectDir} \
                          ^^^^^^^^^^
  ```

- Warning: `modules/local/samtools/dedup/main.nf:33:9`: Variable was declared but not used

  ```nextflow
      def args = task.ext.args ?: ''
          ^^^^
  ```

- Warning: `modules/local/samtools/view_mapq/main.nf:37:9`: Variable was declared but not used

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

- Warning: `modules/nf-core/samtools/idxstats/main.nf:16:9`: Variable was declared but not used

  ```nextflow
      def args = task.ext.args ?: ''
          ^^^^
  ```

- Warning: `modules/nf-core/samtools/stats/main.nf:22:9`: Variable was declared but not used

  ```nextflow
      def args = task.ext.args ?: ''
          ^^^^
  ```

- Warning: `modules/nf-core/trimgalore/main.nf:41:31`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          args_list.removeAll { it.toLowerCase().contains('_r2 ') }
                                ^^
  ```

- Warning: `subworkflows/local/bowtie2/main.nf:19:52`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          sample_meta = ch_reads_to_align.map{ meta, fastq ->
                                                     ^^^^^
  ```

- Warning: `subworkflows/local/bowtie2/main.nf:28:74`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
              ch_index = sample_meta.combine(BOWTIE2_BUILD.out.index.map { genome_name, index -> index } )
                                                                           ^^^^^^^^^^^
  ```

- Warning: `subworkflows/local/bowtie2/main.nf:30:59`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
              ch_index = sample_meta.combine(ch_index.map { genome_name, index -> index })
                                                            ^^^^^^^^^^^
  ```

- Warning: `subworkflows/local/bowtie2/main.nf:34:59`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
              ch_fasta = sample_meta.combine(ch_fasta.map { genome_name, fasta -> fasta } )
                                                            ^^^^^^^^^^^
  ```

- Warning: `subworkflows/local/bowtie2/main.nf:46:79`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          ch_multiqc_files = ch_multiqc_files.mix(BOWTIE2_ALIGN.out.log.collect{it[1]})
                                                                                ^^
  ```

- Warning: `subworkflows/local/cager/main.nf:26:28`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
              ch_data_type = Channel.of("bam")
                             ^^^^^^^
  ```

- Warning: `subworkflows/local/cager/main.nf:28:28`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
              ch_data_type = Channel.of(params.datatype)
                             ^^^^^^^
  ```

- Warning: `subworkflows/local/cager/main.nf:33:43`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
              .map { create_mapping_channel(it) }
                                            ^^
  ```

- Warning: `subworkflows/local/cager/main.nf:74:23`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
          ch_template = Channel.fromPath(params.markdown_path)
                        ^^^^^^^
  ```

- Warning: `subworkflows/local/mapped_inputs/main.nf:12:38`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          .map { create_sample_channel(it) }
                                       ^^
  ```

- Warning: `subworkflows/local/parameter_checks/main.nf:24:29`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
              input_handler = Channel.fromPath(params.input, checkIfExists: true)
                              ^^^^^^^
  ```

- Warning: `subworkflows/local/parameter_checks/main.nf:30:45`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
                  .map { create_fastq_channel(it) }
                                              ^^
  ```

- Warning: `subworkflows/local/parameter_checks/main.nf:44:43`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          sample_meta = ch_fastq.map{ meta, fastq ->
                                            ^^^^^
  ```

- Warning: `subworkflows/local/parameter_checks/main.nf:48:26`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
          ch_genome_name = Channel.of(params.genome_name)
                           ^^^^^^^
  ```

- Warning: `subworkflows/local/parameter_checks/main.nf:54:26`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
              ch_pre_idx = Channel.fromPath(params.index, checkIfExists: true)
                           ^^^^^^^
  ```

- Warning: `subworkflows/local/parameter_checks/main.nf:57:29`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
                  ch_pre_fa = Channel.fromPath(params.genome, checkIfExists: true)
                              ^^^^^^^
  ```

- Warning: `subworkflows/local/parameter_checks/main.nf:60:28`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
                  ch_fasta = Channel.empty()
                             ^^^^^^^
  ```

- Warning: `subworkflows/local/parameter_checks/main.nf:63:25`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
              ch_pre_fa = Channel.fromPath(params.genome, checkIfExists: true)
                          ^^^^^^^
  ```

- Warning: `subworkflows/local/parameter_checks/main.nf:65:24`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
              ch_index = Channel.empty()
                         ^^^^^^^
  ```

- Warning: `subworkflows/local/prepare_cager_metadata/main.nf:43:9`: Variable was declared but not used

  ```nextflow
          ch_txdb = GTF2TXDB(ch_gtf)
          ^^^^^^^
  ```

- Warning: `subworkflows/local/prepare_mapping_metadata/main.nf:18:43`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
              chrom_size_fa = ch_fasta.map{ meta, fasta ->
                                            ^^^^
  ```

- Warning: `subworkflows/local/prepare_mapping_metadata/main.nf:32:30`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
              ch_chrom_sizes = Channel.of([
                               ^^^^^^^
  ```

- Warning: `subworkflows/local/preprocessing/main.nf:45:72`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          ch_multiqc_files = ch_multiqc_files.mix(FASTQC.out.zip.collect{it[1]}.ifEmpty([]))
                                                                         ^^
  ```

- Warning: `subworkflows/local/preprocessing/main.nf:46:76`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          ch_multiqc_files = ch_multiqc_files.mix(TRIMGALORE.out.log.collect{it[1]}.ifEmpty([]))
                                                                             ^^
  ```

- Warning: `subworkflows/local/preprocessing/main.nf:47:76`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          ch_multiqc_files = ch_multiqc_files.mix(TRIMGALORE.out.zip.collect{it[1]}.ifEmpty([]))
                                                                             ^^
  ```

- Warning: `subworkflows/local/samtools_statistics/main.nf:20:23`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
                  .map{[it[3], it[4]]}
                        ^^
  ```

- Warning: `subworkflows/local/samtools_statistics/main.nf:20:30`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
                  .map{[it[3], it[4]]}
                               ^^
  ```

- Warning: `subworkflows/local/samtools_statistics/main.nf:27:23`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
                  .map{[it[3], it[4]]}
                        ^^
  ```

- Warning: `subworkflows/local/samtools_statistics/main.nf:27:30`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
                  .map{[it[3], it[4]]}
                               ^^
  ```

- Warning: `subworkflows/local/samtools_statistics/main.nf:36:82`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          ch_multiqc_files = ch_multiqc_files.mix(SAMTOOLS_STATS.out.stats.collect{it[1]})
                                                                                   ^^
  ```

- Warning: `subworkflows/local/samtools_statistics/main.nf:40:88`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          ch_multiqc_files = ch_multiqc_files.mix(SAMTOOLS_FLAGSTAT.out.flagstat.collect{it[1]})
                                                                                         ^^
  ```

- Warning: `subworkflows/local/samtools_statistics/main.nf:44:88`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          ch_multiqc_files = ch_multiqc_files.mix(SAMTOOLS_IDXSTATS.out.idxstats.collect{it[1]})
                                                                                         ^^
  ```

- Warning: `subworkflows/local/star/main.nf:22:26`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
          ch_genome_name = Channel.of(params.genome_name)
                           ^^^^^^^
  ```

- Warning: `subworkflows/local/star/main.nf:24:52`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          sample_meta = ch_reads_to_align.map{ meta, fastq ->
                                                     ^^^^^
  ```

- Warning: `subworkflows/local/star/main.nf:34:80`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
              ch_index = sample_meta.combine(STAR_GENOMEGENERATE.out.index.map { it[1] })
                                                                                 ^^
  ```

- Warning: `subworkflows/local/star/main.nf:49:82`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          ch_multiqc_files = ch_multiqc_files.mix(STAR_ALIGN.out.log_final.collect{it[1]})
                                                                                   ^^
  ```

- Warning: `subworkflows/local/star/main.nf:51:53`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          ch_chrom_sizes_for_wig = ch_chrom_sizes.map{meta, sizes ->
                                                      ^^^^
  ```

- Warning: `subworkflows/local/utils_nfcore_customcage_pipeline/main.nf:28:5`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
      monochrome_logs   // boolean: Do not use coloured log outputs
      ^^^^^^^^^^^^^^^
  ```

- Warning: `subworkflows/local/utils_nfcore_customcage_pipeline/main.nf:34:19`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_versions = Channel.empty()
                    ^^^^^^^
  ```

- Warning: `subworkflows/local/utils_nfcore_customcage_pipeline/main.nf:80:5`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
      hook_url        //  string: hook URL for notifications
      ^^^^^^^^
  ```

- Warning: `subworkflows/local/utils_nfcore_customcage_pipeline/main.nf:81:5`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
      multiqc_report  //  string: Path to MultiQC report
      ^^^^^^^^^^^^^^
  ```

- Warning: `subworkflows/nf-core/utils_nfcore_pipeline/main.nf:101:98`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      return ch_versions.unique().map { version -> processVersionsFromYAML(version) }.unique().mix(Channel.of(workflowVersionToYAML()))
                                                                                                   ^^^^^^^
  ```

- Warning: `workflows/customcage.nf:98:5`: Variable was declared but not used

  ```nextflow
  def multiqc_report = []
      ^^^^^^^^^^^^^^
  ```

- Warning: `workflows/customcage.nf:108:22`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
              ch_gtf = Channel.fromPath(params.gtf, checkIfExists: true)
                       ^^^^^^^
  ```

- Warning: `workflows/customcage.nf:119:32`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
          ch_cager_sample_file = Channel.fromPath(params.cager_sample_file)
                                 ^^^^^^^
  ```

- Warning: `workflows/customcage.nf:125:24`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_multiqc_files = Channel.empty()
                         ^^^^^^^
  ```

- Warning: `workflows/customcage.nf:129:20`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
          ch_fasta = Channel.empty()
                     ^^^^^^^
  ```

- Warning: `workflows/customcage.nf:130:20`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
          ch_index = Channel.empty()
                     ^^^^^^^
  ```

- Warning: `workflows/customcage.nf:189:49`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
              mapped_files_ch = ch_for_cager.map{ meta, paths ->
                                                  ^^^^
  ```

- Warning: `workflows/customcage.nf:193:49`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
              mapped_files_ch = ch_for_cager.map{ meta, paths ->
                                                  ^^^^
  ```

- Warning: `workflows/customcage.nf:252:32`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_multiqc_config        = Channel.fromPath(
                                 ^^^^^^^
  ```

- Warning: `workflows/customcage.nf:255:9`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
          Channel.fromPath(params.multiqc_config, checkIfExists: true) :
          ^^^^^^^
  ```

- Warning: `workflows/customcage.nf:256:9`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
          Channel.empty()
          ^^^^^^^
  ```

- Warning: `workflows/customcage.nf:258:9`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
          Channel.fromPath(params.multiqc_logo, checkIfExists: true) :
          ^^^^^^^
  ```

- Warning: `workflows/customcage.nf:259:9`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
          Channel.empty()
          ^^^^^^^
  ```

- Warning: `workflows/customcage.nf:263:27`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_workflow_summary = Channel.value(paramsSummaryMultiqc(summary_params))
                            ^^^^^^^
  ```

- Warning: `workflows/customcage.nf:269:45`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_methods_description                = Channel.value(
                                              ^^^^^^^
  ```
