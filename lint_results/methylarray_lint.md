# Nextflow lint results

- Generated: 2026-01-14T09:20:26.844300057Z
- Nextflow version: 25.12.0-edge
- Summary: 3 errors, 19 warnings

## :x: Errors

- Error: `modules/local/remove_confounding_probes/main.nf:10:15`: `samplesheet_name` is already declared

  ```nextflow
      tuple val(samplesheet_name), path(bVals)
                ^^^^^^^^^^^^^^^^
  ```

- Error: `modules/local/remove_confounding_probes/main.nf:11:15`: `samplesheet_name` is already declared

  ```nextflow
      tuple val(samplesheet_name), path(RData_REMOVESNP)
                ^^^^^^^^^^^^^^^^
  ```

- Error: `modules/local/remove_sex_chromosomes/main.nf:10:15`: `samplesheet_name` is already declared

  ```nextflow
      tuple val(samplesheet_name), path(RData_rgSet)
                ^^^^^^^^^^^^^^^^
  ```

## :warning: Warnings

- Warning: `modules/local/remove_confounding_probes/main.nf:9:15`: Variable was declared but not used

  ```nextflow
      tuple val(samplesheet_name), path(mVals)
                ^^^^^^^^^^^^^^^^
  ```

- Warning: `modules/local/remove_confounding_probes/main.nf:10:15`: Variable was declared but not used

  ```nextflow
      tuple val(samplesheet_name), path(bVals)
                ^^^^^^^^^^^^^^^^
  ```

- Warning: `modules/local/remove_sex_chromosomes/main.nf:9:15`: Variable was declared but not used

  ```nextflow
      tuple val(samplesheet_name), path(RData_SNPPROBES)
                ^^^^^^^^^^^^^^^^
  ```

- Warning: `modules/local/xreactive_probes_find_remove/main.nf:25:5`: Variable was declared but not used

  ```nextflow
      chrom_number = params.xreactive_chr_targets ? params.xreactive_chr_targets : 'all'
      ^^^^^^^^^^^^
  ```

- Warning: `subworkflows/local/utils_nfcore_methylarray_pipeline/main.nf:32:5`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
      monochrome_logs   // boolean: Do not use coloured log outputs
      ^^^^^^^^^^^^^^^
  ```

- Warning: `subworkflows/local/utils_nfcore_methylarray_pipeline/main.nf:35:5`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
      input             //  string: Path to input samplesheet
      ^^^^^
  ```

- Warning: `subworkflows/local/utils_nfcore_methylarray_pipeline/main.nf:105:11`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
          ? Channel.fromList(samplesheetToList(params.input, "${projectDir}/assets/schema_input.json")) : Channel.empty()
            ^^^^^^^
  ```

- Warning: `subworkflows/local/utils_nfcore_methylarray_pipeline/main.nf:105:105`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
          ? Channel.fromList(samplesheetToList(params.input, "${projectDir}/assets/schema_input.json")) : Channel.empty()
                                                                                                          ^^^^^^^
  ```

- Warning: `workflows/methylarray.nf:42:5`: Variable was declared but not used

  ```nextflow
      ch_preprocessed_files = channel.empty()
      ^^^^^^^^^^^^^^^^^^^^^
  ```

- Warning: `workflows/methylarray.nf:49:26`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          .map{ meta, red, green -> red.getName().replaceFirst(/_Red\.idat(?:\.gz)?$/,"") + "," + meta.id }
                           ^^^^^
  ```

- Warning: `workflows/methylarray.nf:54:22`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          ch_input.map{meta, red, green -> [red, green]}.collect(),
                       ^^^^
  ```

- Warning: `workflows/methylarray.nf:90:22`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      final_bVals_ch = Channel.empty()
                       ^^^^^^^
  ```

- Warning: `workflows/methylarray.nf:91:24`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      current_bVals_ch = Channel.empty()
                         ^^^^^^^
  ```

- Warning: `workflows/methylarray.nf:95:135`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          current_bVals_ch = params.remove_snp_probes ? REMOVE_SNP_PROBES.out.csv_bVals : XREACTIVE_PROBES_FIND_REMOVE.out.csv.filter { it == "bVals_noXprob.csv" }
                                                                                                                                        ^^
  ```

- Warning: `workflows/methylarray.nf:96:135`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          current_mVals_ch = params.remove_snp_probes ? REMOVE_SNP_PROBES.out.csv_mVals : XREACTIVE_PROBES_FIND_REMOVE.out.csv.filter { it == "mVals_noXprob.csv" }
                                                                                                                                        ^^
  ```

- Warning: `workflows/methylarray.nf:97:137`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          current_mSetSqFlt_ch = params.remove_snp_probes ? REMOVE_SNP_PROBES.out.rdata : XREACTIVE_PROBES_FIND_REMOVE.out.rdata.filter { it == "mSetSqFlt_noXprob.RData" }
                                                                                                                                          ^^
  ```

- Warning: `workflows/methylarray.nf:161:30`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          ch_input.map { meta, red, green -> "${meta.id},${meta.group}" }
                               ^^^
  ```

- Warning: `workflows/methylarray.nf:161:35`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          ch_input.map { meta, red, green -> "${meta.id},${meta.group}" }
                                    ^^^^^
  ```

- Warning: `workflows/methylarray.nf:204:26`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      def topic_versions = Channel.topic("versions")
                           ^^^^^^^
  ```
