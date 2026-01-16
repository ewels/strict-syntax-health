# Nextflow lint results

- Generated: 2026-01-16T10:17:27.383278468Z
- Nextflow version: 25.12.0-edge
- Summary: 27 errors, 131 warnings

## :x: Errors

- Error: `conf/modules.config:279:1`: If statements cannot be mixed with config statements

  ```nextflow
  if (!params.skip_fastqc) {
  ^
  ```

- Error: `conf/modules.config:299:1`: If statements cannot be mixed with config statements

  ```nextflow
  if (!params.skip_fastp) {
  ^
  ```

- Error: `conf/modules.config:344:1`: If statements cannot be mixed with config statements

  ```nextflow
  if (!params.skip_kmerfinder) {
  ^
  ```

- Error: `conf/modules.config:368:1`: If statements cannot be mixed with config statements

  ```nextflow
  if (params.annotation_tool == 'bakta') {
  ^
  ```

- Error: `modules/nf-core/bakta/bakta/main.nf:36:9`: `prodigal_tf` is already declared

  ```nextflow
      def prodigal_tf = prodigal_tf ? "--prodigal-tf ${prodigal_tf[0]}" : ""
          ^^^^^^^^^^^
  ```

- Error: `modules/nf-core/prokka/main.nf:37:9`: `prodigal_tf` is already declared

  ```nextflow
      def prodigal_tf = prodigal_tf ? "--prodigaltf ${prodigal_tf[0]}" : ""
          ^^^^^^^^^^^
  ```

- Error: `nextflow.config:358:30`: `manifest` is not defined

  ```nextflow
  \033[0;35m  nf-core/bacass ${manifest.version}\033[0m
                               ^^^^^^^^
  ```

- Error: `nextflow.config:361:26`: `manifest` is not defined

  ```nextflow
          afterText = """${manifest.doi ? "\n* The pipeline\n" : ""}${manifest.doi.tokenize(",").collect { "    https://doi.org/${it.trim().replace('https://doi.org/','')}"}.join("\n")}${manifest.doi ? "\n" : ""}
                           ^^^^^^^^
  ```

- Error: `nextflow.config:361:69`: `manifest` is not defined

  ```nextflow
          afterText = """${manifest.doi ? "\n* The pipeline\n" : ""}${manifest.doi.tokenize(",").collect { "    https://doi.org/${it.trim().replace('https://doi.org/','')}"}.join("\n")}${manifest.doi ? "\n" : ""}
                                                                      ^^^^^^^^
  ```

- Error: `nextflow.config:361:186`: `manifest` is not defined

  ```nextflow
          afterText = """${manifest.doi ? "\n* The pipeline\n" : ""}${manifest.doi.tokenize(",").collect { "    https://doi.org/${it.trim().replace('https://doi.org/','')}"}.join("\n")}${manifest.doi ? "\n" : ""}
                                                                                                                                                                                           ^^^^^^^^
  ```

- Error: `nextflow.config:370:22`: `validation` is not defined

  ```nextflow
          beforeText = validation.help.beforeText
                       ^^^^^^^^^^
  ```

- Error: `nextflow.config:371:21`: `validation` is not defined

  ```nextflow
          afterText = validation.help.afterText
                      ^^^^^^^^^^
  ```

- Error: `subworkflows/local/kmerfinder_summary_download/main.nf:52:17`: Variables in a closure should be declared with `def`

  ```nextflow
                  species_hits = report_json.splitJson(path:"kmerfinder.results.species_hits").value
                  ^^^^^^^^^^^^
  ```

- Error: `workflows/bacass.nf:65:1`: Statements cannot be mixed with script declarations -- move statements into a process, workflow, or function

  ```nextflow
  def checkPathParamList = [ params.input, params.multiqc_config, params.kraken2db, params.dfast_config, params.reference_fasta, params.reference_gff ]
  ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  ```

- Error: `workflows/bacass.nf:66:1`: `for` loops are no longer supported

  ```nextflow
  for (param in checkPathParamList) { if (param) { file(param, checkIfExists: true) } }
  ^^^
  ```

- Error: `workflows/bacass.nf:66:1`: Statements cannot be mixed with script declarations -- move statements into a process, workflow, or function

  ```nextflow
  for (param in checkPathParamList) { if (param) { file(param, checkIfExists: true) } }
  ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  ```

- Error: `workflows/bacass.nf:66:6`: `param` is not defined

  ```nextflow
  for (param in checkPathParamList) { if (param) { file(param, checkIfExists: true) } }
       ^^^^^
  ```

- Error: `workflows/bacass.nf:66:40`: `param` is not defined

  ```nextflow
  for (param in checkPathParamList) { if (param) { file(param, checkIfExists: true) } }
                                         ^^^^^^^
  ```

- Error: `workflows/bacass.nf:66:55`: `param` is not defined

  ```nextflow
  for (param in checkPathParamList) { if (param) { file(param, checkIfExists: true) } }
                                                        ^^^^^
  ```

- Error: `workflows/bacass.nf:68:1`: Statements cannot be mixed with script declarations -- move statements into a process, workflow, or function

  ```nextflow
  if (params.reference_fasta) {
  ^
  ```

- Error: `workflows/bacass.nf:71:1`: Statements cannot be mixed with script declarations -- move statements into a process, workflow, or function

  ```nextflow
  if (params.reference_gff) {
  ^
  ```

- Error: `workflows/bacass.nf:456:21`: Variables in a closure should be declared with `def`

  ```nextflow
                      info = [:]
                      ^^^^
  ```

- Error: `workflows/bacass.nf:462:49`: `info` is already declared

  ```nextflow
              KRAKEN2_DB_PREPARATION.out.db.map { info, db -> db }.dump(tag: 'kraken2_db_preparation'),
                                                  ^^^^
  ```

- Error: `workflows/bacass.nf:512:44`: `reference_fasta` is not defined

  ```nextflow
              params.reference_fasta ? [[:], reference_fasta] : [[:],[]],
                                             ^^^^^^^^^^^^^^^
  ```

- Error: `workflows/bacass.nf:513:42`: `reference_gff` is not defined

  ```nextflow
              params.reference_gff ? [[:], reference_gff] : [[:],[]]
                                           ^^^^^^^^^^^^^
  ```

- Error: `workflows/bacass.nf:620:17`: `reference_fasta` is not defined

  ```nextflow
                  reference_fasta,
                  ^^^^^^^^^^^^^^^
  ```

- Error: `workflows/bacass.nf:621:17`: `reference_gff` is not defined

  ```nextflow
                  reference_gff,
                  ^^^^^^^^^^^^^
  ```

## :warning: Warnings

- Warning: `modules/local/nanopolish/main.nf:22:9`: Variable was declared but not used

  ```nextflow
      def prefix  = task.ext.prefix ?: "${meta.id}"
          ^^^^^^
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

- Warning: `modules/nf-core/quast/main.nf:52:9`: Variable was declared but not used

  ```nextflow
      def args      = task.ext.args   ?: ''
          ^^^^
  ```

- Warning: `modules/nf-core/quast/main.nf:54:9`: Variable was declared but not used

  ```nextflow
      def features  = gff             ? "--features $gff" : ''
          ^^^^^^^^
  ```

- Warning: `modules/nf-core/quast/main.nf:55:9`: Variable was declared but not used

  ```nextflow
      def reference = fasta           ? "-r $fasta" : ''
          ^^^^^^^^^
  ```

- Warning: `modules/nf-core/toulligqc/main.nf:46:9`: Variable was declared but not used

  ```nextflow
      def args = task.ext.args ?: ''
          ^^^^
  ```

- Warning: `nextflow.config:361:129`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          afterText = """${manifest.doi ? "\n* The pipeline\n" : ""}${manifest.doi.tokenize(",").collect { "    https://doi.org/${it.trim().replace('https://doi.org/','')}"}.join("\n")}${manifest.doi ? "\n" : ""}
                                                                                                                                  ^^
  ```

- Warning: `subworkflows/local/bakta_dbdownload_run/main.nf:17:19`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_versions = Channel.empty()
                    ^^^^^^^
  ```

- Warning: `subworkflows/local/bakta_dbdownload_run/main.nf:24:31`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
              ch_baktadb_tar  = Channel.from(ch_path_baktadb).map{ db -> [ [id: 'baktadb'], db ]}
                                ^^^^^^^
  ```

- Warning: `subworkflows/local/bakta_dbdownload_run/main.nf:28:52`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
              ch_path_baktadb = UNTAR.out.untar.map{ meta, db -> db }
                                                     ^^^^
  ```

- Warning: `subworkflows/local/kmerfinder_summary_download/main.nf:15:19`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_versions = Channel.empty()
                    ^^^^^^^
  ```

- Warning: `subworkflows/local/kmerfinder_summary_download/main.nf:22:54`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          ch_kmerfinderdb_untar = UNTAR.out.untar.map{ meta, file -> file }
                                                       ^^^^
  ```

- Warning: `subworkflows/local/kmerfinder_summary_download/main.nf:26:33`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
          ch_kmerfinderdb_untar = Channel.fromPath(ch_kmerfinderdb)
                                  ^^^^^^^
  ```

- Warning: `subworkflows/local/kmerfinder_summary_download/main.nf:41:35`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          ch_kmerfinder_report.map{ meta, report -> report }.collect()
                                    ^^^^
  ```

- Warning: `subworkflows/local/kmerfinder_summary_download/main.nf:63:27`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
              .map{ specie, meta, report_txt, fasta-> tuple(specie, report_txt) }
                            ^^^^
  ```

- Warning: `subworkflows/local/kmerfinder_summary_download/main.nf:63:45`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
              .map{ specie, meta, report_txt, fasta-> tuple(specie, report_txt) }
                                              ^^^^^
  ```

- Warning: `subworkflows/local/kmerfinder_summary_download/main.nf:64:30`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
              .filter{ specie, report_txt -> specie != "Unknown Species" }
                               ^^^^^^^^^^
  ```

- Warning: `subworkflows/local/kmerfinder_summary_download/main.nf:74:13`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
              specie, meta, report_txt, fasta, fna, gff, winner_id ->
              ^^^^^^
  ```

- Warning: `subworkflows/local/kmerfinder_summary_download/main.nf:74:27`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
              specie, meta, report_txt, fasta, fna, gff, winner_id ->
                            ^^^^^^^^^^
  ```

- Warning: `subworkflows/local/qc_nanoplot_toulliqc/main.nf:21:24`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      nanoplot_png     = Channel.empty()
                         ^^^^^^^
  ```

- Warning: `subworkflows/local/qc_nanoplot_toulliqc/main.nf:22:24`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      nanoplot_html    = Channel.empty()
                         ^^^^^^^
  ```

- Warning: `subworkflows/local/qc_nanoplot_toulliqc/main.nf:23:24`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      nanoplot_txt     = Channel.empty()
                         ^^^^^^^
  ```

- Warning: `subworkflows/local/qc_nanoplot_toulliqc/main.nf:24:24`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      nanoplot_log     = Channel.empty()
                         ^^^^^^^
  ```

- Warning: `subworkflows/local/qc_nanoplot_toulliqc/main.nf:25:24`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      nanoplot_version = Channel.empty()
                         ^^^^^^^
  ```

- Warning: `subworkflows/local/qc_nanoplot_toulliqc/main.nf:38:31`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      toulligqc_report_data   = Channel.empty()
                                ^^^^^^^
  ```

- Warning: `subworkflows/local/qc_nanoplot_toulliqc/main.nf:39:31`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      toulligqc_report_html   = Channel.empty()
                                ^^^^^^^
  ```

- Warning: `subworkflows/local/qc_nanoplot_toulliqc/main.nf:40:31`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      toulligqc_plots_html    = Channel.empty()
                                ^^^^^^^
  ```

- Warning: `subworkflows/local/qc_nanoplot_toulliqc/main.nf:41:31`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      toulligqc_plotly_js     = Channel.empty()
                                ^^^^^^^
  ```

- Warning: `subworkflows/local/qc_nanoplot_toulliqc/main.nf:42:31`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      toulligqc_version       = Channel.empty()
                                ^^^^^^^
  ```

- Warning: `subworkflows/local/utils_nfcore_bacass_pipeline/main.nf:31:5`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
      monochrome_logs   // boolean: Do not use coloured log outputs
      ^^^^^^^^^^^^^^^
  ```

- Warning: `subworkflows/local/utils_nfcore_bacass_pipeline/main.nf:34:5`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
      input             //  string: Path to input samplesheet
      ^^^^^
  ```

- Warning: `subworkflows/local/utils_nfcore_bacass_pipeline/main.nf:38:19`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_versions = Channel.empty()
                    ^^^^^^^
  ```

- Warning: `subworkflows/local/utils_nfcore_bacass_pipeline/main.nf:75:5`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      Channel
      ^^^^^^^
  ```

- Warning: `subworkflows/nf-core/fastq_trim_fastp_fastqc/main.nf:35:19`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_versions = Channel.empty()
                    ^^^^^^^
  ```

- Warning: `subworkflows/nf-core/fastq_trim_fastp_fastqc/main.nf:37:26`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_fastqc_raw_html = Channel.empty()
                           ^^^^^^^
  ```

- Warning: `subworkflows/nf-core/fastq_trim_fastp_fastqc/main.nf:38:26`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_fastqc_raw_zip  = Channel.empty()
                           ^^^^^^^
  ```

- Warning: `subworkflows/nf-core/fastq_trim_fastp_fastqc/main.nf:49:28`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_trim_json         = Channel.empty()
                             ^^^^^^^
  ```

- Warning: `subworkflows/nf-core/fastq_trim_fastp_fastqc/main.nf:50:28`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_trim_html         = Channel.empty()
                             ^^^^^^^
  ```

- Warning: `subworkflows/nf-core/fastq_trim_fastp_fastqc/main.nf:51:28`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_trim_log          = Channel.empty()
                             ^^^^^^^
  ```

- Warning: `subworkflows/nf-core/fastq_trim_fastp_fastqc/main.nf:52:28`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_trim_reads_fail   = Channel.empty()
                             ^^^^^^^
  ```

- Warning: `subworkflows/nf-core/fastq_trim_fastp_fastqc/main.nf:53:28`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_trim_reads_merged = Channel.empty()
                             ^^^^^^^
  ```

- Warning: `subworkflows/nf-core/fastq_trim_fastp_fastqc/main.nf:54:28`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_fastqc_trim_html  = Channel.empty()
                             ^^^^^^^
  ```

- Warning: `subworkflows/nf-core/fastq_trim_fastp_fastqc/main.nf:55:28`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_fastqc_trim_zip   = Channel.empty()
                             ^^^^^^^
  ```

- Warning: `subworkflows/nf-core/utils_nfcore_pipeline/main.nf:101:98`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      return ch_versions.unique().map { version -> processVersionsFromYAML(version) }.unique().mix(Channel.of(workflowVersionToYAML()))
                                                                                                   ^^^^^^^
  ```

- Warning: `workflows/bacass.nf:69:5`: Variable was declared but not used

  ```nextflow
      reference_fasta = file(params.reference_fasta, type: 'file')
      ^^^^^^^^^^^^^^^
  ```

- Warning: `workflows/bacass.nf:72:5`: Variable was declared but not used

  ```nextflow
      reference_gff = file(params.reference_gff, type: 'file')
      ^^^^^^^^^^^^^
  ```

- Warning: `workflows/bacass.nf:86:19`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_versions = Channel.empty()
                    ^^^^^^^
  ```

- Warning: `workflows/bacass.nf:87:5`: Variable was declared but not used

  ```nextflow
      ch_multiqc_files = Channel.empty()
      ^^^^^^^^^^^^^^^^
  ```

- Warning: `workflows/bacass.nf:87:24`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_multiqc_files = Channel.empty()
                         ^^^^^^^
  ```

- Warning: `workflows/bacass.nf:97:44`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_proteins = params.prokka_proteins ? Channel.fromPath(params.prokka_proteins, checkIfExists: true)  : []
                                             ^^^^^^^
  ```

- Warning: `workflows/bacass.nf:106:18`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          .filter{ it != null }
                   ^^
  ```

- Warning: `workflows/bacass.nf:110:18`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          .filter{ it != null }
                   ^^
  ```

- Warning: `workflows/bacass.nf:114:18`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          .filter{ it != null }
                   ^^
  ```

- Warning: `workflows/bacass.nf:138:32`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
          ch_shortreads_concat = Channel.empty()
                                 ^^^^^^^
  ```

- Warning: `workflows/bacass.nf:151:17`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
                  meta, long_fastqs ->
                  ^^^^
  ```

- Warning: `workflows/bacass.nf:166:31`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
          ch_longreads_concat = Channel.empty()
                                ^^^^^^^
  ```

- Warning: `workflows/bacass.nf:172:29`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_fastqc_raw_multiqc = Channel.empty()
                              ^^^^^^^
  ```

- Warning: `workflows/bacass.nf:173:30`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_fastqc_trim_multiqc = Channel.empty()
                               ^^^^^^^
  ```

- Warning: `workflows/bacass.nf:174:29`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_fastp_json_multiqc = Channel.empty()
                              ^^^^^^^
  ```

- Warning: `workflows/bacass.nf:208:25`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_pycoqc_multiqc = Channel.empty()
                          ^^^^^^^
  ```

- Warning: `workflows/bacass.nf:220:31`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_porechop_log_multiqc = Channel.empty()
                                ^^^^^^^
  ```

- Warning: `workflows/bacass.nf:233:31`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_filtlong_log_multiqc = Channel.empty()
                                ^^^^^^^
  ```

- Warning: `workflows/bacass.nf:260:43`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
              .cross(filtered_long_reads) { it[0].id }
                                            ^^
  ```

- Warning: `workflows/bacass.nf:271:35`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
          ch_for_kraken2_long     = Channel.empty()
                                    ^^^^^^^
  ```

- Warning: `workflows/bacass.nf:278:35`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
          ch_for_kraken2_short    = Channel.empty()
                                    ^^^^^^^
  ```

- Warning: `workflows/bacass.nf:290:19`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_assembly = Channel.empty()
                    ^^^^^^^
  ```

- Warning: `workflows/bacass.nf:309:41`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
              ch_for_assembly.map { meta, reads, lr -> tuple( meta, lr ) },
                                          ^^^^^
  ```

- Warning: `workflows/bacass.nf:311:41`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
              ch_for_assembly.map { meta, reads, lr -> meta.gsize }
                                          ^^^^^
  ```

- Warning: `workflows/bacass.nf:311:48`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
              ch_for_assembly.map { meta, reads, lr -> meta.gsize }
                                                 ^^
  ```

- Warning: `workflows/bacass.nf:322:39`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
              ch_for_assembly.map{ meta,sr,lr -> tuple(meta,lr) },
                                        ^^
  ```

- Warning: `workflows/bacass.nf:332:26`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
              .map { meta, sr, lr, paf-> tuple(meta, lr, paf) }
                           ^^
  ```

- Warning: `workflows/bacass.nf:341:39`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
              ch_for_assembly.map{ meta,sr,lr -> tuple(meta,lr) },
                                        ^^
  ```

- Warning: `workflows/bacass.nf:352:26`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
              .map { meta, sr, lr, assembly, paf -> tuple(meta, lr, assembly, paf) }
                           ^^
  ```

- Warning: `workflows/bacass.nf:382:26`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
              .map { meta, sr, lr, fasta -> tuple(meta, lr, fasta) }
                           ^^
  ```

- Warning: `workflows/bacass.nf:402:52`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
                      ch_polish_long.map { meta, lr, fasta -> tuple(meta, lr) },
                                                     ^^^^^
  ```

- Warning: `workflows/bacass.nf:403:48`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
                      ch_polish_long.map { meta, lr, fasta -> tuple(meta, fasta) },
                                                 ^^
  ```

- Warning: `workflows/bacass.nf:437:31`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_kraken_short_multiqc = Channel.empty()
                                ^^^^^^^
  ```

- Warning: `workflows/bacass.nf:438:31`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_kraken_long_multiqc  = Channel.empty()
                                ^^^^^^^
  ```

- Warning: `workflows/bacass.nf:446:49`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
              KRAKEN2_DB_PREPARATION.out.db.map { info, db -> db }.dump(tag: 'kraken2_db_preparation'),
                                                  ^^^^
  ```

- Warning: `workflows/bacass.nf:462:49`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
              KRAKEN2_DB_PREPARATION.out.db.map { info, db -> db }.dump(tag: 'kraken2_db_preparation'),
                                                  ^^^^
  ```

- Warning: `workflows/bacass.nf:475:29`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_kmerfinder_multiqc = Channel.empty()
                              ^^^^^^^
  ```

- Warning: `workflows/bacass.nf:495:26`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
                  refmeta, meta, consensus, ref_fna, ref_gff ->
                           ^^^^
  ```

- Warning: `workflows/bacass.nf:505:18`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          .collect{it[1]}
                   ^^
  ```

- Warning: `workflows/bacass.nf:525:59`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
              ch_to_quast_byrefseq.map{ refmeta, consensus, ref_fasta, ref_gff -> tuple( refmeta, consensus)},
                                                            ^^^^^^^^^
  ```

- Warning: `workflows/bacass.nf:525:70`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
              ch_to_quast_byrefseq.map{ refmeta, consensus, ref_fasta, ref_gff -> tuple( refmeta, consensus)},
                                                                       ^^^^^^^
  ```

- Warning: `workflows/bacass.nf:526:48`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
              ch_to_quast_byrefseq.map{ refmeta, consensus, ref_fasta, ref_gff -> tuple( refmeta, ref_fasta)},
                                                 ^^^^^^^^^
  ```

- Warning: `workflows/bacass.nf:526:70`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
              ch_to_quast_byrefseq.map{ refmeta, consensus, ref_fasta, ref_gff -> tuple( refmeta, ref_fasta)},
                                                                       ^^^^^^^
  ```

- Warning: `workflows/bacass.nf:527:48`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
              ch_to_quast_byrefseq.map{ refmeta, consensus, ref_fasta, ref_gff -> tuple( refmeta, ref_gff)}
                                                 ^^^^^^^^^
  ```

- Warning: `workflows/bacass.nf:527:59`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
              ch_to_quast_byrefseq.map{ refmeta, consensus, ref_fasta, ref_gff -> tuple( refmeta, ref_gff)}
                                                            ^^^^^^^^^
  ```

- Warning: `workflows/bacass.nf:536:18`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          .branch{ meta, fasta ->
                   ^^^^
  ```

- Warning: `workflows/bacass.nf:545:24`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_busco_multiqc = Channel.empty()
                         ^^^^^^^
  ```

- Warning: `workflows/bacass.nf:562:29`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_prokka_txt_multiqc = Channel.empty()
                              ^^^^^^^
  ```

- Warning: `workflows/bacass.nf:570:34`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
              ch_to_prokka.filter{ meta, fasta -> !fasta.isEmpty() },
                                   ^^^^
  ```

- Warning: `workflows/bacass.nf:574:55`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          ch_prokka_txt_multiqc   = PROKKA.out.txt.map{ meta, prokka_txt -> [ prokka_txt ]}
                                                        ^^^^
  ```

- Warning: `workflows/bacass.nf:581:28`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_bakta_txt_multiqc = Channel.empty()
                             ^^^^^^^
  ```

- Warning: `workflows/bacass.nf:589:33`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
              ch_to_bakta.filter{ meta, fasta -> !fasta.isEmpty() },
                                  ^^^^
  ```

- Warning: `workflows/bacass.nf:593:83`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          ch_bakta_txt_multiqc    = BAKTA_DBDOWNLOAD_RUN.out.bakta_txt_multiqc.map{ meta, bakta_txt -> [ bakta_txt ]}
                                                                                    ^^^^
  ```

- Warning: `workflows/bacass.nf:603:13`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
              Channel.value(params.dfast_config ? file(params.dfast_config) : "")
              ^^^^^^^
  ```

- Warning: `workflows/bacass.nf:629:63`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
                  ch_to_quast_byrefseq.map{ refmeta, consensus, ref_fasta, ref_gff -> tuple( refmeta, consensus)},
                                                                ^^^^^^^^^
  ```

- Warning: `workflows/bacass.nf:629:74`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
                  ch_to_quast_byrefseq.map{ refmeta, consensus, ref_fasta, ref_gff -> tuple( refmeta, consensus)},
                                                                           ^^^^^^^
  ```

- Warning: `workflows/bacass.nf:630:52`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
                  ch_to_quast_byrefseq.map{ refmeta, consensus, ref_fasta, ref_gff -> tuple( refmeta, ref_fasta)},
                                                     ^^^^^^^^^
  ```

- Warning: `workflows/bacass.nf:630:74`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
                  ch_to_quast_byrefseq.map{ refmeta, consensus, ref_fasta, ref_gff -> tuple( refmeta, ref_fasta)},
                                                                           ^^^^^^^
  ```

- Warning: `workflows/bacass.nf:631:52`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
                  ch_to_quast_byrefseq.map{ refmeta, consensus, ref_fasta, ref_gff -> tuple( refmeta, ref_gff)},
                                                     ^^^^^^^^^
  ```

- Warning: `workflows/bacass.nf:631:63`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
                  ch_to_quast_byrefseq.map{ refmeta, consensus, ref_fasta, ref_gff -> tuple( refmeta, ref_gff)},
                                                                ^^^^^^^^^
  ```

- Warning: `workflows/bacass.nf:653:95`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_multiqc_config                     = !params.skip_kmerfinder && params.assembly_type ? Channel.fromPath("$projectDir/assets/multiqc_config_${params.assembly_type}.yml", checkIfExists: true) : Channel.fromPath("$projectDir/assets/multiqc_config.yml", checkIfExists: true)
                                                                                                ^^^^^^^
  ```

- Warning: `workflows/bacass.nf:653:200`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_multiqc_config                     = !params.skip_kmerfinder && params.assembly_type ? Channel.fromPath("$projectDir/assets/multiqc_config_${params.assembly_type}.yml", checkIfExists: true) : Channel.fromPath("$projectDir/assets/multiqc_config.yml", checkIfExists: true)
                                                                                                                                                                                                         ^^^^^^^
  ```

- Warning: `workflows/bacass.nf:654:69`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_multiqc_custom_config              = params.multiqc_config ? Channel.fromPath(params.multiqc_config, checkIfExists: true) : Channel.empty()
                                                                      ^^^^^^^
  ```

- Warning: `workflows/bacass.nf:654:132`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_multiqc_custom_config              = params.multiqc_config ? Channel.fromPath(params.multiqc_config, checkIfExists: true) : Channel.empty()
                                                                                                                                     ^^^^^^^
  ```

- Warning: `workflows/bacass.nf:655:67`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_multiqc_logo                       = params.multiqc_logo ? Channel.fromPath(params.multiqc_logo, checkIfExists: true) : Channel.empty()
                                                                    ^^^^^^^
  ```

- Warning: `workflows/bacass.nf:655:128`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_multiqc_logo                       = params.multiqc_logo ? Channel.fromPath(params.multiqc_logo, checkIfExists: true) : Channel.empty()
                                                                                                                                 ^^^^^^^
  ```

- Warning: `workflows/bacass.nf:657:45`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_workflow_summary                   = Channel.value(paramsSummaryMultiqc(summary_params))
                                              ^^^^^^^
  ```

- Warning: `workflows/bacass.nf:658:82`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_multiqc_custom_methods_description = params.multiqc_methods_description ? Channel.fromPath(params.multiqc_methods_description, checkIfExists: true) : Channel.fromPath("$projectDir/assets/methods_description_template.yml", checkIfExists: true)
                                                                                   ^^^^^^^
  ```

- Warning: `workflows/bacass.nf:658:158`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_multiqc_custom_methods_description = params.multiqc_methods_description ? Channel.fromPath(params.multiqc_methods_description, checkIfExists: true) : Channel.fromPath("$projectDir/assets/methods_description_template.yml", checkIfExists: true)
                                                                                                                                                               ^^^^^^^
  ```

- Warning: `workflows/bacass.nf:667:39`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          ch_fastqc_raw_multiqc.collect{it[1]}.ifEmpty([]),
                                        ^^
  ```

- Warning: `workflows/bacass.nf:668:40`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          ch_fastqc_trim_multiqc.collect{it[1]}.ifEmpty([]),
                                         ^^
  ```

- Warning: `workflows/bacass.nf:669:39`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          ch_fastp_json_multiqc.collect{it[1]}.ifEmpty([]),
                                        ^^
  ```

- Warning: `workflows/bacass.nf:670:41`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          ch_nanoplot_txt_multiqc.collect{it[1]}.ifEmpty([]),
                                          ^^
  ```

- Warning: `workflows/bacass.nf:671:41`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          ch_porechop_log_multiqc.collect{it[1]}.ifEmpty([]),
                                          ^^
  ```

- Warning: `workflows/bacass.nf:672:41`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          ch_filtlong_log_multiqc.collect{it[1]}.ifEmpty([]),
                                          ^^
  ```

- Warning: `workflows/bacass.nf:673:35`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          ch_pycoqc_multiqc.collect{it[1]}.ifEmpty([]),
                                    ^^
  ```

- Warning: `workflows/bacass.nf:674:41`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          ch_kraken_short_multiqc.collect{it[1]}.ifEmpty([]),
                                          ^^
  ```

- Warning: `workflows/bacass.nf:675:40`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          ch_kraken_long_multiqc.collect{it[1]}.ifEmpty([]),
                                         ^^
  ```

- Warning: `workflows/bacass.nf:676:34`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          ch_quast_multiqc.collect{it[1]}.ifEmpty([]),
                                   ^^
  ```

- Warning: `workflows/bacass.nf:677:34`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          ch_busco_multiqc.collect{it[1]}.ifEmpty([]),
                                   ^^
  ```

- Warning: `workflows/bacass.nf:682:5`: Variable was declared but not used

  ```nextflow
      multiqc_report = CUSTOM_MULTIQC.out.report.toList()
      ^^^^^^^^^^^^^^
  ```
