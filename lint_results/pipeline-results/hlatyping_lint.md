# Nextflow lint results

- Generated: 2026-09-02T00:21:13.593793977Z
- Nextflow version: 26.08.0-edge
- Summary: 4 warnings

## :warning: Warnings

- Warning: `subworkflows/local/utils_nfcore_hlatyping_pipeline/main.nf:32:5`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
      input //  string: Path to input samplesheet
      ^^^^^
  ```

- Warning: `subworkflows/local/utils_nfcore_hlatyping_pipeline/main.nf:369:92`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
      def actual = file.withInputStream { org.apache.commons.codec.digest.DigestUtils.md5Hex(it) }
                                                                                             ^^
  ```

- Warning: `workflows/hlatyping.nf:206:87`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
                  [meta.id, 'spechla', (files instanceof List ? files : [files]).find { it.name == 'hla.result.txt' }]
                                                                                        ^^
  ```

- Warning: `workflows/hlatyping.nf:290:85`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
                  [meta.id, 'hlala', (files instanceof List ? files : [files]).find { it.name == 'R1_bestguess_G.txt' }]
                                                                                      ^^
  ```
