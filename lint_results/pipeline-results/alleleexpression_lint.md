# Nextflow lint results

- Generated: 2026-01-16T06:28:10.972383354Z
- Nextflow version: 25.12.0-edge
- Summary: 20 warnings

## :warning: Warnings

- Warning: `modules/local/star_align_wasp/main.nf:47:56`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
      meta.single_end ? [reads].flatten().each{reads1 << it} : reads.eachWithIndex{ v, ix -> ( ix & 1 ? reads2 : reads1) << v }
                                                         ^^
  ```

- Warning: `modules/local/star_align_wasp/main.nf:61:22`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
      if (reads1.any { it.toString().endsWith('.gz') } || reads2.any { it.toString().endsWith('.gz') }) {
                       ^^
  ```

- Warning: `modules/local/star_align_wasp/main.nf:61:70`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
      if (reads1.any { it.toString().endsWith('.gz') } || reads2.any { it.toString().endsWith('.gz') }) {
                                                                       ^^
  ```

- Warning: `modules/nf-core/bcftools/index/main.nf:23:9`: Variable was declared but not used

  ```nextflow
      def prefix = task.ext.prefix ?: "${meta.id}"
          ^^^^^^
  ```

- Warning: `modules/nf-core/bcftools/index/main.nf:40:9`: Variable was declared but not used

  ```nextflow
      def prefix = task.ext.prefix ?: "${meta.id}"
          ^^^^^^
  ```

- Warning: `modules/nf-core/star/align/main.nf:46:56`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
      meta.single_end ? [reads].flatten().each{reads1 << it} : reads.eachWithIndex{ v, ix -> ( ix & 1 ? reads2 : reads1) << v }
                                                         ^^
  ```

- Warning: `workflows/alleleexpression.nf:37:19`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_versions = Channel.empty()
                    ^^^^^^^
  ```

- Warning: `workflows/alleleexpression.nf:76:21`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_star_index = Channel.fromPath(params.star_index)
                      ^^^^^^^
  ```

- Warning: `workflows/alleleexpression.nf:78:14`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_gtf = Channel.fromPath(params.gtf)
               ^^^^^^^
  ```

- Warning: `workflows/alleleexpression.nf:110:9`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
          Channel.value([['id': 'dummy'], []])
          ^^^^^^^
  ```

- Warning: `workflows/alleleexpression.nf:144:9`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
          Channel.fromPath(params.beagle_ref).first() :
          ^^^^^^^
  ```

- Warning: `workflows/alleleexpression.nf:145:9`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
          Channel.empty()
          ^^^^^^^
  ```

- Warning: `workflows/alleleexpression.nf:147:9`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
          Channel.fromPath(params.beagle_map).first() :
          ^^^^^^^
  ```

- Warning: `workflows/alleleexpression.nf:148:9`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
          Channel.empty()
          ^^^^^^^
  ```

- Warning: `workflows/alleleexpression.nf:179:24`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_gene_features = Channel.fromPath(params.gene_features).first()
                         ^^^^^^^
  ```

- Warning: `workflows/alleleexpression.nf:195:24`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_multiqc_files = Channel.empty()
                         ^^^^^^^
  ```

- Warning: `workflows/alleleexpression.nf:196:37`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          .mix(FASTQC.out.zip.collect{it[1]})
                                      ^^
  ```

- Warning: `workflows/alleleexpression.nf:203:9`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
          Channel.empty(),  // multiqc_logo
          ^^^^^^^
  ```

- Warning: `workflows/alleleexpression.nf:204:9`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
          Channel.empty(),  // replace_names
          ^^^^^^^
  ```

- Warning: `workflows/alleleexpression.nf:205:9`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
          Channel.empty()   // sample_names
          ^^^^^^^
  ```
