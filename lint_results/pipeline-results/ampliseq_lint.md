# Nextflow lint results

- Generated: 2026-01-16T10:17:10.180198391Z
- Nextflow version: 25.12.0-edge
- Summary: 4 errors, 148 warnings

## :x: Errors

- Error: `conf/modules.config:147:81`: `max_len` is not defined

  ```nextflow
              params.pacbio ? "trimLeft = 0, minLen = ${params.min_len}, maxLen = $max_len, rm.phix = FALSE" :
                                                                                  ^^^^^^^^
  ```

- Error: `conf/modules.config:148:90`: `max_len` is not defined

  ```nextflow
                  params.iontorrent ? "trimLeft = 15, minLen = ${params.min_len}, maxLen = $max_len, rm.phix = TRUE" :
                                                                                           ^^^^^^^^
  ```

- Error: `conf/modules.config:149:94`: `max_len` is not defined

  ```nextflow
                  params.illumina_pe_its ? "trimLeft = 0, minLen = ${params.min_len}, maxLen = $max_len, rm.phix = TRUE" :
                                                                                               ^^^^^^^^
  ```

- Error: `conf/modules.config:150:69`: `max_len` is not defined

  ```nextflow
                  "trimLeft = 0, minLen = ${params.min_len}, maxLen = $max_len, rm.phix = TRUE"
                                                                      ^^^^^^^^
  ```

## :warning: Warnings

- Warning: `modules/local/barrnapsummary.nf:19:9`: Variable was declared but not used

  ```nextflow
      def args = task.ext.args ?: ''
          ^^^^
  ```

- Warning: `modules/local/qiime2_alphararefaction.nf:4:14`: The use of `projectDir` in a process is discouraged -- input files should be provided as process inputs

  ```nextflow
      conda "${projectDir}/modules/local/envs/qiime2-amplicon-2024.10-py310-linux-conda.yml"
               ^^^^^^^^^^
  ```

- Warning: `modules/local/qiime2_ancom_asv.nf:8:14`: The use of `projectDir` in a process is discouraged -- input files should be provided as process inputs

  ```nextflow
      conda "${projectDir}/modules/local/envs/qiime2-amplicon-2024.10-py310-linux-conda.yml"
               ^^^^^^^^^^
  ```

- Warning: `modules/local/qiime2_ancom_tax.nf:6:14`: The use of `projectDir` in a process is discouraged -- input files should be provided as process inputs

  ```nextflow
      conda "${projectDir}/modules/local/envs/qiime2-amplicon-2024.10-py310-linux-conda.yml"
               ^^^^^^^^^^
  ```

- Warning: `modules/local/qiime2_ancombc_asv.nf:8:14`: The use of `projectDir` in a process is discouraged -- input files should be provided as process inputs

  ```nextflow
      conda "${projectDir}/modules/local/envs/qiime2-amplicon-2024.10-py310-linux-conda.yml"
               ^^^^^^^^^^
  ```

- Warning: `modules/local/qiime2_ancombc_tax.nf:6:14`: The use of `projectDir` in a process is discouraged -- input files should be provided as process inputs

  ```nextflow
      conda "${projectDir}/modules/local/envs/qiime2-amplicon-2024.10-py310-linux-conda.yml"
               ^^^^^^^^^^
  ```

- Warning: `modules/local/qiime2_barplot.nf:4:14`: The use of `projectDir` in a process is discouraged -- input files should be provided as process inputs

  ```nextflow
      conda "${projectDir}/modules/local/envs/qiime2-amplicon-2024.10-py310-linux-conda.yml"
               ^^^^^^^^^^
  ```

- Warning: `modules/local/qiime2_classify.nf:5:14`: The use of `projectDir` in a process is discouraged -- input files should be provided as process inputs

  ```nextflow
      conda "${projectDir}/modules/local/envs/qiime2-amplicon-2024.10-py310-linux-conda.yml"
               ^^^^^^^^^^
  ```

- Warning: `modules/local/qiime2_diversity_adonis.nf:5:14`: The use of `projectDir` in a process is discouraged -- input files should be provided as process inputs

  ```nextflow
      conda "${projectDir}/modules/local/envs/qiime2-amplicon-2024.10-py310-linux-conda.yml"
               ^^^^^^^^^^
  ```

- Warning: `modules/local/qiime2_diversity_alpha.nf:5:14`: The use of `projectDir` in a process is discouraged -- input files should be provided as process inputs

  ```nextflow
      conda "${projectDir}/modules/local/envs/qiime2-amplicon-2024.10-py310-linux-conda.yml"
               ^^^^^^^^^^
  ```

- Warning: `modules/local/qiime2_diversity_beta.nf:5:14`: The use of `projectDir` in a process is discouraged -- input files should be provided as process inputs

  ```nextflow
      conda "${projectDir}/modules/local/envs/qiime2-amplicon-2024.10-py310-linux-conda.yml"
               ^^^^^^^^^^
  ```

- Warning: `modules/local/qiime2_diversity_betaord.nf:5:14`: The use of `projectDir` in a process is discouraged -- input files should be provided as process inputs

  ```nextflow
      conda "${projectDir}/modules/local/envs/qiime2-amplicon-2024.10-py310-linux-conda.yml"
               ^^^^^^^^^^
  ```

- Warning: `modules/local/qiime2_diversity_core.nf:4:14`: The use of `projectDir` in a process is discouraged -- input files should be provided as process inputs

  ```nextflow
      conda "${projectDir}/modules/local/envs/qiime2-amplicon-2024.10-py310-linux-conda.yml"
               ^^^^^^^^^^
  ```

- Warning: `modules/local/qiime2_export_absolute.nf:4:14`: The use of `projectDir` in a process is discouraged -- input files should be provided as process inputs

  ```nextflow
      conda "${projectDir}/modules/local/envs/qiime2-amplicon-2024.10-py310-linux-conda.yml"
               ^^^^^^^^^^
  ```

- Warning: `modules/local/qiime2_export_relasv.nf:4:14`: The use of `projectDir` in a process is discouraged -- input files should be provided as process inputs

  ```nextflow
      conda "${projectDir}/modules/local/envs/qiime2-amplicon-2024.10-py310-linux-conda.yml"
               ^^^^^^^^^^
  ```

- Warning: `modules/local/qiime2_export_reltax.nf:4:14`: The use of `projectDir` in a process is discouraged -- input files should be provided as process inputs

  ```nextflow
      conda "${projectDir}/modules/local/envs/qiime2-amplicon-2024.10-py310-linux-conda.yml"
               ^^^^^^^^^^
  ```

- Warning: `modules/local/qiime2_extract.nf:6:14`: The use of `projectDir` in a process is discouraged -- input files should be provided as process inputs

  ```nextflow
      conda "${projectDir}/modules/local/envs/qiime2-amplicon-2024.10-py310-linux-conda.yml"
               ^^^^^^^^^^
  ```

- Warning: `modules/local/qiime2_featuretable_group.nf:5:14`: The use of `projectDir` in a process is discouraged -- input files should be provided as process inputs

  ```nextflow
      conda "${projectDir}/modules/local/envs/qiime2-amplicon-2024.10-py310-linux-conda.yml"
               ^^^^^^^^^^
  ```

- Warning: `modules/local/qiime2_filtersamples.nf:5:14`: The use of `projectDir` in a process is discouraged -- input files should be provided as process inputs

  ```nextflow
      conda "${projectDir}/modules/local/envs/qiime2-amplicon-2024.10-py310-linux-conda.yml"
               ^^^^^^^^^^
  ```

- Warning: `modules/local/qiime2_inasv.nf:5:14`: The use of `projectDir` in a process is discouraged -- input files should be provided as process inputs

  ```nextflow
      conda "${projectDir}/modules/local/envs/qiime2-amplicon-2024.10-py310-linux-conda.yml"
               ^^^^^^^^^^
  ```

- Warning: `modules/local/qiime2_inseq.nf:5:14`: The use of `projectDir` in a process is discouraged -- input files should be provided as process inputs

  ```nextflow
      conda "${projectDir}/modules/local/envs/qiime2-amplicon-2024.10-py310-linux-conda.yml"
               ^^^^^^^^^^
  ```

- Warning: `modules/local/qiime2_intax.nf:5:14`: The use of `projectDir` in a process is discouraged -- input files should be provided as process inputs

  ```nextflow
      conda "${projectDir}/modules/local/envs/qiime2-amplicon-2024.10-py310-linux-conda.yml"
               ^^^^^^^^^^
  ```

- Warning: `modules/local/qiime2_intree.nf:5:14`: The use of `projectDir` in a process is discouraged -- input files should be provided as process inputs

  ```nextflow
      conda "${projectDir}/modules/local/envs/qiime2-amplicon-2024.10-py310-linux-conda.yml"
               ^^^^^^^^^^
  ```

- Warning: `modules/local/qiime2_seqfiltertable.nf:5:14`: The use of `projectDir` in a process is discouraged -- input files should be provided as process inputs

  ```nextflow
      conda "${projectDir}/modules/local/envs/qiime2-amplicon-2024.10-py310-linux-conda.yml"
               ^^^^^^^^^^
  ```

- Warning: `modules/local/qiime2_tablefiltertaxa.nf:5:14`: The use of `projectDir` in a process is discouraged -- input files should be provided as process inputs

  ```nextflow
      conda "${projectDir}/modules/local/envs/qiime2-amplicon-2024.10-py310-linux-conda.yml"
               ^^^^^^^^^^
  ```

- Warning: `modules/local/qiime2_train.nf:6:14`: The use of `projectDir` in a process is discouraged -- input files should be provided as process inputs

  ```nextflow
      conda "${projectDir}/modules/local/envs/qiime2-amplicon-2024.10-py310-linux-conda.yml"
               ^^^^^^^^^^
  ```

- Warning: `modules/local/qiime2_tree.nf:4:14`: The use of `projectDir` in a process is discouraged -- input files should be provided as process inputs

  ```nextflow
      conda "${projectDir}/modules/local/envs/qiime2-amplicon-2024.10-py310-linux-conda.yml"
               ^^^^^^^^^^
  ```

- Warning: `modules/local/sidle_align.nf:5:14`: The use of `projectDir` in a process is discouraged -- input files should be provided as process inputs

  ```nextflow
      conda "${projectDir}/modules/local/envs/pipesidle-0-1-0-beta.yml"
               ^^^^^^^^^^
  ```

- Warning: `modules/local/sidle_align.nf:18:9`: Variable was declared but not used

  ```nextflow
      def primerfw = "${meta.fw_primer}"
          ^^^^^^^^
  ```

- Warning: `modules/local/sidle_align.nf:19:9`: Variable was declared but not used

  ```nextflow
      def primerrv = "${meta.rv_primer}"
          ^^^^^^^^
  ```

- Warning: `modules/local/sidle_dbextract.nf:6:14`: The use of `projectDir` in a process is discouraged -- input files should be provided as process inputs

  ```nextflow
      conda "${projectDir}/modules/local/envs/pipesidle-0-1-0-beta.yml"
               ^^^^^^^^^^
  ```

- Warning: `modules/local/sidle_dbfilt.nf:4:14`: The use of `projectDir` in a process is discouraged -- input files should be provided as process inputs

  ```nextflow
      conda "${projectDir}/modules/local/envs/pipesidle-0-1-0-beta.yml"
               ^^^^^^^^^^
  ```

- Warning: `modules/local/sidle_dbrecon.nf:4:14`: The use of `projectDir` in a process is discouraged -- input files should be provided as process inputs

  ```nextflow
      conda "${projectDir}/modules/local/envs/pipesidle-0-1-0-beta.yml"
               ^^^^^^^^^^
  ```

- Warning: `modules/local/sidle_dbrecon.nf:22:59`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
      def df = [metaid, map, aligned_map].transpose().sort{ it[0] }
                                                            ^^
  ```

- Warning: `modules/local/sidle_filttax.nf:5:14`: The use of `projectDir` in a process is discouraged -- input files should be provided as process inputs

  ```nextflow
      conda "${projectDir}/modules/local/envs/pipesidle-0-1-0-beta.yml"
               ^^^^^^^^^^
  ```

- Warning: `modules/local/sidle_in.nf:5:14`: The use of `projectDir` in a process is discouraged -- input files should be provided as process inputs

  ```nextflow
      conda "${projectDir}/modules/local/envs/pipesidle-0-1-0-beta.yml"
               ^^^^^^^^^^
  ```

- Warning: `modules/local/sidle_in.nf:16:9`: Variable was declared but not used

  ```nextflow
      def args = task.ext.args ?: ''
          ^^^^
  ```

- Warning: `modules/local/sidle_indb.nf:4:14`: The use of `projectDir` in a process is discouraged -- input files should be provided as process inputs

  ```nextflow
      conda "${projectDir}/modules/local/envs/pipesidle-0-1-0-beta.yml"
               ^^^^^^^^^^
  ```

- Warning: `modules/local/sidle_indbaligned.nf:4:14`: The use of `projectDir` in a process is discouraged -- input files should be provided as process inputs

  ```nextflow
      conda "${projectDir}/modules/local/envs/pipesidle-0-1-0-beta.yml"
               ^^^^^^^^^^
  ```

- Warning: `modules/local/sidle_indbaligned.nf:15:9`: Variable was declared but not used

  ```nextflow
      def args = task.ext.args ?: ''
          ^^^^
  ```

- Warning: `modules/local/sidle_seqrecon.nf:5:14`: The use of `projectDir` in a process is discouraged -- input files should be provided as process inputs

  ```nextflow
      conda "${projectDir}/modules/local/envs/pipesidle-0-1-0-beta.yml"
               ^^^^^^^^^^
  ```

- Warning: `modules/local/sidle_tablerecon.nf:4:14`: The use of `projectDir` in a process is discouraged -- input files should be provided as process inputs

  ```nextflow
      conda "${projectDir}/modules/local/envs/pipesidle-0-1-0-beta.yml"
               ^^^^^^^^^^
  ```

- Warning: `modules/local/sidle_tablerecon.nf:25:61`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
      def df = [metaid, aligned_map, table].transpose().sort{ it[0] }
                                                              ^^
  ```

- Warning: `modules/local/sidle_taxrecon.nf:4:14`: The use of `projectDir` in a process is discouraged -- input files should be provided as process inputs

  ```nextflow
      conda "${projectDir}/modules/local/envs/pipesidle-0-1-0-beta.yml"
               ^^^^^^^^^^
  ```

- Warning: `modules/local/sidle_treerecon.nf:4:14`: The use of `projectDir` in a process is discouraged -- input files should be provided as process inputs

  ```nextflow
      conda "${projectDir}/modules/local/envs/pipesidle-0-1-0-beta.yml"
               ^^^^^^^^^^
  ```

- Warning: `modules/local/sidle_trim.nf:5:14`: The use of `projectDir` in a process is discouraged -- input files should be provided as process inputs

  ```nextflow
      conda "${projectDir}/modules/local/envs/pipesidle-0-1-0-beta.yml"
               ^^^^^^^^^^
  ```

- Warning: `modules/local/sidle_trim.nf:17:9`: Variable was declared but not used

  ```nextflow
      def args = task.ext.args ?: ''
          ^^^^
  ```

- Warning: `modules/local/sidle_trim.nf:19:9`: Variable was declared but not used

  ```nextflow
      def primerfw = "${meta.fw_primer}"
          ^^^^^^^^
  ```

- Warning: `modules/local/sidle_trim.nf:20:9`: Variable was declared but not used

  ```nextflow
      def primerrv = "${meta.rv_primer}"
          ^^^^^^^^
  ```

- Warning: `modules/nf-core/kraken2/kraken2/main.nf:59:9`: Variable was declared but not used

  ```nextflow
      def args = task.ext.args ?: ''
          ^^^^
  ```

- Warning: `modules/nf-core/kraken2/kraken2/main.nf:61:9`: Variable was declared but not used

  ```nextflow
      def paired       = meta.single_end ? "" : "--paired"
          ^^^^^^
  ```

- Warning: `modules/nf-core/kraken2/kraken2/main.nf:64:9`: Variable was declared but not used

  ```nextflow
      def readclassification_option = save_reads_assignment ? "--output ${prefix}.kraken2.classifiedreads.txt" : "--output /dev/null"
          ^^^^^^^^^^^^^^^^^^^^^^^^^
  ```

- Warning: `modules/nf-core/kraken2/kraken2/main.nf:65:9`: Variable was declared but not used

  ```nextflow
      def compress_reads_command = save_output_fastqs ? "pigz -p $task.cpus *.fastq" : ""
          ^^^^^^^^^^^^^^^^^^^^^^
  ```

- Warning: `modules/nf-core/pigz/uncompress/main.nf:39:9`: Variable was declared but not used

  ```nextflow
      def args = task.ext.args ?: ''
          ^^^^
  ```

- Warning: `modules/nf-core/vsearch/cluster/main.nf:78:9`: Variable was declared but not used

  ```nextflow
      def args = task.ext.args ?: ''
          ^^^^
  ```

- Warning: `subworkflows/local/cutadapt_workflow.nf:65:22`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          .map { meta, reads -> [ meta.id ] }
                       ^^^^^
  ```

- Warning: `subworkflows/local/dada2_preprocessing.nf:24:20`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
              .map { meta, reads -> [ reads ] }
                     ^^^^
  ```

- Warning: `subworkflows/local/dada2_preprocessing.nf:30:20`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
              .map { meta, reads -> [ reads[0] ] }
                     ^^^^
  ```

- Warning: `subworkflows/local/dada2_preprocessing.nf:35:20`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
              .map { meta, reads -> [ reads[1] ] }
                     ^^^^
  ```

- Warning: `subworkflows/local/dada2_preprocessing.nf:86:22`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          .map { meta, reads, logs, args -> [ meta.id ] }
                       ^^^^^
  ```

- Warning: `subworkflows/local/dada2_preprocessing.nf:86:29`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          .map { meta, reads, logs, args -> [ meta.id ] }
                              ^^^^
  ```

- Warning: `subworkflows/local/dada2_preprocessing.nf:86:35`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          .map { meta, reads, logs, args -> [ meta.id ] }
                                    ^^^^
  ```

- Warning: `subworkflows/local/dada2_preprocessing.nf:100:28`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          .map{ meta, reads, logs, args -> [meta, reads] }
                             ^^^^
  ```

- Warning: `subworkflows/local/dada2_preprocessing.nf:100:34`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          .map{ meta, reads, logs, args -> [meta, reads] }
                                   ^^^^
  ```

- Warning: `subworkflows/local/dada2_preprocessing.nf:103:21`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          .map{ meta, reads, logs, args -> [meta, logs] }
                      ^^^^^
  ```

- Warning: `subworkflows/local/dada2_preprocessing.nf:103:34`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          .map{ meta, reads, logs, args -> [meta, logs] }
                                   ^^^^
  ```

- Warning: `subworkflows/local/dada2_preprocessing.nf:106:15`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          .map{ meta, reads, logs, args -> args }
                ^^^^
  ```

- Warning: `subworkflows/local/dada2_preprocessing.nf:106:21`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          .map{ meta, reads, logs, args -> args }
                      ^^^^^
  ```

- Warning: `subworkflows/local/dada2_preprocessing.nf:106:28`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          .map{ meta, reads, logs, args -> args }
                             ^^^^
  ```

- Warning: `subworkflows/local/dada2_preprocessing.nf:112:20`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
              .map { meta, reads -> [ reads ] }
                     ^^^^
  ```

- Warning: `subworkflows/local/dada2_preprocessing.nf:118:20`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
              .map { meta, reads -> [ reads[0] ] }
                     ^^^^
  ```

- Warning: `subworkflows/local/dada2_preprocessing.nf:123:20`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
              .map { meta, reads -> [ reads[1] ] }
                     ^^^^
  ```

- Warning: `subworkflows/local/dada2_taxonomy_wf.nf:48:20`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
              .map { meta, db -> db }
                     ^^^^
  ```

- Warning: `subworkflows/local/parse_input.nf:47:30`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
              .flatMap { meta, reads -> [ meta.run ] }
                               ^^^^^
  ```

- Warning: `subworkflows/local/parse_input.nf:64:22`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          .map { meta, reads -> [ meta.sample ] }
                       ^^^^^
  ```

- Warning: `subworkflows/local/parse_input.nf:75:22`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          .map { meta, reads -> meta.sample }
                       ^^^^^
  ```

- Warning: `subworkflows/local/parse_input.nf:80:22`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          .map { meta, reads -> meta.sample }
                       ^^^^^
  ```

- Warning: `subworkflows/local/qiime2_diversity.nf:21:5`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
      ch_metacolumn_all //METADATA_ALL.out
      ^^^^^^^^^^^^^^^^^
  ```

- Warning: `subworkflows/local/qiime2_preptax.nf:69:21`: Variable was declared but not used

  ```nextflow
                  def files = file(dir.resolve("*.fna"), checkIfExists: true)
                      ^^^^^
  ```

- Warning: `subworkflows/local/qiime2_preptax.nf:75:21`: Variable was declared but not used

  ```nextflow
                  def files = file(dir.resolve("*.tax"), checkIfExists: true)
                      ^^^^^
  ```

- Warning: `subworkflows/local/utils_nfcore_ampliseq_pipeline/main.nf:32:5`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
      monochrome_logs   // boolean: Do not use coloured log outputs
      ^^^^^^^^^^^^^^^
  ```

- Warning: `subworkflows/local/utils_nfcore_ampliseq_pipeline/main.nf:35:5`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
      input             //  string: Path to input samplesheet
      ^^^^^
  ```

- Warning: `subworkflows/nf-core/fasta_newick_epang_gappa/main.nf:22:19`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_versions = Channel.empty()
                    ^^^^^^^
  ```

- Warning: `subworkflows/nf-core/fasta_newick_epang_gappa/main.nf:25:41`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
      ch_hmmer_data = ch_pp_data.filter { it.data.alignmethod == 'hmmer' }
                                          ^^
  ```

- Warning: `subworkflows/nf-core/fasta_newick_epang_gappa/main.nf:26:41`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
      ch_mafft_data = ch_pp_data.filter { it.data.alignmethod == 'mafft' }
                                          ^^
  ```

- Warning: `subworkflows/nf-core/fasta_newick_epang_gappa/main.nf:31:25`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
              .filter { ! it.data.hmmfile }
                          ^^
  ```

- Warning: `subworkflows/nf-core/fasta_newick_epang_gappa/main.nf:32:22`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
              .map { [ it.meta, it.data.refseqfile ] },
                       ^^
  ```

- Warning: `subworkflows/nf-core/fasta_newick_epang_gappa/main.nf:32:31`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
              .map { [ it.meta, it.data.refseqfile ] },
                                ^^
  ```

- Warning: `subworkflows/nf-core/fasta_newick_epang_gappa/main.nf:36:14`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_hmm = Channel.empty()
               ^^^^^^^
  ```

- Warning: `subworkflows/nf-core/fasta_newick_epang_gappa/main.nf:37:45`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          .mix(HMMER_HMMBUILD.out.hmm.map { [ it[0], it[1] ] })
                                              ^^
  ```

- Warning: `subworkflows/nf-core/fasta_newick_epang_gappa/main.nf:37:52`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          .mix(HMMER_HMMBUILD.out.hmm.map { [ it[0], it[1] ] })
                                                     ^^
  ```

- Warning: `subworkflows/nf-core/fasta_newick_epang_gappa/main.nf:40:27`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
                  .filter { it.data.hmmfile }
                            ^^
  ```

- Warning: `subworkflows/nf-core/fasta_newick_epang_gappa/main.nf:41:26`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
                  .map { [ it.meta, it.data.hmmfile ] }
                           ^^
  ```

- Warning: `subworkflows/nf-core/fasta_newick_epang_gappa/main.nf:41:35`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
                  .map { [ it.meta, it.data.hmmfile ] }
                                    ^^
  ```

- Warning: `subworkflows/nf-core/fasta_newick_epang_gappa/main.nf:49:25`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
              .filter { ! it.data.hmmfile }
                          ^^
  ```

- Warning: `subworkflows/nf-core/fasta_newick_epang_gappa/main.nf:50:22`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
              .map { [ it.meta, it.data.refseqfile ] }
                       ^^
  ```

- Warning: `subworkflows/nf-core/fasta_newick_epang_gappa/main.nf:50:31`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
              .map { [ it.meta, it.data.refseqfile ] }
                                ^^
  ```

- Warning: `subworkflows/nf-core/fasta_newick_epang_gappa/main.nf:52:26`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_hmmer_unaligned = Channel.empty()
                           ^^^^^^^
  ```

- Warning: `subworkflows/nf-core/fasta_newick_epang_gappa/main.nf:53:57`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          .mix(HMMER_UNALIGNREF.out.seqreformated.map { [ it[0], it[1] ] })
                                                          ^^
  ```

- Warning: `subworkflows/nf-core/fasta_newick_epang_gappa/main.nf:53:64`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          .mix(HMMER_UNALIGNREF.out.seqreformated.map { [ it[0], it[1] ] })
                                                                 ^^
  ```

- Warning: `subworkflows/nf-core/fasta_newick_epang_gappa/main.nf:56:27`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
                  .filter { it.data.hmmfile }
                            ^^
  ```

- Warning: `subworkflows/nf-core/fasta_newick_epang_gappa/main.nf:57:26`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
                  .map { [ it.meta, it.data.refseqfile ] }
                           ^^
  ```

- Warning: `subworkflows/nf-core/fasta_newick_epang_gappa/main.nf:57:35`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
                  .map { [ it.meta, it.data.refseqfile ] }
                                    ^^
  ```

- Warning: `subworkflows/nf-core/fasta_newick_epang_gappa/main.nf:65:41`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          .groupTuple(size: 2, sort: { a, b -> a =~ /\.hmm/ ? 1 : -1 })
                                          ^
  ```

- Warning: `subworkflows/nf-core/fasta_newick_epang_gappa/main.nf:68:35`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          ch_hmmer_alignref.map { [ it[0], it[1][0] ] },
                                    ^^
  ```

- Warning: `subworkflows/nf-core/fasta_newick_epang_gappa/main.nf:68:42`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          ch_hmmer_alignref.map { [ it[0], it[1][0] ] },
                                           ^^
  ```

- Warning: `subworkflows/nf-core/fasta_newick_epang_gappa/main.nf:69:33`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          ch_hmmer_alignref.map { it[1][1] }
                                  ^^
  ```

- Warning: `subworkflows/nf-core/fasta_newick_epang_gappa/main.nf:73:27`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_hmmer_alignquery = Channel.empty()
                            ^^^^^^^
  ```

- Warning: `subworkflows/nf-core/fasta_newick_epang_gappa/main.nf:74:36`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          .mix(ch_hmmer_data.map { [ it.meta, it.data.queryseqfile ] })
                                     ^^
  ```

- Warning: `subworkflows/nf-core/fasta_newick_epang_gappa/main.nf:74:45`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          .mix(ch_hmmer_data.map { [ it.meta, it.data.queryseqfile ] })
                                              ^^
  ```

- Warning: `subworkflows/nf-core/fasta_newick_epang_gappa/main.nf:76:41`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          .groupTuple(size: 2, sort: { a, b -> a =~ /\.hmm/ ? 1 : -1 })
                                          ^
  ```

- Warning: `subworkflows/nf-core/fasta_newick_epang_gappa/main.nf:79:37`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          ch_hmmer_alignquery.map { [ it[0], it[1][0] ] },
                                      ^^
  ```

- Warning: `subworkflows/nf-core/fasta_newick_epang_gappa/main.nf:79:44`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          ch_hmmer_alignquery.map { [ it[0], it[1][0] ] },
                                             ^^
  ```

- Warning: `subworkflows/nf-core/fasta_newick_epang_gappa/main.nf:80:35`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          ch_hmmer_alignquery.map { it[1][1] }
                                    ^^
  ```

- Warning: `subworkflows/nf-core/fasta_newick_epang_gappa/main.nf:85:57`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
      HMMER_MASKREF ( HMMER_HMMALIGNREF.out.sthlm.map { [ it[0], it[1], [], [], [], [], [], [] ] }, [] )
                                                          ^^
  ```

- Warning: `subworkflows/nf-core/fasta_newick_epang_gappa/main.nf:85:64`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
      HMMER_MASKREF ( HMMER_HMMALIGNREF.out.sthlm.map { [ it[0], it[1], [], [], [], [], [], [] ] }, [] )
                                                                 ^^
  ```

- Warning: `subworkflows/nf-core/fasta_newick_epang_gappa/main.nf:88:61`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
      HMMER_MASKQUERY ( HMMER_HMMALIGNQUERY.out.sthlm.map { [ it[0], it[1], [], [], [], [], [], [] ] }, [] )
                                                              ^^
  ```

- Warning: `subworkflows/nf-core/fasta_newick_epang_gappa/main.nf:88:68`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
      HMMER_MASKQUERY ( HMMER_HMMALIGNQUERY.out.sthlm.map { [ it[0], it[1], [], [], [], [], [], [] ] }, [] )
                                                                     ^^
  ```

- Warning: `subworkflows/nf-core/fasta_newick_epang_gappa/main.nf:100:31`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          ch_mafft_data.map { [ it.meta, it.data.refseqfile ] },
                                ^^
  ```

- Warning: `subworkflows/nf-core/fasta_newick_epang_gappa/main.nf:100:40`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          ch_mafft_data.map { [ it.meta, it.data.refseqfile ] },
                                         ^^
  ```

- Warning: `subworkflows/nf-core/fasta_newick_epang_gappa/main.nf:101:31`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          ch_mafft_data.map { [ it.data.queryseqfile ] }
                                ^^
  ```

- Warning: `subworkflows/nf-core/fasta_newick_epang_gappa/main.nf:107:31`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          ch_mafft_data.map { [ it.meta, it.data.refseqfile ] }
                                ^^
  ```

- Warning: `subworkflows/nf-core/fasta_newick_epang_gappa/main.nf:107:40`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          ch_mafft_data.map { [ it.meta, it.data.refseqfile ] }
                                         ^^
  ```

- Warning: `subworkflows/nf-core/fasta_newick_epang_gappa/main.nf:113:41`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
      ch_epang_query = ch_pp_data.map { [ it.meta, it.data.model, it.data.refphylogeny ] }
                                          ^^
  ```

- Warning: `subworkflows/nf-core/fasta_newick_epang_gappa/main.nf:113:50`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
      ch_epang_query = ch_pp_data.map { [ it.meta, it.data.model, it.data.refphylogeny ] }
                                                   ^^
  ```

- Warning: `subworkflows/nf-core/fasta_newick_epang_gappa/main.nf:113:65`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
      ch_epang_query = ch_pp_data.map { [ it.meta, it.data.model, it.data.refphylogeny ] }
                                                                  ^^
  ```

- Warning: `subworkflows/nf-core/fasta_newick_epang_gappa/main.nf:117:32`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
              ch_pp_data.map { [ it.meta, it.data.model, it.data.refphylogeny ] }
                                 ^^
  ```

- Warning: `subworkflows/nf-core/fasta_newick_epang_gappa/main.nf:117:41`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
              ch_pp_data.map { [ it.meta, it.data.model, it.data.refphylogeny ] }
                                          ^^
  ```

- Warning: `subworkflows/nf-core/fasta_newick_epang_gappa/main.nf:117:56`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
              ch_pp_data.map { [ it.meta, it.data.model, it.data.refphylogeny ] }
                                                         ^^
  ```

- Warning: `subworkflows/nf-core/fasta_newick_epang_gappa/main.nf:118:53`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
                  .join(EPANG_SPLIT.out.query.map { [ it[0], it[1] ] } )
                                                      ^^
  ```

- Warning: `subworkflows/nf-core/fasta_newick_epang_gappa/main.nf:118:60`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
                  .join(EPANG_SPLIT.out.query.map { [ it[0], it[1] ] } )
                                                             ^^
  ```

- Warning: `subworkflows/nf-core/fasta_newick_epang_gappa/main.nf:119:57`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
                  .join(EPANG_SPLIT.out.reference.map { [ it[0], it[1] ] } )
                                                          ^^
  ```

- Warning: `subworkflows/nf-core/fasta_newick_epang_gappa/main.nf:119:64`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
                  .join(EPANG_SPLIT.out.reference.map { [ it[0], it[1] ] } )
                                                                 ^^
  ```

- Warning: `subworkflows/nf-core/fasta_newick_epang_gappa/main.nf:121:23`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          .map { [ [ id:it[0].id, model:it[1] ], it[3], it[4], it[2] ] }
                        ^^
  ```

- Warning: `subworkflows/nf-core/fasta_newick_epang_gappa/main.nf:121:39`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          .map { [ [ id:it[0].id, model:it[1] ], it[3], it[4], it[2] ] }
                                        ^^
  ```

- Warning: `subworkflows/nf-core/fasta_newick_epang_gappa/main.nf:121:48`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          .map { [ [ id:it[0].id, model:it[1] ], it[3], it[4], it[2] ] }
                                                 ^^
  ```

- Warning: `subworkflows/nf-core/fasta_newick_epang_gappa/main.nf:121:55`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          .map { [ [ id:it[0].id, model:it[1] ], it[3], it[4], it[2] ] }
                                                        ^^
  ```

- Warning: `subworkflows/nf-core/fasta_newick_epang_gappa/main.nf:121:62`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          .map { [ [ id:it[0].id, model:it[1] ], it[3], it[4], it[2] ] }
                                                               ^^
  ```

- Warning: `subworkflows/nf-core/fasta_newick_epang_gappa/main.nf:136:27`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
              .map { [ [ id:it[0].id ], it[1] ] }
                            ^^
  ```

- Warning: `subworkflows/nf-core/fasta_newick_epang_gappa/main.nf:136:39`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
              .map { [ [ id:it[0].id ], it[1] ] }
                                        ^^
  ```

- Warning: `subworkflows/nf-core/fasta_newick_epang_gappa/main.nf:137:39`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
              .join( ch_pp_data.map { [ it.meta, it.data.taxonomy ] } )
                                        ^^
  ```

- Warning: `subworkflows/nf-core/fasta_newick_epang_gappa/main.nf:137:48`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
              .join( ch_pp_data.map { [ it.meta, it.data.taxonomy ] } )
                                                 ^^
  ```

- Warning: `workflows/ampliseq.nf:316:22`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          .map { meta, reads -> [ meta.id ] }
                       ^^^^^
  ```

- Warning: `workflows/ampliseq.nf:406:37`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          DADA2_STATS.out.stats.map { meta, stats -> stats }.collect(),
                                      ^^^^
  ```

- Warning: `workflows/ampliseq.nf:407:39`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          DADA2_RMCHIMERA.out.rds.map { meta, rds -> rds }.collect() )
                                        ^^^^
  ```

- Warning: `workflows/ampliseq.nf:428:27`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
                      info, reads ->
                            ^^^^^
  ```

- Warning: `workflows/ampliseq.nf:1026:96`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
              !params.skip_taxonomy && !params.skip_phyloseq ? ROBJECT_WORKFLOW.out.phyloseq.map{info,rds -> [rds]}.collect().ifEmpty( [] ) : [],
                                                                                                 ^^^^
  ```

- Warning: `workflows/ampliseq.nf:1027:86`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
              !params.skip_taxonomy && !params.skip_tse ? ROBJECT_WORKFLOW.out.tse.map{info,rds -> [rds]}.collect().ifEmpty( [] ) : []
                                                                                       ^^^^
  ```
