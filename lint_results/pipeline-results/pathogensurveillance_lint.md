# Nextflow lint results

- Generated: 2026-09-04T00:21:14.483529005Z
- Nextflow version: 26.08.0-edge
- Summary: 436 warnings

## :warning: Warnings

- Warning: `modules/local/assign_context_references/main.nf:24:9`: Variable was declared but not used

  ```nextflow
      def args = task.ext.args ?: ''
          ^^^^
  ```

- Warning: `modules/local/assign_mapping_reference/main.nf:22:9`: Variable was declared but not used

  ```nextflow
      def args = task.ext.args ?: ''
          ^^^^
  ```

- Warning: `modules/local/calculate_pocp/main.nf:21:9`: Variable was declared but not used

  ```nextflow
      def args = task.ext.args ?: ''
          ^^^^
  ```

- Warning: `modules/local/graphtyper/genotype/main.nf:26:9`: Variable was declared but not used

  ```nextflow
      def prefix = task.ext.prefix ?: "${meta.id}"
          ^^^^^^
  ```

- Warning: `modules/local/graphtyper/genotype/main.nf:28:40`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
      def bai_path_text = bam.collect{"${it}.csi"}.join('\\n')
                                         ^^
  ```

- Warning: `modules/local/initial_classification/main.nf:23:9`: Variable was declared but not used

  ```nextflow
      def args = task.ext.args ?: ''
          ^^^^
  ```

- Warning: `modules/local/pick_assemblies/main.nf:27:9`: Variable was declared but not used

  ```nextflow
      def args = task.ext.args ?: ''
          ^^^^
  ```

- Warning: `modules/local/prepare_report_input/main.nf:21:9`: Variable was declared but not used

  ```nextflow
      def args = task.ext.args ?: ''
          ^^^^
  ```

- Warning: `modules/local/vcf_to_snp_align/main.nf:24:9`: Variable was declared but not used

  ```nextflow
      def args = task.ext.args ?: ''
          ^^^^
  ```

- Warning: `modules/nf-core/busco/download/main.nf:22:9`: Variable was declared but not used

  ```nextflow
      def prefix = task.ext.prefix ?: "${lineage}"
          ^^^^^^
  ```

- Warning: `modules/nf-core/busco/download/main.nf:35:9`: Variable was declared but not used

  ```nextflow
      def args = task.ext.args ?: ''
          ^^^^
  ```

- Warning: `modules/nf-core/graphtyper/genotype/main.nf:26:9`: Variable was declared but not used

  ```nextflow
      def prefix = task.ext.prefix ?: "${meta.id}"
          ^^^^^^
  ```

- Warning: `modules/nf-core/graphtyper/genotype/main.nf:27:34`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
      def bam_path_text = bam.sort{it.name}.join('\\n')
                                   ^^
  ```

- Warning: `modules/nf-core/graphtyper/genotype/main.nf:28:38`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
      def index_path_text = index.sort{it.name}.join('\\n')
                                       ^^
  ```

- Warning: `modules/nf-core/graphtyper/vcfconcatenate/main.nf:27:44`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
      input_vcfs = vcf.collate(1000).collect{it.join(' ')} // Batching needed because if there are too many VCFs the shell cannot run the command
                                             ^^
  ```

- Warning: `modules/nf-core/iqtree/main.nf:68:9`: Variable was declared but not used

  ```nextflow
      def trees_rf_arg                = trees_rf                ? "-rf $trees_rf"                 : ''
          ^^^^^^^^^^^^
  ```

- Warning: `modules/nf-core/quast/main.nf:48:9`: Variable was declared but not used

  ```nextflow
      def args      = task.ext.args   ?: ''
          ^^^^
  ```

- Warning: `modules/nf-core/quast/main.nf:50:9`: Variable was declared but not used

  ```nextflow
      def features  = gff             ? "--features $gff" : ''
          ^^^^^^^^
  ```

- Warning: `modules/nf-core/quast/main.nf:51:9`: Variable was declared but not used

  ```nextflow
      def reference = fasta           ? "-r $fasta" : ''
          ^^^^^^^^^
  ```

- Warning: `modules/nf-core/sourmash/compare/main.nf:32:48`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
      def sigs = signatures ? "${signatures.sort{it.toString()}.join(' ')}" : ''
                                                 ^^
  ```

- Warning: `subworkflows/local/align_reads/main.nf:22:31`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          .map { combined_meta, meta, fastqs, ref_meta, reference, ref_index, bam_index ->
                                ^^^^
  ```

- Warning: `subworkflows/local/align_reads/main.nf:22:45`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          .map { combined_meta, meta, fastqs, ref_meta, reference, ref_index, bam_index ->
                                              ^^^^^^^^
  ```

- Warning: `subworkflows/local/align_reads/main.nf:22:55`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          .map { combined_meta, meta, fastqs, ref_meta, reference, ref_index, bam_index ->
                                                        ^^^^^^^^^
  ```

- Warning: `subworkflows/local/align_reads/main.nf:22:66`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          .map { combined_meta, meta, fastqs, ref_meta, reference, ref_index, bam_index ->
                                                                   ^^^^^^^^^
  ```

- Warning: `subworkflows/local/align_reads/main.nf:22:77`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          .map { combined_meta, meta, fastqs, ref_meta, reference, ref_index, bam_index ->
                                                                              ^^^^^^^^^
  ```

- Warning: `subworkflows/local/align_reads/main.nf:27:56`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
      ch_bwa_index = samp_ref_combo.map { combined_meta, meta, fastqs, ref_meta, reference, ref_index, bam_index ->
                                                         ^^^^
  ```

- Warning: `subworkflows/local/align_reads/main.nf:27:62`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
      ch_bwa_index = samp_ref_combo.map { combined_meta, meta, fastqs, ref_meta, reference, ref_index, bam_index ->
                                                               ^^^^^^
  ```

- Warning: `subworkflows/local/align_reads/main.nf:27:70`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
      ch_bwa_index = samp_ref_combo.map { combined_meta, meta, fastqs, ref_meta, reference, ref_index, bam_index ->
                                                                       ^^^^^^^^
  ```

- Warning: `subworkflows/local/align_reads/main.nf:27:80`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
      ch_bwa_index = samp_ref_combo.map { combined_meta, meta, fastqs, ref_meta, reference, ref_index, bam_index ->
                                                                                 ^^^^^^^^^
  ```

- Warning: `subworkflows/local/align_reads/main.nf:27:91`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
      ch_bwa_index = samp_ref_combo.map { combined_meta, meta, fastqs, ref_meta, reference, ref_index, bam_index ->
                                                                                            ^^^^^^^^^
  ```

- Warning: `subworkflows/local/align_reads/main.nf:34:56`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
      ch_reference = samp_ref_combo.map { combined_meta, meta, fastqs, ref_meta, reference, ref_index, bam_index ->
                                                         ^^^^
  ```

- Warning: `subworkflows/local/align_reads/main.nf:34:62`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
      ch_reference = samp_ref_combo.map { combined_meta, meta, fastqs, ref_meta, reference, ref_index, bam_index ->
                                                               ^^^^^^
  ```

- Warning: `subworkflows/local/align_reads/main.nf:34:70`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
      ch_reference = samp_ref_combo.map { combined_meta, meta, fastqs, ref_meta, reference, ref_index, bam_index ->
                                                                       ^^^^^^^^
  ```

- Warning: `subworkflows/local/align_reads/main.nf:34:91`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
      ch_reference = samp_ref_combo.map { combined_meta, meta, fastqs, ref_meta, reference, ref_index, bam_index ->
                                                                                            ^^^^^^^^^
  ```

- Warning: `subworkflows/local/align_reads/main.nf:34:102`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
      ch_reference = samp_ref_combo.map { combined_meta, meta, fastqs, ref_meta, reference, ref_index, bam_index ->
                                                                                                       ^^^^^^^^^
  ```

- Warning: `subworkflows/local/align_reads/main.nf:37:56`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
      ch_ref_index = samp_ref_combo.map { combined_meta, meta, fastqs, ref_meta, reference, ref_index, bam_index ->
                                                         ^^^^
  ```

- Warning: `subworkflows/local/align_reads/main.nf:37:62`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
      ch_ref_index = samp_ref_combo.map { combined_meta, meta, fastqs, ref_meta, reference, ref_index, bam_index ->
                                                               ^^^^^^
  ```

- Warning: `subworkflows/local/align_reads/main.nf:37:70`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
      ch_ref_index = samp_ref_combo.map { combined_meta, meta, fastqs, ref_meta, reference, ref_index, bam_index ->
                                                                       ^^^^^^^^
  ```

- Warning: `subworkflows/local/align_reads/main.nf:37:80`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
      ch_ref_index = samp_ref_combo.map { combined_meta, meta, fastqs, ref_meta, reference, ref_index, bam_index ->
                                                                                 ^^^^^^^^^
  ```

- Warning: `subworkflows/local/align_reads/main.nf:37:102`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
      ch_ref_index = samp_ref_combo.map { combined_meta, meta, fastqs, ref_meta, reference, ref_index, bam_index ->
                                                                                                       ^^^^^^^^^
  ```

- Warning: `subworkflows/local/busco_phylogeny/main.nf:22:17`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          .filter{it.domain == "Eukaryota"}
                  ^^
  ```

- Warning: `subworkflows/local/busco_phylogeny/main.nf:26:16`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          .map{ [it.sample_id, it.report_group_ids, it.ref_metas] }
                 ^^
  ```

- Warning: `subworkflows/local/busco_phylogeny/main.nf:26:30`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          .map{ [it.sample_id, it.report_group_ids, it.ref_metas] }
                               ^^
  ```

- Warning: `subworkflows/local/busco_phylogeny/main.nf:26:51`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          .map{ [it.sample_id, it.report_group_ids, it.ref_metas] }
                                                    ^^
  ```

- Warning: `subworkflows/local/busco_phylogeny/main.nf:32:82`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          .collectFile() { sample_id, report_group_id, ref_id, ref_name, ref_desc, ref_path, usage ->
                                                                                   ^^^^^^^^
  ```

- Warning: `subworkflows/local/busco_phylogeny/main.nf:35:21`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          .map {[[id: it.getSimpleName()], it]}
                      ^^
  ```

- Warning: `subworkflows/local/busco_phylogeny/main.nf:35:42`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          .map {[[id: it.getSimpleName()], it]}
                                           ^^
  ```

- Warning: `subworkflows/local/busco_phylogeny/main.nf:48:21`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          .map{ [[id: it.report_group_ids], it.ref_metas] }
                      ^^
  ```

- Warning: `subworkflows/local/busco_phylogeny/main.nf:48:43`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          .map{ [[id: it.report_group_ids], it.ref_metas] }
                                            ^^
  ```

- Warning: `subworkflows/local/busco_phylogeny/main.nf:57:17`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          .map { [it[0], it[1].replace('\n', '')] } // remove newline that splitText adds
                  ^^
  ```

- Warning: `subworkflows/local/busco_phylogeny/main.nf:57:24`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          .map { [it[0], it[1].replace('\n', '')] } // remove newline that splitText adds
                         ^^
  ```

- Warning: `subworkflows/local/busco_phylogeny/main.nf:63:48`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          .map {report_meta, ref_meta, ref_path, ref_name ->
                                                 ^^^^^^^^
  ```

- Warning: `subworkflows/local/busco_phylogeny/main.nf:69:21`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          .map{ [[id: it.sample_id], [id: it.report_group_ids]] }
                      ^^
  ```

- Warning: `subworkflows/local/busco_phylogeny/main.nf:69:41`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          .map{ [[id: it.sample_id], [id: it.report_group_ids]] }
                                          ^^
  ```

- Warning: `subworkflows/local/busco_phylogeny/main.nf:80:25`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
              .map{ meta, report_meta, path ->
                          ^^^^^^^^^^^
  ```

- Warning: `subworkflows/local/busco_phylogeny/main.nf:95:15`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          .map{ meta, report_meta, path, busco_dir ->
                ^^^^
  ```

- Warning: `subworkflows/local/busco_phylogeny/main.nf:95:34`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          .map{ meta, report_meta, path, busco_dir ->
                                   ^^^^
  ```

- Warning: `subworkflows/local/busco_phylogeny/main.nf:110:17`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
                  it.sample_id == '' ? null : [id: it.sample_id],
                  ^^
  ```

- Warning: `subworkflows/local/busco_phylogeny/main.nf:110:50`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
                  it.sample_id == '' ? null : [id: it.sample_id],
                                                   ^^
  ```

- Warning: `subworkflows/local/busco_phylogeny/main.nf:111:17`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
                  it.report_group_id == '' ? null : [id: it.report_group_id],
                  ^^
  ```

- Warning: `subworkflows/local/busco_phylogeny/main.nf:111:56`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
                  it.report_group_id == '' ? null : [id: it.report_group_id],
                                                         ^^
  ```

- Warning: `subworkflows/local/busco_phylogeny/main.nf:112:17`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
                  it.reference_id == '' ? null : [id: it.reference_id],
                  ^^
  ```

- Warning: `subworkflows/local/busco_phylogeny/main.nf:112:53`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
                  it.reference_id == '' ? null : [id: it.reference_id],
                                                      ^^
  ```

- Warning: `subworkflows/local/busco_phylogeny/main.nf:114:17`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
                  it.message_type,
                  ^^
  ```

- Warning: `subworkflows/local/busco_phylogeny/main.nf:115:17`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
                  it.description
                  ^^
  ```

- Warning: `subworkflows/local/busco_phylogeny/main.nf:140:17`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          .map { [it[0].group_id, it[1]] } // group_meta, tree
                  ^^
  ```

- Warning: `subworkflows/local/busco_phylogeny/main.nf:140:33`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          .map { [it[0].group_id, it[1]] } // group_meta, tree
                                  ^^
  ```

- Warning: `subworkflows/local/call_variants/main.nf:29:30`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          .map{ combined_meta, sample_meta, bam, bai, ref, fai, dict ->
                               ^^^^^^^^^^^
  ```

- Warning: `subworkflows/local/call_variants/main.nf:29:43`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          .map{ combined_meta, sample_meta, bam, bai, ref, fai, dict ->
                                            ^^^
  ```

- Warning: `subworkflows/local/call_variants/main.nf:29:48`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          .map{ combined_meta, sample_meta, bam, bai, ref, fai, dict ->
                                                 ^^^
  ```

- Warning: `subworkflows/local/call_variants/main.nf:29:53`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          .map{ combined_meta, sample_meta, bam, bai, ref, fai, dict ->
                                                      ^^^
  ```

- Warning: `subworkflows/local/call_variants/main.nf:29:58`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          .map{ combined_meta, sample_meta, bam, bai, ref, fai, dict ->
                                                           ^^^
  ```

- Warning: `subworkflows/local/call_variants/main.nf:29:63`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          .map{ combined_meta, sample_meta, bam, bai, ref, fai, dict ->
                                                                ^^^^
  ```

- Warning: `subworkflows/local/call_variants/main.nf:34:31`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          .map { combined_meta, sample_meta, bam, bai, ref, fai, dict ->
                                ^^^^^^^^^^^
  ```

- Warning: `subworkflows/local/call_variants/main.nf:34:44`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          .map { combined_meta, sample_meta, bam, bai, ref, fai, dict ->
                                             ^^^
  ```

- Warning: `subworkflows/local/call_variants/main.nf:34:49`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          .map { combined_meta, sample_meta, bam, bai, ref, fai, dict ->
                                                  ^^^
  ```

- Warning: `subworkflows/local/call_variants/main.nf:34:59`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          .map { combined_meta, sample_meta, bam, bai, ref, fai, dict ->
                                                            ^^^
  ```

- Warning: `subworkflows/local/call_variants/main.nf:34:64`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          .map { combined_meta, sample_meta, bam, bai, ref, fai, dict ->
                                                                 ^^^^
  ```

- Warning: `subworkflows/local/call_variants/main.nf:41:17`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          .map { [it.getSimpleName(), it] }
                  ^^
  ```

- Warning: `subworkflows/local/call_variants/main.nf:41:37`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          .map { [it.getSimpleName(), it] }
                                      ^^
  ```

- Warning: `subworkflows/local/call_variants/main.nf:43:16`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          .map { combined_meta_id, region_path, combined_meta ->
                 ^^^^^^^^^^^^^^^^
  ```

- Warning: `subworkflows/local/call_variants/main.nf:50:45`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          ch_ref_grouped.map { combined_meta, sample_meta, bam, bai, ref, fai, dict, region_file ->
                                              ^^^^^^^^^^^
  ```

- Warning: `subworkflows/local/call_variants/main.nf:50:68`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          ch_ref_grouped.map { combined_meta, sample_meta, bam, bai, ref, fai, dict, region_file ->
                                                                     ^^^
  ```

- Warning: `subworkflows/local/call_variants/main.nf:50:73`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          ch_ref_grouped.map { combined_meta, sample_meta, bam, bai, ref, fai, dict, region_file ->
                                                                          ^^^
  ```

- Warning: `subworkflows/local/call_variants/main.nf:50:78`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          ch_ref_grouped.map { combined_meta, sample_meta, bam, bai, ref, fai, dict, region_file ->
                                                                               ^^^^
  ```

- Warning: `subworkflows/local/call_variants/main.nf:50:84`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          ch_ref_grouped.map { combined_meta, sample_meta, bam, bai, ref, fai, dict, region_file ->
                                                                                     ^^^^^^^^^^^
  ```

- Warning: `subworkflows/local/call_variants/main.nf:53:45`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          ch_ref_grouped.map { combined_meta, sample_meta, bam, bai, ref, fai, dict, region_file ->
                                              ^^^^^^^^^^^
  ```

- Warning: `subworkflows/local/call_variants/main.nf:53:58`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          ch_ref_grouped.map { combined_meta, sample_meta, bam, bai, ref, fai, dict, region_file ->
                                                           ^^^
  ```

- Warning: `subworkflows/local/call_variants/main.nf:53:63`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          ch_ref_grouped.map { combined_meta, sample_meta, bam, bai, ref, fai, dict, region_file ->
                                                                ^^^
  ```

- Warning: `subworkflows/local/call_variants/main.nf:53:73`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          ch_ref_grouped.map { combined_meta, sample_meta, bam, bai, ref, fai, dict, region_file ->
                                                                          ^^^
  ```

- Warning: `subworkflows/local/call_variants/main.nf:53:78`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          ch_ref_grouped.map { combined_meta, sample_meta, bam, bai, ref, fai, dict, region_file ->
                                                                               ^^^^
  ```

- Warning: `subworkflows/local/call_variants/main.nf:53:84`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          ch_ref_grouped.map { combined_meta, sample_meta, bam, bai, ref, fai, dict, region_file ->
                                                                                     ^^^^^^^^^^^
  ```

- Warning: `subworkflows/local/call_variants/main.nf:56:45`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          ch_ref_grouped.map { combined_meta, sample_meta, bam, bai, ref, fai, dict, region_file ->
                                              ^^^^^^^^^^^
  ```

- Warning: `subworkflows/local/call_variants/main.nf:56:58`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          ch_ref_grouped.map { combined_meta, sample_meta, bam, bai, ref, fai, dict, region_file ->
                                                           ^^^
  ```

- Warning: `subworkflows/local/call_variants/main.nf:56:63`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          ch_ref_grouped.map { combined_meta, sample_meta, bam, bai, ref, fai, dict, region_file ->
                                                                ^^^
  ```

- Warning: `subworkflows/local/call_variants/main.nf:56:68`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          ch_ref_grouped.map { combined_meta, sample_meta, bam, bai, ref, fai, dict, region_file ->
                                                                     ^^^
  ```

- Warning: `subworkflows/local/call_variants/main.nf:56:78`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          ch_ref_grouped.map { combined_meta, sample_meta, bam, bai, ref, fai, dict, region_file ->
                                                                               ^^^^
  ```

- Warning: `subworkflows/local/call_variants/main.nf:56:84`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          ch_ref_grouped.map { combined_meta, sample_meta, bam, bai, ref, fai, dict, region_file ->
                                                                                     ^^^^^^^^^^^
  ```

- Warning: `subworkflows/local/call_variants/main.nf:59:30`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          ch_ref_grouped.map { combined_meta, sample_meta, bam, bai, ref, fai, dict, region_file ->
                               ^^^^^^^^^^^^^
  ```

- Warning: `subworkflows/local/call_variants/main.nf:59:45`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          ch_ref_grouped.map { combined_meta, sample_meta, bam, bai, ref, fai, dict, region_file ->
                                              ^^^^^^^^^^^
  ```

- Warning: `subworkflows/local/call_variants/main.nf:59:58`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          ch_ref_grouped.map { combined_meta, sample_meta, bam, bai, ref, fai, dict, region_file ->
                                                           ^^^
  ```

- Warning: `subworkflows/local/call_variants/main.nf:59:63`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          ch_ref_grouped.map { combined_meta, sample_meta, bam, bai, ref, fai, dict, region_file ->
                                                                ^^^
  ```

- Warning: `subworkflows/local/call_variants/main.nf:59:68`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          ch_ref_grouped.map { combined_meta, sample_meta, bam, bai, ref, fai, dict, region_file ->
                                                                     ^^^
  ```

- Warning: `subworkflows/local/call_variants/main.nf:59:73`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          ch_ref_grouped.map { combined_meta, sample_meta, bam, bai, ref, fai, dict, region_file ->
                                                                          ^^^
  ```

- Warning: `subworkflows/local/call_variants/main.nf:59:78`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          ch_ref_grouped.map { combined_meta, sample_meta, bam, bai, ref, fai, dict, region_file ->
                                                                               ^^^^
  ```

- Warning: `subworkflows/local/call_variants/main.nf:74:45`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          ch_ref_grouped.map { combined_meta, sample_meta, bam, bai, ref, fai, dict, region_file ->
                                              ^^^^^^^^^^^
  ```

- Warning: `subworkflows/local/call_variants/main.nf:74:58`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          ch_ref_grouped.map { combined_meta, sample_meta, bam, bai, ref, fai, dict, region_file ->
                                                           ^^^
  ```

- Warning: `subworkflows/local/call_variants/main.nf:74:63`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          ch_ref_grouped.map { combined_meta, sample_meta, bam, bai, ref, fai, dict, region_file ->
                                                                ^^^
  ```

- Warning: `subworkflows/local/call_variants/main.nf:74:73`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          ch_ref_grouped.map { combined_meta, sample_meta, bam, bai, ref, fai, dict, region_file ->
                                                                          ^^^
  ```

- Warning: `subworkflows/local/call_variants/main.nf:74:78`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          ch_ref_grouped.map { combined_meta, sample_meta, bam, bai, ref, fai, dict, region_file ->
                                                                               ^^^^
  ```

- Warning: `subworkflows/local/call_variants/main.nf:74:84`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          ch_ref_grouped.map { combined_meta, sample_meta, bam, bai, ref, fai, dict, region_file ->
                                                                                     ^^^^^^^^^^^
  ```

- Warning: `subworkflows/local/call_variants/main.nf:84:49`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
              ch_ref_grouped.map { combined_meta, sample_meta, bam, bai, ref, fai, dict, region_file ->
                                                  ^^^^^^^^^^^
  ```

- Warning: `subworkflows/local/call_variants/main.nf:84:62`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
              ch_ref_grouped.map { combined_meta, sample_meta, bam, bai, ref, fai, dict, region_file ->
                                                               ^^^
  ```

- Warning: `subworkflows/local/call_variants/main.nf:84:67`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
              ch_ref_grouped.map { combined_meta, sample_meta, bam, bai, ref, fai, dict, region_file ->
                                                                    ^^^
  ```

- Warning: `subworkflows/local/call_variants/main.nf:84:88`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
              ch_ref_grouped.map { combined_meta, sample_meta, bam, bai, ref, fai, dict, region_file ->
                                                                                         ^^^^^^^^^^^
  ```

- Warning: `subworkflows/local/call_variants/main.nf:90:49`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          vf_input.map { combined_meta, vcf, tbi, ref, fai, dict, gzi ->
                                                  ^^^
  ```

- Warning: `subworkflows/local/call_variants/main.nf:90:54`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          vf_input.map { combined_meta, vcf, tbi, ref, fai, dict, gzi ->
                                                       ^^^
  ```

- Warning: `subworkflows/local/call_variants/main.nf:90:59`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          vf_input.map { combined_meta, vcf, tbi, ref, fai, dict, gzi ->
                                                            ^^^^
  ```

- Warning: `subworkflows/local/call_variants/main.nf:90:65`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          vf_input.map { combined_meta, vcf, tbi, ref, fai, dict, gzi ->
                                                                  ^^^
  ```

- Warning: `subworkflows/local/call_variants/main.nf:93:39`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          vf_input.map { combined_meta, vcf, tbi, ref, fai, dict, gzi ->
                                        ^^^
  ```

- Warning: `subworkflows/local/call_variants/main.nf:93:44`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          vf_input.map { combined_meta, vcf, tbi, ref, fai, dict, gzi ->
                                             ^^^
  ```

- Warning: `subworkflows/local/call_variants/main.nf:93:54`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          vf_input.map { combined_meta, vcf, tbi, ref, fai, dict, gzi ->
                                                       ^^^
  ```

- Warning: `subworkflows/local/call_variants/main.nf:93:59`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          vf_input.map { combined_meta, vcf, tbi, ref, fai, dict, gzi ->
                                                            ^^^^
  ```

- Warning: `subworkflows/local/call_variants/main.nf:93:65`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          vf_input.map { combined_meta, vcf, tbi, ref, fai, dict, gzi ->
                                                                  ^^^
  ```

- Warning: `subworkflows/local/call_variants/main.nf:96:39`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          vf_input.map { combined_meta, vcf, tbi, ref, fai, dict, gzi ->
                                        ^^^
  ```

- Warning: `subworkflows/local/call_variants/main.nf:96:44`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          vf_input.map { combined_meta, vcf, tbi, ref, fai, dict, gzi ->
                                             ^^^
  ```

- Warning: `subworkflows/local/call_variants/main.nf:96:49`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          vf_input.map { combined_meta, vcf, tbi, ref, fai, dict, gzi ->
                                                  ^^^
  ```

- Warning: `subworkflows/local/call_variants/main.nf:96:59`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          vf_input.map { combined_meta, vcf, tbi, ref, fai, dict, gzi ->
                                                            ^^^^
  ```

- Warning: `subworkflows/local/call_variants/main.nf:96:65`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          vf_input.map { combined_meta, vcf, tbi, ref, fai, dict, gzi ->
                                                                  ^^^
  ```

- Warning: `subworkflows/local/call_variants/main.nf:99:39`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          vf_input.map { combined_meta, vcf, tbi, ref, fai, dict, gzi ->
                                        ^^^
  ```

- Warning: `subworkflows/local/call_variants/main.nf:99:44`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          vf_input.map { combined_meta, vcf, tbi, ref, fai, dict, gzi ->
                                             ^^^
  ```

- Warning: `subworkflows/local/call_variants/main.nf:99:49`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          vf_input.map { combined_meta, vcf, tbi, ref, fai, dict, gzi ->
                                                  ^^^
  ```

- Warning: `subworkflows/local/call_variants/main.nf:99:54`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          vf_input.map { combined_meta, vcf, tbi, ref, fai, dict, gzi ->
                                                       ^^^
  ```

- Warning: `subworkflows/local/call_variants/main.nf:99:65`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          vf_input.map { combined_meta, vcf, tbi, ref, fai, dict, gzi ->
                                                                  ^^^
  ```

- Warning: `subworkflows/local/call_variants/main.nf:102:39`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          vf_input.map { combined_meta, vcf, tbi, ref, fai, dict, gzi ->
                                        ^^^
  ```

- Warning: `subworkflows/local/call_variants/main.nf:102:44`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          vf_input.map { combined_meta, vcf, tbi, ref, fai, dict, gzi ->
                                             ^^^
  ```

- Warning: `subworkflows/local/call_variants/main.nf:102:49`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          vf_input.map { combined_meta, vcf, tbi, ref, fai, dict, gzi ->
                                                  ^^^
  ```

- Warning: `subworkflows/local/call_variants/main.nf:102:54`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          vf_input.map { combined_meta, vcf, tbi, ref, fai, dict, gzi ->
                                                       ^^^
  ```

- Warning: `subworkflows/local/call_variants/main.nf:102:59`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          vf_input.map { combined_meta, vcf, tbi, ref, fai, dict, gzi ->
                                                            ^^^^
  ```

- Warning: `subworkflows/local/call_variants/main.nf:115:44`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          .map { combined_meta, sample_meta, bam, bai, ref, fai, dict, region_file ->
                                             ^^^
  ```

- Warning: `subworkflows/local/call_variants/main.nf:115:49`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          .map { combined_meta, sample_meta, bam, bai, ref, fai, dict, region_file ->
                                                  ^^^
  ```

- Warning: `subworkflows/local/call_variants/main.nf:115:54`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          .map { combined_meta, sample_meta, bam, bai, ref, fai, dict, region_file ->
                                                       ^^^
  ```

- Warning: `subworkflows/local/call_variants/main.nf:115:59`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          .map { combined_meta, sample_meta, bam, bai, ref, fai, dict, region_file ->
                                                            ^^^
  ```

- Warning: `subworkflows/local/call_variants/main.nf:115:64`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          .map { combined_meta, sample_meta, bam, bai, ref, fai, dict, region_file ->
                                                                 ^^^^
  ```

- Warning: `subworkflows/local/call_variants/main.nf:115:70`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          .map { combined_meta, sample_meta, bam, bai, ref, fai, dict, region_file ->
                                                                       ^^^^^^^^^^^
  ```

- Warning: `subworkflows/local/core_genome_phylogeny/main.nf:28:17`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          .filter{it.domain == "Bacteria" || it.domain == "Archaea"}
                  ^^
  ```

- Warning: `subworkflows/local/core_genome_phylogeny/main.nf:28:44`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          .filter{it.domain == "Bacteria" || it.domain == "Archaea"}
                                             ^^
  ```

- Warning: `subworkflows/local/core_genome_phylogeny/main.nf:32:16`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          .map{ [it.sample_id, it.report_group_ids, it.ref_metas] }
                 ^^
  ```

- Warning: `subworkflows/local/core_genome_phylogeny/main.nf:32:30`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          .map{ [it.sample_id, it.report_group_ids, it.ref_metas] }
                               ^^
  ```

- Warning: `subworkflows/local/core_genome_phylogeny/main.nf:32:51`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          .map{ [it.sample_id, it.report_group_ids, it.ref_metas] }
                                                    ^^
  ```

- Warning: `subworkflows/local/core_genome_phylogeny/main.nf:38:82`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          .collectFile() { sample_id, report_group_id, ref_id, ref_name, ref_desc, ref_path, usage ->
                                                                                   ^^^^^^^^
  ```

- Warning: `subworkflows/local/core_genome_phylogeny/main.nf:41:21`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          .map {[[id: it.getSimpleName()], it]}
                      ^^
  ```

- Warning: `subworkflows/local/core_genome_phylogeny/main.nf:41:42`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          .map {[[id: it.getSimpleName()], it]}
                                           ^^
  ```

- Warning: `subworkflows/local/core_genome_phylogeny/main.nf:54:21`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          .map{ [[id: it.report_group_ids], it.ref_metas] }
                      ^^
  ```

- Warning: `subworkflows/local/core_genome_phylogeny/main.nf:54:43`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          .map{ [[id: it.report_group_ids], it.ref_metas] }
                                            ^^
  ```

- Warning: `subworkflows/local/core_genome_phylogeny/main.nf:64:17`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          .map { [it[0], it[1].replace('\n', '')] } // remove newline that splitText adds
                  ^^
  ```

- Warning: `subworkflows/local/core_genome_phylogeny/main.nf:64:24`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          .map { [it[0], it[1].replace('\n', '')] } // remove newline that splitText adds
                         ^^
  ```

- Warning: `subworkflows/local/core_genome_phylogeny/main.nf:73:19`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          .branch { ref_meta, report_meta, ref_path, gff_path ->
                    ^^^^^^^^
  ```

- Warning: `subworkflows/local/core_genome_phylogeny/main.nf:73:29`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          .branch { ref_meta, report_meta, ref_path, gff_path ->
                              ^^^^^^^^^^^
  ```

- Warning: `subworkflows/local/core_genome_phylogeny/main.nf:73:42`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          .branch { ref_meta, report_meta, ref_path, gff_path ->
                                           ^^^^^^^^
  ```

- Warning: `subworkflows/local/core_genome_phylogeny/main.nf:82:86`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
              bakta_db_tar = channel.fromPath(params.bakta_db).map{ [ [id: 'baktadb'], it] }
                                                                                       ^^
  ```

- Warning: `subworkflows/local/core_genome_phylogeny/main.nf:84:45`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
              bakta_db = UNTAR.out.untar.map{ meta, db -> db }.first()
                                              ^^^^
  ```

- Warning: `subworkflows/local/core_genome_phylogeny/main.nf:97:21`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          .map{ [[id: it.sample_id], [id: it.report_group_ids]] }
                      ^^
  ```

- Warning: `subworkflows/local/core_genome_phylogeny/main.nf:97:41`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          .map{ [[id: it.sample_id], [id: it.report_group_ids]] }
                                          ^^
  ```

- Warning: `subworkflows/local/core_genome_phylogeny/main.nf:100:49`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          .map { ref_meta, report_meta, ref_path, gff_path ->
                                                  ^^^^^^^^
  ```

- Warning: `subworkflows/local/core_genome_phylogeny/main.nf:107:30`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
              .map { ref_meta, report_meta, assem_path ->
                               ^^^^^^^^^^^
  ```

- Warning: `subworkflows/local/core_genome_phylogeny/main.nf:122:29`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
              .map{ ref_meta, report_meta, ref_path, ref_gff ->
                              ^^^^^^^^^^^
  ```

- Warning: `subworkflows/local/core_genome_phylogeny/main.nf:131:49`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          .map { sample_or_ref_meta, report_meta, assem_path, gff_path ->
                                                  ^^^^^^^^^^
  ```

- Warning: `subworkflows/local/core_genome_phylogeny/main.nf:136:38`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          .map{ ref_meta, report_meta, ref_path, ref_gff, ref_combined ->
                                       ^^^^^^^^
  ```

- Warning: `subworkflows/local/core_genome_phylogeny/main.nf:136:48`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          .map{ ref_meta, report_meta, ref_path, ref_gff, ref_combined ->
                                                 ^^^^^^^
  ```

- Warning: `subworkflows/local/core_genome_phylogeny/main.nf:141:16`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          .map { sample_or_ref_meta, report_meta, gff ->
                 ^^^^^^^^^^^^^^^^^^
  ```

- Warning: `subworkflows/local/core_genome_phylogeny/main.nf:153:19`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          .filter { it[1].any{ it.endsWith("PIRATE.gene_families.ordered.tsv") } }
                    ^^
  ```

- Warning: `subworkflows/local/core_genome_phylogeny/main.nf:153:30`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          .filter { it[1].any{ it.endsWith("PIRATE.gene_families.ordered.tsv") } }
                               ^^
  ```

- Warning: `subworkflows/local/core_genome_phylogeny/main.nf:155:21`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          .filter { ! it[1].any{ it.endsWith("PIRATE.gene_families.ordered.tsv") } }
                      ^^
  ```

- Warning: `subworkflows/local/core_genome_phylogeny/main.nf:155:32`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          .filter { ! it[1].any{ it.endsWith("PIRATE.gene_families.ordered.tsv") } }
                                 ^^
  ```

- Warning: `subworkflows/local/core_genome_phylogeny/main.nf:156:23`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          .map { [null, it[0], null, "CORE_GENOME_PHYLOGENY", "WARNING", "Pirate failed to find a core genome, possibly becuase samples are very different or there are too few reads."] } // meta, group_meta, ref_meta, workflow, level, message
                        ^^
  ```

- Warning: `subworkflows/local/core_genome_phylogeny/main.nf:185:20`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
              .map { file_name, message_data -> [
                     ^^^^^^^^^
  ```

- Warning: `subworkflows/local/core_genome_phylogeny/main.nf:216:17`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          .map { [it[0].group_id, it[1]] } // group_meta, tree
                  ^^
  ```

- Warning: `subworkflows/local/core_genome_phylogeny/main.nf:216:33`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          .map { [it[0].group_id, it[1]] } // group_meta, tree
                                  ^^
  ```

- Warning: `subworkflows/local/core_genome_phylogeny/main.nf:221:17`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          .map { [it[1], null] }
                  ^^
  ```

- Warning: `subworkflows/local/core_genome_phylogeny/main.nf:224:17`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          .map { [it[1], null] }
                  ^^
  ```

- Warning: `subworkflows/local/genome_assembly/main.nf:17:21`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          .map{ [[id: it.sample_id, single_end: it.single_end, domain: it.domain, type: it.sequence_type], [id: it.report_group_ids], it.paths] }
                      ^^
  ```

- Warning: `subworkflows/local/genome_assembly/main.nf:17:47`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          .map{ [[id: it.sample_id, single_end: it.single_end, domain: it.domain, type: it.sequence_type], [id: it.report_group_ids], it.paths] }
                                                ^^
  ```

- Warning: `subworkflows/local/genome_assembly/main.nf:17:70`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          .map{ [[id: it.sample_id, single_end: it.single_end, domain: it.domain, type: it.sequence_type], [id: it.report_group_ids], it.paths] }
                                                                       ^^
  ```

- Warning: `subworkflows/local/genome_assembly/main.nf:17:87`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          .map{ [[id: it.sample_id, single_end: it.single_end, domain: it.domain, type: it.sequence_type], [id: it.report_group_ids], it.paths] }
                                                                                        ^^
  ```

- Warning: `subworkflows/local/genome_assembly/main.nf:17:111`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          .map{ [[id: it.sample_id, single_end: it.single_end, domain: it.domain, type: it.sequence_type], [id: it.report_group_ids], it.paths] }
                                                                                                                ^^
  ```

- Warning: `subworkflows/local/genome_assembly/main.nf:17:133`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          .map{ [[id: it.sample_id, single_end: it.single_end, domain: it.domain, type: it.sequence_type], [id: it.report_group_ids], it.paths] }
                                                                                                                                      ^^
  ```

- Warning: `subworkflows/local/genome_assembly/main.nf:19:28`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          .map{ sample_meta, report_meta, read_paths -> [sample_meta, read_paths]}
                             ^^^^^^^^^^^
  ```

- Warning: `subworkflows/local/genome_assembly/main.nf:21:25`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          .branch { meta, paths->
                          ^^^^^
  ```

- Warning: `subworkflows/local/genome_assembly/main.nf:36:86`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
              [sample_meta, read_paths.size() <= 2 ? read_paths : read_paths.findAll { it ==~ /.+_[12]\..+$/ }, [] ]
                                                                                       ^^
  ```

- Warning: `subworkflows/local/genome_assembly/main.nf:43:18`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          .filter{ sample_meta, json ->
                   ^^^^^^^^^^^
  ```

- Warning: `subworkflows/local/genome_assembly/main.nf:57:29`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          .map { sample_meta, read_paths1, base_count, report_meta, read_paths2 ->
                              ^^^^^^^^^^^
  ```

- Warning: `subworkflows/local/genome_assembly/main.nf:57:67`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          .map { sample_meta, read_paths1, base_count, report_meta, read_paths2 ->
                                                                    ^^^^^^^^^^^
  ```

- Warning: `subworkflows/local/genome_assembly/main.nf:72:19`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          .filter { sample_meta, read_paths, scaffolds ->
                    ^^^^^^^^^^^
  ```

- Warning: `subworkflows/local/genome_assembly/main.nf:72:32`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          .filter { sample_meta, read_paths, scaffolds ->
                                 ^^^^^^^^^^
  ```

- Warning: `subworkflows/local/genome_assembly/main.nf:76:29`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          .map { sample_meta, read_paths, scaffolds, report_meta, read_paths2 ->
                              ^^^^^^^^^^
  ```

- Warning: `subworkflows/local/genome_assembly/main.nf:76:41`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          .map { sample_meta, read_paths, scaffolds, report_meta, read_paths2 ->
                                          ^^^^^^^^^
  ```

- Warning: `subworkflows/local/genome_assembly/main.nf:76:65`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          .map { sample_meta, read_paths, scaffolds, report_meta, read_paths2 ->
                                                                  ^^^^^^^^^^^
  ```

- Warning: `subworkflows/local/genome_assembly/main.nf:104:22`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          .map { [[id: it.sample_id], it] }
                       ^^
  ```

- Warning: `subworkflows/local/genome_assembly/main.nf:104:37`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          .map { [[id: it.sample_id], it] }
                                      ^^
  ```

- Warning: `subworkflows/local/genome_assembly/main.nf:106:44`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          .map{ sample_meta, my_sample_data, paths ->
                                             ^^^^^
  ```

- Warning: `subworkflows/local/initial_qc_checks/main.nf:15:19`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          .filter { it.sequence_type == "illumina" || it.sequence_type == "bgiseq" }
                    ^^
  ```

- Warning: `subworkflows/local/initial_qc_checks/main.nf:15:53`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          .filter { it.sequence_type == "illumina" || it.sequence_type == "bgiseq" }
                                                      ^^
  ```

- Warning: `subworkflows/local/initial_qc_checks/main.nf:16:22`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          .map { [[id: it.sample_id], it.paths] }
                       ^^
  ```

- Warning: `subworkflows/local/initial_qc_checks/main.nf:16:37`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          .map { [[id: it.sample_id], it.paths] }
                                      ^^
  ```

- Warning: `subworkflows/local/initial_qc_checks/main.nf:22:19`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          .filter { it.sequence_type == "nanopore" || it.sequence_type == "pacbio" }
                    ^^
  ```

- Warning: `subworkflows/local/initial_qc_checks/main.nf:22:53`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          .filter { it.sequence_type == "nanopore" || it.sequence_type == "pacbio" }
                                                      ^^
  ```

- Warning: `subworkflows/local/initial_qc_checks/main.nf:23:22`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          .map { [[id: it.sample_id], it.paths] }
                       ^^
  ```

- Warning: `subworkflows/local/initial_qc_checks/main.nf:23:37`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          .map { [[id: it.sample_id], it.paths] }
                                      ^^
  ```

- Warning: `subworkflows/local/prepare_input/main.nf:31:47`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          .map { create_sample_metadata_channel(it) }
                                                ^^
  ```

- Warning: `subworkflows/local/prepare_input/main.nf:35:50`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          .map { create_reference_metadata_channel(it) }
                                                   ^^
  ```

- Warning: `subworkflows/local/prepare_input/main.nf:41:17`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
                  it.sample_id == '' ? null : [id: it.sample_id],
                  ^^
  ```

- Warning: `subworkflows/local/prepare_input/main.nf:41:50`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
                  it.sample_id == '' ? null : [id: it.sample_id],
                                                   ^^
  ```

- Warning: `subworkflows/local/prepare_input/main.nf:42:17`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
                  it.report_group_id == '' ? null : [id: it.report_group_id],
                  ^^
  ```

- Warning: `subworkflows/local/prepare_input/main.nf:42:56`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
                  it.report_group_id == '' ? null : [id: it.report_group_id],
                                                         ^^
  ```

- Warning: `subworkflows/local/prepare_input/main.nf:43:17`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
                  it.reference_id == '' ? null : [id: it.reference_id],
                  ^^
  ```

- Warning: `subworkflows/local/prepare_input/main.nf:43:53`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
                  it.reference_id == '' ? null : [id: it.reference_id],
                                                      ^^
  ```

- Warning: `subworkflows/local/prepare_input/main.nf:45:17`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
                  it.message_type,
                  ^^
  ```

- Warning: `subworkflows/local/prepare_input/main.nf:46:17`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
                  it.description
                  ^^
  ```

- Warning: `subworkflows/local/prepare_input/main.nf:56:27`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          .filter{ ref_ids, sample_meta -> ref_ids.size() > 0 }
                            ^^^^^^^^^^^
  ```

- Warning: `subworkflows/local/prepare_input/main.nf:59:16`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          .map { ref_id, sample_meta, ref_meta -> [sample_meta, ref_meta] }
                 ^^^^^^
  ```

- Warning: `subworkflows/local/prepare_input/main.nf:65:31`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          .filter{ sample_meta, ref_metas -> sample_meta.ncbi_accession}
                                ^^^^^^^^^
  ```

- Warning: `subworkflows/local/prepare_input/main.nf:67:31`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          .filter{ sample_meta, ref_metas -> ! sample_meta.ncbi_accession }
                                ^^^^^^^^^
  ```

- Warning: `subworkflows/local/prepare_input/main.nf:72:31`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          .map { ncbi_acc_meta, sample_meta, ref_metas ->
                                ^^^^^^^^^^^
  ```

- Warning: `subworkflows/local/prepare_input/main.nf:72:44`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          .map { ncbi_acc_meta, sample_meta, ref_metas ->
                                             ^^^^^^^^^
  ```

- Warning: `subworkflows/local/prepare_input/main.nf:80:16`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          .map { ncbi_acc_meta, reads_path, sample_meta, ref_metas ->
                 ^^^^^^^^^^^^^
  ```

- Warning: `subworkflows/local/prepare_input/main.nf:85:60`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
                      sample_meta.paths = reads_path.findAll{it ==~ /^.+_[12]\..+$/}
                                                             ^^
  ```

- Warning: `subworkflows/local/prepare_input/main.nf:98:33`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
              .map { sample_meta, ref_metas ->
                                  ^^^^^^^^^
  ```

- Warning: `subworkflows/local/prepare_input/main.nf:122:15`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          .map{ sample_id, sample_meta, ref_metas, depth, domain ->
                ^^^^^^^^^
  ```

- Warning: `subworkflows/local/prepare_input/main.nf:131:18`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          .filter{ sample_meta, taxon_data ->
                   ^^^^^^^^^^^
  ```

- Warning: `subworkflows/local/prepare_input/main.nf:139:19`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          .filter { sample_meta, ref_metas -> // Dont lookup assembly metadata if no references are to be dowloaded automatically (besides user-defined references)
                    ^^^^^^^^^^^
  ```

- Warning: `subworkflows/local/prepare_input/main.nf:139:32`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          .filter { sample_meta, ref_metas -> // Dont lookup assembly metadata if no references are to be dowloaded automatically (besides user-defined references)
                                 ^^^^^^^^^
  ```

- Warning: `subworkflows/local/prepare_input/main.nf:142:19`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          .filter { sample_meta, ref_metas -> // Dont lookup assembly metadata for samples that the user has defined exclusive references for
                    ^^^^^^^^^^^
  ```

- Warning: `subworkflows/local/prepare_input/main.nf:143:34`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
              ! (ref_metas.collect{it.ref_primary_usage}.contains('exclusive') &&
                                   ^^
  ```

- Warning: `subworkflows/local/prepare_input/main.nf:144:36`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
                  (ref_metas.collect{it.ref_contextual_usage}.contains('exclusive') || no_auto_contextual_refs))
                                     ^^
  ```

- Warning: `subworkflows/local/prepare_input/main.nf:146:29`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          .map { sample_meta, ref_metas ->
                              ^^^^^^^^^
  ```

- Warning: `subworkflows/local/prepare_input/main.nf:150:15`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          .map{ sample_id, sample_meta, family_ids -> [family_ids] }
                ^^^^^^^^^
  ```

- Warning: `subworkflows/local/prepare_input/main.nf:150:26`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          .map{ sample_id, sample_meta, family_ids -> [family_ids] }
                           ^^^^^^^^^^^
  ```

- Warning: `subworkflows/local/prepare_input/main.nf:168:16`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          .map { sample_meta, family_ids ->
                 ^^^^^^^^^^^
  ```

- Warning: `subworkflows/local/prepare_input/main.nf:173:19`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          .filter { it != [null, null] }
                    ^^
  ```

- Warning: `subworkflows/local/prepare_input/main.nf:179:16`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          .map { family_id, sample_id, stats_path -> [sample_id, stats_path] }
                 ^^^^^^^^^
  ```

- Warning: `subworkflows/local/prepare_input/main.nf:183:46`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
              [sample_id, family_stats.findAll{it != null}]
                                               ^^
  ```

- Warning: `subworkflows/local/prepare_input/main.nf:186:29`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          .map { sample_meta, ref_metas -> [[id: sample_meta.sample_id]] }
                              ^^^^^^^^^
  ```

- Warning: `subworkflows/local/prepare_input/main.nf:190:19`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          .filter { sample_meta, taxa_found, family_stats ->
                    ^^^^^^^^^^^
  ```

- Warning: `subworkflows/local/prepare_input/main.nf:190:32`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          .filter { sample_meta, taxa_found, family_stats ->
                                 ^^^^^^^^^^
  ```

- Warning: `subworkflows/local/prepare_input/main.nf:204:29`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          .map { sample_meta, ref_metas -> [[id: sample_meta.sample_id]] }
                              ^^^^^^^^^
  ```

- Warning: `subworkflows/local/prepare_input/main.nf:207:19`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          .filter { it != [null, null] } // above join adds [null, null] if channel is empty
                    ^^
  ```

- Warning: `subworkflows/local/prepare_input/main.nf:216:29`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          .map { sample_meta, ref_metas -> [[id: sample_meta.sample_id]] }
                              ^^^^^^^^^
  ```

- Warning: `subworkflows/local/prepare_input/main.nf:219:19`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          .filter { it != [null, null] } // above join adds [null, null] if channel is empty
                    ^^
  ```

- Warning: `subworkflows/local/prepare_input/main.nf:230:27`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          .map { sample_id, sample_meta, ref_metas_user, ref_metas_to_download ->
                            ^^^^^^^^^^^
  ```

- Warning: `subworkflows/local/prepare_input/main.nf:233:48`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          .combine(sample_data.map{ sample_meta, ref_metas -> [[id: sample_meta.sample_id], sample_meta] }, by: 0)
                                                 ^^^^^^^^^
  ```

- Warning: `subworkflows/local/prepare_input/main.nf:234:16`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          .map { sample_id, ref_metas, sample_meta ->
                 ^^^^^^^^^
  ```

- Warning: `subworkflows/local/prepare_input/main.nf:240:15`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          .map{ sample_id, ref_meta -> ref_meta }
                ^^^^^^^^^
  ```

- Warning: `subworkflows/local/prepare_input/main.nf:245:19`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          .filter { sample_id, line_count ->
                    ^^^^^^^^^
  ```

- Warning: `subworkflows/local/prepare_input/main.nf:249:16`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          .map { sample_id, line_count, sample_meta, ref_metas ->
                 ^^^^^^^^^
  ```

- Warning: `subworkflows/local/prepare_input/main.nf:249:27`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          .map { sample_id, line_count, sample_meta, ref_metas ->
                            ^^^^^^^^^^
  ```

- Warning: `subworkflows/local/prepare_input/main.nf:253:28`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          .map{ sample_meta, ref_metas ->
                             ^^^^^^^^^
  ```

- Warning: `subworkflows/local/prepare_input/main.nf:261:15`: Variable was declared but not used

  ```nextflow
          .tap{ ref_data_with_ncbi_acc }
                ^^^^^^^^^^^^^^^^^^^^^^
  ```

- Warning: `subworkflows/local/prepare_input/main.nf:270:18`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          .filter{ sample_meta, ref_meta ->
                   ^^^^^^^^^^^
  ```

- Warning: `subworkflows/local/prepare_input/main.nf:281:16`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          .map { ncbi_acc_meta, sample_meta, ref_meta, ref_path, gff_path ->
                 ^^^^^^^^^^^^^
  ```

- Warning: `subworkflows/local/prepare_input/main.nf:306:22`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          .map { [[id: it.sample_id], it.paths, it.sendsketch_depth] }
                       ^^
  ```

- Warning: `subworkflows/local/prepare_input/main.nf:306:37`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          .map { [[id: it.sample_id], it.paths, it.sendsketch_depth] }
                                      ^^
  ```

- Warning: `subworkflows/local/prepare_input/main.nf:306:47`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          .map { [[id: it.sample_id], it.paths, it.sendsketch_depth] }
                                                ^^
  ```

- Warning: `subworkflows/local/prepare_input/main.nf:308:19`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          .filter { sample_id, fastq_paths, depth ->
                    ^^^^^^^^^
  ```

- Warning: `subworkflows/local/prepare_input/main.nf:308:30`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          .filter { sample_id, fastq_paths, depth ->
                               ^^^^^^^^^^^
  ```

- Warning: `subworkflows/local/prepare_input/main.nf:313:13`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
              it.sendsketch_depth.toFloat() <= params.max_depth.toFloat()
              ^^
  ```

- Warning: `subworkflows/local/prepare_input/main.nf:317:46`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
              .map { sample_meta, fastq_paths, depth ->
                                               ^^^^^
  ```

- Warning: `subworkflows/local/prepare_input/main.nf:343:16`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          .map { sample_id, sample_meta, subset_reads ->
                 ^^^^^^^^^
  ```

- Warning: `subworkflows/local/sketch_comparison/main.nf:17:22`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          .map { [[id: it.sample_id], it.paths] }
                       ^^
  ```

- Warning: `subworkflows/local/sketch_comparison/main.nf:17:37`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          .map { [[id: it.sample_id], it.paths] }
                                      ^^
  ```

- Warning: `subworkflows/local/sketch_comparison/main.nf:36:16`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          .map{ [it.ref_metas] }
                 ^^
  ```

- Warning: `subworkflows/local/sketch_comparison/main.nf:48:22`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          .map { [[id: it.sample_id], [id: it.report_group_ids]] }
                       ^^
  ```

- Warning: `subworkflows/local/sketch_comparison/main.nf:48:42`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          .map { [[id: it.sample_id], [id: it.report_group_ids]] }
                                           ^^
  ```

- Warning: `subworkflows/local/sketch_comparison/main.nf:50:16`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          .map { sample_id, report_group_id, signature -> [report_group_id, signature]}
                 ^^^^^^^^^
  ```

- Warning: `subworkflows/local/sketch_comparison/main.nf:53:16`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          .map{ [it.ref_metas, [id: it.report_group_ids]] }
                 ^^
  ```

- Warning: `subworkflows/local/sketch_comparison/main.nf:53:35`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          .map{ [it.ref_metas, [id: it.report_group_ids]] }
                                    ^^
  ```

- Warning: `subworkflows/local/sketch_comparison/main.nf:57:15`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          .map{ ref_id, report_group_id, signature -> [report_group_id, signature]}
                ^^^^^^
  ```

- Warning: `subworkflows/local/sketch_comparison/main.nf:60:22`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          .map { [[id: it.sample_id], [id: it.report_group_ids]] }
                       ^^
  ```

- Warning: `subworkflows/local/sketch_comparison/main.nf:60:42`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          .map { [[id: it.sample_id], [id: it.report_group_ids]] }
                                           ^^
  ```

- Warning: `subworkflows/local/sketch_comparison/main.nf:62:15`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          .map{ sample_id, report_group_id, signature -> [report_group_id, signature]}
                ^^^^^^^^^
  ```

- Warning: `subworkflows/local/utils_nfcore_pathogensurveillance_pipeline/main.nf:34:5`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
      input             //  string: Path to input samplesheet
      ^^^^^
  ```

- Warning: `subworkflows/local/utils_nfcore_pathogensurveillance_pipeline/main.nf:38:5`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
      reference_data    //  string: Path to reference data samplesheet
      ^^^^^^^^^^^^^^
  ```

- Warning: `subworkflows/local/variant_analysis/main.nf:21:20`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          .map{[[id: it.report_group_ids], it]}
                     ^^
  ```

- Warning: `subworkflows/local/variant_analysis/main.nf:21:42`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          .map{[[id: it.report_group_ids], it]}
                                           ^^
  ```

- Warning: `subworkflows/local/variant_analysis/main.nf:24:18`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          .filter{ it[1].size() > 1 }
                   ^^
  ```

- Warning: `subworkflows/local/variant_analysis/main.nf:26:15`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          .map{ it[1] }
                ^^
  ```

- Warning: `subworkflows/local/variant_analysis/main.nf:29:22`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
              .filter{ it[1].size() == 1 }
                       ^^
  ```

- Warning: `subworkflows/local/variant_analysis/main.nf:37:16`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          .map{ [it.sample_id, it.report_group_ids, it.ref_metas] }
                 ^^
  ```

- Warning: `subworkflows/local/variant_analysis/main.nf:37:30`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          .map{ [it.sample_id, it.report_group_ids, it.ref_metas] }
                               ^^
  ```

- Warning: `subworkflows/local/variant_analysis/main.nf:37:51`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          .map{ [it.sample_id, it.report_group_ids, it.ref_metas] }
                                                    ^^
  ```

- Warning: `subworkflows/local/variant_analysis/main.nf:44:82`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          .collectFile() { sample_id, report_group_id, ref_id, ref_name, ref_desc, ref_path, usage ->
                                                                                   ^^^^^^^^
  ```

- Warning: `subworkflows/local/variant_analysis/main.nf:47:21`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          .map {[[id: it.getSimpleName()], it]}
                      ^^
  ```

- Warning: `subworkflows/local/variant_analysis/main.nf:47:42`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          .map {[[id: it.getSimpleName()], it]}
                                           ^^
  ```

- Warning: `subworkflows/local/variant_analysis/main.nf:56:51`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          .map {sample_id, report_group_id, ref_id, ref_name, ref_desc, ref_path, usage ->
                                                    ^^^^^^^^
  ```

- Warning: `subworkflows/local/variant_analysis/main.nf:56:61`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          .map {sample_id, report_group_id, ref_id, ref_name, ref_desc, ref_path, usage ->
                                                              ^^^^^^^^
  ```

- Warning: `subworkflows/local/variant_analysis/main.nf:62:17`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          .map { [it[0], it[1].replace('\n', '')] } // remove newline that splitText adds
                  ^^
  ```

- Warning: `subworkflows/local/variant_analysis/main.nf:62:24`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          .map { [it[0], it[1].replace('\n', '')] } // remove newline that splitText adds
                         ^^
  ```

- Warning: `subworkflows/local/variant_analysis/main.nf:68:38`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          .join(sample_data.map{ [[id: it.sample_id], [id: it.report_group_ids], it.paths, it.sequence_type, it.ploidy] }, by: 0..1)
                                       ^^
  ```

- Warning: `subworkflows/local/variant_analysis/main.nf:68:58`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          .join(sample_data.map{ [[id: it.sample_id], [id: it.report_group_ids], it.paths, it.sequence_type, it.ploidy] }, by: 0..1)
                                                           ^^
  ```

- Warning: `subworkflows/local/variant_analysis/main.nf:68:80`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          .join(sample_data.map{ [[id: it.sample_id], [id: it.report_group_ids], it.paths, it.sequence_type, it.ploidy] }, by: 0..1)
                                                                                 ^^
  ```

- Warning: `subworkflows/local/variant_analysis/main.nf:68:90`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          .join(sample_data.map{ [[id: it.sample_id], [id: it.report_group_ids], it.paths, it.sequence_type, it.ploidy] }, by: 0..1)
                                                                                           ^^
  ```

- Warning: `subworkflows/local/variant_analysis/main.nf:68:108`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          .join(sample_data.map{ [[id: it.sample_id], [id: it.report_group_ids], it.paths, it.sequence_type, it.ploidy] }, by: 0..1)
                                                                                                             ^^
  ```

- Warning: `subworkflows/local/variant_analysis/main.nf:70:23`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
              filtered: it[2] != null
                        ^^
  ```

- Warning: `subworkflows/local/variant_analysis/main.nf:71:21`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
              no_ref: it[2] == null
                      ^^
  ```

- Warning: `subworkflows/local/variant_analysis/main.nf:81:18`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          .filter{ it[2].size() >= 2 }
                   ^^
  ```

- Warning: `subworkflows/local/variant_analysis/main.nf:83:15`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          .map{ it[2] }
                ^^
  ```

- Warning: `subworkflows/local/variant_analysis/main.nf:86:22`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
              .filter{ it[2].size() < 2 }
                       ^^
  ```

- Warning: `subworkflows/local/variant_analysis/main.nf:94:19`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          .filter { sample_meta, report_meta, ref_meta, ref_path, usage, read_paths, sequence_type, ploidy ->
                    ^^^^^^^^^^^
  ```

- Warning: `subworkflows/local/variant_analysis/main.nf:94:32`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          .filter { sample_meta, report_meta, ref_meta, ref_path, usage, read_paths, sequence_type, ploidy ->
                                 ^^^^^^^^^^^
  ```

- Warning: `subworkflows/local/variant_analysis/main.nf:94:45`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          .filter { sample_meta, report_meta, ref_meta, ref_path, usage, read_paths, sequence_type, ploidy ->
                                              ^^^^^^^^
  ```

- Warning: `subworkflows/local/variant_analysis/main.nf:94:55`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          .filter { sample_meta, report_meta, ref_meta, ref_path, usage, read_paths, sequence_type, ploidy ->
                                                        ^^^^^^^^
  ```

- Warning: `subworkflows/local/variant_analysis/main.nf:94:65`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          .filter { sample_meta, report_meta, ref_meta, ref_path, usage, read_paths, sequence_type, ploidy ->
                                                                  ^^^^^
  ```

- Warning: `subworkflows/local/variant_analysis/main.nf:94:72`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          .filter { sample_meta, report_meta, ref_meta, ref_path, usage, read_paths, sequence_type, ploidy ->
                                                                         ^^^^^^^^^^
  ```

- Warning: `subworkflows/local/variant_analysis/main.nf:94:99`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          .filter { sample_meta, report_meta, ref_meta, ref_path, usage, read_paths, sequence_type, ploidy ->
                                                                                                    ^^^^^^
  ```

- Warning: `subworkflows/local/variant_analysis/main.nf:98:38`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          longreads.map { sample_meta, report_meta, ref_meta, ref_path, usage, read_paths, sequence_type, ploidy ->
                                       ^^^^^^^^^^^
  ```

- Warning: `subworkflows/local/variant_analysis/main.nf:98:51`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          longreads.map { sample_meta, report_meta, ref_meta, ref_path, usage, read_paths, sequence_type, ploidy ->
                                                    ^^^^^^^^
  ```

- Warning: `subworkflows/local/variant_analysis/main.nf:98:61`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          longreads.map { sample_meta, report_meta, ref_meta, ref_path, usage, read_paths, sequence_type, ploidy ->
                                                              ^^^^^^^^
  ```

- Warning: `subworkflows/local/variant_analysis/main.nf:98:71`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          longreads.map { sample_meta, report_meta, ref_meta, ref_path, usage, read_paths, sequence_type, ploidy ->
                                                                        ^^^^^
  ```

- Warning: `subworkflows/local/variant_analysis/main.nf:98:90`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          longreads.map { sample_meta, report_meta, ref_meta, ref_path, usage, read_paths, sequence_type, ploidy ->
                                                                                           ^^^^^^^^^^^^^
  ```

- Warning: `subworkflows/local/variant_analysis/main.nf:98:105`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          longreads.map { sample_meta, report_meta, ref_meta, ref_path, usage, read_paths, sequence_type, ploidy ->
                                                                                                          ^^^^^^
  ```

- Warning: `subworkflows/local/variant_analysis/main.nf:106:84`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          .map { sample_meta, chopped_reads, report_meta, ref_meta, ref_path, usage, read_paths, sequence_type, ploidy ->
                                                                                     ^^^^^^^^^^
  ```

- Warning: `subworkflows/local/variant_analysis/main.nf:110:19`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          .filter { sample_meta, report_meta, ref_meta, ref_path, usage, read_paths, sequence_type, ploidy ->
                    ^^^^^^^^^^^
  ```

- Warning: `subworkflows/local/variant_analysis/main.nf:110:32`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          .filter { sample_meta, report_meta, ref_meta, ref_path, usage, read_paths, sequence_type, ploidy ->
                                 ^^^^^^^^^^^
  ```

- Warning: `subworkflows/local/variant_analysis/main.nf:110:45`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          .filter { sample_meta, report_meta, ref_meta, ref_path, usage, read_paths, sequence_type, ploidy ->
                                              ^^^^^^^^
  ```

- Warning: `subworkflows/local/variant_analysis/main.nf:110:55`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          .filter { sample_meta, report_meta, ref_meta, ref_path, usage, read_paths, sequence_type, ploidy ->
                                                        ^^^^^^^^
  ```

- Warning: `subworkflows/local/variant_analysis/main.nf:110:65`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          .filter { sample_meta, report_meta, ref_meta, ref_path, usage, read_paths, sequence_type, ploidy ->
                                                                  ^^^^^
  ```

- Warning: `subworkflows/local/variant_analysis/main.nf:110:72`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          .filter { sample_meta, report_meta, ref_meta, ref_path, usage, read_paths, sequence_type, ploidy ->
                                                                         ^^^^^^^^^^
  ```

- Warning: `subworkflows/local/variant_analysis/main.nf:110:99`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          .filter { sample_meta, report_meta, ref_meta, ref_path, usage, read_paths, sequence_type, ploidy ->
                                                                                                    ^^^^^^
  ```

- Warning: `subworkflows/local/variant_analysis/main.nf:118:41`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          .map{ sample_meta, report_meta, ref_meta, ref_path, usage, read_paths, sequence_type, ploidy ->
                                          ^^^^^^^^
  ```

- Warning: `subworkflows/local/variant_analysis/main.nf:118:51`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          .map{ sample_meta, report_meta, ref_meta, ref_path, usage, read_paths, sequence_type, ploidy ->
                                                    ^^^^^^^^
  ```

- Warning: `subworkflows/local/variant_analysis/main.nf:118:61`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          .map{ sample_meta, report_meta, ref_meta, ref_path, usage, read_paths, sequence_type, ploidy ->
                                                              ^^^^^
  ```

- Warning: `subworkflows/local/variant_analysis/main.nf:118:68`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          .map{ sample_meta, report_meta, ref_meta, ref_path, usage, read_paths, sequence_type, ploidy ->
                                                                     ^^^^^^^^^^
  ```

- Warning: `subworkflows/local/variant_analysis/main.nf:118:80`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          .map{ sample_meta, report_meta, ref_meta, ref_path, usage, read_paths, sequence_type, ploidy ->
                                                                                 ^^^^^^^^^^^^^
  ```

- Warning: `subworkflows/local/variant_analysis/main.nf:118:95`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          .map{ sample_meta, report_meta, ref_meta, ref_path, usage, read_paths, sequence_type, ploidy ->
                                                                                                ^^^^^^
  ```

- Warning: `subworkflows/local/variant_analysis/main.nf:126:19`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
              .map{ sample_meta, report_meta, ref_meta, ref_path, usage, read_paths, sequence_type, ploidy ->
                    ^^^^^^^^^^^
  ```

- Warning: `subworkflows/local/variant_analysis/main.nf:126:32`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
              .map{ sample_meta, report_meta, ref_meta, ref_path, usage, read_paths, sequence_type, ploidy ->
                                 ^^^^^^^^^^^
  ```

- Warning: `subworkflows/local/variant_analysis/main.nf:126:65`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
              .map{ sample_meta, report_meta, ref_meta, ref_path, usage, read_paths, sequence_type, ploidy ->
                                                                  ^^^^^
  ```

- Warning: `subworkflows/local/variant_analysis/main.nf:126:72`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
              .map{ sample_meta, report_meta, ref_meta, ref_path, usage, read_paths, sequence_type, ploidy ->
                                                                         ^^^^^^^^^^
  ```

- Warning: `subworkflows/local/variant_analysis/main.nf:126:84`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
              .map{ sample_meta, report_meta, ref_meta, ref_path, usage, read_paths, sequence_type, ploidy ->
                                                                                     ^^^^^^^^^^^^^
  ```

- Warning: `subworkflows/local/variant_analysis/main.nf:126:99`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
              .map{ sample_meta, report_meta, ref_meta, ref_path, usage, read_paths, sequence_type, ploidy ->
                                                                                                    ^^^^^^
  ```

- Warning: `subworkflows/local/variant_analysis/main.nf:134:61`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          .map{ sample_meta, report_meta, ref_meta, ref_path, usage, read_paths, sequence_type, ploidy ->
                                                              ^^^^^
  ```

- Warning: `subworkflows/local/variant_analysis/main.nf:134:80`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          .map{ sample_meta, report_meta, ref_meta, ref_path, usage, read_paths, sequence_type, ploidy ->
                                                                                 ^^^^^^^^^^^^^
  ```

- Warning: `subworkflows/local/variant_analysis/main.nf:134:95`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          .map{ sample_meta, report_meta, ref_meta, ref_path, usage, read_paths, sequence_type, ploidy ->
                                                                                                ^^^^^^
  ```

- Warning: `subworkflows/local/variant_analysis/main.nf:146:20`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
              .map { it[0..3] + it[5..6] }
                     ^^
  ```

- Warning: `subworkflows/local/variant_analysis/main.nf:146:31`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
              .map { it[0..3] + it[5..6] }
                                ^^
  ```

- Warning: `subworkflows/local/variant_analysis/main.nf:153:21`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
              .map { [it[0], it[2], it[1]] + it[3..5] + [it[7]] } // [val(meta), val(ref_meta), [file(fastq)], file(reference), val(report_meta), fai, picard]
                      ^^
  ```

- Warning: `subworkflows/local/variant_analysis/main.nf:153:28`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
              .map { [it[0], it[2], it[1]] + it[3..5] + [it[7]] } // [val(meta), val(ref_meta), [file(fastq)], file(reference), val(report_meta), fai, picard]
                             ^^
  ```

- Warning: `subworkflows/local/variant_analysis/main.nf:153:35`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
              .map { [it[0], it[2], it[1]] + it[3..5] + [it[7]] } // [val(meta), val(ref_meta), [file(fastq)], file(reference), val(report_meta), fai, picard]
                                    ^^
  ```

- Warning: `subworkflows/local/variant_analysis/main.nf:153:44`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
              .map { [it[0], it[2], it[1]] + it[3..5] + [it[7]] } // [val(meta), val(ref_meta), [file(fastq)], file(reference), val(report_meta), fai, picard]
                                             ^^
  ```

- Warning: `subworkflows/local/variant_analysis/main.nf:153:56`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
              .map { [it[0], it[2], it[1]] + it[3..5] + [it[7]] } // [val(meta), val(ref_meta), [file(fastq)], file(reference), val(report_meta), fai, picard]
                                                         ^^
  ```

- Warning: `subworkflows/local/variant_analysis/main.nf:156:21`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
              .map { [it[0], it[7], it[8], it[1]] + it[3..6] }
                      ^^
  ```

- Warning: `subworkflows/local/variant_analysis/main.nf:156:28`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
              .map { [it[0], it[7], it[8], it[1]] + it[3..6] }
                             ^^
  ```

- Warning: `subworkflows/local/variant_analysis/main.nf:156:35`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
              .map { [it[0], it[7], it[8], it[1]] + it[3..6] }
                                    ^^
  ```

- Warning: `subworkflows/local/variant_analysis/main.nf:156:42`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
              .map { [it[0], it[7], it[8], it[1]] + it[3..6] }
                                           ^^
  ```

- Warning: `subworkflows/local/variant_analysis/main.nf:156:51`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
              .map { [it[0], it[7], it[8], it[1]] + it[3..6] }
                                                    ^^
  ```

- Warning: `subworkflows/local/variant_analysis/main.nf:161:87`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          .collectFile(keepHeader: true, skip: 1) { sample_meta, report_meta, ref_meta, ref_path, usage, read_paths, sequence_type, ploidy ->
                                                                                        ^^^^^^^^
  ```

- Warning: `subworkflows/local/variant_analysis/main.nf:161:97`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          .collectFile(keepHeader: true, skip: 1) { sample_meta, report_meta, ref_meta, ref_path, usage, read_paths, sequence_type, ploidy ->
                                                                                                  ^^^^^
  ```

- Warning: `subworkflows/local/variant_analysis/main.nf:161:104`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          .collectFile(keepHeader: true, skip: 1) { sample_meta, report_meta, ref_meta, ref_path, usage, read_paths, sequence_type, ploidy ->
                                                                                                         ^^^^^^^^^^
  ```

- Warning: `subworkflows/local/variant_analysis/main.nf:161:116`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          .collectFile(keepHeader: true, skip: 1) { sample_meta, report_meta, ref_meta, ref_path, usage, read_paths, sequence_type, ploidy ->
                                                                                                                     ^^^^^^^^^^^^^
  ```

- Warning: `subworkflows/local/variant_analysis/main.nf:164:17`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          .map { [it.getSimpleName(), it] }
                  ^^
  ```

- Warning: `subworkflows/local/variant_analysis/main.nf:164:37`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          .map { [it.getSimpleName(), it] }
                                      ^^
  ```

- Warning: `subworkflows/local/variant_analysis/main.nf:165:61`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          .combine(CALL_VARIANTS.out.vcf.map { combined_meta, vcf -> [combined_meta.id, combined_meta]}, by: 0) // add on full combined metadata uing combined ID
                                                              ^^^
  ```

- Warning: `subworkflows/local/variant_analysis/main.nf:166:16`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          .map { combined_id, ploidy_data_path, combined_meta ->
                 ^^^^^^^^^^^
  ```

- Warning: `subworkflows/local/variant_analysis/main.nf:176:5`: Variable was declared but not used

  ```nextflow
      removed_samps = VCF_TO_SNP_ALIGN.out.removed_sample_ids
      ^^^^^^^^^^^^^
  ```

- Warning: `subworkflows/local/variant_analysis/main.nf:178:22`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          .map { [[id: it[1].replace('\n', '')], it[0].group, it[0].ref, "VARIANT_ANALYSIS", "WARNING", "Sample removed from SNP phylogeny due to too much missing data."] } // meta, group_meta, ref_meta, workflow, level, message
                       ^^
  ```

- Warning: `subworkflows/local/variant_analysis/main.nf:178:48`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          .map { [[id: it[1].replace('\n', '')], it[0].group, it[0].ref, "VARIANT_ANALYSIS", "WARNING", "Sample removed from SNP phylogeny due to too much missing data."] } // meta, group_meta, ref_meta, workflow, level, message
                                                 ^^
  ```

- Warning: `subworkflows/local/variant_analysis/main.nf:178:61`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          .map { [[id: it[1].replace('\n', '')], it[0].group, it[0].ref, "VARIANT_ANALYSIS", "WARNING", "Sample removed from SNP phylogeny due to too much missing data."] } // meta, group_meta, ref_meta, workflow, level, message
                                                              ^^
  ```

- Warning: `subworkflows/local/variant_analysis/main.nf:190:22`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          .map { meta, fasta -> [null, meta.group, meta.ref, "VARIANT_ANALYSIS", "WARNING", "Not enough samples to build a SNP tree."] }
                       ^^^^^
  ```

- Warning: `subworkflows/local/variant_analysis/main.nf:200:48`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
      phylogeny = IQTREE_SNP.out.phylogeny.map{ [it[0].group, it[0].ref, it[1]] } // report_meta, ref_meta, tree
                                                 ^^
  ```

- Warning: `subworkflows/local/variant_analysis/main.nf:200:61`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
      phylogeny = IQTREE_SNP.out.phylogeny.map{ [it[0].group, it[0].ref, it[1]] } // report_meta, ref_meta, tree
                                                              ^^
  ```

- Warning: `subworkflows/local/variant_analysis/main.nf:200:72`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
      phylogeny = IQTREE_SNP.out.phylogeny.map{ [it[0].group, it[0].ref, it[1]] } // report_meta, ref_meta, tree
                                                                         ^^
  ```

- Warning: `subworkflows/local/variant_analysis/main.nf:201:50`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
      snp_align = VCF_TO_SNP_ALIGN.out.fasta.map{ [it[0].group, it[0].ref, it[1]] }
                                                   ^^
  ```

- Warning: `subworkflows/local/variant_analysis/main.nf:201:63`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
      snp_align = VCF_TO_SNP_ALIGN.out.fasta.map{ [it[0].group, it[0].ref, it[1]] }
                                                                ^^
  ```

- Warning: `subworkflows/local/variant_analysis/main.nf:201:74`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
      snp_align = VCF_TO_SNP_ALIGN.out.fasta.map{ [it[0].group, it[0].ref, it[1]] }
                                                                           ^^
  ```

- Warning: `subworkflows/local/variant_analysis/main.nf:202:39`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
      vcf = CALL_VARIANTS.out.vcf.map{ [it[0].group, it[0].ref, it[1]] }
                                        ^^
  ```

- Warning: `subworkflows/local/variant_analysis/main.nf:202:52`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
      vcf = CALL_VARIANTS.out.vcf.map{ [it[0].group, it[0].ref, it[1]] }
                                                     ^^
  ```

- Warning: `subworkflows/local/variant_analysis/main.nf:202:63`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
      vcf = CALL_VARIANTS.out.vcf.map{ [it[0].group, it[0].ref, it[1]] }
                                                                ^^
  ```

- Warning: `subworkflows/local/variant_analysis/main.nf:207:16`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          .map{ [it[0].group, it[0].ref] + it[1..3] } // report_meta, ref_meta, vcf, align, tree
                 ^^
  ```

- Warning: `subworkflows/local/variant_analysis/main.nf:207:29`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          .map{ [it[0].group, it[0].ref] + it[1..3] } // report_meta, ref_meta, vcf, align, tree
                              ^^
  ```

- Warning: `subworkflows/local/variant_analysis/main.nf:207:42`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          .map{ [it[0].group, it[0].ref] + it[1..3] } // report_meta, ref_meta, vcf, align, tree
                                           ^^
  ```

- Warning: `workflows/pathogensurveillance.nf:150:21`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          .map{ [[id: it.sample_id], [id: it.report_group_ids]] }
                      ^^
  ```

- Warning: `workflows/pathogensurveillance.nf:150:41`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          .map{ [[id: it.sample_id], [id: it.report_group_ids]] }
                                          ^^
  ```

- Warning: `workflows/pathogensurveillance.nf:152:15`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          .map{ sample_meta, report_meta, fastqc -> [report_meta, fastqc] }
                ^^^^^^^^^^^
  ```

- Warning: `workflows/pathogensurveillance.nf:156:21`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          .map{ [[id: it.sample_id], [id: it.report_group_ids]] }
                      ^^
  ```

- Warning: `workflows/pathogensurveillance.nf:156:41`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          .map{ [[id: it.sample_id], [id: it.report_group_ids]] }
                                          ^^
  ```

- Warning: `workflows/pathogensurveillance.nf:158:15`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          .map{ sample_meta, report_meta, fastp_json -> [report_meta, fastp_json] }
                ^^^^^^^^^^^
  ```

- Warning: `workflows/pathogensurveillance.nf:162:21`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          .map{ [[id: it.sample_id], [id: it.report_group_ids]] }
                      ^^
  ```

- Warning: `workflows/pathogensurveillance.nf:162:41`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          .map{ [[id: it.sample_id], [id: it.report_group_ids]] }
                                          ^^
  ```

- Warning: `workflows/pathogensurveillance.nf:164:15`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          .map{ sample_meta, report_meta, nanoplot_txt -> [report_meta, nanoplot_txt] }
                ^^^^^^^^^^^
  ```

- Warning: `workflows/pathogensurveillance.nf:168:21`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          .map{ [[id: it.sample_id], [id: it.report_group_ids]] }
                      ^^
  ```

- Warning: `workflows/pathogensurveillance.nf:168:41`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          .map{ [[id: it.sample_id], [id: it.report_group_ids]] }
                                          ^^
  ```

- Warning: `workflows/pathogensurveillance.nf:170:15`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          .map{ sample_meta, report_meta, quast -> [report_meta, quast] }
                ^^^^^^^^^^^
  ```

- Warning: `workflows/pathogensurveillance.nf:174:21`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          .map{ [[id: it.report_group_ids]] }
                      ^^
  ```

- Warning: `workflows/pathogensurveillance.nf:202:71`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
              [[id: sample_meta.report_group_ids], sample_meta.findAll {it.key != 'paths' && it.key != 'ref_metas' && it.key != 'ref_ids'}]
                                                                        ^^
  ```

- Warning: `workflows/pathogensurveillance.nf:202:92`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
              [[id: sample_meta.report_group_ids], sample_meta.findAll {it.key != 'paths' && it.key != 'ref_metas' && it.key != 'ref_ids'}]
                                                                                             ^^
  ```

- Warning: `workflows/pathogensurveillance.nf:202:117`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
              [[id: sample_meta.report_group_ids], sample_meta.findAll {it.key != 'paths' && it.key != 'ref_metas' && it.key != 'ref_ids'}]
                                                                                                                      ^^
  ```

- Warning: `workflows/pathogensurveillance.nf:206:87`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
              [ "${report_meta.id}_sample_data.tsv", sample_meta.keySet().collect{'"' + it + '"'}.join('\t') + "\n" + sample_meta.values().collect{'"' + (it ?: '') + '"'}.join('\t') + "\n" ]
                                                                                        ^^
  ```

- Warning: `workflows/pathogensurveillance.nf:206:153`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
              [ "${report_meta.id}_sample_data.tsv", sample_meta.keySet().collect{'"' + it + '"'}.join('\t') + "\n" + sample_meta.values().collect{'"' + (it ?: '') + '"'}.join('\t') + "\n" ]
                                                                                                                                                          ^^
  ```

- Warning: `workflows/pathogensurveillance.nf:208:21`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          .map {[[id: it.getSimpleName().replace('_sample_data', '')], it]}
                      ^^
  ```

- Warning: `workflows/pathogensurveillance.nf:208:70`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          .map {[[id: it.getSimpleName().replace('_sample_data', '')], it]}
                                                                       ^^
  ```

- Warning: `workflows/pathogensurveillance.nf:217:45`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
              [report_meta, ref_meta.findAll {it.key != 'ref_path' && it.key != 'gff'}]
                                              ^^
  ```

- Warning: `workflows/pathogensurveillance.nf:217:69`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
              [report_meta, ref_meta.findAll {it.key != 'ref_path' && it.key != 'gff'}]
                                                                      ^^
  ```

- Warning: `workflows/pathogensurveillance.nf:221:87`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
              [ "${report_meta.id}_reference_data.tsv", ref_meta.keySet().collect{'"' + it + '"'}.join('\t') + "\n" + ref_meta.values().collect{'"' + (it ?: '') + '"'}.join('\t') + "\n" ]
                                                                                        ^^
  ```

- Warning: `workflows/pathogensurveillance.nf:221:150`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
              [ "${report_meta.id}_reference_data.tsv", ref_meta.keySet().collect{'"' + it + '"'}.join('\t') + "\n" + ref_meta.values().collect{'"' + (it ?: '') + '"'}.join('\t') + "\n" ]
                                                                                                                                                       ^^
  ```

- Warning: `workflows/pathogensurveillance.nf:223:21`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          .map {[[id: it.getSimpleName().replace('_reference_data', '')], it]}
                      ^^
  ```

- Warning: `workflows/pathogensurveillance.nf:223:73`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          .map {[[id: it.getSimpleName().replace('_reference_data', '')], it]}
                                                                          ^^
  ```

- Warning: `workflows/pathogensurveillance.nf:227:21`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          .map{ [[id: it.sample_id], [id: it.report_group_ids]] }
                      ^^
  ```

- Warning: `workflows/pathogensurveillance.nf:227:41`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          .map{ [[id: it.sample_id], [id: it.report_group_ids]] }
                                          ^^
  ```

- Warning: `workflows/pathogensurveillance.nf:229:15`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          .map{ sample_meta, report_meta, sendsketch -> [report_meta, sendsketch] }
                ^^^^^^^^^^^
  ```

- Warning: `workflows/pathogensurveillance.nf:235:21`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          .map{ [[id: it.sample_id], [id: it.report_group_ids]] }
                      ^^
  ```

- Warning: `workflows/pathogensurveillance.nf:235:41`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          .map{ [[id: it.sample_id], [id: it.report_group_ids]] }
                                          ^^
  ```

- Warning: `workflows/pathogensurveillance.nf:238:16`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          .map { sample_meta, report_meta, family_stats ->
                 ^^^^^^^^^^^
  ```

- Warning: `workflows/pathogensurveillance.nf:244:21`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          .map{ [[id: it.sample_id], [id: it.report_group_ids]] }
                      ^^
  ```

- Warning: `workflows/pathogensurveillance.nf:244:41`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          .map{ [[id: it.sample_id], [id: it.report_group_ids]] }
                                          ^^
  ```

- Warning: `workflows/pathogensurveillance.nf:246:15`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          .map{ sample_meta, report_meta, ref_meta_file ->
                ^^^^^^^^^^^
  ```

- Warning: `workflows/pathogensurveillance.nf:251:50`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
              [report_meta, ref_meta_files.findAll{it != null}]
                                                   ^^
  ```

- Warning: `workflows/pathogensurveillance.nf:256:29`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          .map { report_meta, ref_meta, fasta -> [report_meta, fasta] }
                              ^^^^^^^^
  ```

- Warning: `workflows/pathogensurveillance.nf:261:29`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          .map { report_meta, ref_meta, tree -> [report_meta, tree] }
                              ^^^^^^^^
  ```

- Warning: `workflows/pathogensurveillance.nf:270:21`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          .map {[[id: it.getSimpleName()], it]}
                      ^^
  ```

- Warning: `workflows/pathogensurveillance.nf:270:42`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          .map {[[id: it.getSimpleName()], it]}
                                           ^^
  ```

- Warning: `workflows/pathogensurveillance.nf:290:17`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          .filter{it[0] != null}
                  ^^
  ```

- Warning: `workflows/pathogensurveillance.nf:291:15`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          .map{ it.size() == 16 ? it + [null] : it }
                ^^
  ```

- Warning: `workflows/pathogensurveillance.nf:291:33`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          .map{ it.size() == 16 ? it + [null] : it }
                                  ^^
  ```

- Warning: `workflows/pathogensurveillance.nf:291:47`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          .map{ it.size() == 16 ? it + [null] : it }
                                                ^^
  ```

- Warning: `workflows/pathogensurveillance.nf:292:18`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          .filter{ it.size() == 17 }
                   ^^
  ```

- Warning: `workflows/pathogensurveillance.nf:293:15`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          .map{ it.collect{ it ?: [] } }
                ^^
  ```

- Warning: `workflows/pathogensurveillance.nf:293:27`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          .map{ it.collect{ it ?: [] } }
                            ^^
  ```

- Warning: `workflows/pathogensurveillance.nf:341:34`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
              sample_meta.findAll {it.key != 'paths' && it.key != 'ref_metas' && it.key != 'ref_ids'}
                                   ^^
  ```

- Warning: `workflows/pathogensurveillance.nf:341:55`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
              sample_meta.findAll {it.key != 'paths' && it.key != 'ref_metas' && it.key != 'ref_ids'}
                                                        ^^
  ```

- Warning: `workflows/pathogensurveillance.nf:341:80`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
              sample_meta.findAll {it.key != 'paths' && it.key != 'ref_metas' && it.key != 'ref_ids'}
                                                                                 ^^
  ```

- Warning: `workflows/pathogensurveillance.nf:350:48`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
              sample_meta.keySet().collect{'"' + it + '"'}.join('\t') + "\n" + sample_meta.values().collect{'"' + (it ?: '') + '"'}.join('\t') + "\n"
                                                 ^^
  ```

- Warning: `workflows/pathogensurveillance.nf:350:114`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
              sample_meta.keySet().collect{'"' + it + '"'}.join('\t') + "\n" + sample_meta.values().collect{'"' + (it ?: '') + '"'}.join('\t') + "\n"
                                                                                                                   ^^
  ```

- Warning: `workflows/pathogensurveillance.nf:360:34`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
              ref_meta[0].findAll {it.key != 'ref_path' && it.key != 'gff'}
                                   ^^
  ```

- Warning: `workflows/pathogensurveillance.nf:360:58`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
              ref_meta[0].findAll {it.key != 'ref_path' && it.key != 'gff'}
                                                           ^^
  ```

- Warning: `workflows/pathogensurveillance.nf:369:45`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
              ref_meta.keySet().collect{'"' + it + '"'}.join('\t') + "\n" + ref_meta.values().collect{'"' + (it ?: '') + '"'}.join('\t') + "\n"
                                              ^^
  ```

- Warning: `workflows/pathogensurveillance.nf:369:108`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
              ref_meta.keySet().collect{'"' + it + '"'}.join('\t') + "\n" + ref_meta.values().collect{'"' + (it ?: '') + '"'}.join('\t') + "\n"
                                                                                                             ^^
  ```
