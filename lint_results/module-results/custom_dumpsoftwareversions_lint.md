# Nextflow lint results

- Generated: 2026-01-16T02:02:17.553758+00:00
- Nextflow version: 25.12.0-edge
- Summary: 2 errors, 2 warnings

## :x: Errors

- Error: `modules/nf-core/custom/dumpsoftwareversions/main.nf:1:1`: Statements cannot be mixed with script declarations -- move statements into a process, workflow, or function

  ```nextflow
  def deprecation_message = """
  ^^^^^^^^^^
  ```

- Error: `modules/nf-core/custom/dumpsoftwareversions/main.nf:30:18`: `deprecation_message` is not defined

  ```nextflow
      assert true: deprecation_message
                   ^^^^^^^^^^
  ```

## :warning: Warnings

- Warning: `modules/nf-core/custom/dumpsoftwareversions/main.nf:1:5`: Variable was declared but not used

  ```nextflow
  def deprecation_message = """
      ^^^^^^^^^^
  ```

- Warning: `modules/nf-core/custom/dumpsoftwareversions/main.nf:31:9`: Variable was declared but not used

  ```nextflow
      def args = task.ext.args ?: ''
          ^^^^^^^^^^
  ```
