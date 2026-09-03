# Nextflow lint results

- Generated: 2026-09-03T00:26:07.548690707Z
- Nextflow version: 26.08.0-edge
- Summary: 1 warning

## :warning: Warnings

- Warning: `workflows/phyloplace.nf:34:38`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
      text.readLines().collect { pad + it }.join('\n')
                                       ^^
  ```
