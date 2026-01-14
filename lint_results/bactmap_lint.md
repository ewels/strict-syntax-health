# Nextflow lint results

- Generated: 2026-01-14T09:09:37.453846430Z
- Nextflow version: 25.12.0-edge
- Summary: 27 errors, 64 warnings

## :x: Errors

- Error: `main.nf:18:1`: Included name 'BACTMAP' is not defined in module '/home/runner/work/strict-syntax-health/strict-syntax-health/pipelines/bactmap/workflows/bactmap.nf'

  ```nextflow
  include { BACTMAP                 } from './workflows/bactmap'
  ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  ```

- Error: `main.nf:59:5`: `BACTMAP` is not defined

  ```nextflow
      BACTMAP (
      ^^^^^^^
  ```

- Error: `main.nf:64:22`: `BACTMAP` is not defined

  ```nextflow
      multiqc_report = BACTMAP.out.multiqc_report // channel: /path/to/multiqc_report.html
                       ^^^^^^^
  ```

- Error: `modules/local/alignpseudogenomes/main.nf:14:15`: `NUM_ALIGNMENT_GENOMES` is not defined

  ```nextflow
      tuple env(NUM_ALIGNMENT_GENOMES), path("aligned_pseudogenomes.fas"), emit: aligned_pseudogenomes
                ^^^^^^^^^^^^^^^^^^^^^
  ```

- Error: `modules/local/read_stats/main.nf:11:39`: `json` is already declared

  ```nextflow
      tuple val(meta), path(json), path(json)
                                        ^^^^
  ```

- Error: `modules/nf-core/snpsites/main.nf:16:11`: `CONSTANT_SITES` is not defined

  ```nextflow
      env   CONSTANT_SITES, emit: constant_sites_string
            ^^^^^^^^^^^^^^
  ```

- Error: `nextflow.config:351:31`: `manifest` is not defined

  ```nextflow
  \033[0;35m  nf-core/bactmap ${manifest.version}\033[0m
                                ^^^^^^^^
  ```

- Error: `nextflow.config:354:26`: `manifest` is not defined

  ```nextflow
          afterText = """${manifest.doi ? "\n* The pipeline\n" : ""}${manifest.doi.tokenize(",").collect { "    https://doi.org/${it.trim().replace('https://doi.org/','')}"}.join("\n")}${manifest.doi ? "\n" : ""}
                           ^^^^^^^^
  ```

- Error: `nextflow.config:354:69`: `manifest` is not defined

  ```nextflow
          afterText = """${manifest.doi ? "\n* The pipeline\n" : ""}${manifest.doi.tokenize(",").collect { "    https://doi.org/${it.trim().replace('https://doi.org/','')}"}.join("\n")}${manifest.doi ? "\n" : ""}
                                                                      ^^^^^^^^
  ```

- Error: `nextflow.config:354:186`: `manifest` is not defined

  ```nextflow
          afterText = """${manifest.doi ? "\n* The pipeline\n" : ""}${manifest.doi.tokenize(",").collect { "    https://doi.org/${it.trim().replace('https://doi.org/','')}"}.join("\n")}${manifest.doi ? "\n" : ""}
                                                                                                                                                                                           ^^^^^^^^
  ```

- Error: `nextflow.config:363:22`: `validation` is not defined

  ```nextflow
          beforeText = validation.help.beforeText
                       ^^^^^^^^^^
  ```

- Error: `nextflow.config:364:21`: `validation` is not defined

  ```nextflow
          afterText = validation.help.afterText
                      ^^^^^^^^^^
  ```

- Error: `subworkflows/local/longread_adapterremoval/main.nf:19:26`: `reads` is already declared

  ```nextflow
              .map { meta, reads -> [meta + [ single_end: true ], reads ] }
                           ^^^^^
  ```

- Error: `subworkflows/local/longread_adapterremoval/main.nf:25:26`: `reads` is already declared

  ```nextflow
              .map { meta, reads -> [ meta + [ single_end: true ], reads ] }
                           ^^^^^
  ```

- Error: `subworkflows/local/longread_filtering/main.nf:18:58`: `reads` is already declared

  ```nextflow
          ch_filtered_reads = FILTLONG ( reads.map { meta, reads -> [ meta, [], reads ] } ).reads
                                                           ^^^^^
  ```

- Error: `subworkflows/local/longread_preprocessing/main.nf:29:26`: `reads` is already declared

  ```nextflow
              .map { meta, reads -> [ meta + [single_end: true], reads ] }
                           ^^^^^
  ```

- Error: `subworkflows/local/shortread_adapterremoval/main.nf:42:26`: `reads` is already declared

  ```nextflow
              .map { meta, reads ->
                           ^^^^^
  ```

- Error: `subworkflows/local/shortread_adapterremoval/main.nf:63:26`: `reads` is already declared

  ```nextflow
              .map { meta, reads ->
                           ^^^^^
  ```

- Error: `subworkflows/local/shortread_fastp/main.nf:30:51`: `reads` is already declared

  ```nextflow
                                              meta, reads ->
                                                    ^^^^^
  ```

- Error: `workflows/bactmap.nf:12:1`: Statements cannot be mixed with script declarations -- move statements into a process or workflow

  ```nextflow
  def checkPathParamList = [ params.input, params.fasta, params.multiqc_config,
  ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  ```

- Error: `workflows/bactmap.nf:16:1`: `for` loops are no longer supported

  ```nextflow
  for (param in checkPathParamList) { if (param) { file(param, checkIfExists: true) } }
  ^^^
  ```

- Error: `workflows/bactmap.nf:16:1`: Statements cannot be mixed with script declarations -- move statements into a process or workflow

  ```nextflow
  for (param in checkPathParamList) { if (param) { file(param, checkIfExists: true) } }
  ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  ```

- Error: `workflows/bactmap.nf:16:6`: `param` is not defined

  ```nextflow
  for (param in checkPathParamList) { if (param) { file(param, checkIfExists: true) } }
       ^^^^^
  ```

- Error: `workflows/bactmap.nf:16:40`: `param` is not defined

  ```nextflow
  for (param in checkPathParamList) { if (param) { file(param, checkIfExists: true) } }
                                         ^^^^^^^
  ```

- Error: `workflows/bactmap.nf:16:55`: `param` is not defined

  ```nextflow
  for (param in checkPathParamList) { if (param) { file(param, checkIfExists: true) } }
                                                        ^^^^^
  ```

- Error: `workflows/bactmap.nf:19:1`: Statements cannot be mixed with script declarations -- move statements into a process or workflow

  ```nextflow
  if ( params.input ) {
  ^
  ```

- Error: `workflows/bactmap.nf:76:1`: Invalid workflow definition -- check for missing or out-of-order section labels

  ```nextflow
  workflow BACTMAP {
  ^
  ```

## :warning: Warnings

- Warning: `conf/modules.config:109:191`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
                  saveAs: { ( params.perform_runmerging == false || ( params.perform_runmerging && !meta.is_multirun ) )  && params.perform_shortread_qc && params.save_analysis_ready_fastqs ? it : null }
                                                                                                                                                                                                ^^
  ```

- Warning: `conf/modules.config:144:191`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
                  saveAs:  { ( params.perform_runmerging == false || ( params.perform_runmerging && !meta.is_multirun ) ) && params.perform_shortread_qc && params.save_analysis_ready_fastqs ? it : null }
                                                                                                                                                                                                ^^
  ```

- Warning: `conf/modules.config:174:190`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
                  saveAs: { ( params.perform_runmerging == false || ( params.perform_runmerging && !meta.is_multirun ) ) && params.perform_shortread_qc && params.save_analysis_ready_fastqs ? it : null }
                                                                                                                                                                                               ^^
  ```

- Warning: `conf/modules.config:207:225`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
                  saveAs: { ( params.perform_runmerging == false || ( params.perform_runmerging && !meta.is_multirun ) ) && params.perform_shortread_qc && !params.shortread_qc_mergepairs && params.save_analysis_ready_fastqs ? it : null}
                                                                                                                                                                                                                                  ^^
  ```

- Warning: `conf/modules.config:231:308`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
                  saveAs: { ( params.perform_runmerging == false || ( params.perform_runmerging && !meta.is_multirun ) ) && !params.perform_longread_hostremoval && params.longread_qc_skipqualityfilter && !params.longread_qc_skipadaptertrim && params.perform_longread_qc && params.save_analysis_ready_fastqs ? it : null }
                                                                                                                                                                                                                                                                                                                     ^^
  ```

- Warning: `conf/modules.config:255:308`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
                  saveAs: { ( params.perform_runmerging == false || ( params.perform_runmerging && !meta.is_multirun ) ) && !params.perform_longread_hostremoval && params.longread_qc_skipqualityfilter && !params.longread_qc_skipadaptertrim && params.perform_longread_qc && params.save_analysis_ready_fastqs ? it : null }
                                                                                                                                                                                                                                                                                                                     ^^
  ```

- Warning: `conf/modules.config:285:270`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
                  saveAs: { ( params.perform_runmerging == false || ( params.perform_runmerging && !meta.is_multirun ) ) && !params.perform_longread_hostremoval && !params.longread_qc_skipqualityfilter && params.perform_longread_qc && params.save_analysis_ready_fastqs ? it : null }
                                                                                                                                                                                                                                                                               ^^
  ```

- Warning: `conf/modules.config:315:270`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
                  saveAs: { ( params.perform_runmerging == false || ( params.perform_runmerging && !meta.is_multirun ) ) && !params.perform_longread_hostremoval && !params.longread_qc_skipqualityfilter && params.perform_longread_qc && params.save_analysis_ready_fastqs ? it : null }
                                                                                                                                                                                                                                                                               ^^
  ```

- Warning: `conf/modules.config:364:190`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
                  saveAs: { ( params.perform_runmerging == false || ( params.perform_runmerging && !meta.is_multirun ) ) && params.perform_shortread_qc && params.save_analysis_ready_fastqs ? it : null }
                                                                                                                                                                                               ^^
  ```

- Warning: `main.nf:50:20`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
          ch_fasta = Channel.fromPath(params.fasta, checkIfExists: true).collect()
                     ^^^^^^^
  ```

- Warning: `modules/local/bcftools/consensus/main.nf:46:9`: Variable was declared but not used

  ```nextflow
      def args = task.ext.args ?: ''
          ^^^^
  ```

- Warning: `modules/local/bcftools/consensus/main.nf:48:9`: Variable was declared but not used

  ```nextflow
      def masking = mask ? "-m $mask" : ""
          ^^^^^^^
  ```

- Warning: `modules/local/bedtools/genomecov/main.nf:30:9`: Variable was declared but not used

  ```nextflow
      def buffer   = task.memory ? "--buffer-size=${task.memory.toGiga().intdiv(2)}G" : ''
          ^^^^^^
  ```

- Warning: `modules/local/clair3/main.nf:46:9`: Variable was declared but not used

  ```nextflow
      def args = task.ext.args ?: ''
          ^^^^
  ```

- Warning: `modules/local/read_stats/main.nf:11:27`: Variable was declared but not used

  ```nextflow
      tuple val(meta), path(json), path(json)
                            ^^^^
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

- Warning: `modules/nf-core/nanoq/main.nf:38:9`: Variable was declared but not used

  ```nextflow
      def args = task.ext.args ?: ''
          ^^^^
  ```

- Warning: `modules/nf-core/porechop/abi/main.nf:44:9`: Variable was declared but not used

  ```nextflow
      def args = task.ext.args ?: ''
          ^^^^
  ```

- Warning: `modules/nf-core/porechop/abi/main.nf:46:9`: Variable was declared but not used

  ```nextflow
      def adapters_list = custom_adapters ? "--custom_adapters ${custom_adapters}" : ""
          ^^^^^^^^^^^^^
  ```

- Warning: `modules/nf-core/seqtk/comp/main.nf:37:9`: Variable was declared but not used

  ```nextflow
      def args = task.ext.args ?: ''
          ^^^^
  ```

- Warning: `nextflow.config:354:129`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          afterText = """${manifest.doi ? "\n* The pipeline\n" : ""}${manifest.doi.tokenize(",").collect { "    https://doi.org/${it.trim().replace('https://doi.org/','')}"}.join("\n")}${manifest.doi ? "\n" : ""}
                                                                                                                                  ^^
  ```

- Warning: `subworkflows/local/bam_variant_calling_sort_freebayes_bcftools/main.nf:16:19`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_versions = Channel.empty()
                    ^^^^^^^
  ```

- Warning: `subworkflows/local/bam_variant_calling_sort_freebayes_bcftools/main.nf:19:58`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
      FREEBAYES ( ch_input, ch_fasta_fai.map{ meta, fasta, fai -> [ meta, fasta ] }, ch_fasta_fai.map{ meta, fasta, fai -> [ meta, fai ] }, ch_samples, ch_populations, ch_cnv )
                                                           ^^^
  ```

- Warning: `subworkflows/local/bam_variant_calling_sort_freebayes_bcftools/main.nf:19:108`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
      FREEBAYES ( ch_input, ch_fasta_fai.map{ meta, fasta, fai -> [ meta, fasta ] }, ch_fasta_fai.map{ meta, fasta, fai -> [ meta, fai ] }, ch_samples, ch_populations, ch_cnv )
                                                                                                             ^^^^^
  ```

- Warning: `subworkflows/local/consensus_bcftools/main.nf:21:19`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_versions = Channel.empty()
                    ^^^^^^^
  ```

- Warning: `subworkflows/local/fastq_align_bwamem2/main.nf:14:19`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_versions = Channel.empty()
                    ^^^^^^^
  ```

- Warning: `subworkflows/local/longread_adapterremoval/main.nf:13:24`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_versions      = Channel.empty()
                         ^^^^^^^
  ```

- Warning: `subworkflows/local/longread_adapterremoval/main.nf:14:24`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_multiqc_files = Channel.empty()
                         ^^^^^^^
  ```

- Warning: `subworkflows/local/longread_filtering/main.nf:13:25`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_versions       = Channel.empty()
                          ^^^^^^^
  ```

- Warning: `subworkflows/local/longread_filtering/main.nf:14:25`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_multiqc_files  = Channel.empty()
                          ^^^^^^^
  ```

- Warning: `subworkflows/local/longread_mapping/main.nf:23:24`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_versions      = Channel.empty()
                         ^^^^^^^
  ```

- Warning: `subworkflows/local/longread_mapping/main.nf:24:24`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_multiqc_files = Channel.empty()
                         ^^^^^^^
  ```

- Warning: `subworkflows/local/longread_preprocessing/main.nf:15:24`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_versions      = Channel.empty()
                         ^^^^^^^
  ```

- Warning: `subworkflows/local/longread_preprocessing/main.nf:16:24`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_multiqc_files = Channel.empty()
                         ^^^^^^^
  ```

- Warning: `subworkflows/local/minimap2_alignment/main.nf:13:19`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_versions = Channel.empty()
                    ^^^^^^^
  ```

- Warning: `subworkflows/local/shortread_adapterremoval/main.nf:16:24`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_versions      = Channel.empty()
                         ^^^^^^^
  ```

- Warning: `subworkflows/local/shortread_adapterremoval/main.nf:17:24`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_multiqc_files = Channel.empty()
                         ^^^^^^^
  ```

- Warning: `subworkflows/local/shortread_adapterremoval/main.nf:21:49`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
                                          single: it[0].single_end
                                                  ^^
  ```

- Warning: `subworkflows/local/shortread_adapterremoval/main.nf:22:50`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
                                          paired: !it[0].single_end
                                                   ^^
  ```

- Warning: `subworkflows/local/shortread_adapterremoval/main.nf:35:27`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
          ch_concat_fastq = Channel.empty()
                            ^^^^^^^
  ```

- Warning: `subworkflows/local/shortread_adapterremoval/main.nf:58:27`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
          ch_concat_fastq = Channel.empty()
                            ^^^^^^^
  ```

- Warning: `subworkflows/local/shortread_fastp/main.nf:14:29`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_versions           = Channel.empty()
                              ^^^^^^^
  ```

- Warning: `subworkflows/local/shortread_fastp/main.nf:15:29`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_multiqc_files      = Channel.empty()
                              ^^^^^^^
  ```

- Warning: `subworkflows/local/shortread_fastp/main.nf:19:41`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
                                  single: it[0]['single_end'] == true
                                          ^^
  ```

- Warning: `subworkflows/local/shortread_fastp/main.nf:20:41`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
                                  paired: it[0]['single_end'] == false
                                          ^^
  ```

- Warning: `subworkflows/local/shortread_fastp/main.nf:31:53`: Variable was declared but not used

  ```nextflow
                                                  def meta_new = meta + [single_end: true]
                                                      ^^^^^^^^
  ```

- Warning: `subworkflows/local/shortread_mapping/main.nf:22:24`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_versions      = Channel.empty()
                         ^^^^^^^
  ```

- Warning: `subworkflows/local/shortread_mapping/main.nf:23:24`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_multiqc_files = Channel.empty()
                         ^^^^^^^
  ```

- Warning: `subworkflows/local/shortread_preprocessing/main.nf:11:25`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_versions       = Channel.empty()
                          ^^^^^^^
  ```

- Warning: `subworkflows/local/shortread_preprocessing/main.nf:12:25`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_multiqc_files  = Channel.empty()
                          ^^^^^^^
  ```

- Warning: `subworkflows/local/utils_nfcore_bactmap_pipeline/main.nf:31:5`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
      monochrome_logs   // boolean: Do not use coloured log outputs
      ^^^^^^^^^^^^^^^
  ```

- Warning: `subworkflows/local/utils_nfcore_bactmap_pipeline/main.nf:34:5`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
      input             //  string: Path to input samplesheet
      ^^^^^
  ```

- Warning: `subworkflows/local/utils_nfcore_bactmap_pipeline/main.nf:38:19`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_versions = Channel.empty()
                    ^^^^^^^
  ```

- Warning: `subworkflows/local/utils_nfcore_bactmap_pipeline/main.nf:75:5`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      Channel
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

- Warning: `subworkflows/nf-core/fastq_align_bowtie2/main.nf:18:19`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_versions = Channel.empty()
                    ^^^^^^^
  ```

- Warning: `subworkflows/nf-core/utils_nfcore_pipeline/main.nf:101:98`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      return ch_versions.unique().map { version -> processVersionsFromYAML(version) }.unique().mix(Channel.of(workflowVersionToYAML()))
                                                                                                   ^^^^^^^
  ```

- Warning: `workflows/bactmap.nf:20:5`: Variable was declared but not used

  ```nextflow
      ch_input = file(params.input, checkIfExists: true)
      ^^^^^^^^
  ```
