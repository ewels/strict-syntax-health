# Nextflow lint results

- Generated: 2026-08-27T01:26:36.615230159Z
- Nextflow version: 26.08.0-edge
- Summary: 2 warnings

## :warning: Warnings

- Warning: `workflows/provenancereport.nf:80:16`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          .map { meta, input_file -> input_file }
                 ^^^^
  ```

- Warning: `workflows/provenancereport.nf:81:44`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          .mix(QUARTONOTEBOOK.out.html.map { meta, report_file -> report_file })
                                             ^^^^
  ```
