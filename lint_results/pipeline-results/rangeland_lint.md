# Nextflow lint results

- Generated: 2026-08-27T01:26:50.974040269Z
- Nextflow version: 26.08.0-edge
- Summary: 1 warning

## :warning: Warnings

- Warning: `workflows/rangeland.nf:166:5`: Variable was declared but not used

  ```nextflow
      grouped_trend_data = HIGHER_LEVEL.out.mosaic.map{ it -> it[1] }.flatten().buffer( size: Integer.MAX_VALUE, remainder: true )
      ^^^^^^^^^^^^^^^^^^
  ```
