# Nextflow lint results

- Generated: 2026-01-21T13:35:35.506926+00:00
- Nextflow version: 25.12.0-edge
- Summary: 6 warnings

## :warning: Warnings

- Warning: `subworkflows/nf-core/bam_tumor_normal_somatic_variant_calling_strelka/main.nf:14:19`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_versions = Channel.empty()
                    ^^^^^^^^^^
  ```

- Warning: `subworkflows/nf-core/bam_tumor_normal_somatic_variant_calling_strelka/main.nf:30:23`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          intervals:    it[0].num_intervals > 1
                        ^^^^^^^^^^
  ```

- Warning: `subworkflows/nf-core/bam_tumor_normal_somatic_variant_calling_strelka/main.nf:31:23`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          no_intervals: it[0].num_intervals <= 1
                        ^^^^^^^^^^
  ```

- Warning: `subworkflows/nf-core/bam_tumor_normal_somatic_variant_calling_strelka/main.nf:37:23`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          intervals:    it[0].num_intervals > 1
                        ^^^^^^^^^^
  ```

- Warning: `subworkflows/nf-core/bam_tumor_normal_somatic_variant_calling_strelka/main.nf:38:23`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          no_intervals: it[0].num_intervals <= 1
                        ^^^^^^^^^^
  ```

- Warning: `subworkflows/nf-core/bam_tumor_normal_somatic_variant_calling_strelka/main.nf:49:14`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_vcf = Channel.empty().mix(MERGE_STRELKA_INDELS.out.vcf, MERGE_STRELKA_SNVS.out.vcf, ch_vcf_indels.no_intervals, ch_vcf_snvs.no_intervals)
               ^^^^^^^^^^
  ```
