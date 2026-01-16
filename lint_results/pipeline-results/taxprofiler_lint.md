# Nextflow lint results

- Generated: 2026-01-16T10:30:37.888729865Z
- Nextflow version: 25.12.0-edge
- Summary: 113 warnings

## :warning: Warnings

- Warning: `conf/modules.config:94:273`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
                  saveAs: { (params.perform_runmerging == false || (params.perform_runmerging && !meta.is_multirun)) && !params.perform_shortread_hostremoval && !params.perform_shortread_complexityfilter && params.perform_shortread_qc && params.save_analysis_ready_fastqs ? it : null },
                                                                                                                                                                                                                                                                                  ^^
  ```

- Warning: `conf/modules.config:127:273`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
                  saveAs: { (params.perform_runmerging == false || (params.perform_runmerging && !meta.is_multirun)) && !params.perform_shortread_hostremoval && !params.perform_shortread_complexityfilter && params.perform_shortread_qc && params.save_analysis_ready_fastqs ? it : null },
                                                                                                                                                                                                                                                                                  ^^
  ```

- Warning: `conf/modules.config:155:273`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
                  saveAs: { (params.perform_runmerging == false || (params.perform_runmerging && !meta.is_multirun)) && !params.perform_shortread_hostremoval && !params.perform_shortread_complexityfilter && params.perform_shortread_qc && params.save_analysis_ready_fastqs ? it : null },
                                                                                                                                                                                                                                                                                  ^^
  ```

- Warning: `conf/modules.config:185:308`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
                  saveAs: { (params.perform_runmerging == false || (params.perform_runmerging && !meta.is_multirun)) && !params.perform_shortread_hostremoval && !params.perform_shortread_complexityfilter && params.perform_shortread_qc && !params.shortread_qc_mergepairs && params.save_analysis_ready_fastqs ? it : null },
                                                                                                                                                                                                                                                                                                                     ^^
  ```

- Warning: `conf/modules.config:236:273`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
                  saveAs: { (params.perform_runmerging == false || (params.perform_runmerging && !meta.is_multirun)) && !params.perform_shortread_hostremoval && !params.perform_shortread_complexityfilter && params.perform_shortread_qc && params.save_analysis_ready_fastqs ? it : null },
                                                                                                                                                                                                                                                                                  ^^
  ```

- Warning: `conf/modules.config:260:304`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
                  saveAs: { (params.perform_runmerging == false || (params.perform_runmerging && !meta.is_multirun)) && !params.perform_longread_hostremoval && params.longread_qc_skipqualityfilter && !params.longread_qc_skipadaptertrim && params.perform_longread_qc && params.save_analysis_ready_fastqs ? it : null },
                                                                                                                                                                                                                                                                                                                 ^^
  ```

- Warning: `conf/modules.config:284:304`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
                  saveAs: { (params.perform_runmerging == false || (params.perform_runmerging && !meta.is_multirun)) && !params.perform_longread_hostremoval && params.longread_qc_skipqualityfilter && !params.longread_qc_skipadaptertrim && params.perform_longread_qc && params.save_analysis_ready_fastqs ? it : null },
                                                                                                                                                                                                                                                                                                                 ^^
  ```

- Warning: `conf/modules.config:313:266`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
                  saveAs: { (params.perform_runmerging == false || (params.perform_runmerging && !meta.is_multirun)) && !params.perform_longread_hostremoval && !params.longread_qc_skipqualityfilter && params.perform_longread_qc && params.save_analysis_ready_fastqs ? it : null },
                                                                                                                                                                                                                                                                           ^^
  ```

- Warning: `conf/modules.config:342:266`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
                  saveAs: { (params.perform_runmerging == false || (params.perform_runmerging && !meta.is_multirun)) && !params.perform_longread_hostremoval && !params.longread_qc_skipqualityfilter && params.perform_longread_qc && params.save_analysis_ready_fastqs ? it : null },
                                                                                                                                                                                                                                                                           ^^
  ```

- Warning: `conf/modules.config:371:238`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
                  saveAs: { (params.perform_runmerging == false || (params.perform_runmerging && !meta.is_multirun)) && !params.perform_shortread_hostremoval && params.shortread_complexityfilter_tool && params.save_analysis_ready_fastqs ? it : null },
                                                                                                                                                                                                                                               ^^
  ```

- Warning: `conf/modules.config:399:238`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
                  saveAs: { (params.perform_runmerging == false || (params.perform_runmerging && !meta.is_multirun)) && !params.perform_shortread_hostremoval && params.shortread_complexityfilter_tool && params.save_analysis_ready_fastqs ? it : null },
                                                                                                                                                                                                                                               ^^
  ```

- Warning: `conf/modules.config:442:195`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
                  saveAs: { (params.perform_runmerging == false || (params.perform_runmerging && !meta.is_multirun)) && params.perform_shortread_hostremoval && params.save_analysis_ready_fastqs ? it : null },
                                                                                                                                                                                                    ^^
  ```

- Warning: `conf/modules.config:503:194`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
                  saveAs: { (params.perform_runmerging == false || (params.perform_runmerging && !meta.is_multirun)) && params.perform_longread_hostremoval && params.save_analysis_ready_fastqs ? it : null },
                                                                                                                                                                                                   ^^
  ```

- Warning: `conf/modules.config:565:99`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
              saveAs: { !params.bracken_save_intermediatekraken2 && meta.tool == "bracken" ? null : it },
                                                                                                    ^^
  ```

- Warning: `modules/nf-core/bbmap/bbduk/main.nf:45:9`: Variable was declared but not used

  ```nextflow
      def args = task.ext.args ?: ''
          ^^^^
  ```

- Warning: `modules/nf-core/bracken/bracken/main.nf:42:9`: Variable was declared but not used

  ```nextflow
      def args = task.ext.args ?: ''
          ^^^^
  ```

- Warning: `modules/nf-core/bracken/combinebrackenoutputs/main.nf:39:9`: Variable was declared but not used

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

- Warning: `modules/nf-core/ganon/classify/main.nf:48:9`: Variable was declared but not used

  ```nextflow
      def args = task.ext.args ?: ''
          ^^^^
  ```

- Warning: `modules/nf-core/ganon/classify/main.nf:50:9`: Variable was declared but not used

  ```nextflow
      def input = meta.single_end ? "--single-reads ${fastqs}" : "--paired-reads ${fastqs}"
          ^^^^^
  ```

- Warning: `modules/nf-core/ganon/report/main.nf:41:9`: Variable was declared but not used

  ```nextflow
      def args = task.ext.args ?: ''
          ^^^^
  ```

- Warning: `modules/nf-core/ganon/table/main.nf:36:9`: Variable was declared but not used

  ```nextflow
      def args = task.ext.args ?: ''
          ^^^^
  ```

- Warning: `modules/nf-core/gunzip/main.nf:43:9`: Variable was declared but not used

  ```nextflow
      def args = task.ext.args ?: ''
          ^^^^
  ```

- Warning: `modules/nf-core/kaiju/kaiju/main.nf:43:9`: Variable was declared but not used

  ```nextflow
      def args = task.ext.args ?: ''
          ^^^^
  ```

- Warning: `modules/nf-core/kaiju/kaiju/main.nf:45:9`: Variable was declared but not used

  ```nextflow
      def input = meta.single_end ? "-i ${reads}" : "-i ${reads[0]} -j ${reads[1]}"
          ^^^^^
  ```

- Warning: `modules/nf-core/kaiju/kaiju2krona/main.nf:41:9`: Variable was declared but not used

  ```nextflow
      def args = task.ext.args ?: ''
          ^^^^
  ```

- Warning: `modules/nf-core/kaiju/kaiju2table/main.nf:42:9`: Variable was declared but not used

  ```nextflow
      def args = task.ext.args ?: ''
          ^^^^
  ```

- Warning: `modules/nf-core/kmcp/profile/main.nf:42:9`: Variable was declared but not used

  ```nextflow
      def args = task.ext.args ?: ''
          ^^^^
  ```

- Warning: `modules/nf-core/kmcp/search/main.nf:24:9`: Variable was declared but not used

  ```nextflow
      def input  = meta.single_end ? "${reads}": "-1 ${reads[0]} -2 ${reads[1]}"
          ^^^^^
  ```

- Warning: `modules/nf-core/kmcp/search/main.nf:40:9`: Variable was declared but not used

  ```nextflow
      def args = task.ext.args ?: ''
          ^^^^
  ```

- Warning: `modules/nf-core/kraken2/kraken2/main.nf:60:9`: Variable was declared but not used

  ```nextflow
      def args = task.ext.args ?: ''
          ^^^^
  ```

- Warning: `modules/nf-core/kraken2/kraken2/main.nf:62:9`: Variable was declared but not used

  ```nextflow
      def paired       = meta.single_end ? "" : "--paired"
          ^^^^^^
  ```

- Warning: `modules/nf-core/kraken2/kraken2/main.nf:65:9`: Variable was declared but not used

  ```nextflow
      def readclassification_option = save_reads_assignment ? "--output ${prefix}.kraken2.classifiedreads.txt" : "--output /dev/null"
          ^^^^^^^^^^^^^^^^^^^^^^^^^
  ```

- Warning: `modules/nf-core/kraken2/kraken2/main.nf:66:9`: Variable was declared but not used

  ```nextflow
      def compress_reads_command = save_output_fastqs ? "pigz -p $task.cpus *.fastq" : ""
          ^^^^^^^^^^^^^^^^^^^^^^
  ```

- Warning: `modules/nf-core/krakentools/combinekreports/main.nf:36:9`: Variable was declared but not used

  ```nextflow
      def args = task.ext.args ?: ''
          ^^^^
  ```

- Warning: `modules/nf-core/krakentools/kreport2krona/main.nf:38:9`: Variable was declared but not used

  ```nextflow
      def args = task.ext.args ?: ''
          ^^^^
  ```

- Warning: `modules/nf-core/malt/run/main.nf:42:9`: Variable was declared but not used

  ```nextflow
      def args = task.ext.args ?: ''
          ^^^^
  ```

- Warning: `modules/nf-core/megan/rma2info/main.nf:40:9`: Variable was declared but not used

  ```nextflow
      def args = task.ext.args ?: ''
          ^^^^
  ```

- Warning: `modules/nf-core/megan/rma2info/main.nf:42:9`: Variable was declared but not used

  ```nextflow
      def summary = megan_summary ? "-es ${prefix}.megan" : ""
          ^^^^^^^
  ```

- Warning: `modules/nf-core/metaphlan/mergemetaphlantables/main.nf:35:9`: Variable was declared but not used

  ```nextflow
      def args = task.ext.args ?: ''
          ^^^^
  ```

- Warning: `modules/nf-core/metaphlan/metaphlan/main.nf:58:9`: Variable was declared but not used

  ```nextflow
      def input_data = ("${input_type}".contains("fastq")) && !meta.single_end ? "${input[0]},${input[1]}" : "${input}"
          ^^^^^^^^^^
  ```

- Warning: `modules/nf-core/metaphlan/metaphlan/main.nf:59:9`: Variable was declared but not used

  ```nextflow
      def bowtie2_out = "${input_type}" == "--input_type bowtie2out" || "${input_type}" == "--input_type sam" ? '' : "--bowtie2out ${prefix}.bowtie2out.txt"
          ^^^^^^^^^^^
  ```

- Warning: `modules/nf-core/metaphlan/metaphlan/main.nf:60:9`: Variable was declared but not used

  ```nextflow
      def samfile_out = save_samfile ? "-s ${prefix}.sam" : ''
          ^^^^^^^^^^^
  ```

- Warning: `modules/nf-core/minimap2/align/main.nf:67:9`: Variable was declared but not used

  ```nextflow
      def target = reference ?: (bam_input ? error("BAM input requires reference") : reads)
          ^^^^^^
  ```

- Warning: `modules/nf-core/motus/merge/main.nf:47:9`: Variable was declared but not used

  ```nextflow
      def args = task.ext.args ?: ''
          ^^^^
  ```

- Warning: `modules/nf-core/motus/merge/main.nf:49:9`: Variable was declared but not used

  ```nextflow
      def cmd_input = input.size() > 1 ? "-i ${input.join(',')}" : input.isDirectory() ? "-d ${input}" : "-i ${input}"
          ^^^^^^^^^
  ```

- Warning: `modules/nf-core/motus/merge/main.nf:50:9`: Variable was declared but not used

  ```nextflow
      def suffix = task.ext.args?.contains("-B") ? "biom" : "txt"
          ^^^^^^
  ```

- Warning: `modules/nf-core/motus/profile/main.nf:58:9`: Variable was declared but not used

  ```nextflow
      def args = task.ext.args ?: ''
          ^^^^
  ```

- Warning: `modules/nf-core/motus/profile/main.nf:60:9`: Variable was declared but not used

  ```nextflow
      def inputs = reads[0].getExtension() == 'bam' ?
          ^^^^^^
  ```

- Warning: `modules/nf-core/motus/profile/main.nf:65:9`: Variable was declared but not used

  ```nextflow
      def refdb = db ? "-db ${db}" : ""
          ^^^^^
  ```

- Warning: `modules/nf-core/nanoq/main.nf:38:9`: Variable was declared but not used

  ```nextflow
      def args = task.ext.args ?: ''
          ^^^^
  ```

- Warning: `modules/nf-core/nonpareil/curve/main.nf:42:9`: Variable was declared but not used

  ```nextflow
      def args = task.ext.args ?: ''
          ^^^^
  ```

- Warning: `modules/nf-core/nonpareil/nonpareil/main.nf:46:9`: Variable was declared but not used

  ```nextflow
      def args = task.ext.args ?: ''
          ^^^^
  ```

- Warning: `modules/nf-core/nonpareil/nonpareilcurvesr/main.nf:44:9`: Variable was declared but not used

  ```nextflow
      def args = task.ext.args ?: ''
          ^^^^
  ```

- Warning: `modules/nf-core/nonpareil/set/main.nf:42:9`: Variable was declared but not used

  ```nextflow
      def args = task.ext.args ?: ''
          ^^^^
  ```

- Warning: `modules/nf-core/porechop/abi/main.nf:39:9`: Variable was declared but not used

  ```nextflow
      def args = task.ext.args ?: ''
          ^^^^
  ```

- Warning: `modules/nf-core/taxpasta/merge/main.nf:46:9`: Variable was declared but not used

  ```nextflow
      def args = task.ext.args ?: ''
          ^^^^
  ```

- Warning: `modules/nf-core/taxpasta/merge/main.nf:48:9`: Variable was declared but not used

  ```nextflow
      def taxonomy_option = taxonomy ? "--taxonomy ${taxonomy}" : ''
          ^^^^^^^^^^^^^^^
  ```

- Warning: `modules/nf-core/taxpasta/merge/main.nf:49:9`: Variable was declared but not used

  ```nextflow
      def samplesheet_input = samplesheet ? "-s ${samplesheet}" : ''
          ^^^^^^^^^^^^^^^^^
  ```

- Warning: `modules/nf-core/taxpasta/standardise/main.nf:42:9`: Variable was declared but not used

  ```nextflow
      def args = task.ext.args ?: ''
          ^^^^
  ```

- Warning: `modules/nf-core/taxpasta/standardise/main.nf:44:9`: Variable was declared but not used

  ```nextflow
      def taxonomy_option = taxonomy ? "--taxonomy ${taxonomy}" : ''
          ^^^^^^^^^^^^^^^
  ```

- Warning: `subworkflows/local/profiling.nf:237:21`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
                  if (it[0].is_fasta) {
                      ^^
  ```

- Warning: `subworkflows/local/profiling.nf:238:145`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
                      log.warn("[nf-core/taxprofiler] Centrifuge currently does not accept FASTA files as input. Skipping Centrifuge for sample ${it[0].id}.")
                                                                                                                                                  ^^
  ```

- Warning: `subworkflows/local/profiling.nf:240:18`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
                  !it[0].is_fasta
                   ^^
  ```

- Warning: `subworkflows/local/profiling.nf:325:21`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
                  if (it[0].is_fasta) {
                      ^^
  ```

- Warning: `subworkflows/local/profiling.nf:326:135`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
                      log.warn("[nf-core/taxprofiler] mOTUs currently does not accept FASTA files as input. Skipping mOTUs for sample ${it[0].id}.")
                                                                                                                                        ^^
  ```

- Warning: `subworkflows/local/profiling.nf:328:18`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
                  !it[0].is_fasta
                   ^^
  ```

- Warning: `subworkflows/local/shortread_adapterremoval.nf:19:17`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          single: it[0].single_end
                  ^^
  ```

- Warning: `subworkflows/local/shortread_adapterremoval.nf:20:18`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          paired: !it[0].single_end
                   ^^
  ```

- Warning: `subworkflows/local/shortread_fastp.nf:18:17`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          single: it[0]['single_end'] == true
                  ^^
  ```

- Warning: `subworkflows/local/shortread_fastp.nf:19:17`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          paired: it[0]['single_end'] == false
                  ^^
  ```

- Warning: `subworkflows/local/standardisation_profiles.nf:74:18`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          bracken: it[0]['tool'] == 'bracken'
                   ^^
  ```

- Warning: `subworkflows/local/standardisation_profiles.nf:75:21`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          centrifuge: it[0]['tool'] == 'centrifuge'
                      ^^
  ```

- Warning: `subworkflows/local/standardisation_profiles.nf:76:16`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          ganon: it[0]['tool'] == 'ganon'
                 ^^
  ```

- Warning: `subworkflows/local/standardisation_profiles.nf:77:15`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          kmcp: it[0]['tool'] == 'kmcp'
                ^^
  ```

- Warning: `subworkflows/local/standardisation_profiles.nf:78:18`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          kraken2: it[0]['tool'] == 'kraken2' || it[0]['tool'] == 'kraken2-bracken'
                   ^^
  ```

- Warning: `subworkflows/local/standardisation_profiles.nf:78:48`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          kraken2: it[0]['tool'] == 'kraken2' || it[0]['tool'] == 'kraken2-bracken'
                                                 ^^
  ```

- Warning: `subworkflows/local/standardisation_profiles.nf:79:20`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          metaphlan: it[0]['tool'] == 'metaphlan'
                     ^^
  ```

- Warning: `subworkflows/local/standardisation_profiles.nf:80:16`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          motus: it[0]['tool'] == 'motus'
                 ^^
  ```

- Warning: `subworkflows/local/standardisation_profiles.nf:85:16`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          kaiju: it[0]['tool'] == 'kaiju'
                 ^^
  ```

- Warning: `subworkflows/local/standardisation_profiles.nf:90:16`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          motus: it[0]['tool'] == 'motus'
                 ^^
  ```

- Warning: `subworkflows/local/standardisation_profiles.nf:91:16`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          kaiju: it[0]['tool'] == 'kaiju'
                 ^^
  ```

- Warning: `subworkflows/local/standardisation_profiles.nf:112:19`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          [sort: { -it.size() }],
                    ^^
  ```

- Warning: `subworkflows/local/standardisation_profiles.nf:141:19`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          [sort: { -it.size() }],
                    ^^
  ```

- Warning: `subworkflows/local/utils_nfcore_taxprofiler_pipeline/main.nf:31:5`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
      monochrome_logs // boolean: Do not use coloured log outputs
      ^^^^^^^^^^^^^^^
  ```

- Warning: `subworkflows/local/utils_nfcore_taxprofiler_pipeline/main.nf:128:22`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          .map { meta, run_accession, instrument_platform, fastq_1, fastq_2, fasta -> [ meta.id, meta.single_end ] }  // Adjust field names
                       ^^^^^^^^^^^^^
  ```

- Warning: `subworkflows/local/utils_nfcore_taxprofiler_pipeline/main.nf:128:37`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          .map { meta, run_accession, instrument_platform, fastq_1, fastq_2, fasta -> [ meta.id, meta.single_end ] }  // Adjust field names
                                      ^^^^^^^^^^^^^^^^^^^
  ```

- Warning: `subworkflows/local/utils_nfcore_taxprofiler_pipeline/main.nf:128:58`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          .map { meta, run_accession, instrument_platform, fastq_1, fastq_2, fasta -> [ meta.id, meta.single_end ] }  // Adjust field names
                                                           ^^^^^^^
  ```

- Warning: `subworkflows/local/utils_nfcore_taxprofiler_pipeline/main.nf:128:67`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          .map { meta, run_accession, instrument_platform, fastq_1, fastq_2, fasta -> [ meta.id, meta.single_end ] }  // Adjust field names
                                                                    ^^^^^^^
  ```

- Warning: `subworkflows/local/utils_nfcore_taxprofiler_pipeline/main.nf:128:76`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          .map { meta, run_accession, instrument_platform, fastq_1, fastq_2, fasta -> [ meta.id, meta.single_end ] }  // Adjust field names
                                                                             ^^^^^
  ```

- Warning: `subworkflows/local/utils_nfcore_taxprofiler_pipeline/main.nf:130:41`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          .map { validateInputSamplesheet(it) }
                                          ^^
  ```

- Warning: `subworkflows/local/visualization_krona.nf:28:21`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          centrifuge: it[0]['tool'] == 'centrifuge'
                      ^^
  ```

- Warning: `subworkflows/local/visualization_krona.nf:29:18`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          kraken2: it[0]['tool'] == 'kraken2' || it[0]['tool'] == 'kraken2-bracken'
                   ^^
  ```

- Warning: `subworkflows/local/visualization_krona.nf:29:48`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          kraken2: it[0]['tool'] == 'kraken2' || it[0]['tool'] == 'kraken2-bracken'
                                                 ^^
  ```

- Warning: `subworkflows/local/visualization_krona.nf:33:16`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          kaiju: it[0]['tool'] == 'kaiju'
                 ^^
  ```

- Warning: `subworkflows/local/visualization_krona.nf:34:15`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          malt: it[0]['tool'] == 'malt'
                ^^
  ```

- Warning: `subworkflows/local/visualization_krona.nf:79:22`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          .map { [[id: it[0]['db_name'], tool: it[0]['tool']], it[1]] }
                       ^^
  ```

- Warning: `subworkflows/local/visualization_krona.nf:79:46`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          .map { [[id: it[0]['db_name'], tool: it[0]['tool']], it[1]] }
                                               ^^
  ```

- Warning: `subworkflows/local/visualization_krona.nf:79:62`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          .map { [[id: it[0]['db_name'], tool: it[0]['tool']], it[1]] }
                                                               ^^
  ```

- Warning: `subworkflows/local/visualization_krona.nf:93:26`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
              .map { [[id: it[0]['db_name'], tool: it[0]['tool']], it[1]] }
                           ^^
  ```

- Warning: `subworkflows/local/visualization_krona.nf:93:50`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
              .map { [[id: it[0]['db_name'], tool: it[0]['tool']], it[1]] }
                                                   ^^
  ```

- Warning: `subworkflows/local/visualization_krona.nf:93:66`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
              .map { [[id: it[0]['db_name'], tool: it[0]['tool']], it[1]] }
                                                                   ^^
  ```

- Warning: `workflows/taxprofiler.nf:68:104`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          ch_shortread_reference_index = channel.fromPath(params.shortread_hostremoval_index).map { [[], it] }
                                                                                                         ^^
  ```

- Warning: `workflows/taxprofiler.nf:357:78`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
              ch_multiqc_files = ch_multiqc_files.mix(FASTQC.out.zip.collect { it[1] }.ifEmpty([]))
                                                                               ^^
  ```

- Warning: `workflows/taxprofiler.nf:362:91`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          ch_multiqc_files = ch_multiqc_files.mix(SHORTREAD_PREPROCESSING.out.mqc.collect { it[1] }.ifEmpty([]))
                                                                                            ^^
  ```

- Warning: `workflows/taxprofiler.nf:366:90`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          ch_multiqc_files = ch_multiqc_files.mix(LONGREAD_PREPROCESSING.out.mqc.collect { it[1] }.ifEmpty([]))
                                                                                           ^^
  ```

- Warning: `workflows/taxprofiler.nf:370:77`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          ch_multiqc_files = ch_multiqc_files.mix(NONPAREIL.out.mqc.collect { it[1] }.ifEmpty([]))
                                                                              ^^
  ```

- Warning: `workflows/taxprofiler.nf:374:97`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          ch_multiqc_files = ch_multiqc_files.mix(SHORTREAD_COMPLEXITYFILTERING.out.mqc.collect { it[1] }.ifEmpty([]))
                                                                                                  ^^
  ```

- Warning: `workflows/taxprofiler.nf:378:89`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          ch_multiqc_files = ch_multiqc_files.mix(SHORTREAD_HOSTREMOVAL.out.mqc.collect { it[1] }.ifEmpty([]))
                                                                                          ^^
  ```

- Warning: `workflows/taxprofiler.nf:382:88`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          ch_multiqc_files = ch_multiqc_files.mix(LONGREAD_HOSTREMOVAL.out.mqc.collect { it[1] }.ifEmpty([]))
                                                                                         ^^
  ```

- Warning: `workflows/taxprofiler.nf:385:73`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
      ch_multiqc_files = ch_multiqc_files.mix(PROFILING.out.mqc.collect { it[1] }.ifEmpty([]))
                                                                          ^^
  ```

- Warning: `workflows/taxprofiler.nf:388:92`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          ch_multiqc_files = ch_multiqc_files.mix(STANDARDISATION_PROFILES.out.mqc.collect { it[1] }.ifEmpty([]))
                                                                                             ^^
  ```
