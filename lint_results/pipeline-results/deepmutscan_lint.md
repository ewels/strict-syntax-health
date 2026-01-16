# Nextflow lint results

- Generated: 2026-01-16T06:30:32.246155493Z
- Nextflow version: 25.12.0-edge
- Summary: 121 errors, 118 warnings

## :x: Errors

- Error: `modules/local/fitness/fitness_standard.nf:103:15`: `sample` is already declared

  ```nextflow
      tuple val(sample), path(wt_seq)   		      // WT sequence
                ^^^^^^
  ```

- Error: `workflows/deepmutscan.nf:53:1`: Statements cannot be mixed with script declarations -- move statements into a process, workflow, or function

  ```nextflow
  Channel
  ^^^^^^^
  ```

- Error: `workflows/deepmutscan.nf:59:1`: Statements cannot be mixed with script declarations -- move statements into a process, workflow, or function

  ```nextflow
  Channel
  ^^^^^^^
  ```

- Error: `workflows/deepmutscan.nf:64:1`: Statements cannot be mixed with script declarations -- move statements into a process, workflow, or function

  ```nextflow
  Channel
  ^^^^^^^
  ```

- Error: `workflows/deepmutscan.nf:69:1`: Statements cannot be mixed with script declarations -- move statements into a process, workflow, or function

  ```nextflow
  Channel
  ^^^^^^^
  ```

- Error: `workflows/deepmutscan.nf:74:1`: Statements cannot be mixed with script declarations -- move statements into a process, workflow, or function

  ```nextflow
  Channel
  ^^^^^^^
  ```

- Error: `workflows/deepmutscan.nf:79:1`: Statements cannot be mixed with script declarations -- move statements into a process, workflow, or function

  ```nextflow
  Channel
  ^^^^^^^
  ```

- Error: `workflows/deepmutscan.nf:84:1`: Statements cannot be mixed with script declarations -- move statements into a process, workflow, or function

  ```nextflow
  Channel
  ^^^^^^^
  ```

- Error: `workflows/deepmutscan.nf:89:1`: Statements cannot be mixed with script declarations -- move statements into a process, workflow, or function

  ```nextflow
  Channel
  ^^^^^^^
  ```

- Error: `workflows/deepmutscan.nf:94:1`: Statements cannot be mixed with script declarations -- move statements into a process, workflow, or function

  ```nextflow
  Channel
  ^^^^^^^
  ```

- Error: `workflows/deepmutscan.nf:101:1`: Statements cannot be mixed with script declarations -- move statements into a process, workflow, or function

  ```nextflow
  def R = { rel -> Channel.fromPath("${workflow.projectDir}/${rel}", checkIfExists: true) }
  ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  ```

- Error: `workflows/deepmutscan.nf:104:1`: Statements cannot be mixed with script declarations -- move statements into a process, workflow, or function

  ```nextflow
  R("modules/local/dmsanalysis/bin/SeqDepth_simulation.R").set { seqdepth_simulation_script_ch }
  ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  ```

- Error: `workflows/deepmutscan.nf:104:1`: `R` is not defined

  ```nextflow
  R("modules/local/dmsanalysis/bin/SeqDepth_simulation.R").set { seqdepth_simulation_script_ch }
  ^
  ```

- Error: `workflows/deepmutscan.nf:105:1`: Statements cannot be mixed with script declarations -- move statements into a process, workflow, or function

  ```nextflow
  R("modules/local/dmsanalysis/bin/aa_seq.R").set { aa_seq_script_ch }
  ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  ```

- Error: `workflows/deepmutscan.nf:105:1`: `R` is not defined

  ```nextflow
  R("modules/local/dmsanalysis/bin/aa_seq.R").set { aa_seq_script_ch }
  ^
  ```

- Error: `workflows/deepmutscan.nf:106:1`: Statements cannot be mixed with script declarations -- move statements into a process, workflow, or function

  ```nextflow
  R("modules/local/dmsanalysis/bin/complete_prefiltered_gatk.R").set { complete_gatk_script_ch }
  ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  ```

- Error: `workflows/deepmutscan.nf:106:1`: `R` is not defined

  ```nextflow
  R("modules/local/dmsanalysis/bin/complete_prefiltered_gatk.R").set { complete_gatk_script_ch }
  ^
  ```

- Error: `workflows/deepmutscan.nf:107:1`: Statements cannot be mixed with script declarations -- move statements into a process, workflow, or function

  ```nextflow
  R("modules/local/dmsanalysis/bin/counts_heatmap.R").set { counts_heatmap_script_ch }
  ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  ```

- Error: `workflows/deepmutscan.nf:107:1`: `R` is not defined

  ```nextflow
  R("modules/local/dmsanalysis/bin/counts_heatmap.R").set { counts_heatmap_script_ch }
  ^
  ```

- Error: `workflows/deepmutscan.nf:108:1`: Statements cannot be mixed with script declarations -- move statements into a process, workflow, or function

  ```nextflow
  R("modules/local/dmsanalysis/bin/counts_per_cov_heatmap.R").set { counts_per_cov_heatmap_script_ch }
  ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  ```

- Error: `workflows/deepmutscan.nf:108:1`: `R` is not defined

  ```nextflow
  R("modules/local/dmsanalysis/bin/counts_per_cov_heatmap.R").set { counts_per_cov_heatmap_script_ch }
  ^
  ```

- Error: `workflows/deepmutscan.nf:109:1`: Statements cannot be mixed with script declarations -- move statements into a process, workflow, or function

  ```nextflow
  R("modules/local/dmsanalysis/bin/detect_codons.R").set { detect_codons_script_ch }
  ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  ```

- Error: `workflows/deepmutscan.nf:109:1`: `R` is not defined

  ```nextflow
  R("modules/local/dmsanalysis/bin/detect_codons.R").set { detect_codons_script_ch }
  ^
  ```

- Error: `workflows/deepmutscan.nf:110:1`: Statements cannot be mixed with script declarations -- move statements into a process, workflow, or function

  ```nextflow
  R("modules/local/dmsanalysis/bin/filter_gatk_by_codon_library.R").set { filter_by_library_script_ch }
  ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  ```

- Error: `workflows/deepmutscan.nf:110:1`: `R` is not defined

  ```nextflow
  R("modules/local/dmsanalysis/bin/filter_gatk_by_codon_library.R").set { filter_by_library_script_ch }
  ^
  ```

- Error: `workflows/deepmutscan.nf:111:1`: Statements cannot be mixed with script declarations -- move statements into a process, workflow, or function

  ```nextflow
  R("modules/local/dmsanalysis/bin/fitness_heatmap.R").set { fitness_heatmap_script_ch }
  ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  ```

- Error: `workflows/deepmutscan.nf:111:1`: `R` is not defined

  ```nextflow
  R("modules/local/dmsanalysis/bin/fitness_heatmap.R").set { fitness_heatmap_script_ch }
  ^
  ```

- Error: `workflows/deepmutscan.nf:112:1`: Statements cannot be mixed with script declarations -- move statements into a process, workflow, or function

  ```nextflow
  R("modules/local/dmsanalysis/bin/gatk_to_fitness.R").set { gatk_to_fitness_script_ch }
  ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  ```

- Error: `workflows/deepmutscan.nf:112:1`: `R` is not defined

  ```nextflow
  R("modules/local/dmsanalysis/bin/gatk_to_fitness.R").set { gatk_to_fitness_script_ch }
  ^
  ```

- Error: `workflows/deepmutscan.nf:113:1`: Statements cannot be mixed with script declarations -- move statements into a process, workflow, or function

  ```nextflow
  R("modules/local/dmsanalysis/bin/global_position_biases_counts_and_counts_per_cov.R").set { global_bias_counts_cov_script_ch }
  ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  ```

- Error: `workflows/deepmutscan.nf:113:1`: `R` is not defined

  ```nextflow
  R("modules/local/dmsanalysis/bin/global_position_biases_counts_and_counts_per_cov.R").set { global_bias_counts_cov_script_ch }
  ^
  ```

- Error: `workflows/deepmutscan.nf:114:1`: Statements cannot be mixed with script declarations -- move statements into a process, workflow, or function

  ```nextflow
  R("modules/local/dmsanalysis/bin/global_position_biases_cov.R").set { global_bias_cov_script_ch }
  ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  ```

- Error: `workflows/deepmutscan.nf:114:1`: `R` is not defined

  ```nextflow
  R("modules/local/dmsanalysis/bin/global_position_biases_cov.R").set { global_bias_cov_script_ch }
  ^
  ```

- Error: `workflows/deepmutscan.nf:115:1`: Statements cannot be mixed with script declarations -- move statements into a process, workflow, or function

  ```nextflow
  R("modules/local/dmsanalysis/bin/install_packages.R").set { install_packages_script_ch }
  ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  ```

- Error: `workflows/deepmutscan.nf:115:1`: `R` is not defined

  ```nextflow
  R("modules/local/dmsanalysis/bin/install_packages.R").set { install_packages_script_ch }
  ^
  ```

- Error: `workflows/deepmutscan.nf:116:1`: Statements cannot be mixed with script declarations -- move statements into a process, workflow, or function

  ```nextflow
  R("modules/local/dmsanalysis/bin/logdiff.R").set { logdiff_script_ch }
  ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  ```

- Error: `workflows/deepmutscan.nf:116:1`: `R` is not defined

  ```nextflow
  R("modules/local/dmsanalysis/bin/logdiff.R").set { logdiff_script_ch }
  ^
  ```

- Error: `workflows/deepmutscan.nf:117:1`: Statements cannot be mixed with script declarations -- move statements into a process, workflow, or function

  ```nextflow
  R("modules/local/dmsanalysis/bin/low_count_variants.R").set { low_count_variants_script_ch }
  ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  ```

- Error: `workflows/deepmutscan.nf:117:1`: `R` is not defined

  ```nextflow
  R("modules/local/dmsanalysis/bin/low_count_variants.R").set { low_count_variants_script_ch }
  ^
  ```

- Error: `workflows/deepmutscan.nf:118:1`: Statements cannot be mixed with script declarations -- move statements into a process, workflow, or function

  ```nextflow
  R("modules/local/dmsanalysis/bin/possible_mutations.R").set { possible_mutations_script_ch }
  ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  ```

- Error: `workflows/deepmutscan.nf:118:1`: `R` is not defined

  ```nextflow
  R("modules/local/dmsanalysis/bin/possible_mutations.R").set { possible_mutations_script_ch }
  ^
  ```

- Error: `workflows/deepmutscan.nf:119:1`: Statements cannot be mixed with script declarations -- move statements into a process, workflow, or function

  ```nextflow
  R("modules/local/dmsanalysis/bin/prepare_gatk_data_for_count_heatmaps.R").set { prepare_counts_heatmap_script_ch }
  ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  ```

- Error: `workflows/deepmutscan.nf:119:1`: `R` is not defined

  ```nextflow
  R("modules/local/dmsanalysis/bin/prepare_gatk_data_for_count_heatmaps.R").set { prepare_counts_heatmap_script_ch }
  ^
  ```

- Error: `workflows/deepmutscan.nf:120:1`: Statements cannot be mixed with script declarations -- move statements into a process, workflow, or function

  ```nextflow
  R("modules/local/dmsanalysis/bin/prepare_gatk_data_for_fitness_heatmap.R").set { prepare_fitness_heatmap_script_ch }
  ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  ```

- Error: `workflows/deepmutscan.nf:120:1`: `R` is not defined

  ```nextflow
  R("modules/local/dmsanalysis/bin/prepare_gatk_data_for_fitness_heatmap.R").set { prepare_fitness_heatmap_script_ch }
  ^
  ```

- Error: `workflows/deepmutscan.nf:121:1`: Statements cannot be mixed with script declarations -- move statements into a process, workflow, or function

  ```nextflow
  R("modules/local/dmsanalysis/bin/process_raw_gatk.R").set { process_raw_gatk_script_ch }
  ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  ```

- Error: `workflows/deepmutscan.nf:121:1`: `R` is not defined

  ```nextflow
  R("modules/local/dmsanalysis/bin/process_raw_gatk.R").set { process_raw_gatk_script_ch }
  ^
  ```

- Error: `workflows/deepmutscan.nf:122:1`: Statements cannot be mixed with script declarations -- move statements into a process, workflow, or function

  ```nextflow
  R("modules/local/dmsanalysis/bin/merge_counts.R").set { merge_counts_script_ch }
  ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  ```

- Error: `workflows/deepmutscan.nf:122:1`: `R` is not defined

  ```nextflow
  R("modules/local/dmsanalysis/bin/merge_counts.R").set { merge_counts_script_ch }
  ^
  ```

- Error: `workflows/deepmutscan.nf:123:1`: Statements cannot be mixed with script declarations -- move statements into a process, workflow, or function

  ```nextflow
  R("modules/local/dmsanalysis/bin/dimsum_experimentalDesign.R").set { exp_design_ch }
  ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  ```

- Error: `workflows/deepmutscan.nf:123:1`: `R` is not defined

  ```nextflow
  R("modules/local/dmsanalysis/bin/dimsum_experimentalDesign.R").set { exp_design_ch }
  ^
  ```

- Error: `workflows/deepmutscan.nf:124:1`: Statements cannot be mixed with script declarations -- move statements into a process, workflow, or function

  ```nextflow
  R("modules/local/dmsanalysis/bin/fitness_calculation.R").set { fitness_calculation_script_ch }
  ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  ```

- Error: `workflows/deepmutscan.nf:124:1`: `R` is not defined

  ```nextflow
  R("modules/local/dmsanalysis/bin/fitness_calculation.R").set { fitness_calculation_script_ch }
  ^
  ```

- Error: `workflows/deepmutscan.nf:125:1`: Statements cannot be mixed with script declarations -- move statements into a process, workflow, or function

  ```nextflow
  R("modules/local/dmsanalysis/bin/fitness_QC.R").set { fitness_QC_script_ch }
  ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  ```

- Error: `workflows/deepmutscan.nf:125:1`: `R` is not defined

  ```nextflow
  R("modules/local/dmsanalysis/bin/fitness_QC.R").set { fitness_QC_script_ch }
  ^
  ```

- Error: `workflows/deepmutscan.nf:126:1`: Statements cannot be mixed with script declarations -- move statements into a process, workflow, or function

  ```nextflow
  R("modules/local/dmsanalysis/bin/fitness_heatmap.R").set { fitness_heatmap_script_ch }
  ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  ```

- Error: `workflows/deepmutscan.nf:126:1`: `R` is not defined

  ```nextflow
  R("modules/local/dmsanalysis/bin/fitness_heatmap.R").set { fitness_heatmap_script_ch }
  ^
  ```

- Error: `workflows/deepmutscan.nf:127:1`: Statements cannot be mixed with script declarations -- move statements into a process, workflow, or function

  ```nextflow
  R("modules/local/dmsanalysis/bin/find_syn_mutation.R").set { syn_mut_ch }
  ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  ```

- Error: `workflows/deepmutscan.nf:127:1`: `R` is not defined

  ```nextflow
  R("modules/local/dmsanalysis/bin/find_syn_mutation.R").set { syn_mut_ch }
  ^
  ```

- Error: `workflows/deepmutscan.nf:205:9`: `ch_fasta` is not defined

  ```nextflow
          ch_fasta
          ^^^^^^^^
  ```

- Error: `workflows/deepmutscan.nf:217:26`: `ch_fasta` is not defined

  ```nextflow
      ch_fasta_broadcast = ch_fasta
                           ^^^^^^^^
  ```

- Error: `workflows/deepmutscan.nf:237:31`: `ch_fasta` is not defined

  ```nextflow
      ch_fasta_path_broadcast = ch_fasta
                                ^^^^^^^^
  ```

- Error: `workflows/deepmutscan.nf:247:26`: `ch_fasta` is not defined

  ```nextflow
      ch_fasta_for_gatk  = ch_fasta.combine(PREMERGE.out.bam).map { it[1] }     // path -- N
                           ^^^^^^^^
  ```

- Error: `workflows/deepmutscan.nf:249:26`: `reading_frame_ch` is not defined

  ```nextflow
      ch_rf_for_gatk     = reading_frame_ch.combine(PREMERGE.out.bam).map { it[0] }  // val  -- N
                           ^^^^^^^^^^^^^^^^
  ```

- Error: `workflows/deepmutscan.nf:251:26`: `min_counts_ch` is not defined

  ```nextflow
      ch_min_for_gatk    = min_counts_ch.combine(PREMERGE.out.bam).map { it[0] }     // val  -- N
                           ^^^^^^^^^^^^^
  ```

- Error: `workflows/deepmutscan.nf:261:5`: `ch_fasta` is not defined

  ```nextflow
      ch_fasta,
      ^^^^^^^^
  ```

- Error: `workflows/deepmutscan.nf:262:5`: `reading_frame_ch` is not defined

  ```nextflow
      reading_frame_ch,
      ^^^^^^^^^^^^^^^^
  ```

- Error: `workflows/deepmutscan.nf:263:5`: `aa_seq_script_ch` is not defined

  ```nextflow
      aa_seq_script_ch // path to aa_seq.R (defined at the top)
      ^^^^^^^^^^^^^^^^
  ```

- Error: `workflows/deepmutscan.nf:268:5`: `ch_fasta` is not defined

  ```nextflow
      ch_fasta,
      ^^^^^^^^
  ```

- Error: `workflows/deepmutscan.nf:269:5`: `reading_frame_ch` is not defined

  ```nextflow
      reading_frame_ch,          // pos_range (as val)
      ^^^^^^^^^^^^^^^^
  ```

- Error: `workflows/deepmutscan.nf:270:5`: `mutagenesis_type_ch` is not defined

  ```nextflow
      mutagenesis_type_ch,       // mutagenesis_type (as val)
      ^^^^^^^^^^^^^^^^^^^
  ```

- Error: `workflows/deepmutscan.nf:271:5`: `custom_codon_library_ch` is not defined

  ```nextflow
      custom_codon_library_ch,   // custom_codon_library (as path)
      ^^^^^^^^^^^^^^^^^^^^^^^
  ```

- Error: `workflows/deepmutscan.nf:272:5`: `possible_mutations_script_ch` is not defined

  ```nextflow
      possible_mutations_script_ch  // path to R script
      ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  ```

- Error: `workflows/deepmutscan.nf:283:32`: `fanout` is not defined

  ```nextflow
      ch_possible_mut_for_proc = fanout( DMSANALYSIS_POSSIBLE_MUTATIONS.out.possible_mutations.map { it[1] } )
                                 ^^^^^^
  ```

- Error: `workflows/deepmutscan.nf:284:32`: `fanout` is not defined

  ```nextflow
      ch_aa_seq_for_proc       = fanout( DMSANALYSIS_AASEQ.out.aa_seq.map { it[1] } )
                                 ^^^^^^
  ```

- Error: `workflows/deepmutscan.nf:285:32`: `fanout` is not defined

  ```nextflow
      ch_min_counts_for_proc   = fanout( min_counts_ch )
                                 ^^^^^^
  ```

- Error: `workflows/deepmutscan.nf:285:40`: `min_counts_ch` is not defined

  ```nextflow
      ch_min_counts_for_proc   = fanout( min_counts_ch )
                                         ^^^^^^^^^^^^^
  ```

- Error: `workflows/deepmutscan.nf:286:32`: `fanout` is not defined

  ```nextflow
      ch_proc_raw_script       = fanout( process_raw_gatk_script_ch )
                                 ^^^^^^
  ```

- Error: `workflows/deepmutscan.nf:286:40`: `process_raw_gatk_script_ch` is not defined

  ```nextflow
      ch_proc_raw_script       = fanout( process_raw_gatk_script_ch )
                                         ^^^^^^^^^^^^^^^^^^^^^^^^^^
  ```

- Error: `workflows/deepmutscan.nf:287:32`: `fanout` is not defined

  ```nextflow
      ch_filter_lib_script     = fanout( filter_by_library_script_ch )
                                 ^^^^^^
  ```

- Error: `workflows/deepmutscan.nf:287:40`: `filter_by_library_script_ch` is not defined

  ```nextflow
      ch_filter_lib_script     = fanout( filter_by_library_script_ch )
                                         ^^^^^^^^^^^^^^^^^^^^^^^^^^^
  ```

- Error: `workflows/deepmutscan.nf:288:32`: `fanout` is not defined

  ```nextflow
      ch_complete_script       = fanout( complete_gatk_script_ch )
                                 ^^^^^^
  ```

- Error: `workflows/deepmutscan.nf:288:40`: `complete_gatk_script_ch` is not defined

  ```nextflow
      ch_complete_script       = fanout( complete_gatk_script_ch )
                                         ^^^^^^^^^^^^^^^^^^^^^^^
  ```

- Error: `workflows/deepmutscan.nf:289:32`: `fanout` is not defined

  ```nextflow
      ch_prepare_heatmap_script= fanout( prepare_counts_heatmap_script_ch )
                                 ^^^^^^
  ```

- Error: `workflows/deepmutscan.nf:289:40`: `prepare_counts_heatmap_script_ch` is not defined

  ```nextflow
      ch_prepare_heatmap_script= fanout( prepare_counts_heatmap_script_ch )
                                         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  ```

- Error: `workflows/deepmutscan.nf:312:38`: `fanoutTo` is not defined

  ```nextflow
      min_counts_for_cov_ch          = fanoutTo(variantCounts_for_heatmaps_ch, min_counts_ch)
                                       ^^^^^^^^
  ```

- Error: `workflows/deepmutscan.nf:312:78`: `min_counts_ch` is not defined

  ```nextflow
      min_counts_for_cov_ch          = fanoutTo(variantCounts_for_heatmaps_ch, min_counts_ch)
                                                                               ^^^^^^^^^^^^^
  ```

- Error: `workflows/deepmutscan.nf:313:38`: `fanoutTo` is not defined

  ```nextflow
      counts_per_cov_heatmap_scriptN = fanoutTo(variantCounts_for_heatmaps_ch, counts_per_cov_heatmap_script_ch)
                                       ^^^^^^^^
  ```

- Error: `workflows/deepmutscan.nf:313:78`: `counts_per_cov_heatmap_script_ch` is not defined

  ```nextflow
      counts_per_cov_heatmap_scriptN = fanoutTo(variantCounts_for_heatmaps_ch, counts_per_cov_heatmap_script_ch)
                                                                               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  ```

- Error: `workflows/deepmutscan.nf:316:38`: `fanoutTo` is not defined

  ```nextflow
      min_counts_for_heatmap_ch      = fanoutTo(variantCounts_for_heatmaps_ch, min_counts_ch)
                                       ^^^^^^^^
  ```

- Error: `workflows/deepmutscan.nf:316:78`: `min_counts_ch` is not defined

  ```nextflow
      min_counts_for_heatmap_ch      = fanoutTo(variantCounts_for_heatmaps_ch, min_counts_ch)
                                                                               ^^^^^^^^^^^^^
  ```

- Error: `workflows/deepmutscan.nf:317:38`: `fanoutTo` is not defined

  ```nextflow
      counts_heatmap_scriptN         = fanoutTo(variantCounts_for_heatmaps_ch, counts_heatmap_script_ch)
                                       ^^^^^^^^
  ```

- Error: `workflows/deepmutscan.nf:317:78`: `counts_heatmap_script_ch` is not defined

  ```nextflow
      counts_heatmap_scriptN         = fanoutTo(variantCounts_for_heatmaps_ch, counts_heatmap_script_ch)
                                                                               ^^^^^^^^^^^^^^^^^^^^^^^^
  ```

- Error: `workflows/deepmutscan.nf:320:38`: `fanoutTo` is not defined

  ```nextflow
      aa_seq_for_bias_ch             = fanoutTo(variantCounts_filtered_by_library_ch, DMSANALYSIS_AASEQ.out.aa_seq.map { it[1] })
                                       ^^^^^^^^
  ```

- Error: `workflows/deepmutscan.nf:321:38`: `fanoutTo` is not defined

  ```nextflow
      sliding_window_size_N          = fanoutTo(variantCounts_filtered_by_library_ch, sliding_window_size_ch)
                                       ^^^^^^^^
  ```

- Error: `workflows/deepmutscan.nf:321:85`: `sliding_window_size_ch` is not defined

  ```nextflow
      sliding_window_size_N          = fanoutTo(variantCounts_filtered_by_library_ch, sliding_window_size_ch)
                                                                                      ^^^^^^^^^^^^^^^^^^^^^^
  ```

- Error: `workflows/deepmutscan.nf:322:38`: `fanoutTo` is not defined

  ```nextflow
      aimed_cov_N                    = fanoutTo(variantCounts_filtered_by_library_ch, aimed_cov_ch)
                                       ^^^^^^^^
  ```

- Error: `workflows/deepmutscan.nf:322:85`: `aimed_cov_ch` is not defined

  ```nextflow
      aimed_cov_N                    = fanoutTo(variantCounts_filtered_by_library_ch, aimed_cov_ch)
                                                                                      ^^^^^^^^^^^^
  ```

- Error: `workflows/deepmutscan.nf:323:38`: `fanoutTo` is not defined

  ```nextflow
      global_bias_counts_cov_scriptN = fanoutTo(variantCounts_filtered_by_library_ch, global_bias_counts_cov_script_ch)
                                       ^^^^^^^^
  ```

- Error: `workflows/deepmutscan.nf:323:85`: `global_bias_counts_cov_script_ch` is not defined

  ```nextflow
      global_bias_counts_cov_scriptN = fanoutTo(variantCounts_filtered_by_library_ch, global_bias_counts_cov_script_ch)
                                                                                      ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  ```

- Error: `workflows/deepmutscan.nf:324:38`: `fanoutTo` is not defined

  ```nextflow
      global_bias_cov_scriptN        = fanoutTo(variantCounts_filtered_by_library_ch, global_bias_cov_script_ch)
                                       ^^^^^^^^
  ```

- Error: `workflows/deepmutscan.nf:324:85`: `global_bias_cov_script_ch` is not defined

  ```nextflow
      global_bias_cov_scriptN        = fanoutTo(variantCounts_filtered_by_library_ch, global_bias_cov_script_ch)
                                                                                      ^^^^^^^^^^^^^^^^^^^^^^^^^
  ```

- Error: `workflows/deepmutscan.nf:327:34`: `fanoutTo` is not defined

  ```nextflow
  logdiff_scriptN                = fanoutTo(library_completed_variantCounts_ch, logdiff_script_ch)
                                   ^^^^^^^^
  ```

- Error: `workflows/deepmutscan.nf:327:79`: `logdiff_script_ch` is not defined

  ```nextflow
  logdiff_scriptN                = fanoutTo(library_completed_variantCounts_ch, logdiff_script_ch)
                                                                                ^^^^^^^^^^^^^^^^^
  ```

- Error: `workflows/deepmutscan.nf:330:38`: `fanoutTo` is not defined

  ```nextflow
      possible_mutations_N           = fanoutTo(variantCounts_filtered_by_library_ch, DMSANALYSIS_POSSIBLE_MUTATIONS.out.possible_mutations.map { it[1] })
                                       ^^^^^^^^
  ```

- Error: `workflows/deepmutscan.nf:331:38`: `fanoutTo` is not defined

  ```nextflow
      min_counts_for_seqdepth_ch     = fanoutTo(variantCounts_filtered_by_library_ch, min_counts_ch)
                                       ^^^^^^^^
  ```

- Error: `workflows/deepmutscan.nf:331:85`: `min_counts_ch` is not defined

  ```nextflow
      min_counts_for_seqdepth_ch     = fanoutTo(variantCounts_filtered_by_library_ch, min_counts_ch)
                                                                                      ^^^^^^^^^^^^^
  ```

- Error: `workflows/deepmutscan.nf:332:38`: `fanoutTo` is not defined

  ```nextflow
      seqdepth_simulation_scriptN    = fanoutTo(variantCounts_filtered_by_library_ch, seqdepth_simulation_script_ch)
                                       ^^^^^^^^
  ```

- Error: `workflows/deepmutscan.nf:332:85`: `seqdepth_simulation_script_ch` is not defined

  ```nextflow
      seqdepth_simulation_scriptN    = fanoutTo(variantCounts_filtered_by_library_ch, seqdepth_simulation_script_ch)
                                                                                      ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  ```

- Error: `workflows/deepmutscan.nf:376:31`: `ch_fasta` is not defined

  ```nextflow
      ch_fasta_for_fitness    = ch_fasta.combine(variantCounts_filtered_by_library_ch).map { it[1] }   // path(fasta) -- N
                                ^^^^^^^^
  ```

- Error: `workflows/deepmutscan.nf:377:31`: `reading_frame_ch` is not defined

  ```nextflow
      ch_rf_for_fitness       = reading_frame_ch.combine(variantCounts_filtered_by_library_ch).map { it[0] }  // val(range) -- N
                                ^^^^^^^^^^^^^^^^
  ```

- Error: `workflows/deepmutscan.nf:378:31`: `gatk_to_fitness_script_ch` is not defined

  ```nextflow
      ch_script_for_fitness   = gatk_to_fitness_script_ch.combine(variantCounts_filtered_by_library_ch).map { it[0] } // path(script) -- N
                                ^^^^^^^^^^^^^^^^^^^^^^^^^
  ```

- Error: `workflows/deepmutscan.nf:411:36`: `merge_counts_script_ch` is not defined

  ```nextflow
      def ch_merge_script_for_each = merge_counts_script_ch
                                     ^^^^^^^^^^^^^^^^^^^^^^
  ```

- Error: `workflows/deepmutscan.nf:426:9`: `ch_samplesheet_csv` is not defined

  ```nextflow
          ch_samplesheet_csv,   // path to CSV
          ^^^^^^^^^^^^^^^^^^
  ```

- Error: `workflows/deepmutscan.nf:427:9`: `exp_design_ch` is not defined

  ```nextflow
          exp_design_ch         // path to R script
          ^^^^^^^^^^^^^
  ```

- Error: `workflows/deepmutscan.nf:434:1`: `ch_fasta` is not defined

  ```nextflow
  ch_fasta.map { it[1] }.set { ch_fasta_path }   // path(/…/GID1A.fasta)
  ^^^^^^^^
  ```

- Error: `workflows/deepmutscan.nf:441:5`: `reading_frame_ch` is not defined

  ```nextflow
      reading_frame_ch.combine(MERGE_COUNTS.out.merged_counts).map { it[0] }, // val pos_range (broadcast)
      ^^^^^^^^^^^^^^^^
  ```

- Error: `workflows/deepmutscan.nf:442:5`: `syn_mut_ch` is not defined

  ```nextflow
      syn_mut_ch.combine(MERGE_COUNTS.out.merged_counts).map { it[0] }     // path R script (broadcast)
      ^^^^^^^^^^
  ```

- Error: `workflows/deepmutscan.nf:487:5`: `fitness_calculation_script_ch` is not defined

  ```nextflow
      fitness_calculation_script_ch
      ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  ```

- Error: `workflows/deepmutscan.nf:492:5`: `fitness_QC_script_ch` is not defined

  ```nextflow
      fitness_QC_script_ch
      ^^^^^^^^^^^^^^^^^^^^
  ```

- Error: `workflows/deepmutscan.nf:498:5`: `fitness_heatmap_script_ch` is not defined

  ```nextflow
      fitness_heatmap_script_ch
      ^^^^^^^^^^^^^^^^^^^^^^^^^
  ```

## :warning: Warnings

- Warning: `modules/local/bamprocessing/bamfilteringdms.nf:22:9`: Variable was declared but not used

  ```nextflow
      def args = task.ext.args ?: ''
          ^^^^
  ```

- Warning: `modules/local/bamprocessing/bamfilteringdms.nf:23:9`: Variable was declared but not used

  ```nextflow
      def prefix = task.ext.prefix ?: "${meta.id}"
          ^^^^^^
  ```

- Warning: `modules/local/bamprocessing/bamfilteringdms.nf:39:9`: Variable was declared but not used

  ```nextflow
      def args = task.ext.args ?: ''
          ^^^^
  ```

- Warning: `modules/local/bamprocessing/premerge.nf:41:9`: Variable was declared but not used

  ```nextflow
      def prefix = task.ext.prefix ?: "${meta.id}"
          ^^^^^^
  ```

- Warning: `modules/local/fitness/fitness_standard.nf:102:15`: Variable was declared but not used

  ```nextflow
      tuple val(sample), path(fitness_estimation_tsv)   // from FITNESS_CALCULATION
                ^^^^^^
  ```

- Warning: `modules/local/fitness/merge_counts.nf:19:42`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
    def in_list  = input_counts .collect { it.getName() }.join(' ')
                                           ^^
  ```

- Warning: `modules/local/fitness/merge_counts.nf:20:42`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
    def out_list = output_counts.collect { it.getName() }.join(' ')
                                           ^^
  ```

- Warning: `modules/local/gatk/saturationmutagenesis.nf:23:9`: Variable was declared but not used

  ```nextflow
      def prefix = task.ext.prefix ?: "${meta.id}"
          ^^^^^^
  ```

- Warning: `modules/local/gatk/saturationmutagenesis.nf:51:9`: Variable was declared but not used

  ```nextflow
      def prefix = task.ext.prefix ?: "${meta.id}"
          ^^^^^^
  ```

- Warning: `subworkflows/local/utils_nfcore_deepmutscan_pipeline/main.nf:32:5`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
      monochrome_logs   // boolean: Do not use coloured log outputs
      ^^^^^^^^^^^^^^^
  ```

- Warning: `subworkflows/local/utils_nfcore_deepmutscan_pipeline/main.nf:35:5`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
      input             //  string: Path to input samplesheet
      ^^^^^
  ```

- Warning: `subworkflows/local/utils_nfcore_deepmutscan_pipeline/main.nf:42:19`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_versions = Channel.empty()
                    ^^^^^^^
  ```

- Warning: `subworkflows/local/utils_nfcore_deepmutscan_pipeline/main.nf:67:144`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
      after_text = """${workflow.manifest.doi ? "\n* The pipeline\n" : ""}${workflow.manifest.doi.tokenize(",").collect { "    https://doi.org/${it.trim().replace('https://doi.org/','')}"}.join("\n")}${workflow.manifest.doi ? "\n" : ""}
                                                                                                                                                 ^^
  ```

- Warning: `subworkflows/local/utils_nfcore_deepmutscan_pipeline/main.nf:104:5`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      Channel
      ^^^^^^^
  ```

- Warning: `subworkflows/nf-core/utils_nfcore_pipeline/main.nf:101:98`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      return ch_versions.unique().map { version -> processVersionsFromYAML(version) }.unique().mix(Channel.of(workflowVersionToYAML()))
                                                                                                   ^^^^^^^
  ```

- Warning: `workflows/deepmutscan.nf:53:1`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
  Channel
  ^^^^^^^
  ```

- Warning: `workflows/deepmutscan.nf:56:12`: Variable was declared but not used

  ```nextflow
      .set { ch_fasta }
             ^^^^^^^^
  ```

- Warning: `workflows/deepmutscan.nf:59:1`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
  Channel
  ^^^^^^^
  ```

- Warning: `workflows/deepmutscan.nf:61:12`: Variable was declared but not used

  ```nextflow
      .set { reading_frame_ch }
             ^^^^^^^^^^^^^^^^
  ```

- Warning: `workflows/deepmutscan.nf:64:1`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
  Channel
  ^^^^^^^
  ```

- Warning: `workflows/deepmutscan.nf:66:12`: Variable was declared but not used

  ```nextflow
      .set { min_counts_ch }
             ^^^^^^^^^^^^^
  ```

- Warning: `workflows/deepmutscan.nf:69:1`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
  Channel
  ^^^^^^^
  ```

- Warning: `workflows/deepmutscan.nf:71:12`: Variable was declared but not used

  ```nextflow
      .set { custom_codon_library_ch }
             ^^^^^^^^^^^^^^^^^^^^^^^
  ```

- Warning: `workflows/deepmutscan.nf:74:1`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
  Channel
  ^^^^^^^
  ```

- Warning: `workflows/deepmutscan.nf:76:12`: Variable was declared but not used

  ```nextflow
      .set { mutagenesis_type_ch }
             ^^^^^^^^^^^^^^^^^^^
  ```

- Warning: `workflows/deepmutscan.nf:79:1`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
  Channel
  ^^^^^^^
  ```

- Warning: `workflows/deepmutscan.nf:81:12`: Variable was declared but not used

  ```nextflow
      .set { sliding_window_size_ch }
             ^^^^^^^^^^^^^^^^^^^^^^
  ```

- Warning: `workflows/deepmutscan.nf:84:1`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
  Channel
  ^^^^^^^
  ```

- Warning: `workflows/deepmutscan.nf:86:12`: Variable was declared but not used

  ```nextflow
      .set { aimed_cov_ch }
             ^^^^^^^^^^^^
  ```

- Warning: `workflows/deepmutscan.nf:89:1`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
  Channel
  ^^^^^^^
  ```

- Warning: `workflows/deepmutscan.nf:91:12`: Variable was declared but not used

  ```nextflow
      .set { run_seqdepth_ch }
             ^^^^^^^^^^^^^^^
  ```

- Warning: `workflows/deepmutscan.nf:94:1`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
  Channel
  ^^^^^^^
  ```

- Warning: `workflows/deepmutscan.nf:96:10`: Variable was declared but not used

  ```nextflow
    .set { ch_samplesheet_csv }
           ^^^^^^^^^^^^^^^^^^
  ```

- Warning: `workflows/deepmutscan.nf:101:5`: Variable was declared but not used

  ```nextflow
  def R = { rel -> Channel.fromPath("${workflow.projectDir}/${rel}", checkIfExists: true) }
      ^
  ```

- Warning: `workflows/deepmutscan.nf:101:18`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
  def R = { rel -> Channel.fromPath("${workflow.projectDir}/${rel}", checkIfExists: true) }
                   ^^^^^^^
  ```

- Warning: `workflows/deepmutscan.nf:104:64`: Variable was declared but not used

  ```nextflow
  R("modules/local/dmsanalysis/bin/SeqDepth_simulation.R").set { seqdepth_simulation_script_ch }
                                                                 ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  ```

- Warning: `workflows/deepmutscan.nf:105:51`: Variable was declared but not used

  ```nextflow
  R("modules/local/dmsanalysis/bin/aa_seq.R").set { aa_seq_script_ch }
                                                    ^^^^^^^^^^^^^^^^
  ```

- Warning: `workflows/deepmutscan.nf:106:70`: Variable was declared but not used

  ```nextflow
  R("modules/local/dmsanalysis/bin/complete_prefiltered_gatk.R").set { complete_gatk_script_ch }
                                                                       ^^^^^^^^^^^^^^^^^^^^^^^
  ```

- Warning: `workflows/deepmutscan.nf:107:59`: Variable was declared but not used

  ```nextflow
  R("modules/local/dmsanalysis/bin/counts_heatmap.R").set { counts_heatmap_script_ch }
                                                            ^^^^^^^^^^^^^^^^^^^^^^^^
  ```

- Warning: `workflows/deepmutscan.nf:108:67`: Variable was declared but not used

  ```nextflow
  R("modules/local/dmsanalysis/bin/counts_per_cov_heatmap.R").set { counts_per_cov_heatmap_script_ch }
                                                                    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  ```

- Warning: `workflows/deepmutscan.nf:109:58`: Variable was declared but not used

  ```nextflow
  R("modules/local/dmsanalysis/bin/detect_codons.R").set { detect_codons_script_ch }
                                                           ^^^^^^^^^^^^^^^^^^^^^^^
  ```

- Warning: `workflows/deepmutscan.nf:110:73`: Variable was declared but not used

  ```nextflow
  R("modules/local/dmsanalysis/bin/filter_gatk_by_codon_library.R").set { filter_by_library_script_ch }
                                                                          ^^^^^^^^^^^^^^^^^^^^^^^^^^^
  ```

- Warning: `workflows/deepmutscan.nf:112:60`: Variable was declared but not used

  ```nextflow
  R("modules/local/dmsanalysis/bin/gatk_to_fitness.R").set { gatk_to_fitness_script_ch }
                                                             ^^^^^^^^^^^^^^^^^^^^^^^^^
  ```

- Warning: `workflows/deepmutscan.nf:113:93`: Variable was declared but not used

  ```nextflow
  R("modules/local/dmsanalysis/bin/global_position_biases_counts_and_counts_per_cov.R").set { global_bias_counts_cov_script_ch }
                                                                                              ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  ```

- Warning: `workflows/deepmutscan.nf:114:71`: Variable was declared but not used

  ```nextflow
  R("modules/local/dmsanalysis/bin/global_position_biases_cov.R").set { global_bias_cov_script_ch }
                                                                        ^^^^^^^^^^^^^^^^^^^^^^^^^
  ```

- Warning: `workflows/deepmutscan.nf:115:61`: Variable was declared but not used

  ```nextflow
  R("modules/local/dmsanalysis/bin/install_packages.R").set { install_packages_script_ch }
                                                              ^^^^^^^^^^^^^^^^^^^^^^^^^^
  ```

- Warning: `workflows/deepmutscan.nf:116:52`: Variable was declared but not used

  ```nextflow
  R("modules/local/dmsanalysis/bin/logdiff.R").set { logdiff_script_ch }
                                                     ^^^^^^^^^^^^^^^^^
  ```

- Warning: `workflows/deepmutscan.nf:117:63`: Variable was declared but not used

  ```nextflow
  R("modules/local/dmsanalysis/bin/low_count_variants.R").set { low_count_variants_script_ch }
                                                                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  ```

- Warning: `workflows/deepmutscan.nf:118:63`: Variable was declared but not used

  ```nextflow
  R("modules/local/dmsanalysis/bin/possible_mutations.R").set { possible_mutations_script_ch }
                                                                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  ```

- Warning: `workflows/deepmutscan.nf:119:81`: Variable was declared but not used

  ```nextflow
  R("modules/local/dmsanalysis/bin/prepare_gatk_data_for_count_heatmaps.R").set { prepare_counts_heatmap_script_ch }
                                                                                  ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  ```

- Warning: `workflows/deepmutscan.nf:120:82`: Variable was declared but not used

  ```nextflow
  R("modules/local/dmsanalysis/bin/prepare_gatk_data_for_fitness_heatmap.R").set { prepare_fitness_heatmap_script_ch }
                                                                                   ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  ```

- Warning: `workflows/deepmutscan.nf:121:61`: Variable was declared but not used

  ```nextflow
  R("modules/local/dmsanalysis/bin/process_raw_gatk.R").set { process_raw_gatk_script_ch }
                                                              ^^^^^^^^^^^^^^^^^^^^^^^^^^
  ```

- Warning: `workflows/deepmutscan.nf:122:57`: Variable was declared but not used

  ```nextflow
  R("modules/local/dmsanalysis/bin/merge_counts.R").set { merge_counts_script_ch }
                                                          ^^^^^^^^^^^^^^^^^^^^^^
  ```

- Warning: `workflows/deepmutscan.nf:123:70`: Variable was declared but not used

  ```nextflow
  R("modules/local/dmsanalysis/bin/dimsum_experimentalDesign.R").set { exp_design_ch }
                                                                       ^^^^^^^^^^^^^
  ```

- Warning: `workflows/deepmutscan.nf:124:64`: Variable was declared but not used

  ```nextflow
  R("modules/local/dmsanalysis/bin/fitness_calculation.R").set { fitness_calculation_script_ch }
                                                                 ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  ```

- Warning: `workflows/deepmutscan.nf:125:55`: Variable was declared but not used

  ```nextflow
  R("modules/local/dmsanalysis/bin/fitness_QC.R").set { fitness_QC_script_ch }
                                                        ^^^^^^^^^^^^^^^^^^^^
  ```

- Warning: `workflows/deepmutscan.nf:127:62`: Variable was declared but not used

  ```nextflow
  R("modules/local/dmsanalysis/bin/find_syn_mutation.R").set { syn_mut_ch }
                                                               ^^^^^^^^^^
  ```

- Warning: `workflows/deepmutscan.nf:137:19`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_versions = Channel.empty()
                    ^^^^^^^
  ```

- Warning: `workflows/deepmutscan.nf:138:24`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_multiqc_files = Channel.empty()
                         ^^^^^^^
  ```

- Warning: `workflows/deepmutscan.nf:146:68`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
      ch_multiqc_files = ch_multiqc_files.mix(FASTQC.out.zip.collect{it[1]})
                                                                     ^^
  ```

- Warning: `workflows/deepmutscan.nf:164:32`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_multiqc_config        = Channel.fromPath(
                                 ^^^^^^^
  ```

- Warning: `workflows/deepmutscan.nf:167:9`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
          Channel.fromPath(params.multiqc_config, checkIfExists: true) :
          ^^^^^^^
  ```

- Warning: `workflows/deepmutscan.nf:168:9`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
          Channel.empty()
          ^^^^^^^
  ```

- Warning: `workflows/deepmutscan.nf:170:9`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
          Channel.fromPath(params.multiqc_logo, checkIfExists: true) :
          ^^^^^^^
  ```

- Warning: `workflows/deepmutscan.nf:171:9`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
          Channel.empty()
          ^^^^^^^
  ```

- Warning: `workflows/deepmutscan.nf:175:27`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_workflow_summary = Channel.value(paramsSummaryMultiqc(summary_params))
                            ^^^^^^^
  ```

- Warning: `workflows/deepmutscan.nf:181:45`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_methods_description                = Channel.value(
                                              ^^^^^^^
  ```

- Warning: `workflows/deepmutscan.nf:214:15`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
        .map { [it[2], it[3]] }
                ^^
  ```

- Warning: `workflows/deepmutscan.nf:214:22`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
        .map { [it[2], it[3]] }
                       ^^
  ```

- Warning: `workflows/deepmutscan.nf:219:15`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
        .map { [it[0], it[1]] }
                ^^
  ```

- Warning: `workflows/deepmutscan.nf:219:22`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
        .map { [it[0], it[1]] }
                       ^^
  ```

- Warning: `workflows/deepmutscan.nf:239:14`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
        .map { it[1] }                    // keep only the fasta path (N emissions)
               ^^
  ```

- Warning: `workflows/deepmutscan.nf:247:67`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
      ch_fasta_for_gatk  = ch_fasta.combine(PREMERGE.out.bam).map { it[1] }     // path -- N
                                                                    ^^
  ```

- Warning: `workflows/deepmutscan.nf:249:75`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
      ch_rf_for_gatk     = reading_frame_ch.combine(PREMERGE.out.bam).map { it[0] }  // val  -- N
                                                                            ^^
  ```

- Warning: `workflows/deepmutscan.nf:251:72`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
      ch_min_for_gatk    = min_counts_ch.combine(PREMERGE.out.bam).map { it[0] }     // val  -- N
                                                                         ^^
  ```

- Warning: `workflows/deepmutscan.nf:280:9`: Variable was declared but not used

  ```nextflow
      def fanout = { ch_singleton -> ch_singleton.combine(ch_vc).map { it[0] } }
          ^^^^^^
  ```

- Warning: `workflows/deepmutscan.nf:280:70`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
      def fanout = { ch_singleton -> ch_singleton.combine(ch_vc).map { it[0] } }
                                                                       ^^
  ```

- Warning: `workflows/deepmutscan.nf:283:100`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
      ch_possible_mut_for_proc = fanout( DMSANALYSIS_POSSIBLE_MUTATIONS.out.possible_mutations.map { it[1] } )
                                                                                                     ^^
  ```

- Warning: `workflows/deepmutscan.nf:284:75`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
      ch_aa_seq_for_proc       = fanout( DMSANALYSIS_AASEQ.out.aa_seq.map { it[1] } )
                                                                            ^^
  ```

- Warning: `workflows/deepmutscan.nf:303:5`: Variable was declared but not used

  ```nextflow
      annotated_variantCounts_ch = DMSANALYSIS_PROCESS_GATK.out.processed_variantCounts.map { meta, a, b, c, d -> tuple(meta, a) }
      ^^^^^^^^^^^^^^^^^^^^^^^^^^
  ```

- Warning: `workflows/deepmutscan.nf:303:102`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
      annotated_variantCounts_ch = DMSANALYSIS_PROCESS_GATK.out.processed_variantCounts.map { meta, a, b, c, d -> tuple(meta, a) }
                                                                                                       ^
  ```

- Warning: `workflows/deepmutscan.nf:303:105`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
      annotated_variantCounts_ch = DMSANALYSIS_PROCESS_GATK.out.processed_variantCounts.map { meta, a, b, c, d -> tuple(meta, a) }
                                                                                                          ^
  ```

- Warning: `workflows/deepmutscan.nf:303:108`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
      annotated_variantCounts_ch = DMSANALYSIS_PROCESS_GATK.out.processed_variantCounts.map { meta, a, b, c, d -> tuple(meta, a) }
                                                                                                             ^
  ```

- Warning: `workflows/deepmutscan.nf:304:109`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
      variantCounts_filtered_by_library_ch = DMSANALYSIS_PROCESS_GATK.out.processed_variantCounts.map { meta, a, b, c, d -> tuple(meta, b) }
                                                                                                              ^
  ```

- Warning: `workflows/deepmutscan.nf:304:115`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
      variantCounts_filtered_by_library_ch = DMSANALYSIS_PROCESS_GATK.out.processed_variantCounts.map { meta, a, b, c, d -> tuple(meta, b) }
                                                                                                                    ^
  ```

- Warning: `workflows/deepmutscan.nf:304:118`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
      variantCounts_filtered_by_library_ch = DMSANALYSIS_PROCESS_GATK.out.processed_variantCounts.map { meta, a, b, c, d -> tuple(meta, b) }
                                                                                                                       ^
  ```

- Warning: `workflows/deepmutscan.nf:305:107`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
      library_completed_variantCounts_ch = DMSANALYSIS_PROCESS_GATK.out.processed_variantCounts.map { meta, a, b, c, d -> tuple(meta, c) }
                                                                                                            ^
  ```

- Warning: `workflows/deepmutscan.nf:305:110`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
      library_completed_variantCounts_ch = DMSANALYSIS_PROCESS_GATK.out.processed_variantCounts.map { meta, a, b, c, d -> tuple(meta, c) }
                                                                                                               ^
  ```

- Warning: `workflows/deepmutscan.nf:305:116`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
      library_completed_variantCounts_ch = DMSANALYSIS_PROCESS_GATK.out.processed_variantCounts.map { meta, a, b, c, d -> tuple(meta, c) }
                                                                                                                     ^
  ```

- Warning: `workflows/deepmutscan.nf:306:102`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
      variantCounts_for_heatmaps_ch = DMSANALYSIS_PROCESS_GATK.out.processed_variantCounts.map { meta, a, b, c, d -> tuple(meta, d) }
                                                                                                       ^
  ```

- Warning: `workflows/deepmutscan.nf:306:105`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
      variantCounts_for_heatmaps_ch = DMSANALYSIS_PROCESS_GATK.out.processed_variantCounts.map { meta, a, b, c, d -> tuple(meta, d) }
                                                                                                          ^
  ```

- Warning: `workflows/deepmutscan.nf:306:108`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
      variantCounts_for_heatmaps_ch = DMSANALYSIS_PROCESS_GATK.out.processed_variantCounts.map { meta, a, b, c, d -> tuple(meta, d) }
                                                                                                             ^
  ```

- Warning: `workflows/deepmutscan.nf:309:9`: Variable was declared but not used

  ```nextflow
      def fanoutTo = { anchorN, singleton -> singleton.combine(anchorN).map { it[0] } }
          ^^^^^^^^
  ```

- Warning: `workflows/deepmutscan.nf:309:77`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
      def fanoutTo = { anchorN, singleton -> singleton.combine(anchorN).map { it[0] } }
                                                                              ^^
  ```

- Warning: `workflows/deepmutscan.nf:320:120`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
      aa_seq_for_bias_ch             = fanoutTo(variantCounts_filtered_by_library_ch, DMSANALYSIS_AASEQ.out.aa_seq.map { it[1] })
                                                                                                                         ^^
  ```

- Warning: `workflows/deepmutscan.nf:330:145`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
      possible_mutations_N           = fanoutTo(variantCounts_filtered_by_library_ch, DMSANALYSIS_POSSIBLE_MUTATIONS.out.possible_mutations.map { it[1] })
                                                                                                                                                  ^^
  ```

- Warning: `workflows/deepmutscan.nf:376:92`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
      ch_fasta_for_fitness    = ch_fasta.combine(variantCounts_filtered_by_library_ch).map { it[1] }   // path(fasta) -- N
                                                                                             ^^
  ```

- Warning: `workflows/deepmutscan.nf:377:100`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
      ch_rf_for_fitness       = reading_frame_ch.combine(variantCounts_filtered_by_library_ch).map { it[0] }  // val(range) -- N
                                                                                                     ^^
  ```

- Warning: `workflows/deepmutscan.nf:378:109`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
      ch_script_for_fitness   = gatk_to_fitness_script_ch.combine(variantCounts_filtered_by_library_ch).map { it[0] } // path(script) -- N
                                                                                                              ^^
  ```

- Warning: `workflows/deepmutscan.nf:402:41`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
            def metas   = pairs.collect { it[0] }
                                          ^^
  ```

- Warning: `workflows/deepmutscan.nf:403:41`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
            def inputs  = pairs.findAll { it[0].type == 'input'  }.sort { it[0].replicate }.collect { it[1] }
                                          ^^
  ```

- Warning: `workflows/deepmutscan.nf:403:73`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
            def inputs  = pairs.findAll { it[0].type == 'input'  }.sort { it[0].replicate }.collect { it[1] }
                                                                          ^^
  ```

- Warning: `workflows/deepmutscan.nf:403:101`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
            def inputs  = pairs.findAll { it[0].type == 'input'  }.sort { it[0].replicate }.collect { it[1] }
                                                                                                      ^^
  ```

- Warning: `workflows/deepmutscan.nf:404:41`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
            def outputs = pairs.findAll { it[0].type == 'output' }.sort { it[0].replicate }.collect { it[1] }
                                          ^^
  ```

- Warning: `workflows/deepmutscan.nf:404:73`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
            def outputs = pairs.findAll { it[0].type == 'output' }.sort { it[0].replicate }.collect { it[1] }
                                                                          ^^
  ```

- Warning: `workflows/deepmutscan.nf:404:101`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
            def outputs = pairs.findAll { it[0].type == 'output' }.sort { it[0].replicate }.collect { it[1] }
                                                                                                      ^^
  ```

- Warning: `workflows/deepmutscan.nf:407:17`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
        .filter { smeta, metas, ins, outs -> ins && outs }
                  ^^^^^
  ```

- Warning: `workflows/deepmutscan.nf:407:24`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
        .filter { smeta, metas, ins, outs -> ins && outs }
                         ^^^^^
  ```

- Warning: `workflows/deepmutscan.nf:413:14`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
        .map { it[0] }   // keep the script path, one per bundle
               ^^
  ```

- Warning: `workflows/deepmutscan.nf:434:16`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
  ch_fasta.map { it[1] }.set { ch_fasta_path }   // path(/…/GID1A.fasta)
                 ^^
  ```

- Warning: `workflows/deepmutscan.nf:440:65`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
      ch_fasta_path.combine(MERGE_COUNTS.out.merged_counts).map { it[0] }, // path wt_fasta (broadcast to N)
                                                                  ^^
  ```

- Warning: `workflows/deepmutscan.nf:441:68`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
      reading_frame_ch.combine(MERGE_COUNTS.out.merged_counts).map { it[0] }, // val pos_range (broadcast)
                                                                     ^^
  ```

- Warning: `workflows/deepmutscan.nf:442:62`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
      syn_mut_ch.combine(MERGE_COUNTS.out.merged_counts).map { it[0] }     // path R script (broadcast)
                                                               ^^
  ```

- Warning: `workflows/deepmutscan.nf:471:14`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
        .map { key, smp, counts, wt -> tuple(smp, counts, wt) }
               ^^^
  ```

- Warning: `workflows/deepmutscan.nf:476:14`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
        .map { it[0] }
               ^^
  ```

- Warning: `workflows/deepmutscan.nf:479:59`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
    def ch_run_counts_d = ch_counts_wt_d.map { smp, counts, wt -> tuple(smp, counts) }  // matches: tuple val(sample), path(counts_merged)
                                                            ^^
  ```

- Warning: `workflows/deepmutscan.nf:480:46`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
    def ch_run_wt_d     = ch_counts_wt_d.map { smp, counts, wt -> wt }                  // matches: path(wt_txt)
                                               ^^^
  ```

- Warning: `workflows/deepmutscan.nf:480:51`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
    def ch_run_wt_d     = ch_counts_wt_d.map { smp, counts, wt -> wt }                  // matches: path(wt_txt)
                                                    ^^^^^^
  ```
