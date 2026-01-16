# Nextflow lint results

- Generated: 2026-01-16T10:27:19.185568559Z
- Nextflow version: 25.12.0-edge
- Summary: 31 warnings

## :warning: Warnings

- Warning: `modules/nf-core/gunzip/main.nf:43:9`: Variable was declared but not used

  ```nextflow
      def args = task.ext.args ?: ''
          ^^^^
  ```

- Warning: `modules/nf-core/unzip/main.nf:38:9`: Variable was declared but not used

  ```nextflow
      def args = task.ext.args ?: ''
          ^^^^
  ```

- Warning: `modules/nf-side/gawk/main.nf:29:52`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
      suffix = task.ext.suffix ?: "${input.collect { it.getExtension() }.get(0)}"
                                                     ^^
  ```

- Warning: `modules/nf-side/gawk/main.nf:32:34`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
      lst_gz = input.findResults { it.getExtension().endsWith("gz") ? it.toString() : null }
                                   ^^
  ```

- Warning: `modules/nf-side/gawk/main.nf:32:69`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
      lst_gz = input.findResults { it.getExtension().endsWith("gz") ? it.toString() : null }
                                                                      ^^
  ```

- Warning: `modules/nf-side/gawk/main.nf:34:33`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
      input_cmd = input.collect { it.toString() - ~/\.gz$/ }.join(" ")
                                  ^^
  ```

- Warning: `modules/nf-side/gawk/main.nf:37:47`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
      cleanup = lst_gz ? "rm ${lst_gz.collect { it - ~/\.gz$/ }.join(" ")}" : ""
                                                ^^
  ```

- Warning: `modules/nf-side/gawk/main.nf:40:16`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          assert it.name != "${prefix}.${suffix}" : "Input and output names are the same, set prefix in module configuration to disambiguate!"
                 ^^
  ```

- Warning: `modules/nf-side/gffread/main.nf:25:91`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
      def extension = args.contains("-T") ? 'gtf' : (['-w', '-x', '-y'].any { args.contains(it) } ? 'fasta' : 'gff3')
                                                                                            ^^
  ```

- Warning: `modules/nf-side/gffread/main.nf:45:91`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
      def extension = args.contains("-T") ? 'gtf' : (['-w', '-x', '-y'].any { args.contains(it) } ? 'fasta' : 'gff3')
                                                                                            ^^
  ```

- Warning: `modules/nf-side/rsem/preparereference/main.nf:27:30`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          args_list.removeIf { it.contains('--star') }
                               ^^
  ```

- Warning: `subworkflows/nf-core/archive_extract/main.nf:10:16`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      versions = Channel.empty()
                 ^^^^^^^
  ```

- Warning: `subworkflows/nf-core/archive_extract/main.nf:28:17`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      extracted = Channel
                  ^^^^^^^
  ```

- Warning: `subworkflows/nf-side/prepare_genome_dnaseq/main.nf:29:21`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      bwamem1_index = Channel.empty()
                      ^^^^^^^
  ```

- Warning: `subworkflows/nf-side/prepare_genome_dnaseq/main.nf:30:21`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      bwamem2_index = Channel.empty()
                      ^^^^^^^
  ```

- Warning: `subworkflows/nf-side/prepare_genome_dnaseq/main.nf:31:23`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      dragmap_hashmap = Channel.empty()
                        ^^^^^^^
  ```

- Warning: `subworkflows/nf-side/prepare_genome_dnaseq/main.nf:32:18`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      fasta_dict = Channel.empty()
                   ^^^^^^^
  ```

- Warning: `subworkflows/nf-side/prepare_genome_dnaseq/main.nf:33:21`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      intervals_bed = Channel.empty()
                      ^^^^^^^
  ```

- Warning: `subworkflows/nf-side/prepare_genome_dnaseq/main.nf:34:25`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      msisensorpro_list = Channel.empty()
                          ^^^^^^^
  ```

- Warning: `subworkflows/nf-side/prepare_genome_dnaseq/main.nf:35:14`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      vcf_gz = Channel.empty()
               ^^^^^^^
  ```

- Warning: `subworkflows/nf-side/prepare_genome_dnaseq/main.nf:36:15`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      vcf_tbi = Channel.empty()
                ^^^^^^^
  ```

- Warning: `subworkflows/nf-side/prepare_genome_dnaseq/main.nf:37:25`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      snapaligner_index = Channel.empty()
                          ^^^^^^^
  ```

- Warning: `subworkflows/nf-side/prepare_genome_rnaseq/main.nf:34:21`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      bowtie1_index = Channel.empty()
                      ^^^^^^^
  ```

- Warning: `subworkflows/nf-side/prepare_genome_rnaseq/main.nf:35:21`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      bowtie2_index = Channel.empty()
                      ^^^^^^^
  ```

- Warning: `subworkflows/nf-side/prepare_genome_rnaseq/main.nf:36:20`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      hisat2_index = Channel.empty()
                     ^^^^^^^
  ```

- Warning: `subworkflows/nf-side/prepare_genome_rnaseq/main.nf:37:22`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      kallisto_index = Channel.empty()
                       ^^^^^^^
  ```

- Warning: `subworkflows/nf-side/prepare_genome_rnaseq/main.nf:38:18`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      rsem_index = Channel.empty()
                   ^^^^^^^
  ```

- Warning: `subworkflows/nf-side/prepare_genome_rnaseq/main.nf:39:20`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      salmon_index = Channel.empty()
                     ^^^^^^^
  ```

- Warning: `subworkflows/nf-side/prepare_genome_rnaseq/main.nf:40:18`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      star_index = Channel.empty()
                   ^^^^^^^
  ```

- Warning: `subworkflows/nf-side/prepare_genome_rnaseq/main.nf:41:19`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      fasta_sizes = Channel.empty()
                    ^^^^^^^
  ```

- Warning: `subworkflows/nf-side/utils_references/main.nf:20:18`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      references = Channel.fromList(
                   ^^^^^^^
  ```
