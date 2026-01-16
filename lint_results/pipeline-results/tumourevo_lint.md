# Nextflow lint results

- Generated: 2026-01-16T10:31:01.854610858Z
- Nextflow version: 25.12.0-edge
- Summary: 9 errors, 56 warnings

## :x: Errors

- Error: `main.nf:45:1`: Statements cannot be mixed with script declarations -- move statements into a process, workflow, or function

  ```nextflow
  input = params.input ? Channel.fromList(samplesheetToList(params.input, "assets/schema_input.json")) : Channel.empty()
  ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  ```

- Error: `main.nf:74:51`: `path` is already declared

  ```nextflow
              vep_cache = UNTAR.out.untar.map{meta, path ->
                                                    ^^^^
  ```

- Error: `main.nf:114:9`: `input` is not defined

  ```nextflow
          input
          ^^^^^
  ```

- Error: `subworkflows/local/lifter/main.nf:23:36`: `bam` is already declared

  ```nextflow
          rds = data.map{ meta, rds, bam, bai ->
                                     ^^^
  ```

- Error: `subworkflows/local/lifter/main.nf:27:35`: `rds` is already declared

  ```nextflow
          all_rds = data.map{ meta, rds, bam, bai ->
                                    ^^^
  ```

- Error: `subworkflows/local/lifter/main.nf:27:40`: `bam` is already declared

  ```nextflow
          all_rds = data.map{ meta, rds, bam, bai ->
                                         ^^^
  ```

- Error: `subworkflows/local/lifter/main.nf:33:72`: `rds` is already declared

  ```nextflow
          all_pos = GET_POSITIONS_ALL.out.all_pos.transpose().map{ meta, rds ->
                                                                         ^^^
  ```

- Error: `workflows/tumourevo.nf:36:17`: Variables in a closure should be declared with `def`

  ```nextflow
                  n = vcf.baseName.unique().size()
                  ^
  ```

- Error: `workflows/tumourevo.nf:39:71`: `n` is already declared

  ```nextflow
              .map { id, meta, vcf, tbi, bam, bai, cna_segs, cna_extra, n  ->
                                                                        ^
  ```

## :warning: Warnings

- Warning: `conf/modules/cnaqc.config:28:20`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          .findAll { it }      // remove empty strings
                     ^^
  ```

- Warning: `main.nf:45:1`: Variable was declared but not used

  ```nextflow
  input = params.input ? Channel.fromList(samplesheetToList(params.input, "assets/schema_input.json")) : Channel.empty()
  ^^^^^
  ```

- Warning: `main.nf:45:24`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
  input = params.input ? Channel.fromList(samplesheetToList(params.input, "assets/schema_input.json")) : Channel.empty()
                         ^^^^^^^
  ```

- Warning: `main.nf:45:104`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
  input = params.input ? Channel.fromList(samplesheetToList(params.input, "assets/schema_input.json")) : Channel.empty()
                                                                                                         ^^^^^^^
  ```

- Warning: `main.nf:62:28`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      fasta = params.fasta ? Channel.fromPath(params.fasta).map{ it -> [ [id:it.baseName], it ] }.collect() : Channel.empty()
                             ^^^^^^^
  ```

- Warning: `main.nf:62:109`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      fasta = params.fasta ? Channel.fromPath(params.fasta).map{ it -> [ [id:it.baseName], it ] }.collect() : Channel.empty()
                                                                                                              ^^^^^^^
  ```

- Warning: `main.nf:63:45`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      drivers_table =  params.drivers_table ? Channel.fromPath(params.drivers_table).map{ it -> [ it ] }.collect() : Channel.empty()
                                              ^^^^^^^
  ```

- Warning: `main.nf:63:116`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      drivers_table =  params.drivers_table ? Channel.fromPath(params.drivers_table).map{ it -> [ it ] }.collect() : Channel.empty()
                                                                                                                     ^^^^^^^
  ```

- Warning: `main.nf:66:27`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
          ensemblvep_info = Channel.of([ [ id:"${params.vep_cache_version}_${params.vep_genome}" ], params.vep_genome, params.vep_species, params.vep_cache_version ])
                            ^^^^^^^
  ```

- Warning: `main.nf:68:66`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          vep_cache = ENSEMBLVEP_DOWNLOAD.out.cache.collect().map{ meta, cache -> [ cache ] }
                                                                   ^^^^
  ```

- Warning: `main.nf:72:39`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
              path = params.vep_cache ? Channel.fromPath(params.vep_cache).map{ it -> [ [id:it.baseName], it ] }.collect() : Channel.empty()
                                        ^^^^^^^
  ```

- Warning: `main.nf:72:124`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
              path = params.vep_cache ? Channel.fromPath(params.vep_cache).map{ it -> [ [id:it.baseName], it ] }.collect() : Channel.empty()
                                                                                                                             ^^^^^^^
  ```

- Warning: `main.nf:74:45`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
              vep_cache = UNTAR.out.untar.map{meta, path ->
                                              ^^^^
  ```

- Warning: `modules/local/annotate_driver/main.nf:19:9`: Variable was declared but not used

  ```nextflow
      def args   = task.ext.args   ?: ""
          ^^^^
  ```

- Warning: `modules/local/get_positions/main.nf:19:9`: Variable was declared but not used

  ```nextflow
      def args   = task.ext.args   ?: ""
          ^^^^
  ```

- Warning: `modules/local/get_positions/main_rel.nf:19:9`: Variable was declared but not used

  ```nextflow
      def args   = task.ext.args   ?: ""
          ^^^^
  ```

- Warning: `modules/local/get_positions/main_rel.nf:20:9`: Variable was declared but not used

  ```nextflow
      def prefix = task.ext.prefix ?: "${meta.id}"
          ^^^^^^
  ```

- Warning: `modules/local/join_cnaqc/main.nf:22:9`: Variable was declared but not used

  ```nextflow
      def qc_filter = args!='' && args.qc_filter ? "$args.qc_filter" : ""
          ^^^^^^^^^
  ```

- Warning: `modules/local/join_positions/main.nf:19:9`: Variable was declared but not used

  ```nextflow
      def args = task.ext.args ?: ''
          ^^^^
  ```

- Warning: `modules/nf-core/cnaqc/main.nf:25:9`: Variable was declared but not used

  ```nextflow
      def args = task.ext.args ?: ''
          ^^^^
  ```

- Warning: `modules/nf-core/cnaqc/main.nf:26:9`: Variable was declared but not used

  ```nextflow
      def prefix = task.ext.prefix ?: "${meta.id}"
          ^^^^^^
  ```

- Warning: `modules/nf-core/cnaqc/main.nf:31:9`: Variable was declared but not used

  ```nextflow
      def args = task.ext.args ?: ''
          ^^^^
  ```

- Warning: `modules/nf-core/pyclonevi/main.nf:26:9`: Variable was declared but not used

  ```nextflow
      def args = task.ext.args ?: ''
          ^^^^
  ```

- Warning: `modules/nf-core/sigprofiler/main.nf:26:9`: Variable was declared but not used

  ```nextflow
      def args   = task.ext.args   ?: ''
          ^^^^
  ```

- Warning: `modules/nf-core/sigprofiler/main.nf:36:57`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
      def signatures = context_types.collect { context_map[it] }
                                                          ^^
  ```

- Warning: `subworkflows/local/annotation_cache_initialisation/main.nf:22:24`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ensemblvep_cache = Channel.fromPath(file("${vep_cache}/${vep_annotation_cache_key}"), checkIfExists: true).collect()
                         ^^^^^^^
  ```

- Warning: `subworkflows/local/lifter/main.nf:17:15`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
          out = Channel.empty()
                ^^^^^^^
  ```

- Warning: `subworkflows/local/lifter/main.nf:19:31`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          bam = data.map{ meta, rds, bam, bai ->
                                ^^^
  ```

- Warning: `subworkflows/local/lifter/main.nf:19:41`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          bam = data.map{ meta, rds, bam, bai ->
                                          ^^^
  ```

- Warning: `subworkflows/local/lifter/main.nf:23:36`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          rds = data.map{ meta, rds, bam, bai ->
                                     ^^^
  ```

- Warning: `subworkflows/local/lifter/main.nf:23:41`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          rds = data.map{ meta, rds, bam, bai ->
                                          ^^^
  ```

- Warning: `subworkflows/local/lifter/main.nf:27:40`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          all_rds = data.map{ meta, rds, bam, bai ->
                                         ^^^
  ```

- Warning: `subworkflows/local/lifter/main.nf:27:45`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          all_rds = data.map{ meta, rds, bam, bai ->
                                              ^^^
  ```

- Warning: `subworkflows/local/lifter/main.nf:33:66`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          all_pos = GET_POSITIONS_ALL.out.all_pos.transpose().map{ meta, rds ->
                                                                   ^^^^
  ```

- Warning: `subworkflows/local/signature_deconvolution/main.nf:27:79`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          input_sparsesig = FORMATTER_RDS_SPARSESIGNATURES.out.map { meta, tsv, sample ->
                                                                                ^^^^^^
  ```

- Warning: `subworkflows/local/signature_deconvolution/main.nf:52:76`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          input_sigprofiler = FORMATTER_RDS_SIGPROFILER.out.map { meta, tsv, sample ->
                                                                             ^^^^^^
  ```

- Warning: `subworkflows/local/utils_nfcore_tumourevo_pipeline/main.nf:32:5`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
      monochrome_logs   // boolean: Do not use coloured log outputs
      ^^^^^^^^^^^^^^^
  ```

- Warning: `subworkflows/local/utils_nfcore_tumourevo_pipeline/main.nf:35:5`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
      input             //  string: Path to input samplesheet
      ^^^^^
  ```

- Warning: `workflows/tumourevo.nf:39:20`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
              .map { id, meta, vcf, tbi, bam, bai, cna_segs, cna_extra, n  ->
                     ^^
  ```

- Warning: `workflows/tumourevo.nf:48:44`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
      input_vcf = input.map{ meta, vcf, tbi, bam, bai, cna_segs, cna_extra  ->
                                             ^^^
  ```

- Warning: `workflows/tumourevo.nf:48:49`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
      input_vcf = input.map{ meta, vcf, tbi, bam, bai, cna_segs, cna_extra  ->
                                                  ^^^
  ```

- Warning: `workflows/tumourevo.nf:48:54`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
      input_vcf = input.map{ meta, vcf, tbi, bam, bai, cna_segs, cna_extra  ->
                                                       ^^^^^^^^
  ```

- Warning: `workflows/tumourevo.nf:48:64`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
      input_vcf = input.map{ meta, vcf, tbi, bam, bai, cna_segs, cna_extra  ->
                                                                 ^^^^^^^^^
  ```

- Warning: `workflows/tumourevo.nf:52:34`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
      input_cna = input.map{ meta, vcf, tbi, bam, bai, cna_segs, cna_extra  ->
                                   ^^^
  ```

- Warning: `workflows/tumourevo.nf:52:39`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
      input_cna = input.map{ meta, vcf, tbi, bam, bai, cna_segs, cna_extra  ->
                                        ^^^
  ```

- Warning: `workflows/tumourevo.nf:52:44`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
      input_cna = input.map{ meta, vcf, tbi, bam, bai, cna_segs, cna_extra  ->
                                             ^^^
  ```

- Warning: `workflows/tumourevo.nf:52:49`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
      input_cna = input.map{ meta, vcf, tbi, bam, bai, cna_segs, cna_extra  ->
                                                  ^^^
  ```

- Warning: `workflows/tumourevo.nf:56:34`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
      input_bam = input.map{ meta, vcf, tbi, bam, bai, cna_segs, cna_extra  ->
                                   ^^^
  ```

- Warning: `workflows/tumourevo.nf:56:39`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
      input_bam = input.map{ meta, vcf, tbi, bam, bai, cna_segs, cna_extra  ->
                                        ^^^
  ```

- Warning: `workflows/tumourevo.nf:56:54`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
      input_bam = input.map{ meta, vcf, tbi, bam, bai, cna_segs, cna_extra  ->
                                                       ^^^^^^^^
  ```

- Warning: `workflows/tumourevo.nf:56:64`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
      input_bam = input.map{ meta, vcf, tbi, bam, bai, cna_segs, cna_extra  ->
                                                                 ^^^^^^^^^
  ```

- Warning: `workflows/tumourevo.nf:85:29`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
              .branch { meta, rds, bam, bai ->
                              ^^^
  ```

- Warning: `workflows/tumourevo.nf:85:34`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
              .branch { meta, rds, bam, bai ->
                                   ^^^
  ```

- Warning: `workflows/tumourevo.nf:85:39`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
              .branch { meta, rds, bam, bai ->
                                        ^^^
  ```

- Warning: `workflows/tumourevo.nf:92:56`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
      rds_input = join_input.multisample.map{ meta, rds, bam, bai ->
                                                         ^^^
  ```

- Warning: `workflows/tumourevo.nf:92:61`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
      rds_input = join_input.multisample.map{ meta, rds, bam, bai ->
                                                              ^^^
  ```
