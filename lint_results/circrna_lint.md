# Nextflow lint results

- Generated: 2026-01-14T09:10:23.291145543Z
- Nextflow version: 25.12.0-edge
- Summary: 14 errors, 157 warnings

## :x: Errors

- Error: `modules/nf-core/bedtools/groupby/main.nf:24:9`: `summary_col` is already declared

  ```nextflow
      def summary_col = task.ext.summary_col ? "-c ${task.ext.summary_col}" : "-c 5"
          ^^^^^^^^^^^
  ```

- Error: `modules/nf-core/segemehl/align/main.nf:28:9`: `reads` is already declared

  ```nextflow
      def reads = meta.single_end ? "-q ${reads}" : "-q ${reads[0]} -p ${reads[1]}"
          ^^^^^
  ```

- Error: `modules/nf-core/trinity/main.nf:26:20`: Unexpected input: ','

  ```nextflow
      def reads1 = [], reads2 = []
                     ^
  ```

- Error: `nextflow.config:233:21`: Invalid include source: '/home/runner/work/strict-syntax-health/strict-syntax-health/pipelines/circrna/conf/test_igenomes.config'

  ```nextflow
      test_igenomes { includeConfig 'conf/test_igenomes.config' }
                      ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  ```

- Error: `nextflow.config:349:31`: `manifest` is not defined

  ```nextflow
  \033[0;35m  nf-core/circrna ${manifest.version}\033[0m
                                ^^^^^^^^
  ```

- Error: `nextflow.config:352:26`: `manifest` is not defined

  ```nextflow
          afterText = """${manifest.doi ? "\n* The pipeline\n" : ""}${manifest.doi.tokenize(",").collect { "    https://doi.org/${it.trim().replace('https://doi.org/','')}"}.join("\n")}${manifest.doi ? "\n" : ""}
                           ^^^^^^^^
  ```

- Error: `nextflow.config:352:69`: `manifest` is not defined

  ```nextflow
          afterText = """${manifest.doi ? "\n* The pipeline\n" : ""}${manifest.doi.tokenize(",").collect { "    https://doi.org/${it.trim().replace('https://doi.org/','')}"}.join("\n")}${manifest.doi ? "\n" : ""}
                                                                      ^^^^^^^^
  ```

- Error: `nextflow.config:352:186`: `manifest` is not defined

  ```nextflow
          afterText = """${manifest.doi ? "\n* The pipeline\n" : ""}${manifest.doi.tokenize(",").collect { "    https://doi.org/${it.trim().replace('https://doi.org/','')}"}.join("\n")}${manifest.doi ? "\n" : ""}
                                                                                                                                                                                           ^^^^^^^^
  ```

- Error: `nextflow.config:361:22`: `validation` is not defined

  ```nextflow
          beforeText = validation.help.beforeText
                       ^^^^^^^^^^
  ```

- Error: `nextflow.config:362:21`: `validation` is not defined

  ```nextflow
          afterText = validation.help.afterText
                      ^^^^^^^^^^
  ```

- Error: `subworkflows/local/fli_tools/jccirc.nf:1:1`: Module could not be parsed: '/home/runner/work/strict-syntax-health/strict-syntax-health/pipelines/circrna/modules/nf-core/trinity/main.nf'

  ```nextflow
  include { TRINITY } from '../../../modules/nf-core/trinity'
  ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  ```

- Error: `subworkflows/local/fli_tools/jccirc.nf:20:5`: `TRINITY` is not defined

  ```nextflow
      TRINITY(ch_trinity)
      ^^^^^^^
  ```

- Error: `subworkflows/local/fli_tools/jccirc.nf:21:35`: `TRINITY` is not defined

  ```nextflow
      ch_versions = ch_versions.mix(TRINITY.out.versions)
                                    ^^^^^^^
  ```

- Error: `subworkflows/local/fli_tools/jccirc.nf:32:22`: `TRINITY` is not defined

  ```nextflow
              .combine(TRINITY.out.transcript_fasta
                       ^^^^^^^
  ```

## :warning: Warnings

- Warning: `main.nf:92:19`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_versions = Channel.empty()
                    ^^^^^^^
  ```

- Warning: `main.nf:97:16`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_fasta = Channel.value([[id: "fasta"], file(params.fasta, checkIfExists: true)])
                 ^^^^^^^
  ```

- Warning: `main.nf:98:14`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_gtf = Channel.value([[id: "gtf"], file(params.gtf, checkIfExists: true)])
               ^^^^^^^
  ```

- Warning: `main.nf:99:39`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_blacklist = params.blacklist ? Channel.value(file(params.blacklist, checkIfExists: true)) : Channel.empty()
                                        ^^^^^^^
  ```

- Warning: `main.nf:99:100`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_blacklist = params.blacklist ? Channel.value(file(params.blacklist, checkIfExists: true)) : Channel.empty()
                                                                                                     ^^^^^^^
  ```

- Warning: `main.nf:100:33`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_mature = params.mature ? Channel.value([[id: "mature"], file(params.mature, checkIfExists: true)]) : Channel.empty()
                                  ^^^^^^^
  ```

- Warning: `main.nf:100:109`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_mature = params.mature ? Channel.value([[id: "mature"], file(params.mature, checkIfExists: true)]) : Channel.empty()
                                                                                                              ^^^^^^^
  ```

- Warning: `main.nf:101:39`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_phenotype = params.phenotype ? Channel.value([[id: "phenotype"], file(params.phenotype, checkIfExists: true)]) : Channel.empty()
                                        ^^^^^^^
  ```

- Warning: `main.nf:101:121`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_phenotype = params.phenotype ? Channel.value([[id: "phenotype"], file(params.phenotype, checkIfExists: true)]) : Channel.empty()
                                                                                                                          ^^^^^^^
  ```

- Warning: `main.nf:103:11`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
          ? Channel.fromList(
            ^^^^^^^
  ```

- Warning: `main.nf:106:11`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
          : Channel.empty()
            ^^^^^^^
  ```

- Warning: `main.nf:107:59`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_mirna = params.mature && params.mirna_expression ? Channel.value([[id: "mirna"], file(params.mirna_expression, checkIfExists: true)]) : Channel.empty()
                                                            ^^^^^^^
  ```

- Warning: `main.nf:107:144`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_mirna = params.mature && params.mirna_expression ? Channel.value([[id: "mirna"], file(params.mirna_expression, checkIfExists: true)]) : Channel.empty()
                                                                                                                                                 ^^^^^^^
  ```

- Warning: `modules/local/circtest/prepare/main.nf:19:5`: Variable was declared but not used

  ```nextflow
      prefix = task.ext.prefix ?: meta.id
      ^^^^^^
  ```

- Warning: `modules/local/ciri/build_list/main.nf:19:5`: Variable was declared but not used

  ```nextflow
      max_shift = task.ext.max_shift ?: 0
      ^^^^^^^^^
  ```

- Warning: `modules/local/combinebeds/reads/main.nf:21:5`: Variable was declared but not used

  ```nextflow
      consider_strand = task.ext.consider_strand ?: false
      ^^^^^^^^^^^^^^^
  ```

- Warning: `modules/local/combinebeds/reads/main.nf:22:5`: Variable was declared but not used

  ```nextflow
      min_tools       = task.ext.min_tools       ?: 2
      ^^^^^^^^^
  ```

- Warning: `modules/local/combinebeds/shifts/main.nf:19:5`: Variable was declared but not used

  ```nextflow
      prefix      = task.ext.prefix      ?: "${meta.id}"
      ^^^^^^
  ```

- Warning: `modules/local/majority_vote/main.nf:22:5`: Variable was declared but not used

  ```nextflow
      min_tools = params.mirna_min_tools
      ^^^^^^^^^
  ```

- Warning: `modules/local/matrix/join_samples/main.nf:21:5`: Variable was declared but not used

  ```nextflow
      metacols = task.ext.metacols ?: "gene_id,gene_name"
      ^^^^^^^^
  ```

- Warning: `modules/local/matrix/join_samples/main.nf:22:5`: Variable was declared but not used

  ```nextflow
      has_header = task.ext.has_header == null ? true : task.ext.has_header
      ^^^^^^^^^^
  ```

- Warning: `modules/local/mirna_targets/main.nf:21:9`: Variable was declared but not used

  ```nextflow
      def args = task.ext.args ?: ''
          ^^^^
  ```

- Warning: `modules/local/tximeta/tximeta/main.nf:22:5`: Variable was declared but not used

  ```nextflow
      prefix = task.ext.prefix ?: meta.id
      ^^^^^^
  ```

- Warning: `modules/nf-core/bowtie/build/main.nf:21:9`: Variable was declared but not used

  ```nextflow
      def args = task.ext.args ?: ''
          ^^^^
  ```

- Warning: `modules/nf-core/bwa/mem/main.nf:31:9`: Variable was declared but not used

  ```nextflow
      def samtools_command = sort_bam ? 'sort' : 'view'
          ^^^^^^^^^^^^^^^^
  ```

- Warning: `modules/nf-core/bwa/mem/main.nf:37:9`: Variable was declared but not used

  ```nextflow
      def reference = fasta && extension=="cram"  ? "--reference ${fasta}" : ""
          ^^^^^^^^^
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

- Warning: `modules/nf-core/csvtk/split/main.nf:24:9`: Variable was declared but not used

  ```nextflow
      def prefix = task.ext.prefix ?: "${meta.id}"
          ^^^^^^
  ```

- Warning: `modules/nf-core/custom/dumpsoftwareversions/main.nf:22:9`: Variable was declared but not used

  ```nextflow
      def args = task.ext.args ?: ''
          ^^^^
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

- Warning: `modules/nf-core/gffread/main.nf:26:103`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
      def extension   = args.contains("-T")       ? 'gtf' : ( ( ['-w', '-x', '-y' ].any { args.contains(it) } ) ? 'fasta' : 'gff3' )
                                                                                                        ^^
  ```

- Warning: `modules/nf-core/gffread/main.nf:30:61`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
      def args_sorted = args.replaceAll(/(.*)(-[wxy])(.*)/) { all, pre, param, post -> "$pre $post $param" }.trim()
                                                              ^^^
  ```

- Warning: `modules/nf-core/gffread/main.nf:49:103`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
      def extension   = args.contains("-T")       ? 'gtf' : ( ( ['-w', '-x', '-y' ].any { args.contains(it) } ) ? 'fasta' : 'gff3' )
                                                                                                        ^^
  ```

- Warning: `modules/nf-core/hisat2/extractsplicesites/main.nf:21:9`: Variable was declared but not used

  ```nextflow
      def args = task.ext.args ?: ''
          ^^^^
  ```

- Warning: `modules/nf-core/star/align/main.nf:46:56`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
      meta.single_end ? [reads].flatten().each{reads1 << it} : reads.eachWithIndex{ v, ix -> ( ix & 1 ? reads2 : reads1) << v }
                                                         ^^
  ```

- Warning: `modules/nf-core/trimgalore/main.nf:47:31`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          args_list.removeAll { it.toLowerCase().contains('_r2 ') }
                                ^^
  ```

- Warning: `nextflow.config:352:129`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          afterText = """${manifest.doi ? "\n* The pipeline\n" : ""}${manifest.doi.tokenize(",").collect { "    https://doi.org/${it.trim().replace('https://doi.org/','')}"}.join("\n")}${manifest.doi ? "\n" : ""}
                                                                                                                                  ^^
  ```

- Warning: `subworkflows/local/annotation.nf:18:19`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_versions = Channel.empty()
                    ^^^^^^^
  ```

- Warning: `subworkflows/local/bsj_detection.nf:44:19`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_versions = Channel.empty()
                    ^^^^^^^
  ```

- Warning: `subworkflows/local/bsj_detection.nf:45:34`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_bsj_bed_per_sample_tool = Channel.empty()
                                   ^^^^^^^
  ```

- Warning: `subworkflows/local/bsj_detection.nf:46:24`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_multiqc_files = Channel.empty()
                         ^^^^^^^
  ```

- Warning: `subworkflows/local/bsj_detection.nf:50:60`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
      def tools_selected = params.tools.split(',').collect { it.trim().toLowerCase() }
                                                             ^^
  ```

- Warning: `subworkflows/local/bsj_detection.nf:51:68`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
      def fli_tools_selected = params.fli_tools.split(',').collect { it.trim().toLowerCase() }
                                                                     ^^
  ```

- Warning: `subworkflows/local/bsj_detection.nf:64:23`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
          ch_star_bam = Channel.empty()
                        ^^^^^^^
  ```

- Warning: `subworkflows/local/bsj_detection.nf:112:33`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
          ch_reads_fixed_length = Channel.empty()
                                  ^^^^^^^
  ```

- Warning: `subworkflows/local/bsj_detection.nf:113:23`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
          ch_ciri_txt = Channel.empty()
                        ^^^^^^^
  ```

- Warning: `subworkflows/local/bsj_detection.nf:114:23`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
          ch_ciri_sam = Channel.empty()
                        ^^^^^^^
  ```

- Warning: `subworkflows/local/bsj_detection.nf:154:24`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
          ch_psirc_bsj = Channel.empty()
                         ^^^^^^^
  ```

- Warning: `subworkflows/local/bsj_detection.nf:266:9`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
          Channel.empty().mix(ch_bsj_bed12_combined).mix(ch_bsj_bed12_per_sample).mix(ch_bsj_bed12_per_sample_tool).mix(ch_bsj_fasta_combined).mix(ch_bsj_fasta_per_sample).mix(ch_bsj_fasta_per_sample_tool).map { _meta, f -> f }.collect(),
          ^^^^^^^
  ```

- Warning: `subworkflows/local/combine_transcriptomes.nf:12:19`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_versions = Channel.empty()
                    ^^^^^^^
  ```

- Warning: `subworkflows/local/combine_transcriptomes.nf:15:101`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          ch_genome_gtf.mix(ch_circ_gtf).map{_meta, gtf -> gtf}.collect().map{[[id: "transcriptome"], it]},
                                                                                                      ^^
  ```

- Warning: `subworkflows/local/detection_tools/circexplorer2.nf:6:5`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
      fasta
      ^^^^^
  ```

- Warning: `subworkflows/local/detection_tools/circexplorer2.nf:8:5`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
      circexplorer2_index
      ^^^^^^^^^^^^^^^^^^^
  ```

- Warning: `subworkflows/local/detection_tools/circexplorer2.nf:11:19`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_versions = Channel.empty()
                    ^^^^^^^
  ```

- Warning: `subworkflows/local/detection_tools/circrna_finder.nf:11:19`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_versions = Channel.empty()
                    ^^^^^^^
  ```

- Warning: `subworkflows/local/detection_tools/circtools.nf:19:19`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_versions = Channel.empty()
                    ^^^^^^^
  ```

- Warning: `subworkflows/local/detection_tools/ciri.nf:17:19`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_versions = Channel.empty()
                    ^^^^^^^
  ```

- Warning: `subworkflows/local/detection_tools/ciri.nf:19:66`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
      def cirifull_enabled = params.fli_tools.split(',').collect { it.trim() }.contains('cirifull')
                                                                   ^^
  ```

- Warning: `subworkflows/local/detection_tools/ciri.nf:77:63`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      reads_fixed_length = cirifull_enabled ? FASTP.out.reads : Channel.empty()
                                                                ^^^^^^^
  ```

- Warning: `subworkflows/local/detection_tools/find_circ.nf:18:19`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_versions = Channel.empty()
                    ^^^^^^^
  ```

- Warning: `subworkflows/local/detection_tools/mapsplice.nf:9:5`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
      fasta
      ^^^^^
  ```

- Warning: `subworkflows/local/detection_tools/mapsplice.nf:12:5`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
      star_junctions
      ^^^^^^^^^^^^^^
  ```

- Warning: `subworkflows/local/detection_tools/mapsplice.nf:13:5`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
      circexplorer2_index
      ^^^^^^^^^^^^^^^^^^^
  ```

- Warning: `subworkflows/local/detection_tools/mapsplice.nf:16:19`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_versions = Channel.empty()
                    ^^^^^^^
  ```

- Warning: `subworkflows/local/detection_tools/psirc.nf:10:19`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_versions = Channel.empty()
                    ^^^^^^^
  ```

- Warning: `subworkflows/local/detection_tools/segemehl.nf:15:19`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_versions = Channel.empty()
                    ^^^^^^^
  ```

- Warning: `subworkflows/local/detection_tools/star2pass.nf:17:19`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_versions = Channel.empty()
                    ^^^^^^^
  ```

- Warning: `subworkflows/local/detection_tools/star2pass.nf:20:93`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
      sjdb = PASS_1.out.tab.map{ _meta, tab -> return tab }.collect().map{[[id: "star_sjdb"], it]}
                                                                                              ^^
  ```

- Warning: `subworkflows/local/fli_detection.nf:24:19`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_versions = Channel.empty()
                    ^^^^^^^
  ```

- Warning: `subworkflows/local/fli_detection.nf:26:16`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_bed12 = Channel.empty()
                 ^^^^^^^
  ```

- Warning: `subworkflows/local/fli_detection.nf:27:16`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_fasta = Channel.empty()
                 ^^^^^^^
  ```

- Warning: `subworkflows/local/fli_detection.nf:29:59`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
      def fli_tools = params.fli_tools.split(',').collect { it.trim() }
                                                            ^^
  ```

- Warning: `subworkflows/local/fli_tools/circtools.nf:16:19`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_versions = Channel.empty()
                    ^^^^^^^
  ```

- Warning: `subworkflows/local/fli_tools/cirifull.nf:21:19`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_versions = Channel.empty()
                    ^^^^^^^
  ```

- Warning: `subworkflows/local/fli_tools/jccirc.nf:14:19`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_versions = Channel.empty()
                    ^^^^^^^
  ```

- Warning: `subworkflows/local/fli_tools/psirc.nf:11:19`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_versions = Channel.empty()
                    ^^^^^^^
  ```

- Warning: `subworkflows/local/longread.nf:9:19`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_versions = Channel.empty()
                    ^^^^^^^
  ```

- Warning: `subworkflows/local/longread_tools/circtools.nf:10:19`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_versions = Channel.empty()
                    ^^^^^^^
  ```

- Warning: `subworkflows/local/mirna/mirna_bindingsites.nf:13:5`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
      circrna_bed12
      ^^^^^^^^^^^^^
  ```

- Warning: `subworkflows/local/mirna/mirna_bindingsites.nf:17:19`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_versions = Channel.empty()
                    ^^^^^^^
  ```

- Warning: `subworkflows/local/mirna/mirna_bindingsites.nf:18:22`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_predictions = Channel.empty()
                       ^^^^^^^
  ```

- Warning: `subworkflows/local/mirna/mirna_bindingsites.nf:33:60`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
      tools_selected = params.mirna_tools.split(',').collect{it.trim().toLowerCase()}
                                                             ^^
  ```

- Warning: `subworkflows/local/mirna/mirna_bindingsites.nf:78:90`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
      MAJORITY_VOTE( ch_predictions.map{_meta, file -> file}.collect().map{[[id: "mirna"], it]} )
                                                                                           ^^
  ```

- Warning: `subworkflows/local/mirna/mirna_bindingsites.nf:109:99`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
      ch_targetscan_meta_formatted = ch_targetscan_meta_formatted.map { [[id: "mature_targetscan"], it] }
                                                                                                    ^^
  ```

- Warning: `subworkflows/local/mirna_prediction.nf:17:5`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
      transcript_counts
      ^^^^^^^^^^^^^^^^^
  ```

- Warning: `subworkflows/local/mirna_prediction.nf:21:19`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_versions = Channel.empty()
                    ^^^^^^^
  ```

- Warning: `subworkflows/local/mirna_prediction.nf:45:98`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          ch_uniq_mirnas = ch_mirna_filtered.map{ _meta, path -> path }.splitCsv( sep: '\t' ).map{ it[0] }.unique().collect()
                                                                                                   ^^
  ```

- Warning: `subworkflows/local/mirna_prediction.nf:73:9`: Variable was declared but not used

  ```nextflow
          ch_correlation_results = COMPUTE_CORRELATIONS.out.correlations
          ^^^^^^^^^^^^^^^^^^^^^^
  ```

- Warning: `subworkflows/local/prepare_genome.nf:23:19`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_versions = Channel.empty()
                    ^^^^^^^
  ```

- Warning: `subworkflows/local/prepare_genome.nf:25:57`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
      detection_tools = params.tools.split(',').collect { it.trim().toLowerCase() }
                                                          ^^
  ```

- Warning: `subworkflows/local/prepare_genome.nf:47:21`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
          ch_bowtie = Channel.value([[id: "bowtie"], file(params.bowtie, checkIfExists: true)])
                      ^^^^^^^
  ```

- Warning: `subworkflows/local/prepare_genome.nf:55:21`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
          ch_bowtie = Channel.empty()
                      ^^^^^^^
  ```

- Warning: `subworkflows/local/prepare_genome.nf:59:22`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
          ch_bowtie2 = Channel.value([[id: "bowtie2"], file(params.bowtie2, checkIfExists: true)])
                       ^^^^^^^
  ```

- Warning: `subworkflows/local/prepare_genome.nf:67:22`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
          ch_bowtie2 = Channel.empty()
                       ^^^^^^^
  ```

- Warning: `subworkflows/local/prepare_genome.nf:71:18`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
          ch_bwa = Channel.value([[id: "bwa"], file(params.bwa, checkIfExists: true)])
                   ^^^^^^^
  ```

- Warning: `subworkflows/local/prepare_genome.nf:79:18`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
          ch_bwa = Channel.empty()
                   ^^^^^^^
  ```

- Warning: `subworkflows/local/prepare_genome.nf:82:30`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_hisat2_splice_sites = Channel.empty()
                               ^^^^^^^
  ```

- Warning: `subworkflows/local/prepare_genome.nf:84:21`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
          ch_hisat2 = Channel.value([[id: "hisat2"], file(params.hisat2, checkIfExists: true)])
                      ^^^^^^^
  ```

- Warning: `subworkflows/local/prepare_genome.nf:96:21`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
          ch_hisat2 = Channel.empty()
                      ^^^^^^^
  ```

- Warning: `subworkflows/local/prepare_genome.nf:100:19`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
          ch_star = Channel.value([[id: "star"], file(params.star, checkIfExists: true)])
                    ^^^^^^^
  ```

- Warning: `subworkflows/local/prepare_genome.nf:108:19`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
          ch_star = Channel.empty()
                    ^^^^^^^
  ```

- Warning: `subworkflows/local/prepare_genome.nf:119:22`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_psirc_index = Channel.empty()
                       ^^^^^^^
  ```

- Warning: `subworkflows/local/quantification.nf:13:5`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
      circ_annotation_gtf
      ^^^^^^^^^^^^^^^^^^^
  ```

- Warning: `subworkflows/local/quantification.nf:22:19`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_versions = Channel.empty()
                    ^^^^^^^
  ```

- Warning: `subworkflows/local/quantification.nf:23:22`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_gene_counts = Channel.empty()
                       ^^^^^^^
  ```

- Warning: `subworkflows/local/quantification.nf:24:22`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_circ_counts = Channel.empty()
                       ^^^^^^^
  ```

- Warning: `subworkflows/local/quantification.nf:25:20`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_ciriquant = Channel.empty()
                     ^^^^^^^
  ```

- Warning: `subworkflows/local/quantification.nf:26:20`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_stringtie = Channel.empty()
                     ^^^^^^^
  ```

- Warning: `subworkflows/local/quantification.nf:27:14`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_rds = Channel.empty()
               ^^^^^^^
  ```

- Warning: `subworkflows/local/quantification.nf:29:71`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
      tools_selected = params.quantification_tools.split(',').collect { it.trim().toLowerCase() }
                                                                        ^^
  ```

- Warning: `subworkflows/local/quantification.nf:67:27`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
          ch_aggregations = Channel.fromList(tools_selected.intersect(aggregations))
                            ^^^^^^^
  ```

- Warning: `subworkflows/local/quantification_tools/ciriquant.nf:17:19`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_versions = Channel.empty()
                    ^^^^^^^
  ```

- Warning: `subworkflows/local/quantification_tools/psirc_quant.nf:25:19`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_versions = Channel.empty()
                    ^^^^^^^
  ```

- Warning: `subworkflows/local/quantification_tools/psirc_quant.nf:38:91`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          QUANT.out.directory.map { _meta, quant -> quant }.collect().map { [[id: "quant"], it] },
                                                                                            ^^
  ```

- Warning: `subworkflows/local/quantification_tools/psirc_quant.nf:59:112`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          TXIMETA_TXIMPORT.out.counts_gene.map { _meta, counts -> counts }.collect().map { [[id: "gene_counts"], it] }
                                                                                                                 ^^
  ```

- Warning: `subworkflows/local/quantification_tools/psirc_quant.nf:64:100`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          TXIMETA_TXIMPORT.out.tpm_gene.map { _meta, tpm -> tpm }.collect().map { [[id: "gene_tpm"], it] }
                                                                                                     ^^
  ```

- Warning: `subworkflows/local/quantification_tools/psirc_quant.nf:69:116`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          TXIMETA_TXIMPORT.out.counts_transcript.map { _meta, counts -> counts }.collect().map { [[id: "tx_counts"], it] }
                                                                                                                     ^^
  ```

- Warning: `subworkflows/local/quantification_tools/psirc_quant.nf:74:104`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          TXIMETA_TXIMPORT.out.tpm_transcript.map { _meta, tpm -> tpm }.collect().map { [[id: "tx_tpm"], it] }
                                                                                                         ^^
  ```

- Warning: `subworkflows/local/quantification_tools/psirc_quant.nf:89:94`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          TXIMETA_TXIMETA.out.se.map { _meta, se -> se }.collect().map { [[id: "experiments"], it] },
                                                                                               ^^
  ```

- Warning: `subworkflows/local/statistical_tests.nf:16:19`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_versions = Channel.empty()
                    ^^^^^^^
  ```

- Warning: `subworkflows/local/utils_nfcore_circrna_pipeline/main.nf:31:5`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
      monochrome_logs   // boolean: Do not use coloured log outputs
      ^^^^^^^^^^^^^^^
  ```

- Warning: `subworkflows/local/utils_nfcore_circrna_pipeline/main.nf:34:5`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
      input             //  string: Path to input samplesheet
      ^^^^^
  ```

- Warning: `subworkflows/local/utils_nfcore_circrna_pipeline/main.nf:38:19`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_versions = Channel.empty()
                    ^^^^^^^
  ```

- Warning: `subworkflows/local/utils_nfcore_circrna_pipeline/main.nf:75:5`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      Channel
      ^^^^^^^
  ```

- Warning: `subworkflows/local/utils_nfcore_circrna_pipeline/main.nf:155:59`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
      def fli_tools = params.fli_tools.split(',').collect { it.trim().toLowerCase() }
                                                            ^^
  ```

- Warning: `subworkflows/local/utils_nfcore_circrna_pipeline/main.nf:156:55`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
      def bsj_tools = params.tools.split(',').collect { it.trim().toLowerCase() }
                                                        ^^
  ```

- Warning: `subworkflows/local/utils_nfcore_circrna_pipeline/main.nf:190:42`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
      def strandedness_ok = metas.collect{ it.strandedness }.unique().size == 1
                                           ^^
  ```

- Warning: `subworkflows/local/utils_nfcore_circrna_pipeline/main.nf:195:59`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
      def fli_tools = params.fli_tools.split(',').collect { it.trim().toLowerCase() }
                                                            ^^
  ```

- Warning: `subworkflows/nf-core/bam_sort_stats_samtools/main.nf:16:19`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_versions = Channel.empty()
                    ^^^^^^^
  ```

- Warning: `subworkflows/nf-core/bam_stats_samtools/main.nf:15:19`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_versions = Channel.empty()
                    ^^^^^^^
  ```

- Warning: `subworkflows/nf-core/fastqc_trimgalore.nf:15:19`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_versions = Channel.empty()
                    ^^^^^^^
  ```

- Warning: `subworkflows/nf-core/fastqc_trimgalore.nf:16:19`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      fastqc_html = Channel.empty()
                    ^^^^^^^
  ```

- Warning: `subworkflows/nf-core/fastqc_trimgalore.nf:17:19`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      fastqc_zip  = Channel.empty()
                    ^^^^^^^
  ```

- Warning: `subworkflows/nf-core/fastqc_trimgalore.nf:25:18`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      trim_html  = Channel.empty()
                   ^^^^^^^
  ```

- Warning: `subworkflows/nf-core/fastqc_trimgalore.nf:26:18`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      trim_zip   = Channel.empty()
                   ^^^^^^^
  ```

- Warning: `subworkflows/nf-core/fastqc_trimgalore.nf:27:18`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      trim_log   = Channel.empty()
                   ^^^^^^^
  ```

- Warning: `subworkflows/nf-core/fastqc_trimgalore.nf:28:5`: Variable was declared but not used

  ```nextflow
      trimgalore_versions = Channel.empty()
      ^^^^^^^^^^^^^^^^^^^
  ```

- Warning: `subworkflows/nf-core/fastqc_trimgalore.nf:28:27`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      trimgalore_versions = Channel.empty()
                            ^^^^^^^
  ```

- Warning: `subworkflows/nf-core/utils_nfcore_pipeline/main.nf:101:98`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      return ch_versions.unique().map { version -> processVersionsFromYAML(version) }.unique().mix(Channel.of(workflowVersionToYAML()))
                                                                                                   ^^^^^^^
  ```

- Warning: `workflows/circrna/main.nf:52:24`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_multiqc_files = Channel.empty()
                         ^^^^^^^
  ```

- Warning: `workflows/circrna/main.nf:91:5`: Variable was declared but not used

  ```nextflow
      hisat2_index        = PREPARE_GENOME.out.hisat2
      ^^^^^^^^^^^^
  ```

- Warning: `workflows/circrna/main.nf:113:89`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          ch_multiqc_files  = ch_multiqc_files.mix(FASTQC_TRIMGALORE.out.trim_zip.collect{it[1]}.ifEmpty([]))
                                                                                          ^^
  ```

- Warning: `workflows/circrna/main.nf:114:89`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          ch_multiqc_files  = ch_multiqc_files.mix(FASTQC_TRIMGALORE.out.trim_log.collect{it[1]}.ifEmpty([]))
                                                                                          ^^
  ```

- Warning: `workflows/circrna/main.nf:232:34`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_multiqc_config          = Channel.fromPath("$projectDir/assets/multiqc_config.yml", checkIfExists: true)
                                   ^^^^^^^
  ```

- Warning: `workflows/circrna/main.nf:233:56`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_multiqc_custom_config = params.multiqc_config ? Channel.fromPath(params.multiqc_config) : Channel.empty()
                                                         ^^^^^^^
  ```

- Warning: `workflows/circrna/main.nf:233:98`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_multiqc_custom_config = params.multiqc_config ? Channel.fromPath(params.multiqc_config) : Channel.empty()
                                                                                                   ^^^^^^^
  ```

- Warning: `workflows/circrna/main.nf:234:56`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_multiqc_logo          = params.multiqc_logo   ? Channel.fromPath(params.multiqc_logo)   : Channel.empty()
                                                         ^^^^^^^
  ```

- Warning: `workflows/circrna/main.nf:234:98`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_multiqc_logo          = params.multiqc_logo   ? Channel.fromPath(params.multiqc_logo)   : Channel.empty()
                                                                                                   ^^^^^^^
  ```

- Warning: `workflows/circrna/main.nf:236:32`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_workflow_summary      = Channel.value(paramsSummaryMultiqc(summary_params))
                                 ^^^^^^^
  ```
