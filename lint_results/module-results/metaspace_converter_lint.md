# Nextflow lint results

- Generated: 2026-01-16T02:02:17.602958+00:00
- Nextflow version: 25.12.0-edge
- Summary: 5 warnings

## :warning: Warnings

- Warning: `modules/nf-core/metaspace/converter/main.nf:21:5`: Variable was declared but not used

  ```nextflow
      database_name    = task.ext.database_name ?: "HMDB"
      ^^^^^^^^^^
  ```

- Warning: `modules/nf-core/metaspace/converter/main.nf:22:5`: Variable was declared but not used

  ```nextflow
      database_version = task.ext.database_version ?: "v4"
      ^^^^^^^^^^
  ```

- Warning: `modules/nf-core/metaspace/converter/main.nf:23:5`: Variable was declared but not used

  ```nextflow
      fdr              = task.ext.fdr ?: "0.1"
      ^^^^^^^^^^
  ```

- Warning: `modules/nf-core/metaspace/converter/main.nf:24:5`: Variable was declared but not used

  ```nextflow
      use_tic          = task.ext.use_tic ?: "true"
      ^^^^^^^^^^
  ```

- Warning: `modules/nf-core/metaspace/converter/main.nf:25:5`: Variable was declared but not used

  ```nextflow
      metadata_as_obs  = task.ext.metadata_as_obs ?: "false"
      ^^^^^^^^^^
  ```
