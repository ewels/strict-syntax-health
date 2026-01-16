# Nextflow lint results

- Generated: 2026-01-16T06:27:57.791232845Z
- Nextflow version: 25.12.0-edge
- Summary: 26 errors, 64 warnings

## :x: Errors

- Error: `main.nf:39:1`: Statements cannot be mixed with script declarations -- move statements into a process, workflow, or function

  ```nextflow
  exon6fai          = params.exon6fai   ? Channel.fromPath(params.exon6fai).map { it -> [[id: it.baseName, exon: 'exon6'], it] }   : Channel.empty()
  ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  ```

- Error: `main.nf:40:1`: Statements cannot be mixed with script declarations -- move statements into a process, workflow, or function

  ```nextflow
  exon6fasta        = params.exon6fasta ? Channel.fromPath(params.exon6fasta).map { it -> [[id: it.baseName, exon: 'exon6'], it] } : Channel.empty()
  ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  ```

- Error: `main.nf:41:1`: Statements cannot be mixed with script declarations -- move statements into a process, workflow, or function

  ```nextflow
  exon7fai          = params.exon7fai   ? Channel.fromPath(params.exon7fai).map { it -> [[id: it.baseName, exon: 'exon7'], it] }   : Channel.empty()
  ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  ```

- Error: `main.nf:42:1`: Statements cannot be mixed with script declarations -- move statements into a process, workflow, or function

  ```nextflow
  exon7fasta        = params.exon7fasta ? Channel.fromPath(params.exon7fasta).map { it -> [[id: it.baseName, exon: 'exon7'], it] } : Channel.empty()
  ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  ```

- Error: `main.nf:43:1`: Statements cannot be mixed with script declarations -- move statements into a process, workflow, or function

  ```nextflow
  logo              = params.logo       ? Channel.fromPath(params.logo).collect()                                                  : Channel.empty()
  ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  ```

- Error: `main.nf:60:9`: `exon6fai` is not defined

  ```nextflow
          exon6fai,
          ^^^^^^^^
  ```

- Error: `main.nf:61:9`: `exon6fasta` is not defined

  ```nextflow
          exon6fasta,
          ^^^^^^^^^^
  ```

- Error: `main.nf:62:9`: `exon7fai` is not defined

  ```nextflow
          exon7fai,
          ^^^^^^^^
  ```

- Error: `main.nf:63:9`: `exon7fasta` is not defined

  ```nextflow
          exon7fasta,
          ^^^^^^^^^^
  ```

- Error: `main.nf:64:9`: `logo` is not defined

  ```nextflow
          logo
          ^^^^
  ```

- Error: `nextflow.config:314:32`: `manifest` is not defined

  ```nextflow
  \033[0;35m  nf-core/abotyper ${manifest.version}\033[0m
                                 ^^^^^^^^
  ```

- Error: `nextflow.config:317:26`: `manifest` is not defined

  ```nextflow
          afterText = """${manifest.doi ? "\n* The pipeline\n" : ""}${manifest.doi.tokenize(",").collect { "    https://doi.org/${it.trim().replace('https://doi.org/','')}"}.join("\n")}${manifest.doi ? "\n" : ""}
                           ^^^^^^^^
  ```

- Error: `nextflow.config:317:69`: `manifest` is not defined

  ```nextflow
          afterText = """${manifest.doi ? "\n* The pipeline\n" : ""}${manifest.doi.tokenize(",").collect { "    https://doi.org/${it.trim().replace('https://doi.org/','')}"}.join("\n")}${manifest.doi ? "\n" : ""}
                                                                      ^^^^^^^^
  ```

- Error: `nextflow.config:317:186`: `manifest` is not defined

  ```nextflow
          afterText = """${manifest.doi ? "\n* The pipeline\n" : ""}${manifest.doi.tokenize(",").collect { "    https://doi.org/${it.trim().replace('https://doi.org/','')}"}.join("\n")}${manifest.doi ? "\n" : ""}
                                                                                                                                                                                           ^^^^^^^^
  ```

- Error: `nextflow.config:326:22`: `validation` is not defined

  ```nextflow
          beforeText = validation.help.beforeText
                       ^^^^^^^^^^
  ```

- Error: `nextflow.config:327:21`: `validation` is not defined

  ```nextflow
          afterText = validation.help.afterText
                      ^^^^^^^^^^
  ```

- Error: `subworkflows/local/minimap_align_exons/main.nf:41:19`: Unexpected input: '='

  ```nextflow
          bam_format="bam",
                    ^
  ```

- Error: `workflows/abotyper.nf:19:1`: Module could not be parsed: '/home/runner/work/strict-syntax-health/strict-syntax-health/pipelines/abotyper/subworkflows/local/minimap_align_exons/main.nf'

  ```nextflow
  include { MINIMAP2_ALIGN_READS    } from '../subworkflows/local/minimap_align_exons/main'
  ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  ```

- Error: `workflows/abotyper.nf:82:5`: `MINIMAP2_ALIGN_READS` is not defined

  ```nextflow
      MINIMAP2_ALIGN_READS (
      ^^^^^^^^^^^^^^^^^^^^
  ```

- Error: `workflows/abotyper.nf:87:35`: `MINIMAP2_ALIGN_READS` is not defined

  ```nextflow
      ch_versions = ch_versions.mix(MINIMAP2_ALIGN_READS.out.versions)
                                    ^^^^^^^^^^^^^^^^^^^^
  ```

- Error: `workflows/abotyper.nf:93:9`: `MINIMAP2_ALIGN_READS` is not defined

  ```nextflow
          MINIMAP2_ALIGN_READS.out.bam,
          ^^^^^^^^^^^^^^^^^^^^
  ```

- Error: `workflows/abotyper.nf:94:9`: `MINIMAP2_ALIGN_READS` is not defined

  ```nextflow
          MINIMAP2_ALIGN_READS.out.bai,
          ^^^^^^^^^^^^^^^^^^^^
  ```

- Error: `workflows/abotyper.nf:95:9`: `MINIMAP2_ALIGN_READS` is not defined

  ```nextflow
          MINIMAP2_ALIGN_READS.out.fasta,
          ^^^^^^^^^^^^^^^^^^^^
  ```

- Error: `workflows/abotyper.nf:96:9`: `MINIMAP2_ALIGN_READS` is not defined

  ```nextflow
          MINIMAP2_ALIGN_READS.out.fai,
          ^^^^^^^^^^^^^^^^^^^^
  ```

- Error: `workflows/abotyper.nf:106:15`: `MINIMAP2_ALIGN_READS` is not defined

  ```nextflow
          .join(MINIMAP2_ALIGN_READS.out.coverage)
                ^^^^^^^^^^^^^^^^^^^^
  ```

- Error: `workflows/abotyper.nf:139:14`: `MINIMAP2_ALIGN_READS` is not defined

  ```nextflow
          .mix(MINIMAP2_ALIGN_READS.out.coverage.map { meta, cov -> cov })
               ^^^^^^^^^^^^^^^^^^^^
  ```

## :warning: Warnings

- Warning: `main.nf:39:1`: Variable was declared but not used

  ```nextflow
  exon6fai          = params.exon6fai   ? Channel.fromPath(params.exon6fai).map { it -> [[id: it.baseName, exon: 'exon6'], it] }   : Channel.empty()
  ^^^^^^^^
  ```

- Warning: `main.nf:39:41`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
  exon6fai          = params.exon6fai   ? Channel.fromPath(params.exon6fai).map { it -> [[id: it.baseName, exon: 'exon6'], it] }   : Channel.empty()
                                          ^^^^^^^
  ```

- Warning: `main.nf:39:132`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
  exon6fai          = params.exon6fai   ? Channel.fromPath(params.exon6fai).map { it -> [[id: it.baseName, exon: 'exon6'], it] }   : Channel.empty()
                                                                                                                                     ^^^^^^^
  ```

- Warning: `main.nf:40:1`: Variable was declared but not used

  ```nextflow
  exon6fasta        = params.exon6fasta ? Channel.fromPath(params.exon6fasta).map { it -> [[id: it.baseName, exon: 'exon6'], it] } : Channel.empty()
  ^^^^^^^^^^
  ```

- Warning: `main.nf:40:41`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
  exon6fasta        = params.exon6fasta ? Channel.fromPath(params.exon6fasta).map { it -> [[id: it.baseName, exon: 'exon6'], it] } : Channel.empty()
                                          ^^^^^^^
  ```

- Warning: `main.nf:40:132`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
  exon6fasta        = params.exon6fasta ? Channel.fromPath(params.exon6fasta).map { it -> [[id: it.baseName, exon: 'exon6'], it] } : Channel.empty()
                                                                                                                                     ^^^^^^^
  ```

- Warning: `main.nf:41:1`: Variable was declared but not used

  ```nextflow
  exon7fai          = params.exon7fai   ? Channel.fromPath(params.exon7fai).map { it -> [[id: it.baseName, exon: 'exon7'], it] }   : Channel.empty()
  ^^^^^^^^
  ```

- Warning: `main.nf:41:41`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
  exon7fai          = params.exon7fai   ? Channel.fromPath(params.exon7fai).map { it -> [[id: it.baseName, exon: 'exon7'], it] }   : Channel.empty()
                                          ^^^^^^^
  ```

- Warning: `main.nf:41:132`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
  exon7fai          = params.exon7fai   ? Channel.fromPath(params.exon7fai).map { it -> [[id: it.baseName, exon: 'exon7'], it] }   : Channel.empty()
                                                                                                                                     ^^^^^^^
  ```

- Warning: `main.nf:42:1`: Variable was declared but not used

  ```nextflow
  exon7fasta        = params.exon7fasta ? Channel.fromPath(params.exon7fasta).map { it -> [[id: it.baseName, exon: 'exon7'], it] } : Channel.empty()
  ^^^^^^^^^^
  ```

- Warning: `main.nf:42:41`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
  exon7fasta        = params.exon7fasta ? Channel.fromPath(params.exon7fasta).map { it -> [[id: it.baseName, exon: 'exon7'], it] } : Channel.empty()
                                          ^^^^^^^
  ```

- Warning: `main.nf:42:132`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
  exon7fasta        = params.exon7fasta ? Channel.fromPath(params.exon7fasta).map { it -> [[id: it.baseName, exon: 'exon7'], it] } : Channel.empty()
                                                                                                                                     ^^^^^^^
  ```

- Warning: `main.nf:43:1`: Variable was declared but not used

  ```nextflow
  logo              = params.logo       ? Channel.fromPath(params.logo).collect()                                                  : Channel.empty()
  ^^^^
  ```

- Warning: `main.nf:43:41`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
  logo              = params.logo       ? Channel.fromPath(params.logo).collect()                                                  : Channel.empty()
                                          ^^^^^^^
  ```

- Warning: `main.nf:43:132`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
  logo              = params.logo       ? Channel.fromPath(params.logo).collect()                                                  : Channel.empty()
                                                                                                                                     ^^^^^^^
  ```

- Warning: `modules/local/abo/abosnps/main.nf:19:9`: Variable was declared but not used

  ```nextflow
      def args = task.ext.args ?: ''
          ^^^^
  ```

- Warning: `modules/local/abo/snps2pheno/main.nf:31:13`: The use of `projectDir` in a process is discouraged -- input files should be provided as process inputs

  ```nextflow
      python3 $projectDir/bin/aggregate_abo_reports.py \\
              ^^^^^^^^^^
  ```

- Warning: `modules/local/mpileupstats/main.nf:36:9`: Variable was declared but not used

  ```nextflow
      def args = task.ext.args ?: ''
          ^^^^
  ```

- Warning: `modules/local/mpileupstats/main.nf:40:13`: The use of `projectDir` in a process is discouraged -- input files should be provided as process inputs

  ```nextflow
      python3 $projectDir/bin/stats_from_pileup.py \\
              ^^^^^^^^^^
  ```

- Warning: `modules/nf-core/minimap2/align/main.nf:67:9`: Variable was declared but not used

  ```nextflow
      def target = reference ?: (bam_input ? error("BAM input requires reference") : reads)
          ^^^^^^
  ```

- Warning: `nextflow.config:317:129`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          afterText = """${manifest.doi ? "\n* The pipeline\n" : ""}${manifest.doi.tokenize(",").collect { "    https://doi.org/${it.trim().replace('https://doi.org/','')}"}.join("\n")}${manifest.doi ? "\n" : ""}
                                                                                                                                  ^^
  ```

- Warning: `subworkflows/local/predictabophenotype/main.nf:19:19`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_versions = Channel.empty()
                    ^^^^^^^
  ```

- Warning: `subworkflows/local/predictabophenotype/main.nf:46:51`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
                  def exon_dir = sample_dir.resolve(it.exon)
                                                    ^^
  ```

- Warning: `subworkflows/local/predictabophenotype/main.nf:48:17`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
                  it.file.copyTo(exon_dir.resolve(it.file.name))
                  ^^
  ```

- Warning: `subworkflows/local/predictabophenotype/main.nf:48:49`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
                  it.file.copyTo(exon_dir.resolve(it.file.name))
                                                  ^^
  ```

- Warning: `subworkflows/local/predictabophenotype/main.nf:55:32`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_per_sample_processing = Channel.fromPath("${params.outdir}/per_sample_processing", type: 'dir')
                                 ^^^^^^^
  ```

- Warning: `subworkflows/local/utils_nfcore_abotyper_pipeline/main.nf:31:5`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
      monochrome_logs   // boolean: Do not use coloured log outputs
      ^^^^^^^^^^^^^^^
  ```

- Warning: `subworkflows/local/utils_nfcore_abotyper_pipeline/main.nf:34:5`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
      input             //  string: Path to input samplesheet
      ^^^^^
  ```

- Warning: `subworkflows/local/utils_nfcore_abotyper_pipeline/main.nf:38:19`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_versions = Channel.empty()
                    ^^^^^^^
  ```

- Warning: `subworkflows/local/utils_nfcore_abotyper_pipeline/main.nf:75:5`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      Channel
      ^^^^^^^
  ```

- Warning: `subworkflows/local/variant_calling_mpileup/main.nf:8:5`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
      ch_bai       // channel: [ val(meta), path(bai)]    - BAI file from minimap2 alignment
      ^^^^^^
  ```

- Warning: `subworkflows/local/variant_calling_mpileup/main.nf:10:5`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
      ch_fai       // channel: [ val(meta1), path(fai)]   - fasta index for the references
      ^^^^^^
  ```

- Warning: `subworkflows/local/variant_calling_mpileup/main.nf:15:19`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_versions = Channel.empty()
                    ^^^^^^^
  ```

- Warning: `subworkflows/local/variant_calling_mpileup/main.nf:20:29`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          .filter { bam_meta, bam, bed_meta, bed ->
                              ^^^
  ```

- Warning: `subworkflows/local/variant_calling_mpileup/main.nf:20:44`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          .filter { bam_meta, bam, bed_meta, bed ->
                                             ^^^
  ```

- Warning: `subworkflows/local/variant_calling_mpileup/main.nf:24:31`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          .map { bam_meta, bam, bed_meta, bed ->
                                ^^^^^^^^
  ```

- Warning: `subworkflows/local/variant_calling_mpileup/main.nf:31:29`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          .filter { bam_meta, bam, bed, fasta_meta, fasta ->
                              ^^^
  ```

- Warning: `subworkflows/local/variant_calling_mpileup/main.nf:31:34`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          .filter { bam_meta, bam, bed, fasta_meta, fasta ->
                                   ^^^
  ```

- Warning: `subworkflows/local/variant_calling_mpileup/main.nf:31:51`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          .filter { bam_meta, bam, bed, fasta_meta, fasta ->
                                                    ^^^^^
  ```

- Warning: `subworkflows/local/variant_calling_mpileup/main.nf:43:52`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          ch_fasta_matched.map { bam_meta, bam, bed, fasta_meta, fasta -> [bam_meta, bam, bed] },
                                                     ^^^^^^^^^^
  ```

- Warning: `subworkflows/local/variant_calling_mpileup/main.nf:43:64`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          ch_fasta_matched.map { bam_meta, bam, bed, fasta_meta, fasta -> [bam_meta, bam, bed] },
                                                                 ^^^^^
  ```

- Warning: `subworkflows/local/variant_calling_mpileup/main.nf:44:32`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          ch_fasta_matched.map { bam_meta, bam, bed, fasta_meta, fasta -> [fasta_meta, fasta] }
                                 ^^^^^^^^
  ```

- Warning: `subworkflows/local/variant_calling_mpileup/main.nf:44:42`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          ch_fasta_matched.map { bam_meta, bam, bed, fasta_meta, fasta -> [fasta_meta, fasta] }
                                           ^^^
  ```

- Warning: `subworkflows/local/variant_calling_mpileup/main.nf:44:47`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          ch_fasta_matched.map { bam_meta, bam, bed, fasta_meta, fasta -> [fasta_meta, fasta] }
                                                ^^^
  ```

- Warning: `subworkflows/local/variant_calling_mpileup/main.nf:52:33`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          .filter { mpileup_meta, mpileup, fasta_meta, fasta ->
                                  ^^^^^^^
  ```

- Warning: `subworkflows/local/variant_calling_mpileup/main.nf:52:54`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          .filter { mpileup_meta, mpileup, fasta_meta, fasta ->
                                                       ^^^^^
  ```

- Warning: `subworkflows/local/variant_calling_mpileup/main.nf:60:57`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          ch_nucl_freq_input.map { mpileup_meta, mpileup, fasta_meta, fasta -> [mpileup_meta, mpileup] },
                                                          ^^^^^^^^^^
  ```

- Warning: `subworkflows/local/variant_calling_mpileup/main.nf:60:69`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          ch_nucl_freq_input.map { mpileup_meta, mpileup, fasta_meta, fasta -> [mpileup_meta, mpileup] },
                                                                      ^^^^^
  ```

- Warning: `subworkflows/local/variant_calling_mpileup/main.nf:61:34`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          ch_nucl_freq_input.map { mpileup_meta, mpileup, fasta_meta, fasta -> [fasta_meta, fasta] }
                                   ^^^^^^^^^^^^
  ```

- Warning: `subworkflows/local/variant_calling_mpileup/main.nf:61:48`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          ch_nucl_freq_input.map { mpileup_meta, mpileup, fasta_meta, fasta -> [fasta_meta, fasta] }
                                                 ^^^^^^^
  ```

- Warning: `subworkflows/nf-core/utils_nfcore_pipeline/main.nf:101:98`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      return ch_versions.unique().map { version -> processVersionsFromYAML(version) }.unique().mix(Channel.of(workflowVersionToYAML()))
                                                                                                   ^^^^^^^
  ```

- Warning: `workflows/abotyper.nf:39:5`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
      logo           // channel: png from params.logo (custom pathwest logo)
      ^^^^
  ```

- Warning: `workflows/abotyper.nf:43:19`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_versions = Channel.empty()
                    ^^^^^^^
  ```

- Warning: `workflows/abotyper.nf:129:27`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_workflow_summary = Channel.value(paramsSummaryMultiqc(summary_params))
                            ^^^^^^^
  ```

- Warning: `workflows/abotyper.nf:134:30`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_methods_description = Channel.value(methodsDescriptionText(ch_multiqc_custom_methods_description))
                               ^^^^^^^
  ```

- Warning: `workflows/abotyper.nf:137:25`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_multiqc_inputs = Channel.empty()
                          ^^^^^^^
  ```

- Warning: `workflows/abotyper.nf:138:35`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          .mix(FASTQC.out.zip.map { meta, files -> files }.flatten())
                                    ^^^^
  ```

- Warning: `workflows/abotyper.nf:139:54`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          .mix(MINIMAP2_ALIGN_READS.out.coverage.map { meta, cov -> cov })
                                                       ^^^^
  ```

- Warning: `workflows/abotyper.nf:140:56`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          .mix(VARIANTS_QUANTIFICATION.out.metrics.map { meta, metrics -> metrics })
                                                         ^^^^
  ```

- Warning: `workflows/abotyper.nf:145:32`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_multiqc_config        = Channel.fromPath(
                                 ^^^^^^^
  ```

- Warning: `workflows/abotyper.nf:148:9`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
          Channel.fromPath(params.multiqc_config, checkIfExists: true) :
          ^^^^^^^
  ```

- Warning: `workflows/abotyper.nf:149:9`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
          Channel.empty()
          ^^^^^^^
  ```

- Warning: `workflows/abotyper.nf:151:9`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
          Channel.fromPath(params.multiqc_logo, checkIfExists: true) :
          ^^^^^^^
  ```

- Warning: `workflows/abotyper.nf:152:9`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
          Channel.empty()
          ^^^^^^^
  ```
