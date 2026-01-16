# Nextflow lint results

- Generated: 2026-01-16T02:02:17.527102+00:00
- Nextflow version: 25.12.0-edge
- Summary: 2 errors, 1 warning

## :x: Errors

- Error: `modules/nf-core/bam2fastx/bam2fastq/main.nf:1:1`: Statements cannot be mixed with script declarations -- move statements into a process, workflow, or function

  ```nextflow
  def deprecation_message = """
  ^^^^^^^^^^
  ```

- Error: `modules/nf-core/bam2fastx/bam2fastq/main.nf:30:18`: `deprecation_message` is not defined

  ```nextflow
      assert true: deprecation_message
                   ^^^^^^^^^^
  ```

## :warning: Warnings

- Warning: `modules/nf-core/bam2fastx/bam2fastq/main.nf:1:5`: Variable was declared but not used

  ```nextflow
  def deprecation_message = """
      ^^^^^^^^^^
  ```
