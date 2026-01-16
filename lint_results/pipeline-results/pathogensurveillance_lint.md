# Nextflow lint results

- Generated: 2026-01-16T06:36:42.470387355Z
- Nextflow version: 25.12.0-edge
- Summary: 40 errors, 486 warnings

## :x: Errors

- Error: `main.nf:46:9`: Unexpected input: 'params'

  ```nextflow
          params.reference_data
          ^
  ```

- Error: `modules/local/initial_classification/main.nf:16:26`: `DOMAIN` is not defined

  ```nextflow
      tuple val(meta), env(DOMAIN)                     , emit: domain
                           ^^^^^^
  ```

- Error: `modules/local/picard_format/main.nf:79:9`: `prefix` is already declared

  ```nextflow
      def prefix = task.ext.prefix    ?: "${meta.id}"
          ^^^^^^
  ```

- Error: `modules/local/pick_assemblies/main.nf:20:26`: `COUNT` is not defined

  ```nextflow
      tuple val(meta), env(COUNT)                     , emit: line_count
                           ^^^^^
  ```

- Error: `modules/local/vcf_to_snp_align/main.nf:17:30`: `SEQ_COUNT` is not defined

  ```nextflow
      tuple val(ref_meta), env(SEQ_COUNT)                , emit: seq_count
                               ^^^^^^^^^
  ```

- Error: `modules/nf-core/bakta/bakta/main.nf:36:9`: `prodigal_tf` is already declared

  ```nextflow
      def prodigal_tf = prodigal_tf ? "--prodigal-tf ${prodigal_tf[0]}" : ""
          ^^^^^^^^^^^
  ```

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

- Error: `modules/nf-core/mafft/main.nf:29:9`: `add` is already declared

  ```nextflow
      def add          = add             ? "--add <(unpigz -cdf ${add})"                   : ''
          ^^^
  ```

- Error: `modules/nf-core/mafft/main.nf:30:9`: `addfragments` is already declared

  ```nextflow
      def addfragments = addfragments    ? "--addfragments <(unpigz -cdf ${addfragments})" : ''
          ^^^^^^^^^^^^
  ```

- Error: `modules/nf-core/mafft/main.nf:31:9`: `addfull` is already declared

  ```nextflow
      def addfull      = addfull         ? "--addfull <(unpigz -cdf ${addfull})"           : ''
          ^^^^^^^
  ```

- Error: `modules/nf-core/mafft/main.nf:32:9`: `addprofile` is already declared

  ```nextflow
      def addprofile   = addprofile      ? "--addprofile <(unpigz -cdf ${addprofile})"     : ''
          ^^^^^^^^^^
  ```

- Error: `modules/nf-core/mafft/main.nf:33:9`: `addlong` is already declared

  ```nextflow
      def addlong      = addlong         ? "--addlong <(unpigz -cdf ${addlong})"           : ''
          ^^^^^^^
  ```

- Error: `modules/nf-core/mafft/main.nf:59:9`: `add` is already declared

  ```nextflow
      def add          = add             ? "--add ${add}"                   : ''
          ^^^
  ```

- Error: `modules/nf-core/mafft/main.nf:60:9`: `addfragments` is already declared

  ```nextflow
      def addfragments = addfragments    ? "--addfragments ${addfragments}" : ''
          ^^^^^^^^^^^^
  ```

- Error: `modules/nf-core/mafft/main.nf:61:9`: `addfull` is already declared

  ```nextflow
      def addfull      = addfull         ? "--addfull ${addfull}"           : ''
          ^^^^^^^
  ```

- Error: `modules/nf-core/mafft/main.nf:62:9`: `addprofile` is already declared

  ```nextflow
      def addprofile   = addprofile      ? "--addprofile ${addprofile}"     : ''
          ^^^^^^^^^^
  ```

- Error: `modules/nf-core/mafft/main.nf:63:9`: `addlong` is already declared

  ```nextflow
      def addlong      = addlong         ? "--addlong ${addlong}"           : ''
          ^^^^^^^
  ```

- Error: `modules/nf-core/sratools/fasterqdump/main.nf:58:9`: `prefix` is already declared

  ```nextflow
      def prefix = task.ext.prefix ?: "${meta.id}"
          ^^^^^^
  ```

- Error: `subworkflows/local/core_genome_phylogeny/main.nf:82:13`: `UNTAR` is not defined

  ```nextflow
              UNTAR( bakta_db_tar )
              ^^^^^
  ```

- Error: `subworkflows/local/core_genome_phylogeny/main.nf:83:24`: `UNTAR` is not defined

  ```nextflow
              bakta_db = UNTAR.out.untar.map{ meta, db -> db }.first()
                         ^^^^^
  ```

- Error: `subworkflows/local/core_genome_phylogeny/main.nf:84:37`: `UNTAR` is not defined

  ```nextflow
              versions = versions.mix(UNTAR.out.versions)
                                      ^^^^^
  ```

- Error: `subworkflows/local/genome_assembly/main.nf:111:28`: `sample_data` is already declared

  ```nextflow
          .map{ sample_meta, sample_data, paths ->
                             ^^^^^^^^^^^
  ```

- Error: `subworkflows/local/prepare_input/main.nf:333:53`: `read_count` is already declared

  ```nextflow
              .map { sample_meta, fastq_paths, depth, read_count ->
                                                      ^^^^^^^^^^
  ```

- Error: `subworkflows/local/utils_nfcore_pathogensurveillance_pipeline/main.nf:106:5`: `for` loops are no longer supported

  ```nextflow
      for (param in checkPathParamList) {
      ^^^
  ```

- Error: `subworkflows/local/utils_nfcore_pathogensurveillance_pipeline/main.nf:106:10`: `param` is not defined

  ```nextflow
      for (param in checkPathParamList) {
           ^^^^^
  ```

- Error: `subworkflows/local/utils_nfcore_pathogensurveillance_pipeline/main.nf:107:12`: `param` is not defined

  ```nextflow
          if (param) { file(param, checkIfExists: true) }
             ^^^^^^^
  ```

- Error: `subworkflows/local/utils_nfcore_pathogensurveillance_pipeline/main.nf:107:27`: `param` is not defined

  ```nextflow
          if (param) { file(param, checkIfExists: true) }
                            ^^^^^
  ```

- Error: `subworkflows/local/utils_nfcore_pathogensurveillance_pipeline/main.nf:125:26`: `versions` is not defined

  ```nextflow
      versions           = versions
                           ^^^^^^^^
  ```

- Error: `workflows/pathogensurveillance.nf:134:5`: `ch_methods_description` is not defined

  ```nextflow
      ch_methods_description.collectFile(
      ^^^^^^^^^^^^^^^^^^^^^^
  ```

- Error: `workflows/pathogensurveillance.nf:172:29`: `versions` is already declared

  ```nextflow
          .map { report_meta, versions, fastqc, fastp, nanoplot, quast ->
                              ^^^^^^^^
  ```

- Error: `workflows/pathogensurveillance.nf:173:13`: Variables in a closure should be declared with `def`

  ```nextflow
              files = (fastqc ?: []) + (fastp ?: []) + (nanoplot ?: []) + (quast ?: []) + ([versions])
              ^^^^^
  ```

## :warning: Warnings

- Warning: `modules/local/assign_context_references/main.nf:24:9`: Variable was declared but not used

  ```nextflow
      def args = task.ext.args ?: ''
          ^^^^
  ```

- Warning: `modules/local/assign_mapping_reference/main.nf:22:9`: Variable was declared but not used

  ```nextflow
      def args = task.ext.args ?: ''
          ^^^^
  ```

- Warning: `modules/local/calculate_pocp/main.nf:21:9`: Variable was declared but not used

  ```nextflow
      def args = task.ext.args ?: ''
          ^^^^
  ```

- Warning: `modules/local/graphtyper/genotype/main.nf:26:9`: Variable was declared but not used

  ```nextflow
      def prefix = task.ext.prefix ?: "${meta.id}"
          ^^^^^^
  ```

- Warning: `modules/local/graphtyper/genotype/main.nf:28:40`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
      def bai_path_text = bam.collect{"${it}.csi"}.join('\\n')
                                         ^^
  ```

- Warning: `modules/local/initial_classification/main.nf:23:9`: Variable was declared but not used

  ```nextflow
      def args = task.ext.args ?: ''
          ^^^^
  ```

- Warning: `modules/local/pick_assemblies/main.nf:27:9`: Variable was declared but not used

  ```nextflow
      def args = task.ext.args ?: ''
          ^^^^
  ```

- Warning: `modules/local/prepare_report_input/main.nf:21:9`: Variable was declared but not used

  ```nextflow
      def args = task.ext.args ?: ''
          ^^^^
  ```

- Warning: `modules/local/vcf_to_snp_align/main.nf:24:9`: Variable was declared but not used

  ```nextflow
      def args = task.ext.args ?: ''
          ^^^^
  ```

- Warning: `modules/nf-core/busco/download/main.nf:22:9`: Variable was declared but not used

  ```nextflow
      def prefix = task.ext.prefix ?: "${lineage}"
          ^^^^^^
  ```

- Warning: `modules/nf-core/busco/download/main.nf:35:9`: Variable was declared but not used

  ```nextflow
      def args = task.ext.args ?: ''
          ^^^^
  ```

- Warning: `modules/nf-core/graphtyper/genotype/main.nf:26:9`: Variable was declared but not used

  ```nextflow
      def prefix = task.ext.prefix ?: "${meta.id}"
          ^^^^^^
  ```

- Warning: `modules/nf-core/graphtyper/genotype/main.nf:27:34`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
      def bam_path_text = bam.sort{it.name}.join('\\n')
                                   ^^
  ```

- Warning: `modules/nf-core/graphtyper/genotype/main.nf:28:38`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
      def index_path_text = index.sort{it.name}.join('\\n')
                                       ^^
  ```

- Warning: `modules/nf-core/graphtyper/vcfconcatenate/main.nf:27:44`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
      input_vcfs = vcf.collate(1000).collect{it.join(' ')} // Batching needed because if there are too many VCFs the shell cannot run the command
                                             ^^
  ```

- Warning: `modules/nf-core/iqtree/main.nf:68:9`: Variable was declared but not used

  ```nextflow
      def trees_rf_arg                = trees_rf                ? "-rf $trees_rf"                 : ''
          ^^^^^^^^^^^^
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

- Warning: `modules/nf-core/mafft/main.nf:57:9`: Variable was declared but not used

  ```nextflow
      def args         = task.ext.args   ?: ''
          ^^^^
  ```

- Warning: `modules/nf-core/mafft/main.nf:59:9`: Variable was declared but not used

  ```nextflow
      def add          = add             ? "--add ${add}"                   : ''
          ^^^
  ```

- Warning: `modules/nf-core/mafft/main.nf:60:9`: Variable was declared but not used

  ```nextflow
      def addfragments = addfragments    ? "--addfragments ${addfragments}" : ''
          ^^^^^^^^^^^^
  ```

- Warning: `modules/nf-core/mafft/main.nf:61:9`: Variable was declared but not used

  ```nextflow
      def addfull      = addfull         ? "--addfull ${addfull}"           : ''
          ^^^^^^^
  ```

- Warning: `modules/nf-core/mafft/main.nf:62:9`: Variable was declared but not used

  ```nextflow
      def addprofile   = addprofile      ? "--addprofile ${addprofile}"     : ''
          ^^^^^^^^^^
  ```

- Warning: `modules/nf-core/mafft/main.nf:63:9`: Variable was declared but not used

  ```nextflow
      def addlong      = addlong         ? "--addlong ${addlong}"           : ''
          ^^^^^^^
  ```

- Warning: `modules/nf-core/picard/sortsam/main.nf:22:9`: Variable was declared but not used

  ```nextflow
      def args = task.ext.args ?: ''
          ^^^^
  ```

- Warning: `modules/nf-core/quast/main.nf:52:9`: Variable was declared but not used

  ```nextflow
      def args      = task.ext.args   ?: ''
          ^^^^
  ```

- Warning: `modules/nf-core/quast/main.nf:54:9`: Variable was declared but not used

  ```nextflow
      def features  = gff             ? "--features $gff" : ''
          ^^^^^^^^
  ```

- Warning: `modules/nf-core/quast/main.nf:55:9`: Variable was declared but not used

  ```nextflow
      def reference = fasta           ? "-r $fasta" : ''
          ^^^^^^^^^
  ```

- Warning: `modules/nf-core/sourmash/compare/main.nf:32:48`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
      def sigs = signatures ? "${signatures.sort{it.toString()}.join(' ')}" : ''
                                                 ^^
  ```

- Warning: `modules/nf-core/spades/main.nf:80:9`: Variable was declared but not used

  ```nextflow
      def args = task.ext.args ?: ''
          ^^^^
  ```

- Warning: `modules/nf-core/spades/main.nf:82:9`: Variable was declared but not used

  ```nextflow
      def maxmem = task.memory.toGiga()
          ^^^^^^
  ```

- Warning: `modules/nf-core/spades/main.nf:86:9`: Variable was declared but not used

  ```nextflow
      def custom_hmms = hmm ? "--custom-hmms $hmm" : ""
          ^^^^^^^^^^^
  ```

- Warning: `modules/nf-core/spades/main.nf:87:9`: Variable was declared but not used

  ```nextflow
      def reads = yml ? "--dataset $yml" : "$illumina_reads $pacbio_reads $nanopore_reads"
          ^^^^^
  ```

- Warning: `subworkflows/local/align_reads/main.nf:12:16`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      versions = Channel.empty()
                 ^^^^^^^
  ```

- Warning: `subworkflows/local/align_reads/main.nf:22:31`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          .map { combined_meta, meta, fastqs, ref_meta, reference, ref_index, bam_index ->
                                ^^^^
  ```

- Warning: `subworkflows/local/align_reads/main.nf:22:45`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          .map { combined_meta, meta, fastqs, ref_meta, reference, ref_index, bam_index ->
                                              ^^^^^^^^
  ```

- Warning: `subworkflows/local/align_reads/main.nf:22:55`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          .map { combined_meta, meta, fastqs, ref_meta, reference, ref_index, bam_index ->
                                                        ^^^^^^^^^
  ```

- Warning: `subworkflows/local/align_reads/main.nf:22:66`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          .map { combined_meta, meta, fastqs, ref_meta, reference, ref_index, bam_index ->
                                                                   ^^^^^^^^^
  ```

- Warning: `subworkflows/local/align_reads/main.nf:22:77`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          .map { combined_meta, meta, fastqs, ref_meta, reference, ref_index, bam_index ->
                                                                              ^^^^^^^^^
  ```

- Warning: `subworkflows/local/align_reads/main.nf:27:56`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
      ch_bwa_index = samp_ref_combo.map { combined_meta, meta, fastqs, ref_meta, reference, ref_index, bam_index ->
                                                         ^^^^
  ```

- Warning: `subworkflows/local/align_reads/main.nf:27:62`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
      ch_bwa_index = samp_ref_combo.map { combined_meta, meta, fastqs, ref_meta, reference, ref_index, bam_index ->
                                                               ^^^^^^
  ```

- Warning: `subworkflows/local/align_reads/main.nf:27:70`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
      ch_bwa_index = samp_ref_combo.map { combined_meta, meta, fastqs, ref_meta, reference, ref_index, bam_index ->
                                                                       ^^^^^^^^
  ```

- Warning: `subworkflows/local/align_reads/main.nf:27:80`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
      ch_bwa_index = samp_ref_combo.map { combined_meta, meta, fastqs, ref_meta, reference, ref_index, bam_index ->
                                                                                 ^^^^^^^^^
  ```

- Warning: `subworkflows/local/align_reads/main.nf:27:91`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
      ch_bwa_index = samp_ref_combo.map { combined_meta, meta, fastqs, ref_meta, reference, ref_index, bam_index ->
                                                                                            ^^^^^^^^^
  ```

- Warning: `subworkflows/local/align_reads/main.nf:34:56`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
      ch_reference = samp_ref_combo.map { combined_meta, meta, fastqs, ref_meta, reference, ref_index, bam_index ->
                                                         ^^^^
  ```

- Warning: `subworkflows/local/align_reads/main.nf:34:62`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
      ch_reference = samp_ref_combo.map { combined_meta, meta, fastqs, ref_meta, reference, ref_index, bam_index ->
                                                               ^^^^^^
  ```

- Warning: `subworkflows/local/align_reads/main.nf:34:70`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
      ch_reference = samp_ref_combo.map { combined_meta, meta, fastqs, ref_meta, reference, ref_index, bam_index ->
                                                                       ^^^^^^^^
  ```

- Warning: `subworkflows/local/align_reads/main.nf:34:91`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
      ch_reference = samp_ref_combo.map { combined_meta, meta, fastqs, ref_meta, reference, ref_index, bam_index ->
                                                                                            ^^^^^^^^^
  ```

- Warning: `subworkflows/local/align_reads/main.nf:34:102`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
      ch_reference = samp_ref_combo.map { combined_meta, meta, fastqs, ref_meta, reference, ref_index, bam_index ->
                                                                                                       ^^^^^^^^^
  ```

- Warning: `subworkflows/local/align_reads/main.nf:37:56`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
      ch_ref_index = samp_ref_combo.map { combined_meta, meta, fastqs, ref_meta, reference, ref_index, bam_index ->
                                                         ^^^^
  ```

- Warning: `subworkflows/local/align_reads/main.nf:37:62`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
      ch_ref_index = samp_ref_combo.map { combined_meta, meta, fastqs, ref_meta, reference, ref_index, bam_index ->
                                                               ^^^^^^
  ```

- Warning: `subworkflows/local/align_reads/main.nf:37:70`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
      ch_ref_index = samp_ref_combo.map { combined_meta, meta, fastqs, ref_meta, reference, ref_index, bam_index ->
                                                                       ^^^^^^^^
  ```

- Warning: `subworkflows/local/align_reads/main.nf:37:80`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
      ch_ref_index = samp_ref_combo.map { combined_meta, meta, fastqs, ref_meta, reference, ref_index, bam_index ->
                                                                                 ^^^^^^^^^
  ```

- Warning: `subworkflows/local/align_reads/main.nf:37:102`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
      ch_ref_index = samp_ref_combo.map { combined_meta, meta, fastqs, ref_meta, reference, ref_index, bam_index ->
                                                                                                       ^^^^^^^^^
  ```

- Warning: `subworkflows/local/busco_phylogeny/main.nf:17:16`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      versions = Channel.empty()
                 ^^^^^^^
  ```

- Warning: `subworkflows/local/busco_phylogeny/main.nf:18:16`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      messages = Channel.empty()
                 ^^^^^^^
  ```

- Warning: `subworkflows/local/busco_phylogeny/main.nf:22:17`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          .filter{it.domain == "Eukaryota"}
                  ^^
  ```

- Warning: `subworkflows/local/busco_phylogeny/main.nf:26:16`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          .map{ [it.sample_id, it.report_group_ids, it.ref_metas] }
                 ^^
  ```

- Warning: `subworkflows/local/busco_phylogeny/main.nf:26:30`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          .map{ [it.sample_id, it.report_group_ids, it.ref_metas] }
                               ^^
  ```

- Warning: `subworkflows/local/busco_phylogeny/main.nf:26:51`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          .map{ [it.sample_id, it.report_group_ids, it.ref_metas] }
                                                    ^^
  ```

- Warning: `subworkflows/local/busco_phylogeny/main.nf:32:82`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          .collectFile() { sample_id, report_group_id, ref_id, ref_name, ref_desc, ref_path, usage ->
                                                                                   ^^^^^^^^
  ```

- Warning: `subworkflows/local/busco_phylogeny/main.nf:35:21`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          .map {[[id: it.getSimpleName()], it]}
                      ^^
  ```

- Warning: `subworkflows/local/busco_phylogeny/main.nf:35:42`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          .map {[[id: it.getSimpleName()], it]}
                                           ^^
  ```

- Warning: `subworkflows/local/busco_phylogeny/main.nf:48:21`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          .map{ [[id: it.report_group_ids], it.ref_metas] }
                      ^^
  ```

- Warning: `subworkflows/local/busco_phylogeny/main.nf:48:43`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          .map{ [[id: it.report_group_ids], it.ref_metas] }
                                            ^^
  ```

- Warning: `subworkflows/local/busco_phylogeny/main.nf:57:17`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          .map { [it[0], it[1].replace('\n', '')] } // remove newline that splitText adds
                  ^^
  ```

- Warning: `subworkflows/local/busco_phylogeny/main.nf:57:24`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          .map { [it[0], it[1].replace('\n', '')] } // remove newline that splitText adds
                         ^^
  ```

- Warning: `subworkflows/local/busco_phylogeny/main.nf:63:48`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          .map {report_meta, ref_meta, ref_path, ref_name ->
                                                 ^^^^^^^^
  ```

- Warning: `subworkflows/local/busco_phylogeny/main.nf:69:21`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          .map{ [[id: it.sample_id], [id: it.report_group_ids]] }
                      ^^
  ```

- Warning: `subworkflows/local/busco_phylogeny/main.nf:69:41`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          .map{ [[id: it.sample_id], [id: it.report_group_ids]] }
                                          ^^
  ```

- Warning: `subworkflows/local/busco_phylogeny/main.nf:74:22`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      BUSCO_DOWNLOAD ( Channel.from( "eukaryota_odb10" ) )
                       ^^^^^^^
  ```

- Warning: `subworkflows/local/busco_phylogeny/main.nf:80:25`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
              .map{ meta, report_meta, path ->
                          ^^^^^^^^^^^
  ```

- Warning: `subworkflows/local/busco_phylogeny/main.nf:95:15`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          .map{ meta, report_meta, path, busco_dir ->
                ^^^^
  ```

- Warning: `subworkflows/local/busco_phylogeny/main.nf:95:34`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          .map{ meta, report_meta, path, busco_dir ->
                                   ^^^^
  ```

- Warning: `subworkflows/local/busco_phylogeny/main.nf:110:17`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
                  it.sample_id == '' ? null : [id: it.sample_id],
                  ^^
  ```

- Warning: `subworkflows/local/busco_phylogeny/main.nf:110:50`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
                  it.sample_id == '' ? null : [id: it.sample_id],
                                                   ^^
  ```

- Warning: `subworkflows/local/busco_phylogeny/main.nf:111:17`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
                  it.report_group_id == '' ? null : [id: it.report_group_id],
                  ^^
  ```

- Warning: `subworkflows/local/busco_phylogeny/main.nf:111:56`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
                  it.report_group_id == '' ? null : [id: it.report_group_id],
                                                         ^^
  ```

- Warning: `subworkflows/local/busco_phylogeny/main.nf:112:17`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
                  it.reference_id == '' ? null : [id: it.reference_id],
                  ^^
  ```

- Warning: `subworkflows/local/busco_phylogeny/main.nf:112:53`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
                  it.reference_id == '' ? null : [id: it.reference_id],
                                                      ^^
  ```

- Warning: `subworkflows/local/busco_phylogeny/main.nf:114:17`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
                  it.message_type,
                  ^^
  ```

- Warning: `subworkflows/local/busco_phylogeny/main.nf:115:17`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
                  it.description
                  ^^
  ```

- Warning: `subworkflows/local/busco_phylogeny/main.nf:141:17`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          .map { [it[0].group_id, it[1]] } // group_meta, tree
                  ^^
  ```

- Warning: `subworkflows/local/busco_phylogeny/main.nf:141:33`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          .map { [it[0].group_id, it[1]] } // group_meta, tree
                                  ^^
  ```

- Warning: `subworkflows/local/call_variants/main.nf:15:16`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      versions = Channel.empty()
                 ^^^^^^^
  ```

- Warning: `subworkflows/local/call_variants/main.nf:29:30`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          .map{ combined_meta, sample_meta, bam, bai, ref, fai, dict ->
                               ^^^^^^^^^^^
  ```

- Warning: `subworkflows/local/call_variants/main.nf:29:43`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          .map{ combined_meta, sample_meta, bam, bai, ref, fai, dict ->
                                            ^^^
  ```

- Warning: `subworkflows/local/call_variants/main.nf:29:48`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          .map{ combined_meta, sample_meta, bam, bai, ref, fai, dict ->
                                                 ^^^
  ```

- Warning: `subworkflows/local/call_variants/main.nf:29:53`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          .map{ combined_meta, sample_meta, bam, bai, ref, fai, dict ->
                                                      ^^^
  ```

- Warning: `subworkflows/local/call_variants/main.nf:29:58`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          .map{ combined_meta, sample_meta, bam, bai, ref, fai, dict ->
                                                           ^^^
  ```

- Warning: `subworkflows/local/call_variants/main.nf:29:63`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          .map{ combined_meta, sample_meta, bam, bai, ref, fai, dict ->
                                                                ^^^^
  ```

- Warning: `subworkflows/local/call_variants/main.nf:34:31`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          .map { combined_meta, sample_meta, bam, bai, ref, fai, dict ->
                                ^^^^^^^^^^^
  ```

- Warning: `subworkflows/local/call_variants/main.nf:34:44`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          .map { combined_meta, sample_meta, bam, bai, ref, fai, dict ->
                                             ^^^
  ```

- Warning: `subworkflows/local/call_variants/main.nf:34:49`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          .map { combined_meta, sample_meta, bam, bai, ref, fai, dict ->
                                                  ^^^
  ```

- Warning: `subworkflows/local/call_variants/main.nf:34:59`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          .map { combined_meta, sample_meta, bam, bai, ref, fai, dict ->
                                                            ^^^
  ```

- Warning: `subworkflows/local/call_variants/main.nf:34:64`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          .map { combined_meta, sample_meta, bam, bai, ref, fai, dict ->
                                                                 ^^^^
  ```

- Warning: `subworkflows/local/call_variants/main.nf:41:17`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          .map { [it.getSimpleName(), it] }
                  ^^
  ```

- Warning: `subworkflows/local/call_variants/main.nf:41:37`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          .map { [it.getSimpleName(), it] }
                                      ^^
  ```

- Warning: `subworkflows/local/call_variants/main.nf:43:16`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          .map { combined_meta_id, region_path, combined_meta ->
                 ^^^^^^^^^^^^^^^^
  ```

- Warning: `subworkflows/local/call_variants/main.nf:50:45`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          ch_ref_grouped.map { combined_meta, sample_meta, bam, bai, ref, fai, dict, region_file ->
                                              ^^^^^^^^^^^
  ```

- Warning: `subworkflows/local/call_variants/main.nf:50:68`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          ch_ref_grouped.map { combined_meta, sample_meta, bam, bai, ref, fai, dict, region_file ->
                                                                     ^^^
  ```

- Warning: `subworkflows/local/call_variants/main.nf:50:73`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          ch_ref_grouped.map { combined_meta, sample_meta, bam, bai, ref, fai, dict, region_file ->
                                                                          ^^^
  ```

- Warning: `subworkflows/local/call_variants/main.nf:50:78`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          ch_ref_grouped.map { combined_meta, sample_meta, bam, bai, ref, fai, dict, region_file ->
                                                                               ^^^^
  ```

- Warning: `subworkflows/local/call_variants/main.nf:50:84`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          ch_ref_grouped.map { combined_meta, sample_meta, bam, bai, ref, fai, dict, region_file ->
                                                                                     ^^^^^^^^^^^
  ```

- Warning: `subworkflows/local/call_variants/main.nf:53:45`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          ch_ref_grouped.map { combined_meta, sample_meta, bam, bai, ref, fai, dict, region_file ->
                                              ^^^^^^^^^^^
  ```

- Warning: `subworkflows/local/call_variants/main.nf:53:58`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          ch_ref_grouped.map { combined_meta, sample_meta, bam, bai, ref, fai, dict, region_file ->
                                                           ^^^
  ```

- Warning: `subworkflows/local/call_variants/main.nf:53:63`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          ch_ref_grouped.map { combined_meta, sample_meta, bam, bai, ref, fai, dict, region_file ->
                                                                ^^^
  ```

- Warning: `subworkflows/local/call_variants/main.nf:53:73`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          ch_ref_grouped.map { combined_meta, sample_meta, bam, bai, ref, fai, dict, region_file ->
                                                                          ^^^
  ```

- Warning: `subworkflows/local/call_variants/main.nf:53:78`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          ch_ref_grouped.map { combined_meta, sample_meta, bam, bai, ref, fai, dict, region_file ->
                                                                               ^^^^
  ```

- Warning: `subworkflows/local/call_variants/main.nf:53:84`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          ch_ref_grouped.map { combined_meta, sample_meta, bam, bai, ref, fai, dict, region_file ->
                                                                                     ^^^^^^^^^^^
  ```

- Warning: `subworkflows/local/call_variants/main.nf:56:45`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          ch_ref_grouped.map { combined_meta, sample_meta, bam, bai, ref, fai, dict, region_file ->
                                              ^^^^^^^^^^^
  ```

- Warning: `subworkflows/local/call_variants/main.nf:56:58`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          ch_ref_grouped.map { combined_meta, sample_meta, bam, bai, ref, fai, dict, region_file ->
                                                           ^^^
  ```

- Warning: `subworkflows/local/call_variants/main.nf:56:63`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          ch_ref_grouped.map { combined_meta, sample_meta, bam, bai, ref, fai, dict, region_file ->
                                                                ^^^
  ```

- Warning: `subworkflows/local/call_variants/main.nf:56:68`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          ch_ref_grouped.map { combined_meta, sample_meta, bam, bai, ref, fai, dict, region_file ->
                                                                     ^^^
  ```

- Warning: `subworkflows/local/call_variants/main.nf:56:78`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          ch_ref_grouped.map { combined_meta, sample_meta, bam, bai, ref, fai, dict, region_file ->
                                                                               ^^^^
  ```

- Warning: `subworkflows/local/call_variants/main.nf:56:84`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          ch_ref_grouped.map { combined_meta, sample_meta, bam, bai, ref, fai, dict, region_file ->
                                                                                     ^^^^^^^^^^^
  ```

- Warning: `subworkflows/local/call_variants/main.nf:59:30`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          ch_ref_grouped.map { combined_meta, sample_meta, bam, bai, ref, fai, dict, region_file ->
                               ^^^^^^^^^^^^^
  ```

- Warning: `subworkflows/local/call_variants/main.nf:59:45`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          ch_ref_grouped.map { combined_meta, sample_meta, bam, bai, ref, fai, dict, region_file ->
                                              ^^^^^^^^^^^
  ```

- Warning: `subworkflows/local/call_variants/main.nf:59:58`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          ch_ref_grouped.map { combined_meta, sample_meta, bam, bai, ref, fai, dict, region_file ->
                                                           ^^^
  ```

- Warning: `subworkflows/local/call_variants/main.nf:59:63`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          ch_ref_grouped.map { combined_meta, sample_meta, bam, bai, ref, fai, dict, region_file ->
                                                                ^^^
  ```

- Warning: `subworkflows/local/call_variants/main.nf:59:68`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          ch_ref_grouped.map { combined_meta, sample_meta, bam, bai, ref, fai, dict, region_file ->
                                                                     ^^^
  ```

- Warning: `subworkflows/local/call_variants/main.nf:59:73`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          ch_ref_grouped.map { combined_meta, sample_meta, bam, bai, ref, fai, dict, region_file ->
                                                                          ^^^
  ```

- Warning: `subworkflows/local/call_variants/main.nf:59:78`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          ch_ref_grouped.map { combined_meta, sample_meta, bam, bai, ref, fai, dict, region_file ->
                                                                               ^^^^
  ```

- Warning: `subworkflows/local/call_variants/main.nf:75:45`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          ch_ref_grouped.map { combined_meta, sample_meta, bam, bai, ref, fai, dict, region_file ->
                                              ^^^^^^^^^^^
  ```

- Warning: `subworkflows/local/call_variants/main.nf:75:58`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          ch_ref_grouped.map { combined_meta, sample_meta, bam, bai, ref, fai, dict, region_file ->
                                                           ^^^
  ```

- Warning: `subworkflows/local/call_variants/main.nf:75:63`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          ch_ref_grouped.map { combined_meta, sample_meta, bam, bai, ref, fai, dict, region_file ->
                                                                ^^^
  ```

- Warning: `subworkflows/local/call_variants/main.nf:75:73`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          ch_ref_grouped.map { combined_meta, sample_meta, bam, bai, ref, fai, dict, region_file ->
                                                                          ^^^
  ```

- Warning: `subworkflows/local/call_variants/main.nf:75:78`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          ch_ref_grouped.map { combined_meta, sample_meta, bam, bai, ref, fai, dict, region_file ->
                                                                               ^^^^
  ```

- Warning: `subworkflows/local/call_variants/main.nf:75:84`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          ch_ref_grouped.map { combined_meta, sample_meta, bam, bai, ref, fai, dict, region_file ->
                                                                                     ^^^^^^^^^^^
  ```

- Warning: `subworkflows/local/call_variants/main.nf:85:49`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
              ch_ref_grouped.map { combined_meta, sample_meta, bam, bai, ref, fai, dict, region_file ->
                                                  ^^^^^^^^^^^
  ```

- Warning: `subworkflows/local/call_variants/main.nf:85:62`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
              ch_ref_grouped.map { combined_meta, sample_meta, bam, bai, ref, fai, dict, region_file ->
                                                               ^^^
  ```

- Warning: `subworkflows/local/call_variants/main.nf:85:67`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
              ch_ref_grouped.map { combined_meta, sample_meta, bam, bai, ref, fai, dict, region_file ->
                                                                    ^^^
  ```

- Warning: `subworkflows/local/call_variants/main.nf:85:88`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
              ch_ref_grouped.map { combined_meta, sample_meta, bam, bai, ref, fai, dict, region_file ->
                                                                                         ^^^^^^^^^^^
  ```

- Warning: `subworkflows/local/call_variants/main.nf:91:49`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          vf_input.map { combined_meta, vcf, tbi, ref, fai, dict, gzi ->
                                                  ^^^
  ```

- Warning: `subworkflows/local/call_variants/main.nf:91:54`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          vf_input.map { combined_meta, vcf, tbi, ref, fai, dict, gzi ->
                                                       ^^^
  ```

- Warning: `subworkflows/local/call_variants/main.nf:91:59`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          vf_input.map { combined_meta, vcf, tbi, ref, fai, dict, gzi ->
                                                            ^^^^
  ```

- Warning: `subworkflows/local/call_variants/main.nf:91:65`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          vf_input.map { combined_meta, vcf, tbi, ref, fai, dict, gzi ->
                                                                  ^^^
  ```

- Warning: `subworkflows/local/call_variants/main.nf:94:39`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          vf_input.map { combined_meta, vcf, tbi, ref, fai, dict, gzi ->
                                        ^^^
  ```

- Warning: `subworkflows/local/call_variants/main.nf:94:44`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          vf_input.map { combined_meta, vcf, tbi, ref, fai, dict, gzi ->
                                             ^^^
  ```

- Warning: `subworkflows/local/call_variants/main.nf:94:54`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          vf_input.map { combined_meta, vcf, tbi, ref, fai, dict, gzi ->
                                                       ^^^
  ```

- Warning: `subworkflows/local/call_variants/main.nf:94:59`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          vf_input.map { combined_meta, vcf, tbi, ref, fai, dict, gzi ->
                                                            ^^^^
  ```

- Warning: `subworkflows/local/call_variants/main.nf:94:65`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          vf_input.map { combined_meta, vcf, tbi, ref, fai, dict, gzi ->
                                                                  ^^^
  ```

- Warning: `subworkflows/local/call_variants/main.nf:97:39`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          vf_input.map { combined_meta, vcf, tbi, ref, fai, dict, gzi ->
                                        ^^^
  ```

- Warning: `subworkflows/local/call_variants/main.nf:97:44`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          vf_input.map { combined_meta, vcf, tbi, ref, fai, dict, gzi ->
                                             ^^^
  ```

- Warning: `subworkflows/local/call_variants/main.nf:97:49`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          vf_input.map { combined_meta, vcf, tbi, ref, fai, dict, gzi ->
                                                  ^^^
  ```

- Warning: `subworkflows/local/call_variants/main.nf:97:59`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          vf_input.map { combined_meta, vcf, tbi, ref, fai, dict, gzi ->
                                                            ^^^^
  ```

- Warning: `subworkflows/local/call_variants/main.nf:97:65`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          vf_input.map { combined_meta, vcf, tbi, ref, fai, dict, gzi ->
                                                                  ^^^
  ```

- Warning: `subworkflows/local/call_variants/main.nf:100:39`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          vf_input.map { combined_meta, vcf, tbi, ref, fai, dict, gzi ->
                                        ^^^
  ```

- Warning: `subworkflows/local/call_variants/main.nf:100:44`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          vf_input.map { combined_meta, vcf, tbi, ref, fai, dict, gzi ->
                                             ^^^
  ```

- Warning: `subworkflows/local/call_variants/main.nf:100:49`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          vf_input.map { combined_meta, vcf, tbi, ref, fai, dict, gzi ->
                                                  ^^^
  ```

- Warning: `subworkflows/local/call_variants/main.nf:100:54`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          vf_input.map { combined_meta, vcf, tbi, ref, fai, dict, gzi ->
                                                       ^^^
  ```

- Warning: `subworkflows/local/call_variants/main.nf:100:65`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          vf_input.map { combined_meta, vcf, tbi, ref, fai, dict, gzi ->
                                                                  ^^^
  ```

- Warning: `subworkflows/local/call_variants/main.nf:103:39`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          vf_input.map { combined_meta, vcf, tbi, ref, fai, dict, gzi ->
                                        ^^^
  ```

- Warning: `subworkflows/local/call_variants/main.nf:103:44`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          vf_input.map { combined_meta, vcf, tbi, ref, fai, dict, gzi ->
                                             ^^^
  ```

- Warning: `subworkflows/local/call_variants/main.nf:103:49`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          vf_input.map { combined_meta, vcf, tbi, ref, fai, dict, gzi ->
                                                  ^^^
  ```

- Warning: `subworkflows/local/call_variants/main.nf:103:54`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          vf_input.map { combined_meta, vcf, tbi, ref, fai, dict, gzi ->
                                                       ^^^
  ```

- Warning: `subworkflows/local/call_variants/main.nf:103:59`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          vf_input.map { combined_meta, vcf, tbi, ref, fai, dict, gzi ->
                                                            ^^^^
  ```

- Warning: `subworkflows/local/call_variants/main.nf:116:44`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          .map { combined_meta, sample_meta, bam, bai, ref, fai, dict, region_file ->
                                             ^^^
  ```

- Warning: `subworkflows/local/call_variants/main.nf:116:49`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          .map { combined_meta, sample_meta, bam, bai, ref, fai, dict, region_file ->
                                                  ^^^
  ```

- Warning: `subworkflows/local/call_variants/main.nf:116:54`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          .map { combined_meta, sample_meta, bam, bai, ref, fai, dict, region_file ->
                                                       ^^^
  ```

- Warning: `subworkflows/local/call_variants/main.nf:116:59`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          .map { combined_meta, sample_meta, bam, bai, ref, fai, dict, region_file ->
                                                            ^^^
  ```

- Warning: `subworkflows/local/call_variants/main.nf:116:64`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          .map { combined_meta, sample_meta, bam, bai, ref, fai, dict, region_file ->
                                                                 ^^^^
  ```

- Warning: `subworkflows/local/call_variants/main.nf:116:70`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          .map { combined_meta, sample_meta, bam, bai, ref, fai, dict, region_file ->
                                                                       ^^^^^^^^^^^
  ```

- Warning: `subworkflows/local/core_genome_phylogeny/main.nf:22:16`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      versions = Channel.empty()
                 ^^^^^^^
  ```

- Warning: `subworkflows/local/core_genome_phylogeny/main.nf:23:16`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      messages = Channel.empty()
                 ^^^^^^^
  ```

- Warning: `subworkflows/local/core_genome_phylogeny/main.nf:27:17`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          .filter{it.domain == "Bacteria" || it.domain == "Archaea"}
                  ^^
  ```

- Warning: `subworkflows/local/core_genome_phylogeny/main.nf:27:44`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          .filter{it.domain == "Bacteria" || it.domain == "Archaea"}
                                             ^^
  ```

- Warning: `subworkflows/local/core_genome_phylogeny/main.nf:31:16`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          .map{ [it.sample_id, it.report_group_ids, it.ref_metas] }
                 ^^
  ```

- Warning: `subworkflows/local/core_genome_phylogeny/main.nf:31:30`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          .map{ [it.sample_id, it.report_group_ids, it.ref_metas] }
                               ^^
  ```

- Warning: `subworkflows/local/core_genome_phylogeny/main.nf:31:51`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          .map{ [it.sample_id, it.report_group_ids, it.ref_metas] }
                                                    ^^
  ```

- Warning: `subworkflows/local/core_genome_phylogeny/main.nf:37:82`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          .collectFile() { sample_id, report_group_id, ref_id, ref_name, ref_desc, ref_path, usage ->
                                                                                   ^^^^^^^^
  ```

- Warning: `subworkflows/local/core_genome_phylogeny/main.nf:40:21`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          .map {[[id: it.getSimpleName()], it]}
                      ^^
  ```

- Warning: `subworkflows/local/core_genome_phylogeny/main.nf:40:42`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          .map {[[id: it.getSimpleName()], it]}
                                           ^^
  ```

- Warning: `subworkflows/local/core_genome_phylogeny/main.nf:53:21`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          .map{ [[id: it.report_group_ids], it.ref_metas] }
                      ^^
  ```

- Warning: `subworkflows/local/core_genome_phylogeny/main.nf:53:43`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          .map{ [[id: it.report_group_ids], it.ref_metas] }
                                            ^^
  ```

- Warning: `subworkflows/local/core_genome_phylogeny/main.nf:63:17`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          .map { [it[0], it[1].replace('\n', '')] } // remove newline that splitText adds
                  ^^
  ```

- Warning: `subworkflows/local/core_genome_phylogeny/main.nf:63:24`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          .map { [it[0], it[1].replace('\n', '')] } // remove newline that splitText adds
                         ^^
  ```

- Warning: `subworkflows/local/core_genome_phylogeny/main.nf:72:19`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          .branch { ref_meta, report_meta, ref_path, gff_path ->
                    ^^^^^^^^
  ```

- Warning: `subworkflows/local/core_genome_phylogeny/main.nf:72:29`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          .branch { ref_meta, report_meta, ref_path, gff_path ->
                              ^^^^^^^^^^^
  ```

- Warning: `subworkflows/local/core_genome_phylogeny/main.nf:72:42`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          .branch { ref_meta, report_meta, ref_path, gff_path ->
                                           ^^^^^^^^
  ```

- Warning: `subworkflows/local/core_genome_phylogeny/main.nf:81:28`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
              bakta_db_tar = Channel.fromPath(params.bakta_db).map{ [ [id: 'baktadb'], it] }
                             ^^^^^^^
  ```

- Warning: `subworkflows/local/core_genome_phylogeny/main.nf:81:86`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
              bakta_db_tar = Channel.fromPath(params.bakta_db).map{ [ [id: 'baktadb'], it] }
                                                                                       ^^
  ```

- Warning: `subworkflows/local/core_genome_phylogeny/main.nf:83:45`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
              bakta_db = UNTAR.out.untar.map{ meta, db -> db }.first()
                                              ^^^^
  ```

- Warning: `subworkflows/local/core_genome_phylogeny/main.nf:86:24`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
              bakta_db = Channel.fromPath(params.bakta_db).first()
                         ^^^^^^^
  ```

- Warning: `subworkflows/local/core_genome_phylogeny/main.nf:96:21`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          .map{ [[id: it.sample_id], [id: it.report_group_ids]] }
                      ^^
  ```

- Warning: `subworkflows/local/core_genome_phylogeny/main.nf:96:41`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          .map{ [[id: it.sample_id], [id: it.report_group_ids]] }
                                          ^^
  ```

- Warning: `subworkflows/local/core_genome_phylogeny/main.nf:99:49`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          .map { ref_meta, report_meta, ref_path, gff_path ->
                                                  ^^^^^^^^
  ```

- Warning: `subworkflows/local/core_genome_phylogeny/main.nf:106:30`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
              .map { ref_meta, report_meta, assem_path ->
                               ^^^^^^^^^^^
  ```

- Warning: `subworkflows/local/core_genome_phylogeny/main.nf:119:29`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
              .map{ ref_meta, report_meta, ref_path, ref_gff ->
                              ^^^^^^^^^^^
  ```

- Warning: `subworkflows/local/core_genome_phylogeny/main.nf:128:49`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          .map { sample_or_ref_meta, report_meta, assem_path, gff_path ->
                                                  ^^^^^^^^^^
  ```

- Warning: `subworkflows/local/core_genome_phylogeny/main.nf:133:38`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          .map{ ref_meta, report_meta, ref_path, ref_gff, ref_combined ->
                                       ^^^^^^^^
  ```

- Warning: `subworkflows/local/core_genome_phylogeny/main.nf:133:48`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          .map{ ref_meta, report_meta, ref_path, ref_gff, ref_combined ->
                                                 ^^^^^^^
  ```

- Warning: `subworkflows/local/core_genome_phylogeny/main.nf:138:16`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          .map { sample_or_ref_meta, report_meta, gff ->
                 ^^^^^^^^^^^^^^^^^^
  ```

- Warning: `subworkflows/local/core_genome_phylogeny/main.nf:150:19`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          .filter { it[1].any{ it.endsWith("PIRATE.gene_families.ordered.tsv") } }
                    ^^
  ```

- Warning: `subworkflows/local/core_genome_phylogeny/main.nf:150:30`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          .filter { it[1].any{ it.endsWith("PIRATE.gene_families.ordered.tsv") } }
                               ^^
  ```

- Warning: `subworkflows/local/core_genome_phylogeny/main.nf:152:21`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          .filter { ! it[1].any{ it.endsWith("PIRATE.gene_families.ordered.tsv") } }
                      ^^
  ```

- Warning: `subworkflows/local/core_genome_phylogeny/main.nf:152:32`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          .filter { ! it[1].any{ it.endsWith("PIRATE.gene_families.ordered.tsv") } }
                                 ^^
  ```

- Warning: `subworkflows/local/core_genome_phylogeny/main.nf:153:23`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          .map { [null, it[0], null, "CORE_GENOME_PHYLOGENY", "WARNING", "Pirate failed to find a core genome, possibly becuase samples are very different or there are too few reads."] } // meta, group_meta, ref_meta, workflow, level, message
                        ^^
  ```

- Warning: `subworkflows/local/core_genome_phylogeny/main.nf:182:20`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
              .map { file_name, message_data -> [
                     ^^^^^^^^^
  ```

- Warning: `subworkflows/local/core_genome_phylogeny/main.nf:214:17`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          .map { [it[0].group_id, it[1]] } // group_meta, tree
                  ^^
  ```

- Warning: `subworkflows/local/core_genome_phylogeny/main.nf:214:33`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          .map { [it[0].group_id, it[1]] } // group_meta, tree
                                  ^^
  ```

- Warning: `subworkflows/local/core_genome_phylogeny/main.nf:219:17`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          .map { [it[1], null] }
                  ^^
  ```

- Warning: `subworkflows/local/core_genome_phylogeny/main.nf:222:17`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          .map { [it[1], null] }
                  ^^
  ```

- Warning: `subworkflows/local/genome_assembly/main.nf:15:16`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      versions = Channel.empty()
                 ^^^^^^^
  ```

- Warning: `subworkflows/local/genome_assembly/main.nf:16:16`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      messages = Channel.empty()
                 ^^^^^^^
  ```

- Warning: `subworkflows/local/genome_assembly/main.nf:18:21`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          .map{ [[id: it.sample_id, single_end: it.single_end, domain: it.domain, type: it.sequence_type], [id: it.report_group_ids], it.paths] }
                      ^^
  ```

- Warning: `subworkflows/local/genome_assembly/main.nf:18:47`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          .map{ [[id: it.sample_id, single_end: it.single_end, domain: it.domain, type: it.sequence_type], [id: it.report_group_ids], it.paths] }
                                                ^^
  ```

- Warning: `subworkflows/local/genome_assembly/main.nf:18:70`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          .map{ [[id: it.sample_id, single_end: it.single_end, domain: it.domain, type: it.sequence_type], [id: it.report_group_ids], it.paths] }
                                                                       ^^
  ```

- Warning: `subworkflows/local/genome_assembly/main.nf:18:87`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          .map{ [[id: it.sample_id, single_end: it.single_end, domain: it.domain, type: it.sequence_type], [id: it.report_group_ids], it.paths] }
                                                                                        ^^
  ```

- Warning: `subworkflows/local/genome_assembly/main.nf:18:111`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          .map{ [[id: it.sample_id, single_end: it.single_end, domain: it.domain, type: it.sequence_type], [id: it.report_group_ids], it.paths] }
                                                                                                                ^^
  ```

- Warning: `subworkflows/local/genome_assembly/main.nf:18:133`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          .map{ [[id: it.sample_id, single_end: it.single_end, domain: it.domain, type: it.sequence_type], [id: it.report_group_ids], it.paths] }
                                                                                                                                      ^^
  ```

- Warning: `subworkflows/local/genome_assembly/main.nf:20:28`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          .map{ sample_meta, report_meta, read_paths -> [sample_meta, read_paths]}
                             ^^^^^^^^^^^
  ```

- Warning: `subworkflows/local/genome_assembly/main.nf:22:25`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          .branch { meta, paths->
                          ^^^^^
  ```

- Warning: `subworkflows/local/genome_assembly/main.nf:37:86`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
              [sample_meta, read_paths.size() <= 2 ? read_paths : read_paths.findAll { it ==~ /.+_[12]\..+$/ }]
                                                                                       ^^
  ```

- Warning: `subworkflows/local/genome_assembly/main.nf:45:18`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          .filter{ sample_meta, json ->
                   ^^^^^^^^^^^
  ```

- Warning: `subworkflows/local/genome_assembly/main.nf:59:29`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          .map { sample_meta, read_paths1, base_count, report_meta, read_paths2 ->
                              ^^^^^^^^^^^
  ```

- Warning: `subworkflows/local/genome_assembly/main.nf:59:67`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          .map { sample_meta, read_paths1, base_count, report_meta, read_paths2 ->
                                                                    ^^^^^^^^^^^
  ```

- Warning: `subworkflows/local/genome_assembly/main.nf:74:19`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          .filter { sample_meta, read_paths, scaffolds ->
                    ^^^^^^^^^^^
  ```

- Warning: `subworkflows/local/genome_assembly/main.nf:74:32`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          .filter { sample_meta, read_paths, scaffolds ->
                                 ^^^^^^^^^^
  ```

- Warning: `subworkflows/local/genome_assembly/main.nf:78:29`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          .map { sample_meta, read_paths, scaffolds, report_meta, read_paths2 ->
                              ^^^^^^^^^^
  ```

- Warning: `subworkflows/local/genome_assembly/main.nf:78:41`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          .map { sample_meta, read_paths, scaffolds, report_meta, read_paths2 ->
                                          ^^^^^^^^^
  ```

- Warning: `subworkflows/local/genome_assembly/main.nf:78:65`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          .map { sample_meta, read_paths, scaffolds, report_meta, read_paths2 ->
                                                                  ^^^^^^^^^^^
  ```

- Warning: `subworkflows/local/genome_assembly/main.nf:109:22`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          .map { [[id: it.sample_id], it] }
                       ^^
  ```

- Warning: `subworkflows/local/genome_assembly/main.nf:109:37`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          .map { [[id: it.sample_id], it] }
                                      ^^
  ```

- Warning: `subworkflows/local/genome_assembly/main.nf:111:41`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          .map{ sample_meta, sample_data, paths ->
                                          ^^^^^
  ```

- Warning: `subworkflows/local/initial_qc_checks/main.nf:10:16`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      versions = Channel.empty()
                 ^^^^^^^
  ```

- Warning: `subworkflows/local/initial_qc_checks/main.nf:11:16`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      messages = Channel.empty()
                 ^^^^^^^
  ```

- Warning: `subworkflows/local/initial_qc_checks/main.nf:15:19`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          .filter { it.sequence_type == "illumina" || it.sequence_type == "bgiseq" }
                    ^^
  ```

- Warning: `subworkflows/local/initial_qc_checks/main.nf:15:53`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          .filter { it.sequence_type == "illumina" || it.sequence_type == "bgiseq" }
                                                      ^^
  ```

- Warning: `subworkflows/local/initial_qc_checks/main.nf:16:22`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          .map { [[id: it.sample_id], it.paths] }
                       ^^
  ```

- Warning: `subworkflows/local/initial_qc_checks/main.nf:16:37`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          .map { [[id: it.sample_id], it.paths] }
                                      ^^
  ```

- Warning: `subworkflows/local/initial_qc_checks/main.nf:23:19`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          .filter { it.sequence_type == "nanopore" || it.sequence_type == "pacbio" }
                    ^^
  ```

- Warning: `subworkflows/local/initial_qc_checks/main.nf:23:53`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          .filter { it.sequence_type == "nanopore" || it.sequence_type == "pacbio" }
                                                      ^^
  ```

- Warning: `subworkflows/local/initial_qc_checks/main.nf:24:22`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          .map { [[id: it.sample_id], it.paths] }
                       ^^
  ```

- Warning: `subworkflows/local/initial_qc_checks/main.nf:24:37`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          .map { [[id: it.sample_id], it.paths] }
                                      ^^
  ```

- Warning: `subworkflows/local/prepare_input/main.nf:23:16`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      versions = Channel.empty()
                 ^^^^^^^
  ```

- Warning: `subworkflows/local/prepare_input/main.nf:24:16`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      messages = Channel.empty()
                 ^^^^^^^
  ```

- Warning: `subworkflows/local/prepare_input/main.nf:31:47`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          .map { create_sample_metadata_channel(it) }
                                                ^^
  ```

- Warning: `subworkflows/local/prepare_input/main.nf:35:50`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          .map { create_reference_metadata_channel(it) }
                                                   ^^
  ```

- Warning: `subworkflows/local/prepare_input/main.nf:41:17`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
                  it.sample_id == '' ? null : [id: it.sample_id],
                  ^^
  ```

- Warning: `subworkflows/local/prepare_input/main.nf:41:50`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
                  it.sample_id == '' ? null : [id: it.sample_id],
                                                   ^^
  ```

- Warning: `subworkflows/local/prepare_input/main.nf:42:17`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
                  it.report_group_id == '' ? null : [id: it.report_group_id],
                  ^^
  ```

- Warning: `subworkflows/local/prepare_input/main.nf:42:56`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
                  it.report_group_id == '' ? null : [id: it.report_group_id],
                                                         ^^
  ```

- Warning: `subworkflows/local/prepare_input/main.nf:43:17`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
                  it.reference_id == '' ? null : [id: it.reference_id],
                  ^^
  ```

- Warning: `subworkflows/local/prepare_input/main.nf:43:53`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
                  it.reference_id == '' ? null : [id: it.reference_id],
                                                      ^^
  ```

- Warning: `subworkflows/local/prepare_input/main.nf:45:17`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
                  it.message_type,
                  ^^
  ```

- Warning: `subworkflows/local/prepare_input/main.nf:46:17`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
                  it.description
                  ^^
  ```

- Warning: `subworkflows/local/prepare_input/main.nf:56:27`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          .filter{ ref_ids, sample_meta -> ref_ids.size() > 0 }
                            ^^^^^^^^^^^
  ```

- Warning: `subworkflows/local/prepare_input/main.nf:59:16`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          .map { ref_id, sample_meta, ref_meta -> [sample_meta, ref_meta] }
                 ^^^^^^
  ```

- Warning: `subworkflows/local/prepare_input/main.nf:65:31`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          .filter{ sample_meta, ref_metas -> sample_meta.ncbi_accession}
                                ^^^^^^^^^
  ```

- Warning: `subworkflows/local/prepare_input/main.nf:67:31`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          .filter{ sample_meta, ref_metas -> ! sample_meta.ncbi_accession }
                                ^^^^^^^^^
  ```

- Warning: `subworkflows/local/prepare_input/main.nf:72:31`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          .map { ncbi_acc_meta, sample_meta, ref_metas ->
                                ^^^^^^^^^^^
  ```

- Warning: `subworkflows/local/prepare_input/main.nf:72:44`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          .map { ncbi_acc_meta, sample_meta, ref_metas ->
                                             ^^^^^^^^^
  ```

- Warning: `subworkflows/local/prepare_input/main.nf:80:16`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          .map { ncbi_acc_meta, reads_path, sample_meta, ref_metas ->
                 ^^^^^^^^^^^^^
  ```

- Warning: `subworkflows/local/prepare_input/main.nf:85:60`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
                      sample_meta.paths = reads_path.findAll{it ==~ /^.+_[12]\..+$/}
                                                             ^^
  ```

- Warning: `subworkflows/local/prepare_input/main.nf:98:33`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
              .map { sample_meta, ref_metas ->
                                  ^^^^^^^^^
  ```

- Warning: `subworkflows/local/prepare_input/main.nf:122:15`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          .map{ sample_id, sample_meta, ref_metas, depth, domain ->
                ^^^^^^^^^
  ```

- Warning: `subworkflows/local/prepare_input/main.nf:131:18`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          .filter{ sample_meta, taxon_data ->
                   ^^^^^^^^^^^
  ```

- Warning: `subworkflows/local/prepare_input/main.nf:139:19`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          .filter { sample_meta, ref_metas -> // Dont lookup assembly metadata if no references are to be dowloaded automatically (besides user-defined references)
                    ^^^^^^^^^^^
  ```

- Warning: `subworkflows/local/prepare_input/main.nf:139:32`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          .filter { sample_meta, ref_metas -> // Dont lookup assembly metadata if no references are to be dowloaded automatically (besides user-defined references)
                                 ^^^^^^^^^
  ```

- Warning: `subworkflows/local/prepare_input/main.nf:142:19`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          .filter { sample_meta, ref_metas -> // Dont lookup assembly metadata for samples that the user has defined exclusive references for
                    ^^^^^^^^^^^
  ```

- Warning: `subworkflows/local/prepare_input/main.nf:143:34`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
              ! (ref_metas.collect{it.ref_primary_usage}.contains('exclusive') &&
                                   ^^
  ```

- Warning: `subworkflows/local/prepare_input/main.nf:144:36`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
                  (ref_metas.collect{it.ref_contextual_usage}.contains('exclusive') || no_auto_contextual_refs))
                                     ^^
  ```

- Warning: `subworkflows/local/prepare_input/main.nf:146:29`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          .map { sample_meta, ref_metas ->
                              ^^^^^^^^^
  ```

- Warning: `subworkflows/local/prepare_input/main.nf:150:15`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          .map{ sample_id, sample_meta, family_ids -> [family_ids] }
                ^^^^^^^^^
  ```

- Warning: `subworkflows/local/prepare_input/main.nf:150:26`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          .map{ sample_id, sample_meta, family_ids -> [family_ids] }
                           ^^^^^^^^^^^
  ```

- Warning: `subworkflows/local/prepare_input/main.nf:168:16`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          .map { sample_meta, family_ids ->
                 ^^^^^^^^^^^
  ```

- Warning: `subworkflows/local/prepare_input/main.nf:173:19`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          .filter { it != [null, null] }
                    ^^
  ```

- Warning: `subworkflows/local/prepare_input/main.nf:179:16`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          .map { family_id, sample_id, stats_path -> [sample_id, stats_path] }
                 ^^^^^^^^^
  ```

- Warning: `subworkflows/local/prepare_input/main.nf:183:46`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
              [sample_id, family_stats.findAll{it != null}]
                                               ^^
  ```

- Warning: `subworkflows/local/prepare_input/main.nf:186:29`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          .map { sample_meta, ref_metas -> [[id: sample_meta.sample_id]] }
                              ^^^^^^^^^
  ```

- Warning: `subworkflows/local/prepare_input/main.nf:190:19`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          .filter { sample_meta, taxa_found, family_stats ->
                    ^^^^^^^^^^^
  ```

- Warning: `subworkflows/local/prepare_input/main.nf:190:32`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          .filter { sample_meta, taxa_found, family_stats ->
                                 ^^^^^^^^^^
  ```

- Warning: `subworkflows/local/prepare_input/main.nf:204:29`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          .map { sample_meta, ref_metas -> [[id: sample_meta.sample_id]] }
                              ^^^^^^^^^
  ```

- Warning: `subworkflows/local/prepare_input/main.nf:207:19`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          .filter { it != [null, null] } // above join adds [null, null] if channel is empty
                    ^^
  ```

- Warning: `subworkflows/local/prepare_input/main.nf:216:29`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          .map { sample_meta, ref_metas -> [[id: sample_meta.sample_id]] }
                              ^^^^^^^^^
  ```

- Warning: `subworkflows/local/prepare_input/main.nf:219:19`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          .filter { it != [null, null] } // above join adds [null, null] if channel is empty
                    ^^
  ```

- Warning: `subworkflows/local/prepare_input/main.nf:230:27`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          .map { sample_id, sample_meta, ref_metas_user, ref_metas_to_download ->
                            ^^^^^^^^^^^
  ```

- Warning: `subworkflows/local/prepare_input/main.nf:233:48`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          .combine(sample_data.map{ sample_meta, ref_metas -> [[id: sample_meta.sample_id], sample_meta] }, by: 0)
                                                 ^^^^^^^^^
  ```

- Warning: `subworkflows/local/prepare_input/main.nf:234:16`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          .map { sample_id, ref_metas, sample_meta ->
                 ^^^^^^^^^
  ```

- Warning: `subworkflows/local/prepare_input/main.nf:240:15`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          .map{ sample_id, ref_meta -> ref_meta }
                ^^^^^^^^^
  ```

- Warning: `subworkflows/local/prepare_input/main.nf:245:19`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          .filter { sample_id, line_count ->
                    ^^^^^^^^^
  ```

- Warning: `subworkflows/local/prepare_input/main.nf:249:16`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          .map { sample_id, line_count, sample_meta, ref_metas ->
                 ^^^^^^^^^
  ```

- Warning: `subworkflows/local/prepare_input/main.nf:249:27`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          .map { sample_id, line_count, sample_meta, ref_metas ->
                            ^^^^^^^^^^
  ```

- Warning: `subworkflows/local/prepare_input/main.nf:253:28`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          .map{ sample_meta, ref_metas ->
                             ^^^^^^^^^
  ```

- Warning: `subworkflows/local/prepare_input/main.nf:261:15`: Variable was declared but not used

  ```nextflow
          .tap{ ref_data_with_ncbi_acc }
                ^^^^^^^^^^^^^^^^^^^^^^
  ```

- Warning: `subworkflows/local/prepare_input/main.nf:270:18`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          .filter{ sample_meta, ref_meta ->
                   ^^^^^^^^^^^
  ```

- Warning: `subworkflows/local/prepare_input/main.nf:281:16`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          .map { ncbi_acc_meta, sample_meta, ref_meta, ref_path, gff_path ->
                 ^^^^^^^^^^^^^
  ```

- Warning: `subworkflows/local/prepare_input/main.nf:306:22`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          .map { [[id: it.sample_id], it.paths, it.sendsketch_depth] }
                       ^^
  ```

- Warning: `subworkflows/local/prepare_input/main.nf:306:37`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          .map { [[id: it.sample_id], it.paths, it.sendsketch_depth] }
                                      ^^
  ```

- Warning: `subworkflows/local/prepare_input/main.nf:306:47`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          .map { [[id: it.sample_id], it.paths, it.sendsketch_depth] }
                                                ^^
  ```

- Warning: `subworkflows/local/prepare_input/main.nf:308:19`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          .filter { sample_id, fastq_paths, depth ->
                    ^^^^^^^^^
  ```

- Warning: `subworkflows/local/prepare_input/main.nf:308:30`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          .filter { sample_id, fastq_paths, depth ->
                               ^^^^^^^^^^^
  ```

- Warning: `subworkflows/local/prepare_input/main.nf:313:13`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
              it.sendsketch_depth.toFloat() <= params.max_depth.toFloat()
              ^^
  ```

- Warning: `subworkflows/local/prepare_input/main.nf:317:46`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
              .map { sample_meta, fastq_paths, depth ->
                                               ^^^^^
  ```

- Warning: `subworkflows/local/prepare_input/main.nf:343:16`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          .map { sample_id, sample_meta, subset_reads ->
                 ^^^^^^^^^
  ```

- Warning: `subworkflows/local/reference_index/main.nf:32:19`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      ch_versions = Channel.empty()
                    ^^^^^^^
  ```

- Warning: `subworkflows/local/sketch_comparison/main.nf:14:16`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      versions = Channel.empty()
                 ^^^^^^^
  ```

- Warning: `subworkflows/local/sketch_comparison/main.nf:15:16`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      messages = Channel.empty()
                 ^^^^^^^
  ```

- Warning: `subworkflows/local/sketch_comparison/main.nf:19:22`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          .map { [[id: it.sample_id], it.paths] }
                       ^^
  ```

- Warning: `subworkflows/local/sketch_comparison/main.nf:19:37`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          .map { [[id: it.sample_id], it.paths] }
                                      ^^
  ```

- Warning: `subworkflows/local/sketch_comparison/main.nf:38:16`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          .map{ [it.ref_metas] }
                 ^^
  ```

- Warning: `subworkflows/local/sketch_comparison/main.nf:50:22`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          .map { [[id: it.sample_id], [id: it.report_group_ids]] }
                       ^^
  ```

- Warning: `subworkflows/local/sketch_comparison/main.nf:50:42`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          .map { [[id: it.sample_id], [id: it.report_group_ids]] }
                                           ^^
  ```

- Warning: `subworkflows/local/sketch_comparison/main.nf:52:16`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          .map { sample_id, report_group_id, signature -> [report_group_id, signature]}
                 ^^^^^^^^^
  ```

- Warning: `subworkflows/local/sketch_comparison/main.nf:55:16`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          .map{ [it.ref_metas, [id: it.report_group_ids]] }
                 ^^
  ```

- Warning: `subworkflows/local/sketch_comparison/main.nf:55:35`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          .map{ [it.ref_metas, [id: it.report_group_ids]] }
                                    ^^
  ```

- Warning: `subworkflows/local/sketch_comparison/main.nf:59:15`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          .map{ ref_id, report_group_id, signature -> [report_group_id, signature]}
                ^^^^^^
  ```

- Warning: `subworkflows/local/sketch_comparison/main.nf:62:22`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          .map { [[id: it.sample_id], [id: it.report_group_ids]] }
                       ^^
  ```

- Warning: `subworkflows/local/sketch_comparison/main.nf:62:42`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          .map { [[id: it.sample_id], [id: it.report_group_ids]] }
                                           ^^
  ```

- Warning: `subworkflows/local/sketch_comparison/main.nf:64:15`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          .map{ sample_id, report_group_id, signature -> [report_group_id, signature]}
                ^^^^^^^^^
  ```

- Warning: `subworkflows/local/utils_nfcore_pathogensurveillance_pipeline/main.nf:32:5`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
      monochrome_logs   // boolean: Do not use coloured log outputs
      ^^^^^^^^^^^^^^^
  ```

- Warning: `subworkflows/local/utils_nfcore_pathogensurveillance_pipeline/main.nf:35:5`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
      input             //  string: Path to input samplesheet
      ^^^^^
  ```

- Warning: `subworkflows/local/utils_nfcore_pathogensurveillance_pipeline/main.nf:42:5`: Variable was declared but not used

  ```nextflow
      ch_versions = channel.empty()
      ^^^^^^^^^^^
  ```

- Warning: `subworkflows/local/variant_analysis/main.nf:16:16`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      versions = Channel.empty()
                 ^^^^^^^
  ```

- Warning: `subworkflows/local/variant_analysis/main.nf:17:16`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      messages = Channel.empty()
                 ^^^^^^^
  ```

- Warning: `subworkflows/local/variant_analysis/main.nf:21:20`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          .map{[[id: it.report_group_ids], it]}
                     ^^
  ```

- Warning: `subworkflows/local/variant_analysis/main.nf:21:42`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          .map{[[id: it.report_group_ids], it]}
                                           ^^
  ```

- Warning: `subworkflows/local/variant_analysis/main.nf:24:18`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          .filter{ it[1].size() > 1 }
                   ^^
  ```

- Warning: `subworkflows/local/variant_analysis/main.nf:26:15`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          .map{ it[1] }
                ^^
  ```

- Warning: `subworkflows/local/variant_analysis/main.nf:29:22`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
              .filter{ it[1].size() == 1 }
                       ^^
  ```

- Warning: `subworkflows/local/variant_analysis/main.nf:37:16`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          .map{ [it.sample_id, it.report_group_ids, it.ref_metas] }
                 ^^
  ```

- Warning: `subworkflows/local/variant_analysis/main.nf:37:30`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          .map{ [it.sample_id, it.report_group_ids, it.ref_metas] }
                               ^^
  ```

- Warning: `subworkflows/local/variant_analysis/main.nf:37:51`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          .map{ [it.sample_id, it.report_group_ids, it.ref_metas] }
                                                    ^^
  ```

- Warning: `subworkflows/local/variant_analysis/main.nf:44:82`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          .collectFile() { sample_id, report_group_id, ref_id, ref_name, ref_desc, ref_path, usage ->
                                                                                   ^^^^^^^^
  ```

- Warning: `subworkflows/local/variant_analysis/main.nf:47:21`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          .map {[[id: it.getSimpleName()], it]}
                      ^^
  ```

- Warning: `subworkflows/local/variant_analysis/main.nf:47:42`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          .map {[[id: it.getSimpleName()], it]}
                                           ^^
  ```

- Warning: `subworkflows/local/variant_analysis/main.nf:56:51`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          .map {sample_id, report_group_id, ref_id, ref_name, ref_desc, ref_path, usage ->
                                                    ^^^^^^^^
  ```

- Warning: `subworkflows/local/variant_analysis/main.nf:56:61`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          .map {sample_id, report_group_id, ref_id, ref_name, ref_desc, ref_path, usage ->
                                                              ^^^^^^^^
  ```

- Warning: `subworkflows/local/variant_analysis/main.nf:62:17`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          .map { [it[0], it[1].replace('\n', '')] } // remove newline that splitText adds
                  ^^
  ```

- Warning: `subworkflows/local/variant_analysis/main.nf:62:24`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          .map { [it[0], it[1].replace('\n', '')] } // remove newline that splitText adds
                         ^^
  ```

- Warning: `subworkflows/local/variant_analysis/main.nf:68:38`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          .join(sample_data.map{ [[id: it.sample_id], [id: it.report_group_ids], it.paths, it.sequence_type, it.ploidy] }, by: 0..1)
                                       ^^
  ```

- Warning: `subworkflows/local/variant_analysis/main.nf:68:58`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          .join(sample_data.map{ [[id: it.sample_id], [id: it.report_group_ids], it.paths, it.sequence_type, it.ploidy] }, by: 0..1)
                                                           ^^
  ```

- Warning: `subworkflows/local/variant_analysis/main.nf:68:80`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          .join(sample_data.map{ [[id: it.sample_id], [id: it.report_group_ids], it.paths, it.sequence_type, it.ploidy] }, by: 0..1)
                                                                                 ^^
  ```

- Warning: `subworkflows/local/variant_analysis/main.nf:68:90`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          .join(sample_data.map{ [[id: it.sample_id], [id: it.report_group_ids], it.paths, it.sequence_type, it.ploidy] }, by: 0..1)
                                                                                           ^^
  ```

- Warning: `subworkflows/local/variant_analysis/main.nf:68:108`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          .join(sample_data.map{ [[id: it.sample_id], [id: it.report_group_ids], it.paths, it.sequence_type, it.ploidy] }, by: 0..1)
                                                                                                             ^^
  ```

- Warning: `subworkflows/local/variant_analysis/main.nf:70:23`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
              filtered: it[2] != null
                        ^^
  ```

- Warning: `subworkflows/local/variant_analysis/main.nf:71:21`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
              no_ref: it[2] == null
                      ^^
  ```

- Warning: `subworkflows/local/variant_analysis/main.nf:81:18`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          .filter{ it[2].size() >= 2 }
                   ^^
  ```

- Warning: `subworkflows/local/variant_analysis/main.nf:83:15`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          .map{ it[2] }
                ^^
  ```

- Warning: `subworkflows/local/variant_analysis/main.nf:86:22`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
              .filter{ it[2].size() < 2 }
                       ^^
  ```

- Warning: `subworkflows/local/variant_analysis/main.nf:94:19`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          .filter { sample_meta, report_meta, ref_meta, ref_path, usage, read_paths, sequence_type, ploidy ->
                    ^^^^^^^^^^^
  ```

- Warning: `subworkflows/local/variant_analysis/main.nf:94:32`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          .filter { sample_meta, report_meta, ref_meta, ref_path, usage, read_paths, sequence_type, ploidy ->
                                 ^^^^^^^^^^^
  ```

- Warning: `subworkflows/local/variant_analysis/main.nf:94:45`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          .filter { sample_meta, report_meta, ref_meta, ref_path, usage, read_paths, sequence_type, ploidy ->
                                              ^^^^^^^^
  ```

- Warning: `subworkflows/local/variant_analysis/main.nf:94:55`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          .filter { sample_meta, report_meta, ref_meta, ref_path, usage, read_paths, sequence_type, ploidy ->
                                                        ^^^^^^^^
  ```

- Warning: `subworkflows/local/variant_analysis/main.nf:94:65`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          .filter { sample_meta, report_meta, ref_meta, ref_path, usage, read_paths, sequence_type, ploidy ->
                                                                  ^^^^^
  ```

- Warning: `subworkflows/local/variant_analysis/main.nf:94:72`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          .filter { sample_meta, report_meta, ref_meta, ref_path, usage, read_paths, sequence_type, ploidy ->
                                                                         ^^^^^^^^^^
  ```

- Warning: `subworkflows/local/variant_analysis/main.nf:94:99`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          .filter { sample_meta, report_meta, ref_meta, ref_path, usage, read_paths, sequence_type, ploidy ->
                                                                                                    ^^^^^^
  ```

- Warning: `subworkflows/local/variant_analysis/main.nf:98:38`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          longreads.map { sample_meta, report_meta, ref_meta, ref_path, usage, read_paths, sequence_type, ploidy ->
                                       ^^^^^^^^^^^
  ```

- Warning: `subworkflows/local/variant_analysis/main.nf:98:51`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          longreads.map { sample_meta, report_meta, ref_meta, ref_path, usage, read_paths, sequence_type, ploidy ->
                                                    ^^^^^^^^
  ```

- Warning: `subworkflows/local/variant_analysis/main.nf:98:61`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          longreads.map { sample_meta, report_meta, ref_meta, ref_path, usage, read_paths, sequence_type, ploidy ->
                                                              ^^^^^^^^
  ```

- Warning: `subworkflows/local/variant_analysis/main.nf:98:71`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          longreads.map { sample_meta, report_meta, ref_meta, ref_path, usage, read_paths, sequence_type, ploidy ->
                                                                        ^^^^^
  ```

- Warning: `subworkflows/local/variant_analysis/main.nf:98:90`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          longreads.map { sample_meta, report_meta, ref_meta, ref_path, usage, read_paths, sequence_type, ploidy ->
                                                                                           ^^^^^^^^^^^^^
  ```

- Warning: `subworkflows/local/variant_analysis/main.nf:98:105`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          longreads.map { sample_meta, report_meta, ref_meta, ref_path, usage, read_paths, sequence_type, ploidy ->
                                                                                                          ^^^^^^
  ```

- Warning: `subworkflows/local/variant_analysis/main.nf:106:84`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          .map { sample_meta, chopped_reads, report_meta, ref_meta, ref_path, usage, read_paths, sequence_type, ploidy ->
                                                                                     ^^^^^^^^^^
  ```

- Warning: `subworkflows/local/variant_analysis/main.nf:110:19`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          .filter { sample_meta, report_meta, ref_meta, ref_path, usage, read_paths, sequence_type, ploidy ->
                    ^^^^^^^^^^^
  ```

- Warning: `subworkflows/local/variant_analysis/main.nf:110:32`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          .filter { sample_meta, report_meta, ref_meta, ref_path, usage, read_paths, sequence_type, ploidy ->
                                 ^^^^^^^^^^^
  ```

- Warning: `subworkflows/local/variant_analysis/main.nf:110:45`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          .filter { sample_meta, report_meta, ref_meta, ref_path, usage, read_paths, sequence_type, ploidy ->
                                              ^^^^^^^^
  ```

- Warning: `subworkflows/local/variant_analysis/main.nf:110:55`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          .filter { sample_meta, report_meta, ref_meta, ref_path, usage, read_paths, sequence_type, ploidy ->
                                                        ^^^^^^^^
  ```

- Warning: `subworkflows/local/variant_analysis/main.nf:110:65`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          .filter { sample_meta, report_meta, ref_meta, ref_path, usage, read_paths, sequence_type, ploidy ->
                                                                  ^^^^^
  ```

- Warning: `subworkflows/local/variant_analysis/main.nf:110:72`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          .filter { sample_meta, report_meta, ref_meta, ref_path, usage, read_paths, sequence_type, ploidy ->
                                                                         ^^^^^^^^^^
  ```

- Warning: `subworkflows/local/variant_analysis/main.nf:110:99`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          .filter { sample_meta, report_meta, ref_meta, ref_path, usage, read_paths, sequence_type, ploidy ->
                                                                                                    ^^^^^^
  ```

- Warning: `subworkflows/local/variant_analysis/main.nf:118:41`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          .map{ sample_meta, report_meta, ref_meta, ref_path, usage, read_paths, sequence_type, ploidy ->
                                          ^^^^^^^^
  ```

- Warning: `subworkflows/local/variant_analysis/main.nf:118:51`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          .map{ sample_meta, report_meta, ref_meta, ref_path, usage, read_paths, sequence_type, ploidy ->
                                                    ^^^^^^^^
  ```

- Warning: `subworkflows/local/variant_analysis/main.nf:118:61`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          .map{ sample_meta, report_meta, ref_meta, ref_path, usage, read_paths, sequence_type, ploidy ->
                                                              ^^^^^
  ```

- Warning: `subworkflows/local/variant_analysis/main.nf:118:68`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          .map{ sample_meta, report_meta, ref_meta, ref_path, usage, read_paths, sequence_type, ploidy ->
                                                                     ^^^^^^^^^^
  ```

- Warning: `subworkflows/local/variant_analysis/main.nf:118:80`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          .map{ sample_meta, report_meta, ref_meta, ref_path, usage, read_paths, sequence_type, ploidy ->
                                                                                 ^^^^^^^^^^^^^
  ```

- Warning: `subworkflows/local/variant_analysis/main.nf:118:95`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          .map{ sample_meta, report_meta, ref_meta, ref_path, usage, read_paths, sequence_type, ploidy ->
                                                                                                ^^^^^^
  ```

- Warning: `subworkflows/local/variant_analysis/main.nf:126:19`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
              .map{ sample_meta, report_meta, ref_meta, ref_path, usage, read_paths, sequence_type, ploidy ->
                    ^^^^^^^^^^^
  ```

- Warning: `subworkflows/local/variant_analysis/main.nf:126:32`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
              .map{ sample_meta, report_meta, ref_meta, ref_path, usage, read_paths, sequence_type, ploidy ->
                                 ^^^^^^^^^^^
  ```

- Warning: `subworkflows/local/variant_analysis/main.nf:126:65`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
              .map{ sample_meta, report_meta, ref_meta, ref_path, usage, read_paths, sequence_type, ploidy ->
                                                                  ^^^^^
  ```

- Warning: `subworkflows/local/variant_analysis/main.nf:126:72`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
              .map{ sample_meta, report_meta, ref_meta, ref_path, usage, read_paths, sequence_type, ploidy ->
                                                                         ^^^^^^^^^^
  ```

- Warning: `subworkflows/local/variant_analysis/main.nf:126:84`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
              .map{ sample_meta, report_meta, ref_meta, ref_path, usage, read_paths, sequence_type, ploidy ->
                                                                                     ^^^^^^^^^^^^^
  ```

- Warning: `subworkflows/local/variant_analysis/main.nf:126:99`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
              .map{ sample_meta, report_meta, ref_meta, ref_path, usage, read_paths, sequence_type, ploidy ->
                                                                                                    ^^^^^^
  ```

- Warning: `subworkflows/local/variant_analysis/main.nf:134:61`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          .map{ sample_meta, report_meta, ref_meta, ref_path, usage, read_paths, sequence_type, ploidy ->
                                                              ^^^^^
  ```

- Warning: `subworkflows/local/variant_analysis/main.nf:134:80`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          .map{ sample_meta, report_meta, ref_meta, ref_path, usage, read_paths, sequence_type, ploidy ->
                                                                                 ^^^^^^^^^^^^^
  ```

- Warning: `subworkflows/local/variant_analysis/main.nf:134:95`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          .map{ sample_meta, report_meta, ref_meta, ref_path, usage, read_paths, sequence_type, ploidy ->
                                                                                                ^^^^^^
  ```

- Warning: `subworkflows/local/variant_analysis/main.nf:146:20`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
              .map { it[0..3] + it[5..6] }
                     ^^
  ```

- Warning: `subworkflows/local/variant_analysis/main.nf:146:31`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
              .map { it[0..3] + it[5..6] }
                                ^^
  ```

- Warning: `subworkflows/local/variant_analysis/main.nf:153:21`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
              .map { [it[0], it[2], it[1]] + it[3..5] + [it[7]] } // [val(meta), val(ref_meta), [file(fastq)], file(reference), val(report_meta), fai, picard]
                      ^^
  ```

- Warning: `subworkflows/local/variant_analysis/main.nf:153:28`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
              .map { [it[0], it[2], it[1]] + it[3..5] + [it[7]] } // [val(meta), val(ref_meta), [file(fastq)], file(reference), val(report_meta), fai, picard]
                             ^^
  ```

- Warning: `subworkflows/local/variant_analysis/main.nf:153:35`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
              .map { [it[0], it[2], it[1]] + it[3..5] + [it[7]] } // [val(meta), val(ref_meta), [file(fastq)], file(reference), val(report_meta), fai, picard]
                                    ^^
  ```

- Warning: `subworkflows/local/variant_analysis/main.nf:153:44`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
              .map { [it[0], it[2], it[1]] + it[3..5] + [it[7]] } // [val(meta), val(ref_meta), [file(fastq)], file(reference), val(report_meta), fai, picard]
                                             ^^
  ```

- Warning: `subworkflows/local/variant_analysis/main.nf:153:56`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
              .map { [it[0], it[2], it[1]] + it[3..5] + [it[7]] } // [val(meta), val(ref_meta), [file(fastq)], file(reference), val(report_meta), fai, picard]
                                                         ^^
  ```

- Warning: `subworkflows/local/variant_analysis/main.nf:156:21`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
              .map { [it[0], it[7], it[8], it[1]] + it[3..6] }
                      ^^
  ```

- Warning: `subworkflows/local/variant_analysis/main.nf:156:28`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
              .map { [it[0], it[7], it[8], it[1]] + it[3..6] }
                             ^^
  ```

- Warning: `subworkflows/local/variant_analysis/main.nf:156:35`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
              .map { [it[0], it[7], it[8], it[1]] + it[3..6] }
                                    ^^
  ```

- Warning: `subworkflows/local/variant_analysis/main.nf:156:42`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
              .map { [it[0], it[7], it[8], it[1]] + it[3..6] }
                                           ^^
  ```

- Warning: `subworkflows/local/variant_analysis/main.nf:156:51`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
              .map { [it[0], it[7], it[8], it[1]] + it[3..6] }
                                                    ^^
  ```

- Warning: `subworkflows/local/variant_analysis/main.nf:161:87`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          .collectFile(keepHeader: true, skip: 1) { sample_meta, report_meta, ref_meta, ref_path, usage, read_paths, sequence_type, ploidy ->
                                                                                        ^^^^^^^^
  ```

- Warning: `subworkflows/local/variant_analysis/main.nf:161:97`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          .collectFile(keepHeader: true, skip: 1) { sample_meta, report_meta, ref_meta, ref_path, usage, read_paths, sequence_type, ploidy ->
                                                                                                  ^^^^^
  ```

- Warning: `subworkflows/local/variant_analysis/main.nf:161:104`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          .collectFile(keepHeader: true, skip: 1) { sample_meta, report_meta, ref_meta, ref_path, usage, read_paths, sequence_type, ploidy ->
                                                                                                         ^^^^^^^^^^
  ```

- Warning: `subworkflows/local/variant_analysis/main.nf:161:116`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          .collectFile(keepHeader: true, skip: 1) { sample_meta, report_meta, ref_meta, ref_path, usage, read_paths, sequence_type, ploidy ->
                                                                                                                     ^^^^^^^^^^^^^
  ```

- Warning: `subworkflows/local/variant_analysis/main.nf:164:17`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          .map { [it.getSimpleName(), it] }
                  ^^
  ```

- Warning: `subworkflows/local/variant_analysis/main.nf:164:37`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          .map { [it.getSimpleName(), it] }
                                      ^^
  ```

- Warning: `subworkflows/local/variant_analysis/main.nf:165:61`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          .combine(CALL_VARIANTS.out.vcf.map { combined_meta, vcf -> [combined_meta.id, combined_meta]}, by: 0) // add on full combined metadata uing combined ID
                                                              ^^^
  ```

- Warning: `subworkflows/local/variant_analysis/main.nf:166:16`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          .map { combined_id, ploidy_data_path, combined_meta ->
                 ^^^^^^^^^^^
  ```

- Warning: `subworkflows/local/variant_analysis/main.nf:176:5`: Variable was declared but not used

  ```nextflow
      removed_samps = VCF_TO_SNP_ALIGN.out.removed_sample_ids
      ^^^^^^^^^^^^^
  ```

- Warning: `subworkflows/local/variant_analysis/main.nf:178:22`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          .map { [[id: it[1].replace('\n', '')], it[0].group, it[0].ref, "VARIANT_ANALYSIS", "WARNING", "Sample removed from SNP phylogeny due to too much missing data."] } // meta, group_meta, ref_meta, workflow, level, message
                       ^^
  ```

- Warning: `subworkflows/local/variant_analysis/main.nf:178:48`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          .map { [[id: it[1].replace('\n', '')], it[0].group, it[0].ref, "VARIANT_ANALYSIS", "WARNING", "Sample removed from SNP phylogeny due to too much missing data."] } // meta, group_meta, ref_meta, workflow, level, message
                                                 ^^
  ```

- Warning: `subworkflows/local/variant_analysis/main.nf:178:61`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          .map { [[id: it[1].replace('\n', '')], it[0].group, it[0].ref, "VARIANT_ANALYSIS", "WARNING", "Sample removed from SNP phylogeny due to too much missing data."] } // meta, group_meta, ref_meta, workflow, level, message
                                                              ^^
  ```

- Warning: `subworkflows/local/variant_analysis/main.nf:190:22`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          .map { meta, fasta -> [null, meta.group, meta.ref, "VARIANT_ANALYSIS", "WARNING", "Not enough samples to build a SNP tree."] }
                       ^^^^^
  ```

- Warning: `subworkflows/local/variant_analysis/main.nf:200:48`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
      phylogeny = IQTREE_SNP.out.phylogeny.map{ [it[0].group, it[0].ref, it[1]] } // report_meta, ref_meta, tree
                                                 ^^
  ```

- Warning: `subworkflows/local/variant_analysis/main.nf:200:61`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
      phylogeny = IQTREE_SNP.out.phylogeny.map{ [it[0].group, it[0].ref, it[1]] } // report_meta, ref_meta, tree
                                                              ^^
  ```

- Warning: `subworkflows/local/variant_analysis/main.nf:200:72`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
      phylogeny = IQTREE_SNP.out.phylogeny.map{ [it[0].group, it[0].ref, it[1]] } // report_meta, ref_meta, tree
                                                                         ^^
  ```

- Warning: `subworkflows/local/variant_analysis/main.nf:201:50`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
      snp_align = VCF_TO_SNP_ALIGN.out.fasta.map{ [it[0].group, it[0].ref, it[1]] }
                                                   ^^
  ```

- Warning: `subworkflows/local/variant_analysis/main.nf:201:63`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
      snp_align = VCF_TO_SNP_ALIGN.out.fasta.map{ [it[0].group, it[0].ref, it[1]] }
                                                                ^^
  ```

- Warning: `subworkflows/local/variant_analysis/main.nf:201:74`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
      snp_align = VCF_TO_SNP_ALIGN.out.fasta.map{ [it[0].group, it[0].ref, it[1]] }
                                                                           ^^
  ```

- Warning: `subworkflows/local/variant_analysis/main.nf:202:39`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
      vcf = CALL_VARIANTS.out.vcf.map{ [it[0].group, it[0].ref, it[1]] }
                                        ^^
  ```

- Warning: `subworkflows/local/variant_analysis/main.nf:202:52`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
      vcf = CALL_VARIANTS.out.vcf.map{ [it[0].group, it[0].ref, it[1]] }
                                                     ^^
  ```

- Warning: `subworkflows/local/variant_analysis/main.nf:202:63`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
      vcf = CALL_VARIANTS.out.vcf.map{ [it[0].group, it[0].ref, it[1]] }
                                                                ^^
  ```

- Warning: `subworkflows/local/variant_analysis/main.nf:207:16`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          .map{ [it[0].group, it[0].ref] + it[1..3] } // report_meta, ref_meta, vcf, align, tree
                 ^^
  ```

- Warning: `subworkflows/local/variant_analysis/main.nf:207:29`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          .map{ [it[0].group, it[0].ref] + it[1..3] } // report_meta, ref_meta, vcf, align, tree
                              ^^
  ```

- Warning: `subworkflows/local/variant_analysis/main.nf:207:42`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          .map{ [it[0].group, it[0].ref] + it[1..3] } // report_meta, ref_meta, vcf, align, tree
                                           ^^
  ```

- Warning: `workflows/pathogensurveillance.nf:41:16`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      versions = Channel.empty()
                 ^^^^^^^
  ```

- Warning: `workflows/pathogensurveillance.nf:42:16`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      messages = Channel.empty()
                 ^^^^^^^
  ```

- Warning: `workflows/pathogensurveillance.nf:96:26`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      def topic_versions = Channel.topic("versions")
                           ^^^^^^^
  ```

- Warning: `workflows/pathogensurveillance.nf:123:31`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      multiqc_config          = Channel.fromPath("$projectDir/assets/multiqc_config.yml", checkIfExists: true)
                                ^^^^^^^
  ```

- Warning: `workflows/pathogensurveillance.nf:124:55`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      multiqc_custom_config   = params.multiqc_config ? Channel.fromPath( params.multiqc_config, checkIfExists: true ) : Channel.empty()
                                                        ^^^^^^^
  ```

- Warning: `workflows/pathogensurveillance.nf:124:120`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      multiqc_custom_config   = params.multiqc_config ? Channel.fromPath( params.multiqc_config, checkIfExists: true ) : Channel.empty()
                                                                                                                         ^^^^^^^
  ```

- Warning: `workflows/pathogensurveillance.nf:125:55`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      multiqc_logo            = params.multiqc_logo   ? Channel.fromPath( params.multiqc_logo, checkIfExists: true ) : Channel.empty()
                                                        ^^^^^^^
  ```

- Warning: `workflows/pathogensurveillance.nf:125:118`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      multiqc_logo            = params.multiqc_logo   ? Channel.fromPath( params.multiqc_logo, checkIfExists: true ) : Channel.empty()
                                                                                                                       ^^^^^^^
  ```

- Warning: `workflows/pathogensurveillance.nf:129:5`: Variable was declared but not used

  ```nextflow
      methods_description     = channel.value(methodsDescriptionText(multiqc_custom_methods_description))
      ^^^^^^^^^^^^^^^^^^^
  ```

- Warning: `workflows/pathogensurveillance.nf:141:21`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          .map{ [[id: it.sample_id], [id: it.report_group_ids]] }
                      ^^
  ```

- Warning: `workflows/pathogensurveillance.nf:141:41`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          .map{ [[id: it.sample_id], [id: it.report_group_ids]] }
                                          ^^
  ```

- Warning: `workflows/pathogensurveillance.nf:143:15`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          .map{ sample_meta, report_meta, fastqc -> [report_meta, fastqc] }
                ^^^^^^^^^^^
  ```

- Warning: `workflows/pathogensurveillance.nf:147:21`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          .map{ [[id: it.sample_id], [id: it.report_group_ids]] }
                      ^^
  ```

- Warning: `workflows/pathogensurveillance.nf:147:41`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          .map{ [[id: it.sample_id], [id: it.report_group_ids]] }
                                          ^^
  ```

- Warning: `workflows/pathogensurveillance.nf:149:15`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          .map{ sample_meta, report_meta, fastp_json -> [report_meta, fastp_json] }
                ^^^^^^^^^^^
  ```

- Warning: `workflows/pathogensurveillance.nf:153:21`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          .map{ [[id: it.sample_id], [id: it.report_group_ids]] }
                      ^^
  ```

- Warning: `workflows/pathogensurveillance.nf:153:41`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          .map{ [[id: it.sample_id], [id: it.report_group_ids]] }
                                          ^^
  ```

- Warning: `workflows/pathogensurveillance.nf:155:15`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          .map{ sample_meta, report_meta, nanoplot_txt -> [report_meta, nanoplot_txt] }
                ^^^^^^^^^^^
  ```

- Warning: `workflows/pathogensurveillance.nf:159:21`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          .map{ [[id: it.sample_id], [id: it.report_group_ids]] }
                      ^^
  ```

- Warning: `workflows/pathogensurveillance.nf:159:41`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          .map{ [[id: it.sample_id], [id: it.report_group_ids]] }
                                          ^^
  ```

- Warning: `workflows/pathogensurveillance.nf:161:15`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          .map{ sample_meta, report_meta, quast -> [report_meta, quast] }
                ^^^^^^^^^^^
  ```

- Warning: `workflows/pathogensurveillance.nf:165:21`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          .map{ [[id: it.report_group_ids]] }
                      ^^
  ```

- Warning: `workflows/pathogensurveillance.nf:189:71`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
              [[id: sample_meta.report_group_ids], sample_meta.findAll {it.key != 'paths' && it.key != 'ref_metas' && it.key != 'ref_ids'}]
                                                                        ^^
  ```

- Warning: `workflows/pathogensurveillance.nf:189:92`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
              [[id: sample_meta.report_group_ids], sample_meta.findAll {it.key != 'paths' && it.key != 'ref_metas' && it.key != 'ref_ids'}]
                                                                                             ^^
  ```

- Warning: `workflows/pathogensurveillance.nf:189:117`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
              [[id: sample_meta.report_group_ids], sample_meta.findAll {it.key != 'paths' && it.key != 'ref_metas' && it.key != 'ref_ids'}]
                                                                                                                      ^^
  ```

- Warning: `workflows/pathogensurveillance.nf:193:87`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
              [ "${report_meta.id}_sample_data.tsv", sample_meta.keySet().collect{'"' + it + '"'}.join('\t') + "\n" + sample_meta.values().collect{'"' + (it ?: '') + '"'}.join('\t') + "\n" ]
                                                                                        ^^
  ```

- Warning: `workflows/pathogensurveillance.nf:193:153`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
              [ "${report_meta.id}_sample_data.tsv", sample_meta.keySet().collect{'"' + it + '"'}.join('\t') + "\n" + sample_meta.values().collect{'"' + (it ?: '') + '"'}.join('\t') + "\n" ]
                                                                                                                                                          ^^
  ```

- Warning: `workflows/pathogensurveillance.nf:195:21`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          .map {[[id: it.getSimpleName().replace('_sample_data', '')], it]}
                      ^^
  ```

- Warning: `workflows/pathogensurveillance.nf:195:70`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          .map {[[id: it.getSimpleName().replace('_sample_data', '')], it]}
                                                                       ^^
  ```

- Warning: `workflows/pathogensurveillance.nf:204:45`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
              [report_meta, ref_meta.findAll {it.key != 'ref_path' && it.key != 'gff'}]
                                              ^^
  ```

- Warning: `workflows/pathogensurveillance.nf:204:69`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
              [report_meta, ref_meta.findAll {it.key != 'ref_path' && it.key != 'gff'}]
                                                                      ^^
  ```

- Warning: `workflows/pathogensurveillance.nf:208:87`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
              [ "${report_meta.id}_reference_data.tsv", ref_meta.keySet().collect{'"' + it + '"'}.join('\t') + "\n" + ref_meta.values().collect{'"' + (it ?: '') + '"'}.join('\t') + "\n" ]
                                                                                        ^^
  ```

- Warning: `workflows/pathogensurveillance.nf:208:150`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
              [ "${report_meta.id}_reference_data.tsv", ref_meta.keySet().collect{'"' + it + '"'}.join('\t') + "\n" + ref_meta.values().collect{'"' + (it ?: '') + '"'}.join('\t') + "\n" ]
                                                                                                                                                       ^^
  ```

- Warning: `workflows/pathogensurveillance.nf:210:21`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          .map {[[id: it.getSimpleName().replace('_reference_data', '')], it]}
                      ^^
  ```

- Warning: `workflows/pathogensurveillance.nf:210:73`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          .map {[[id: it.getSimpleName().replace('_reference_data', '')], it]}
                                                                          ^^
  ```

- Warning: `workflows/pathogensurveillance.nf:214:21`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          .map{ [[id: it.sample_id], [id: it.report_group_ids]] }
                      ^^
  ```

- Warning: `workflows/pathogensurveillance.nf:214:41`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          .map{ [[id: it.sample_id], [id: it.report_group_ids]] }
                                          ^^
  ```

- Warning: `workflows/pathogensurveillance.nf:216:15`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          .map{ sample_meta, report_meta, sendsketch -> [report_meta, sendsketch] }
                ^^^^^^^^^^^
  ```

- Warning: `workflows/pathogensurveillance.nf:222:21`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          .map{ [[id: it.sample_id], [id: it.report_group_ids]] }
                      ^^
  ```

- Warning: `workflows/pathogensurveillance.nf:222:41`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          .map{ [[id: it.sample_id], [id: it.report_group_ids]] }
                                          ^^
  ```

- Warning: `workflows/pathogensurveillance.nf:225:16`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          .map { sample_meta, report_meta, family_stats ->
                 ^^^^^^^^^^^
  ```

- Warning: `workflows/pathogensurveillance.nf:231:21`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          .map{ [[id: it.sample_id], [id: it.report_group_ids]] }
                      ^^
  ```

- Warning: `workflows/pathogensurveillance.nf:231:41`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          .map{ [[id: it.sample_id], [id: it.report_group_ids]] }
                                          ^^
  ```

- Warning: `workflows/pathogensurveillance.nf:233:15`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          .map{ sample_meta, report_meta, ref_meta_file ->
                ^^^^^^^^^^^
  ```

- Warning: `workflows/pathogensurveillance.nf:238:50`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
              [report_meta, ref_meta_files.findAll{it != null}]
                                                   ^^
  ```

- Warning: `workflows/pathogensurveillance.nf:243:29`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          .map { report_meta, ref_meta, fasta -> [report_meta, fasta] }
                              ^^^^^^^^
  ```

- Warning: `workflows/pathogensurveillance.nf:248:29`: Parameter was not used -- prefix with `_` to suppress warning

  ```nextflow
          .map { report_meta, ref_meta, tree -> [report_meta, tree] }
                              ^^^^^^^^
  ```

- Warning: `workflows/pathogensurveillance.nf:257:21`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          .map {[[id: it.getSimpleName()], it]}
                      ^^
  ```

- Warning: `workflows/pathogensurveillance.nf:257:42`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          .map {[[id: it.getSimpleName()], it]}
                                           ^^
  ```

- Warning: `workflows/pathogensurveillance.nf:277:17`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          .filter{it[0] != null} // remove extra item if messages is empty
                  ^^
  ```

- Warning: `workflows/pathogensurveillance.nf:278:15`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          .map{ it.size() == 16 ? it + [null] : it } // adds placeholder if messages is empty
                ^^
  ```

- Warning: `workflows/pathogensurveillance.nf:278:33`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          .map{ it.size() == 16 ? it + [null] : it } // adds placeholder if messages is empty
                                  ^^
  ```

- Warning: `workflows/pathogensurveillance.nf:278:47`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          .map{ it.size() == 16 ? it + [null] : it } // adds placeholder if messages is empty
                                                ^^
  ```

- Warning: `workflows/pathogensurveillance.nf:279:18`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          .filter{ it.size() == 17 } // remove any malformed inputs
                   ^^
  ```

- Warning: `workflows/pathogensurveillance.nf:280:15`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          .map{ it.collect{ it ?: [] } } //replace nulls with empty lists
                ^^
  ```

- Warning: `workflows/pathogensurveillance.nf:280:27`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
          .map{ it.collect{ it ?: [] } } //replace nulls with empty lists
                            ^^
  ```

- Warning: `workflows/pathogensurveillance.nf:285:9`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
          Channel.fromPath("${projectDir}/assets/.pathogensurveillance_output.json", checkIfExists: true).first() // .first converts it to a value channel so it can be reused for multiple reports.
          ^^^^^^^
  ```

- Warning: `workflows/pathogensurveillance.nf:290:9`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
          Channel.fromPath("${projectDir}/assets/main_report", checkIfExists: true).first() // .first converts it to a value channel so it can be reused for multiple reports.
          ^^^^^^^
  ```

- Warning: `workflows/pathogensurveillance.nf:309:5`: The use of `Channel` to access channel factories is deprecated -- use `channel` instead

  ```nextflow
      Channel.value(
      ^^^^^^^
  ```

- Warning: `workflows/pathogensurveillance.nf:328:34`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
              sample_meta.findAll {it.key != 'paths' && it.key != 'ref_metas' && it.key != 'ref_ids'}
                                   ^^
  ```

- Warning: `workflows/pathogensurveillance.nf:328:55`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
              sample_meta.findAll {it.key != 'paths' && it.key != 'ref_metas' && it.key != 'ref_ids'}
                                                        ^^
  ```

- Warning: `workflows/pathogensurveillance.nf:328:80`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
              sample_meta.findAll {it.key != 'paths' && it.key != 'ref_metas' && it.key != 'ref_ids'}
                                                                                 ^^
  ```

- Warning: `workflows/pathogensurveillance.nf:337:48`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
              sample_meta.keySet().collect{'"' + it + '"'}.join('\t') + "\n" + sample_meta.values().collect{'"' + (it ?: '') + '"'}.join('\t') + "\n"
                                                 ^^
  ```

- Warning: `workflows/pathogensurveillance.nf:337:114`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
              sample_meta.keySet().collect{'"' + it + '"'}.join('\t') + "\n" + sample_meta.values().collect{'"' + (it ?: '') + '"'}.join('\t') + "\n"
                                                                                                                   ^^
  ```

- Warning: `workflows/pathogensurveillance.nf:347:34`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
              ref_meta[0].findAll {it.key != 'ref_path' && it.key != 'gff'}
                                   ^^
  ```

- Warning: `workflows/pathogensurveillance.nf:347:58`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
              ref_meta[0].findAll {it.key != 'ref_path' && it.key != 'gff'}
                                                           ^^
  ```

- Warning: `workflows/pathogensurveillance.nf:356:45`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
              ref_meta.keySet().collect{'"' + it + '"'}.join('\t') + "\n" + ref_meta.values().collect{'"' + (it ?: '') + '"'}.join('\t') + "\n"
                                              ^^
  ```

- Warning: `workflows/pathogensurveillance.nf:356:108`: Implicit closure parameter is deprecated, declare an explicit parameter instead

  ```nextflow
              ref_meta.keySet().collect{'"' + it + '"'}.join('\t') + "\n" + ref_meta.values().collect{'"' + (it ?: '') + '"'}.join('\t') + "\n"
                                                                                                             ^^
  ```
