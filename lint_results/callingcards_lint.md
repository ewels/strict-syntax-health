# Nextflow lint results

- Generated: 2026-01-14T09:09:55.460750279Z
- Nextflow version: 25.12.0-edge
- Summary: 41 errors, 168 warnings

## :x: Errors

- Error: `conf/modules.config:87:17`: Unexpected input: ':'

  ```nextflow
          withName: FASTQC {
                  ^
  ```

- Error: `main.nf:34:1`: Statements cannot be mixed with script declarations -- move statements into a process or workflow

  ```nextflow
  if (params.datatype == 'yeast'){
  ^
  ```

- Error: `main.nf:49:1`: Statements cannot be mixed with script declarations -- move statements into a process or workflow

  ```nextflow
  if (params.genome == 'GRCm38'){
  ^
  ```

- Error: `main.nf:55:1`: Statements cannot be mixed with script declarations -- move statements into a process or workflow

  ```nextflow
  if(!params.containsKey('regions_mask')){
  ^
  ```

- Error: `main.nf:60:1`: Statements cannot be mixed with script declarations -- move statements into a process or workflow

  ```nextflow
  if(!params.containsKey('additional_fasta')){
  ^
  ```

- Error: `main.nf:65:1`: Statements cannot be mixed with script declarations -- move statements into a process or workflow

  ```nextflow
  if (!params.containsKey('fasta_index')){
  ^
  ```

- Error: `main.nf:73:1`: Statements cannot be mixed with script declarations -- move statements into a process or workflow

  ```nextflow
  if(!params.containsKey('bwa_index')){
  ^
  ```

- Error: `main.nf:76:1`: Statements cannot be mixed with script declarations -- move statements into a process or workflow

  ```nextflow
  if(!params.containsKey('bwamem2_index')){
  ^
  ```

- Error: `main.nf:79:1`: Statements cannot be mixed with script declarations -- move statements into a process or workflow

  ```nextflow
  if(!params.containsKey('bowtie_index')){
  ^
  ```

- Error: `main.nf:82:1`: Statements cannot be mixed with script declarations -- move statements into a process or workflow

  ```nextflow
  if(!params.containsKey('bowtie2_index')){
  ^
  ```

- Error: `modules/local/callingcardstools/mammals/concatQC/main.nf:12:15`: `meta` is already declared

  ```nextflow
      tuple val(meta), path(barcode_qc_files)
                ^^^^
  ```

- Error: `modules/nf-core/bwa/index/main.nf:14:27`: `bwa` is not defined

  ```nextflow
      tuple val(meta), path(bwa) , emit: index
                            ^^^
  ```

- Error: `nextflow.config:312:14`: Unexpected input: '('

  ```nextflow
  def check_max(obj, type) {
               ^
  ```

- Error: `subworkflows/local/align.nf:7:37`: Unexpected input: '"'

  ```nextflow
  include { SAMTOOLS_SORT      } from "${projectDir}/modules/nf-core/samtools/sort/main"
                                      ^
  ```

- Error: `subworkflows/local/mammals/process_alignments.nf:33:25`: `fasta` is already declared

  ```nextflow
          fasta.map{meta, fasta -> fasta},
                          ^^^^^
  ```

- Error: `subworkflows/local/mammals/process_alignments.nf:34:22`: `fai` is already declared

  ```nextflow
          fai.map{meta,fai -> fai} )
                       ^^^
  ```

- Error: `subworkflows/local/prepare_genome.nf:33:29`: `fasta` is already declared

  ```nextflow
              fasta.map{meta, fasta -> fasta}
                              ^^^^^
  ```

- Error: `subworkflows/local/prepare_genome.nf:37:24`: `fasta` is already declared

  ```nextflow
              .map{meta, fasta -> [[id: 'masked_' + meta.id], fasta]}
                         ^^^^^
  ```

- Error: `subworkflows/local/prepare_genome.nf:52:24`: `fasta` is already declared

  ```nextflow
              .map{meta, fasta -> [[id: 'concat_' + meta.id], fasta]}
                         ^^^^^
  ```

- Error: `subworkflows/local/prepare_genome.nf:93:47`: `fasta` is already declared

  ```nextflow
              BOWTIE_BUILD ( ch_fasta.map{meta, fasta -> fasta}  )
                                                ^^^^^
  ```

- Error: `subworkflows/local/utils_nfcore_callingcards_pipeline/main.nf:97:34`: `True` is not defined

  ```nextflow
                      single_end = True
                                   ^^^^
  ```

- Error: `subworkflows/local/yeast/prepare_reads.nf:48:20`: `reads` is already declared

  ```nextflow
          .map{meta, reads ->
                     ^^^^^
  ```

- Error: `subworkflows/local/yeast/prepare_reads.nf:51:30`: `barcode_details` is already declared

  ```nextflow
          .map{id, meta, read, barcode_details ->
                               ^^^^^^^^^^^^^^^
  ```

- Error: `subworkflows/local/yeast/prepare_reads.nf:72:21`: `reads` is already declared

  ```nextflow
          .map{ meta, reads ->
                      ^^^^^
  ```

- Error: `subworkflows/local/yeast/prepare_reads.nf:89:28`: `barcode_details` is already declared

  ```nextflow
          .map{meta, pickle, barcode_details ->
                             ^^^^^^^^^^^^^^^
  ```

- Error: `subworkflows/local/yeast/prepare_reads.nf:105:19`: `reads` is already declared

  ```nextflow
              meta, reads ->
                    ^^^^^
  ```

- Error: `subworkflows/local/yeast/prepare_reads.nf:109:20`: `reads` is already declared

  ```nextflow
          .map{meta, reads ->
                     ^^^^^
  ```

- Error: `subworkflows/local/yeast/prepare_reads.nf:111:23`: `reads` is already declared

  ```nextflow
          .filter{meta, reads ->
                        ^^^^^
  ```

- Error: `subworkflows/local/yeast/prepare_reads.nf:117:21`: `reads` is already declared

  ```nextflow
          .map{ meta, reads ->
                      ^^^^^
  ```

- Error: `subworkflows/local/yeast/prepare_reads.nf:150:1`: Groovy `import` declarations are not supported -- use fully-qualified name inline instead

  ```nextflow
  import nextflow.util.ArrayBag
  ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  ```

- Error: `subworkflows/local/yeast/prepare_reads.nf:243:9`: `extractDigit` is not defined

  ```nextflow
          extractDigit(a.toString()) <=> extractDigit(b.toString())
          ^^^^^^^^^^^^
  ```

- Error: `subworkflows/local/yeast/prepare_reads.nf:243:40`: `extractDigit` is not defined

  ```nextflow
          extractDigit(a.toString()) <=> extractDigit(b.toString())
                                         ^^^^^^^^^^^^
  ```

- Error: `subworkflows/local/yeast/prepare_reads.nf:261:9`: `extractReadEnd` is not defined

  ```nextflow
          extractReadEnd(a.toString()) <=> extractReadEnd(b.toString())
          ^^^^^^^^^^^^^^
  ```

- Error: `subworkflows/local/yeast/prepare_reads.nf:261:42`: `extractReadEnd` is not defined

  ```nextflow
          extractReadEnd(a.toString()) <=> extractReadEnd(b.toString())
                                           ^^^^^^^^^^^^^^
  ```

- Error: `subworkflows/local/yeast/process_alignments.nf:27:25`: `fasta` is already declared

  ```nextflow
          fasta.map{meta, fasta -> fasta},
                          ^^^^^
  ```

- Error: `subworkflows/local/yeast/process_alignments.nf:28:22`: `fai` is already declared

  ```nextflow
          fai.map{meta,fai -> fai}
                       ^^^
  ```

- Error: `workflows/callingcards.nf:10:1`: Module could not be parsed: '/home/runner/work/strict-syntax-health/strict-syntax-health/pipelines/callingcards/subworkflows/local/align.nf'

  ```nextflow
  include { ALIGN                                            } from "../subworkflows/local/align.nf"
  ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  ```

- Error: `workflows/callingcards.nf:96:5`: `ALIGN` is not defined

  ```nextflow
      ALIGN (
      ^^^^^
  ```

- Error: `workflows/callingcards.nf:103:35`: `ALIGN` is not defined

  ```nextflow
      ch_versions = ch_versions.mix(ALIGN.out.versions)
                                    ^^^^^
  ```

- Error: `workflows/callingcards.nf:115:9`: `ALIGN` is not defined

  ```nextflow
          ALIGN.out.bam
          ^^^^^
  ```

- Error: `workflows/callingcards.nf:163:9`: `ALIGN` is not defined

  ```nextflow
          ALIGN.out.bam
          ^^^^^
  ```

## :warning: Warnings

- Warning: `main.nf:37:9`: Params should be declared at the top-level (i.e. outside the workflow)

  ```nextflow
          params.regions_mask = "${projectDir}/assets/yeast/igenomes/R64-1-1/regions_mask.bed"
          ^^^^^^
  ```

- Warning: `main.nf:40:9`: Params should be declared at the top-level (i.e. outside the workflow)

  ```nextflow
          params.fasta_index = null
          ^^^^^^
  ```

- Warning: `main.nf:44:9`: Params should be declared at the top-level (i.e. outside the workflow)

  ```nextflow
          params.additional_fasta = "${projectDir}/assets/yeast/plasmid_sequences.fasta"
          ^^^^^^
  ```

- Warning: `main.nf:51:9`: Params should be declared at the top-level (i.e. outside the workflow)

  ```nextflow
          params.bwa_index = getGenomeAttribute(params, 'bwa')
          ^^^^^^
  ```

- Warning: `main.nf:56:5`: Params should be declared at the top-level (i.e. outside the workflow)

  ```nextflow
      params.regions_mask = null
      ^^^^^^
  ```

- Warning: `main.nf:61:5`: Params should be declared at the top-level (i.e. outside the workflow)

  ```nextflow
      params.additional_fasta = null
      ^^^^^^
  ```

- Warning: `main.nf:66:5`: Params should be declared at the top-level (i.e. outside the workflow)

  ```nextflow
      params.fasta_index = null
      ^^^^^^
  ```

- Warning: `main.nf:74:5`: Params should be declared at the top-level (i.e. outside the workflow)

  ```nextflow
      params.bwa_index = null
      ^^^^^^
  ```

- Warning: `main.nf:77:5`: Params should be declared at the top-level (i.e. outside the workflow)

  ```nextflow
      params.bwamem2_index = null
      ^^^^^^
  ```

- Warning: `main.nf:80:5`: Params should be declared at the top-level (i.e. outside the workflow)

  ```nextflow
      params.bowtie_index = null
      ^^^^^^
  ```

- Warning: `main.nf:83:5`: Params should be declared at the top-level (i.e. outside the workflow)

  ```nextflow
      params.bowtie2_index = null
      ^^^^^^
  ```

- Warning: `main.nf:104:20`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
          ch_fasta = Channel.fromPath(params.fasta, checkIfExists: true).collect()
                     ^^^^^^^
  ```

- Warning: `main.nf:111:18`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
          ch_gtf = Channel.fromPath(params.gtf, checkIfExists:true).collect()
                   ^^^^^^^
  ```

- Warning: `main.nf:117:13`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
              Channel.fromPath(params.regions_mask, checkIfExists: true)
              ^^^^^^^
  ```

- Warning: `main.nf:119:13`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
              Channel.empty()
              ^^^^^^^
  ```

- Warning: `main.nf:122:13`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
              Channel.fromPath(params.additional_fasta, checkIfExists: true).collect() :
              ^^^^^^^
  ```

- Warning: `main.nf:123:13`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
              Channel.empty()
              ^^^^^^^
  ```

- Warning: `main.nf:126:50`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          params.rseqc_modules.split(',').collect{ it.trim().toLowerCase() } :
                                                   ^^
  ```

- Warning: `modules/local/callingcardstools/mammals/concatQC/main.nf:11:15`: Variable was declared but not used

  ```nextflow
      tuple val(meta), path(qbed_files)
                ^^^^
  ```

- Warning: `modules/local/callingcardstools/mammals/concatQC/main.nf:27:9`: Variable was declared but not used

  ```nextflow
      def suffix = task.ext.prefix ?: ""
          ^^^^^^
  ```

- Warning: `modules/local/callingcardstools/mammals/count_hops/main.nf:28:9`: Variable was declared but not used

  ```nextflow
      def args2 = task.ext.args2 ?: ''
          ^^^^^
  ```

- Warning: `modules/local/callingcardstools/yeast/count_hops/main.nf:28:9`: Variable was declared but not used

  ```nextflow
      def prefix = task.ext.prefix ?: "${meta.id}"
          ^^^^^^
  ```

- Warning: `modules/local/callingcardstools/yeast/demultiplex/main.nf:25:9`: Variable was declared but not used

  ```nextflow
      def prefix = task.ext.prefix ?: "${meta.id}"
          ^^^^^^
  ```

- Warning: `modules/local/concatFasta/main.nf:21:9`: Variable was declared but not used

  ```nextflow
      def args        = task.ext.args     ?: ''
          ^^^^
  ```

- Warning: `modules/local/concatFastq/main.nf:20:9`: Variable was declared but not used

  ```nextflow
      def args        = task.ext.args     ?: ''
          ^^^^
  ```

- Warning: `modules/nf-core/bowtie/build/main.nf:21:9`: Variable was declared but not used

  ```nextflow
      def args = task.ext.args ?: ''
          ^^^^
  ```

- Warning: `modules/nf-core/bowtie2/align/main.nf:93:9`: Variable was declared but not used

  ```nextflow
      def reference = fasta && extension=="cram"  ? "--reference ${fasta}" : ""
          ^^^^^^^^^
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

- Warning: `modules/nf-core/custom/dumpsoftwareversions/main.nf:22:9`: Variable was declared but not used

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

- Warning: `subworkflows/local/mammals/prepare_reads.nf:18:23`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_versions     = Channel.empty()
                        ^^^^^^^
  ```

- Warning: `subworkflows/local/mammals/prepare_reads.nf:19:23`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      umi_log         = Channel.empty()
                        ^^^^^^^
  ```

- Warning: `subworkflows/local/mammals/prepare_reads.nf:20:23`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      fastqc_html     = Channel.empty()
                        ^^^^^^^
  ```

- Warning: `subworkflows/local/mammals/prepare_reads.nf:21:23`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      fastqc_zip      = Channel.empty()
                        ^^^^^^^
  ```

- Warning: `subworkflows/local/mammals/prepare_reads.nf:22:23`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      trimmomatic_log = Channel.empty()
                        ^^^^^^^
  ```

- Warning: `subworkflows/local/mammals/prepare_reads.nf:30:16`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_reads = Channel.empty()
                 ^^^^^^^
  ```

- Warning: `subworkflows/local/mammals/process_alignments.nf:23:5`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
      ch_gtf                  // [ path(gtf) ]
      ^^^^^^
  ```

- Warning: `subworkflows/local/mammals/process_alignments.nf:27:19`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_versions = Channel.empty()
                    ^^^^^^^
  ```

- Warning: `subworkflows/local/mammals/process_alignments.nf:33:19`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          fasta.map{meta, fasta -> fasta},
                    ^^^^
  ```

- Warning: `subworkflows/local/mammals/process_alignments.nf:34:17`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          fai.map{meta,fai -> fai} )
                  ^^^^
  ```

- Warning: `subworkflows/local/prepare_genome.nf:23:19`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_versions = Channel.empty()
                    ^^^^^^^
  ```

- Warning: `subworkflows/local/prepare_genome.nf:24:24`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_bwamem2_index = Channel.empty()
                         ^^^^^^^
  ```

- Warning: `subworkflows/local/prepare_genome.nf:25:20`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_bwa_index = Channel.empty()
                     ^^^^^^^
  ```

- Warning: `subworkflows/local/prepare_genome.nf:26:24`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_bowtie2_index = Channel.empty()
                         ^^^^^^^
  ```

- Warning: `subworkflows/local/prepare_genome.nf:27:23`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_bowtie_index = Channel.of("")
                        ^^^^^^^
  ```

- Warning: `subworkflows/local/prepare_genome.nf:33:23`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
              fasta.map{meta, fasta -> fasta}
                        ^^^^
  ```

- Warning: `subworkflows/local/prepare_genome.nf:67:32`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
              ch_bwamem2_index = Channel.of([[id: 'input_genome_index'],params.bwamem2_index]).collect()
                                 ^^^^^^^
  ```

- Warning: `subworkflows/local/prepare_genome.nf:77:28`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
              ch_bwa_index = Channel.of([[id: 'input_genome_index'],params.bwa_index]).collect()
                             ^^^^^^^
  ```

- Warning: `subworkflows/local/prepare_genome.nf:87:32`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
              ch_bowtie2_index = Channel.of([[id: 'input_genome_index'],params.bowtie2_index]).collect()
                                 ^^^^^^^
  ```

- Warning: `subworkflows/local/prepare_genome.nf:93:41`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
              BOWTIE_BUILD ( ch_fasta.map{meta, fasta -> fasta}  )
                                          ^^^^
  ```

- Warning: `subworkflows/local/prepare_genome.nf:97:31`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
              ch_bowtie_index = Channel.of([params.bowtie_index]).collect()
                                ^^^^^^^
  ```

- Warning: `subworkflows/local/prepare_genome.nf:113:26`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
          ch_fasta_index = Channel.of(["",params.fasta_index]).collect()
                           ^^^^^^^
  ```

- Warning: `subworkflows/local/utils_nfcore_callingcards_pipeline/main.nf:31:5`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
      monochrome_logs   // boolean: Do not use coloured log outputs
      ^^^^^^^^^^^^^^^
  ```

- Warning: `subworkflows/local/utils_nfcore_callingcards_pipeline/main.nf:34:5`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
      input             //  string: Path to input samplesheet
      ^^^^^
  ```

- Warning: `subworkflows/local/utils_nfcore_callingcards_pipeline/main.nf:38:19`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_versions = Channel.empty()
                    ^^^^^^^
  ```

- Warning: `subworkflows/local/utils_nfcore_callingcards_pipeline/main.nf:76:9`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
          Channel
          ^^^^^^^
  ```

- Warning: `subworkflows/local/utils_nfcore_callingcards_pipeline/main.nf:91:9`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
          Channel
          ^^^^^^^
  ```

- Warning: `subworkflows/local/yeast/prepare_reads.nf:22:19`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_versions = Channel.empty()
                    ^^^^^^^
  ```

- Warning: `subworkflows/local/yeast/prepare_reads.nf:23:5`: Variable was declared but not used

  ```nextflow
      fastqc_html = Channel.empty()
      ^^^^^^^^^^^
  ```

- Warning: `subworkflows/local/yeast/prepare_reads.nf:23:19`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      fastqc_html = Channel.empty()
                    ^^^^^^^
  ```

- Warning: `subworkflows/local/yeast/prepare_reads.nf:24:5`: Variable was declared but not used

  ```nextflow
      fastqc_zip  = Channel.empty()
      ^^^^^^^^^^
  ```

- Warning: `subworkflows/local/yeast/prepare_reads.nf:24:19`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      fastqc_zip  = Channel.empty()
                    ^^^^^^^
  ```

- Warning: `subworkflows/local/yeast/prepare_reads.nf:25:23`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      trimmomatic_log = Channel.empty()
                        ^^^^^^^
  ```

- Warning: `subworkflows/local/yeast/prepare_reads.nf:28:19`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      demux_reads = Channel.empty()
                    ^^^^^^^
  ```

- Warning: `subworkflows/local/yeast/prepare_reads.nf:29:20`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      output_reads = Channel.empty()
                     ^^^^^^^
  ```

- Warning: `subworkflows/local/yeast/prepare_reads.nf:51:14`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          .map{id, meta, read, barcode_details ->
               ^^
  ```

- Warning: `subworkflows/local/yeast/prepare_reads.nf:111:17`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          .filter{meta, reads ->
                  ^^^^
  ```

- Warning: `subworkflows/local/yeast/prepare_reads.nf:112:26`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
              reads.every {it.size() > 0} }
                           ^^
  ```

- Warning: `subworkflows/local/yeast/prepare_reads.nf:231:9`: Variable was declared but not used

  ```nextflow
      def extractDigit = { String path ->
          ^^^^^^^^^^^^
  ```

- Warning: `subworkflows/local/yeast/prepare_reads.nf:249:9`: Variable was declared but not used

  ```nextflow
      def extractReadEnd = { String path ->
          ^^^^^^^^^^^^^^
  ```

- Warning: `subworkflows/local/yeast/process_alignments.nf:17:5`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
      ch_gtf         // [ path(gtf) ]
      ^^^^^^
  ```

- Warning: `subworkflows/local/yeast/process_alignments.nf:21:19`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_versions = Channel.empty()
                    ^^^^^^^
  ```

- Warning: `subworkflows/local/yeast/process_alignments.nf:27:19`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          fasta.map{meta, fasta -> fasta},
                    ^^^^
  ```

- Warning: `subworkflows/local/yeast/process_alignments.nf:28:17`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          fai.map{meta,fai -> fai}
                  ^^^^
  ```

- Warning: `subworkflows/local/yeast/process_alignments.nf:51:14`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          .map{meta_join, meta, bam, bai ->
               ^^^^^^^^^
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

- Warning: `workflows/callingcards.nf:39:28`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_versions          = Channel.empty()
                             ^^^^^^^
  ```

- Warning: `workflows/callingcards.nf:40:28`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_multiqc_files     = Channel.empty()
                             ^^^^^^^
  ```

- Warning: `workflows/callingcards.nf:41:5`: Variable was declared but not used

  ```nextflow
      ch_fasta_index       = Channel.empty()
      ^^^^^^^^^^^^^^
  ```

- Warning: `workflows/callingcards.nf:41:28`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_fasta_index       = Channel.empty()
                             ^^^^^^^
  ```

- Warning: `workflows/callingcards.nf:42:5`: Variable was declared but not used

  ```nextflow
      ch_bam_index         = Channel.empty()
      ^^^^^^^^^^^^
  ```

- Warning: `workflows/callingcards.nf:42:28`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_bam_index         = Channel.empty()
                             ^^^^^^^
  ```

- Warning: `workflows/callingcards.nf:43:28`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_prepared_reads    = Channel.empty()
                             ^^^^^^^
  ```

- Warning: `workflows/callingcards.nf:44:5`: Variable was declared but not used

  ```nextflow
      ch_samtools_stats    = Channel.empty()
      ^^^^^^^^^^^^^^^^^
  ```

- Warning: `workflows/callingcards.nf:44:28`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_samtools_stats    = Channel.empty()
                             ^^^^^^^
  ```

- Warning: `workflows/callingcards.nf:45:5`: Variable was declared but not used

  ```nextflow
      ch_samtools_flatstat = Channel.empty()
      ^^^^^^^^^^^^^^^^^^^^
  ```

- Warning: `workflows/callingcards.nf:45:28`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_samtools_flatstat = Channel.empty()
                             ^^^^^^^
  ```

- Warning: `workflows/callingcards.nf:46:5`: Variable was declared but not used

  ```nextflow
      ch_samtools_idxstats = Channel.empty()
      ^^^^^^^^^^^^^^^^^^^^
  ```

- Warning: `workflows/callingcards.nf:46:28`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_samtools_idxstats = Channel.empty()
                             ^^^^^^^
  ```

- Warning: `workflows/callingcards.nf:77:96`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          ch_multiqc_files = ch_multiqc_files.mix(YEAST_PREPARE_READS.out.raw_fastqc_zip.collect{it[1]}.ifEmpty([]))
                                                                                                 ^^
  ```

- Warning: `workflows/callingcards.nf:78:97`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          ch_multiqc_files = ch_multiqc_files.mix(YEAST_PREPARE_READS.out.trimmomatic_log.collect{it[1]}.ifEmpty([]))
                                                                                                  ^^
  ```

- Warning: `workflows/callingcards.nf:79:98`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          ch_multiqc_files = ch_multiqc_files.mix(YEAST_PREPARE_READS.out.demux_fastqc_zip.collect{it[1]}.ifEmpty([]))
                                                                                                   ^^
  ```

- Warning: `workflows/callingcards.nf:89:94`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          ch_multiqc_files = ch_multiqc_files.mix(MAMMALS_PREPARE_READS.out.fastqc_zip.collect{it[1]}.ifEmpty([]))
                                                                                               ^^
  ```

- Warning: `workflows/callingcards.nf:90:99`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          ch_multiqc_files = ch_multiqc_files.mix(MAMMALS_PREPARE_READS.out.trimmomatic_log.collect{it[1]}.ifEmpty([]))
                                                                                                    ^^
  ```

- Warning: `workflows/callingcards.nf:91:91`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          ch_multiqc_files = ch_multiqc_files.mix(MAMMALS_PREPARE_READS.out.umi_log.collect{it[1]}.ifEmpty([]))
                                                                                            ^^
  ```

- Warning: `workflows/callingcards.nf:119:19`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
              .map{ key, meta, bam, bai, barcode_details ->
                    ^^^
  ```

- Warning: `workflows/callingcards.nf:147:101`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          ch_multiqc_files = ch_multiqc_files.mix(YEAST_PROCESS_ALIGNMENTS.out.samtools_stats.collect{it[1]}.ifEmpty([]))
                                                                                                      ^^
  ```

- Warning: `workflows/callingcards.nf:148:104`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          ch_multiqc_files = ch_multiqc_files.mix(YEAST_PROCESS_ALIGNMENTS.out.samtools_flagstat.collect{it[1]}.ifEmpty([]))
                                                                                                         ^^
  ```

- Warning: `workflows/callingcards.nf:149:104`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          ch_multiqc_files = ch_multiqc_files.mix(YEAST_PROCESS_ALIGNMENTS.out.samtools_idxstats.collect{it[1]}.ifEmpty([]))
                                                                                                         ^^
  ```

- Warning: `workflows/callingcards.nf:150:96`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          ch_multiqc_files = ch_multiqc_files.mix(YEAST_PROCESS_ALIGNMENTS.out.picard_qc.collect{it[1]}.ifEmpty([]))
                                                                                                 ^^
  ```

- Warning: `workflows/callingcards.nf:151:100`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          ch_multiqc_files = ch_multiqc_files.mix(YEAST_PROCESS_ALIGNMENTS.out.rseqc_bamstat.collect{it[1]}.ifEmpty([]))
                                                                                                     ^^
  ```

- Warning: `workflows/callingcards.nf:152:108`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          ch_multiqc_files = ch_multiqc_files.mix(YEAST_PROCESS_ALIGNMENTS.out.rseqc_inferexperiment.collect{it[1]}.ifEmpty([]))
                                                                                                             ^^
  ```

- Warning: `workflows/callingcards.nf:153:106`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          ch_multiqc_files = ch_multiqc_files.mix(YEAST_PROCESS_ALIGNMENTS.out.rseqc_innerdistance.collect{it[1]}.ifEmpty([]))
                                                                                                           ^^
  ```

- Warning: `workflows/callingcards.nf:154:109`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          ch_multiqc_files = ch_multiqc_files.mix(YEAST_PROCESS_ALIGNMENTS.out.rseqc_readdistribution.collect{it[1]}.ifEmpty([]))
                                                                                                              ^^
  ```

- Warning: `workflows/callingcards.nf:155:108`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          ch_multiqc_files = ch_multiqc_files.mix(YEAST_PROCESS_ALIGNMENTS.out.rseqc_readduplication.collect{it[1]}.ifEmpty([]))
                                                                                                             ^^
  ```

- Warning: `workflows/callingcards.nf:156:96`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          ch_multiqc_files = ch_multiqc_files.mix(YEAST_PROCESS_ALIGNMENTS.out.rseqc_tin.collect{it[1]}.ifEmpty([]))
                                                                                                 ^^
  ```

- Warning: `workflows/callingcards.nf:169:18`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
              .map{id, meta, bam, bai, barcode_details ->
                   ^^
  ```

- Warning: `workflows/callingcards.nf:186:103`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          ch_multiqc_files = ch_multiqc_files.mix(MAMMALS_PROCESS_ALIGNMENTS.out.samtools_stats.collect{it[1]}.ifEmpty([]))
                                                                                                        ^^
  ```

- Warning: `workflows/callingcards.nf:187:106`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          ch_multiqc_files = ch_multiqc_files.mix(MAMMALS_PROCESS_ALIGNMENTS.out.samtools_flagstat.collect{it[1]}.ifEmpty([]))
                                                                                                           ^^
  ```

- Warning: `workflows/callingcards.nf:188:106`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          ch_multiqc_files = ch_multiqc_files.mix(MAMMALS_PROCESS_ALIGNMENTS.out.samtools_idxstats.collect{it[1]}.ifEmpty([]))
                                                                                                           ^^
  ```

- Warning: `workflows/callingcards.nf:189:98`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          ch_multiqc_files = ch_multiqc_files.mix(MAMMALS_PROCESS_ALIGNMENTS.out.picard_qc.collect{it[1]}.ifEmpty([]))
                                                                                                   ^^
  ```

- Warning: `workflows/callingcards.nf:190:102`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          ch_multiqc_files = ch_multiqc_files.mix(MAMMALS_PROCESS_ALIGNMENTS.out.rseqc_bamstat.collect{it[1]}.ifEmpty([]))
                                                                                                       ^^
  ```

- Warning: `workflows/callingcards.nf:191:110`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          ch_multiqc_files = ch_multiqc_files.mix(MAMMALS_PROCESS_ALIGNMENTS.out.rseqc_inferexperiment.collect{it[1]}.ifEmpty([]))
                                                                                                               ^^
  ```

- Warning: `workflows/callingcards.nf:192:108`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          ch_multiqc_files = ch_multiqc_files.mix(MAMMALS_PROCESS_ALIGNMENTS.out.rseqc_innerdistance.collect{it[1]}.ifEmpty([]))
                                                                                                             ^^
  ```

- Warning: `workflows/callingcards.nf:193:111`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          ch_multiqc_files = ch_multiqc_files.mix(MAMMALS_PROCESS_ALIGNMENTS.out.rseqc_readdistribution.collect{it[1]}.ifEmpty([]))
                                                                                                                ^^
  ```

- Warning: `workflows/callingcards.nf:194:110`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          ch_multiqc_files = ch_multiqc_files.mix(MAMMALS_PROCESS_ALIGNMENTS.out.rseqc_readduplication.collect{it[1]}.ifEmpty([]))
                                                                                                               ^^
  ```

- Warning: `workflows/callingcards.nf:195:98`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          ch_multiqc_files = ch_multiqc_files.mix(MAMMALS_PROCESS_ALIGNMENTS.out.rseqc_tin.collect{it[1]}.ifEmpty([]))
                                                                                                   ^^
  ```

- Warning: `workflows/callingcards.nf:214:32`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_multiqc_config        = Channel.fromPath(
                                 ^^^^^^^
  ```

- Warning: `workflows/callingcards.nf:217:9`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
          Channel.fromPath(params.multiqc_config, checkIfExists: true) :
          ^^^^^^^
  ```

- Warning: `workflows/callingcards.nf:218:9`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
          Channel.empty()
          ^^^^^^^
  ```

- Warning: `workflows/callingcards.nf:220:9`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
          Channel.fromPath(params.multiqc_logo, checkIfExists: true) :
          ^^^^^^^
  ```

- Warning: `workflows/callingcards.nf:221:9`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
          Channel.empty()
          ^^^^^^^
  ```

- Warning: `workflows/callingcards.nf:225:27`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_workflow_summary = Channel.value(paramsSummaryMultiqc(summary_params))
                            ^^^^^^^
  ```

- Warning: `workflows/callingcards.nf:231:45`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_methods_description                = Channel.value(
                                              ^^^^^^^
  ```
