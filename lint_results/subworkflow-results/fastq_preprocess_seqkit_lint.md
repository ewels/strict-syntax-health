# Nextflow lint results

- Generated: 2026-01-24T00:20:36.578823+00:00
- Nextflow version: 25.12.0-edge
- Summary: 2 warnings

## :warning: Warnings

- Warning: `subworkflows/nf-core/fastq_preprocess_seqkit/main.nf:64:50`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
              def clean_meta = meta.findAll { key, value -> key != 'strandness' }
                                                   ^^^^^^^^^^
  ```

- Warning: `subworkflows/nf-core/fastq_preprocess_seqkit/main.nf:72:59`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
                  def sorted_files = files.flatten().sort { it.name }
                                                            ^^^^^^^^^
  ```
