# Nextflow lint results

- Generated: 2026-01-16T02:02:17.572228+00:00
- Nextflow version: 25.12.0-edge
- Summary: 2 warnings

## :warning: Warnings

- Warning: `modules/nf-core/gatk4/postprocessgermlinecnvcalls/main.nf:25:71`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
      def calls_command = calls ? calls.collect { "--calls-shard-path ${it}" }.join(' ') : ""
                                                                        ^^^^^^^^^^
  ```

- Warning: `modules/nf-core/gatk4/postprocessgermlinecnvcalls/main.nf:26:71`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
      def model_command = model ? model.collect { "--model-shard-path ${it}" }.join(' ') : ""
                                                                        ^^^^^^^^^^
  ```
