# Nextflow lint results

- Generated: 2026-01-16T10:26:16.559083008Z
- Nextflow version: 25.12.0-edge
- Summary: 10 errors, 19 warnings

## :x: Errors

- Error: `modules/nf-core/mafft/align/main.nf:29:9`: `add` is already declared

  ```nextflow
      def add          = add             ? "--add <(unpigz -cdf ${add})"                   : ''
          ^^^
  ```

- Error: `modules/nf-core/mafft/align/main.nf:30:9`: `addfragments` is already declared

  ```nextflow
      def addfragments = addfragments    ? "--addfragments <(unpigz -cdf ${addfragments})" : ''
          ^^^^^^^^^^^^
  ```

- Error: `modules/nf-core/mafft/align/main.nf:31:9`: `addfull` is already declared

  ```nextflow
      def addfull      = addfull         ? "--addfull <(unpigz -cdf ${addfull})"           : ''
          ^^^^^^^
  ```

- Error: `modules/nf-core/mafft/align/main.nf:32:9`: `addprofile` is already declared

  ```nextflow
      def addprofile   = addprofile      ? "--addprofile <(unpigz -cdf ${addprofile})"     : ''
          ^^^^^^^^^^
  ```

- Error: `modules/nf-core/mafft/align/main.nf:33:9`: `addlong` is already declared

  ```nextflow
      def addlong      = addlong         ? "--addlong <(unpigz -cdf ${addlong})"           : ''
          ^^^^^^^
  ```

- Error: `modules/nf-core/mafft/align/main.nf:59:9`: `add` is already declared

  ```nextflow
      def add          = add             ? "--add ${add}"                   : ''
          ^^^
  ```

- Error: `modules/nf-core/mafft/align/main.nf:60:9`: `addfragments` is already declared

  ```nextflow
      def addfragments = addfragments    ? "--addfragments ${addfragments}" : ''
          ^^^^^^^^^^^^
  ```

- Error: `modules/nf-core/mafft/align/main.nf:61:9`: `addfull` is already declared

  ```nextflow
      def addfull      = addfull         ? "--addfull ${addfull}"           : ''
          ^^^^^^^
  ```

- Error: `modules/nf-core/mafft/align/main.nf:62:9`: `addprofile` is already declared

  ```nextflow
      def addprofile   = addprofile      ? "--addprofile ${addprofile}"     : ''
          ^^^^^^^^^^
  ```

- Error: `modules/nf-core/mafft/align/main.nf:63:9`: `addlong` is already declared

  ```nextflow
      def addlong      = addlong         ? "--addlong ${addlong}"           : ''
          ^^^^^^^
  ```

## :warning: Warnings

- Warning: `modules/nf-core/hhsuite/reformat/main.nf:48:9`: Variable was declared but not used

  ```nextflow
      def args = task.ext.args ?: ''
          ^^^^
  ```

- Warning: `modules/nf-core/mafft/align/main.nf:57:9`: Variable was declared but not used

  ```nextflow
      def args         = task.ext.args   ?: ''
          ^^^^
  ```

- Warning: `modules/nf-core/mafft/align/main.nf:59:9`: Variable was declared but not used

  ```nextflow
      def add          = add             ? "--add ${add}"                   : ''
          ^^^
  ```

- Warning: `modules/nf-core/mafft/align/main.nf:60:9`: Variable was declared but not used

  ```nextflow
      def addfragments = addfragments    ? "--addfragments ${addfragments}" : ''
          ^^^^^^^^^^^^
  ```

- Warning: `modules/nf-core/mafft/align/main.nf:61:9`: Variable was declared but not used

  ```nextflow
      def addfull      = addfull         ? "--addfull ${addfull}"           : ''
          ^^^^^^^
  ```

- Warning: `modules/nf-core/mafft/align/main.nf:62:9`: Variable was declared but not used

  ```nextflow
      def addprofile   = addprofile      ? "--addprofile ${addprofile}"     : ''
          ^^^^^^^^^^
  ```

- Warning: `modules/nf-core/mafft/align/main.nf:63:9`: Variable was declared but not used

  ```nextflow
      def addlong      = addlong         ? "--addlong ${addlong}"           : ''
          ^^^^^^^
  ```

- Warning: `subworkflows/local/generate_families/main.nf:48:16`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          .map { id, meta, hmm, seqs -> [ meta, hmm, seqs, false, hmmsearch_write_target, hmmsearch_write_domain ] }
                 ^^
  ```

- Warning: `subworkflows/local/generate_families/main.nf:58:20`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
              .map { id, meta, domtbl, seqs -> [ meta, domtbl, seqs ] }
                     ^^
  ```

- Warning: `subworkflows/local/utils_nfcore_proteinfamilies_pipeline/main.nf:32:5`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
      monochrome_logs   // boolean: Do not use coloured log outputs
      ^^^^^^^^^^^^^^^
  ```

- Warning: `subworkflows/local/utils_nfcore_proteinfamilies_pipeline/main.nf:35:5`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
      input             //  string: Path to input samplesheet
      ^^^^^
  ```

- Warning: `subworkflows/local/utils_nfcore_proteinfamilies_pipeline/main.nf:291:16`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          .map { meta, folder1, folder2 ->
                 ^^^^
  ```

- Warning: `subworkflows/local/utils_nfcore_proteinfamilies_pipeline/main.nf:301:47`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
              def baseNames1 = files1.collect { it.getSimpleName() }.sort()
                                                ^^
  ```

- Warning: `subworkflows/local/utils_nfcore_proteinfamilies_pipeline/main.nf:302:47`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
              def baseNames2 = files2.collect { it.getSimpleName() }.sort()
                                                ^^
  ```

- Warning: `subworkflows/nf-core/faa_seqfu_seqkit/main.nf:15:24`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_multiqc_files = Channel.empty()
                         ^^^^^^^
  ```

- Warning: `subworkflows/nf-core/faa_seqfu_seqkit/main.nf:16:24`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_versions      = Channel.empty()
                         ^^^^^^^
  ```

- Warning: `workflows/proteinfamilies.nf:231:88`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
      ch_multiqc_files = ch_multiqc_files.mix(FAA_SEQFU_SEQKIT.out.multiqc_files.collect{it[1]}.ifEmpty([]))
                                                                                         ^^
  ```

- Warning: `workflows/proteinfamilies.nf:232:92`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
      ch_multiqc_files = ch_multiqc_files.mix(CALCULATE_CLUSTER_DISTRIBUTION.out.mqc.collect{it[1]}.ifEmpty([]))
                                                                                             ^^
  ```

- Warning: `workflows/proteinfamilies.nf:233:70`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
      ch_multiqc_files = ch_multiqc_files.mix(ch_family_reps.collect { it[1] }.ifEmpty([]))
                                                                       ^^
  ```
