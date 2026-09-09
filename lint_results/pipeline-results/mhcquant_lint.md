# Nextflow lint results

- Generated: 2026-09-09T00:21:09.340680054Z
- Nextflow version: 26.08.0-edge
- Summary: 45 warnings

## :warning: Warnings

- Warning: `conf/modules.config:109:106`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
              "-fixed_modifications ${meta.fixed_mods.trim() ? meta.fixed_mods.tokenize(',').collect { "'${it.trim()}'" }.join(' ') : ''}",
                                                                                                           ^^
  ```

- Warning: `conf/modules.config:110:115`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
              meta.variable_mods.trim() ? "-variable_modifications ${meta.variable_mods.tokenize(',').collect { "'${it.trim()}'" }.join(' ')}" : "",
                                                                                                                    ^^
  ```

- Warning: `modules/local/epicore/main.nf:38:9`: Variable was declared but not used

  ```nextflow
      def args = task.ext.args ?: ''
          ^^^^
  ```

- Warning: `modules/local/openms/idmassaccuracy/main.nf:35:9`: Variable was declared but not used

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

- Warning: `modules/local/openms/maprttransformer/main.nf:36:44`: Implicit closure parameter is deprecated, declare an explicit parameter instead

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

- Warning: `subworkflows/local/map_alignment/main.nf:22:24`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
              .flatMap { group_meta, metas -> metas }
                         ^^^^^^^^^^
  ```

- Warning: `subworkflows/local/map_alignment/main.nf:25:32`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
                      .flatMap { group_meta, trafoxmls -> [trafoxmls].flatten().collect { trafoxml -> [[spectra: trafoxml.baseName], trafoxml] } })
                                 ^^^^^^^^^^
  ```

- Warning: `subworkflows/local/map_alignment/main.nf:26:20`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
              .map { spectra, meta, trafoxml -> [meta, trafoxml] }
                     ^^^^^^^
  ```

- Warning: `subworkflows/local/map_alignment/main.nf:35:24`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
              .flatMap { group_meta, idxmls -> [idxmls].flatten().collect { idxml -> [[spectra: idxml.baseName.replace("_fdr_filtered","")], idxml] } }
                         ^^^^^^^^^^
  ```

- Warning: `subworkflows/local/map_alignment/main.nf:37:32`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
                      .flatMap { group_meta, metas -> metas }
                                 ^^^^^^^^^^
  ```

- Warning: `subworkflows/local/map_alignment/main.nf:39:20`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
              .map { group_meta, idxml, meta -> [meta, idxml] }
                     ^^^^^^^^^^
  ```

- Warning: `subworkflows/local/process_feature/main.nf:20:61`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          .map { key, featurexmls -> [key, featurexmls.sort { it.name.tokenize('_')[0] as int }] }
                                                              ^^
  ```

- Warning: `subworkflows/local/quant/main.nf:30:24`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
              .flatMap { group_meta, idxmls -> [idxmls].flatten().collect { idxml -> [[spectra: idxml.baseName], idxml] } }
                         ^^^^^^^^^^
  ```

- Warning: `subworkflows/local/quant/main.nf:33:32`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
                      .flatMap { group_meta, metas -> metas }
                                 ^^^^^^^^^^
  ```

- Warning: `subworkflows/local/quant/main.nf:35:20`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
              .map { spectra, idxmls, meta -> [meta, idxmls] }
                     ^^^^^^^
  ```

- Warning: `subworkflows/local/quant/main.nf:51:20`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
              .map { group_meta, meta, idxml, q_value -> [meta, idxml, q_value] }
                     ^^^^^^^^^^
  ```

- Warning: `subworkflows/local/quant/main.nf:79:24`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
                  .map { group_meta, meta, aligned_mzml, idxml, merged_idxml -> [meta, aligned_mzml, idxml, merged_idxml] }
                         ^^^^^^^^^^
  ```

- Warning: `subworkflows/local/rescore/main.nf:56:100`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          ch_multiqc_files = ch_multiqc_files.mix(OPENMS_PERCOLATORADAPTER.out.feature_weights.map { meta, feature_weights -> feature_weights })
                                                                                                     ^^^^
  ```

- Warning: `subworkflows/local/rescore/main.nf:77:25`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
                  ).map { preset, group_meta, local_idxml, global_filtered_idxml ->
                          ^^^^^^
  ```

- Warning: `subworkflows/local/rescore/main.nf:97:24`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
              non_empty: it[1].countLines() > 130
                         ^^
  ```

- Warning: `subworkflows/local/utils_nfcore_mhcquant_pipeline/main.nf:35:5`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
      input             //  string: Path to input samplesheet
      ^^^^^
  ```

- Warning: `subworkflows/local/utils_nfcore_mhcquant_pipeline/main.nf:163:28`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          .map { group_meta, metas, files, fastas -> [group_meta, files.size()] }
                             ^^^^^
  ```

- Warning: `subworkflows/local/utils_nfcore_mhcquant_pipeline/main.nf:163:42`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          .map { group_meta, metas, files, fastas -> [group_meta, files.size()] }
                                           ^^^^^^
  ```

- Warning: `subworkflows/local/utils_nfcore_mhcquant_pipeline/main.nf:165:16`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          .map { group_meta, group_count, meta, file, fasta ->
                 ^^^^^^^^^^
  ```

- Warning: `subworkflows/local/utils_nfcore_mhcquant_pipeline/main.nf:173:28`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          .map { meta, file, fasta, presetsMap ->
                             ^^^^^
  ```

- Warning: `subworkflows/local/utils_nfcore_mhcquant_pipeline/main.nf:186:19`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
              .map{ meta, file, fasta -> fasta }
                    ^^^^
  ```

- Warning: `subworkflows/local/utils_nfcore_mhcquant_pipeline/main.nf:186:25`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
              .map{ meta, file, fasta -> fasta }
                          ^^^^
  ```

- Warning: `subworkflows/local/utils_nfcore_mhcquant_pipeline/main.nf:198:51`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          ch_fasta = ch_samplesheet_raw.map { meta, file, fasta -> [groupKey([id: "${meta.sample}_${meta.condition}"], meta.group_count), fasta] }
                                                    ^^^^
  ```

- Warning: `subworkflows/local/utils_nfcore_mhcquant_pipeline/main.nf:200:20`: Parameter was not used -- prefix with `_` to suppress warning

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

- Warning: `workflows/mhcquant.nf:104:74`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          OPENMSTHIRDPARTY_COMETADAPTER.out.idxml.combine(ch_decoy_db.map{ meta, fasta -> [fasta] }) :
                                                                           ^^^^
  ```

- Warning: `workflows/mhcquant.nf:108:20`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
              .map { groupKey, meta, idxml, fasta -> [meta, idxml, fasta] }
                     ^^^^^^^^
  ```

- Warning: `workflows/mhcquant.nf:114:85`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
      ch_multiqc_files = ch_multiqc_files.mix(OPENMS_IDMASSACCURACY.out.frag_err.map{ meta, frag_err -> frag_err })
                                                                                      ^^^^
  ```

- Warning: `workflows/mhcquant.nf:118:22`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          .map { meta, idxml -> [ groupKey([id: "${meta.sample}_${meta.condition}"], meta.group_count), meta] }
                       ^^^^^
  ```

- Warning: `workflows/mhcquant.nf:135:20`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
              .map { gkey, metas, mzmls, idxml ->
                     ^^^^
  ```

- Warning: `workflows/mhcquant.nf:162:24`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
                  .map { groupKey, meta, comet_idxml, fdr_filtered_idxml -> [meta, comet_idxml, fdr_filtered_idxml] }
                         ^^^^^^^^
  ```

- Warning: `workflows/mhcquant.nf:239:88`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          params.epicore ? EPICORE.out.stats : SUMMARIZE_RESULTS.out.epicore_input.map { meta, tsv, stats -> stats }
                                                                                         ^^^^
  ```

- Warning: `workflows/mhcquant.nf:239:94`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          params.epicore ? EPICORE.out.stats : SUMMARIZE_RESULTS.out.epicore_input.map { meta, tsv, stats -> stats }
                                                                                               ^^^
  ```
