# Nextflow lint results

- Generated: 2026-01-16T06:42:23.396670034Z
- Nextflow version: 25.12.0-edge
- Summary: 6 errors, 14 warnings

## :x: Errors

- Error: `modules/local/pcgr/main.nf:27:9`: `cna` is already declared

  ```nextflow
      def cna      = params.cna_analysis ? "--input_cna $cna" : ''
          ^^^
  ```

- Error: `subworkflows/local/format_files.nf:18:1`: Statements cannot be mixed with script declarations -- move statements into a process, workflow, or function

  ```nextflow
  pcgr_header = Channel.fromPath("${projectDir}/bin/pcgr_header.txt", checkIfExists:true)
  ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  ```

- Error: `subworkflows/local/format_files.nf:46:61`: Variables in a closure should be declared with `def`

  ```nextflow
      per_sample_somatic      = vcf_ch.map{ meta, vcf, tbi -> var = [:]; var.patient = meta.patient; var.status = meta.status; var.sample = meta.sample; return [ var, vcf, tbi ] }
                                                              ^^^
  ```

- Error: `subworkflows/local/format_files.nf:74:33`: `pcgr_header` is not defined

  ```nextflow
      PCGR_VCF( sample_vcfs_keys, pcgr_header.collect() )
                                  ^^^^^^^^^^^
  ```

- Error: `subworkflows/local/utils_nfcore_variantprioritization_pipeline/main.nf:228:147`: `metas` is not defined

  ```nextflow
              error("Please check input samplesheet -> CNA analysis selected but no copy number alteration files provided with somatic VCF files: ${metas[0].id}")
                                                                                                                                                    ^^^^^
  ```

- Error: `subworkflows/local/vcf_preprocessing.nf:36:54`: Variables in a closure should be declared with `def`

  ```nextflow
      ch_cna_files = files.cna_files.map{ meta, cna -> var = [:]; var.patient = meta.patient; var.status = meta.status; var.sample = meta.sample; return [ var, cna ] }.distinct()
                                                       ^^^
  ```

## :warning: Warnings

- Warning: `conf/modules.config:63:22`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
              ].grep { it != null }.join("").trim()
                       ^^
  ```

- Warning: `modules/local/reformat_input/isec_vcf.nf:20:9`: Variable was declared but not used

  ```nextflow
      def args = task.ext.args ?: ''
          ^^^^
  ```

- Warning: `modules/local/reformat_input/pcgr_vcf.nf:21:9`: Variable was declared but not used

  ```nextflow
      def args = task.ext.args ?: ''
          ^^^^
  ```

- Warning: `modules/nf-core/bcftools/norm/main.nf:56:65`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          if (['--write-index=tbi', '-W=tbi'].any { args.contains(it) }  && extension == 'vcf.gz') {
                                                                  ^^
  ```

- Warning: `modules/nf-core/bcftools/norm/main.nf:58:126`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          } else if (['--write-index=tbi', '-W=tbi', '--write-index=csi', '-W=csi', '--write-index', '-W'].any { args.contains(it) }) {
                                                                                                                               ^^
  ```

- Warning: `subworkflows/local/format_files.nf:18:1`: Variable was declared but not used

  ```nextflow
  pcgr_header = Channel.fromPath("${projectDir}/bin/pcgr_header.txt", checkIfExists:true)
  ^^^^^^^^^^^
  ```

- Warning: `subworkflows/local/format_files.nf:18:15`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
  pcgr_header = Channel.fromPath("${projectDir}/bin/pcgr_header.txt", checkIfExists:true)
                ^^^^^^^
  ```

- Warning: `subworkflows/local/format_files.nf:28:19`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_versions = Channel.empty()
                    ^^^^^^^
  ```

- Warning: `subworkflows/local/format_files.nf:47:55`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
      per_sample_somatic_vcfs = per_sample_somatic.map{ meta, vcf, tbi -> return [ var, vcf, tbi ] }.groupTuple()
                                                        ^^^^
  ```

- Warning: `subworkflows/local/utils_nfcore_variantprioritization_pipeline/main.nf:31:5`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
      monochrome_logs // boolean: Do not use coloured log outputs
      ^^^^^^^^^^^^^^^
  ```

- Warning: `subworkflows/local/utils_nfcore_variantprioritization_pipeline/main.nf:102:5`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      Channel
      ^^^^^^^
  ```

- Warning: `subworkflows/local/vcf_preprocessing.nf:26:19`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_versions = Channel.empty()
                    ^^^^^^^
  ```

- Warning: `subworkflows/local/vcf_preprocessing.nf:41:19`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          to_bgzip: it[0].bgzip_vcf == false
                    ^^
  ```

- Warning: `subworkflows/local/vcf_preprocessing.nf:42:19`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          to_tabix: it[0].tabix_vcf == false
                    ^^
  ```
