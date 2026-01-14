# Nextflow lint results

- Generated: 2026-01-14T09:21:45.380629738Z
- Nextflow version: 25.12.0-edge
- Summary: 12 errors, 54 warnings

## :x: Errors

- Error: `modules/nf-core/deepvariant/main.nf:1:1`: Statements cannot be mixed with script declarations -- move statements into a process or workflow

  ```nextflow
  def deprecation_message = """
  ^^^
  ```

- Error: `modules/nf-core/deepvariant/main.nf:29:30`: `prefix` is not defined

  ```nextflow
      tuple val(meta), path("${prefix}.vcf.gz")      ,  emit: vcf
                               ^^^^^^
  ```

- Error: `modules/nf-core/deepvariant/main.nf:30:30`: `prefix` is not defined

  ```nextflow
      tuple val(meta), path("${prefix}.vcf.gz.tbi")  ,  emit: vcf_tbi
                               ^^^^^^
  ```

- Error: `modules/nf-core/deepvariant/main.nf:31:30`: `prefix` is not defined

  ```nextflow
      tuple val(meta), path("${prefix}.g.vcf.gz")    ,  emit: gvcf
                               ^^^^^^
  ```

- Error: `modules/nf-core/deepvariant/main.nf:32:30`: `prefix` is not defined

  ```nextflow
      tuple val(meta), path("${prefix}.g.vcf.gz.tbi"),  emit: gvcf_tbi
                               ^^^^^^
  ```

- Error: `modules/nf-core/deepvariant/main.nf:39:19`: `deprecation_message` is not defined

  ```nextflow
      assert false: deprecation_message
                    ^^^^^^^^^^^^^^^^^^^
  ```

- Error: `nextflow.config:298:30`: `manifest` is not defined

  ```nextflow
  \033[0;35m  nf-core/pacvar ${manifest.version}\033[0m
                               ^^^^^^^^
  ```

- Error: `nextflow.config:301:26`: `manifest` is not defined

  ```nextflow
          afterText = """${manifest.doi ? "\n* The pipeline\n" : ""}${manifest.doi.tokenize(",").collect { "    https://doi.org/${it.trim().replace('https://doi.org/','')}"}.join("\n")}${manifest.doi ? "\n" : ""}
                           ^^^^^^^^
  ```

- Error: `nextflow.config:301:69`: `manifest` is not defined

  ```nextflow
          afterText = """${manifest.doi ? "\n* The pipeline\n" : ""}${manifest.doi.tokenize(",").collect { "    https://doi.org/${it.trim().replace('https://doi.org/','')}"}.join("\n")}${manifest.doi ? "\n" : ""}
                                                                      ^^^^^^^^
  ```

- Error: `nextflow.config:301:186`: `manifest` is not defined

  ```nextflow
          afterText = """${manifest.doi ? "\n* The pipeline\n" : ""}${manifest.doi.tokenize(",").collect { "    https://doi.org/${it.trim().replace('https://doi.org/','')}"}.join("\n")}${manifest.doi ? "\n" : ""}
                                                                                                                                                                                           ^^^^^^^^
  ```

- Error: `nextflow.config:310:22`: `validation` is not defined

  ```nextflow
          beforeText = validation.help.beforeText
                       ^^^^^^^^^^
  ```

- Error: `nextflow.config:311:21`: `validation` is not defined

  ```nextflow
          afterText = validation.help.afterText
                      ^^^^^^^^^^
  ```

## :warning: Warnings

- Warning: `main.nf:71:42`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      fasta               = params.fasta ? Channel.fromPath(params.fasta).map{ it -> [ [id:it.baseName], it ] }.collect() : Channel.empty()
                                           ^^^^^^^
  ```

- Warning: `main.nf:71:123`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      fasta               = params.fasta ? Channel.fromPath(params.fasta).map{ it -> [ [id:it.baseName], it ] }.collect() : Channel.empty()
                                                                                                                            ^^^^^^^
  ```

- Warning: `main.nf:72:46`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      fasta_fai           = params.fasta_fai ? Channel.fromPath(params.fasta_fai).map{ it -> [ [id:it.baseName], it ] }.collect() : Channel.empty()
                                               ^^^^^^^
  ```

- Warning: `main.nf:72:131`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      fasta_fai           = params.fasta_fai ? Channel.fromPath(params.fasta_fai).map{ it -> [ [id:it.baseName], it ] }.collect() : Channel.empty()
                                                                                                                                    ^^^^^^^
  ```

- Warning: `main.nf:73:41`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      dict                = params.dict ? Channel.fromPath(params.dict).map{ it -> [ [id:it.baseName], it ] }.collect() : Channel.empty()
                                          ^^^^^^^
  ```

- Warning: `main.nf:73:121`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      dict                = params.dict ? Channel.fromPath(params.dict).map{ it -> [ [id:it.baseName], it ] }.collect() : Channel.empty()
                                                                                                                          ^^^^^^^
  ```

- Warning: `main.nf:74:42`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      dbsnp               = params.dbsnp ? Channel.fromPath(params.dbsnp).collect() : Channel.value([])
                                           ^^^^^^^
  ```

- Warning: `main.nf:74:85`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      dbsnp               = params.dbsnp ? Channel.fromPath(params.dbsnp).collect() : Channel.value([])
                                                                                      ^^^^^^^
  ```

- Warning: `main.nf:75:46`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      dbsnp_tbi           = params.dbsnp_tbi ? Channel.fromPath(params.dbsnp_tbi).collect() : Channel.value([])
                                               ^^^^^^^
  ```

- Warning: `main.nf:75:93`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      dbsnp_tbi           = params.dbsnp_tbi ? Channel.fromPath(params.dbsnp_tbi).collect() : Channel.value([])
                                                                                              ^^^^^^^
  ```

- Warning: `main.nf:76:46`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      intervals           = params.intervals ? Channel.fromPath(params.intervals).map{ it -> [ [id:it.baseName], it ] }.collect() : Channel.value([[],[]])
                                               ^^^^^^^
  ```

- Warning: `main.nf:76:131`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      intervals           = params.intervals ? Channel.fromPath(params.intervals).map{ it -> [ [id:it.baseName], it ] }.collect() : Channel.value([[],[]])
                                                                                                                                    ^^^^^^^
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

- Warning: `modules/nf-core/deepvariant/main.nf:1:5`: Variable was declared but not used

  ```nextflow
  def deprecation_message = """
      ^^^^^^^^^^^^^^^^^^^
  ```

- Warning: `modules/nf-core/gunzip/main.nf:43:9`: Variable was declared but not used

  ```nextflow
      def args        = task.ext.args ?: ''
          ^^^^
  ```

- Warning: `modules/nf-core/lima/main.nf:72:9`: Variable was declared but not used

  ```nextflow
      def args = task.ext.args ?: ''
          ^^^^
  ```

- Warning: `modules/nf-core/lima/main.nf:73:9`: Variable was declared but not used

  ```nextflow
      def prefix = task.ext.prefix ?: "${meta.id}"
          ^^^^^^
  ```

- Warning: `modules/nf-core/pbmm2/align/main.nf:49:9`: Variable was declared but not used

  ```nextflow
      def args = task.ext.args ?: ''
          ^^^^
  ```

- Warning: `modules/nf-core/pbsv/call/main.nf:40:9`: Variable was declared but not used

  ```nextflow
      def args = task.ext.args ?: ''
          ^^^^
  ```

- Warning: `modules/nf-core/pbsv/discover/main.nf:36:9`: Variable was declared but not used

  ```nextflow
      def args = task.ext.args ?: ''
          ^^^^
  ```

- Warning: `modules/nf-core/pbtk/pbmerge/main.nf:38:9`: Variable was declared but not used

  ```nextflow
      def args = task.ext.args ?: ''
          ^^^^
  ```

- Warning: `modules/nf-core/trgt/genotype/main.nf:45:9`: Variable was declared but not used

  ```nextflow
      def args = task.ext.args ?: ''
          ^^^^
  ```

- Warning: `modules/nf-core/trgt/plot/main.nf:67:9`: Variable was declared but not used

  ```nextflow
      def args = task.ext.args ?: ''
          ^^^^
  ```

- Warning: `nextflow.config:301:129`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          afterText = """${manifest.doi ? "\n* The pipeline\n" : ""}${manifest.doi.tokenize(",").collect { "    https://doi.org/${it.trim().replace('https://doi.org/','')}"}.join("\n")}${manifest.doi ? "\n" : ""}
                                                                                                                                  ^^
  ```

- Warning: `subworkflows/local/bam_snp_variant_calling/main.nf:16:19`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_versions = Channel.empty()
                    ^^^^^^^
  ```

- Warning: `subworkflows/local/bam_snp_variant_calling/main.nf:18:36`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
      intervals_path = intervals.map{metadata, interval -> [interval]}
                                     ^^^^^^^^
  ```

- Warning: `subworkflows/local/bam_sv_variant_calling/main.nf:11:5`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
      sorted_bai
      ^^^^^^^^^^
  ```

- Warning: `subworkflows/local/bam_sv_variant_calling/main.nf:13:5`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
      fasta_fai
      ^^^^^^^^^
  ```

- Warning: `subworkflows/local/bam_sv_variant_calling/main.nf:16:19`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_versions = Channel.empty()
                    ^^^^^^^
  ```

- Warning: `subworkflows/local/repeat_characterization/main.nf:19:19`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_versions = Channel.empty()
                    ^^^^^^^
  ```

- Warning: `subworkflows/local/set_value_channel/main.nf:13:5`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      Channel // Prepare value channel
      ^^^^^^^
  ```

- Warning: `subworkflows/local/utils_nfcore_pacvar_pipeline/main.nf:33:5`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
      monochrome_logs   // boolean: Do not use coloured log outputs
      ^^^^^^^^^^^^^^^
  ```

- Warning: `subworkflows/local/utils_nfcore_pacvar_pipeline/main.nf:36:5`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
      input             //  string: Path to input samplesheet
      ^^^^^
  ```

- Warning: `subworkflows/local/utils_nfcore_pacvar_pipeline/main.nf:40:19`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_versions = Channel.empty()
                    ^^^^^^^
  ```

- Warning: `subworkflows/local/utils_nfcore_pacvar_pipeline/main.nf:78:5`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      Channel
      ^^^^^^^
  ```

- Warning: `subworkflows/local/utils_nfcore_pacvar_pipeline/main.nf:81:24`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
              meta, bam, pbi, fail ->
                         ^^^
  ```

- Warning: `subworkflows/local/utils_nfcore_pacvar_pipeline/main.nf:121:9`: Variable was declared but not used

  ```nextflow
      def multiqc_reports = multiqc_report.toList()
          ^^^^^^^^^^^^^^^
  ```

- Warning: `subworkflows/nf-core/utils_nfcore_pipeline/main.nf:101:98`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      return ch_versions.unique().map { version -> processVersionsFromYAML(version) }.unique().mix(Channel.of(workflowVersionToYAML()))
                                                                                                   ^^^^^^^
  ```

- Warning: `workflows/pacvar.nf:59:19`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_versions = Channel.empty()
                    ^^^^^^^
  ```

- Warning: `workflows/pacvar.nf:63:22`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
          ch_barcode = Channel.value(file(params.barcodes))
                       ^^^^^^^
  ```

- Warning: `workflows/pacvar.nf:87:59`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
      pbmm2_input_filter_ch = pbmm2_input_ch.filter { meta, bam ->
                                                            ^^^
  ```

- Warning: `workflows/pacvar.nf:114:23`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
              .filter { meta, bams -> bams.size() > 1 }
                        ^^^^
  ```

- Warning: `workflows/pacvar.nf:119:23`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
              .filter { meta, bams -> bams.size() == 1 }
                        ^^^^
  ```

- Warning: `workflows/pacvar.nf:138:50`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
      ordered_bam_ch = bam_bai_ch.map { meta, bam, bai -> [meta, bam] }
                                                   ^^^
  ```

- Warning: `workflows/pacvar.nf:139:45`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
      ordered_bai_ch = bam_bai_ch.map { meta, bam, bai -> [meta, bai] }
                                              ^^^
  ```

- Warning: `workflows/pacvar.nf:216:24`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_multiqc_files = Channel.empty()
                         ^^^^^^^
  ```

- Warning: `workflows/pacvar.nf:230:32`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_multiqc_config        = Channel.fromPath(
                                 ^^^^^^^
  ```

- Warning: `workflows/pacvar.nf:233:9`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
          Channel.fromPath(params.multiqc_config, checkIfExists: true) :
          ^^^^^^^
  ```

- Warning: `workflows/pacvar.nf:234:9`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
          Channel.empty()
          ^^^^^^^
  ```

- Warning: `workflows/pacvar.nf:236:9`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
          Channel.fromPath(params.multiqc_logo, checkIfExists: true) :
          ^^^^^^^
  ```

- Warning: `workflows/pacvar.nf:237:9`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
          Channel.empty()
          ^^^^^^^
  ```

- Warning: `workflows/pacvar.nf:241:27`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_workflow_summary = Channel.value(paramsSummaryMultiqc(summary_params))
                            ^^^^^^^
  ```

- Warning: `workflows/pacvar.nf:249:45`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_methods_description                = Channel.value(
                                              ^^^^^^^
  ```
