# Nextflow lint results

- Generated: 2026-09-10T00:17:47.947940585Z
- Nextflow version: 26.08.0-edge
- Summary: 13 warnings

## :warning: Warnings

- Warning: `main.nf:44:54`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      abo_reference_fai   = params.abo_reference_fai ? Channel.fromPath(params.abo_reference_fai)
                                                       ^^^^^^^
  ```

- Warning: `main.nf:45:50`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
          .map { it -> [[id: it.baseName], it] } : Channel.empty()
                                                   ^^^^^^^
  ```

- Warning: `main.nf:46:56`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      abo_reference_fasta = params.abo_reference_fasta ? Channel.fromPath(params.abo_reference_fasta)
                                                         ^^^^^^^
  ```

- Warning: `main.nf:47:50`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
          .map { it -> [[id: it.baseName], it] } : Channel.empty()
                                                   ^^^^^^^
  ```

- Warning: `main.nf:48:26`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      logo = params.logo ? Channel.fromPath(params.logo).collect() : Channel.empty()
                           ^^^^^^^
  ```

- Warning: `main.nf:48:68`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      logo = params.logo ? Channel.fromPath(params.logo).collect() : Channel.empty()
                                                                     ^^^^^^^
  ```

- Warning: `subworkflows/local/minimap_align_exons/main.nf:29:16`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          .map { meta_fa, fa, meta_fai, fai -> [ [id: 'ABO_REF'], fa, fai ] }
                 ^^^^^^^
  ```

- Warning: `subworkflows/local/minimap_align_exons/main.nf:29:29`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          .map { meta_fa, fa, meta_fai, fai -> [ [id: 'ABO_REF'], fa, fai ] }
                              ^^^^^^^^
  ```

- Warning: `subworkflows/local/predictabophenotype/main.nf:51:17`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
                  it.file.copyTo(combined_dir.resolve(it.file.name))
                  ^^
  ```

- Warning: `subworkflows/local/predictabophenotype/main.nf:51:53`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
                  it.file.copyTo(combined_dir.resolve(it.file.name))
                                                      ^^
  ```

- Warning: `subworkflows/local/variant_calling_haploscan/main.nf:29:35`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          .map { fasta_meta, fasta, fai_meta, fai -> [fasta_meta, fasta, fai] }
                                    ^^^^^^^^
  ```

- Warning: `workflows/abotyper.nf:34:5`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
      logo // channel: png from params.logo (custom pathwest logo)
      ^^^^
  ```

- Warning: `workflows/abotyper.nf:88:26`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      def topic_versions = Channel.topic("versions")
                           ^^^^^^^
  ```
