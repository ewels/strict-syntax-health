# Nextflow lint results

- Generated: 2026-01-14T09:10:31.545733117Z
- Nextflow version: 25.12.0-edge
- Summary: 38 errors, 58 warnings

## :x: Errors

- Error: `main.nf:19:1`: Included name 'PIPELINE_INITIALISATION' is not defined in module '/home/runner/work/strict-syntax-health/strict-syntax-health/pipelines/coproid/subworkflows/local/utils_nfcore_coproid_pipeline/main.nf'

  ```nextflow
  include { PIPELINE_INITIALISATION } from './subworkflows/local/utils_nfcore_coproid_pipeline'
  ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  ```

- Error: `main.nf:75:5`: `PIPELINE_INITIALISATION` is not defined

  ```nextflow
      PIPELINE_INITIALISATION (
      ^^^^^^^^^^^^^^^^^^^^^^^
  ```

- Error: `main.nf:89:9`: `PIPELINE_INITIALISATION` is not defined

  ```nextflow
          PIPELINE_INITIALISATION.out.samplesheet,
          ^^^^^^^^^^^^^^^^^^^^^^^
  ```

- Error: `main.nf:90:9`: `PIPELINE_INITIALISATION` is not defined

  ```nextflow
          PIPELINE_INITIALISATION.out.genomesheet
          ^^^^^^^^^^^^^^^^^^^^^^^
  ```

- Error: `modules/nf-core/quartonotebook/parametrize.nf:1:1`: Groovy `import` declarations are not supported -- use fully-qualified name inline instead

  ```nextflow
  import org.yaml.snakeyaml.Yaml
  ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  ```

- Error: `modules/nf-core/quartonotebook/parametrize.nf:2:1`: Groovy `import` declarations are not supported -- use fully-qualified name inline instead

  ```nextflow
  import org.yaml.snakeyaml.DumperOptions
  ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  ```

- Error: `modules/nf-core/quartonotebook/parametrize.nf:21:29`: `DumperOptions` is not defined

  ```nextflow
      DumperOptions options = new DumperOptions();
                              ^^^^^^^^^^^^^^^^^^^
  ```

- Error: `modules/nf-core/quartonotebook/parametrize.nf:22:33`: `DumperOptions` is not defined

  ```nextflow
      options.setDefaultFlowStyle(DumperOptions.FlowStyle.BLOCK);
                                  ^^^^^^^^^^^^^
  ```

- Error: `modules/nf-core/quartonotebook/parametrize.nf:23:16`: `Yaml` is not defined

  ```nextflow
      def yaml = new Yaml(options)
                 ^^^^^^^^^^^^^^^^^
  ```

- Error: `modules/nf-core/sam2lca/analyze/main.nf:28:9`: `database` is already declared

  ```nextflow
      def database = database ? "${database}" : "sam2lca_db"
          ^^^^^^^^
  ```

- Error: `modules/nf-core/sourcepredict/main.nf:29:9`: `save_embedding` is already declared

  ```nextflow
      def save_embedding = save_embedding ? "-e ${prefix}.embedding.sourcepredict.csv" : ""
          ^^^^^^^^^^^^^^
  ```

- Error: `nextflow.config:215:1`: Variable declarations cannot be mixed with config statements

  ```nextflow
  def trace_timestamp = new java.util.Date().format( 'yyyy-MM-dd_HH-mm-ss')
  ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  ```

- Error: `nextflow.config:218:68`: `trace_timestamp` is not defined

  ```nextflow
      file    = "${params.outdir}/pipeline_info/execution_timeline_${trace_timestamp}.html"
                                                                     ^^^^^^^^^^^^^^^
  ```

- Error: `nextflow.config:222:66`: `trace_timestamp` is not defined

  ```nextflow
      file    = "${params.outdir}/pipeline_info/execution_report_${trace_timestamp}.html"
                                                                   ^^^^^^^^^^^^^^^
  ```

- Error: `nextflow.config:226:65`: `trace_timestamp` is not defined

  ```nextflow
      file    = "${params.outdir}/pipeline_info/execution_trace_${trace_timestamp}.txt"
                                                                  ^^^^^^^^^^^^^^^
  ```

- Error: `nextflow.config:230:62`: `trace_timestamp` is not defined

  ```nextflow
      file    = "${params.outdir}/pipeline_info/pipeline_dag_${trace_timestamp}.html"
                                                               ^^^^^^^^^^^^^^^
  ```

- Error: `nextflow.config:290:31`: `manifest` is not defined

  ```nextflow
  \033[0;35m  nf-core/coproid ${manifest.version}\033[0m
                                ^^^^^^^^
  ```

- Error: `nextflow.config:293:26`: `manifest` is not defined

  ```nextflow
          afterText = """${manifest.doi ? "\n* The pipeline\n" : ""}${manifest.doi.tokenize(",").collect { "    https://doi.org/${it.trim().replace('https://doi.org/','')}"}.join("\n")}${manifest.doi ? "\n" : ""}
                           ^^^^^^^^
  ```

- Error: `nextflow.config:293:69`: `manifest` is not defined

  ```nextflow
          afterText = """${manifest.doi ? "\n* The pipeline\n" : ""}${manifest.doi.tokenize(",").collect { "    https://doi.org/${it.trim().replace('https://doi.org/','')}"}.join("\n")}${manifest.doi ? "\n" : ""}
                                                                      ^^^^^^^^
  ```

- Error: `nextflow.config:293:186`: `manifest` is not defined

  ```nextflow
          afterText = """${manifest.doi ? "\n* The pipeline\n" : ""}${manifest.doi.tokenize(",").collect { "    https://doi.org/${it.trim().replace('https://doi.org/','')}"}.join("\n")}${manifest.doi ? "\n" : ""}
                                                                                                                                                                                           ^^^^^^^^
  ```

- Error: `nextflow.config:302:22`: `validation` is not defined

  ```nextflow
          beforeText = validation.help.beforeText
                       ^^^^^^^^^^
  ```

- Error: `nextflow.config:303:21`: `validation` is not defined

  ```nextflow
          afterText = validation.help.afterText
                      ^^^^^^^^^^
  ```

- Error: `subworkflows/local/kraken2_classification/main.nf:8:1`: Statements cannot be mixed with script declarations -- move statements into a process or workflow

  ```nextflow
  ch_sp_sources      = file(params.sp_sources)
  ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  ```

- Error: `subworkflows/local/kraken2_classification/main.nf:9:1`: Statements cannot be mixed with script declarations -- move statements into a process or workflow

  ```nextflow
  ch_sp_labels       = file(params.sp_labels)
  ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  ```

- Error: `subworkflows/local/kraken2_classification/main.nf:10:1`: Statements cannot be mixed with script declarations -- move statements into a process or workflow

  ```nextflow
  ch_sqlite_traverse = file(params.taxa_sqlite_traverse_pkl)
  ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  ```

- Error: `subworkflows/local/kraken2_classification/main.nf:24:17`: `kraken2_db` is already declared

  ```nextflow
                  kraken2_db -> [
                  ^^^^^^^^^^
  ```

- Error: `subworkflows/local/kraken2_classification/main.nf:89:9`: `ch_sp_sources` is not defined

  ```nextflow
          ch_sp_sources,
          ^^^^^^^^^^^^^
  ```

- Error: `subworkflows/local/kraken2_classification/main.nf:90:9`: `ch_sp_labels` is not defined

  ```nextflow
          ch_sp_labels,
          ^^^^^^^^^^^^
  ```

- Error: `subworkflows/local/kraken2_classification/main.nf:92:9`: `ch_sqlite_traverse` is not defined

  ```nextflow
          ch_sqlite_traverse,
          ^^^^^^^^^^^^^^^^^^
  ```

- Error: `subworkflows/local/prepare_genome_indices/main.nf:48:49`: `igenome` is not defined

  ```nextflow
          genome_meta = [meta, file(params.genomes[ igenome ][ fasta ]), path(params.genomes[ igenome ][ bowtie2 ])]
                                                  ^^^^^^^^^^^
  ```

- Error: `subworkflows/local/prepare_genome_indices/main.nf:48:60`: `fasta` is not defined

  ```nextflow
          genome_meta = [meta, file(params.genomes[ igenome ][ fasta ]), path(params.genomes[ igenome ][ bowtie2 ])]
                                                             ^^^^^^^^^
  ```

- Error: `subworkflows/local/prepare_genome_indices/main.nf:48:72`: `path` is not defined

  ```nextflow
          genome_meta = [meta, file(params.genomes[ igenome ][ fasta ]), path(params.genomes[ igenome ][ bowtie2 ])]
                                                                         ^^^^
  ```

- Error: `subworkflows/local/prepare_genome_indices/main.nf:48:91`: `igenome` is not defined

  ```nextflow
          genome_meta = [meta, file(params.genomes[ igenome ][ fasta ]), path(params.genomes[ igenome ][ bowtie2 ])]
                                                                                            ^^^^^^^^^^^
  ```

- Error: `subworkflows/local/prepare_genome_indices/main.nf:48:102`: `bowtie2` is not defined

  ```nextflow
          genome_meta = [meta, file(params.genomes[ igenome ][ fasta ]), path(params.genomes[ igenome ][ bowtie2 ])]
                                                                                                       ^^^^^^^^^^^
  ```

- Error: `subworkflows/local/quarto_reporting/main.nf:26:9`: `coproid_notebook` is already declared

  ```nextflow
          coproid_notebook ->
          ^^^^^^^^^^^^^^^^
  ```

- Error: `subworkflows/local/utils_nfcore_coproid_pipeline/main.nf:27:1`: Invalid workflow definition -- check for missing or out-of-order section labels

  ```nextflow
  workflow PIPELINE_INITIALISATION {
  ^
  ```

- Error: `workflows/coproid.nf:37:1`: Statements cannot be mixed with script declarations -- move statements into a process or workflow

  ```nextflow
  ch_kraken2_db = file(params.kraken2_db)
  ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  ```

- Error: `workflows/coproid.nf:212:9`: `ch_kraken2_db` is not defined

  ```nextflow
          ch_kraken2_db
          ^^^^^^^^^^^^^
  ```

## :warning: Warnings

- Warning: `modules/local/create_acc2tax/main.nf:18:9`: Variable was declared but not used

  ```nextflow
      def args = task.ext.args ?: ""
          ^^^^
  ```

- Warning: `modules/local/damageprofiler/merge/main.nf:17:9`: Variable was declared but not used

  ```nextflow
      def args = task.ext.args   ?: ''
          ^^^^
  ```

- Warning: `modules/local/kraken/merge/main.nf:18:9`: Variable was declared but not used

  ```nextflow
      def args = task.ext.args   ?: ''
          ^^^^
  ```

- Warning: `modules/local/kraken/parse/main.nf:19:9`: Variable was declared but not used

  ```nextflow
      def args = task.ext.args   ?: ''
          ^^^^
  ```

- Warning: `modules/local/pydamage/merge/main.nf:17:9`: Variable was declared but not used

  ```nextflow
      def args = task.ext.args   ?: ''
          ^^^^
  ```

- Warning: `modules/local/sam2lca/merge/main.nf:18:9`: Variable was declared but not used

  ```nextflow
      def args = task.ext.args   ?: ''
          ^^^^
  ```

- Warning: `modules/local/sam2lca/prep_db/main.nf:19:9`: Variable was declared but not used

  ```nextflow
      def args = task.ext.args ?: ""
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

- Warning: `modules/nf-core/quartonotebook/main.nf:102:9`: Variable was declared but not used

  ```nextflow
      def args = task.ext.args ?: ''
          ^^^^
  ```

- Warning: `modules/nf-core/sam2lca/analyze/main.nf:45:9`: Variable was declared but not used

  ```nextflow
      def args = task.ext.args ?: ''
          ^^^^
  ```

- Warning: `modules/nf-core/sourcepredict/main.nf:50:9`: Variable was declared but not used

  ```nextflow
      def args = task.ext.args ?: ''
          ^^^^
  ```

- Warning: `nextflow.config:293:129`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          afterText = """${manifest.doi ? "\n* The pipeline\n" : ""}${manifest.doi.tokenize(",").collect { "    https://doi.org/${it.trim().replace('https://doi.org/','')}"}.join("\n")}${manifest.doi ? "\n" : ""}
                                                                                                                                  ^^
  ```

- Warning: `subworkflows/local/align_index/main.nf:9:23`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
          ch_versions = Channel.empty()
                        ^^^^^^^
  ```

- Warning: `subworkflows/local/kraken2_classification/main.nf:8:1`: Variable was declared but not used

  ```nextflow
  ch_sp_sources      = file(params.sp_sources)
  ^^^^^^^^^^^^^
  ```

- Warning: `subworkflows/local/kraken2_classification/main.nf:9:1`: Variable was declared but not used

  ```nextflow
  ch_sp_labels       = file(params.sp_labels)
  ^^^^^^^^^^^^
  ```

- Warning: `subworkflows/local/kraken2_classification/main.nf:10:1`: Variable was declared but not used

  ```nextflow
  ch_sqlite_traverse = file(params.taxa_sqlite_traverse_pkl)
  ^^^^^^^^^^^^^^^^^^
  ```

- Warning: `subworkflows/local/kraken2_classification/main.nf:18:23`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
          ch_versions = Channel.empty()
                        ^^^^^^^
  ```

- Warning: `subworkflows/local/kraken2_classification/main.nf:21:13`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
              Channel
              ^^^^^^^
  ```

- Warning: `subworkflows/local/kraken2_classification/main.nf:77:55`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
              sqlite      = XZ_DECOMPRESS.out.file.map{ it[1] }
                                                        ^^
  ```

- Warning: `subworkflows/local/merge_sort_index_samtools/main.nf:10:19`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_versions = Channel.empty()
                    ^^^^^^^
  ```

- Warning: `subworkflows/local/prepare_genome_indices/main.nf:9:19`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_versions = Channel.empty()
                    ^^^^^^^
  ```

- Warning: `subworkflows/local/prepare_genome_indices/main.nf:12:38`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          .map { create_genome_channel(it) }
                                       ^^
  ```

- Warning: `subworkflows/local/prepare_genome_indices/main.nf:17:26`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
              index_avail: it.size() > 2
                           ^^
  ```

- Warning: `subworkflows/local/prepare_genome_indices/main.nf:18:29`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
              no_index_avail: it.size() == 2
                              ^^
  ```

- Warning: `subworkflows/local/quarto_reporting/main.nf:14:19`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_versions = Channel.empty()
                    ^^^^^^^
  ```

- Warning: `subworkflows/local/quarto_reporting/main.nf:20:18`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      extensions = Channel.fromPath("${projectDir}/assets/_extensions").collect()
                   ^^^^^^^
  ```

- Warning: `subworkflows/local/quarto_reporting/main.nf:23:5`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      Channel
      ^^^^^^^
  ```

- Warning: `subworkflows/local/sam2lca_db/main.nf:15:23`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
          ch_versions = Channel.empty()
                        ^^^^^^^
  ```

- Warning: `subworkflows/nf-core/utils_nfcore_pipeline/main.nf:101:98`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      return ch_versions.unique().map { version -> processVersionsFromYAML(version) }.unique().mix(Channel.of(workflowVersionToYAML()))
                                                                                                   ^^^^^^^
  ```

- Warning: `workflows/coproid.nf:37:1`: Variable was declared but not used

  ```nextflow
  ch_kraken2_db = file(params.kraken2_db)
  ^^^^^^^^^^^^^
  ```

- Warning: `workflows/coproid.nf:53:24`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_versions      = Channel.empty()
                         ^^^^^^^
  ```

- Warning: `workflows/coproid.nf:54:24`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_multiqc_files = Channel.empty()
                         ^^^^^^^
  ```

- Warning: `workflows/coproid.nf:71:68`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
      ch_multiqc_files = ch_multiqc_files.mix(FASTQC.out.zip.collect{it[1]})
                                                                     ^^
  ```

- Warning: `workflows/coproid.nf:84:5`: Variable was declared but not used

  ```nextflow
      ch_trimmed       = FASTP.out.reads
      ^^^^^^^^^^
  ```

- Warning: `workflows/coproid.nf:85:68`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
      ch_multiqc_files = ch_multiqc_files.mix(FASTP.out.json.collect{it[1]})
                                                                     ^^
  ```

- Warning: `workflows/coproid.nf:117:83`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
      ch_multiqc_files = ch_multiqc_files.mix(ALIGN_INDEX.out.multiqc_files.collect{it[1]})
                                                                                    ^^
  ```

- Warning: `workflows/coproid.nf:126:80`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
      ch_multiqc_files = ch_multiqc_files.mix(DAMAGEPROFILER.out.results.collect{it[1]})
                                                                                 ^^
  ```

- Warning: `workflows/coproid.nf:128:41`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
      DAMAGEPROFILER.out.results.collect({it[1]})
                                          ^^
  ```

- Warning: `workflows/coproid.nf:148:39`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
      PYDAMAGE_ANALYZE.out.csv.collect({it[1]})
                                        ^^
  ```

- Warning: `workflows/coproid.nf:160:20`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          meta, bam, bai -> [['id':meta.sample_name], bam] // meta.id, bam
                     ^^^
  ```

- Warning: `workflows/coproid.nf:174:30`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
                  meta, fasta, index -> [meta, fasta]
                               ^^^^^
  ```

- Warning: `workflows/coproid.nf:184:25`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
          ch_sam2lca_db = Channel.fromPath(params.sam2lca_db).first()
                          ^^^^^^^
  ```

- Warning: `workflows/coproid.nf:196:5`: Variable was declared but not used

  ```nextflow
      ch_sam2lca  = SAM2LCA_ANALYZE.out.csv
      ^^^^^^^^^^
  ```

- Warning: `workflows/coproid.nf:199:38`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
      SAM2LCA_ANALYZE.out.csv.collect({it[1]})
                                       ^^
  ```

- Warning: `workflows/coproid.nf:214:94`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
      ch_multiqc_files = ch_multiqc_files.mix(KRAKEN2_CLASSIFICATION.out.kraken_report.collect{it[1]})
                                                                                               ^^
  ```

- Warning: `workflows/coproid.nf:230:62`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
              KRAKEN2_CLASSIFICATION.out.sp_report.collectFile{it[1]},
                                                               ^^
  ```

- Warning: `workflows/coproid.nf:231:65`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
              KRAKEN2_CLASSIFICATION.out.sp_embedding.collectFile{it[1]},
                                                                  ^^
  ```

- Warning: `workflows/coproid.nf:234:13`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
              Channel.fromPath(params.genome_sheet),
              ^^^^^^^
  ```

- Warning: `workflows/coproid.nf:249:32`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_multiqc_config        = Channel.fromPath(
                                 ^^^^^^^
  ```

- Warning: `workflows/coproid.nf:252:9`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
          Channel.fromPath(params.multiqc_config, checkIfExists: true) :
          ^^^^^^^
  ```

- Warning: `workflows/coproid.nf:253:9`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
          Channel.empty()
          ^^^^^^^
  ```

- Warning: `workflows/coproid.nf:255:9`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
          Channel.fromPath(params.multiqc_logo, checkIfExists: true) :
          ^^^^^^^
  ```

- Warning: `workflows/coproid.nf:256:9`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
          Channel.empty()
          ^^^^^^^
  ```

- Warning: `workflows/coproid.nf:261:32`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_workflow_summary      = Channel.value(paramsSummaryMultiqc(summary_params))
                                 ^^^^^^^
  ```

- Warning: `workflows/coproid.nf:268:45`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_methods_description                = Channel.value(
                                              ^^^^^^^
  ```
