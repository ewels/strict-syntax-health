# Nextflow lint results

- Generated: 2026-01-15T09:02:15.422136Z
- Nextflow version: 25.12.0-edge
- Summary: 5 errors, 7 warnings

## :x: Errors

- Error: `/Users/ewels/GitHub/nf-core/strict-syntax-health/modules/modules/nf-core/metaphlan/makedb/main.nf:1:1`: Invalid process definition -- check for missing or out-of-order section labels

  ```nextflow
  process METAPHLAN_MAKEDB {
  ^
  ```

- Error: `subworkflows/nf-core/fastq_taxonomic_profile_metaphlan/main.nf:1:1`: Included name 'METAPHLAN_MAKEDB' is not defined in module '/Users/ewels/GitHub/nf-core/strict-syntax-health/modules/modules/nf-core/metaphlan/makedb/main.nf'

  ```nextflow
  include { METAPHLAN_MAKEDB               } from '../../../modules/nf-core/metaphlan/makedb/main'
  ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  ```

- Error: `subworkflows/nf-core/fastq_taxonomic_profile_metaphlan/main.nf:14:5`: `METAPHLAN_MAKEDB` is not defined

  ```nextflow
      METAPHLAN_MAKEDB()
      ^^^^^^^^^^^^^^^^
  ```

- Error: `subworkflows/nf-core/fastq_taxonomic_profile_metaphlan/main.nf:15:35`: `METAPHLAN_MAKEDB` is not defined

  ```nextflow
      ch_versions = ch_versions.mix(METAPHLAN_MAKEDB.out.versions.first())
                                    ^^^^^^^^^^^^^^^^
  ```

- Error: `subworkflows/nf-core/fastq_taxonomic_profile_metaphlan/main.nf:17:35`: `METAPHLAN_MAKEDB` is not defined

  ```nextflow
      METAPHLAN_METAPHLAN(ch_fastq, METAPHLAN_MAKEDB.out.db, false)
                                    ^^^^^^^^^^^^^^^^
  ```

## :warning: Warnings

- Warning: `/Users/ewels/GitHub/nf-core/strict-syntax-health/modules/modules/nf-core/metaphlan/mergemetaphlantables/main.nf:35:9`: Variable was declared but not used

  ```nextflow
      def args = task.ext.args ?: ''
          ^^^^
  ```

- Warning: `/Users/ewels/GitHub/nf-core/strict-syntax-health/modules/modules/nf-core/metaphlan/metaphlan/main.nf:58:9`: Variable was declared but not used

  ```nextflow
      def input_data = ("${input_type}".contains("fastq")) && !meta.single_end ? "${input[0]},${input[1]}" : "${input}"
          ^^^^^^^^^^
  ```

- Warning: `/Users/ewels/GitHub/nf-core/strict-syntax-health/modules/modules/nf-core/metaphlan/metaphlan/main.nf:59:9`: Variable was declared but not used

  ```nextflow
      def bowtie2_out = "${input_type}" == "--input_type bowtie2out" || "${input_type}" == "--input_type sam" ? '' : "--bowtie2out ${prefix}.bowtie2out.txt"
          ^^^^^^^^^^^
  ```

- Warning: `/Users/ewels/GitHub/nf-core/strict-syntax-health/modules/modules/nf-core/metaphlan/metaphlan/main.nf:60:9`: Variable was declared but not used

  ```nextflow
      def samfile_out = save_samfile ? "-s ${prefix}.sam" : ''
          ^^^^^^^^^^^
  ```

- Warning: `subworkflows/nf-core/fastq_taxonomic_profile_metaphlan/main.nf:12:19`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_versions = Channel.empty()
                    ^^^^^^^
  ```

- Warning: `subworkflows/nf-core/fastq_taxonomic_profile_metaphlan/main.nf:20:128`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
      metaphlan_merged_profiles_txt = METAPHLAN_MERGEMETAPHLANTABLES(METAPHLAN_METAPHLAN.out.profile.map { [[id: 'all_samples'], it[1]] }.groupTuple(sort: { it.getName() })).txt
                                                                                                                                 ^^
  ```

- Warning: `subworkflows/nf-core/fastq_taxonomic_profile_metaphlan/main.nf:20:156`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
      metaphlan_merged_profiles_txt = METAPHLAN_MERGEMETAPHLANTABLES(METAPHLAN_METAPHLAN.out.profile.map { [[id: 'all_samples'], it[1]] }.groupTuple(sort: { it.getName() })).txt
                                                                                                                                                             ^^
  ```
