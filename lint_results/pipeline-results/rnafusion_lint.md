# Nextflow lint results

- Generated: 2026-01-16T06:39:12.311765367Z
- Nextflow version: 25.12.0-edge
- Summary: 13 errors, 116 warnings

## :x: Errors

- Error: `modules/nf-core/samtools/sort/main.nf:68:9`: `reference` is already declared

  ```nextflow
      def reference = fasta ? "--reference ${fasta}" : ""
          ^^^^^^^^^
  ```

- Error: `nextflow.config:383:33`: `manifest` is not defined

  ```nextflow
  \033[0;35m  nf-core/rnafusion ${manifest.version}\033[0m
                                  ^^^^^^^^
  ```

- Error: `nextflow.config:386:26`: `manifest` is not defined

  ```nextflow
          afterText = """${manifest.doi ? "\n* The pipeline\n" : ""}${manifest.doi.tokenize(",").collect { "    https://doi.org/${it.trim().replace('https://doi.org/','')}"}.join("\n")}${manifest.doi ? "\n" : ""}
                           ^^^^^^^^
  ```

- Error: `nextflow.config:386:69`: `manifest` is not defined

  ```nextflow
          afterText = """${manifest.doi ? "\n* The pipeline\n" : ""}${manifest.doi.tokenize(",").collect { "    https://doi.org/${it.trim().replace('https://doi.org/','')}"}.join("\n")}${manifest.doi ? "\n" : ""}
                                                                      ^^^^^^^^
  ```

- Error: `nextflow.config:386:186`: `manifest` is not defined

  ```nextflow
          afterText = """${manifest.doi ? "\n* The pipeline\n" : ""}${manifest.doi.tokenize(",").collect { "    https://doi.org/${it.trim().replace('https://doi.org/','')}"}.join("\n")}${manifest.doi ? "\n" : ""}
                                                                                                                                                                                           ^^^^^^^^
  ```

- Error: `nextflow.config:395:22`: `validation` is not defined

  ```nextflow
          beforeText = validation.help.beforeText
                       ^^^^^^^^^^
  ```

- Error: `nextflow.config:396:21`: `validation` is not defined

  ```nextflow
          afterText = validation.help.afterText
                      ^^^^^^^^^^
  ```

- Error: `tests/nextflow.config:27:38`: `pipelines_testdata_base_path` is not defined

  ```nextflow
      dfam_hmm                    = "${pipelines_testdata_base_path}/testdata/human/test_starfusion_dfam.hmm"
                                       ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  ```

- Error: `tests/nextflow.config:28:38`: `pipelines_testdata_base_path` is not defined

  ```nextflow
      dfam_h3f                    = "${pipelines_testdata_base_path}/testdata/human/test_starfusion_dfam.hmm.h3f"
                                       ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  ```

- Error: `tests/nextflow.config:29:38`: `pipelines_testdata_base_path` is not defined

  ```nextflow
      dfam_h3i                    = "${pipelines_testdata_base_path}/testdata/human/test_starfusion_dfam.hmm.h3i"
                                       ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  ```

- Error: `tests/nextflow.config:30:38`: `pipelines_testdata_base_path` is not defined

  ```nextflow
      dfam_h3m                    = "${pipelines_testdata_base_path}/testdata/human/test_starfusion_dfam.hmm.h3m"
                                       ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  ```

- Error: `tests/nextflow.config:31:38`: `pipelines_testdata_base_path` is not defined

  ```nextflow
      dfam_h3p                    = "${pipelines_testdata_base_path}/testdata/human/test_starfusion_dfam.hmm.h3p"
                                       ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  ```

- Error: `tests/nextflow.config:32:38`: `pipelines_testdata_base_path` is not defined

  ```nextflow
      pfam_file                   = "${pipelines_testdata_base_path}/testdata/human/Pfam-A.hmm.gz"
                                       ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  ```

## :warning: Warnings

- Warning: `modules/nf-core/agat/convertgff2bed/main.nf:36:9`: Variable was declared but not used

  ```nextflow
      def args   = task.ext.args   ?: ''
          ^^^^
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

- Warning: `modules/nf-core/ctatsplicing/prepgenomelib/main.nf:23:9`: Variable was declared but not used

  ```nextflow
      def args = task.ext.args ?: ''
          ^^^^
  ```

- Warning: `modules/nf-core/ctatsplicing/prepgenomelib/main.nf:24:9`: Variable was declared but not used

  ```nextflow
      def prefix = task.ext.prefix ?: "${meta.id}"
          ^^^^^^
  ```

- Warning: `modules/nf-core/ctatsplicing/prepgenomelib/main.nf:38:9`: Variable was declared but not used

  ```nextflow
      def args = task.ext.args ?: ''
          ^^^^
  ```

- Warning: `modules/nf-core/ctatsplicing/prepgenomelib/main.nf:39:9`: Variable was declared but not used

  ```nextflow
      def prefix = task.ext.prefix ?: "${meta.id}"
          ^^^^^^
  ```

- Warning: `modules/nf-core/gatk4/markduplicates/main.nf:33:47`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
      def input_list = bam.collect { "--INPUT ${it}" }.join(' ')
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

- Warning: `modules/nf-core/salmon/quant/main.nf:34:58`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
      meta.single_end ? [reads].flatten().each { reads1 << it } : reads.eachWithIndex { v, ix -> (ix & 1 ? reads2 : reads1) << v }
                                                           ^^
  ```

- Warning: `modules/nf-core/samtools/sort/main.nf:68:9`: Variable was declared but not used

  ```nextflow
      def reference = fasta ? "--reference ${fasta}" : ""
          ^^^^^^^^^
  ```

- Warning: `modules/nf-core/star/align/main.nf:46:56`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
      meta.single_end ? [reads].flatten().each{reads1 << it} : reads.eachWithIndex{ v, ix -> ( ix & 1 ? reads2 : reads1) << v }
                                                         ^^
  ```

- Warning: `nextflow.config:386:129`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          afterText = """${manifest.doi ? "\n* The pipeline\n" : ""}${manifest.doi.tokenize(",").collect { "    https://doi.org/${it.trim().replace('https://doi.org/','')}"}.join("\n")}${manifest.doi ? "\n" : ""}
                                                                                                                                  ^^
  ```

- Warning: `subworkflows/local/build_references/main.nf:40:23`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      def ch_versions = Channel.empty()
                        ^^^^^^^
  ```

- Warning: `subworkflows/local/build_references/main.nf:42:20`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      def ch_fasta = Channel.empty()
                     ^^^^^^^
  ```

- Warning: `subworkflows/local/build_references/main.nf:43:20`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      def ch_gtf   = Channel.empty()
                     ^^^^^^^
  ```

- Warning: `subworkflows/local/build_references/main.nf:50:20`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
          ch_fasta = Channel.fromPath(params.fasta).map { that -> [[id:that.Name], that] }
                     ^^^^^^^
  ```

- Warning: `subworkflows/local/build_references/main.nf:51:18`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
          ch_gtf = Channel.fromPath(params.gtf).map { that -> [[id:that.Name], that] }
                   ^^^^^^^
  ```

- Warning: `subworkflows/local/build_references/main.nf:54:18`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      def ch_fai = Channel.empty()
                   ^^^^^^^
  ```

- Warning: `subworkflows/local/build_references/main.nf:60:18`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
          ch_fai = Channel.fromPath(params.fai).map { that -> [[id:that.Name], that] }
                   ^^^^^^^
  ```

- Warning: `subworkflows/local/build_references/main.nf:63:24`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      def ch_hgnc_date = Channel.empty()
                         ^^^^^^^
  ```

- Warning: `subworkflows/local/build_references/main.nf:64:24`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      def ch_hgnc_ref  = Channel.empty()
                         ^^^^^^^
  ```

- Warning: `subworkflows/local/build_references/main.nf:74:27`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
              ch_hgnc_ref = Channel.fromPath(params.hgnc_ref).map { that -> [[id:that.Name], that] }
                            ^^^^^^^
  ```

- Warning: `subworkflows/local/build_references/main.nf:75:28`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
              ch_hgnc_date = Channel.fromPath(params.hgnc_date).map { that -> [[id:that.Name], that] }
                             ^^^^^^^
  ```

- Warning: `subworkflows/local/build_references/main.nf:79:28`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      def ch_rrna_interval = Channel.empty()
                             ^^^^^^^
  ```

- Warning: `subworkflows/local/build_references/main.nf:96:32`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
              ch_rrna_interval = Channel.fromPath(params.rrna_intervals).map { that -> [[id:that.Name], that] }
                                 ^^^^^^^
  ```

- Warning: `subworkflows/local/build_references/main.nf:100:22`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      def ch_refflat = Channel.empty()
                       ^^^^^^^
  ```

- Warning: `subworkflows/local/build_references/main.nf:107:26`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
              ch_refflat = Channel.fromPath(params.refflat).map { that -> [[id:that.Name], that] }
                           ^^^^^^^
  ```

- Warning: `subworkflows/local/build_references/main.nf:111:27`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      def ch_salmon_index = Channel.empty()
                            ^^^^^^^
  ```

- Warning: `subworkflows/local/build_references/main.nf:122:35`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
                  ch_salmon_index = Channel.fromPath(params.salmon_index)
                                    ^^^^^^^
  ```

- Warning: `subworkflows/local/build_references/main.nf:127:28`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      def ch_starindex_ref = Channel.empty()
                             ^^^^^^^
  ```

- Warning: `subworkflows/local/build_references/main.nf:135:32`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
              ch_starindex_ref = Channel.fromPath(params.starindex_ref).map { that -> [[id:that.Name], that] }
                                 ^^^^^^^
  ```

- Warning: `subworkflows/local/build_references/main.nf:139:71`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      def ch_arriba_ref_blacklist       = params.arriba_ref_blacklist ? Channel.fromPath(params.arriba_ref_blacklist) : Channel.empty()
                                                                        ^^^^^^^
  ```

- Warning: `subworkflows/local/build_references/main.nf:139:119`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      def ch_arriba_ref_blacklist       = params.arriba_ref_blacklist ? Channel.fromPath(params.arriba_ref_blacklist) : Channel.empty()
                                                                                                                        ^^^^^^^
  ```

- Warning: `subworkflows/local/build_references/main.nf:140:71`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      def ch_arriba_ref_cytobands       = params.arriba_ref_cytobands ? Channel.fromPath(params.arriba_ref_cytobands) : Channel.empty()
                                                                        ^^^^^^^
  ```

- Warning: `subworkflows/local/build_references/main.nf:140:119`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      def ch_arriba_ref_cytobands       = params.arriba_ref_cytobands ? Channel.fromPath(params.arriba_ref_cytobands) : Channel.empty()
                                                                                                                        ^^^^^^^
  ```

- Warning: `subworkflows/local/build_references/main.nf:141:75`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      def ch_arriba_ref_known_fusions   = params.arriba_ref_known_fusions ? Channel.fromPath(params.arriba_ref_known_fusions) : Channel.empty()
                                                                            ^^^^^^^
  ```

- Warning: `subworkflows/local/build_references/main.nf:141:127`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      def ch_arriba_ref_known_fusions   = params.arriba_ref_known_fusions ? Channel.fromPath(params.arriba_ref_known_fusions) : Channel.empty()
                                                                                                                                ^^^^^^^
  ```

- Warning: `subworkflows/local/build_references/main.nf:142:77`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      def ch_arriba_ref_protein_domains = params.arriba_ref_protein_domains ? Channel.fromPath(params.arriba_ref_protein_domains) : Channel.empty()
                                                                              ^^^^^^^
  ```

- Warning: `subworkflows/local/build_references/main.nf:142:131`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      def ch_arriba_ref_protein_domains = params.arriba_ref_protein_domains ? Channel.fromPath(params.arriba_ref_protein_domains) : Channel.empty()
                                                                                                                                    ^^^^^^^
  ```

- Warning: `subworkflows/local/build_references/main.nf:144:59`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      def ch_fusioncatcher_ref = params.fusioncatcher_ref ? Channel.fromPath(params.fusioncatcher_ref).map { it -> [[id:it.name], it] } : Channel.empty()
                                                            ^^^^^^^
  ```

- Warning: `subworkflows/local/build_references/main.nf:144:137`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      def ch_fusioncatcher_ref = params.fusioncatcher_ref ? Channel.fromPath(params.fusioncatcher_ref).map { it -> [[id:it.name], it] } : Channel.empty()
                                                                                                                                          ^^^^^^^
  ```

- Warning: `subworkflows/local/build_references/main.nf:146:29`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      def ch_starfusion_ref = Channel.empty()
                              ^^^^^^^
  ```

- Warning: `subworkflows/local/build_references/main.nf:154:29`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
                  pfam_file = Channel.fromPath(params.pfam_file, checkIfExists: true)
                              ^^^^^^^
  ```

- Warning: `subworkflows/local/build_references/main.nf:160:28`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
                  dfam_hmm = Channel.fromPath(params.dfam_hmm, checkIfExists: true)
                             ^^^^^^^
  ```

- Warning: `subworkflows/local/build_references/main.nf:161:28`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
                  dfam_h3f = Channel.fromPath(params.dfam_h3f, checkIfExists: true)
                             ^^^^^^^
  ```

- Warning: `subworkflows/local/build_references/main.nf:162:28`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
                  dfam_h3i = Channel.fromPath(params.dfam_h3i, checkIfExists: true)
                             ^^^^^^^
  ```

- Warning: `subworkflows/local/build_references/main.nf:163:28`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
                  dfam_h3m = Channel.fromPath(params.dfam_h3m, checkIfExists: true)
                             ^^^^^^^
  ```

- Warning: `subworkflows/local/build_references/main.nf:164:28`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
                  dfam_h3p = Channel.fromPath(params.dfam_h3p, checkIfExists: true)
                             ^^^^^^^
  ```

- Warning: `subworkflows/local/build_references/main.nf:192:33`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
              ch_starfusion_ref = Channel.fromPath(params.starfusion_ref).map { it -> [[id:it.name], it] }
                                  ^^^^^^^
  ```

- Warning: `subworkflows/local/build_references/main.nf:196:31`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      def ch_fusionreport_ref = Channel.empty()
                                ^^^^^^^
  ```

- Warning: `subworkflows/local/build_references/main.nf:206:35`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
              ch_fusionreport_ref = Channel.fromPath(params.fusionreport_ref).map { that -> [[id:that.Name], that] }
                                    ^^^^^^^
  ```

- Warning: `subworkflows/local/fusioncatcher_workflow/main.nf:17:25`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
          ch_versions   = Channel.empty()
                          ^^^^^^^
  ```

- Warning: `subworkflows/local/fusioncatcher_workflow/main.nf:21:54`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
              ch_fusioncatcher_fusions = reads.combine(Channel.value(file(fusioncatcher_fusions, checkIfExists:true)))
                                                       ^^^^^^^
  ```

- Warning: `subworkflows/local/fusioninspector_workflow/main.nf:27:23`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
          ch_versions = Channel.empty()
                        ^^^^^^^
  ```

- Warning: `subworkflows/local/fusioninspector_workflow/main.nf:28:35`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
          ch_arriba_visualisation = Channel.empty()
                                    ^^^^^^^
  ```

- Warning: `subworkflows/local/fusioninspector_workflow/main.nf:33:51`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
              ch_whitelist = ch_fusion_list.combine(Channel.value(file(whitelist, checkIfExists:true)))
                                                    ^^^^^^^
  ```

- Warning: `subworkflows/local/qc_workflow/main.nf:18:23`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
          ch_versions = Channel.empty()
                        ^^^^^^^
  ```

- Warning: `subworkflows/local/utils_nfcore_rnafusion_pipeline/main.nf:36:19`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_versions = Channel.empty()
                    ^^^^^^^
  ```

- Warning: `subworkflows/local/utils_nfcore_rnafusion_pipeline/main.nf:73:5`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      Channel
      ^^^^^^^
  ```

- Warning: `subworkflows/local/utils_nfcore_rnafusion_pipeline/main.nf:170:56`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          def setDfamParams = dfamParams.findAll { params[it] }
                                                         ^^
  ```

- Warning: `subworkflows/local/utils_nfcore_rnafusion_pipeline/main.nf:228:42`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
      def strandedness_ok = metas.collect{ it.strandedness }.unique().size == 1
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

- Warning: `subworkflows/nf-core/bam_stringtie_merge/main.nf:12:25`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_versions       = Channel.empty()
                          ^^^^^^^
  ```

- Warning: `subworkflows/nf-core/bam_stringtie_merge/main.nf:13:25`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_stringtie_gtfs = Channel.empty()
                          ^^^^^^^
  ```

- Warning: `subworkflows/nf-core/bam_stringtie_merge/main.nf:22:16`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          .map { it[1] }
                 ^^
  ```

- Warning: `subworkflows/nf-core/fastq_align_star/main.nf:20:19`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_versions = Channel.empty()
                    ^^^^^^^
  ```

- Warning: `subworkflows/nf-core/fastq_fastqc_umitools_fastp/main.nf:33:22`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
      catch (Exception ex) {
                       ^^
  ```

- Warning: `subworkflows/nf-core/fastq_fastqc_umitools_fastp/main.nf:52:19`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_versions = Channel.empty()
                    ^^^^^^^
  ```

- Warning: `subworkflows/nf-core/fastq_fastqc_umitools_fastp/main.nf:53:23`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      fastqc_raw_html = Channel.empty()
                        ^^^^^^^
  ```

- Warning: `subworkflows/nf-core/fastq_fastqc_umitools_fastp/main.nf:54:22`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      fastqc_raw_zip = Channel.empty()
                       ^^^^^^^
  ```

- Warning: `subworkflows/nf-core/fastq_fastqc_umitools_fastp/main.nf:55:15`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      umi_log = Channel.empty()
                ^^^^^^^
  ```

- Warning: `subworkflows/nf-core/fastq_fastqc_umitools_fastp/main.nf:56:17`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      trim_json = Channel.empty()
                  ^^^^^^^
  ```

- Warning: `subworkflows/nf-core/fastq_fastqc_umitools_fastp/main.nf:57:17`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      trim_html = Channel.empty()
                  ^^^^^^^
  ```

- Warning: `subworkflows/nf-core/fastq_fastqc_umitools_fastp/main.nf:58:16`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      trim_log = Channel.empty()
                 ^^^^^^^
  ```

- Warning: `subworkflows/nf-core/fastq_fastqc_umitools_fastp/main.nf:59:23`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      trim_reads_fail = Channel.empty()
                        ^^^^^^^
  ```

- Warning: `subworkflows/nf-core/fastq_fastqc_umitools_fastp/main.nf:60:25`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      trim_reads_merged = Channel.empty()
                          ^^^^^^^
  ```

- Warning: `subworkflows/nf-core/fastq_fastqc_umitools_fastp/main.nf:61:24`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      fastqc_trim_html = Channel.empty()
                         ^^^^^^^
  ```

- Warning: `subworkflows/nf-core/fastq_fastqc_umitools_fastp/main.nf:62:23`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      fastqc_trim_zip = Channel.empty()
                        ^^^^^^^
  ```

- Warning: `subworkflows/nf-core/fastq_fastqc_umitools_fastp/main.nf:63:23`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      trim_read_count = Channel.empty()
                        ^^^^^^^
  ```

- Warning: `subworkflows/nf-core/fastq_fastqc_umitools_fastp/main.nf:64:19`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      adapter_seq = Channel.empty()
                    ^^^^^^^
  ```

- Warning: `subworkflows/nf-core/utils_nfcore_pipeline/main.nf:101:98`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      return ch_versions.unique().map { version -> processVersionsFromYAML(version) }.unique().mix(Channel.of(workflowVersionToYAML()))
                                                                                                   ^^^^^^^
  ```

- Warning: `workflows/rnafusion.nf:47:23`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      def ch_versions = Channel.empty()
                        ^^^^^^^
  ```

- Warning: `workflows/rnafusion.nf:48:28`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      def ch_multiqc_files = Channel.empty()
                             ^^^^^^^
  ```

- Warning: `workflows/rnafusion.nf:137:24`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
          def ch_reads = Channel.empty()
                         ^^^^^^^
  ```

- Warning: `workflows/rnafusion.nf:140:55`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
          def ch_adapter_fasta = params.adapter_fasta ? Channel.fromPath(params.adapter_fasta).collect() : []
                                                        ^^^^^^^
  ```

- Warning: `workflows/rnafusion.nf:171:29`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
          ch_sbwf_fastp_mqc = Channel.empty()
                              ^^^^^^^
  ```

- Warning: `workflows/rnafusion.nf:172:71`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
              .mix(FASTQ_FASTQC_UMITOOLS_FASTP.out.fastqc_raw_zip.map { it[1] })
                                                                        ^^
  ```

- Warning: `workflows/rnafusion.nf:173:72`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
              .mix(FASTQ_FASTQC_UMITOOLS_FASTP.out.fastqc_trim_zip.map { it[1] })
                                                                         ^^
  ```

- Warning: `workflows/rnafusion.nf:174:66`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
              .mix(FASTQ_FASTQC_UMITOOLS_FASTP.out.trim_html.map { it[1] })
                                                                   ^^
  ```

- Warning: `workflows/rnafusion.nf:175:66`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
              .mix(FASTQ_FASTQC_UMITOOLS_FASTP.out.trim_json.map { it[1] })
                                                                   ^^
  ```

- Warning: `workflows/rnafusion.nf:193:88`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
              ch_multiqc_files = ch_multiqc_files.mix(SALMON_QUANT.out.json_info.collect{it[1]})
                                                                                         ^^
  ```

- Warning: `workflows/rnafusion.nf:227:99`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
              ch_multiqc_files        = ch_multiqc_files.mix(FASTQ_ALIGN_STAR.out.log_final.collect{it[1]}.ifEmpty([]))
                                                                                                    ^^
  ```

- Warning: `workflows/rnafusion.nf:228:100`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
              ch_multiqc_files        = ch_multiqc_files.mix(FASTQ_ALIGN_STAR.out.gene_count.collect{it[1]}.ifEmpty([]))
                                                                                                     ^^
  ```

- Warning: `workflows/rnafusion.nf:262:30`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
                      .combine(Channel.value(file(params.arriba_fusions, checkIfExists: true)))
                               ^^^^^^^
  ```

- Warning: `workflows/rnafusion.nf:338:30`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
          def ch_fusion_list = Channel.empty()
                               ^^^^^^^
  ```

- Warning: `workflows/rnafusion.nf:339:39`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
          def ch_fusion_list_filtered = Channel.empty()
                                        ^^^^^^^
  ```

- Warning: `workflows/rnafusion.nf:340:38`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
          def ch_fusionreport_report = Channel.empty()
                                       ^^^^^^^
  ```

- Warning: `workflows/rnafusion.nf:341:35`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
          def ch_fusionreport_csv = Channel.empty()
                                    ^^^^^^^
  ```

- Warning: `workflows/rnafusion.nf:396:114`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
              ch_multiqc_files = ch_multiqc_files.mix(FUSIONINSPECTOR_WORKFLOW.out.ch_arriba_visualisation.collect{it[1]}.ifEmpty([]))
                                                                                                                   ^^
  ```

- Warning: `workflows/rnafusion.nf:412:92`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
              ch_multiqc_files = ch_multiqc_files.mix(QC_WORKFLOW.out.rnaseq_metrics.collect{it[1]})
                                                                                             ^^
  ```

- Warning: `workflows/rnafusion.nf:413:95`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
              ch_multiqc_files = ch_multiqc_files.mix(QC_WORKFLOW.out.duplicate_metrics.collect{it[1]})
                                                                                                ^^
  ```

- Warning: `workflows/rnafusion.nf:414:96`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
              ch_multiqc_files = ch_multiqc_files.mix(QC_WORKFLOW.out.insertsize_metrics.collect{it[1]})
                                                                                                 ^^
  ```

- Warning: `workflows/rnafusion.nf:433:29`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      def ch_multiqc_output = Channel.empty()
                              ^^^^^^^
  ```

- Warning: `workflows/rnafusion.nf:435:36`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
          ch_multiqc_config        = Channel.fromPath(
                                     ^^^^^^^
  ```

- Warning: `workflows/rnafusion.nf:438:13`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
              Channel.fromPath(params.multiqc_config, checkIfExists: true) :
              ^^^^^^^
  ```

- Warning: `workflows/rnafusion.nf:439:13`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
              Channel.empty()
              ^^^^^^^
  ```

- Warning: `workflows/rnafusion.nf:441:13`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
              Channel.fromPath(params.multiqc_logo, checkIfExists: true) :
              ^^^^^^^
  ```

- Warning: `workflows/rnafusion.nf:442:13`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
              Channel.empty()
              ^^^^^^^
  ```

- Warning: `workflows/rnafusion.nf:446:31`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
          ch_workflow_summary = Channel.value(paramsSummaryMultiqc(summary_params))
                                ^^^^^^^
  ```

- Warning: `workflows/rnafusion.nf:452:49`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
          ch_methods_description                = Channel.value(
                                                  ^^^^^^^
  ```
