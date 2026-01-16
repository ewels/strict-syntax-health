# Nextflow lint results

- Generated: 2026-01-16T10:21:48.841330284Z
- Nextflow version: 25.12.0-edge
- Summary: 27 errors, 73 warnings

## :x: Errors

- Error: `modules/local/hicpro/dnase_mapping_stats.nf:2:10`: `sample` is not defined

  ```nextflow
      tag "$sample = $bam"
           ^^^^^^^
  ```

- Error: `modules/nf-core/bwa/index/main.nf:14:27`: `bwa` is not defined

  ```nextflow
      tuple val(meta), path(bwa) , emit: index
                            ^^^
  ```

- Error: `nextflow.config:365:27`: `manifest` is not defined

  ```nextflow
  \033[0;35m  nf-core/hic ${manifest.version}\033[0m
                            ^^^^^^^^
  ```

- Error: `nextflow.config:368:26`: `manifest` is not defined

  ```nextflow
          afterText = """${manifest.doi ? "\n* The pipeline\n" : ""}${manifest.doi.tokenize(",").collect { "    https://doi.org/${it.trim().replace('https://doi.org/','')}"}.join("\n")}${manifest.doi ? "\n" : ""}
                           ^^^^^^^^
  ```

- Error: `nextflow.config:368:69`: `manifest` is not defined

  ```nextflow
          afterText = """${manifest.doi ? "\n* The pipeline\n" : ""}${manifest.doi.tokenize(",").collect { "    https://doi.org/${it.trim().replace('https://doi.org/','')}"}.join("\n")}${manifest.doi ? "\n" : ""}
                                                                      ^^^^^^^^
  ```

- Error: `nextflow.config:368:186`: `manifest` is not defined

  ```nextflow
          afterText = """${manifest.doi ? "\n* The pipeline\n" : ""}${manifest.doi.tokenize(",").collect { "    https://doi.org/${it.trim().replace('https://doi.org/','')}"}.join("\n")}${manifest.doi ? "\n" : ""}
                                                                                                                                                                                           ^^^^^^^^
  ```

- Error: `nextflow.config:377:22`: `validation` is not defined

  ```nextflow
          beforeText = validation.help.beforeText
                       ^^^^^^^^^^
  ```

- Error: `nextflow.config:378:21`: `validation` is not defined

  ```nextflow
          afterText = validation.help.afterText
                      ^^^^^^^^^^
  ```

- Error: `subworkflows/local/compartments.nf:26:28`: `cool` is already declared

  ```nextflow
              cool.map{meta, cool, res -> [meta, cool] },
                             ^^^^
  ```

- Error: `subworkflows/local/hicpro.nf:18:5`: `meta` was assigned but not declared

  ```nextflow
      meta = row[0].clone()
      ^^^^
  ```

- Error: `subworkflows/local/hicpro.nf:19:5`: `meta` is not defined

  ```nextflow
      meta.remove('chunk')
      ^^^^
  ```

- Error: `subworkflows/local/hicpro.nf:20:13`: `meta` is not defined

  ```nextflow
      return [meta, row[1]]
              ^^^^
  ```

- Error: `subworkflows/local/utils_nfcore_hic_pipeline/main.nf:284:9`: `meta` was assigned but not declared

  ```nextflow
          meta = row[0].clone()
          ^^^^
  ```

- Error: `subworkflows/local/utils_nfcore_hic_pipeline/main.nf:285:9`: `meta` is not defined

  ```nextflow
          meta.chunk = i
          ^^^^
  ```

- Error: `subworkflows/local/utils_nfcore_hic_pipeline/main.nf:286:9`: `meta` is not defined

  ```nextflow
          meta.part = row[1].size()
          ^^^^
  ```

- Error: `subworkflows/local/utils_nfcore_hic_pipeline/main.nf:287:17`: `meta` is not defined

  ```nextflow
          map += [meta, file]
                  ^^^^
  ```

- Error: `workflows/hic.nf:26:1`: Statements cannot be mixed with script declarations -- move statements into a process, workflow, or function

  ```nextflow
  ch_map_res = Channel.from( params.bin_size ).splitCsv().flatten().toInteger()
  ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  ```

- Error: `workflows/hic.nf:28:1`: Statements cannot be mixed with script declarations -- move statements into a process, workflow, or function

  ```nextflow
  if (params.res_zoomify){
  ^
  ```

- Error: `workflows/hic.nf:33:1`: Statements cannot be mixed with script declarations -- move statements into a process, workflow, or function

  ```nextflow
  if (params.res_tads && !params.skip_tads){
  ^
  ```

- Error: `workflows/hic.nf:43:1`: Statements cannot be mixed with script declarations -- move statements into a process, workflow, or function

  ```nextflow
  if (params.res_dist_decay && !params.skip_dist_decay){
  ^
  ```

- Error: `workflows/hic.nf:53:1`: Statements cannot be mixed with script declarations -- move statements into a process, workflow, or function

  ```nextflow
  if (params.res_compartments && !params.skip_compartments){
  ^
  ```

- Error: `workflows/hic.nf:63:1`: Statements cannot be mixed with script declarations -- move statements into a process, workflow, or function

  ```nextflow
  ch_map_res = ch_map_res.unique()
  ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  ```

- Error: `workflows/hic.nf:106:13`: `ch_map_res` is not defined

  ```nextflow
              ch_map_res
              ^^^^^^^^^^
  ```

- Error: `workflows/hic.nf:130:9`: `ch_map_res` is not defined

  ```nextflow
          ch_map_res
          ^^^^^^^^^^
  ```

- Error: `workflows/hic.nf:139:22`: `ch_ddecay_res` is not defined

  ```nextflow
              .combine(ch_ddecay_res)
                       ^^^^^^^^^^^^^
  ```

- Error: `workflows/hic.nf:155:22`: `ch_comp_res` is not defined

  ```nextflow
              .combine(ch_comp_res)
                       ^^^^^^^^^^^
  ```

- Error: `workflows/hic.nf:173:22`: `ch_tads_res` is not defined

  ```nextflow
              .combine(ch_tads_res)
                       ^^^^^^^^^^^
  ```

## :warning: Warnings

- Warning: `main.nf:50:19`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_versions = Channel.empty()
                    ^^^^^^^
  ```

- Warning: `modules/local/hicexplorer/hicPlotDistVsCounts.nf:22:9`: Variable was declared but not used

  ```nextflow
      def args = task.ext.args ?: ''
          ^^^^
  ```

- Warning: `modules/local/split_cooler_dump.nf:21:9`: Variable was declared but not used

  ```nextflow
      def args = task.ext.args ?: ''
          ^^^^
  ```

- Warning: `modules/nf-core/bowtie2/align/main.nf:93:9`: Variable was declared but not used

  ```nextflow
      def reference = fasta && extension=="cram"  ? "--reference ${fasta}" : ""
          ^^^^^^^^^
  ```

- Warning: `modules/nf-core/bwa/mem/main.nf:56:9`: Variable was declared but not used

  ```nextflow
      def args = task.ext.args ?: ''
          ^^^^
  ```

- Warning: `modules/nf-core/bwa/mem/main.nf:59:9`: Variable was declared but not used

  ```nextflow
      def samtools_command = sort_bam ? 'sort' : 'view'
          ^^^^^^^^^^^^^^^^
  ```

- Warning: `modules/nf-core/custom/getchromsizes/main.nf:23:9`: Variable was declared but not used

  ```nextflow
      def args = task.ext.args ?: ''
          ^^^^
  ```

- Warning: `modules/nf-core/samtools/flagstat/main.nf:21:9`: Variable was declared but not used

  ```nextflow
      def args = task.ext.args ?: ''
          ^^^^
  ```

- Warning: `nextflow.config:368:129`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          afterText = """${manifest.doi ? "\n* The pipeline\n" : ""}${manifest.doi.tokenize(",").collect { "    https://doi.org/${it.trim().replace('https://doi.org/','')}"}.join("\n")}${manifest.doi ? "\n" : ""}
                                                                                                                                  ^^
  ```

- Warning: `subworkflows/local/compartments.nf:12:19`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_versions = Channel.empty()
                    ^^^^^^^
  ```

- Warning: `subworkflows/local/compartments.nf:26:34`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
              cool.map{meta, cool, res -> [meta, cool] },
                                   ^^^
  ```

- Warning: `subworkflows/local/compartments.nf:27:13`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
              Channel.value([])
              ^^^^^^^
  ```

- Warning: `subworkflows/local/cooler.nf:31:19`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_versions = Channel.empty()
                    ^^^^^^^
  ```

- Warning: `subworkflows/local/cooler.nf:57:22`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          ch_cool.map{[it[0], it[1], ""]}
                       ^^
  ```

- Warning: `subworkflows/local/cooler.nf:57:29`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          ch_cool.map{[it[0], it[1], ""]}
                              ^^
  ```

- Warning: `subworkflows/local/cooler.nf:65:26`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
          ch_res_zoomify = Channel.from(params.res_zoomify).splitCsv().flatten().unique().toInteger()
                           ^^^^^^^
  ```

- Warning: `subworkflows/local/cooler.nf:70:18`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          .filter{ it[2] == it[3] }
                   ^^
  ```

- Warning: `subworkflows/local/cooler.nf:70:27`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          .filter{ it[2] == it[3] }
                            ^^
  ```

- Warning: `subworkflows/local/cooler.nf:84:38`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          COOLER_BALANCE.out.cool.map{[it[0], it[1], ""]}
                                       ^^
  ```

- Warning: `subworkflows/local/cooler.nf:84:45`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          COOLER_BALANCE.out.cool.map{[it[0], it[1], ""]}
                                              ^^
  ```

- Warning: `subworkflows/local/hicpro.nf:35:19`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_versions = Channel.empty()
                    ^^^^^^^
  ```

- Warning: `subworkflows/local/hicpro.nf:140:30`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
          ch_hicpro_raw_maps = Channel.empty()
                               ^^^^^^^
  ```

- Warning: `subworkflows/local/hicpro.nf:141:31`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
          ch_hicpro_iced_maps = Channel.empty()
                                ^^^^^^^
  ```

- Warning: `subworkflows/local/hicpro_mapping.nf:23:19`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_versions = Channel.empty()
                    ^^^^^^^
  ```

- Warning: `subworkflows/local/pairtools.nf:36:19`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_versions = Channel.empty()
                    ^^^^^^^
  ```

- Warning: `subworkflows/local/pairtools.nf:42:9`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
          Channel.value([])
          ^^^^^^^
  ```

- Warning: `subworkflows/local/pairtools.nf:71:21`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
              single: it[0].part <=1
                      ^^
  ```

- Warning: `subworkflows/local/pairtools.nf:72:23`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
              multiple: it[0].part > 1
                        ^^
  ```

- Warning: `subworkflows/local/prepare_genome.nf:18:19`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_versions = Channel.empty()
                    ^^^^^^^
  ```

- Warning: `subworkflows/local/prepare_genome.nf:24:16`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_fasta = Channel.fromPath( fasta )
                 ^^^^^^^
  ```

- Warning: `subworkflows/local/prepare_genome.nf:39:24`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
              ch_index = Channel.fromPath( bwt2_index , checkIfExists: true)
                         ^^^^^^^
  ```

- Warning: `subworkflows/local/prepare_genome.nf:56:24`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
              ch_index = Channel.fromPath( bwa_index , checkIfExists: true)
                         ^^^^^^^
  ```

- Warning: `subworkflows/local/prepare_genome.nf:72:24`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
          ch_chromsize = Channel.fromPath( params.chromosome_size , checkIfExists: true)
                         ^^^^^^^
  ```

- Warning: `subworkflows/local/prepare_genome.nf:82:31`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
          ch_restriction_site = Channel.value(restriction_site)
                                ^^^^^^^
  ```

- Warning: `subworkflows/local/prepare_genome.nf:84:28`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
          ch_ligation_site = Channel.value(ligation_site)
                             ^^^^^^^
  ```

- Warning: `subworkflows/local/prepare_genome.nf:86:31`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
          ch_restriction_site = Channel.value(params.restriction_site)
                                ^^^^^^^
  ```

- Warning: `subworkflows/local/prepare_genome.nf:87:28`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
          ch_ligation_site = Channel.value(params.ligation_site)
                             ^^^^^^^
  ```

- Warning: `subworkflows/local/prepare_genome.nf:89:31`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
          ch_restriction_site = Channel.empty()
                                ^^^^^^^
  ```

- Warning: `subworkflows/local/prepare_genome.nf:90:28`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
          ch_ligation_site = Channel.empty()
                             ^^^^^^^
  ```

- Warning: `subworkflows/local/prepare_genome.nf:107:9`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
          Channel.fromPath( params.restriction_fragments, checkIfExists: true )
          ^^^^^^^
  ```

- Warning: `subworkflows/local/prepare_genome.nf:111:22`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
          ch_resfrag = Channel.empty()
                       ^^^^^^^
  ```

- Warning: `subworkflows/local/tads.nf:10:19`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_versions = Channel.empty()
                    ^^^^^^^
  ```

- Warning: `subworkflows/local/tads.nf:11:15`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_tads = Channel.empty()
                ^^^^^^^
  ```

- Warning: `subworkflows/local/utils_nfcore_hic_pipeline/main.nf:31:5`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
      monochrome_logs   // boolean: Do not use coloured log outputs
      ^^^^^^^^^^^^^^^
  ```

- Warning: `subworkflows/local/utils_nfcore_hic_pipeline/main.nf:34:5`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
      input             //  string: Path to input samplesheet
      ^^^^^
  ```

- Warning: `subworkflows/local/utils_nfcore_hic_pipeline/main.nf:38:19`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_versions = Channel.empty()
                    ^^^^^^^
  ```

- Warning: `subworkflows/local/utils_nfcore_hic_pipeline/main.nf:74:16`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_input = Channel.fromList(samplesheetToList(params.input, "${projectDir}/assets/schema_input.json"))
                 ^^^^^^^
  ```

- Warning: `subworkflows/nf-core/utils_nfcore_pipeline/main.nf:101:98`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      return ch_versions.unique().map { version -> processVersionsFromYAML(version) }.unique().mix(Channel.of(workflowVersionToYAML()))
                                                                                                   ^^^^^^^
  ```

- Warning: `workflows/hic.nf:26:14`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
  ch_map_res = Channel.from( params.bin_size ).splitCsv().flatten().toInteger()
               ^^^^^^^
  ```

- Warning: `workflows/hic.nf:29:19`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_zoom_res = Channel.from( params.res_zoomify ).splitCsv().flatten().toInteger()
                    ^^^^^^^
  ```

- Warning: `workflows/hic.nf:34:19`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_tads_res = Channel.from( "${params.res_tads}" ).splitCsv().flatten().toInteger()
                    ^^^^^^^
  ```

- Warning: `workflows/hic.nf:37:17`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_tads_res=Channel.empty()
                  ^^^^^^^
  ```

- Warning: `workflows/hic.nf:44:21`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_ddecay_res = Channel.from( "${params.res_dist_decay}" ).splitCsv().flatten().toInteger()
                      ^^^^^^^
  ```

- Warning: `workflows/hic.nf:47:21`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_ddecay_res = Channel.empty()
                      ^^^^^^^
  ```

- Warning: `workflows/hic.nf:54:19`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_comp_res = Channel.from( "${params.res_compartments}" ).splitCsv().flatten().toInteger()
                    ^^^^^^^
  ```

- Warning: `workflows/hic.nf:57:19`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_comp_res = Channel.empty()
                    ^^^^^^^
  ```

- Warning: `workflows/hic.nf:79:5`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
      ch_restriction_site
      ^^^^^^^^^^^^^^^^^^^
  ```

- Warning: `workflows/hic.nf:84:19`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_versions = Channel.empty()
                    ^^^^^^^
  ```

- Warning: `workflows/hic.nf:85:24`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_multiqc_files = Channel.empty()
                         ^^^^^^^
  ```

- Warning: `workflows/hic.nf:92:68`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
      ch_multiqc_files = ch_multiqc_files.mix(FASTQC.out.zip.collect{it[1]})
                                                                     ^^
  ```

- Warning: `workflows/hic.nf:140:22`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
              .filter{ it[0].resolution == it[2] }
                       ^^
  ```

- Warning: `workflows/hic.nf:140:42`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
              .filter{ it[0].resolution == it[2] }
                                           ^^
  ```

- Warning: `workflows/hic.nf:156:22`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
              .filter{ it[0].resolution == it[2] }
                       ^^
  ```

- Warning: `workflows/hic.nf:156:42`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
              .filter{ it[0].resolution == it[2] }
                                           ^^
  ```

- Warning: `workflows/hic.nf:174:22`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
              .filter{ it[0].resolution == it[2] }
                       ^^
  ```

- Warning: `workflows/hic.nf:174:42`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
              .filter{ it[0].resolution == it[2] }
                                           ^^
  ```

- Warning: `workflows/hic.nf:199:32`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_multiqc_config        = Channel.fromPath(
                                 ^^^^^^^
  ```

- Warning: `workflows/hic.nf:202:9`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
          Channel.fromPath(params.multiqc_config, checkIfExists: true) :
          ^^^^^^^
  ```

- Warning: `workflows/hic.nf:203:9`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
          Channel.empty()
          ^^^^^^^
  ```

- Warning: `workflows/hic.nf:205:9`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
          Channel.fromPath(params.multiqc_logo, checkIfExists: true) :
          ^^^^^^^
  ```

- Warning: `workflows/hic.nf:206:9`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
          Channel.empty()
          ^^^^^^^
  ```

- Warning: `workflows/hic.nf:210:27`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_workflow_summary = Channel.value(paramsSummaryMultiqc(summary_params))
                            ^^^^^^^
  ```

- Warning: `workflows/hic.nf:216:45`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_methods_description                = Channel.value(
                                              ^^^^^^^
  ```
