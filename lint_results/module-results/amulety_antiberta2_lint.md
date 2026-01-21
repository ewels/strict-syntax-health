# Nextflow lint results

- Generated: 2026-01-21T13:35:22.706547+00:00
- Nextflow version: 25.12.0-edge
- Summary: 3 errors, 1 warning

## :x: Errors

- Error: `modules/nf-core/amulety/antiberta2/main.nf:1:1`: Statements cannot be mixed with script declarations -- move statements into a process, workflow, or function

  ```nextflow
  def deprecation_message = """
  ^^^^^^^^^^
  ```

- Error: `modules/nf-core/amulety/antiberta2/main.nf:32:19`: `deprecation_message` is not defined

  ```nextflow
      assert false: deprecation_message
                    ^^^^^^^^^^
  ```

- Error: `modules/nf-core/amulety/antiberta2/main.nf:35:19`: `deprecation_message` is not defined

  ```nextflow
      assert false: deprecation_message
                    ^^^^^^^^^^
  ```

## :warning: Warnings

- Warning: `modules/nf-core/amulety/antiberta2/main.nf:1:5`: Variable was declared but not used

  ```nextflow
  def deprecation_message = """
      ^^^^^^^^^^
  ```
