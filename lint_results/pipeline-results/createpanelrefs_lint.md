# Nextflow lint results

- Generated: 2026-01-16T10:18:38.629147475Z
- Nextflow version: 25.12.0-edge
- Summary: 15 warnings

## :warning: Warnings

- Warning: `modules/nf-core/gatk4/annotateintervals/main.nf:31:53`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
      def inputs = intervals.collect { "--intervals ${it}" }.join(" ")
                                                      ^^
  ```

- Warning: `modules/nf-core/gatk4/createreadcountpanelofnormals/main.nf:23:50`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
      def input_list = counts.collect { "--input ${it}" }.join(" ")
                                                   ^^
  ```

- Warning: `modules/nf-core/gatk4/determinegermlinecontigploidy/main.nf:27:80`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
      def exclude = exclude_beds ? exclude_beds.collect { "--exclude-intervals ${it}" }.join(" ") : ""
                                                                                 ^^
  ```

- Warning: `modules/nf-core/gatk4/determinegermlinecontigploidy/main.nf:30:50`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
      def input_list = counts.collect { "--input ${it}" }.join(" ")
                                                   ^^
  ```

- Warning: `modules/nf-core/gatk4/filterintervals/main.nf:26:78`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
      def read_counts_command = read_counts ? read_counts.collect { "--input ${it}" }.join(" ") : ""
                                                                               ^^
  ```

- Warning: `modules/nf-core/gatk4/germlinecnvcaller/main.nf:28:47`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
      def input_list = tsv.collect { "--input ${it}" }.join(' ')
                                                ^^
  ```

- Warning: `modules/nf-core/gawk/main.nf:26:54`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
      suffix    = task.ext.suffix ?: "${input.collect{ it.getExtension()}.get(0)}" // use the first extension of the input files
                                                       ^^
  ```

- Warning: `modules/nf-core/gawk/main.nf:29:37`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
      lst_gz     = input.findResults{ it.getExtension().endsWith("gz") ? it.toString() : null }
                                      ^^
  ```

- Warning: `modules/nf-core/gawk/main.nf:29:72`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
      lst_gz     = input.findResults{ it.getExtension().endsWith("gz") ? it.toString() : null }
                                                                         ^^
  ```

- Warning: `modules/nf-core/gawk/main.nf:31:34`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
      input_cmd  = input.collect { it.toString() - ~/\.gz$/ }.join(" ")
                                   ^^
  ```

- Warning: `modules/nf-core/gawk/main.nf:34:49`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
      cleanup    = lst_gz ? "rm ${lst_gz.collect{ it - ~/\.gz$/ }.join(" ")}" : ""
                                                  ^^
  ```

- Warning: `modules/nf-core/gawk/main.nf:37:16`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          assert it.name != "${prefix}.${suffix}" : "Input and output names are the same, set prefix in module configuration to disambiguate!"
                 ^^
  ```

- Warning: `subworkflows/local/gens_pon/main.nf:45:20`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          .collect { it[1] }
                     ^^
  ```

- Warning: `subworkflows/local/germlinecnvcaller_cohort/main.nf:124:20`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          .collect { it[1] }
                     ^^
  ```

- Warning: `subworkflows/local/utils_nfcore_createpanelrefs_pipeline/main.nf:31:5`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
      monochrome_logs // boolean: Do not use coloured log outputs
      ^^^^^^^^^^^^^^^
  ```
