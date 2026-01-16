# Nextflow lint results

- Generated: 2026-01-16T10:24:29.834982671Z
- Nextflow version: 25.12.0-edge
- Summary: 31 errors, 158 warnings

## :x: Errors

- Error: `conf/modules.config:179:21`: Unexpected input: '{'

  ```nextflow
              saveAs: { filename -> filename.equals('versions.yml') ? null : filename }
                      ^
  ```

- Error: `main.nf:20:1`: Module could not be parsed: '/home/runner/work/strict-syntax-health/strict-syntax-health/pipelines/multiplesequencealign/subworkflows/local/utils_nfcore_multiplesequencealign_pipeline/main.nf'

  ```nextflow
  include { PIPELINE_INITIALISATION } from './subworkflows/local/utils_nfcore_multiplesequencealign_pipeline'
  ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  ```

- Error: `main.nf:21:1`: Module could not be parsed: '/home/runner/work/strict-syntax-health/strict-syntax-health/pipelines/multiplesequencealign/subworkflows/local/utils_nfcore_multiplesequencealign_pipeline/main.nf'

  ```nextflow
  include { PIPELINE_COMPLETION     } from './subworkflows/local/utils_nfcore_multiplesequencealign_pipeline'
  ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  ```

- Error: `main.nf:64:5`: `PIPELINE_INITIALISATION` is not defined

  ```nextflow
      PIPELINE_INITIALISATION (
      ^^^^^^^^^^^^^^^^^^^^^^^
  ```

- Error: `main.nf:78:9`: `PIPELINE_INITIALISATION` is not defined

  ```nextflow
          PIPELINE_INITIALISATION.out.samplesheet,
          ^^^^^^^^^^^^^^^^^^^^^^^
  ```

- Error: `main.nf:79:9`: `PIPELINE_INITIALISATION` is not defined

  ```nextflow
          PIPELINE_INITIALISATION.out.tools
          ^^^^^^^^^^^^^^^^^^^^^^^
  ```

- Error: `main.nf:85:5`: `PIPELINE_COMPLETION` is not defined

  ```nextflow
      PIPELINE_COMPLETION (
      ^^^^^^^^^^^^^^^^^^^
  ```

- Error: `modules/nf-core/mafft/align/main.nf:29:9`: `add` is already declared

  ```nextflow
      def add          = add             ? "--add <(unpigz -cdf ${add})"                   : ''
          ^^^
  ```

- Error: `modules/nf-core/mafft/align/main.nf:30:9`: `addfragments` is already declared

  ```nextflow
      def addfragments = addfragments    ? "--addfragments <(unpigz -cdf ${addfragments})" : ''
          ^^^^^^^^^^^^
  ```

- Error: `modules/nf-core/mafft/align/main.nf:31:9`: `addfull` is already declared

  ```nextflow
      def addfull      = addfull         ? "--addfull <(unpigz -cdf ${addfull})"           : ''
          ^^^^^^^
  ```

- Error: `modules/nf-core/mafft/align/main.nf:32:9`: `addprofile` is already declared

  ```nextflow
      def addprofile   = addprofile      ? "--addprofile <(unpigz -cdf ${addprofile})"     : ''
          ^^^^^^^^^^
  ```

- Error: `modules/nf-core/mafft/align/main.nf:33:9`: `addlong` is already declared

  ```nextflow
      def addlong      = addlong         ? "--addlong <(unpigz -cdf ${addlong})"           : ''
          ^^^^^^^
  ```

- Error: `modules/nf-core/mafft/align/main.nf:59:9`: `add` is already declared

  ```nextflow
      def add          = add             ? "--add ${add}"                   : ''
          ^^^
  ```

- Error: `modules/nf-core/mafft/align/main.nf:60:9`: `addfragments` is already declared

  ```nextflow
      def addfragments = addfragments    ? "--addfragments ${addfragments}" : ''
          ^^^^^^^^^^^^
  ```

- Error: `modules/nf-core/mafft/align/main.nf:61:9`: `addfull` is already declared

  ```nextflow
      def addfull      = addfull         ? "--addfull ${addfull}"           : ''
          ^^^^^^^
  ```

- Error: `modules/nf-core/mafft/align/main.nf:62:9`: `addprofile` is already declared

  ```nextflow
      def addprofile   = addprofile      ? "--addprofile ${addprofile}"     : ''
          ^^^^^^^^^^
  ```

- Error: `modules/nf-core/mafft/align/main.nf:63:9`: `addlong` is already declared

  ```nextflow
      def addlong      = addlong         ? "--addlong ${addlong}"           : ''
          ^^^^^^^
  ```

- Error: `nextflow.config:341:1`: Variable declarations cannot be mixed with config statements

  ```nextflow
  def co2_timestamp = new java.util.Date().format( 'yyyy-MM-dd_HH-mm-ss')
  ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  ```

- Error: `nextflow.config:344:72`: `co2_timestamp` is not defined

  ```nextflow
      traceFile   = "${params.outdir}/pipeline_info/co2footprint_trace_${co2_timestamp}.txt"
                                                                         ^^^^^^^^^^^^^
  ```

- Error: `nextflow.config:345:73`: `co2_timestamp` is not defined

  ```nextflow
      reportFile  = "${params.outdir}/pipeline_info/co2footprint_report_${co2_timestamp}.html"
                                                                          ^^^^^^^^^^^^^
  ```

- Error: `nextflow.config:346:74`: `co2_timestamp` is not defined

  ```nextflow
      summaryFile = "${params.outdir}/pipeline_info/co2footprint_summary_${co2_timestamp}.txt"
                                                                           ^^^^^^^^^^^^^
  ```

- Error: `nextflow.config:364:45`: `manifest` is not defined

  ```nextflow
  \033[0;35m  nf-core/multiplesequencealign ${manifest.version}\033[0m
                                              ^^^^^^^^
  ```

- Error: `nextflow.config:367:26`: `manifest` is not defined

  ```nextflow
          afterText = """${manifest.doi ? "\n* The pipeline\n" : ""}${manifest.doi.tokenize(",").collect { "    https://doi.org/${it.trim().replace('https://doi.org/','')}"}.join("\n")}${manifest.doi ? "\n" : ""}
                           ^^^^^^^^
  ```

- Error: `nextflow.config:367:69`: `manifest` is not defined

  ```nextflow
          afterText = """${manifest.doi ? "\n* The pipeline\n" : ""}${manifest.doi.tokenize(",").collect { "    https://doi.org/${it.trim().replace('https://doi.org/','')}"}.join("\n")}${manifest.doi ? "\n" : ""}
                                                                      ^^^^^^^^
  ```

- Error: `nextflow.config:367:186`: `manifest` is not defined

  ```nextflow
          afterText = """${manifest.doi ? "\n* The pipeline\n" : ""}${manifest.doi.tokenize(",").collect { "    https://doi.org/${it.trim().replace('https://doi.org/','')}"}.join("\n")}${manifest.doi ? "\n" : ""}
                                                                                                                                                                                           ^^^^^^^^
  ```

- Error: `nextflow.config:376:22`: `validation` is not defined

  ```nextflow
          beforeText = validation.help.beforeText
                       ^^^^^^^^^^
  ```

- Error: `nextflow.config:377:21`: `validation` is not defined

  ```nextflow
          afterText = validation.help.afterText
                      ^^^^^^^^^^
  ```

- Error: `subworkflows/local/utils_nfcore_multiplesequencealign_pipeline/main.nf:570:66`: Unexpected input: '='

  ```nextflow
      def traceTrees = prepTrace(cleanTraceData, suffix_to_replace = "_GUIDETREE", subworkflow = "COMPUTE_TREES", keys)
                                                                   ^
  ```

- Error: `workflows/multiplesequencealign.nf:10:1`: Module could not be parsed: '/home/runner/work/strict-syntax-health/strict-syntax-health/pipelines/multiplesequencealign/subworkflows/local/utils_nfcore_multiplesequencealign_pipeline/main.nf'

  ```nextflow
  include { methodsDescriptionText } from '../subworkflows/local/utils_nfcore_multiplesequencealign_pipeline'
  ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  ```

- Error: `workflows/multiplesequencealign.nf:311:13`: Variables in a closure should be declared with `def`

  ```nextflow
              content =  meta.keySet().collect{it}.join(",")
              ^^^^^^^
  ```

- Error: `workflows/multiplesequencealign.nf:390:13`: `methodsDescriptionText` is not defined

  ```nextflow
              methodsDescriptionText(ch_multiqc_custom_methods_description))
              ^^^^^^^^^^^^^^^^^^^^^^
  ```

## :warning: Warnings

- Warning: `modules/local/custom/calculate_gaps/main.nf:20:9`: Variable was declared but not used

  ```nextflow
      def args = task.ext.args ?: ''
          ^^^^
  ```

- Warning: `modules/local/custom/calculate_seqstats/main.nf:22:9`: Variable was declared but not used

  ```nextflow
      def args = task.ext.args ?: ''
          ^^^^
  ```

- Warning: `modules/local/custom/create_template/main.nf:20:9`: Variable was declared but not used

  ```nextflow
      def args = task.ext.args ?: ''
          ^^^^
  ```

- Warning: `modules/local/custom/extract_plddt/main.nf:21:9`: Variable was declared but not used

  ```nextflow
      def args = task.ext.args ?: ''
          ^^^^
  ```

- Warning: `modules/local/custom/parse_irmsd/main.nf:21:9`: Variable was declared but not used

  ```nextflow
      def args = task.ext.args ?: ''
          ^^^^
  ```

- Warning: `modules/local/custom/parse_sim/main.nf:20:9`: Variable was declared but not used

  ```nextflow
      def args = task.ext.args ?: ''
          ^^^^
  ```

- Warning: `modules/local/custom/prepare_multiqc/main.nf:21:9`: Variable was declared but not used

  ```nextflow
      def args = task.ext.args ?: ''
          ^^^^
  ```

- Warning: `modules/local/custom/prepare_shiny/main.nf:23:9`: Variable was declared but not used

  ```nextflow
      def args         = task.ext.args ?: ''
          ^^^^
  ```

- Warning: `modules/local/custom/prepare_shiny/main.nf:24:5`: Variable was declared but not used

  ```nextflow
      prefix           = task.ext.prefix ?: "${meta.id}"
      ^^^^^^
  ```

- Warning: `modules/nf-core/clustalo/align/main.nf:60:9`: Variable was declared but not used

  ```nextflow
      def args = task.ext.args ?: ''
          ^^^^
  ```

- Warning: `modules/nf-core/clustalo/guidetree/main.nf:37:9`: Variable was declared but not used

  ```nextflow
      def args = task.ext.args ?: ''
          ^^^^
  ```

- Warning: `modules/nf-core/famsa/guidetree/main.nf:38:9`: Variable was declared but not used

  ```nextflow
      def args = task.ext.args ?: ''
          ^^^^
  ```

- Warning: `modules/nf-core/foldmason/createdb/main.nf:37:9`: Variable was declared but not used

  ```nextflow
      def args = task.ext.args ?: ''
          ^^^^
  ```

- Warning: `modules/nf-core/foldmason/easymsa/main.nf:52:9`: Variable was declared but not used

  ```nextflow
      def args = task.ext.args ?: ''
          ^^^^
  ```

- Warning: `modules/nf-core/foldmason/msa2lddtreport/main.nf:42:9`: Variable was declared but not used

  ```nextflow
      def args = task.ext.args ?: ''
          ^^^^
  ```

- Warning: `modules/nf-core/kalign/align/main.nf:59:9`: Variable was declared but not used

  ```nextflow
      def args = task.ext.args ?: ''
          ^^^^
  ```

- Warning: `modules/nf-core/learnmsa/align/main.nf:35:9`: Variable was declared but not used

  ```nextflow
      def args = task.ext.args ?: ''
          ^^^^
  ```

- Warning: `modules/nf-core/mafft/align/main.nf:57:9`: Variable was declared but not used

  ```nextflow
      def args         = task.ext.args   ?: ''
          ^^^^
  ```

- Warning: `modules/nf-core/mafft/align/main.nf:59:9`: Variable was declared but not used

  ```nextflow
      def add          = add             ? "--add ${add}"                   : ''
          ^^^
  ```

- Warning: `modules/nf-core/mafft/align/main.nf:60:9`: Variable was declared but not used

  ```nextflow
      def addfragments = addfragments    ? "--addfragments ${addfragments}" : ''
          ^^^^^^^^^^^^
  ```

- Warning: `modules/nf-core/mafft/align/main.nf:61:9`: Variable was declared but not used

  ```nextflow
      def addfull      = addfull         ? "--addfull ${addfull}"           : ''
          ^^^^^^^
  ```

- Warning: `modules/nf-core/mafft/align/main.nf:62:9`: Variable was declared but not used

  ```nextflow
      def addprofile   = addprofile      ? "--addprofile ${addprofile}"     : ''
          ^^^^^^^^^^
  ```

- Warning: `modules/nf-core/mafft/align/main.nf:63:9`: Variable was declared but not used

  ```nextflow
      def addlong      = addlong         ? "--addlong ${addlong}"           : ''
          ^^^^^^^
  ```

- Warning: `modules/nf-core/mafft/guidetree/main.nf:42:9`: Variable was declared but not used

  ```nextflow
      def args = task.ext.args ?: ''
          ^^^^
  ```

- Warning: `modules/nf-core/magus/align/main.nf:47:9`: Variable was declared but not used

  ```nextflow
      def args = task.ext.args ?: ''
          ^^^^
  ```

- Warning: `modules/nf-core/mtmalign/align/main.nf:25:9`: Variable was declared but not used

  ```nextflow
      def args = task.ext.args ?: ''
          ^^^^
  ```

- Warning: `modules/nf-core/muscle5/super5/main.nf:52:9`: Variable was declared but not used

  ```nextflow
      def args = task.ext.args ?: ''
          ^^^^
  ```

- Warning: `modules/nf-core/pigz/compress/main.nf:35:9`: Variable was declared but not used

  ```nextflow
      def args = task.ext.args ?: ''
          ^^^^
  ```

- Warning: `modules/nf-core/pigz/uncompress/main.nf:39:9`: Variable was declared but not used

  ```nextflow
      def args = task.ext.args ?: ''
          ^^^^
  ```

- Warning: `modules/nf-core/tcoffee/alncompare/main.nf:58:9`: Variable was declared but not used

  ```nextflow
      def args = task.ext.args ?: ''
          ^^^^
  ```

- Warning: `modules/nf-core/tcoffee/extractfrompdb/main.nf:40:9`: Variable was declared but not used

  ```nextflow
      def args = task.ext.args ?: ''
          ^^^^
  ```

- Warning: `modules/nf-core/tcoffee/irmsd/main.nf:44:9`: Variable was declared but not used

  ```nextflow
      def args = task.ext.args ?: ''
          ^^^^
  ```

- Warning: `modules/nf-core/tcoffee/seqreformat/main.nf:38:9`: Variable was declared but not used

  ```nextflow
      def args = task.ext.args ?: ''
          ^^^^
  ```

- Warning: `modules/nf-core/tcoffee/tcs/main.nf:23:9`: Variable was declared but not used

  ```nextflow
      def args          = task.ext.args ?: ''
          ^^^^
  ```

- Warning: `modules/nf-core/tcoffee/tcs/main.nf:63:9`: Variable was declared but not used

  ```nextflow
      def args = task.ext.args ?: ''
          ^^^^
  ```

- Warning: `modules/nf-core/upp/align/main.nf:23:9`: Variable was declared but not used

  ```nextflow
      def tree_args = tree ? "-t $tree" : ""
          ^^^^^^^^^
  ```

- Warning: `nextflow.config:367:129`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          afterText = """${manifest.doi ? "\n* The pipeline\n" : ""}${manifest.doi.tokenize(",").collect { "    https://doi.org/${it.trim().replace('https://doi.org/','')}"}.join("\n")}${manifest.doi ? "\n" : ""}
                                                                                                                                  ^^
  ```

- Warning: `subworkflows/local/ALIGN/main.nf:40:19`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_msa      = Channel.empty()
                    ^^^^^^^
  ```

- Warning: `subworkflows/local/ALIGN/main.nf:41:19`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_versions = Channel.empty()
                    ^^^^^^^
  ```

- Warning: `subworkflows/local/ALIGN/main.nf:81:13`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
              it[1] != null
              ^^
  ```

- Warning: `subworkflows/local/ALIGN/main.nf:92:25`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
              clustalo:   it[0]["aligner"] == "CLUSTALO"
                          ^^
  ```

- Warning: `subworkflows/local/ALIGN/main.nf:93:25`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
              famsa:      it[0]["aligner"] == "FAMSA"
                          ^^
  ```

- Warning: `subworkflows/local/ALIGN/main.nf:94:25`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
              kalign:     it[0]["aligner"] == "KALIGN"
                          ^^
  ```

- Warning: `subworkflows/local/ALIGN/main.nf:95:25`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
              learnmsa:   it[0]["aligner"] == "LEARNMSA"
                          ^^
  ```

- Warning: `subworkflows/local/ALIGN/main.nf:96:25`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
              mafft:      it[0]["aligner"] == "MAFFT"
                          ^^
  ```

- Warning: `subworkflows/local/ALIGN/main.nf:97:25`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
              magus:      it[0]["aligner"] == "MAGUS"
                          ^^
  ```

- Warning: `subworkflows/local/ALIGN/main.nf:98:25`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
              muscle5:    it[0]["aligner"] == "MUSCLE5"
                          ^^
  ```

- Warning: `subworkflows/local/ALIGN/main.nf:99:25`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
              mtmalign:   it[0]["aligner"] == "MTMALIGN"
                          ^^
  ```

- Warning: `subworkflows/local/ALIGN/main.nf:100:25`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
              regressive: it[0]["aligner"] == "REGRESSIVE"
                          ^^
  ```

- Warning: `subworkflows/local/ALIGN/main.nf:101:25`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
              tcoffee:    it[0]["aligner"] == "TCOFFEE"
                          ^^
  ```

- Warning: `subworkflows/local/ALIGN/main.nf:102:25`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
              tcoffee3d:  it[0]["aligner"] == "3DCOFFEE"
                          ^^
  ```

- Warning: `subworkflows/local/ALIGN/main.nf:103:25`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
              upp:        it[0]["aligner"] == "UPP"
                          ^^
  ```

- Warning: `subworkflows/local/ALIGN/main.nf:114:23`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
              mtmalign: it[0]["aligner"] == "MTMALIGN"
                        ^^
  ```

- Warning: `subworkflows/local/ALIGN/main.nf:127:13`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
              it.size() == 5
              ^^
  ```

- Warning: `subworkflows/local/ALIGN/main.nf:134:24`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
              foldmason: it[0]["aligner"] == "FOLDMASON"
                         ^^
  ```

- Warning: `subworkflows/local/ALIGN/main.nf:184:30`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
              meta, fastafile, treefile ->
                               ^^^^^^^^
  ```

- Warning: `subworkflows/local/ALIGN/main.nf:199:30`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
              meta, fastafile, treefile ->
                               ^^^^^^^^
  ```

- Warning: `subworkflows/local/ALIGN/main.nf:221:30`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
              meta, fastafile, treefile ->
                               ^^^^^^^^
  ```

- Warning: `subworkflows/local/ALIGN/main.nf:258:30`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
              meta, fastafile, treefile ->
                               ^^^^^^^^
  ```

- Warning: `subworkflows/local/ALIGN/main.nf:331:17`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
                  merging_id, meta, fastafile, treefile, templatefile, datafiles ->
                  ^^^^^^^^^^
  ```

- Warning: `subworkflows/local/ALIGN/main.nf:352:23`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
                  meta, template, dependency ->
                        ^^^^^^^^
  ```

- Warning: `subworkflows/local/ALIGN/main.nf:369:29`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
                  meta, tree, template, dependency ->
                              ^^^^^^^^
  ```

- Warning: `subworkflows/local/ALIGN/main.nf:388:23`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
              .filter { it[1].size() > 1 }
                        ^^
  ```

- Warning: `subworkflows/local/COMPUTE_TREES/main.nf:16:5`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
      ch_optional_data //channel: [ meta, template, [ /path/to/file1, /path/to/file2, ... ] ]
      ^^^^^^^^^^^^^^^^
  ```

- Warning: `subworkflows/local/COMPUTE_TREES/main.nf:20:19`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_versions = Channel.empty()
                    ^^^^^^^
  ```

- Warning: `subworkflows/local/COMPUTE_TREES/main.nf:21:19`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_trees    = Channel.empty()
                    ^^^^^^^
  ```

- Warning: `subworkflows/local/COMPUTE_TREES/main.nf:33:23`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
              famsa:    it[0]["tree"] == "FAMSA"
                        ^^
  ```

- Warning: `subworkflows/local/COMPUTE_TREES/main.nf:34:23`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
              clustalo: it[0]["tree"] == "CLUSTALO"
                        ^^
  ```

- Warning: `subworkflows/local/COMPUTE_TREES/main.nf:35:23`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
              mafft:    it[0]["tree"] == "MAFFT"
                        ^^
  ```

- Warning: `subworkflows/local/EVALUATE/main.nf:28:23`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_versions     = Channel.empty()
                        ^^^^^^^
  ```

- Warning: `subworkflows/local/EVALUATE/main.nf:29:23`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      sp_csv          = Channel.empty()
                        ^^^^^^^
  ```

- Warning: `subworkflows/local/EVALUATE/main.nf:30:23`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      tc_csv          = Channel.empty()
                        ^^^^^^^
  ```

- Warning: `subworkflows/local/EVALUATE/main.nf:31:23`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      irmsd_csv       = Channel.empty()
                        ^^^^^^^
  ```

- Warning: `subworkflows/local/EVALUATE/main.nf:32:23`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      tcs_csv         = Channel.empty()
                        ^^^^^^^
  ```

- Warning: `subworkflows/local/EVALUATE/main.nf:33:23`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      gaps_csv        = Channel.empty()
                        ^^^^^^^
  ```

- Warning: `subworkflows/local/EVALUATE/main.nf:34:23`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_eval_summary = Channel.empty()
                        ^^^^^^^
  ```

- Warning: `subworkflows/local/EVALUATE/main.nf:66:17`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
                  meta, csv -> csv
                  ^^^^
  ```

- Warning: `subworkflows/local/EVALUATE/main.nf:87:17`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
                  meta, csv ->
                  ^^^^
  ```

- Warning: `subworkflows/local/EVALUATE/main.nf:114:17`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
                  meta, csv ->
                  ^^^^
  ```

- Warning: `subworkflows/local/EVALUATE/main.nf:163:53`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
                                                      meta, csv -> csv
                                                      ^^^^
  ```

- Warning: `subworkflows/local/EVALUATE/main.nf:169:9`: Variable was declared but not used

  ```nextflow
          versions = ch_versions.mix(CONCAT_IRMSD.out.versions)
          ^^^^^^^^
  ```

- Warning: `subworkflows/local/EVALUATE/main.nf:186:17`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
                  meta, csv ->
                  ^^^^
  ```

- Warning: `subworkflows/local/EVALUATE/main.nf:206:31`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
      sp      = sp_csv.map    { meta, csv -> csv }
                                ^^^^
  ```

- Warning: `subworkflows/local/EVALUATE/main.nf:207:31`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
      tc      = tc_csv.map    { meta, csv -> csv }
                                ^^^^
  ```

- Warning: `subworkflows/local/EVALUATE/main.nf:208:31`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
      irmsd   = irmsd_csv.map { meta, csv -> csv }
                                ^^^^
  ```

- Warning: `subworkflows/local/EVALUATE/main.nf:209:31`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
      gaps    = gaps_csv.map  { meta, csv -> csv }
                                ^^^^
  ```

- Warning: `subworkflows/local/EVALUATE/main.nf:210:31`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
      tcs     = tcs_csv.map   { meta, csv -> csv }
                                ^^^^
  ```

- Warning: `subworkflows/local/PREPROCESS/main.nf:10:19`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_versions = Channel.empty()
                    ^^^^^^^
  ```

- Warning: `subworkflows/local/PREPROCESS/main.nf:11:28`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_preprocessed_data = Channel.empty()
                             ^^^^^^^
  ```

- Warning: `subworkflows/local/STATS/main.nf:20:24`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_versions      = Channel.empty()
                         ^^^^^^^
  ```

- Warning: `subworkflows/local/STATS/main.nf:21:24`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      sim_csv          = Channel.empty()
                         ^^^^^^^
  ```

- Warning: `subworkflows/local/STATS/main.nf:22:24`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      seqstats_csv     = Channel.empty()
                         ^^^^^^^
  ```

- Warning: `subworkflows/local/STATS/main.nf:23:24`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      plddts_csv       = Channel.empty()
                         ^^^^^^^
  ```

- Warning: `subworkflows/local/STATS/main.nf:24:24`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_stats_summary = Channel.empty()
                         ^^^^^^^
  ```

- Warning: `subworkflows/local/STATS/main.nf:39:17`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
                  meta, csv ->
                  ^^^^
  ```

- Warning: `subworkflows/local/STATS/main.nf:70:17`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
                  meta, csv ->
                  ^^^^
  ```

- Warning: `subworkflows/local/STATS/main.nf:99:17`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
                  meta, csv -> csv
                  ^^^^
  ```

- Warning: `subworkflows/local/STATS/main.nf:121:35`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
      sim      = sim_csv.map      { meta, csv -> csv }
                                    ^^^^
  ```

- Warning: `subworkflows/local/STATS/main.nf:122:35`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
      seqstats = seqstats_csv.map { meta, csv -> csv }
                                    ^^^^
  ```

- Warning: `subworkflows/local/STATS/main.nf:123:35`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
      plddts   = plddts_csv.map   { meta, csv -> csv }
                                    ^^^^
  ```

- Warning: `subworkflows/local/STATS/main.nf:139:14`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
      ].count{ it == true }
               ^^
  ```

- Warning: `subworkflows/local/TEMPLATES/main.nf:12:19`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_versions = Channel.empty()
                    ^^^^^^^
  ```

- Warning: `subworkflows/local/TEMPLATES/main.nf:17:23`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
              template: it[2] != null
                        ^^
  ```

- Warning: `subworkflows/local/TEMPLATES/main.nf:26:36`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
                  meta,optional_data,template ->
                                     ^^^^^^^^
  ```

- Warning: `subworkflows/local/TEMPLATES/main.nf:35:18`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
              meta,optional_data,template ->
                   ^^^^^^^^^^^^^
  ```

- Warning: `subworkflows/local/VISUALIZATION/main.nf:13:19`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_versions = Channel.empty()
                    ^^^^^^^
  ```

- Warning: `subworkflows/local/VISUALIZATION/main.nf:14:19`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_html     = Channel.empty()
                    ^^^^^^^
  ```

- Warning: `subworkflows/local/VISUALIZATION/main.nf:25:13`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
              it.size() == 4
              ^^
  ```

- Warning: `subworkflows/local/VISUALIZATION/main.nf:28:13`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
              tree_meta, meta, msa, tree -> [ meta.subMap(["id"]), meta, msa, tree ]
              ^^^^^^^^^
  ```

- Warning: `subworkflows/nf-core/utils_nfcore_pipeline/main.nf:101:98`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      return ch_versions.unique().map { version -> processVersionsFromYAML(version) }.unique().mix(Channel.of(workflowVersionToYAML()))
                                                                                                   ^^^^^^^
  ```

- Warning: `workflows/multiplesequencealign.nf:63:36`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_multiqc_files             = Channel.empty()
                                     ^^^^^^^
  ```

- Warning: `workflows/multiplesequencealign.nf:64:36`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_multiqc_report            = Channel.empty()
                                     ^^^^^^^
  ```

- Warning: `workflows/multiplesequencealign.nf:65:36`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      evaluation_summary           = Channel.empty()
                                     ^^^^^^^
  ```

- Warning: `workflows/multiplesequencealign.nf:66:36`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      stats_summary                = Channel.empty()
                                     ^^^^^^^
  ```

- Warning: `workflows/multiplesequencealign.nf:67:36`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      stats_and_evaluation_summary = Channel.empty()
                                     ^^^^^^^
  ```

- Warning: `workflows/multiplesequencealign.nf:68:36`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_refs                      = Channel.empty()
                                     ^^^^^^^
  ```

- Warning: `workflows/multiplesequencealign.nf:69:36`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_templates                 = Channel.empty()
                                     ^^^^^^^
  ```

- Warning: `workflows/multiplesequencealign.nf:70:36`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_optional_data             = Channel.empty()
                                     ^^^^^^^
  ```

- Warning: `workflows/multiplesequencealign.nf:71:36`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_versions                  = Channel.empty()
                                     ^^^^^^^
  ```

- Warning: `workflows/multiplesequencealign.nf:74:19`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          .filter { it[1].size() > 0}
                    ^^
  ```

- Warning: `workflows/multiplesequencealign.nf:76:26`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
              meta, fasta, ref, str, template ->
                           ^^^
  ```

- Warning: `workflows/multiplesequencealign.nf:76:31`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
              meta, fasta, ref, str, template ->
                                ^^^
  ```

- Warning: `workflows/multiplesequencealign.nf:76:36`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
              meta, fasta, ref, str, template ->
                                     ^^^^^^^^
  ```

- Warning: `workflows/multiplesequencealign.nf:82:19`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          .filter { it[2].size() > 0}
                    ^^
  ```

- Warning: `workflows/multiplesequencealign.nf:84:19`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
              meta, fasta, ref, str, template ->
                    ^^^^^
  ```

- Warning: `workflows/multiplesequencealign.nf:84:31`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
              meta, fasta, ref, str, template ->
                                ^^^
  ```

- Warning: `workflows/multiplesequencealign.nf:84:36`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
              meta, fasta, ref, str, template ->
                                     ^^^^^^^^
  ```

- Warning: `workflows/multiplesequencealign.nf:90:19`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          .filter { it[4].size() > 0}
                    ^^
  ```

- Warning: `workflows/multiplesequencealign.nf:92:19`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
              meta, fasta, ref, str, template ->
                    ^^^^^
  ```

- Warning: `workflows/multiplesequencealign.nf:92:26`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
              meta, fasta, ref, str, template ->
                           ^^^
  ```

- Warning: `workflows/multiplesequencealign.nf:92:31`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
              meta, fasta, ref, str, template ->
                                ^^^
  ```

- Warning: `workflows/multiplesequencealign.nf:119:24`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
              pdbs_dir = Channel.fromPath(params.pdbs_dir)
                         ^^^^^^^
  ```

- Warning: `workflows/multiplesequencealign.nf:124:24`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
                  .map { meta, dir -> [ file(dir).listFiles() ] }
                         ^^^^
  ```

- Warning: `workflows/multiplesequencealign.nf:132:42`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
              optional_data_to_be_mapped = Channel.fromPath(params.pdbs_dir+"/**")
                                           ^^^^^^^
  ```

- Warning: `workflows/multiplesequencealign.nf:158:24`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
                  .map { dep_id, dep, fasta_id -> [ fasta_id, dep ] }
                         ^^^^^^
  ```

- Warning: `workflows/multiplesequencealign.nf:168:23`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
                  meta, fasta, ref, str, template ->
                        ^^^^^
  ```

- Warning: `workflows/multiplesequencealign.nf:168:30`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
                  meta, fasta, ref, str, template ->
                               ^^^
  ```

- Warning: `workflows/multiplesequencealign.nf:168:40`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
                  meta, fasta, ref, str, template ->
                                         ^^^^^^^^
  ```

- Warning: `workflows/multiplesequencealign.nf:171:23`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
              .filter { it[1].size() > 0 }
                        ^^
  ```

- Warning: `workflows/multiplesequencealign.nf:178:31`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
                  compressed:   it[1].endsWith('.tar.gz')
                                ^^
  ```

- Warning: `workflows/multiplesequencealign.nf:202:13`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
              it[-1] == null
              ^^
  ```

- Warning: `workflows/multiplesequencealign.nf:242:19`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          .filter { it[3]["aligner"] == "3DCOFFEE" }
                    ^^
  ```

- Warning: `workflows/multiplesequencealign.nf:249:33`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_optional_data_template = Channel.empty()
                                  ^^^^^^^
  ```

- Warning: `workflows/multiplesequencealign.nf:263:13`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
              it[-1] == null
              ^^
  ```

- Warning: `workflows/multiplesequencealign.nf:310:80`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          ALIGN.out.msa.collectFile(keepHeader: true, skip: 1,sort: true){ meta, msa ->
                                                                                 ^^^
  ```

- Warning: `workflows/multiplesequencealign.nf:311:46`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
              content =  meta.keySet().collect{it}.join(",")
                                               ^^
  ```

- Warning: `workflows/multiplesequencealign.nf:313:46`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
              content += meta.values().collect{it}.join(",")
                                               ^^
  ```

- Warning: `workflows/multiplesequencealign.nf:328:48`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          stats_summary_csv = stats_summary.map{ meta, csv -> csv }
                                                 ^^^^
  ```

- Warning: `workflows/multiplesequencealign.nf:329:53`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          eval_summary_csv  = evaluation_summary.map{ meta, csv -> csv }
                                                      ^^^^
  ```

- Warning: `workflows/multiplesequencealign.nf:346:21`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
          shiny_app = Channel.fromPath(params.shiny_app)
                      ^^^^^^^
  ```

- Warning: `workflows/multiplesequencealign.nf:372:36`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
          ch_multiqc_config        = Channel.fromPath(
                                     ^^^^^^^
  ```

- Warning: `workflows/multiplesequencealign.nf:375:13`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
              Channel.fromPath(params.multiqc_config, checkIfExists: true) :
              ^^^^^^^
  ```

- Warning: `workflows/multiplesequencealign.nf:376:13`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
              Channel.empty()
              ^^^^^^^
  ```

- Warning: `workflows/multiplesequencealign.nf:378:13`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
              Channel.fromPath(params.multiqc_logo, checkIfExists: true) :
              ^^^^^^^
  ```

- Warning: `workflows/multiplesequencealign.nf:379:13`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
              Channel.empty()
              ^^^^^^^
  ```

- Warning: `workflows/multiplesequencealign.nf:383:49`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
          ch_workflow_summary                   = Channel.value(paramsSummaryMultiqc(summary_params))
                                                  ^^^^^^^
  ```

- Warning: `workflows/multiplesequencealign.nf:389:49`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
          ch_methods_description                = Channel.value(
                                                  ^^^^^^^
  ```

- Warning: `workflows/multiplesequencealign.nf:401:112`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          ch_multiqc_files                      = ch_multiqc_files.mix(PREPARE_MULTIQC.out.multiqc_table.collect{it[1]}.ifEmpty([]))
                                                                                                                 ^^
  ```
