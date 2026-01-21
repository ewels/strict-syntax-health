# Nextflow lint results

- Generated: 2026-01-21T13:35:35.504755+00:00
- Nextflow version: 25.12.0-edge
- Summary: 8 warnings

## :warning: Warnings

- Warning: `subworkflows/nf-core/bam_methyldackel/main.nf:13:40`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_methydackel_extract_bedgraph  = Channel.empty()
                                         ^^^^^^^^^^
  ```

- Warning: `subworkflows/nf-core/bam_methyldackel/main.nf:14:40`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_methydackel_extract_methylkit = Channel.empty()
                                         ^^^^^^^^^^
  ```

- Warning: `subworkflows/nf-core/bam_methyldackel/main.nf:15:40`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_methydackel_mbias             = Channel.empty()
                                         ^^^^^^^^^^
  ```

- Warning: `subworkflows/nf-core/bam_methyldackel/main.nf:16:40`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_multiqc_files                 = Channel.empty()
                                         ^^^^^^^^^^
  ```

- Warning: `subworkflows/nf-core/bam_methyldackel/main.nf:17:40`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_versions                      = Channel.empty()
                                         ^^^^^^^^^^
  ```

- Warning: `subworkflows/nf-core/bam_methyldackel/main.nf:45:65`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
      ch_multiqc_files = ch_methydackel_extract_bedgraph.collect{ meta, bedgraph -> bedgraph  }
                                                                  ^^^^^^^^^^
  ```

- Warning: `subworkflows/nf-core/bam_methyldackel/main.nf:46:72`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
                          .mix(ch_methydackel_extract_methylkit.collect{ meta, methylkit -> methylkit })
                                                                         ^^^^^^^^^^
  ```

- Warning: `subworkflows/nf-core/bam_methyldackel/main.nf:47:60`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
                          .mix(ch_methydackel_mbias.collect{ meta, txt -> txt  })
                                                             ^^^^^^^^^^
  ```
