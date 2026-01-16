# Nextflow lint results

- Generated: 2026-01-16T06:41:53.386258181Z
- Nextflow version: 25.12.0-edge
- Summary: 6 errors, 57 warnings

## :x: Errors

- Error: `nextflow.config:324:34`: `manifest` is not defined

  ```nextflow
  \033[0;35m  nf-core/tfactivity ${manifest.version}\033[0m
                                   ^^^^^^^^
  ```

- Error: `nextflow.config:327:26`: `manifest` is not defined

  ```nextflow
          afterText = """${manifest.doi ? "\n* The pipeline\n" : ""}${manifest.doi.tokenize(",").collect { "    https://doi.org/${it.trim().replace('https://doi.org/','')}"}.join("\n")}${manifest.doi ? "\n" : ""}
                           ^^^^^^^^
  ```

- Error: `nextflow.config:327:69`: `manifest` is not defined

  ```nextflow
          afterText = """${manifest.doi ? "\n* The pipeline\n" : ""}${manifest.doi.tokenize(",").collect { "    https://doi.org/${it.trim().replace('https://doi.org/','')}"}.join("\n")}${manifest.doi ? "\n" : ""}
                                                                      ^^^^^^^^
  ```

- Error: `nextflow.config:327:186`: `manifest` is not defined

  ```nextflow
          afterText = """${manifest.doi ? "\n* The pipeline\n" : ""}${manifest.doi.tokenize(",").collect { "    https://doi.org/${it.trim().replace('https://doi.org/','')}"}.join("\n")}${manifest.doi ? "\n" : ""}
                                                                                                                                                                                           ^^^^^^^^
  ```

- Error: `nextflow.config:336:22`: `validation` is not defined

  ```nextflow
          beforeText = validation.help.beforeText
                       ^^^^^^^^^^
  ```

- Error: `nextflow.config:337:21`: `validation` is not defined

  ```nextflow
          afterText = validation.help.afterText
                      ^^^^^^^^^^
  ```

## :warning: Warnings

- Warning: `main.nf:54:19`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_versions = Channel.empty()
                    ^^^^^^^
  ```

- Warning: `main.nf:59:20`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_blacklist = Channel.value(params.blacklist ? file(params.blacklist, checkIfExists: true) : [])
                     ^^^^^^^
  ```

- Warning: `main.nf:61:17`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_counts = Channel.value(file(params.counts, checkIfExists: true))
                  ^^^^^^^
  ```

- Warning: `main.nf:104:9`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
          Channel.value([[id: "design"], file(params.counts_design, checkIfExists: true)]),
          ^^^^^^^
  ```

- Warning: `modules/nf-core/cat/cat/main.nf:23:40`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
      def file_list = files_in.collect { it.toString() }
                                         ^^
  ```

- Warning: `modules/nf-core/cat/cat/main.nf:58:42`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
      def file_list   = files_in.collect { it.toString() }
                                           ^^
  ```

- Warning: `modules/nf-core/gawk/main.nf:26:54`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
      suffix    = task.ext.suffix ?: "${input.collect{ it.getExtension()}.get(0)}" // use the first extension of the input files
                                                       ^^
  ```

- Warning: `modules/nf-core/gawk/main.nf:29:37`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
      lst_gz     = input.findResults{ it.getExtension().endsWith("gz") ? it.toString() : null }
                                      ^^
  ```

- Warning: `modules/nf-core/gawk/main.nf:29:72`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
      lst_gz     = input.findResults{ it.getExtension().endsWith("gz") ? it.toString() : null }
                                                                         ^^
  ```

- Warning: `modules/nf-core/gawk/main.nf:31:34`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
      input_cmd  = input.collect { it.toString() - ~/\.gz$/ }.join(" ")
                                   ^^
  ```

- Warning: `modules/nf-core/gawk/main.nf:34:49`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
      cleanup    = lst_gz ? "rm ${lst_gz.collect{ it - ~/\.gz$/ }.join(" ")}" : ""
                                                  ^^
  ```

- Warning: `modules/nf-core/gawk/main.nf:37:16`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          assert it.name != "${prefix}.${suffix}" : "Input and output names are the same, set prefix in module configuration to disambiguate!"
                 ^^
  ```

- Warning: `modules/nf-core/gawk/main.nf:59:51`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
      suffix = task.ext.suffix ?: "${input.collect{ it.getExtension()}.get(0)}"
                                                    ^^
  ```

- Warning: `modules/nf-core/gunzip/main.nf:43:9`: Variable was declared but not used

  ```nextflow
      def args = task.ext.args ?: ''
          ^^^^
  ```

- Warning: `nextflow.config:327:129`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          afterText = """${manifest.doi ? "\n* The pipeline\n" : ""}${manifest.doi.tokenize(",").collect { "    https://doi.org/${it.trim().replace('https://doi.org/','')}"}.join("\n")}${manifest.doi ? "\n" : ""}
                                                                                                                                  ^^
  ```

- Warning: `subworkflows/local/chromhmm/main.nf:17:19`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_versions = Channel.empty()
                    ^^^^^^^
  ```

- Warning: `subworkflows/local/chromhmm/main.nf:24:39`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
              ["cellmarkfiletable.tsv", it.join("\t") + "\n"]
                                        ^^
  ```

- Warning: `subworkflows/local/chromhmm/main.nf:26:17`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          .map { [it.baseName, it] }
                  ^^
  ```

- Warning: `subworkflows/local/chromhmm/main.nf:26:30`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          .map { [it.baseName, it] }
                               ^^
  ```

- Warning: `subworkflows/local/counts/main.nf:24:19`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_versions = Channel.empty()
                    ^^^^^^^
  ```

- Warning: `subworkflows/local/counts/main.nf:61:9`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
          Channel.value(["condition"]).combine(contrasts).map { variable, reference, target ->
          ^^^^^^^
  ```

- Warning: `subworkflows/local/dynamite/main.nf:16:19`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_versions = Channel.empty()
                    ^^^^^^^
  ```

- Warning: `subworkflows/local/fimo/main.nf:18:19`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_versions = Channel.empty()
                    ^^^^^^^
  ```

- Warning: `subworkflows/local/footprinting/main.nf:10:19`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_versions = Channel.empty()
                    ^^^^^^^
  ```

- Warning: `subworkflows/local/merge_samples/main.nf:14:19`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_versions = Channel.empty()
                    ^^^^^^^
  ```

- Warning: `subworkflows/local/motifs/main.nf:16:19`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_versions = Channel.empty()
                    ^^^^^^^
  ```

- Warning: `subworkflows/local/motifs/main.nf:19:21`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
          ch_motifs = Channel.value(motifs)
                      ^^^^^^^
  ```

- Warning: `subworkflows/local/motifs/main.nf:43:24`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          .splitText() { it.trim() }
                         ^^
  ```

- Warning: `subworkflows/local/motifs/main.nf:44:19`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          .filter { it.startsWith("Removing duplicate motif with symbol") }
                    ^^
  ```

- Warning: `subworkflows/local/motifs/main.nf:45:31`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          .subscribe { log.warn(it) }
                                ^^
  ```

- Warning: `subworkflows/local/peaks/main.nf:37:19`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_versions = Channel.empty()
                    ^^^^^^^
  ```

- Warning: `subworkflows/local/peaks/main.nf:58:23`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_chromhmm_out = Channel.empty()
                        ^^^^^^^
  ```

- Warning: `subworkflows/local/peaks/main.nf:65:19`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_rose_out = Channel.empty()
                    ^^^^^^^
  ```

- Warning: `subworkflows/local/peaks/main.nf:132:24`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          .splitText() { it.trim() }
                         ^^
  ```

- Warning: `subworkflows/local/peaks/main.nf:133:19`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          .filter { it.startsWith("Merging duplicate motif in") }
                    ^^
  ```

- Warning: `subworkflows/local/peaks/main.nf:134:31`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          .subscribe { log.warn(it) }
                                ^^
  ```

- Warning: `subworkflows/local/prepare_genome/main.nf:14:19`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_versions = Channel.empty()
                    ^^^^^^^
  ```

- Warning: `subworkflows/local/prepare_genome/main.nf:16:16`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_fasta = Channel.value([[id: 'fasta'], fasta])
                 ^^^^^^^
  ```

- Warning: `subworkflows/local/prepare_genome/main.nf:17:14`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_gtf = Channel.value([[id: 'gtf'], gtf])
               ^^^^^^^
  ```

- Warning: `subworkflows/local/ranking/main.nf:18:19`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_versions = Channel.empty()
                    ^^^^^^^
  ```

- Warning: `subworkflows/local/report/main.nf:49:27`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_workflow_summary = Channel.value(paramsSummaryToYAML(summary_params))
                            ^^^^^^^
  ```

- Warning: `subworkflows/local/report/main.nf:50:30`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_methods_description = Channel.value(methodsDescriptionText())
                               ^^^^^^^
  ```

- Warning: `subworkflows/local/rose/main.nf:21:19`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_versions = Channel.empty()
                    ^^^^^^^
  ```

- Warning: `subworkflows/local/rose/main.nf:47:29`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_filter_predictions = Channel.empty()
                              ^^^^^^^
  ```

- Warning: `subworkflows/local/sneep/main.nf:17:19`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_versions = Channel.empty()
                    ^^^^^^^
  ```

- Warning: `subworkflows/local/utils_nfcore_tfactivity_pipeline/main.nf:31:5`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
      monochrome_logs   // boolean: Do not use coloured log outputs
      ^^^^^^^^^^^^^^^
  ```

- Warning: `subworkflows/local/utils_nfcore_tfactivity_pipeline/main.nf:34:5`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
      input             //  string: Path to input samplesheet
      ^^^^^
  ```

- Warning: `subworkflows/local/utils_nfcore_tfactivity_pipeline/main.nf:38:19`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_versions = Channel.empty()
                    ^^^^^^^
  ```

- Warning: `subworkflows/local/utils_nfcore_tfactivity_pipeline/main.nf:75:5`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      Channel
      ^^^^^^^
  ```

- Warning: `subworkflows/local/utils_nfcore_tfactivity_pipeline/main.nf:78:38`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
              validateInputSamplesheet(it)
                                       ^^
  ```

- Warning: `subworkflows/local/utils_nfcore_tfactivity_pipeline/main.nf:82:45`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_samplesheet_bam = params.input_bam ? Channel.fromList(samplesheetToList(params.input_bam, "${projectDir}/assets/schema_input_bam.json")) : Channel.empty()
                                              ^^^^^^^
  ```

- Warning: `subworkflows/local/utils_nfcore_tfactivity_pipeline/main.nf:82:147`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_samplesheet_bam = params.input_bam ? Channel.fromList(samplesheetToList(params.input_bam, "${projectDir}/assets/schema_input_bam.json")) : Channel.empty()
                                                                                                                                                    ^^^^^^^
  ```

- Warning: `subworkflows/local/utils_nfcore_tfactivity_pipeline/main.nf:83:24`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_counts_design = Channel.fromList(samplesheetToList(params.counts_design, "${projectDir}/assets/schema_counts_design.json"))
                         ^^^^^^^
  ```

- Warning: `subworkflows/local/utils_nfcore_tfactivity_pipeline/main.nf:224:21`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          ].findAll { it }
                      ^^
  ```

- Warning: `subworkflows/nf-core/utils_nfcore_pipeline/main.nf:101:98`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      return ch_versions.unique().map { version -> processVersionsFromYAML(version) }.unique().mix(Channel.of(workflowVersionToYAML()))
                                                                                                   ^^^^^^^
  ```

- Warning: `workflows/tfactivity.nf:62:19`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_versions = Channel.empty()
                    ^^^^^^^
  ```

- Warning: `workflows/tfactivity.nf:136:29`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_fimo_binding_sites = Channel.empty()
                              ^^^^^^^
  ```
