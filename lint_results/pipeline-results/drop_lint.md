# Nextflow lint results

- Generated: 2026-01-16T06:31:20.978693788Z
- Nextflow version: 25.12.0-edge
- Summary: 12 errors, 77 warnings

## :x: Errors

- Error: `nextflow.config:388:28`: `manifest` is not defined

  ```nextflow
  \033[0;35m  nf-core/drop ${manifest.version}\033[0m
                             ^^^^^^^^
  ```

- Error: `nextflow.config:391:26`: `manifest` is not defined

  ```nextflow
          afterText = """${manifest.doi ? "\n* The pipeline\n" : ""}${manifest.doi.tokenize(",").collect { "    https://doi.org/${it.trim().replace('https://doi.org/','')}"}.join("\n")}${manifest.doi ? "\n" : ""}
                           ^^^^^^^^
  ```

- Error: `nextflow.config:391:69`: `manifest` is not defined

  ```nextflow
          afterText = """${manifest.doi ? "\n* The pipeline\n" : ""}${manifest.doi.tokenize(",").collect { "    https://doi.org/${it.trim().replace('https://doi.org/','')}"}.join("\n")}${manifest.doi ? "\n" : ""}
                                                                      ^^^^^^^^
  ```

- Error: `nextflow.config:391:186`: `manifest` is not defined

  ```nextflow
          afterText = """${manifest.doi ? "\n* The pipeline\n" : ""}${manifest.doi.tokenize(",").collect { "    https://doi.org/${it.trim().replace('https://doi.org/','')}"}.join("\n")}${manifest.doi ? "\n" : ""}
                                                                                                                                                                                           ^^^^^^^^
  ```

- Error: `nextflow.config:400:22`: `validation` is not defined

  ```nextflow
          beforeText = validation.help.beforeText
                       ^^^^^^^^^^
  ```

- Error: `nextflow.config:401:21`: `validation` is not defined

  ```nextflow
          afterText = validation.help.afterText
                      ^^^^^^^^^^
  ```

- Error: `subworkflows/local/aberrantexpression/main.nf:270:29`: `_` is not allowed as an identifier because it is reserved for future use

  ```nextflow
          .collectFile { tag, _ ->
                              ^
  ```

- Error: `subworkflows/local/aberrantexpression/main.nf:320:29`: `_` is not allowed as an identifier because it is reserved for future use

  ```nextflow
          .collectFile { tag, _ ->
                              ^
  ```

- Error: `subworkflows/local/aberrantsplicing/main.nf:447:29`: `_` is not allowed as an identifier because it is reserved for future use

  ```nextflow
          .collectFile { tag, _ ->
                              ^
  ```

- Error: `subworkflows/local/aberrantsplicing/main.nf:492:29`: `_` is not allowed as an identifier because it is reserved for future use

  ```nextflow
          .collectFile { tag, _ ->
                              ^
  ```

- Error: `subworkflows/local/mae/main.nf:192:29`: `_` is not allowed as an identifier because it is reserved for future use

  ```nextflow
          .collectFile { tag, _ ->
                              ^
  ```

- Error: `subworkflows/local/mae/main.nf:236:29`: `_` is not allowed as an identifier because it is reserved for future use

  ```nextflow
          .collectFile { tag, _ ->
                              ^
  ```

## :warning: Warnings

- Warning: `main.nf:68:42`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      def ucsc_fasta = params.ucsc_fasta ? Channel.value([[id: 'ucsc'], file(params.ucsc_fasta)]) : Channel.of([[id:'ucsc'], []])
                                           ^^^^^^^
  ```

- Warning: `main.nf:68:99`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      def ucsc_fasta = params.ucsc_fasta ? Channel.value([[id: 'ucsc'], file(params.ucsc_fasta)]) : Channel.of([[id:'ucsc'], []])
                                                                                                    ^^^^^^^
  ```

- Warning: `main.nf:69:38`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      def ucsc_fai = params.ucsc_fai ? Channel.value([[id: 'ucsc'], file(params.ucsc_fai)]) : Channel.of([[id:'ucsc'], []])
                                       ^^^^^^^
  ```

- Warning: `main.nf:69:93`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      def ucsc_fai = params.ucsc_fai ? Channel.value([[id: 'ucsc'], file(params.ucsc_fai)]) : Channel.of([[id:'ucsc'], []])
                                                                                              ^^^^^^^
  ```

- Warning: `main.nf:70:42`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      def ncbi_fasta = params.ncbi_fasta ? Channel.value([[id: 'ncbi'], file(params.ncbi_fasta)]) : Channel.of([[id:'ncbi'], []])
                                           ^^^^^^^
  ```

- Warning: `main.nf:70:99`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      def ncbi_fasta = params.ncbi_fasta ? Channel.value([[id: 'ncbi'], file(params.ncbi_fasta)]) : Channel.of([[id:'ncbi'], []])
                                                                                                    ^^^^^^^
  ```

- Warning: `main.nf:71:38`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      def ncbi_fai = params.ncbi_fai ? Channel.value([[id: 'ncbi'], file(params.ncbi_fai)]) : Channel.of([[id:'ncbi'], []])
                                       ^^^^^^^
  ```

- Warning: `main.nf:71:93`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      def ncbi_fai = params.ncbi_fai ? Channel.value([[id: 'ncbi'], file(params.ncbi_fai)]) : Channel.of([[id:'ncbi'], []])
                                                                                              ^^^^^^^
  ```

- Warning: `main.nf:74:9`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
          Channel.value([[id: 'qc_vcf'], file(params.mae_qc_vcf), params.mae_qc_vcf_tbi ? file(params.mae_qc_vcf_tbi) : []]) :
          ^^^^^^^
  ```

- Warning: `main.nf:77:21`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      def ucsc_dict = Channel.of([[id:'ucsc'], []])
                      ^^^^^^^
  ```

- Warning: `main.nf:79:21`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
          ucsc_dict = Channel.value([[id: 'ucsc'], file(params.ucsc_dict)])
                      ^^^^^^^
  ```

- Warning: `main.nf:87:21`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      def ncbi_dict = Channel.of([[id:'ncbi'], []])
                      ^^^^^^^
  ```

- Warning: `main.nf:89:21`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
          ncbi_dict = Channel.value([[id: 'ncbi'], file(params.ncbi_dict)])
                      ^^^^^^^
  ```

- Warning: `main.nf:97:28`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      def samplesheet_file = Channel.value([[id: 'samplesheet'], file(params.input)])
                             ^^^^^^^
  ```

- Warning: `main.nf:99:38`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      def hpo_file = params.hpo_file ? Channel.value([[id: 'hpo'], file(params.hpo_file)]) : [[:], []]
                                       ^^^^^^^
  ```

- Warning: `main.nf:102:54`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      def ae_genes_to_test = params.ae_genes_to_test ? Channel.value([[id: 'genes_to_test'], file(params.ae_genes_to_test)]) : [[:], []]
                                                       ^^^^^^^
  ```

- Warning: `main.nf:105:54`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      def as_genes_to_test = params.as_genes_to_test ? Channel.value([[id: 'genes_to_test'], file(params.as_genes_to_test)]) : [[:], []]
                                                       ^^^^^^^
  ```

- Warning: `modules/local/fraser/summary/main.nf:33:9`: Variable was declared but not used

  ```nextflow
      def prefix = task.ext.prefix ?: "${meta.id}"
          ^^^^^^
  ```

- Warning: `modules/local/splicecounts/summary/main.nf:31:9`: Variable was declared but not used

  ```nextflow
      def prefix = task.ext.prefix ?: "${meta.id}"
          ^^^^^^
  ```

- Warning: `nextflow.config:391:129`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          afterText = """${manifest.doi ? "\n* The pipeline\n" : ""}${manifest.doi.tokenize(",").collect { "    https://doi.org/${it.trim().replace('https://doi.org/','')}"}.join("\n")}${manifest.doi ? "\n" : ""}
                                                                                                                                  ^^
  ```

- Warning: `subworkflows/local/aberrantexpression/main.nf:28:23`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      def ch_versions = Channel.empty()
                        ^^^^^^^
  ```

- Warning: `subworkflows/local/aberrantexpression/main.nf:30:29`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      def inputs_to_analyse = Channel.empty()
                              ^^^^^^^
  ```

- Warning: `subworkflows/local/aberrantexpression/main.nf:263:43`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          def files = tup.drop(1).findAll { it instanceof Path } // drop meta and null
                                            ^^
  ```

- Warning: `subworkflows/local/aberrantexpression/main.nf:289:36`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          ch_genecounts_bundle.map { it[0] },
                                     ^^
  ```

- Warning: `subworkflows/local/aberrantexpression/main.nf:290:9`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
          Channel.fromPath("$projectDir/assets/multiqc_configs/multiqc_genecounts_config.yml", checkIfExists: true).collect(),
          ^^^^^^^
  ```

- Warning: `subworkflows/local/aberrantexpression/main.nf:291:36`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          ch_genecounts_bundle.map { it[1] },
                                     ^^
  ```

- Warning: `subworkflows/local/aberrantexpression/main.nf:313:43`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          def files = tup.drop(1).findAll { it instanceof Path } // drop meta and null
                                            ^^
  ```

- Warning: `subworkflows/local/aberrantexpression/main.nf:339:34`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          ch_outrider_bundle.map { it[0] },
                                   ^^
  ```

- Warning: `subworkflows/local/aberrantexpression/main.nf:340:9`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
          Channel.fromPath("$projectDir/assets/multiqc_configs/multiqc_outrider_config.yml", checkIfExists: true).collect(),
          ^^^^^^^
  ```

- Warning: `subworkflows/local/aberrantexpression/main.nf:341:34`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          ch_outrider_bundle.map { it[1] },
                                   ^^
  ```

- Warning: `subworkflows/local/aberrantsplicing/main.nf:33:23`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      def ch_versions = Channel.empty()
                        ^^^^^^^
  ```

- Warning: `subworkflows/local/aberrantsplicing/main.nf:35:40`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      def inputs_to_analyse_unfiltered = Channel.empty()
                                         ^^^^^^^
  ```

- Warning: `subworkflows/local/aberrantsplicing/main.nf:282:60`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
              def count_dirs = splice_counts_group.collect { it.file }.unique() // Prevent the same directory from being used multiple times
                                                             ^^
  ```

- Warning: `subworkflows/local/aberrantsplicing/main.nf:283:59`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
              def count_ids = splice_counts_group.collect { it.id }
                                                            ^^
  ```

- Warning: `subworkflows/local/aberrantsplicing/main.nf:290:9`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
          Channel.value([[id:'samplesheet'], samplesheet]),
          ^^^^^^^
  ```

- Warning: `subworkflows/local/aberrantsplicing/main.nf:402:9`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
          Channel.value([[id:'samplesheet'], samplesheet]),
          ^^^^^^^
  ```

- Warning: `subworkflows/local/aberrantsplicing/main.nf:440:43`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          def files = tup.drop(1).findAll { it instanceof Path } // drop meta and null
                                            ^^
  ```

- Warning: `subworkflows/local/aberrantsplicing/main.nf:466:38`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          ch_splicecounts_bundle.map { it[0] },
                                       ^^
  ```

- Warning: `subworkflows/local/aberrantsplicing/main.nf:467:9`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
          Channel.fromPath("$projectDir/assets/multiqc_configs/multiqc_splicecounts_config.yml", checkIfExists: true).collect(),
          ^^^^^^^
  ```

- Warning: `subworkflows/local/aberrantsplicing/main.nf:468:38`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          ch_splicecounts_bundle.map { it[1] },
                                       ^^
  ```

- Warning: `subworkflows/local/aberrantsplicing/main.nf:485:116`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          def files = ([overview, aberrant_png, total_outliers, results_tsv] + q_list + bc_list).flatten().findAll { it instanceof Path } // drop meta and null
                                                                                                                     ^^
  ```

- Warning: `subworkflows/local/aberrantsplicing/main.nf:511:32`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          ch_fraser_bundle.map { it[0] },
                                 ^^
  ```

- Warning: `subworkflows/local/aberrantsplicing/main.nf:512:9`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
          Channel.fromPath("$projectDir/assets/multiqc_configs/multiqc_fraser_config.yml", checkIfExists: true).collect(),
          ^^^^^^^
  ```

- Warning: `subworkflows/local/aberrantsplicing/main.nf:513:32`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          ch_fraser_bundle.map { it[1] },
                                 ^^
  ```

- Warning: `subworkflows/local/bam_stats_idxstats_merge/main.nf:12:40`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
      def ucsc_chr = ucsc2ncbi.collect { it[0] }
                                         ^^
  ```

- Warning: `subworkflows/local/bam_stats_idxstats_merge/main.nf:13:40`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
      def ncbi_chr = ucsc2ncbi.collect { it[1] }
                                         ^^
  ```

- Warning: `subworkflows/local/bam_stats_idxstats_merge/main.nf:14:23`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      def ch_versions = Channel.empty()
                        ^^^^^^^
  ```

- Warning: `subworkflows/local/mae/main.nf:27:5`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
      include_qc_groups   // list         : A list of groups to include in the QC steps of the mono allelic expression analysis
      ^^^^^^^^^^^^^^^^^
  ```

- Warning: `subworkflows/local/mae/main.nf:32:23`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      def ch_versions = Channel.empty()
                        ^^^^^^^
  ```

- Warning: `subworkflows/local/mae/main.nf:44:30`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      def ch_filtered_inputs = Channel.empty()
                               ^^^^^^^
  ```

- Warning: `subworkflows/local/mae/main.nf:167:59`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          .view {println "[DEBUG ch_dnarnamatrixplot_input] $it"}
                                                            ^^
  ```

- Warning: `subworkflows/local/mae/main.nf:185:43`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          def files = tup.drop(1).findAll { it instanceof Path } // drop meta and null
                                            ^^
  ```

- Warning: `subworkflows/local/mae/main.nf:211:29`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          ch_mae_bundle.map { it[0] },
                              ^^
  ```

- Warning: `subworkflows/local/mae/main.nf:212:9`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
          Channel.fromPath("$projectDir/assets/multiqc_configs/multiqc_mae_config.yml", checkIfExists: true).collect(),
          ^^^^^^^
  ```

- Warning: `subworkflows/local/mae/main.nf:213:29`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          ch_mae_bundle.map { it[1] },
                              ^^
  ```

- Warning: `subworkflows/local/mae/main.nf:229:43`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          def files = tup.drop(1).findAll { it instanceof Path } // drop meta and null
                                            ^^
  ```

- Warning: `subworkflows/local/mae/main.nf:255:31`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          ch_maeqc_bundle.map { it[0] },
                                ^^
  ```

- Warning: `subworkflows/local/mae/main.nf:256:9`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
          Channel.fromPath("$projectDir/assets/multiqc_configs/multiqc_maeqc_config.yml", checkIfExists: true).collect(),
          ^^^^^^^
  ```

- Warning: `subworkflows/local/mae/main.nf:257:31`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          ch_maeqc_bundle.map { it[1] },
                                ^^
  ```

- Warning: `subworkflows/local/utils_nfcore_drop_pipeline/main.nf:37:19`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_versions = Channel.empty()
                    ^^^^^^^
  ```

- Warning: `subworkflows/local/utils_nfcore_drop_pipeline/main.nf:78:63`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
      def all_gene_annotations = gene_annotation_list.collect { it[0].id }.sort().toSet()
                                                                ^^
  ```

- Warning: `subworkflows/local/utils_nfcore_drop_pipeline/main.nf:81:11`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
          ? Channel.fromList(gene_annotation_list)
            ^^^^^^^
  ```

- Warning: `subworkflows/local/utils_nfcore_drop_pipeline/main.nf:82:11`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
          : Channel.empty()
            ^^^^^^^
  ```

- Warning: `subworkflows/local/utils_nfcore_drop_pipeline/main.nf:129:26`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      def ch_samplesheet = Channel.fromList(samplesheet_list)
                           ^^^^^^^
  ```

- Warning: `subworkflows/local/utils_nfcore_drop_pipeline/main.nf:336:37`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
      def offending = flags.findAll { k, v -> v.hasNo && v.hasStranded }.keySet().sort()
                                      ^
  ```

- Warning: `subworkflows/nf-core/utils_nfcore_pipeline/main.nf:101:98`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      return ch_versions.unique().map { version -> processVersionsFromYAML(version) }.unique().mix(Channel.of(workflowVersionToYAML()))
                                                                                                   ^^^^^^^
  ```

- Warning: `workflows/drop.nf:62:19`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_versions = Channel.empty()
                    ^^^^^^^
  ```

- Warning: `workflows/drop.nf:63:24`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_multiqc_files = Channel.empty()
                         ^^^^^^^
  ```

- Warning: `workflows/drop.nf:213:13`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
              Channel.value(file("${projectDir}/assets/chr_NCBI_UCSC.txt", checkIfExists: true)),
              ^^^^^^^
  ```

- Warning: `workflows/drop.nf:214:13`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
              Channel.value(file("${projectDir}/assets/chr_UCSC_NCBI.txt", checkIfExists: true))
              ^^^^^^^
  ```

- Warning: `workflows/drop.nf:235:32`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_multiqc_config        = Channel.fromPath(
                                 ^^^^^^^
  ```

- Warning: `workflows/drop.nf:238:9`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
          Channel.fromPath(params.multiqc_config, checkIfExists: true) :
          ^^^^^^^
  ```

- Warning: `workflows/drop.nf:239:9`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
          Channel.empty()
          ^^^^^^^
  ```

- Warning: `workflows/drop.nf:241:9`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
          Channel.fromPath(params.multiqc_logo, checkIfExists: true) :
          ^^^^^^^
  ```

- Warning: `workflows/drop.nf:242:9`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
          Channel.empty()
          ^^^^^^^
  ```

- Warning: `workflows/drop.nf:246:27`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_workflow_summary = Channel.value(paramsSummaryMultiqc(summary_params))
                            ^^^^^^^
  ```

- Warning: `workflows/drop.nf:252:45`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_methods_description                = Channel.value(
                                              ^^^^^^^
  ```
