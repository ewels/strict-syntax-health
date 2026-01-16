# Nextflow lint results

- Generated: 2026-01-16T02:02:17.577540+00:00
- Nextflow version: 25.12.0-edge
- Summary: 3 warnings

## :warning: Warnings

- Warning: `modules/nf-core/goleft/indexcov/main.nf:31:38`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
      def input_files = bams.findAll { it.name.endsWith(".bam") } + indexes.findAll { it.name.endsWith(".crai") }
                                       ^^^^^^^^^^
  ```

- Warning: `modules/nf-core/goleft/indexcov/main.nf:31:85`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
      def input_files = bams.findAll { it.name.endsWith(".bam") } + indexes.findAll { it.name.endsWith(".crai") }
                                                                                      ^^^^^^^^^^
  ```

- Warning: `modules/nf-core/goleft/indexcov/main.nf:32:44`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
      def extranormalize = input_files.any { it.name.endsWith(".crai") } ? " --extranormalize " : ""
                                             ^^^^^^^^^^
  ```
