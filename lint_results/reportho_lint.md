# Nextflow lint results

- Generated: 2026-01-14T09:23:52.015205965Z
- Nextflow version: 25.12.0-edge
- Summary: 2 errors, 90 warnings

## :x: Errors

- Error: `conf/test.config:26:14`: `pipelines_testdata_base_path` is not defined

  ```nextflow
      input  = pipelines_testdata_base_path + 'reportho/testdata/samplesheet/samplesheet.csv'
               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  ```

- Error: `conf/test_fasta.config:27:14`: `pipelines_testdata_base_path` is not defined

  ```nextflow
      input  = pipelines_testdata_base_path + 'reportho/testdata/samplesheet/samplesheet_fasta.csv'
               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  ```

## :warning: Warnings

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

- Warning: `modules/nf-core/diamond/cluster/main.nf:41:9`: Variable was declared but not used

  ```nextflow
      def args = task.ext.args ?: ''
          ^^^^
  ```

- Warning: `modules/nf-core/gawk/main.nf:25:51`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
      suffix = task.ext.suffix ?: "${input.collect{ it.getExtension()}.get(0)}" // use the first extension of the input files
                                                    ^^
  ```

- Warning: `modules/nf-core/gawk/main.nf:28:32`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
      lst_gz    = input.collect{ it.getExtension().endsWith("gz") }
                                 ^^
  ```

- Warning: `subworkflows/local/get_orthologs.nf:27:23`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_versions     = Channel.empty()
                        ^^^^^^^
  ```

- Warning: `subworkflows/local/get_orthologs.nf:28:23`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_orthogroups  = Channel.empty()
                        ^^^^^^^
  ```

- Warning: `subworkflows/local/get_orthologs.nf:34:16`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          return it
                 ^^
  ```

- Warning: `subworkflows/local/get_orthologs.nf:160:34`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
      id          = ch_query.map { it[1] }
                                   ^^
  ```

- Warning: `subworkflows/local/get_orthologs.nf:161:34`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
      taxid       = ch_query.map { it[2] }
                                   ^^
  ```

- Warning: `subworkflows/local/get_orthologs.nf:162:34`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
      exact       = ch_query.map { it[3] }
                                   ^^
  ```

- Warning: `subworkflows/local/get_sequences.nf:17:19`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_versions = Channel.empty()
                    ^^^^^^^
  ```

- Warning: `subworkflows/local/get_sequences.nf:31:17`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_fasta  = Channel.empty()
                  ^^^^^^^
  ```

- Warning: `subworkflows/local/get_sequences.nf:32:17`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_hits   = Channel.empty()
                  ^^^^^^^
  ```

- Warning: `subworkflows/local/get_sequences.nf:33:17`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_misses = Channel.empty()
                  ^^^^^^^
  ```

- Warning: `subworkflows/local/merge_ids.nf:15:19`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_versions = Channel.empty()
                    ^^^^^^^
  ```

- Warning: `subworkflows/local/merge_ids.nf:16:22`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_id_clusters = Channel.empty()
                       ^^^^^^^
  ```

- Warning: `subworkflows/local/merge_ids.nf:32:27`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
              single_entry: it[2] == 1
                            ^^
  ```

- Warning: `subworkflows/local/merge_ids.nf:33:31`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
              multiple_entries: it[2] > 1
                                ^^
  ```

- Warning: `subworkflows/local/merge_ids.nf:40:32`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
              .map { meta, file, count -> [ meta, file ] }
                                 ^^^^^
  ```

- Warning: `subworkflows/local/merge_ids.nf:50:32`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
              .map { meta, file, count -> [ meta, file ] }
                                 ^^^^^
  ```

- Warning: `subworkflows/local/report.nf:7:5`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
      use_centroid
      ^^^^^^^^^^^^
  ```

- Warning: `subworkflows/local/report.nf:8:5`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
      min_score
      ^^^^^^^^^
  ```

- Warning: `subworkflows/local/report.nf:22:20`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_versions  = Channel.empty()
                     ^^^^^^^
  ```

- Warning: `subworkflows/local/report.nf:23:5`: Variable was declared but not used

  ```nextflow
      ch_fasta     = ch_seqinfo.map { [it[0], []] }
      ^^^^^^^^
  ```

- Warning: `subworkflows/local/report.nf:23:38`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
      ch_fasta     = ch_seqinfo.map { [it[0], []] }
                                       ^^
  ```

- Warning: `subworkflows/local/report.nf:26:27`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          ch_seqinfo.map { [it[0], it[3]] },
                            ^^
  ```

- Warning: `subworkflows/local/report.nf:26:34`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          ch_seqinfo.map { [it[0], it[3]] },
                                   ^^
  ```

- Warning: `subworkflows/local/score_orthologs.nf:23:19`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_versions = Channel.empty()
                    ^^^^^^^
  ```

- Warning: `subworkflows/local/score_orthologs.nf:33:34`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          .map { id, score, query, taxid, exact -> [id, score, query] }
                                   ^^^^^
  ```

- Warning: `subworkflows/local/score_orthologs.nf:33:41`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          .map { id, score, query, taxid, exact -> [id, score, query] }
                                          ^^^^^
  ```

- Warning: `subworkflows/local/score_orthologs.nf:45:39`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
      ch_supportsplot = ch_query.map { [it[0], []]}
                                        ^^
  ```

- Warning: `subworkflows/local/score_orthologs.nf:46:39`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
      ch_vennplot     = ch_query.map { [it[0], []]}
                                        ^^
  ```

- Warning: `subworkflows/local/score_orthologs.nf:47:39`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
      ch_jaccardplot  = ch_query.map { [it[0], []]}
                                        ^^
  ```

- Warning: `subworkflows/local/score_orthologs.nf:70:20`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          .collect { it[1] }
                     ^^
  ```

- Warning: `subworkflows/local/score_orthologs.nf:71:30`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          .map { [[id: "all"], it] }
                               ^^
  ```

- Warning: `subworkflows/local/score_orthologs.nf:81:27`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_merge_table      = Channel.empty()
                            ^^^^^^^
  ```

- Warning: `subworkflows/local/score_orthologs.nf:82:27`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_aggregated_merge = Channel.empty()
                            ^^^^^^^
  ```

- Warning: `subworkflows/local/score_orthologs.nf:94:24`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
              .collect { it[1] }
                         ^^
  ```

- Warning: `subworkflows/local/score_orthologs.nf:95:34`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
              .map { [[id: "all"], it] }
                                   ^^
  ```

- Warning: `subworkflows/local/score_orthologs.nf:123:20`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          .collect { it[1] }
                     ^^
  ```

- Warning: `subworkflows/local/score_orthologs.nf:124:30`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          .map { [[id: "all"], it] }
                               ^^
  ```

- Warning: `subworkflows/local/utils_nfcore_reportho_pipeline/main.nf:32:5`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
      monochrome_logs   // boolean: Do not use coloured log outputs
      ^^^^^^^^^^^^^^^
  ```

- Warning: `subworkflows/local/utils_nfcore_reportho_pipeline/main.nf:35:5`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
      input             //  string: Path to input samplesheet
      ^^^^^
  ```

- Warning: `subworkflows/local/utils_nfcore_reportho_pipeline/main.nf:42:19`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_versions = Channel.empty()
                    ^^^^^^^
  ```

- Warning: `subworkflows/local/utils_nfcore_reportho_pipeline/main.nf:67:144`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
      after_text = """${workflow.manifest.doi ? "\n* The pipeline\n" : ""}${workflow.manifest.doi.tokenize(",").collect { "    https://doi.org/${it.trim().replace('https://doi.org/','')}"}.join("\n")}${workflow.manifest.doi ? "\n" : ""}
                                                                                                                                                 ^^
  ```

- Warning: `subworkflows/local/utils_nfcore_reportho_pipeline/main.nf:104:5`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      Channel
      ^^^^^^^
  ```

- Warning: `subworkflows/nf-core/utils_nfcore_pipeline/main.nf:101:98`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      return ch_versions.unique().map { version -> processVersionsFromYAML(version) }.unique().mix(Channel.of(workflowVersionToYAML()))
                                                                                                   ^^^^^^^
  ```

- Warning: `workflows/reportho.nf:32:24`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_versions      = Channel.empty()
                         ^^^^^^^
  ```

- Warning: `workflows/reportho.nf:33:24`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_multiqc_files = Channel.empty()
                         ^^^^^^^
  ```

- Warning: `workflows/reportho.nf:34:52`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
      ch_fasta_query   = ch_samplesheet_query.map { [it[0], []] }.mix(ch_samplesheet_fasta.map { [it[0], file(it[1])] })
                                                     ^^
  ```

- Warning: `workflows/reportho.nf:34:97`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
      ch_fasta_query   = ch_samplesheet_query.map { [it[0], []] }.mix(ch_samplesheet_fasta.map { [it[0], file(it[1])] })
                                                                                                  ^^
  ```

- Warning: `workflows/reportho.nf:34:109`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
      ch_fasta_query   = ch_samplesheet_query.map { [it[0], []] }.mix(ch_samplesheet_fasta.map { [it[0], file(it[1])] })
                                                                                                              ^^
  ```

- Warning: `workflows/reportho.nf:36:42`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_oma_groups    = params.oma_path ? Channel.value(file(params.oma_path)) : Channel.empty()
                                           ^^^^^^^
  ```

- Warning: `workflows/reportho.nf:36:81`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_oma_groups    = params.oma_path ? Channel.value(file(params.oma_path)) : Channel.empty()
                                                                                  ^^^^^^^
  ```

- Warning: `workflows/reportho.nf:37:50`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_oma_uniprot   = params.oma_uniprot_path ? Channel.value(file(params.oma_uniprot_path)) : Channel.empty()
                                                   ^^^^^^^
  ```

- Warning: `workflows/reportho.nf:37:97`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_oma_uniprot   = params.oma_uniprot_path ? Channel.value(file(params.oma_uniprot_path)) : Channel.empty()
                                                                                                  ^^^^^^^
  ```

- Warning: `workflows/reportho.nf:38:50`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_oma_ensembl   = params.oma_ensembl_path ? Channel.value(file(params.oma_ensembl_path)) : Channel.empty()
                                                   ^^^^^^^
  ```

- Warning: `workflows/reportho.nf:38:97`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_oma_ensembl   = params.oma_ensembl_path ? Channel.value(file(params.oma_ensembl_path)) : Channel.empty()
                                                                                                  ^^^^^^^
  ```

- Warning: `workflows/reportho.nf:39:49`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_oma_refseq    = params.oma_refseq_path ? Channel.value(file(params.oma_refseq_path)) : Channel.empty()
                                                  ^^^^^^^
  ```

- Warning: `workflows/reportho.nf:39:95`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_oma_refseq    = params.oma_refseq_path ? Channel.value(file(params.oma_refseq_path)) : Channel.empty()
                                                                                                ^^^^^^^
  ```

- Warning: `workflows/reportho.nf:40:46`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_panther       = params.panther_path ? Channel.value(file(params.panther_path)) : Channel.empty()
                                               ^^^^^^^
  ```

- Warning: `workflows/reportho.nf:40:89`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_panther       = params.panther_path ? Channel.value(file(params.panther_path)) : Channel.empty()
                                                                                          ^^^^^^^
  ```

- Warning: `workflows/reportho.nf:41:45`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_eggnog        = params.eggnog_path ? Channel.value(file(params.eggnog_path)) : Channel.empty()
                                              ^^^^^^^
  ```

- Warning: `workflows/reportho.nf:41:87`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_eggnog        = params.eggnog_path ? Channel.value(file(params.eggnog_path)) : Channel.empty()
                                                                                        ^^^^^^^
  ```

- Warning: `workflows/reportho.nf:42:51`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_eggnog_idmap  = params.eggnog_idmap_path ? Channel.value(file(params.eggnog_idmap_path)) : Channel.empty()
                                                    ^^^^^^^
  ```

- Warning: `workflows/reportho.nf:42:99`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_eggnog_idmap  = params.eggnog_idmap_path ? Channel.value(file(params.eggnog_idmap_path)) : Channel.empty()
                                                                                                    ^^^^^^^
  ```

- Warning: `workflows/reportho.nf:44:52`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
      ch_seqhits       = ch_samplesheet_query.map { [it[0], []] }
                                                     ^^
  ```

- Warning: `workflows/reportho.nf:45:52`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
      ch_seqmisses     = ch_samplesheet_query.map { [it[0], []] }
                                                     ^^
  ```

- Warning: `workflows/reportho.nf:61:43`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
      ch_seqs = ch_samplesheet_query.map { [it[0], []] }
                                            ^^
  ```

- Warning: `workflows/reportho.nf:77:41`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
      ch_id_map   = ch_fasta_query.map { [it[0], []] }
                                          ^^
  ```

- Warning: `workflows/reportho.nf:78:41`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
      ch_clusters = ch_fasta_query.map { [it[0], []] }
                                          ^^
  ```

- Warning: `workflows/reportho.nf:103:5`: Variable was declared but not used

  ```nextflow
      ch_samplesheet = ch_samplesheet_query.mix (ch_samplesheet_fasta)
      ^^^^^^^^^^^^^^
  ```

- Warning: `workflows/reportho.nf:105:87`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
      ch_multiqc_files = ch_multiqc_files.mix(SCORE_ORTHOLOGS.out.aggregated_stats.map {it[1]})
                                                                                        ^^
  ```

- Warning: `workflows/reportho.nf:106:86`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
      ch_multiqc_files = ch_multiqc_files.mix(SCORE_ORTHOLOGS.out.aggregated_hits.map {it[1]})
                                                                                       ^^
  ```

- Warning: `workflows/reportho.nf:107:87`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
      ch_multiqc_files = ch_multiqc_files.mix(SCORE_ORTHOLOGS.out.aggregated_merge.map {it[1]})
                                                                                        ^^
  ```

- Warning: `workflows/reportho.nf:123:54`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
              SCORE_ORTHOLOGS.out.supports_plot.map { [it[0], it[2]]},
                                                       ^^
  ```

- Warning: `workflows/reportho.nf:123:61`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
              SCORE_ORTHOLOGS.out.supports_plot.map { [it[0], it[2]]},
                                                              ^^
  ```

- Warning: `workflows/reportho.nf:124:50`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
              SCORE_ORTHOLOGS.out.venn_plot.map { [it[0], it[2]]},
                                                   ^^
  ```

- Warning: `workflows/reportho.nf:124:57`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
              SCORE_ORTHOLOGS.out.venn_plot.map { [it[0], it[2]]},
                                                          ^^
  ```

- Warning: `workflows/reportho.nf:125:53`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
              SCORE_ORTHOLOGS.out.jaccard_plot.map { [it[0], it[2]]},
                                                      ^^
  ```

- Warning: `workflows/reportho.nf:125:60`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
              SCORE_ORTHOLOGS.out.jaccard_plot.map { [it[0], it[2]]},
                                                             ^^
  ```

- Warning: `workflows/reportho.nf:151:25`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_multiqc_report = Channel.empty()
                          ^^^^^^^
  ```

- Warning: `workflows/reportho.nf:153:36`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
          ch_multiqc_config        = Channel.fromPath(
                                     ^^^^^^^
  ```

- Warning: `workflows/reportho.nf:157:13`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
              Channel.fromPath(params.multiqc_config, checkIfExists: true) :
              ^^^^^^^
  ```

- Warning: `workflows/reportho.nf:158:13`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
              Channel.empty()
              ^^^^^^^
  ```

- Warning: `workflows/reportho.nf:161:13`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
              Channel.fromPath(params.multiqc_logo, checkIfExists: true) :
              ^^^^^^^
  ```

- Warning: `workflows/reportho.nf:162:13`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
              Channel.empty()
              ^^^^^^^
  ```

- Warning: `workflows/reportho.nf:166:31`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
          ch_workflow_summary = Channel.value(paramsSummaryMultiqc(summary_params))
                                ^^^^^^^
  ```

- Warning: `workflows/reportho.nf:172:49`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
          ch_methods_description                = Channel.value(
                                                  ^^^^^^^
  ```
