# Nextflow lint results

- Generated: 2026-09-05T00:20:08.508724712Z
- Nextflow version: 26.08.0-edge
- Summary: 12 warnings

## :warning: Warnings

- Warning: `subworkflows/local/align_genome/main.nf:20:9`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          ch_genome_dictionary          // channel: [mandatory] [ val(meta), path(dict) ]
          ^^^^^^^^^^^^^^^^^^^^
  ```

- Warning: `subworkflows/local/call_snv_sentieon/main.nf:66:62`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
                  def sorted = [vcfs, idxs].transpose().sort { it[0].name }
                                                               ^^
  ```

- Warning: `subworkflows/local/call_snv_sentieon/main.nf:67:48`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
                  return [meta, sorted.collect { it[0] }, sorted.collect { it[1] }]
                                                 ^^
  ```

- Warning: `subworkflows/local/call_snv_sentieon/main.nf:67:74`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
                  return [meta, sorted.collect { it[0] }, sorted.collect { it[1] }]
                                                                           ^^
  ```

- Warning: `subworkflows/local/call_sv_MT/main.nf:137:28`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
                  .filter { !it.isEmpty() }
                             ^^
  ```

- Warning: `subworkflows/local/contamination/main.nf:58:65`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
              ch_variants_vcf = ch_contamination_sites.map { vcf, tbi -> vcf }.collect()
                                                                  ^^^
  ```

- Warning: `subworkflows/local/contamination/main.nf:59:60`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
              ch_variants_tbi = ch_contamination_sites.map { vcf, tbi -> tbi }.collect()
                                                             ^^^
  ```

- Warning: `subworkflows/local/generate_cytosure_files/main.nf:35:29`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
              .branch { meta, vcf ->
                              ^^^
  ```

- Warning: `workflows/raredisease.nf:1021:9`: Variable was declared but not used

  ```nextflow
          ch_somalier_publish = VCF_EXTRACT_RELATE_SOMALIER.out.publish
          ^^^^^^^^^^^^^^^^^^^
  ```

- Warning: `workflows/raredisease.nf:1104:5`: Variable was declared but not used

  ```nextflow
      ch_multiqc_config        = channel.fromPath(
      ^^^^^^^^^^^^^^^^^
  ```

- Warning: `workflows/raredisease.nf:1106:5`: Variable was declared but not used

  ```nextflow
      ch_multiqc_custom_config = val_multiqc_config ?
      ^^^^^^^^^^^^^^^^^^^^^^^^
  ```

- Warning: `workflows/raredisease.nf:1109:5`: Variable was declared but not used

  ```nextflow
      ch_multiqc_logo          = val_multiqc_logo ?
      ^^^^^^^^^^^^^^^
  ```
