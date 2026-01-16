# Nextflow lint results

- Generated: 2026-01-16T02:02:17.584776+00:00
- Nextflow version: 25.12.0-edge
- Summary: 2 warnings

## :warning: Warnings

- Warning: `modules/nf-core/hostile/clean/main.nf:25:75`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
      def sorted_reads = meta.single_end ? [reads].flatten() : reads.sort { it.simpleName }
                                                                            ^^^^^^^^^^
  ```

- Warning: `modules/nf-core/hostile/clean/main.nf:52:75`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
      def sorted_reads = meta.single_end ? [reads].flatten() : reads.sort { it.simpleName }
                                                                            ^^^^^^^^^^
  ```
