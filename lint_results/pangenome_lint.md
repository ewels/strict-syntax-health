# Nextflow lint results

- Generated: 2026-01-14T09:21:55.712628929Z
- Nextflow version: 25.12.0-edge
- Summary: 14 errors, 63 warnings

## :x: Errors

- Error: `conf/modules.config:14:35`: Unexpected input: '('

  ```nextflow
  def generate_wfmash_sparse_map_cmd() {
                                    ^
  ```

- Error: `nextflow.config:396:33`: `manifest` is not defined

  ```nextflow
  \033[0;35m  nf-core/pangenome ${manifest.version}\033[0m
                                  ^^^^^^^^
  ```

- Error: `nextflow.config:399:26`: `manifest` is not defined

  ```nextflow
          afterText = """${manifest.doi ? "\n* The pipeline\n" : ""}${manifest.doi.tokenize(",").collect { "    https://doi.org/${it.trim().replace('https://doi.org/','')}"}.join("\n")}${manifest.doi ? "\n" : ""}
                           ^^^^^^^^
  ```

- Error: `nextflow.config:399:69`: `manifest` is not defined

  ```nextflow
          afterText = """${manifest.doi ? "\n* The pipeline\n" : ""}${manifest.doi.tokenize(",").collect { "    https://doi.org/${it.trim().replace('https://doi.org/','')}"}.join("\n")}${manifest.doi ? "\n" : ""}
                                                                      ^^^^^^^^
  ```

- Error: `nextflow.config:399:186`: `manifest` is not defined

  ```nextflow
          afterText = """${manifest.doi ? "\n* The pipeline\n" : ""}${manifest.doi.tokenize(",").collect { "    https://doi.org/${it.trim().replace('https://doi.org/','')}"}.join("\n")}${manifest.doi ? "\n" : ""}
                                                                                                                                                                                           ^^^^^^^^
  ```

- Error: `nextflow.config:408:22`: `validation` is not defined

  ```nextflow
          beforeText = validation.help.beforeText
                       ^^^^^^^^^^
  ```

- Error: `nextflow.config:409:21`: `validation` is not defined

  ```nextflow
          afterText = validation.help.afterText
                      ^^^^^^^^^^
  ```

- Error: `subworkflows/local/community.nf:26:37`: `fasta` is already declared

  ```nextflow
      ch_wfmash_map = fasta.map{meta, fasta -> [ meta, fasta, [] ]}
                                      ^^^^^
  ```

- Error: `subworkflows/local/community.nf:40:55`: `fasta` is already declared

  ```nextflow
      ch_txt_communities = ch_txt_communities.map{meta, fasta, community -> [ [ id: community.baseName.split("//.")[-1] ], fasta, community ]}
                                                        ^^^^^
  ```

- Error: `subworkflows/local/pggb.nf:38:51`: `fasta` is already declared

  ```nextflow
              ch_wfmash_map_align = fasta.map{meta, fasta -> [ meta, fasta, []]}
                                                    ^^^^^
  ```

- Error: `subworkflows/local/pggb.nf:45:45`: `fasta` is already declared

  ```nextflow
              ch_wfmash_map = fasta.map{meta, fasta -> [ meta, fasta, [] ]}
                                              ^^^^^
  ```

- Error: `subworkflows/local/pggb.nf:67:55`: `fasta` is already declared

  ```nextflow
                  ch_wfmash_map_align = fasta.map{meta, fasta -> [ meta, fasta, [] ]}
                                                        ^^^^^
  ```

- Error: `subworkflows/local/pggb.nf:77:49`: `fasta` is already declared

  ```nextflow
                  ch_wfmash_map = fasta.map{meta, fasta -> [ meta, fasta, [] ]}
                                                  ^^^^^
  ```

- Error: `subworkflows/local/utils_nfcore_pangenome_pipeline/main.nf:5:1`: Groovy `import` declarations are not supported -- use fully-qualified name inline instead

  ```nextflow
  import groovy.json.JsonSlurper
  ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  ```

## :warning: Warnings

- Warning: `main.nf:29:19`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_versions = Channel.empty()
                    ^^^^^^^
  ```

- Warning: `modules/local/extract_communities/main.nf:21:9`: Variable was declared but not used

  ```nextflow
      def args = task.ext.args ?: ''
          ^^^^
  ```

- Warning: `modules/local/paf2net/main.nf:22:9`: Variable was declared but not used

  ```nextflow
      def prefix = task.ext.prefix ?: "${meta.id}"
          ^^^^^^
  ```

- Warning: `modules/local/split_approx_mappings_in_chunks/main.nf:22:9`: Variable was declared but not used

  ```nextflow
      def prefix = task.ext.prefix ?: "${meta.id}"
          ^^^^^^
  ```

- Warning: `modules/local/vg_deconstruct/main.nf:46:9`: Variable was declared but not used

  ```nextflow
      def args = task.ext.args ?: ''
          ^^^^
  ```

- Warning: `modules/local/vg_deconstruct/main.nf:47:9`: Variable was declared but not used

  ```nextflow
      def prefix = task.ext.prefix ?: "${meta.id}"
          ^^^^^^
  ```

- Warning: `nextflow.config:399:129`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          afterText = """${manifest.doi ? "\n* The pipeline\n" : ""}${manifest.doi.tokenize(",").collect { "    https://doi.org/${it.trim().replace('https://doi.org/','')}"}.join("\n")}${manifest.doi ? "\n" : ""}
                                                                                                                                  ^^
  ```

- Warning: `subworkflows/local/community.nf:21:19`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_versions = Channel.empty() // we collect all versions here
                    ^^^^^^^
  ```

- Warning: `subworkflows/local/community.nf:22:5`: Variable was declared but not used

  ```nextflow
      ch_communities = Channel.empty()
      ^^^^^^^^^^^^^^
  ```

- Warning: `subworkflows/local/community.nf:22:22`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_communities = Channel.empty()
                       ^^^^^^^
  ```

- Warning: `subworkflows/local/community.nf:40:49`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
      ch_txt_communities = ch_txt_communities.map{meta, fasta, community -> [ [ id: community.baseName.split("//.")[-1] ], fasta, community ]}
                                                  ^^^^
  ```

- Warning: `subworkflows/local/input_check.nf:14:19`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_versions = Channel.empty() // we collect all versions here
                    ^^^^^^^
  ```

- Warning: `subworkflows/local/input_check.nf:15:16`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_fasta = Channel.empty() // final output channel [ val(meta) , [ fasta ] ]
                 ^^^^^^^
  ```

- Warning: `subworkflows/local/input_check.nf:20:11`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      fai = Channel.empty() // we store the .fai index here [ fai ]
            ^^^^^^^
  ```

- Warning: `subworkflows/local/input_check.nf:21:11`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      gzi = Channel.empty() // we store the .gzi index here [ gzi ]
            ^^^^^^^
  ```

- Warning: `subworkflows/local/input_check.nf:23:18`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      meta_fasta = Channel.empty() // intermediate channel where we build our [ val(meta) , [ fasta ] ]
                   ^^^^^^^
  ```

- Warning: `subworkflows/local/input_check.nf:36:19`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
              fai = Channel.of([ [ id:fasta_file_name ], fai_path ])
                    ^^^^^^^
  ```

- Warning: `subworkflows/local/input_check.nf:37:19`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
              gzi = Channel.of([ [ id:fasta_file_name ], gzi_path ])
                    ^^^^^^^
  ```

- Warning: `subworkflows/local/odgi_qc.nf:25:19`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_versions = Channel.empty() // we collect all versions here
                    ^^^^^^^
  ```

- Warning: `subworkflows/local/odgi_qc.nf:26:19`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_graph_qc = Channel.empty() // we collect all graph quality control PNGs here
                    ^^^^^^^
  ```

- Warning: `subworkflows/local/odgi_qc.nf:71:61`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
              ch_graph_qc = ODGI_STATS.out.yaml.collect().map{seqwish_id, seqwish_qc, gfaffix_id, gfaffix_qc -> [ gfaffix_id, gfaffix_qc, seqwish_qc ]}
                                                              ^^^^^^^^^^
  ```

- Warning: `subworkflows/local/pggb.nf:29:19`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_versions = Channel.empty()  // we collect all versions here
                    ^^^^^^^
  ```

- Warning: `subworkflows/local/pggb.nf:30:19`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_graph_qc = Channel.empty()  // we collect all graph quality control PNGs and graph statistics here
                    ^^^^^^^
  ```

- Warning: `subworkflows/local/pggb.nf:31:20`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_odgi_view = Channel.empty() // we collect the final graph in GFA format here
                     ^^^^^^^
  ```

- Warning: `subworkflows/local/pggb.nf:32:29`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_odgi_build_seqwish = Channel.empty()
                              ^^^^^^^
  ```

- Warning: `subworkflows/local/pggb.nf:33:23`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_sorted_graph = Channel.empty()
                        ^^^^^^^
  ```

- Warning: `subworkflows/local/pggb.nf:62:27`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
              ch_combined = Channel.of([ [ id:file_fasta.getName() ], file(params.seqwish_paf), file_fasta ])
                            ^^^^^^^
  ```

- Warning: `subworkflows/local/pggb.nf:105:42`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          ch_gfaffix = GFAFFIX.out.gfa.map{meta, gfa -> [ [ id: gfa.baseName ], gfa ]}
                                           ^^^^
  ```

- Warning: `subworkflows/local/pggb.nf:106:42`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          ch_seqwish = SEQWISH.out.gfa.map{meta, gfa -> [ [ id: gfa.baseName ], gfa ]}
                                           ^^^^
  ```

- Warning: `subworkflows/local/pggb.nf:115:24`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
              }}.filter{ it != null }
                         ^^
  ```

- Warning: `subworkflows/local/pggb.nf:129:24`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
              }}.filter{ it != null }
                         ^^
  ```

- Warning: `subworkflows/local/utils_nfcore_pangenome_pipeline/main.nf:33:5`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
      monochrome_logs   // boolean: Do not use coloured log outputs
      ^^^^^^^^^^^^^^^
  ```

- Warning: `subworkflows/local/utils_nfcore_pangenome_pipeline/main.nf:132:42`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
      def strandedness_ok = metas.collect{ it.strandedness }.unique().size == 1
                                           ^^
  ```

- Warning: `subworkflows/nf-core/utils_nfcore_pipeline/main.nf:101:98`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      return ch_versions.unique().map { version -> processVersionsFromYAML(version) }.unique().mix(Channel.of(workflowVersionToYAML()))
                                                                                                   ^^^^^^^
  ```

- Warning: `workflows/pangenome.nf:58:19`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_versions = Channel.empty()
                    ^^^^^^^
  ```

- Warning: `workflows/pangenome.nf:59:24`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_multiqc_files = Channel.empty()
                         ^^^^^^^
  ```

- Warning: `workflows/pangenome.nf:60:5`: Variable was declared but not used

  ```nextflow
      multiqc_report = Channel.empty()
      ^^^^^^^^^^^^^^
  ```

- Warning: `workflows/pangenome.nf:60:22`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      multiqc_report = Channel.empty()
                       ^^^^^^^
  ```

- Warning: `workflows/pangenome.nf:69:32`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_multiqc_config        = Channel.fromPath("$projectDir/assets/multiqc_config.yml", checkIfExists: true)
                                 ^^^^^^^
  ```

- Warning: `workflows/pangenome.nf:71:25`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_multiqc_config = Channel.fromPath("$projectDir/assets/multiqc_config.yml", checkIfExists: true)
                          ^^^^^^^
  ```

- Warning: `workflows/pangenome.nf:72:56`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_multiqc_custom_config = params.multiqc_config ? Channel.fromPath(params.multiqc_config, checkIfExists: true) : Channel.empty()
                                                         ^^^^^^^
  ```

- Warning: `workflows/pangenome.nf:72:119`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_multiqc_custom_config = params.multiqc_config ? Channel.fromPath(params.multiqc_config, checkIfExists: true) : Channel.empty()
                                                                                                                        ^^^^^^^
  ```

- Warning: `workflows/pangenome.nf:75:56`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_multiqc_custom_config = params.multiqc_config ? Channel.fromPath(params.multiqc_config) : Channel.empty()
                                                         ^^^^^^^
  ```

- Warning: `workflows/pangenome.nf:75:98`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_multiqc_custom_config = params.multiqc_config ? Channel.fromPath(params.multiqc_config) : Channel.empty()
                                                                                                   ^^^^^^^
  ```

- Warning: `workflows/pangenome.nf:76:56`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_multiqc_logo          = params.multiqc_logo   ? Channel.fromPath(params.multiqc_logo)   : Channel.empty()
                                                         ^^^^^^^
  ```

- Warning: `workflows/pangenome.nf:76:98`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_multiqc_logo          = params.multiqc_logo   ? Channel.fromPath(params.multiqc_logo)   : Channel.empty()
                                                                                                   ^^^^^^^
  ```

- Warning: `workflows/pangenome.nf:88:48`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
              ch_community_join.map{meta, fasta, gzi, fai -> [ meta, fasta ]},
                                                 ^^^
  ```

- Warning: `workflows/pangenome.nf:88:53`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
              ch_community_join.map{meta, fasta, gzi, fai -> [ meta, fasta ]},
                                                      ^^^
  ```

- Warning: `workflows/pangenome.nf:89:41`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
              ch_community_join.map{meta, fasta, gzi, fai -> [ meta, fai ]},
                                          ^^^^^
  ```

- Warning: `workflows/pangenome.nf:89:48`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
              ch_community_join.map{meta, fasta, gzi, fai -> [ meta, fai ]},
                                                 ^^^
  ```

- Warning: `workflows/pangenome.nf:90:41`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
              ch_community_join.map{meta, fasta, gzi, fai -> [ meta, gzi ]},
                                          ^^^^^
  ```

- Warning: `workflows/pangenome.nf:90:53`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
              ch_community_join.map{meta, fasta, gzi, fai -> [ meta, gzi ]},
                                                      ^^^
  ```

- Warning: `workflows/pangenome.nf:101:17`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
          ODGI_QC(Channel.empty(), ch_odgi_qc_in, false, true)
                  ^^^^^^^
  ```

- Warning: `workflows/pangenome.nf:127:23`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
          ch_vcf_spec = Channel.from(params.vcf_spec).splitCsv().flatten()
                        ^^^^^^^
  ```

- Warning: `workflows/pangenome.nf:148:25`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_multiqc_config = Channel.fromPath("$projectDir/assets/multiqc_config.yml", checkIfExists: true)
                          ^^^^^^^
  ```

- Warning: `workflows/pangenome.nf:149:56`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_multiqc_custom_config = params.multiqc_config ? Channel.fromPath(params.multiqc_config, checkIfExists: true) : Channel.empty()
                                                         ^^^^^^^
  ```

- Warning: `workflows/pangenome.nf:149:119`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_multiqc_custom_config = params.multiqc_config ? Channel.fromPath(params.multiqc_config, checkIfExists: true) : Channel.empty()
                                                                                                                        ^^^^^^^
  ```

- Warning: `workflows/pangenome.nf:150:45`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_multiqc_logo = params.multiqc_logo ? Channel.fromPath(params.multiqc_logo, checkIfExists: true) : Channel.empty()
                                              ^^^^^^^
  ```

- Warning: `workflows/pangenome.nf:150:106`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_multiqc_logo = params.multiqc_logo ? Channel.fromPath(params.multiqc_logo, checkIfExists: true) : Channel.empty()
                                                                                                           ^^^^^^^
  ```

- Warning: `workflows/pangenome.nf:153:27`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_workflow_summary = Channel.value(paramsSummaryMultiqc(summary_params))
                            ^^^^^^^
  ```

- Warning: `workflows/pangenome.nf:158:30`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_methods_description = Channel.value(methodsDescriptionText(ch_multiqc_custom_methods_description))
                               ^^^^^^^
  ```

- Warning: `workflows/pangenome.nf:165:76`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
              ch_multiqc_files = ch_multiqc_files.mix(PGGB.out.qc.map{return it[1..9]})
                                                                             ^^
  ```

- Warning: `workflows/pangenome.nf:169:75`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          ch_multiqc_files = ch_multiqc_files.mix(ODGI_QC.out.qc.map{return it[1..8]})
                                                                            ^^
  ```
