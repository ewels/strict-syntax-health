# Nextflow lint results

- Generated: 2026-01-16T02:02:17.533568+00:00
- Nextflow version: 25.12.0-edge
- Summary: 2 warnings

## :warning: Warnings

- Warning: `modules/nf-core/bedtools/unionbedg/main.nf:25:29`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
      bedgraph.collect { if ("$it" == "${prefix}.bed") error "$it has the same name as the output, use \"task.ext.prefix\" to disambiguate!" }
                              ^^^^^^^^^^
  ```

- Warning: `modules/nf-core/bedtools/unionbedg/main.nf:25:61`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
      bedgraph.collect { if ("$it" == "${prefix}.bed") error "$it has the same name as the output, use \"task.ext.prefix\" to disambiguate!" }
                                                              ^^^^^^^^^^
  ```
