# Nextflow lint results

- Generated: 2026-01-16T02:02:17.554604+00:00
- Nextflow version: 25.12.0-edge
- Summary: 2 warnings

## :warning: Warnings

- Warning: `modules/nf-core/custom/sratoolsncbisettings/main.nf:20:5`: The `shell` block is deprecated, use `script` instead

  ```nextflow
      shell:
      ^^^^^^
  ```

- Warning: `modules/nf-core/custom/sratoolsncbisettings/main.nf:21:5`: Variable was declared but not used

  ```nextflow
      config = "/LIBS/GUID = \"${UUID.randomUUID().toString()}\"\\n/libs/cloud/report_instance_identity = \"true\"\\n"
      ^^^^^^^^^^
  ```
