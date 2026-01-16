# Nextflow lint results

- Generated: 2026-01-16T10:19:30.741826969Z
- Nextflow version: 25.12.0-edge
- Summary: 54 errors, 67 warnings

## :x: Errors

- Error: `subworkflows/local/bases_demultiplex/main.nf:89:5`: `sequencer_serial` was assigned but not declared

  ```nextflow
      sequencer_serial = fields[0]
      ^^^^^^^^^^^^^^^^
  ```

- Error: `subworkflows/local/bases_demultiplex/main.nf:90:5`: `run_nubmer` was assigned but not declared

  ```nextflow
      run_nubmer       = fields[1]
      ^^^^^^^^^^
  ```

- Error: `subworkflows/local/bases_demultiplex/main.nf:91:5`: `fcid` was assigned but not declared

  ```nextflow
      fcid             = fields[2]
      ^^^^
  ```

- Error: `subworkflows/local/bases_demultiplex/main.nf:92:5`: `lane` was assigned but not declared

  ```nextflow
      lane             = fields[3]
      ^^^^
  ```

- Error: `subworkflows/local/bases_demultiplex/main.nf:93:5`: `index` was assigned but not declared

  ```nextflow
      index            = fields[-1] =~ /[GATC+-]/ ? fields[-1] : ""
      ^^^^^
  ```

- Error: `subworkflows/local/bases_demultiplex/main.nf:95:14`: `fcid` is not defined

  ```nextflow
      rg.ID = [fcid,lane].join(".")
               ^^^^
  ```

- Error: `subworkflows/local/bases_demultiplex/main.nf:95:19`: `lane` is not defined

  ```nextflow
      rg.ID = [fcid,lane].join(".")
                    ^^^^
  ```

- Error: `subworkflows/local/bases_demultiplex/main.nf:96:14`: `fcid` is not defined

  ```nextflow
      rg.PU = [fcid, lane, index].findAll().join(".")
               ^^^^
  ```

- Error: `subworkflows/local/bases_demultiplex/main.nf:96:20`: `lane` is not defined

  ```nextflow
      rg.PU = [fcid, lane, index].findAll().join(".")
                     ^^^^
  ```

- Error: `subworkflows/local/bases_demultiplex/main.nf:96:26`: `index` is not defined

  ```nextflow
      rg.PU = [fcid, lane, index].findAll().join(".")
                           ^^^^^
  ```

- Error: `subworkflows/local/fqtk_demultiplex/main.nf:90:5`: `sequencer_serial` was assigned but not declared

  ```nextflow
      sequencer_serial = fields[0]
      ^^^^^^^^^^^^^^^^
  ```

- Error: `subworkflows/local/fqtk_demultiplex/main.nf:91:5`: `run_nubmer` was assigned but not declared

  ```nextflow
      run_nubmer       = fields[1]
      ^^^^^^^^^^
  ```

- Error: `subworkflows/local/fqtk_demultiplex/main.nf:92:5`: `fcid` was assigned but not declared

  ```nextflow
      fcid             = fields[2]
      ^^^^
  ```

- Error: `subworkflows/local/fqtk_demultiplex/main.nf:93:5`: `lane` was assigned but not declared

  ```nextflow
      lane             = fields[3]
      ^^^^
  ```

- Error: `subworkflows/local/fqtk_demultiplex/main.nf:94:5`: `index` was assigned but not declared

  ```nextflow
      index            = fields[-1] =~ /[GATC+-]/ ? fields[-1] : ""
      ^^^^^
  ```

- Error: `subworkflows/local/fqtk_demultiplex/main.nf:96:14`: `fcid` is not defined

  ```nextflow
      rg.ID = [fcid,lane].join(".")
               ^^^^
  ```

- Error: `subworkflows/local/fqtk_demultiplex/main.nf:96:19`: `lane` is not defined

  ```nextflow
      rg.ID = [fcid,lane].join(".")
                    ^^^^
  ```

- Error: `subworkflows/local/fqtk_demultiplex/main.nf:97:14`: `fcid` is not defined

  ```nextflow
      rg.PU = [fcid, lane, index].findAll().join(".")
               ^^^^
  ```

- Error: `subworkflows/local/fqtk_demultiplex/main.nf:97:20`: `lane` is not defined

  ```nextflow
      rg.PU = [fcid, lane, index].findAll().join(".")
                     ^^^^
  ```

- Error: `subworkflows/local/fqtk_demultiplex/main.nf:97:26`: `index` is not defined

  ```nextflow
      rg.PU = [fcid, lane, index].findAll().join(".")
                           ^^^^^
  ```

- Error: `subworkflows/local/mgikit_demultiplex/main.nf:86:5`: `sequencer_serial` was assigned but not declared

  ```nextflow
      sequencer_serial = fields[0]
      ^^^^^^^^^^^^^^^^
  ```

- Error: `subworkflows/local/mgikit_demultiplex/main.nf:87:5`: `run_nubmer` was assigned but not declared

  ```nextflow
      run_nubmer       = fields[1]
      ^^^^^^^^^^
  ```

- Error: `subworkflows/local/mgikit_demultiplex/main.nf:88:5`: `fcid` was assigned but not declared

  ```nextflow
      fcid             = fields[2]
      ^^^^
  ```

- Error: `subworkflows/local/mgikit_demultiplex/main.nf:89:5`: `lane` was assigned but not declared

  ```nextflow
      lane             = fields[3]
      ^^^^
  ```

- Error: `subworkflows/local/mgikit_demultiplex/main.nf:90:5`: `index` was assigned but not declared

  ```nextflow
      index            = fields[-1] =~ /[GATC+-]/ ? fields[-1] : ""
      ^^^^^
  ```

- Error: `subworkflows/local/mgikit_demultiplex/main.nf:92:14`: `fcid` is not defined

  ```nextflow
      rg.ID = [fcid,lane].join(".")
               ^^^^
  ```

- Error: `subworkflows/local/mgikit_demultiplex/main.nf:92:19`: `lane` is not defined

  ```nextflow
      rg.ID = [fcid,lane].join(".")
                    ^^^^
  ```

- Error: `subworkflows/local/mgikit_demultiplex/main.nf:93:14`: `fcid` is not defined

  ```nextflow
      rg.PU = [fcid, lane, index].findAll().join(".")
               ^^^^
  ```

- Error: `subworkflows/local/mgikit_demultiplex/main.nf:93:20`: `lane` is not defined

  ```nextflow
      rg.PU = [fcid, lane, index].findAll().join(".")
                     ^^^^
  ```

- Error: `subworkflows/local/mgikit_demultiplex/main.nf:93:26`: `index` is not defined

  ```nextflow
      rg.PU = [fcid, lane, index].findAll().join(".")
                           ^^^^^
  ```

- Error: `subworkflows/local/mkfastq_demultiplex/main.nf:83:5`: `sequencer_serial` was assigned but not declared

  ```nextflow
      sequencer_serial = fields[0]
      ^^^^^^^^^^^^^^^^
  ```

- Error: `subworkflows/local/mkfastq_demultiplex/main.nf:84:5`: `run_nubmer` was assigned but not declared

  ```nextflow
      run_nubmer       = fields[1]
      ^^^^^^^^^^
  ```

- Error: `subworkflows/local/mkfastq_demultiplex/main.nf:85:5`: `fcid` was assigned but not declared

  ```nextflow
      fcid             = fields[2]
      ^^^^
  ```

- Error: `subworkflows/local/mkfastq_demultiplex/main.nf:86:5`: `lane` was assigned but not declared

  ```nextflow
      lane             = fields[3]
      ^^^^
  ```

- Error: `subworkflows/local/mkfastq_demultiplex/main.nf:87:5`: `index` was assigned but not declared

  ```nextflow
      index            = fields[-1] =~ /[GATC+-]/ ? fields[-1] : ""
      ^^^^^
  ```

- Error: `subworkflows/local/mkfastq_demultiplex/main.nf:89:14`: `fcid` is not defined

  ```nextflow
      rg.ID = [fcid,lane].join(".")
               ^^^^
  ```

- Error: `subworkflows/local/mkfastq_demultiplex/main.nf:89:19`: `lane` is not defined

  ```nextflow
      rg.ID = [fcid,lane].join(".")
                    ^^^^
  ```

- Error: `subworkflows/local/mkfastq_demultiplex/main.nf:90:14`: `fcid` is not defined

  ```nextflow
      rg.PU = [fcid, lane, index].findAll().join(".")
               ^^^^
  ```

- Error: `subworkflows/local/mkfastq_demultiplex/main.nf:90:20`: `lane` is not defined

  ```nextflow
      rg.PU = [fcid, lane, index].findAll().join(".")
                     ^^^^
  ```

- Error: `subworkflows/local/mkfastq_demultiplex/main.nf:90:26`: `index` is not defined

  ```nextflow
      rg.PU = [fcid, lane, index].findAll().join(".")
                           ^^^^^
  ```

- Error: `subworkflows/local/singular_demultiplex/main.nf:88:5`: `sequencer_serial` was assigned but not declared

  ```nextflow
      sequencer_serial = fields[0]
      ^^^^^^^^^^^^^^^^
  ```

- Error: `subworkflows/local/singular_demultiplex/main.nf:89:5`: `run_nubmer` was assigned but not declared

  ```nextflow
      run_nubmer       = fields[1]
      ^^^^^^^^^^
  ```

- Error: `subworkflows/local/singular_demultiplex/main.nf:90:5`: `fcid` was assigned but not declared

  ```nextflow
      fcid             = fields[2]
      ^^^^
  ```

- Error: `subworkflows/local/singular_demultiplex/main.nf:91:5`: `lane` was assigned but not declared

  ```nextflow
      lane             = fields[3]
      ^^^^
  ```

- Error: `subworkflows/local/singular_demultiplex/main.nf:92:5`: `index` was assigned but not declared

  ```nextflow
      index            = fields[-1] =~ /[GATC+-]/ ? fields[-1] : ""
      ^^^^^
  ```

- Error: `subworkflows/local/singular_demultiplex/main.nf:94:14`: `fcid` is not defined

  ```nextflow
      rg.ID = [fcid,lane].join(".")
               ^^^^
  ```

- Error: `subworkflows/local/singular_demultiplex/main.nf:94:19`: `lane` is not defined

  ```nextflow
      rg.ID = [fcid,lane].join(".")
                    ^^^^
  ```

- Error: `subworkflows/local/singular_demultiplex/main.nf:95:14`: `fcid` is not defined

  ```nextflow
      rg.PU = [fcid, lane, index].findAll().join(".")
               ^^^^
  ```

- Error: `subworkflows/local/singular_demultiplex/main.nf:95:20`: `lane` is not defined

  ```nextflow
      rg.PU = [fcid, lane, index].findAll().join(".")
                     ^^^^
  ```

- Error: `subworkflows/local/singular_demultiplex/main.nf:95:26`: `index` is not defined

  ```nextflow
      rg.PU = [fcid, lane, index].findAll().join(".")
                           ^^^^^
  ```

- Error: `workflows/demultiplex.nf:86:60`: `AdapterRemover` is not defined

  ```nextflow
                  ["${item[0].id}${suffix}_no_adapters.csv", AdapterRemover.removeAdaptersFromSampleSheet(item[1])]
                                                             ^^^^^^^^^^^^^^
  ```

- Error: `workflows/demultiplex.nf:120:55`: `FormattingService` is not defined

  ```nextflow
      ch_samplesheet.dump(tag: 'DEMULTIPLEX::inputs') { FormattingService.prettyFormat(it) }
                                                        ^^^^^^^^^^^^^^^^^
  ```

- Error: `workflows/demultiplex.nf:261:66`: `FormattingService` is not defined

  ```nextflow
      ch_raw_fastq.dump(tag: "DEMULTIPLEX::Demultiplexed Fastq") { FormattingService.prettyFormat(it) }
                                                                   ^^^^^^^^^^^^^^^^^
  ```

- Error: `workflows/demultiplex.nf:378:65`: `FormattingService` is not defined

  ```nextflow
          ch_multiqc_files.collect().dump(tag: "multiqc_files") { FormattingService.prettyFormat(it) }
                                                                  ^^^^^^^^^^^^^^^^^
  ```

## :warning: Warnings

- Warning: `modules/local/checkqc_dir/main.nf:17:9`: Variable was declared but not used

  ```nextflow
      def args = task.ext.args ?: ''
          ^^^^
  ```

- Warning: `modules/local/fastq_to_samplesheet/main.nf:20:34`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
      def sortedMeta = meta.sort { it.id }
                                   ^^
  ```

- Warning: `modules/local/fastq_to_samplesheet/main.nf:70:52`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
      samplesheetHeader = allColumns.collect { '"' + it + '"' }
                                                     ^^
  ```

- Warning: `modules/nf-core/checkqc/main.nf:47:9`: Variable was declared but not used

  ```nextflow
      def args = task.ext.args ?: ''
          ^^^^
  ```

- Warning: `modules/nf-core/fqtk/main.nf:28:9`: Variable was declared but not used

  ```nextflow
      def prefix = task.ext.prefix ?: "${meta.id}"
          ^^^^^^
  ```

- Warning: `modules/nf-core/fqtk/main.nf:30:48`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
      fastqs = fastq_readstructure_pairs.collect{it[2]/it[0]}.join(" ")
                                                 ^^
  ```

- Warning: `modules/nf-core/fqtk/main.nf:30:54`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
      fastqs = fastq_readstructure_pairs.collect{it[2]/it[0]}.join(" ")
                                                       ^^
  ```

- Warning: `modules/nf-core/fqtk/main.nf:32:57`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
      read_structures = fastq_readstructure_pairs.collect{it[1]}.join(" ")
                                                          ^^
  ```

- Warning: `modules/nf-core/kraken2/kraken2/main.nf:60:9`: Variable was declared but not used

  ```nextflow
      def args = task.ext.args ?: ''
          ^^^^
  ```

- Warning: `modules/nf-core/kraken2/kraken2/main.nf:62:9`: Variable was declared but not used

  ```nextflow
      def paired       = meta.single_end ? "" : "--paired"
          ^^^^^^
  ```

- Warning: `modules/nf-core/kraken2/kraken2/main.nf:65:9`: Variable was declared but not used

  ```nextflow
      def readclassification_option = save_reads_assignment ? "--output ${prefix}.kraken2.classifiedreads.txt" : "--output /dev/null"
          ^^^^^^^^^^^^^^^^^^^^^^^^^
  ```

- Warning: `modules/nf-core/kraken2/kraken2/main.nf:66:9`: Variable was declared but not used

  ```nextflow
      def compress_reads_command = save_output_fastqs ? "pigz -p $task.cpus *.fastq" : ""
          ^^^^^^^^^^^^^^^^^^^^^^
  ```

- Warning: `subworkflows/local/bases_demultiplex/main.nf:77:68`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          InputStream gzipStream = new java.util.zip.GZIPInputStream(it)
                                                                     ^^
  ```

- Warning: `subworkflows/local/fqtk_demultiplex/main.nf:79:68`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          InputStream gzipStream = new java.util.zip.GZIPInputStream(it)
                                                                     ^^
  ```

- Warning: `subworkflows/local/mgikit_demultiplex/main.nf:72:68`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          InputStream gzipStream = new java.util.zip.GZIPInputStream(it)
                                                                     ^^
  ```

- Warning: `subworkflows/local/mkfastq_demultiplex/main.nf:72:68`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          InputStream gzipStream = new java.util.zip.GZIPInputStream(it)
                                                                     ^^
  ```

- Warning: `subworkflows/local/rundir_checkqc/main.nf:20:28`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
          ch_versions      = Channel.empty()
                             ^^^^^^^
  ```

- Warning: `subworkflows/local/rundir_checkqc/main.nf:21:28`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
          ch_report        = Channel.empty()
                             ^^^^^^^
  ```

- Warning: `subworkflows/local/rundir_checkqc/main.nf:22:28`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
          ch_checkqc_dir   = Channel.empty()
                             ^^^^^^^
  ```

- Warning: `subworkflows/local/rundir_checkqc/main.nf:27:23`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
              .branch { meta, samplesheet, run ->
                        ^^^^
  ```

- Warning: `subworkflows/local/rundir_checkqc/main.nf:27:29`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
              .branch { meta, samplesheet, run ->
                              ^^^^^^^^^^^
  ```

- Warning: `subworkflows/local/singular_demultiplex/main.nf:77:68`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          InputStream gzipStream = new java.util.zip.GZIPInputStream(it)
                                                                     ^^
  ```

- Warning: `subworkflows/local/utils_nfcore_demultiplex_pipeline/main.nf:31:5`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
      monochrome_logs // boolean: Do not use coloured log outputs
      ^^^^^^^^^^^^^^^
  ```

- Warning: `subworkflows/local/utils_nfcore_demultiplex_pipeline/main.nf:34:5`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
      input //  string: Path to input samplesheet
      ^^^^^
  ```

- Warning: `subworkflows/local/utils_nfcore_demultiplex_pipeline/main.nf:105:26`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
          ch_samplesheet = Channel
                           ^^^^^^^
  ```

- Warning: `subworkflows/local/utils_nfcore_demultiplex_pipeline/main.nf:114:9`: Variable was declared but not used

  ```nextflow
          ch_flowcell_manifest = ch_samplesheet
          ^^^^^^^^^^^^^^^^^^^^
  ```

- Warning: `subworkflows/local/utils_nfcore_demultiplex_pipeline/main.nf:115:20`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
              .map { meta, samplesheet, flowcell, per_flowcell_manifest -> per_flowcell_manifest }
                     ^^^^
  ```

- Warning: `subworkflows/local/utils_nfcore_demultiplex_pipeline/main.nf:115:26`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
              .map { meta, samplesheet, flowcell, per_flowcell_manifest -> per_flowcell_manifest }
                           ^^^^^^^^^^^
  ```

- Warning: `subworkflows/local/utils_nfcore_demultiplex_pipeline/main.nf:115:39`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
              .map { meta, samplesheet, flowcell, per_flowcell_manifest -> per_flowcell_manifest }
                                        ^^^^^^^^
  ```

- Warning: `subworkflows/local/utils_nfcore_demultiplex_pipeline/main.nf:124:26`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
          ch_samplesheet = Channel
                           ^^^^^^^
  ```

- Warning: `subworkflows/nf-core/bcl_demultiplex/main.nf:16:28`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
          ch_versions      = Channel.empty()
                             ^^^^^^^
  ```

- Warning: `subworkflows/nf-core/bcl_demultiplex/main.nf:17:28`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
          ch_fastq         = Channel.empty()
                             ^^^^^^^
  ```

- Warning: `subworkflows/nf-core/bcl_demultiplex/main.nf:18:28`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
          ch_reports       = Channel.empty()
                             ^^^^^^^
  ```

- Warning: `subworkflows/nf-core/bcl_demultiplex/main.nf:19:28`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
          ch_stats         = Channel.empty()
                             ^^^^^^^
  ```

- Warning: `subworkflows/nf-core/bcl_demultiplex/main.nf:20:28`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
          ch_interop       = Channel.empty()
                             ^^^^^^^
  ```

- Warning: `subworkflows/nf-core/bcl_demultiplex/main.nf:124:27`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
              fastq       : it[0].empty == false
                            ^^
  ```

- Warning: `subworkflows/nf-core/bcl_demultiplex/main.nf:125:27`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
              empty_fastq : it[0].empty == true
                            ^^
  ```

- Warning: `subworkflows/nf-core/fastq_contam_seqtk_kraken/main.nf:17:23`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
          ch_reports  = Channel.empty()
                        ^^^^^^^
  ```

- Warning: `subworkflows/nf-core/fastq_contam_seqtk_kraken/main.nf:18:23`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
          ch_versions = Channel.empty()
                        ^^^^^^^
  ```

- Warning: `workflows/demultiplex.nf:98:26`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
              .map { meta, samplesheet, flowcell, lane, new_samplesheet -> [meta, new_samplesheet, flowcell, lane] }
                           ^^^^^^^^^^^
  ```

- Warning: `workflows/demultiplex.nf:110:53`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
              ch_samplesheet.map { meta, samplesheet, flowcell, lane -> [meta, samplesheet] },
                                                      ^^^^^^^^
  ```

- Warning: `workflows/demultiplex.nf:110:63`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
              ch_samplesheet.map { meta, samplesheet, flowcell, lane -> [meta, samplesheet] },
                                                                ^^^^
  ```

- Warning: `workflows/demultiplex.nf:116:26`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
              .map { meta, samplesheet, flowcell, lane, samplesheet_formatted -> [meta, samplesheet_formatted, flowcell, lane] }
                           ^^^^^^^^^^^
  ```

- Warning: `workflows/demultiplex.nf:120:86`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
      ch_samplesheet.dump(tag: 'DEMULTIPLEX::inputs') { FormattingService.prettyFormat(it) }
                                                                                       ^^
  ```

- Warning: `workflows/demultiplex.nf:126:48`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          ch_flowcells = ch_samplesheet.branch { meta, samplesheet, flowcell, per_flowcell_manifest ->
                                                 ^^^^
  ```

- Warning: `workflows/demultiplex.nf:126:54`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          ch_flowcells = ch_samplesheet.branch { meta, samplesheet, flowcell, per_flowcell_manifest ->
                                                       ^^^^^^^^^^^
  ```

- Warning: `workflows/demultiplex.nf:126:77`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          ch_flowcells = ch_samplesheet.branch { meta, samplesheet, flowcell, per_flowcell_manifest ->
                                                                              ^^^^^^^^^^^^^^^^^^^^^
  ```

- Warning: `workflows/demultiplex.nf:138:49`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
              .map { meta, samplesheet, flowcell, per_flowcell_manifest ->
                                                  ^^^^^^^^^^^^^^^^^^^^^
  ```

- Warning: `workflows/demultiplex.nf:141:23`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
              .branch { meta, samplesheet, flowcell ->
                        ^^^^
  ```

- Warning: `workflows/demultiplex.nf:141:29`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
              .branch { meta, samplesheet, flowcell ->
                              ^^^^^^^^^^^
  ```

- Warning: `workflows/demultiplex.nf:180:85`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          ch_multiqc_files = ch_multiqc_files.mix(BASES_DEMULTIPLEX.out.metrics.map { meta, metrics ->
                                                                                      ^^^^
  ```

- Warning: `workflows/demultiplex.nf:190:83`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          ch_multiqc_files = ch_multiqc_files.mix(BCL_DEMULTIPLEX.out.reports.map { meta, report ->
                                                                                    ^^^^
  ```

- Warning: `workflows/demultiplex.nf:193:81`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          ch_multiqc_files = ch_multiqc_files.mix(BCL_DEMULTIPLEX.out.stats.map { meta, stats ->
                                                                                  ^^^^
  ```

- Warning: `workflows/demultiplex.nf:201:85`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
              ch_multiqc_files = ch_multiqc_files.mix(RUNDIR_CHECKQC.out.report.map { meta, json ->
                                                                                      ^^^^
  ```

- Warning: `workflows/demultiplex.nf:212:20`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
              .map { it[2] }
                     ^^
  ```

- Warning: `workflows/demultiplex.nf:214:21`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
              .map { [it.fastq, it.read_structure] }
                      ^^
  ```

- Warning: `workflows/demultiplex.nf:214:31`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
              .map { [it.fastq, it.read_structure] }
                                ^^
  ```

- Warning: `workflows/demultiplex.nf:218:93`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          fastqs_with_paths = fastq_read_structure.combine(UNTAR_FLOWCELL.out.untar.collect { it[1] }).toList()
                                                                                              ^^
  ```

- Warning: `workflows/demultiplex.nf:226:84`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          ch_multiqc_files = ch_multiqc_files.mix(FQTK_DEMULTIPLEX.out.metrics.map { meta, metrics ->
                                                                                     ^^^^
  ```

- Warning: `workflows/demultiplex.nf:236:88`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          ch_multiqc_files = ch_multiqc_files.mix(SINGULAR_DEMULTIPLEX.out.metrics.map { meta, metrics ->
                                                                                         ^^^^
  ```

- Warning: `workflows/demultiplex.nf:253:89`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          ch_multiqc_files = ch_multiqc_files.mix(MGIKIT_DEMULTIPLEX.out.qc_reports.map { meta, metrics ->
                                                                                          ^^^^
  ```

- Warning: `workflows/demultiplex.nf:261:97`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
      ch_raw_fastq.dump(tag: "DEMULTIPLEX::Demultiplexed Fastq") { FormattingService.prettyFormat(it) }
                                                                                                  ^^
  ```

- Warning: `workflows/demultiplex.nf:272:70`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          ch_multiqc_files = ch_multiqc_files.mix(FASTP.out.json.map { meta, json ->
                                                                       ^^^^
  ```

- Warning: `workflows/demultiplex.nf:282:69`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          ch_multiqc_files = ch_multiqc_files.mix(FALCO.out.txt.map { meta, txt ->
                                                                      ^^^^
  ```

- Warning: `workflows/demultiplex.nf:299:57`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
              kraken_db = UNTAR_KRAKEN_DB.out.untar.map { meta, file -> file }
                                                          ^^^^
  ```

- Warning: `workflows/demultiplex.nf:310:93`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          ch_multiqc_files = ch_multiqc_files.mix(FASTQ_CONTAM_SEQTK_KRAKEN.out.reports.map { meta, log ->
                                                                                              ^^^^
  ```

- Warning: `workflows/demultiplex.nf:378:96`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          ch_multiqc_files.collect().dump(tag: "multiqc_files") { FormattingService.prettyFormat(it) }
                                                                                                 ^^
  ```
