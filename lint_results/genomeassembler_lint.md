# Nextflow lint results

- Generated: 2026-01-14T09:18:14.380548474Z
- Nextflow version: 25.12.0-edge
- Summary: 16 errors, 92 warnings

## :x: Errors

- Error: `modules/local/genomescope/main.nf:16:30`: `est_hap_len` is not defined

  ```nextflow
          tuple val(meta), env(est_hap_len)           , emit: estimated_hap_len
                               ^^^^^^^^^^^
  ```

- Error: `modules/local/nanoq/main.nf:16:26`: `median` is not defined

  ```nextflow
      tuple val(meta), env(median), emit: median_length
                           ^^^^^^
  ```

- Error: `nextflow.config:289:1`: Variable declarations cannot be mixed with config statements

  ```nextflow
  def trace_timestamp = new java.util.Date().format( 'yyyy-MM-dd_HH-mm-ss')
  ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  ```

- Error: `nextflow.config:292:68`: `trace_timestamp` is not defined

  ```nextflow
      file    = "${params.outdir}/pipeline_info/execution_timeline_${trace_timestamp}.html"
                                                                     ^^^^^^^^^^^^^^^
  ```

- Error: `nextflow.config:296:66`: `trace_timestamp` is not defined

  ```nextflow
      file    = "${params.outdir}/pipeline_info/execution_report_${trace_timestamp}.html"
                                                                   ^^^^^^^^^^^^^^^
  ```

- Error: `nextflow.config:300:65`: `trace_timestamp` is not defined

  ```nextflow
      file    = "${params.outdir}/pipeline_info/execution_trace_${trace_timestamp}.txt"
                                                                  ^^^^^^^^^^^^^^^
  ```

- Error: `nextflow.config:304:62`: `trace_timestamp` is not defined

  ```nextflow
      file    = "${params.outdir}/pipeline_info/pipeline_dag_${trace_timestamp}.html"
                                                               ^^^^^^^^^^^^^^^
  ```

- Error: `nextflow.config:338:34`: `manifest` is not defined

  ```nextflow
          command = "nextflow run $manifest.name -profile <docker/singularity/.../institute> --input samplesheet.csv --outdir <OUTDIR>"
                                   ^^^^^^^^
  ```

- Error: `nextflow.config:348:15`: `manifest` is not defined

  ```nextflow
  \033[0;35m  ${manifest.name} ${manifest.version}\033[0m
                ^^^^^^^^
  ```

- Error: `nextflow.config:348:32`: `manifest` is not defined

  ```nextflow
  \033[0;35m  ${manifest.name} ${manifest.version}\033[0m
                                 ^^^^^^^^
  ```

- Error: `nextflow.config:351:26`: `manifest` is not defined

  ```nextflow
          afterText = """${manifest.doi ? "* The pipeline\n" : ""}${manifest.doi.tokenize(",").collect { "  https://doi.org/${it.trim().replace('https://doi.org/','')}"}.join("\n")}${manifest.doi ? "\n" : ""}
                           ^^^^^^^^
  ```

- Error: `nextflow.config:351:67`: `manifest` is not defined

  ```nextflow
          afterText = """${manifest.doi ? "* The pipeline\n" : ""}${manifest.doi.tokenize(",").collect { "  https://doi.org/${it.trim().replace('https://doi.org/','')}"}.join("\n")}${manifest.doi ? "\n" : ""}
                                                                    ^^^^^^^^
  ```

- Error: `nextflow.config:351:182`: `manifest` is not defined

  ```nextflow
          afterText = """${manifest.doi ? "* The pipeline\n" : ""}${manifest.doi.tokenize(",").collect { "  https://doi.org/${it.trim().replace('https://doi.org/','')}"}.join("\n")}${manifest.doi ? "\n" : ""}
                                                                                                                                                                                       ^^^^^^^^
  ```

- Error: `nextflow.config:356:26`: `manifest` is not defined

  ```nextflow
      https://github.com/${manifest.name}/blob/master/CITATIONS.md
                           ^^^^^^^^
  ```

- Error: `nextflow.config:360:22`: `validation` is not defined

  ```nextflow
          beforeText = validation.help.beforeText
                       ^^^^^^^^^^
  ```

- Error: `nextflow.config:361:21`: `validation` is not defined

  ```nextflow
          afterText = validation.help.afterText
                      ^^^^^^^^^^
  ```

## :warning: Warnings

- Warning: `modules/nf-core/hifiasm/main.nf:36:75`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
      def long_reads_sorted = long_reads instanceof List ? long_reads.sort{ it.name } : long_reads
                                                                            ^^
  ```

- Warning: `modules/nf-core/hifiasm/main.nf:37:69`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
      def ul_reads_sorted = ul_reads instanceof List ? ul_reads.sort{ it.name } : ul_reads
                                                                      ^^
  ```

- Warning: `modules/nf-core/meryl/unionsum/main.nf:40:9`: Variable was declared but not used

  ```nextflow
      def args = task.ext.args ?: ''
          ^^^^
  ```

- Warning: `modules/nf-core/minimap2/align/main.nf:66:9`: Variable was declared but not used

  ```nextflow
      def target = reference ?: (bam_input ? error("BAM input requires reference") : reads)
          ^^^^^^
  ```

- Warning: `modules/nf-core/trimgalore/main.nf:47:31`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          args_list.removeAll { it.toLowerCase().contains('_r2 ') }
                                ^^
  ```

- Warning: `nextflow.config:351:125`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          afterText = """${manifest.doi ? "* The pipeline\n" : ""}${manifest.doi.tokenize(",").collect { "  https://doi.org/${it.trim().replace('https://doi.org/','')}"}.join("\n")}${manifest.doi ? "\n" : ""}
                                                                                                                              ^^
  ```

- Warning: `subworkflows/local/assemble/main.nf:22:5`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      Channel.empty().set { ch_refs }
      ^^^^^^^
  ```

- Warning: `subworkflows/local/assemble/main.nf:23:5`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      Channel.empty().set { ch_ref_bam }
      ^^^^^^^
  ```

- Warning: `subworkflows/local/assemble/main.nf:24:5`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      Channel.empty().set { ch_assembly_bam }
      ^^^^^^^
  ```

- Warning: `subworkflows/local/assemble/main.nf:25:5`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      Channel.empty().set { ch_assembly }
      ^^^^^^^
  ```

- Warning: `subworkflows/local/assemble/main.nf:26:5`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      Channel.empty().set { flye_inputs }
      ^^^^^^^
  ```

- Warning: `subworkflows/local/assemble/main.nf:27:5`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      Channel.empty().set { hifiasm_inputs }
      ^^^^^^^
  ```

- Warning: `subworkflows/local/assemble/main.nf:28:5`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      Channel.empty().set { longreads }
      ^^^^^^^
  ```

- Warning: `subworkflows/local/assemble/main.nf:29:5`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      Channel.empty().set { ch_versions }
      ^^^^^^^
  ```

- Warning: `subworkflows/local/assemble/main.nf:45:13`: Variable was declared but not used

  ```nextflow
          def hifi_only = params.hifi && !params.ont ? true : false
              ^^^^^^^^^
  ```

- Warning: `subworkflows/local/assemble/main.nf:171:9`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
          Channel.empty().set { ch_ref_bam }
          ^^^^^^^
  ```

- Warning: `subworkflows/local/bam_sort_stat/main.nf:20:5`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      Channel.empty().set { ch_versions }
      ^^^^^^^
  ```

- Warning: `subworkflows/local/hifi/main.nf:9:5`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      Channel.empty().set { ch_versions }
      ^^^^^^^
  ```

- Warning: `subworkflows/local/jellyfish/main.nf:13:5`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      Channel.empty().set { genomescope_in }
      ^^^^^^^
  ```

- Warning: `subworkflows/local/jellyfish/main.nf:14:5`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      Channel.empty().set { ch_versions }
      ^^^^^^^
  ```

- Warning: `subworkflows/local/liftoff/main.nf:9:5`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      Channel.empty().set { ch_versions }
      ^^^^^^^
  ```

- Warning: `subworkflows/local/mapping/map_sr/main.nf:10:5`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      Channel.empty().set { ch_versions }
      ^^^^^^^
  ```

- Warning: `subworkflows/local/mapping/map_to_assembly/main.nf:10:5`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      Channel.empty().set { ch_versions }
      ^^^^^^^
  ```

- Warning: `subworkflows/local/mapping/map_to_ref/main.nf:10:5`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      Channel.empty().set { ch_versions }
      ^^^^^^^
  ```

- Warning: `subworkflows/local/ont/main.nf:10:5`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      Channel.empty().set { ch_versions }
      ^^^^^^^
  ```

- Warning: `subworkflows/local/ont/main.nf:11:5`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      Channel.of([[],[]])
      ^^^^^^^
  ```

- Warning: `subworkflows/local/polishing/main.nf:16:5`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      Channel.empty().set { ch_versions }
      ^^^^^^^
  ```

- Warning: `subworkflows/local/polishing/main.nf:17:5`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      Channel.empty().set { polish_busco_reports }
      ^^^^^^^
  ```

- Warning: `subworkflows/local/polishing/main.nf:18:5`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      Channel.empty().set { polish_quast_reports }
      ^^^^^^^
  ```

- Warning: `subworkflows/local/polishing/main.nf:19:5`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      Channel.empty().set { polish_merqury_reports }
      ^^^^^^^
  ```

- Warning: `subworkflows/local/polishing/medaka/polish_medaka/main.nf:14:5`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      Channel.empty().set { ch_versions }
      ^^^^^^^
  ```

- Warning: `subworkflows/local/polishing/medaka/polish_medaka/main.nf:15:5`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      Channel.empty().set { quast_out }
      ^^^^^^^
  ```

- Warning: `subworkflows/local/polishing/medaka/polish_medaka/main.nf:15:27`: Variable was declared but not used

  ```nextflow
      Channel.empty().set { quast_out }
                            ^^^^^^^^^
  ```

- Warning: `subworkflows/local/polishing/medaka/polish_medaka/main.nf:16:5`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      Channel.empty().set { busco_out }
      ^^^^^^^
  ```

- Warning: `subworkflows/local/polishing/medaka/polish_medaka/main.nf:16:27`: Variable was declared but not used

  ```nextflow
      Channel.empty().set { busco_out }
                            ^^^^^^^^^
  ```

- Warning: `subworkflows/local/polishing/medaka/polish_medaka/main.nf:17:5`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      Channel.empty().set { merqury_report_files }
      ^^^^^^^
  ```

- Warning: `subworkflows/local/polishing/medaka/polish_medaka/main.nf:17:27`: Variable was declared but not used

  ```nextflow
      Channel.empty().set { merqury_report_files }
                            ^^^^^^^^^^^^^^^^^^^^
  ```

- Warning: `subworkflows/local/polishing/pilon/polish_pilon/main.nf:16:5`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      Channel.empty().set { ch_versions }
      ^^^^^^^
  ```

- Warning: `subworkflows/local/prepare_hifi/main.nf:9:5`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      Channel.empty().set { ch_versions }
      ^^^^^^^
  ```

- Warning: `subworkflows/local/prepare_ont/chop/main.nf:8:5`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      Channel.empty().set { chopped_reads }
      ^^^^^^^
  ```

- Warning: `subworkflows/local/prepare_ont/chop/main.nf:9:5`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      Channel.empty().set { ch_versions }
      ^^^^^^^
  ```

- Warning: `subworkflows/local/prepare_ont/collect/main.nf:8:5`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      Channel.empty().set { ch_versions }
      ^^^^^^^
  ```

- Warning: `subworkflows/local/prepare_ont/main.nf:10:5`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      Channel.empty().set { ch_versions }
      ^^^^^^^
  ```

- Warning: `subworkflows/local/prepare_ont/run_nanoq/main.nf:8:5`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      Channel.empty().set { versions }
      ^^^^^^^
  ```

- Warning: `subworkflows/local/prepare_shortreads/main.nf:10:5`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      Channel.empty().set { ch_versions }
      ^^^^^^^
  ```

- Warning: `subworkflows/local/prepare_shortreads/main.nf:13:41`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          .map { create_shortread_channel(it) }
                                          ^^
  ```

- Warning: `subworkflows/local/qc/busco/main.nf:8:5`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      Channel.empty().set { versions }
      ^^^^^^^
  ```

- Warning: `subworkflows/local/qc/busco/main.nf:9:5`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      Channel.empty().set { batch_summary }
      ^^^^^^^
  ```

- Warning: `subworkflows/local/qc/busco/main.nf:10:5`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      Channel.empty().set { short_summary_txt }
      ^^^^^^^
  ```

- Warning: `subworkflows/local/qc/busco/main.nf:11:5`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      Channel.empty().set { short_summary_json }
      ^^^^^^^
  ```

- Warning: `subworkflows/local/qc/main.nf:15:5`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      Channel.empty().set { ch_versions }
      ^^^^^^^
  ```

- Warning: `subworkflows/local/qc/main.nf:16:5`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      Channel.empty().set { quast_out }
      ^^^^^^^
  ```

- Warning: `subworkflows/local/qc/main.nf:17:5`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      Channel.empty().set { busco_out }
      ^^^^^^^
  ```

- Warning: `subworkflows/local/qc/main.nf:18:5`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      Channel.empty().set { merqury_report_files }
      ^^^^^^^
  ```

- Warning: `subworkflows/local/qc/main.nf:19:5`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      Channel.empty().set { map_to_assembly }
      ^^^^^^^
  ```

- Warning: `subworkflows/local/qc/merqury/main.nf:9:5`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      Channel.empty().set { versions }
      ^^^^^^^
  ```

- Warning: `subworkflows/local/qc/quast/main.nf:11:5`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      Channel.empty().set { versions }
      ^^^^^^^
  ```

- Warning: `subworkflows/local/qc/quast/main.nf:16:5`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      Channel.empty().set { quast_results }
      ^^^^^^^
  ```

- Warning: `subworkflows/local/qc/quast/main.nf:17:5`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      Channel.empty().set { quast_tsv }
      ^^^^^^^
  ```

- Warning: `subworkflows/local/scaffolding/links/main.nf:15:5`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      Channel.empty().set { ch_versions }
      ^^^^^^^
  ```

- Warning: `subworkflows/local/scaffolding/longstitch/main.nf:16:5`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      Channel.empty().set { ch_versions }
      ^^^^^^^
  ```

- Warning: `subworkflows/local/scaffolding/main.nf:16:5`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      Channel.empty().set { ch_versions }
      ^^^^^^^
  ```

- Warning: `subworkflows/local/scaffolding/main.nf:17:5`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      Channel.empty().set { links_busco }
      ^^^^^^^
  ```

- Warning: `subworkflows/local/scaffolding/main.nf:18:5`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      Channel.empty().set { links_quast }
      ^^^^^^^
  ```

- Warning: `subworkflows/local/scaffolding/main.nf:19:5`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      Channel.empty().set { links_merqury }
      ^^^^^^^
  ```

- Warning: `subworkflows/local/scaffolding/main.nf:20:5`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      Channel.empty().set { longstitch_busco }
      ^^^^^^^
  ```

- Warning: `subworkflows/local/scaffolding/main.nf:21:5`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      Channel.empty().set { longstitch_quast }
      ^^^^^^^
  ```

- Warning: `subworkflows/local/scaffolding/main.nf:22:5`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      Channel.empty().set { longstitch_merqury }
      ^^^^^^^
  ```

- Warning: `subworkflows/local/scaffolding/main.nf:23:5`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      Channel.empty().set { ragtag_busco }
      ^^^^^^^
  ```

- Warning: `subworkflows/local/scaffolding/main.nf:24:5`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      Channel.empty().set { ragtag_quast }
      ^^^^^^^
  ```

- Warning: `subworkflows/local/scaffolding/main.nf:25:5`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      Channel.empty().set { ragtag_merqury }
      ^^^^^^^
  ```

- Warning: `subworkflows/local/scaffolding/ragtag/main.nf:16:5`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      Channel.empty().set { ch_versions }
      ^^^^^^^
  ```

- Warning: `subworkflows/local/utils_nfcore_genomeassembler_pipeline/main.nf:31:5`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
      monochrome_logs // boolean: Do not use coloured log outputs
      ^^^^^^^^^^^^^^^
  ```

- Warning: `subworkflows/local/utils_nfcore_genomeassembler_pipeline/main.nf:34:5`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
      input             //  string: Path to input samplesheet
      ^^^^^
  ```

- Warning: `subworkflows/local/utils_nfcore_genomeassembler_pipeline/main.nf:98:5`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      Channel.empty().set { ch_refs }
      ^^^^^^^
  ```

- Warning: `subworkflows/local/utils_nfcore_genomeassembler_pipeline/main.nf:99:5`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      Channel.fromPath(params.input)
      ^^^^^^^
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

- Warning: `workflows/genomeassembler.nf:44:5`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      Channel.empty().set { ch_ref_bam }
      ^^^^^^^
  ```

- Warning: `workflows/genomeassembler.nf:45:5`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      Channel.empty().set { ch_polished_genome }
      ^^^^^^^
  ```

- Warning: `workflows/genomeassembler.nf:46:5`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      Channel.empty().set { ch_ont_reads }
      ^^^^^^^
  ```

- Warning: `workflows/genomeassembler.nf:47:5`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      Channel.empty().set { ch_hifi_reads }
      ^^^^^^^
  ```

- Warning: `workflows/genomeassembler.nf:48:5`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      Channel.empty().set { ch_shortreads }
      ^^^^^^^
  ```

- Warning: `workflows/genomeassembler.nf:49:5`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      Channel.empty().set { meryl_kmers }
      ^^^^^^^
  ```

- Warning: `workflows/genomeassembler.nf:50:5`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      Channel.empty().set { genome_size }
      ^^^^^^^
  ```

- Warning: `workflows/genomeassembler.nf:51:5`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      Channel.empty().set { ch_versions }
      ^^^^^^^
  ```

- Warning: `workflows/genomeassembler.nf:53:5`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      Channel
      ^^^^^^^
  ```

- Warning: `workflows/genomeassembler.nf:198:5`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      Channel
      ^^^^^^^
  ```

- Warning: `workflows/genomeassembler.nf:203:5`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      Channel
      ^^^^^^^
  ```

- Warning: `workflows/genomeassembler.nf:209:25`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
          merqury_files = Channel.of([])
                          ^^^^^^^
  ```

- Warning: `workflows/genomeassembler.nf:212:117`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      REPORT(report_files, report_functions, nanoq_files, genomescope_files, quast_files, busco_files, merqury_files, Channel.fromPath("${params.outdir}/pipeline_info/nf_core_pipeline_software_versions.yml"))
                                                                                                                      ^^^^^^^
  ```

- Warning: `workflows/genomeassembler.nf:217:26`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      def topic_versions = Channel.topic("versions")
                           ^^^^^^^
  ```
