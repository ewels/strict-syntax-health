# Nextflow lint results

- Generated: 2026-01-24T00:20:36.579394+00:00
- Nextflow version: 25.12.0-edge
- Summary: 4 errors, 3 warnings

## :x: Errors

- Error: `subworkflows/nf-core/fastq_taxonomic_profile_metaphlan/main.nf:1:1`: Included name 'METAPHLAN_MAKEDB' is not defined in module '/home/runner/work/strict-syntax-health/strict-syntax-health/modules/modules/nf-core/metaphlan/makedb/main.nf'

  ```nextflow
  include { METAPHLAN_MAKEDB               } from '../../../modules/nf-core/metaphlan/makedb/main'
  ^^^^^^^^^^
  ```

- Error: `subworkflows/nf-core/fastq_taxonomic_profile_metaphlan/main.nf:14:5`: `METAPHLAN_MAKEDB` is not defined

  ```nextflow
      METAPHLAN_MAKEDB()
      ^^^^^^^^^^
  ```

- Error: `subworkflows/nf-core/fastq_taxonomic_profile_metaphlan/main.nf:15:35`: `METAPHLAN_MAKEDB` is not defined

  ```nextflow
      ch_versions = ch_versions.mix(METAPHLAN_MAKEDB.out.versions.first())
                                    ^^^^^^^^^^
  ```

- Error: `subworkflows/nf-core/fastq_taxonomic_profile_metaphlan/main.nf:17:35`: `METAPHLAN_MAKEDB` is not defined

  ```nextflow
      METAPHLAN_METAPHLAN(ch_fastq, METAPHLAN_MAKEDB.out.db, false)
                                    ^^^^^^^^^^
  ```

## :warning: Warnings

- Warning: `subworkflows/nf-core/fastq_taxonomic_profile_metaphlan/main.nf:12:19`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_versions = Channel.empty()
                    ^^^^^^^^^^
  ```

- Warning: `subworkflows/nf-core/fastq_taxonomic_profile_metaphlan/main.nf:20:128`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
      metaphlan_merged_profiles_txt = METAPHLAN_MERGEMETAPHLANTABLES(METAPHLAN_METAPHLAN.out.profile.map { [[id: 'all_samples'], it[1]] }.groupTuple(sort: { it.getName() })).txt
                                                                                                                                 ^^^^^^^^^^
  ```

- Warning: `subworkflows/nf-core/fastq_taxonomic_profile_metaphlan/main.nf:20:156`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
      metaphlan_merged_profiles_txt = METAPHLAN_MERGEMETAPHLANTABLES(METAPHLAN_METAPHLAN.out.profile.map { [[id: 'all_samples'], it[1]] }.groupTuple(sort: { it.getName() })).txt
                                                                                                                                                             ^^^^^^^^^^
  ```
