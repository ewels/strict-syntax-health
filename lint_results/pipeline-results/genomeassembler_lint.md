# Nextflow lint results

- Generated: 2026-09-02T00:20:26.412564242Z
- Nextflow version: 26.08.0-edge
- Summary: 7 warnings

## :warning: Warnings

- Warning: `modules/local/dorado/aligner/main.nf:36:9`: Variable was declared but not used

  ```nextflow
      def args   = task.ext.args ?: ''
          ^^^^
  ```

- Warning: `modules/local/dorado/polish/main.nf:34:9`: Variable was declared but not used

  ```nextflow
      def args   = task.ext.args ?: ''
          ^^^^
  ```

- Warning: `modules/nf-core/merqury/merqury/main.nf:59:9`: Variable was declared but not used

  ```nextflow
      def VERSION = 1.3 // WARN: Version information not provided by tool on CLI. Please update this string when bumping container versions.
          ^^^^^^^
  ```

- Warning: `modules/nf-core/meryl/unionsum/main.nf:35:9`: Variable was declared but not used

  ```nextflow
      def args = task.ext.args ?: ''
          ^^^^
  ```

- Warning: `subworkflows/local/prepare/main.nf:233:5`: Variable was declared but not used

  ```nextflow
      genomescope_summary = JELLYFISH.out.genomescope_summary
      ^^^^^^^^^^^^^^^^^^^
  ```

- Warning: `subworkflows/local/prepare/main.nf:235:5`: Variable was declared but not used

  ```nextflow
      genomescope_plot = JELLYFISH.out.genomescope_plot
      ^^^^^^^^^^^^^^^^
  ```

- Warning: `subworkflows/local/utils_nfcore_genomeassembler_pipeline/main.nf:33:5`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
      input             //  string: Path to input samplesheet
      ^^^^^
  ```
