# Nextflow lint results

- Generated: 2026-01-16T10:30:26.935907564Z
- Nextflow version: 25.12.0-edge
- Summary: 28 errors, 36 warnings

## :x: Errors

- Error: `modules/local/expressionatlas/getaccessions/main.nf:27:19`: `PWD` is not defined

  ```nextflow
          NLTK_DATA=$PWD get_eatlas_accessions.py --species $species
                    ^^^^
  ```

- Error: `modules/local/expressionatlas/getaccessions/main.nf:31:19`: `PWD` is not defined

  ```nextflow
          NLTK_DATA=$PWD get_eatlas_accessions.py --species $species --keywords $keywords_string
                    ^^^^
  ```

- Error: `modules/local/expressionatlas/getdata/main.nf:10:5`: Invalid process directive

  ```nextflow
      errorStrategy = {
      ^
  ```

- Error: `modules/local/expressionatlas/getdata/main.nf:36:5`: Invalid process directive

  ```nextflow
      maxRetries = 5
      ^^^^^^^^^^^^^^
  ```

- Error: `modules/local/gene_statistics/main.nf:9:17`: Unexpected input: '+'

  ```nextflow
                  + "Please check the provided accessions and datasets and run again"
                  ^
  ```

- Error: `modules/local/gprofiler/idmapping/main.nf:12:5`: Invalid process directive

  ```nextflow
      errorStrategy = {
      ^
  ```

- Error: `nextflow.config:295:40`: `manifest` is not defined

  ```nextflow
  \033[0;35m  nf-core/stableexpression ${manifest.version}\033[0m
                                         ^^^^^^^^
  ```

- Error: `nextflow.config:298:26`: `manifest` is not defined

  ```nextflow
          afterText = """${manifest.doi ? "\n* The pipeline\n" : ""}${manifest.doi.tokenize(",").collect { "    https://doi.org/${it.trim().replace('https://doi.org/','')}"}.join("\n")}${manifest.doi ? "\n" : ""}
                           ^^^^^^^^
  ```

- Error: `nextflow.config:298:69`: `manifest` is not defined

  ```nextflow
          afterText = """${manifest.doi ? "\n* The pipeline\n" : ""}${manifest.doi.tokenize(",").collect { "    https://doi.org/${it.trim().replace('https://doi.org/','')}"}.join("\n")}${manifest.doi ? "\n" : ""}
                                                                      ^^^^^^^^
  ```

- Error: `nextflow.config:298:186`: `manifest` is not defined

  ```nextflow
          afterText = """${manifest.doi ? "\n* The pipeline\n" : ""}${manifest.doi.tokenize(",").collect { "    https://doi.org/${it.trim().replace('https://doi.org/','')}"}.join("\n")}${manifest.doi ? "\n" : ""}
                                                                                                                                                                                           ^^^^^^^^
  ```

- Error: `nextflow.config:307:22`: `validation` is not defined

  ```nextflow
          beforeText = validation.help.beforeText
                       ^^^^^^^^^^
  ```

- Error: `nextflow.config:308:21`: `validation` is not defined

  ```nextflow
          afterText = validation.help.afterText
                      ^^^^^^^^^^
  ```

- Error: `subworkflows/local/utils_nfcore_stableexpression_pipeline/main.nf:5:1`: Groovy `import` declarations are not supported -- use fully-qualified name inline instead

  ```nextflow
  import org.yaml.snakeyaml.Yaml
  ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  ```

- Error: `subworkflows/local/utils_nfcore_stableexpression_pipeline/main.nf:161:9`: `for` loops are no longer supported

  ```nextflow
          for ( accession in params.eatlas_accessions.tokenize(',') ) {
          ^^^
  ```

- Error: `subworkflows/local/utils_nfcore_stableexpression_pipeline/main.nf:161:15`: `accession` is not defined

  ```nextflow
          for ( accession in params.eatlas_accessions.tokenize(',') ) {
                ^^^^^^^^^
  ```

- Error: `subworkflows/local/utils_nfcore_stableexpression_pipeline/main.nf:162:19`: `accession` is not defined

  ```nextflow
              if ( !accession.startsWith('E-') ) {
                    ^^^^^^^^^
  ```

- Error: `subworkflows/local/utils_nfcore_stableexpression_pipeline/main.nf:163:55`: `accession` is not defined

  ```nextflow
                  error('Expression Atlas accession ' + accession + ' is not well formated. All accessions should start with "E-".')
                                                        ^^^^^^^^^
  ```

- Error: `subworkflows/local/utils_nfcore_stableexpression_pipeline/main.nf:174:30`: `samplesheetToList` is not defined

  ```nextflow
      return Channel.fromList( samplesheetToList(samplesheet, "assets/schema_datasets.json") )
                               ^^^^^^^^^^^^^^^^^
  ```

- Error: `subworkflows/local/utils_nfcore_stableexpression_pipeline/main.nf:178:21`: `new_meta` was assigned but not declared

  ```nextflow
                      new_meta = meta + [dataset: count_file.getBaseName()]
                      ^^^^^^^^
  ```

- Error: `subworkflows/local/utils_nfcore_stableexpression_pipeline/main.nf:179:22`: `new_meta` is not defined

  ```nextflow
                      [new_meta, count_file]
                       ^^^^^^^^
  ```

- Error: `subworkflows/local/utils_nfcore_stableexpression_pipeline/main.nf:275:17`: `Yaml` is not defined

  ```nextflow
      Yaml yaml = new Yaml()
                  ^^^^^^^^^^
  ```

- Error: `subworkflows/local/utils_nfcore_stableexpression_pipeline/main.nf:276:5`: `versions` was assigned but not declared

  ```nextflow
      versions = yaml.load(yaml_file)
      ^^^^^^^^
  ```

- Error: `subworkflows/local/utils_nfcore_stableexpression_pipeline/main.nf:277:27`: `versions` is not defined

  ```nextflow
      return yaml.dumpAsMap(versions).trim()
                            ^^^^^^^^
  ```

- Error: `workflows/stableexpression.nf:12:1`: Module could not be parsed: '/home/runner/work/strict-syntax-health/strict-syntax-health/pipelines/stableexpression/modules/local/gene_statistics/main.nf'

  ```nextflow
  include { GENE_STATISTICS                        } from '../modules/local/gene_statistics/main'
  ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  ```

- Error: `workflows/stableexpression.nf:125:5`: `GENE_STATISTICS` is not defined

  ```nextflow
      GENE_STATISTICS(
      ^^^^^^^^^^^^^^^
  ```

- Error: `workflows/stableexpression.nf:135:31`: `GENE_STATISTICS` is not defined

  ```nextflow
                          .mix( GENE_STATISTICS.out.top_stable_genes_summary.collect() )
                                ^^^^^^^^^^^^^^^
  ```

- Error: `workflows/stableexpression.nf:136:31`: `GENE_STATISTICS` is not defined

  ```nextflow
                          .mix( GENE_STATISTICS.out.all_statistics.collect() )
                                ^^^^^^^^^^^^^^^
  ```

- Error: `workflows/stableexpression.nf:137:31`: `GENE_STATISTICS` is not defined

  ```nextflow
                          .mix( GENE_STATISTICS.out.top_stable_genes_transposed_counts.collect() )
                                ^^^^^^^^^^^^^^^
  ```

## :warning: Warnings

- Warning: `modules/local/expressionatlas/getaccessions/main.nf:22:57`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
      def keywords_string = keywords.split(',').collect { it.trim() }.join(' ')
                                                          ^^
  ```

- Warning: `nextflow.config:298:129`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          afterText = """${manifest.doi ? "\n* The pipeline\n" : ""}${manifest.doi.tokenize(",").collect { "    https://doi.org/${it.trim().replace('https://doi.org/','')}"}.join("\n")}${manifest.doi ? "\n" : ""}
                                                                                                                                  ^^
  ```

- Warning: `subworkflows/local/expression_normalisation/main.nf:37:15`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          meta, file ->
                ^^^^
  ```

- Warning: `subworkflows/local/expression_normalisation/main.nf:42:61`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
      ch_raw_rnaseq_datasets = ch_datasets.raw.filter { meta, file -> meta.platform == 'rnaseq' }
                                                              ^^^^
  ```

- Warning: `subworkflows/local/expressionatlas_fetchdata/main.nf:31:21`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_accessions = Channel.fromList( eatlas_accessions.tokenize(',') )
                      ^^^^^^^
  ```

- Warning: `subworkflows/local/expressionatlas_fetchdata/main.nf:39:30`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
          ch_eatlas_keywords = Channel.value( eatlas_keywords )
                               ^^^^^^^
  ```

- Warning: `subworkflows/local/expressionatlas_fetchdata/main.nf:52:39`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
                              .filter { it.startsWith('E-') && !it.startsWith('E-PROT-') }
                                        ^^
  ```

- Warning: `subworkflows/local/expressionatlas_fetchdata/main.nf:52:63`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
                              .filter { it.startsWith('E-') && !it.startsWith('E-PROT-') }
                                                                ^^
  ```

- Warning: `subworkflows/local/expressionatlas_fetchdata/main.nf:107:13`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
              it.get(1).size() == 2 // only groups with two files
              ^^
  ```

- Warning: `subworkflows/local/expressionatlas_fetchdata/main.nf:110:13`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
              meta, files ->
              ^^^^
  ```

- Warning: `subworkflows/local/utils_nfcore_stableexpression_pipeline/main.nf:33:5`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
      monochrome_logs   // boolean: Do not use coloured log outputs
      ^^^^^^^^^^^^^^^
  ```

- Warning: `subworkflows/local/utils_nfcore_stableexpression_pipeline/main.nf:76:29`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
          ch_input_datasets = Channel.empty()
                              ^^^^^^^
  ```

- Warning: `subworkflows/local/utils_nfcore_stableexpression_pipeline/main.nf:174:12`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      return Channel.fromList( samplesheetToList(samplesheet, "assets/schema_datasets.json") )
             ^^^^^^^
  ```

- Warning: `subworkflows/local/utils_nfcore_stableexpression_pipeline/main.nf:190:15`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          meta, file ->
                ^^^^
  ```

- Warning: `subworkflows/local/utils_nfcore_stableexpression_pipeline/main.nf:285:12`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      return Channel.of(workflowVersionToYAML())
             ^^^^^^^
  ```

- Warning: `subworkflows/local/utils_nfcore_stableexpression_pipeline/main.nf:298:54`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
                  .map { customProcessVersionsFromYAML(it) }
                                                       ^^
  ```

- Warning: `subworkflows/nf-core/utils_nfcore_pipeline/main.nf:116:98`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      return ch_versions.unique().map { version -> processVersionsFromYAML(version) }.unique().mix(Channel.of(workflowVersionToYAML()))
                                                                                                   ^^^^^^^
  ```

- Warning: `workflows/stableexpression.nf:35:24`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_multiqc_files = Channel.empty()
                         ^^^^^^^
  ```

- Warning: `workflows/stableexpression.nf:36:18`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_species = Channel.value( params.species.split(' ').join('_') )
                   ^^^^^^^
  ```

- Warning: `workflows/stableexpression.nf:56:24`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_gene_metadata = Channel.empty()
                         ^^^^^^^
  ```

- Warning: `workflows/stableexpression.nf:58:28`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
          ch_gene_metadata = Channel.fromPath( params.gene_metadata, checkIfExists: true )
                             ^^^^^^^
  ```

- Warning: `workflows/stableexpression.nf:63:30`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
          ch_gene_id_mapping = Channel.empty()
                               ^^^^^^^
  ```

- Warning: `workflows/stableexpression.nf:66:34`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
              ch_gene_id_mapping = Channel.fromPath( params.gene_id_mapping, checkIfExists: true )
                                   ^^^^^^^
  ```

- Warning: `workflows/stableexpression.nf:73:38`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
              params.gene_id_mapping ? Channel.fromPath( params.gene_id_mapping, checkIfExists: true ) : 'none'
                                       ^^^^^^^
  ```

- Warning: `workflows/stableexpression.nf:98:16`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          .map { meta, file -> [file] }
                 ^^^^
  ```

- Warning: `workflows/stableexpression.nf:103:22`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          .map { meta, file -> [meta.design] }
                       ^^^^
  ```

- Warning: `workflows/stableexpression.nf:108:16`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          .map { meta, file -> [file] }
                 ^^^^
  ```

- Warning: `workflows/stableexpression.nf:119:5`: Variable was declared but not used

  ```nextflow
      ch_candidate_gene_counts = MERGE_DATA.out.candidate_gene_counts
      ^^^^^^^^^^^^^^^^^^^^^^^^
  ```

- Warning: `workflows/stableexpression.nf:149:58`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_collated_versions = customSoftwareVersionsToYAML( Channel.topic('versions') )
                                                           ^^^^^^^
  ```

- Warning: `workflows/stableexpression.nf:160:32`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_multiqc_config        = Channel.fromPath(
                                 ^^^^^^^
  ```

- Warning: `workflows/stableexpression.nf:163:9`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
          Channel.fromPath(params.multiqc_config, checkIfExists: true) :
          ^^^^^^^
  ```

- Warning: `workflows/stableexpression.nf:164:9`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
          Channel.empty()
          ^^^^^^^
  ```

- Warning: `workflows/stableexpression.nf:166:9`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
          Channel.fromPath(params.multiqc_logo, checkIfExists: true) :
          ^^^^^^^
  ```

- Warning: `workflows/stableexpression.nf:167:9`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
          Channel.empty()
          ^^^^^^^
  ```

- Warning: `workflows/stableexpression.nf:171:27`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_workflow_summary = Channel.value(paramsSummaryMultiqc(summary_params))
                            ^^^^^^^
  ```

- Warning: `workflows/stableexpression.nf:177:45`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_methods_description                = Channel.value(
                                              ^^^^^^^
  ```
