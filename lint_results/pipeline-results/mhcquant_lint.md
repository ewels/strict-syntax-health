# Nextflow lint results

- Generated: 2026-01-16T10:24:08.076402670Z
- Nextflow version: 25.12.0-edge
- Summary: 9 errors, 60 warnings

## :x: Errors

- Error: `conf/base.config:61:29`: Unexpected input: ':'

  ```nextflow
      withName:NFCORE_MHCQUANT:MHCQUANT:PREPARE_SPECTRA:TDF2MZML {
                              ^
  ```

- Error: `conf/modules.config:271:17`: Unexpected input: ':'

  ```nextflow
          withName: 'NFCORE_MHCQUANT:MHCQUANT:QUANT:OPENMS_IDSCORESWITCHER' {
                  ^
  ```

- Error: `modules/local/ms2rescore/main.nf:11:5`: Invalid process directive

  ```nextflow
      containerOptions = (workflow.containerEngine == 'docker') ? '-u $(id -u) -e "HOME=${HOME}" -v /etc/passwd:/etc/passwd:ro -v /etc/shadow:/etc/shadow:ro -v /etc/group:/etc/group:ro -v $HOME:$HOME' : ''
      ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  ```

- Error: `nextflow.config:233:25`: Invalid include source: '/home/runner/work/strict-syntax-health/strict-syntax-health/pipelines/mhcquant/conf/test_percolator.config'

  ```nextflow
      test_percolator   { includeConfig 'conf/test_percolator.config'   }
                          ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  ```

- Error: `nextflow.config:235:25`: Invalid include source: '/home/runner/work/strict-syntax-health/strict-syntax-health/pipelines/mhcquant/conf/test_epicore.config'

  ```nextflow
      test_epicore      { includeConfig 'conf/test_epicore.config'      }
                          ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  ```

- Error: `subworkflows/local/quant/main.nf:18:1`: Statements cannot be mixed with script declarations -- move statements into a process, workflow, or function

  ```nextflow
  def sortById = { a, b -> a.id <=> b.id }
  ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  ```

- Error: `subworkflows/local/quant/main.nf:83:30`: `mzml` is already declared

  ```nextflow
                  .map { meta, mzml, idxml -> [ groupKey([id: "${meta.sample}_${meta.condition}"], meta.group_count), meta, mzml, idxml] }
                               ^^^^
  ```

- Error: `subworkflows/local/quant/main.nf:85:42`: `mzml` is already declared

  ```nextflow
                  .map { group_meta, meta, mzml, idxml -> [group_meta, meta, mzml, idxml] }
                                           ^^^^
  ```

- Error: `subworkflows/local/quant/main.nf:87:42`: `mzml` is already declared

  ```nextflow
                  .map { group_meta, meta, mzml, idxml, merged_idxml -> [meta, mzml, idxml, merged_idxml] }
                                           ^^^^
  ```

## :warning: Warnings

- Warning: `modules/local/epicore/main.nf:43:9`: Variable was declared but not used

  ```nextflow
      def args = task.ext.args ?: ''
          ^^^^
  ```

- Warning: `modules/local/openms/mapaligneridentification/main.nf:22:38`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
      def out_names = idxmls.collect { it.baseName.replace('_fdr_filtered','')+'.trafoXML' }.join(' ')
                                       ^^
  ```

- Warning: `modules/local/openms/maprttransformer/main.nf:23:44`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
      def fileExt = alignment_file.collect { it.name.tokenize("\\.")[1] }.join(' ')
                                             ^^
  ```

- Warning: `modules/local/openms/maprttransformer/main.nf:41:44`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
      def fileExt = alignment_file.collect { it.name.tokenize("\\.")[1] }.join(' ')
                                             ^^
  ```

- Warning: `modules/local/openms/psmfeatureextractor/main.nf:23:9`: Variable was declared but not used

  ```nextflow
      def extra_features = ""
          ^^^^^^^^^^^^^^
  ```

- Warning: `modules/local/pyopenms/chromatogramextractor/main.nf:21:9`: Variable was declared but not used

  ```nextflow
      def args   = task.ext.args  ?: ''
          ^^^^
  ```

- Warning: `modules/local/pyopenms/ionannotator/main.nf:22:9`: Variable was declared but not used

  ```nextflow
      def prefix = task.ext.prefix ?: "${meta.id}"
          ^^^^^^
  ```

- Warning: `modules/nf-core/gunzip/main.nf:43:9`: Variable was declared but not used

  ```nextflow
      def args = task.ext.args ?: ''
          ^^^^
  ```

- Warning: `modules/nf-core/openms/decoydatabase/main.nf:39:9`: Variable was declared but not used

  ```nextflow
      def args = task.ext.args ?: ''
          ^^^^
  ```

- Warning: `modules/nf-core/openms/filefilter/main.nf:42:9`: Variable was declared but not used

  ```nextflow
      def args = task.ext.args ?: ''
          ^^^^
  ```

- Warning: `modules/nf-core/openms/idfilter/main.nf:43:9`: Variable was declared but not used

  ```nextflow
      def args = task.ext.args ?: ''
          ^^^^
  ```

- Warning: `modules/nf-core/openms/idfilter/main.nf:49:9`: Variable was declared but not used

  ```nextflow
      def filter = filter_file ? "${filter_citerion} ${filter_file}" : ""
          ^^^^^^
  ```

- Warning: `modules/nf-core/openms/idmassaccuracy/main.nf:40:9`: Variable was declared but not used

  ```nextflow
      def args = task.ext.args ?: ''
          ^^^^
  ```

- Warning: `modules/nf-core/openms/idmerger/main.nf:38:9`: Variable was declared but not used

  ```nextflow
      def args = task.ext.args ?: ''
          ^^^^
  ```

- Warning: `modules/nf-core/openms/idripper/main.nf:22:9`: Variable was declared but not used

  ```nextflow
      def prefix = task.ext.prefix ?: "${meta.id}"
          ^^^^^^
  ```

- Warning: `modules/nf-core/openms/idripper/main.nf:38:9`: Variable was declared but not used

  ```nextflow
      def args = task.ext.args ?: ''
          ^^^^
  ```

- Warning: `modules/nf-core/openms/idscoreswitcher/main.nf:39:9`: Variable was declared but not used

  ```nextflow
      def args = task.ext.args ?: ''
          ^^^^
  ```

- Warning: `modules/nf-core/openms/peakpickerhires/main.nf:38:9`: Variable was declared but not used

  ```nextflow
      def args = task.ext.args ?: ''
          ^^^^
  ```

- Warning: `modules/nf-core/openms/peptideindexer/main.nf:41:9`: Variable was declared but not used

  ```nextflow
      def args = task.ext.args ?: ''
          ^^^^
  ```

- Warning: `modules/nf-core/openmsthirdparty/cometadapter/main.nf:42:9`: Variable was declared but not used

  ```nextflow
      def args = task.ext.args ?: ''
          ^^^^
  ```

- Warning: `subworkflows/local/map_alignment/main.nf:25:24`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
              .flatMap { group_meta, metas -> metas }
                         ^^^^^^^^^^
  ```

- Warning: `subworkflows/local/map_alignment/main.nf:28:32`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
                      .flatMap { group_meta, trafoxmls -> trafoxmls.collect { trafoxml -> [[spectra: trafoxml.baseName], trafoxml] } })
                                 ^^^^^^^^^^
  ```

- Warning: `subworkflows/local/map_alignment/main.nf:29:20`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
              .map { spectra, meta, trafoxml -> [meta, trafoxml] }
                     ^^^^^^^
  ```

- Warning: `subworkflows/local/map_alignment/main.nf:39:28`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
                  .flatMap { group_meta, idxmls -> idxmls.collect { idxml -> [[spectra: idxml.baseName.replace("_fdr_filtered","")], idxml] } }
                             ^^^^^^^^^^
  ```

- Warning: `subworkflows/local/map_alignment/main.nf:41:36`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
                          .flatMap { group_meta, metas -> metas }
                                     ^^^^^^^^^^
  ```

- Warning: `subworkflows/local/map_alignment/main.nf:43:24`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
                  .map { group_meta, idxml, meta -> [meta, idxml] }
                         ^^^^^^^^^^
  ```

- Warning: `subworkflows/local/quant/main.nf:18:5`: Variable was declared but not used

  ```nextflow
  def sortById = { a, b -> a.id <=> b.id }
      ^^^^^^^^
  ```

- Warning: `subworkflows/local/quant/main.nf:33:28`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
                  .flatMap { group_meta, idxmls -> idxmls.collect { idxml -> [[spectra: idxml.baseName], idxml] } }
                             ^^^^^^^^^^
  ```

- Warning: `subworkflows/local/quant/main.nf:37:36`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
                          .flatMap { group_meta, metas -> metas }
                                     ^^^^^^^^^^
  ```

- Warning: `subworkflows/local/quant/main.nf:39:24`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
                  .map { spectra, idxmls, meta -> [meta, idxmls] }
                         ^^^^^^^
  ```

- Warning: `subworkflows/local/quant/main.nf:56:20`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
              .map { group_meta, meta, idxml, q_value -> [meta, idxml, q_value] }
                     ^^^^^^^^^^
  ```

- Warning: `subworkflows/local/quant/main.nf:87:24`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
                  .map { group_meta, meta, mzml, idxml, merged_idxml -> [meta, mzml, idxml, merged_idxml] }
                         ^^^^^^^^^^
  ```

- Warning: `subworkflows/local/rescore/main.nf:60:99`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          ch_multiqc_files = ch_multiqc_files.mix(OPENMS_PERCOLATORADAPTER.out.feature_weights.map{ meta, feature_weights -> feature_weights })
                                                                                                    ^^^^
  ```

- Warning: `subworkflows/local/rescore/main.nf:65:78`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
              OPENMS_IDMERGER_GLOBAL(OPENMS_PSMFEATUREEXTRACTOR.out.idxml.map {group_meta, idxml -> [[id:'global'], idxml] }.groupTuple())
                                                                               ^^^^^^^^^^
  ```

- Warning: `subworkflows/local/rescore/main.nf:73:101`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
              OPENMS_IDFILTER_GLOBAL(ch_pout.combine(OPENMS_IDFILTER_Q_VALUE_GLOBAL.out.filtered.map{ it[1] }))
                                                                                                      ^^
  ```

- Warning: `subworkflows/local/speclib/main.nf:49:20`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
              .map { meta, psmpkl -> [[id: "global"], psmpkl] }
                     ^^^^
  ```

- Warning: `subworkflows/local/speclib/main.nf:53:20`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
              .map { meta, peakpkl -> [[id: "global"], peakpkl] }
                     ^^^^
  ```

- Warning: `subworkflows/local/utils_nfcore_mhcquant_pipeline/main.nf:32:5`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
      monochrome_logs   // boolean: Do not use coloured log outputs
      ^^^^^^^^^^^^^^^
  ```

- Warning: `subworkflows/local/utils_nfcore_mhcquant_pipeline/main.nf:35:5`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
      input             //  string: Path to input samplesheet
      ^^^^^
  ```

- Warning: `subworkflows/local/utils_nfcore_mhcquant_pipeline/main.nf:42:5`: Variable was declared but not used

  ```nextflow
      ch_versions = channel.empty()
      ^^^^^^^^^^^
  ```

- Warning: `subworkflows/local/utils_nfcore_mhcquant_pipeline/main.nf:105:28`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          .map { group_meta, metas, files, fastas -> [ group_meta, files.size()] }
                             ^^^^^
  ```

- Warning: `subworkflows/local/utils_nfcore_mhcquant_pipeline/main.nf:105:42`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          .map { group_meta, metas, files, fastas -> [ group_meta, files.size()] }
                                           ^^^^^^
  ```

- Warning: `subworkflows/local/utils_nfcore_mhcquant_pipeline/main.nf:107:16`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          .map { group_meta, group_count, meta, file, fasta -> [meta + ['group_count':group_count, 'spectra':file.baseName.tokenize('.')[0], 'ext':getCustomExtension(file)], file, fasta] }
                 ^^^^^^^^^^
  ```

- Warning: `subworkflows/local/utils_nfcore_mhcquant_pipeline/main.nf:110:59`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
      ch_samplesheet = ch_samplesheet_raw.map { meta, file, fasta -> [ meta, file ]}
                                                            ^^^^^
  ```

- Warning: `subworkflows/local/utils_nfcore_mhcquant_pipeline/main.nf:122:19`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
              .map{ meta, file, fasta -> fasta }
                    ^^^^
  ```

- Warning: `subworkflows/local/utils_nfcore_mhcquant_pipeline/main.nf:122:25`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
              .map{ meta, file, fasta -> fasta }
                          ^^^^
  ```

- Warning: `subworkflows/local/utils_nfcore_mhcquant_pipeline/main.nf:135:51`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          ch_fasta = ch_samplesheet_raw.map { meta, file, fasta -> [ groupKey([id: "${meta.sample}_${meta.condition}"], meta.group_count), fasta] }
                                                    ^^^^
  ```

- Warning: `subworkflows/local/utils_nfcore_mhcquant_pipeline/main.nf:137:20`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
              .map { meta, fasta -> fasta }
                     ^^^^
  ```

- Warning: `workflows/mhcquant.nf:89:89`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
      ch_multiqc_files = ch_multiqc_files.mix(PYOPENMS_CHROMATOGRAMEXTRACTOR.out.csv.map{ meta, mzml -> mzml })
                                                                                          ^^^^
  ```

- Warning: `workflows/mhcquant.nf:93:53`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          ch_clean_mzml_file.combine(ch_decoy_db.map{ meta, fasta -> [fasta] }) :
                                                      ^^^^
  ```

- Warning: `workflows/mhcquant.nf:97:20`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
              .map { groupKey, meta, mzml, fasta -> [meta, mzml, fasta] }
                     ^^^^^^^^
  ```

- Warning: `workflows/mhcquant.nf:105:74`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          OPENMSTHIRDPARTY_COMETADAPTER.out.idxml.combine(ch_decoy_db.map{ meta, fasta -> [fasta] }) :
                                                                           ^^^^
  ```

- Warning: `workflows/mhcquant.nf:109:20`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
              .map { groupKey, meta, idxml, fasta -> [meta, idxml, fasta] }
                     ^^^^^^^^
  ```

- Warning: `workflows/mhcquant.nf:117:85`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
      ch_multiqc_files = ch_multiqc_files.mix(OPENMS_IDMASSACCURACY.out.frag_err.map{ meta, frag_err -> frag_err })
                                                                                      ^^^^
  ```

- Warning: `workflows/mhcquant.nf:121:22`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          .map { meta, idxml -> [ groupKey([id: "${meta.sample}_${meta.condition}"], meta.group_count), meta] }
                       ^^^^^
  ```

- Warning: `workflows/mhcquant.nf:154:24`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
                  .map { groupKey, meta, comet_idxml, fdr_filtered_idxml -> [meta, comet_idxml, fdr_filtered_idxml] }
                         ^^^^^^^^
  ```

- Warning: `workflows/mhcquant.nf:160:23`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
              .filter { meta, idxml -> idxml.countLines() > 130 }
                        ^^^^
  ```

- Warning: `workflows/mhcquant.nf:212:31`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          EPICORE(ch_fasta.map{ it.last()}, SUMMARIZE_RESULTS.out.epicore_input)
                                ^^
  ```

- Warning: `workflows/mhcquant.nf:230:88`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          params.epicore ? EPICORE.out.stats : SUMMARIZE_RESULTS.out.epicore_input.map { meta, tsv, stats -> stats }
                                                                                         ^^^^
  ```

- Warning: `workflows/mhcquant.nf:230:94`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          params.epicore ? EPICORE.out.stats : SUMMARIZE_RESULTS.out.epicore_input.map { meta, tsv, stats -> stats }
                                                                                               ^^^
  ```
